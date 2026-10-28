#!/usr/bin/env python3
"""Translate phase README, quizzes and Markdown artifacts into i18n/<lang>.

The canonical English files stay on main. This companion to translate_lessons.py
is scoped by phase so CI can resume from a published per-phase hash cache.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import translate_lessons as lessons  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
CODE_LIKE = re.compile(r"^(?:python\d*\s+-|pip\s+|npm\s+|uv\s+|git\s+|npx\s+|sudo\s+|import\s+\w+[;.]|\w+\.\w+\()")


def translate_string(value: str, lang: str, provider: str) -> str:
    """Translate a single quiz field, retaining commands and technical spans."""
    if not value.strip() or CODE_LIKE.search(value) or re.search(r"\s--[a-z]", value):
        return value
    protected, spans = lessons.protect(value, lessons.NLLB_INLINE)
    if provider == "echo":
        translated = protected
    elif provider == "nllb":
        # The sentence model is not instructed to retain sentinels. Translate
        # only the prose between them, as the lesson Markdown walker does.
        pipe = lessons._nllb_pipe(lessons.NLLB_CODES[lang])
        translated = "".join(
            part if (lessons.SENT_RE.fullmatch(part) or not part.strip())
            else lessons._nllb_sentence(pipe, part)
            for part in re.split(r"(⁣PROTECT\d+⁣)", protected)
        )
    else:
        translated = lessons.translate_text(protected, lang, provider)
    # A dropped or mangled placeholder is worse than retaining the English.
    if any(protected.count(lessons.SENTINEL.format(i)) != translated.count(lessons.SENTINEL.format(i))
           for i in range(len(spans))):
        return value
    return lessons.restore(translated, spans)


def translate_quiz(source: str, lang: str, provider: str) -> str:
    data = json.loads(source)
    questions = data if isinstance(data, list) else data["questions"]
    if not isinstance(questions, list):
        raise ValueError("quiz questions must be a list")
    if isinstance(data, dict) and isinstance(data.get("title"), str):
        data["title"] = translate_string(data["title"], lang, provider)
    for item in questions:
        for key in ("question", "explanation"):
            if isinstance(item.get(key), str):
                item[key] = translate_string(item[key], lang, provider)
        if isinstance(item.get("options"), list):
            item["options"] = [translate_string(x, lang, provider) for x in item["options"]]
    return json.dumps(data, indent=2, ensure_ascii=False) + "\n"


def translate_markdown(source: str, lang: str, provider: str) -> str:
    # Preserve prompt/skill metadata and its machine-readable names.
    match = re.match(r"\A(---\n.*?\n---\n)([\s\S]*)\Z", source, re.S)
    header, body = match.groups() if match else ("", source)
    if header:
        header = re.sub(
            r"(?m)^(description:\s*)([^\n]+)$",
            lambda m: m.group(1) + translate_string(m.group(2), lang, provider),
            header,
        )
    if provider in {"echo", "nllb"}:
        translated = lessons.nllb_translate_doc(body, lessons.NLLB_CODES[lang],
                                                 translate_fn=(lambda s: s) if provider == "echo" else None)
    else:
        translated = lessons.translate_doc(body, lang, provider)
    if translated is None:
        return source
    return header + translated


def refresh_description(source: str, published: str, lang: str, provider: str) -> str:
    """Update old cache hits whose frontmatter description stayed English."""
    pattern = re.compile(r"(?m)^(description:\s*)([^\n]+)$")
    original = pattern.search(source)
    current = pattern.search(published)
    if not original or not current or original.group(2) != current.group(2):
        return published
    replacement = translate_string(original.group(2), lang, provider)
    return published[:current.start(2)] + replacement + published[current.end(2):]


def source_files(phase: Path):
    phase_readme = phase / "README.md"
    if phase_readme.is_file():
        yield phase_readme
    for lesson in sorted(phase.iterdir()):
        if not lesson.is_dir() or not lessons.LESSON_DIR_RE.match(lesson.name):
            continue
        quiz = lesson / "quiz.json"
        if quiz.is_file():
            yield quiz
        yield from sorted((lesson / "outputs").glob("*.md"))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lang", required=True, choices=sorted(lessons.LANG_NAMES))
    parser.add_argument("--phase", required=True)
    parser.add_argument("--provider", choices=("nllb", "openai", "anthropic", "deepl", "echo"), default="nllb")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if not lessons.PHASE_DIR_RE.match(args.phase):
        parser.error("invalid phase")
    phase = lessons.PHASES / args.phase
    if not phase.is_dir():
        parser.error("unknown phase")

    cache_file = lessons.OUT_ROOT / args.lang / ".extras-cache" / f"{args.phase}.json"
    cache = json.loads(cache_file.read_text(encoding="utf-8")) if cache_file.exists() else {}
    current = set()
    translated = skipped = 0
    for source_file in source_files(phase):
        rel = source_file.relative_to(ROOT).as_posix()
        current.add(rel)
        source = source_file.read_text(encoding="utf-8")
        digest = lessons.source_hash(source)
        dest = lessons.OUT_ROOT / args.lang / rel
        if cache.get(rel) == digest and dest.exists():
            if source_file.suffix == ".md" and source_file.name != "README.md" and not args.dry_run:
                published = dest.read_text(encoding="utf-8")
                updated = refresh_description(source, published, args.lang, args.provider)
                if updated != published:
                    dest.write_text(updated, encoding="utf-8")
                    translated += 1
                    continue
            skipped += 1
            continue
        if args.dry_run:
            translated += 1
            continue
        result = (translate_quiz(source, args.lang, args.provider) if source_file.name == "quiz.json"
                  else translate_markdown(source, args.lang, args.provider))
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(result, encoding="utf-8")
        cache[rel] = digest
        cache_file.parent.mkdir(parents=True, exist_ok=True)
        cache_file.write_text(json.dumps(cache, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        translated += 1
    removed = 0
    for rel in set(cache) - current:
        if not rel.startswith(f"phases/{args.phase}/"):
            continue
        if not args.dry_run:
            (lessons.OUT_ROOT / args.lang / rel).unlink(missing_ok=True)
            del cache[rel]
        removed += 1
    if not args.dry_run:
        cache_file.parent.mkdir(parents=True, exist_ok=True)
        cache_file.write_text(json.dumps(cache, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"{args.lang}/{args.phase}: {translated} translated, {skipped} cached, {removed} removed")


if __name__ == "__main__":
    main()

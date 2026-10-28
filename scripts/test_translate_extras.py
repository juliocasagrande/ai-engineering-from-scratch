import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import translate_extras as extras


class TranslateExtrasTest(unittest.TestCase):
    def test_quiz_preserves_answer_and_machine_fields(self):
        source = json.dumps({
            "lesson": "01-dev-environment", "title": "Environment",
            "questions": [{"stage": "pre", "question": "Why use `uv`?",
                           "options": ["Speed", "python -c 'print(1)'"],
                           "correct": 1, "explanation": "Use `uv` to install packages."}]
        })
        result = json.loads(extras.translate_quiz(source, "pt-BR", "echo"))
        self.assertEqual(result, json.loads(source))

    def test_list_quiz_keeps_shape(self):
        source = '[{"question":"Why?","options":["One","Two"],"correct":0}]'
        self.assertEqual(json.loads(extras.translate_quiz(source, "pt-BR", "echo")), json.loads(source))

    def test_markdown_preserves_frontmatter_and_fenced_code(self):
        source = '---\nname: sample\ndescription: AI prompt\n---\n\nRun it.\n\n```bash\npython3 main.py\n```\n'
        self.assertEqual(extras.translate_markdown(source, "pt-BR", "echo"), source)

    def test_technical_span_never_reaches_sentence_model(self):
        original = extras.lessons._nllb_sentence
        original_pipe = extras.lessons._nllb_pipe
        try:
            extras.lessons._nllb_pipe = lambda _: object()
            def translate(_pipe, text):
                self.assertNotIn('uv', text)
                return 'tradução ' if text.strip() else text
            extras.lessons._nllb_sentence = translate
            self.assertEqual(extras.translate_string('Use `uv` today.', 'pt-BR', 'nllb'), 'tradução `uv`tradução ')
        finally:
            extras.lessons._nllb_sentence = original
            extras.lessons._nllb_pipe = original_pipe


if __name__ == '__main__':
    unittest.main()

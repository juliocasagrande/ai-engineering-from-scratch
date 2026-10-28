---
name: skill-jax-patterns
description: Padrões de programação funcional no JAX - quando e como usar grad, jit, vmap e pmap
version: 1.0.0
phase: 3
lesson: 12
tags: [jax, functional-programming, autodiff, compilation, vectorization]
---

# Padrões funcionais JAX

JAX transforma funções puras. Cada padrão abaixo segue uma regra: escrever uma função que recebe entradas e retorna saídas, sem efeitos colaterais. Depois transformá-la.

## As Quatro Transformações

### grad -- Diferenciar uma função

```python
grads = jax.grad(loss_fn)(params, x, y)
loss, grads = jax.value_and_grad(loss_fn)(params, x, y)
```

Utilize quando: você precisa de gradientes para a otimização.
Constrangimento: a função deve retornar um escalar. `jax.jacobian`- Não .

### jit -- Compile uma função

```python
fast_fn = jax.jit(f)
```

Utilize quando: a função será chamada mais de uma vez com entradas de forma igual.
Constraint: nenhum fluxo de controle Python que dependa dos valores rastreados. `jax.lax.cond` para os condicionados, `jax.lax.scan` para os circuitos.

### vmap -- Vectorize uma função

```python
batch_fn = jax.vmap(f, in_axes=(None, 0))
```

Utilize quando: escreveu uma função para um exemplo e precisa dela para funcionar em lotes.
`in_axes` especifica qual eixo de argumento deve ser substituído. `None` Meio-divisão não em lote (divisão).

### pmap -- Paralelamente em todos os dispositivos

```python
parallel_fn = jax.pmap(f, axis_name='devices')
```

Utilize quando: você tem várias GPUs/TPUs e deseja paralelo de dados.
Dentro da função, `jax.lax.pmean(x, 'devices')` medias entre os dispositivos.

## Regras de composição

Transforma compõe.

```python
per_example_grads = jax.jit(jax.vmap(jax.grad(loss_fn), in_axes=(None, 0, 0)))
```

Leitura de direita para esquerda: tomar gradiente de loss_fn, vectorizar sobre exemplos, compilar o resultado.

Composições válidas:
- `jit(grad(f))` -- cálculo de gradientes compilado
- `jit(vmap(f))` -- compilação de partidas
- `vmap(grad(f))` -- gradientes por exemplo
- `pmap(jit(f))` -- Computação compilada paralela
- `grad(jit(f))` -- gradiente da função compilada (sim como jit(grad(f)))

## Modelo de gestão de parâmetros

Os parâmetros JAX são pytrees (dictas de matrizes aninhadas):

```python
params = {
    'layer1': {'w': jnp.zeros((784, 256)), 'b': jnp.zeros(256)},
    'layer2': {'w': jnp.zeros((256, 10)),  'b': jnp.zeros(10)},
}
```

Atualizar todos os parâmetros de uma só vez:
```python
params = jax.tree.map(lambda p, g: p - lr * g, params, grads)
```

Parâmetros de contagem:
```python
n_params = sum(p.size for p in jax.tree.leaves(params))
```

## Gerenciamento das chaves do PRNG

JAX requer chaves aleatórias explícitas:

```python
key = jax.random.PRNGKey(0)
key, subkey = jax.random.split(key)
noise = jax.random.normal(subkey, shape)
```

Para múltiplas operações aleatórias, dividir uma vez:
```python
keys = jax.random.split(key, n)
```

Nunca reutilize uma chave, sempre dividida antes de usar.

## Erros comuns

1. **Mutating arrays inside jit**As matrizes JAX são imutáveis. `x.at[i].set(v)` em vez de `x[i] = v`- Não .

2. **Using Python print inside jit**- Não . `print` - O que é que é? `jax.debug.print("{}", x)`- Não .

3. **Python if/for inside jit on traced values**Utilização: `jax.lax.cond`- Não . `jax.lax.switch`- Não . `jax.lax.scan`- Não . `jax.lax.fori_loop`- Não .

4. **Forgetting `.block_until_ready()`**Para comparar, ligar para o sistema de correção de dados `.block_until_ready()` A espera da conclusão real.

5. **Reusing PRNG keys**Duas operações com a mesma chave produzem os mesmos valores "aleatórios".

6. **Global state in jitted functions**As variáveis globais são capturadas no tempo de rastreamento. As alterações após o rastreamento são invisíveis. Passe tudo como argumentos.

## Lista de verificação das decisões

1. A função é chamada mais de uma vez? `@jax.jit`- Não .
2. - Precisa de gradientes? `jax.grad` ou `jax.value_and_grad`- Não .
3. Procede um exemplo, mas você tem um lote? `jax.vmap`- Não .
4. Tem vários dispositivos? `jax.pmap`- Não .
5. - É aleatório?
6. Tem o fluxo de controle Python em valores de matriz? `jax.lax` primitivos.

## Quando utilizar JAX

Use JAX quando:
- Precisa de gradientes por exemplo (privalidade diferencial, informação Fisher)
- Você está treinando em TPUs (JAX é a estrutura nativa)
- Precisamos de derivados de ordem superior (Hessenses, Jacobianos)
- Quer compilar todo o passo de treinamento para um único núcleo
- A sua equipa está no Google DeepMind ou Anthropic

Use PyTorch quando:
- Quer o maior ecossistema (HuggingFace, torchvision, Lightning)
- Você priorizar facilidade de depuração sobre velocidade bruta
- Você está a implementar em GPUs NVIDIA com TorchServe / Triton
- Você está contratando (existem mais desenvolvedores PyTorch)
- Quer iterar rapidamente em novas arquiteturas

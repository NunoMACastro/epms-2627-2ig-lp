![Cabeçalho](../../imagens/cabecalho.png)

# Ficha de exercícios: A primeira página com JavaScript

Praticas o rótulo de um campo, o contraste das cores, os operadores, a tradução de uma função de Python, um ciclo e a procura de erros na consola. Os exercícios 1 a 6 são obrigatórios. Entregas a pasta `ficha-01` pelo meio que o professor indicar. As respostas escritas vão para comentários no fim do `exercicios.js`, cada uma começada pelo número do exercício e, quando a há, da alínea. Para rever: o [guia do tema](../01-primeira-pagina-com-javascript.md) e o [laboratório](../laboratorios/01-primeira-pagina-com-javascript-laboratorio.md).

## O cenário

Num jogo de aventura, a personagem tem pontos de vida, de 0 a 100, apanha moedas em cada nível e leva uma mochila com itens. A vida nunca passa de 100.

Cria a pasta `ficha-01`, com este `index.html`, a página de treino, e um `exercicios.js` vazio:

```html
<!doctype html>
<html lang="pt-PT">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Ficha do tema 01</title>
    <script src="exercicios.js" defer></script>
  </head>
  <body>
    <main>
      <h1>Ficha do tema 01</h1>
      <p>Os resultados dos exercícios aparecem na consola.</p>
    </main>
  </body>
</html>
```

O código de cada exercício vai para o `exercicios.js`, e o do exercício anterior fica com `//` no início de cada linha. No VS Code, seleciona as linhas e escolhe `Toggle Line Comment`, no menu `Edit`. O `/*` e o `*/` não servem, porque o `*/` do JSDoc fecha o comentário antes do tempo.

## Exercício 1: O rótulo e o campo

A página da loja do jogo tem dois campos, neste excerto do `main`:

```html
<p>
  <label>Nome da personagem</label>
  <input id="nome-personagem" type="text">
</p>
<p>
  <label for="pocoes">Número de poções</label>
  <input id="numero-pocoes" type="text">
</p>
```

O JavaScript da loja já usa os dois `id` tal como estão.

1. Diz, para cada rótulo, se está ligado ao seu campo, e porquê.
2. Copia o excerto para o `main` do `index.html` da ficha, por baixo do parágrafo, e corrige-o para os dois rótulos ficarem ligados. Confirma no browser, sem leres o código, que ficaram.

Rever: [Os controlos da página](../01-primeira-pagina-com-javascript.md#os-controlos-da-página).

<details>
<summary>Pista</summary>

Para cada rótulo, procura o valor do `for` e o `id` do campo que está ao lado, e compara-os letra a letra.

</details>

## Exercício 2: As cores do botão

A loja tem um botão "Beber poção". Para as cores do botão há três propostas, com a razão de contraste medida numa calculadora:

| Proposta | Texto | Fundo do botão | Razão de contraste |
| --- | --- | --- | ---: |
| A | `#ffffff`, branco | `#ff9900`, laranja | 2,14 para 1 |
| B | `#000000`, preto | `#ff9900`, laranja | 9,81 para 1 |
| C | `#ffffff`, branco | `#2e7d32`, verde-escuro | 5,13 para 1 |

1. Que propostas servem para o texto do botão, e porquê?
2. Escolhe uma das que servem e escreve a regra de CSS que dá essas cores ao botão. A regra também vai num comentário, porque a página de treino não tem folha de estilos.
3. Um colega prefere a proposta A, porque "o laranja com o branco chama mais a atenção", e não quer largar o fundo laranja. O que lhe propões, e com que número da tabela o convences?

Rever: [As cores escolhem-se pelo contraste](../01-primeira-pagina-com-javascript.md#as-cores-escolhem-se-pelo-contraste) e [A apresentação com uma folha de CSS](../01-primeira-pagina-com-javascript.md#a-apresentação-com-uma-folha-de-css).

<details>
<summary>Pista</summary>

Compara cada razão com o mínimo do guia para o texto de tamanho normal.

</details>

## Exercício 3: Prever na consola

Descobre, sem correr, o valor de cada expressão, e confirma-o depois na consola do browser:

1. `40 + 25 + " de vida"`
2. `"Moedas: " + 3 * 2`
3. `9 % 3`
4. `100 / 8`
5. `"100" === 100 || 100 >= 100`
6. `!(25 > 30) && 25 !== 30`

As plicas, ou as aspas, que a consola põe à volta de um texto só mostram que o valor é um texto.

Cada valor em que falhaste leva um comentário, numa frase, com a razão. Depois, inventa outra expressão, com números teus, que engane da mesma maneira que uma das que te enganaram, ou que a que achaste mais difícil. Escreve-a no comentário, com o valor que dá e a razão, numa frase.

Rever: [Os operadores que enganam quem vem do Python](../01-primeira-pagina-com-javascript.md#os-operadores-que-enganam-quem-vem-do-python) e [O resto do Python, escrito em JavaScript](../01-primeira-pagina-com-javascript.md#o-resto-do-python-escrito-em-javascript).

<details>
<summary>Pista</summary>

Segue cada expressão como o browser: uma operação de cada vez, pela ordem certa. Em cada passo, vê se o resultado é um número, um texto ou um valor lógico.

</details>

## Exercício 4: Traduzir uma função de Python

No jogo, beber uma poção soma pontos de vida, sem a vida passar de 100. Esta função de Python faz a conta:

```python
def beber_pocao(vida, cura):
    """Devolve a vida depois de beber uma poção, sem passar de 100."""
    nova_vida = vida + cura
    if nova_vida > 100:
        return 100
    return nova_vida
```

Traduz a função para JavaScript, no `exercicios.js`, com os nomes à maneira do JavaScript e com JSDoc: o `@param` de cada parâmetro e o `@returns`. Testa-a por baixo, com um `console.log` para cada caso: vida 40 e cura 25, vida 90 e cura 25, vida 75 e cura 25. O resultado certo de cada caso tira-se da regra do cenário, e não do código.

A variável que guarda a vida nova declaraste-a com `const` ou com `let`? Justifica a escolha.

Rever: [Do Python ao JavaScript, a função `retirar`](../01-primeira-pagina-com-javascript.md#do-python-ao-javascript-a-função-retirar), [`const` para o que não muda, `let` para o que muda](../01-primeira-pagina-com-javascript.md#const-para-o-que-não-muda-let-para-o-que-muda) e [O resto do Python, escrito em JavaScript](../01-primeira-pagina-com-javascript.md#o-resto-do-python-escrito-em-javascript).

## Exercício 5: Um ciclo pelas moedas

O jogo guarda num array as moedas que a personagem apanhou em cada nível:

```js
const moedasPorNivel = [3, 0, 5, 2];
```

No `exercicios.js`, escreve um programa que comece por esta linha e some, com um `for...of`, as moedas de todos os níveis. No fim, a consola mostra `Total de moedas: ` seguido do total. O programa tem de dar o total certo também com `[]`, o array de uma personagem que ainda não jogou nenhum nível.

Rever: [Os ciclos `for` do JavaScript](../01-primeira-pagina-com-javascript.md#os-ciclos-for-do-javascript).

<details>
<summary>Pista</summary>

O total tem de existir antes do ciclo. Experimenta o programa com o `[]`: sem nenhum nível jogado, quantas moedas tem a personagem? Se a consola mostrar outra coisa, segue o programa linha a linha com esse array.

</details>

## Exercício 6: Três hábitos do Python

Uma colega escreveu esta função para descrever a mochila da personagem. O código tem três hábitos do Python, um deles em mais do que uma linha, e por isso não corre. Copia-o para o `exercicios.js`.

```js partial
// Ficha 01, exercício 6: a função da colega, que tem três erros.

/**
 * Descreve a mochila da personagem: quantos itens tem e se já tem a chave.
 * @param {string[]} itens os nomes dos itens que estão na mochila
 * @param {boolean} temChave se a personagem já apanhou a chave da arena
 * @returns {string} a frase que o jogo mostra ao jogador
 */
function descreverMochila(itens, temChave) {
  if (len(itens) === 0) {
    return "A mochila está vazia.";
  } elif (temChave === True) {
    return "Tens " + len(itens) + " itens e a chave.";
  } else {
    return "Tens " + len(itens) + " itens, mas falta a chave.";
  }
}

console.log(descreverMochila(["poção", "mapa"], true));
console.log(descreverMochila(["poção", "mapa", "corda"], false));
console.log(descreverMochila([], true));
```

O `string[]` do JSDoc quer dizer "um array de textos".

Põe a função a funcionar sem mudares o que ela faz. No fim, a consola não mostra nenhum erro e mostra a frase certa para cada uma das três mochilas. O comentário do fim do `exercicios.js` leva, para cada um dos três erros:

- a mensagem que a consola mostra para ele, com o número da linha, e o tipo de erro: de escrita, de execução ou de lógica;
- a causa, numa frase;
- a linha que mudaste, e como ficou.

Rever: [Quando a página não faz o que devia](../01-primeira-pagina-com-javascript.md#quando-a-página-não-faz-o-que-devia) e [O resto do Python, escrito em JavaScript](../01-primeira-pagina-com-javascript.md#o-resto-do-python-escrito-em-javascript).

<details>
<summary>Pista</summary>

O browser para no primeiro erro que encontra, e por isso cada correção pode fazer aparecer outro. Quando a mensagem aponta para um símbolo que parece certo, olha para o que está antes dele, na mesma linha.

</details>

## Desafios

### Desafio 1: Quantas poções

A personagem tem 20 pontos de vida, e cada poção cura 15. Tira os `//` da tua função do exercício 4. Com um `while` e essa função, escreve um programa que conte quantas poções a personagem tem de beber até a vida chegar a 100. No fim, a consola mostra o número de poções e a vida final. O resultado certo tira-se da regra do cenário, e não do programa.

Rever: [Os ciclos `for` do JavaScript](../01-primeira-pagina-com-javascript.md#os-ciclos-for-do-javascript) e [O resto do Python, escrito em JavaScript](../01-primeira-pagina-com-javascript.md#o-resto-do-python-escrito-em-javascript).

<details>
<summary>Pista</summary>

Se a página deixar de responder e a consola não mostrar o resultado do desafio, fecha o separador da página. Depois, olha para a condição do `while`: com a tua função, a vida pode alguma vez passar de 100?

</details>

### Desafio 2: O botão que não funciona

Um colega fez uma página com um botão "Beber poção", que soma 25 pontos de vida a uma personagem que começa com 40. O botão não funciona, e a consola mostra um erro. Os `id` do HTML e do JavaScript estão escritos exatamente da mesma maneira.

O `index.html` do colega:

```html
<!doctype html>
<html lang="pt-PT">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Poção</title>
    <script src="pocao.js"></script>
  </head>
  <body>
    <main>
      <h1>Poção</h1>
      <p>
        <button id="beber" type="button">Beber poção</button>
      </p>
      <p>
        <output id="vida"></output>
      </p>
    </main>
  </body>
</html>
```

O `pocao.js` do colega, na mesma pasta:

```js
// pocao.js: soma 25 pontos de vida a cada clique no botão.

let vida = 40;

const botaoBeber = document.querySelector("#beber");
const saidaVida = document.querySelector("#vida");

/**
 * Trata o clique no botão: soma 25 pontos de vida, sem passar de 100, e mostra a vida.
 * Não devolve nada: muda a vida e o texto da saída.
 */
function aoCarregarEmBeber() {
  vida = vida + 25;
  if (vida > 100) {
    vida = 100;
  }
  saidaVida.textContent = "Vida: " + vida;
}

botaoBeber.addEventListener("click", aoCarregarEmBeber);
```

Cria os dois ficheiros numa pasta nova, dentro da `ficha-01`, e põe o botão a funcionar. A rotina da depuração fica num comentário no fim do `pocao.js`. Leva a mensagem e a linha que a consola mostra, uma hipótese que não seja a dos `id`, como a verificaste e a correção. Explica também porque é que a linha da mensagem não é a linha onde está a causa.

Rever: [Quando a página não faz o que devia](../01-primeira-pagina-com-javascript.md#quando-a-página-não-faz-o-que-devia).

<details>
<summary>Pista</summary>

A mensagem diz que o `botaoBeber` vale `null`. Confirma esse valor na consola, e procura uma razão para o `querySelector` não ter encontrado um botão que está na página.

</details>

### Desafio 3: A página da poção

Queremos uma página para a personagem beber poções, numa pasta nova dentro da `ficha-01`. A personagem começa com 40 pontos de vida. A página tem um campo "Pontos de cura", com o seu rótulo, um botão "Beber poção" e uma saída com o texto `Vida: ` seguido da vida. A saída mostra a vida logo que a página abre. Cada clique dá à personagem uma poção com os pontos de cura do campo, pela regra do cenário, com a tua função do exercício 4.

Testa a página sem recarregar, com `25`, depois `50`, depois `10`: o resultado certo de cada pedido tira-se da regra do cenário. Depois recarrega a página, escreve `abc` no campo e carrega no botão. Num comentário no fim do teu ficheiro de JavaScript, explica o que a saída mostra com o `abc`, e porquê. Não precisas de corrigir este caso.

Rever: [O script encontra os elementos da página](../01-primeira-pagina-com-javascript.md#o-script-encontra-os-elementos-da-página), [O botão chama a função](../01-primeira-pagina-com-javascript.md#o-botão-chama-a-função) e [O `Number` converte o texto num número](../01-primeira-pagina-com-javascript.md#o-number-converte-o-texto-num-número).

<details>
<summary>Pista</summary>

Se o pedido de 25 não der o resultado certo, confirma de que tipo é o valor que a tua função recebe: um número ou um texto?

</details>

## Critérios de conclusão

- No exercício 1, os dois rótulos estão ligados aos seus campos, com os `id` como estavam, e o comentário diz porque é que cada rótulo não estava ligado.
- No exercício 2, a regra de CSS é a de uma proposta que serve, e a resposta ao colega usa os números da tabela.
- No exercício 3, cada valor em que falhaste tem um comentário com a razão, e a tua expressão tem o valor e a razão.
- A função do exercício 4 tem JSDoc e dá na consola o resultado certo nos três casos, e o comentário justifica o `const` ou o `let`.
- O programa do exercício 5 mostra o total certo, também com o array vazio.
- A função do exercício 6 corre sem erros. O comentário do fim do `exercicios.js` tem as três mensagens da consola, uma por erro, com a linha, o tipo, a causa e a correção.

![Rodapé](../../imagens/rodape.png)

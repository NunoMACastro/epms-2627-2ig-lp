![Cabeçalho](../../imagens/cabecalho.png)

# Ficha de exercícios: A primeira página com JavaScript

Ficha do tema A primeira página com JavaScript, do módulo M11, Introdução à Linguagem de Programação Orientada por Objetos. Praticas, em exercícios curtos, o rótulo ligado ao campo, o contraste das cores e os operadores do JavaScript. Praticas também a tradução de uma função de Python, um ciclo sobre um array e a procura de erros na consola. Fazes sozinho, ao teu ritmo: o que não acabares na aula, acabas em casa ou na aula seguinte.

## O que precisas de saber

O [guia do tema](../01-primeira-pagina-com-javascript.md) e o [laboratório](../laboratorios/01-primeira-pagina-com-javascript-laboratorio.md). Cada exercício diz em que secção do guia está a ideia que usa.

## Como trabalhar

Faz os exercícios 1 a 6 pela ordem. São a parte obrigatória, e cada um treina uma coisa só. O desafio opcional é para quem acabar. Os exercícios de "Para ires mais longe" são mais longos e servem para aprofundar: fazes os que quiseres, ou os que o professor indicar.

As respostas escritas vão para comentários no fim do `exercicios.js` da página de treino, que preparas a seguir: com `//`, ou entre `/*` e `*/` quando ocupam várias linhas. Começa cada resposta pelo número do exercício e da alínea. O HTML do exercício 1 e o CSS do exercício 2 também ficam num comentário, porque não correm no `exercicios.js`. Nos exercícios com código, pensa no resultado antes de abrires a página: é a previsão, e não o resultado, que mostra o que percebeste. Se o browser mostrar outra coisa, procura a explicação. Entrega a pasta `ficha-01` pelo meio indicado pelo professor.

Para os exercícios que correm JavaScript, prepara uma página de treino. Cria uma pasta `ficha-01` e, dentro dela, um `index.html` com o conteúdo seguinte e um `exercicios.js` vazio. O código de cada exercício vai para o `exercicios.js`, e os resultados aparecem na consola do browser. Quando passares a outro exercício, apaga o código do anterior, ou põe-no num comentário. Os comentários com as respostas ficam no fim do ficheiro.

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

Abres a página com um duplo clique no `index.html`, na janela de ficheiros do computador, e a consola com F12 no Windows ou Cmd+Option+I no macOS.

## O cenário

Num jogo de aventura, a personagem tem pontos de vida, de 0 a 100, apanha moedas em cada nível e leva uma mochila com itens. A vida nunca passa de 100. Todos os dados são inventados.

## Exercício 1: O rótulo e o campo

A página da loja do jogo tem este excerto de HTML, com dois campos. É um excerto: estaria dentro do `main` de uma página completa.

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

1. Para cada um dos dois rótulos, diz se está ligado ao seu campo e porquê. ("Rótulo, campo, botão e saída", no guia.)
2. Reescreve as linhas que precisam de mudar, para os dois rótulos ficarem ligados aos seus campos. O JavaScript da loja já usa os `id` dos dois campos tal como estão.
3. Diz como confirmas no browser, sem ler o código, que os dois rótulos ficaram ligados.

## Exercício 2: As cores do botão

A página tem um botão "Beber poção", sobre um fundo branco. Há três propostas para as cores do botão. A razão de contraste de cada uma foi medida com uma calculadora de contraste.

| Proposta | Texto | Fundo do botão | Razão de contraste |
| --- | --- | --- | ---: |
| A | `#ffffff`, branco | `#ff9900`, laranja | 2,14 para 1 |
| B | `#000000`, preto | `#ff9900`, laranja | 9,81 para 1 |
| C | `#ffffff`, branco | `#2e7d32`, verde-escuro | 5,13 para 1 |

1. Que propostas servem para o texto do botão? Porquê? ("Contraste e foco visível", no guia.)
2. Escolhe uma das propostas que servem e escreve a regra de CSS que dá essas cores ao botão.
3. Um colega prefere a proposta A, porque "o laranja com o branco chama mais a atenção". O que lhe respondes, com o número da tabela?

## Exercício 3: Prever na consola

Prevê o valor de cada uma destas expressões, e só depois escreve a expressão na consola do browser e carrega em Enter. ("Números, textos e valores lógicos" e "Operadores", no guia.)

1. `40 + 25 + " de vida"`
2. `"Moedas: " + 3 * 2`
3. `9 % 3`
4. `100 / 8`
5. `"100" === 100 || 100 >= 100`
6. `!(25 > 30) && 25 !== 30`

A consola mostra os textos entre plicas, como `'Caderno'`, ou entre aspas, conforme o browser. As plicas dizem que o valor é um texto, e não fazem parte dele.

Para cada previsão errada, explica numa frase, num comentário, porque é que a consola mostrou outro valor. Escolhe também uma das expressões que te enganaram e escreve outra, com números teus, que engane da mesma maneira.

## Exercício 4: Traduzir uma função de Python

No jogo, beber uma poção soma pontos de vida, mas a vida nunca passa de 100. Esta função de Python já faz a conta:

```python
def beber_pocao(vida, cura):
    """Devolve a vida depois de beber uma poção, sem passar de 100."""
    nova_vida = vida + cura
    if nova_vida > 100:
        return 100
    return nova_vida
```

1. Traduz a função para JavaScript, no `exercicios.js`. Os nomes seguem a convenção do JavaScript, e a função leva JSDoc, com o `@param` de cada parâmetro e o `@returns`. ("Variáveis com `const` e `let`", "Funções com `function` e `return`" e o passo 1 do "Exemplo guiado", no guia.)
2. Testa a função com um `console.log` por baixo dela para cada um destes pares de valores. O resultado esperado de cada chamada tira-se da regra do cenário, e não do código.

   | Vida | Cura | O que esperas |
   | ---: | ---: | --- |
   | 40 | 25 | |
   | 90 | 25 | |
   | 75 | 25 | |

3. A variável que guarda a vida nova declaraste-a com `const` ou com `let`? Justifica a escolha.

## Exercício 5: Um ciclo pelas moedas

O jogo guarda num array as moedas que a personagem apanhou em cada nível:

```js partial
const moedasPorNivel = [3, 0, 5, 2];
```

É só a primeira linha do programa, que vais completar.

No `exercicios.js`, escreve um programa que comece por esta linha e que use um `for...of` para somar as moedas de todos os níveis. No fim, mostra na consola o texto `Total de moedas: ` seguido do total. ("Ciclos: `for`, `while` e `for...of`", no guia.) O programa tem de dar o total certo também com o array `[]`, um array sem nenhum valor, que é o de uma personagem que ainda não jogou nenhum nível.

## Exercício 6: Três hábitos do Python

Uma colega escreveu esta função para descrever a mochila da personagem. O código tem três hábitos do Python, um deles repetido em mais do que uma linha, e por isso não corre. Copia-o para o `exercicios.js`.

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

Põe a função a funcionar, sem mudares o que ela faz: no fim, a consola não mostra nenhum erro e mostra as três frases da mochila. ("Quando a página não faz o que devia", no guia.) Para cada erro que a consola mostrar, segue a rotina da depuração e escreve-a num comentário no fim do `exercicios.js`, para o código não mudar de linha:

1. A mensagem de erro, com o número da linha, e o tipo de erro: de escrita, de execução ou de lógica.
2. A causa, numa frase.
3. A correção: a linha que mudaste, e como ficou.

Com os três erros corrigidos, prevê as três linhas que a consola vai mostrar, e confirma.

## Apoio

- Exercício 1: relê, no guia, o que o atributo `for` de um rótulo tem de ter.
- Exercício 2: o texto de tamanho normal precisa de pelo menos 4,5 para 1. Numa regra, a cor do texto é o `color` e a do fundo é o `background-color`.
- Exercício 3: o `+` com um texto junta em vez de somar, e o JavaScript faz os `+` da esquerda para a direita. O `%` é o resto da divisão.
- Exercício 4: relê, no guia, a secção "Os nomes em JavaScript" e a tabela do passo 1 do exemplo guiado, que traduz outra função linha a linha.
- Exercício 5: o total tem de existir antes do ciclo e de mudar dentro dele. Pensa no valor com que começa, para que o primeiro nível conte bem.
- Exercício 6: cada correção pode fazer aparecer o erro seguinte, porque o browser para no primeiro que encontra. Compara cada linha com as secções "Decisões com `if` e `else`", "Números, textos e valores lógicos" e "Os arrays e o `for...of`" do guia.

## Desafio opcional

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

Cria os dois ficheiros numa pasta nova e põe o botão a funcionar. Segue a rotina da depuração do guia e escreve-a num comentário no fim do `pocao.js`. Escreve a mensagem e a linha que a consola mostra. Como os `id` estão iguais, essa causa fica de fora: escreve outra hipótese e como a verificaste. Por fim, escreve a correção. Explica também, no mesmo comentário, porque é que a linha apontada pela mensagem não é a linha onde está a causa.

## Para ires mais longe

### Mais longe 1: A página da poção

Faz uma página com um campo "Pontos de cura", com o seu rótulo, um botão "Beber poção" e uma saída que mostra `Vida: ` seguido da vida da personagem. A personagem começa com 40 pontos de vida. Cada clique lê o campo, chama a tua função do exercício 4 e mostra a vida nova. A saída mostra a vida inicial logo que a página abre.

Testa a página com esta sequência, sem recarregar: `25`, depois `50`, depois `10`. O resultado esperado de cada pedido tira-se da regra do cenário. Depois recarrega e escreve `abc` no campo. Explica, num comentário no fim do teu ficheiro de JavaScript, o que a saída mostra com o `abc`, e porquê. Não precisas de corrigir este último caso: a recusa dos valores impossíveis é o assunto do tema 03.

### Mais longe 2: Quantas poções

A personagem tem 20 pontos de vida, e cada poção cura 15. Escreve um programa com um `while` que use a tua função do exercício 4 para contar quantas poções a personagem tem de beber até a vida chegar a 100. No fim, mostra na consola o número de poções e a vida final. Antes de abrires a página, segue de cabeça a vida antes e depois de cada poção, para saberes o resultado certo.

## Critérios de conclusão

- Os dois rótulos do exercício 1 estão ligados aos seus campos, e sabes como o confirmar no browser.
- Escolheste no exercício 2 uma proposta com pelo menos 4,5 para 1 e escreveste a regra de CSS dela.
- No exercício 3, previste as seis expressões antes de as escreveres na consola, e explicaste num comentário as que falharam.
- A tua função do exercício 4 tem JSDoc e dá na consola os resultados que a regra do cenário pede para as três chamadas.
- O teu ciclo do exercício 5 mostra o total das moedas, também com o array vazio.
- Encontraste e corrigiste os três hábitos do Python do exercício 6. O comentário do fim do `exercicios.js` tem a mensagem, a linha e o tipo de cada erro que a consola mostrou.

## Autoavaliação

1. Em que exercício a tua previsão falhou mais vezes? O que é que isso te diz sobre o que ainda tens de rever no guia?
2. No exercício 6, o que te ajudou mais a encontrar cada erro: a mensagem, o número da linha ou a comparação com o Python?
3. Que diferença entre o Python e o JavaScript te parece mais fácil de esquecer?

![Rodapé](../../imagens/rodape.png)

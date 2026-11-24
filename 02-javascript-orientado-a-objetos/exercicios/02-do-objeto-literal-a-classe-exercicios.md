![Cabeçalho](../../imagens/cabecalho.png)

# Ficha de exercícios: Do objeto literal à classe

Praticas o objeto literal, a classe com o `constructor` e o `new`, o `this` de cada pedido e a procura de erros numa classe. Os exercícios 1 a 5 são obrigatórios. Entregas a pasta `ficha-02` pelo meio que o professor indicar. As respostas escritas vão para comentários no fim do `exercicios.js`, cada uma começada pelo número do exercício. Para rever: o [guia do tema](../02-do-objeto-literal-a-classe.md) e o [laboratório](../laboratorios/02-do-objeto-literal-a-classe-laboratorio.md).

## O cenário

É o jogo de aventura da ficha anterior. A personagem tem pontos de vida, de 0 a 100, e apanha moedas pelo caminho, que guarda numa bolsa com lugar para 20. A vida nunca passa de 100, e as moedas nunca passam de 20: as que não cabem na bolsa perdem-se. Em todos os exercícios, o resultado certo de cada caso tira-se destas regras, e não do teu código.

Cria a pasta `ficha-02`, com este `index.html`, a página de treino, e um `exercicios.js` vazio:

```html
<!doctype html>
<html lang="pt-PT">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Ficha do tema 02</title>
    <script src="exercicios.js" defer></script>
  </head>
  <body>
    <main>
      <h1>Ficha do tema 02</h1>
      <p>Os resultados dos exercícios aparecem na consola.</p>
    </main>
  </body>
</html>
```

O código de cada exercício vai para o `exercicios.js`. Quando passas ao exercício seguinte, o código do anterior fica com `//` no início de cada linha, com o `Toggle Line Comment` do menu `Edit`. A exceção é a classe do exercício 2, que fica ativa, porque o exercício 3 e os desafios a usam. Os testes do exercício 2 ficam com `//`.

## Exercício 1: A personagem num objeto literal

No `exercicios.js`, escreve um objeto literal `heroi` para a personagem Aria, que tem 40 pontos de vida e 0 moedas. Dá-lhe um método `apanharMoedas(quantidade)`, com JSDoc, que soma à personagem as moedas apanhadas, sem passar das 20 da bolsa, e devolve o total que ela fica a ter. Só conta um número de moedas maior do que 0: com 0, ou com um número negativo, as moedas ficam como estavam.

Testa com um `console.log` para cada pedido, por esta ordem: apanhar 3, apanhar 5, apanhar 15 e apanhar -2. No fim, mostra `heroi.moedas`.

Rever: [Um objeto literal junta os dados do artigo](../02-do-objeto-literal-a-classe.md#um-objeto-literal-junta-os-dados-do-artigo) e [O método do objeto e o `this`](../02-do-objeto-literal-a-classe.md#o-método-do-objeto-e-o-this).

<details>
<summary>Pista</summary>

O método muda uma propriedade do próprio objeto. Dentro do método, que palavra te dá esse objeto?

</details>

## Exercício 2: A classe Personagem

Passa a personagem para uma classe `Personagem`, com JSDoc na classe, no `constructor` e em cada método. Cada personagem recebe o nome e os pontos de vida quando é criada, e começa sempre com 0 moedas. A classe tem três métodos:

- `beberPocao(cura)`: soma a cura à vida, sem a vida passar de 100, e devolve a vida que fica;
- `apanharMoedas(quantidade)`: com a regra do exercício 1;
- `descrever()`: devolve um texto como `Aria: vida 40, moedas 0`.

Cria a Aria, com 40 pontos de vida, e o Bruno, com 90. Testa com um `console.log` para cada pedido, por esta ordem: a Aria bebe uma poção de 25, o Bruno bebe uma de 25 e a Aria apanha 3 moedas. No fim, mostra a descrição das duas personagens.

Rever: [A classe, o `constructor` e o `new`](../02-do-objeto-literal-a-classe.md#a-classe-o-constructor-e-o-new) e [O mesmo método serve os dois artigos](../02-do-objeto-literal-a-classe.md#o-mesmo-método-serve-os-dois-artigos).

<details>
<summary>Pista</summary>

Se a descrição mostrar `moedas undefined` ou `moedas NaN`, escreve na consola `new Personagem("Aria", 40)` e vê que propriedades tem uma personagem acabada de criar.

</details>

## Exercício 3: Qual personagem muda

Com a tua classe do exercício 2 ativa, copia este código para o fim do `exercicios.js`:

```js partial
// Ficha 02, exercício 3: qual personagem muda.

const ines = new Personagem("Inês", 50);
const rui = new Personagem("Rui", 95);
const capitao = ines;

capitao.beberPocao(30);
rui.beberPocao(10);
rui.apanharMoedas(4);
capitao.apanharMoedas(2);
const outraInes = new Personagem("Inês", 50);

console.log(ines.descrever());
console.log(rui.descrever());
console.log(outraInes.descrever());
console.log(outraInes.nome === ines.nome);
console.log(outraInes === ines);
```

Descobre, sem correr, o que mostra cada uma das cinco linhas. Depois recarrega a página e confirma na consola. Cada linha em que falhaste leva um comentário, numa frase, com a razão.

Rever: [Cada instância é um objeto diferente](../02-do-objeto-literal-a-classe.md#cada-instância-é-um-objeto-diferente).

<details>
<summary>Pista</summary>

Conta os `new` do código: cada um é uma personagem. Depois, para cada nome, vê para que personagem ele aponta.

</details>

## Exercício 4: Literal ou classe

Para cada situação do jogo, decide se escreves um objeto literal ou uma classe:

1. A última jogada, para mostrar no ecrã do fim: o nível e os pontos feitos. Há só uma, e o programa não lhe pede nada.
2. Os inimigos de um nível: cada um tem um nome e pontos de vida, há dezenas em cada nível, e todos podem perder vida quando são atingidos.
3. Os três baús do nível 1: cada um tem moedas lá dentro, e todos se podem abrir.

Para cada uma, escreve num comentário a tua escolha e a razão, numa frase. Depois, escreve no `exercicios.js` o objeto da situação 1, com valores teus.

Rever: [Um objeto literal ou uma classe](../02-do-objeto-literal-a-classe.md#um-objeto-literal-ou-uma-classe).

## Exercício 5: Três erros na classe do cofre

Um colega escreveu a classe de um cofre do jogo, e o código tem três erros. Copia-o para o fim do `exercicios.js`.

```js partial
// Ficha 02, exercício 5: a classe Cofre do colega, que tem três erros.

/**
 * Um cofre do jogo, com as moedas que estão lá dentro.
 */
class Cofre {
  /**
   * Cria um cofre com as moedas que recebe.
   * @param {number} moedas as moedas que ficam dentro do cofre
   */
  construtor(moedas) {
    this.moedas = moedas;
  },

  /**
   * Abre o cofre: tira as moedas todas e devolve quantas eram.
   * @returns {number} as moedas que estavam no cofre
   */
  function abrir() {
    const dentro = this.moedas;
    this.moedas = 0;
    return dentro;
  }
}

const cofre = new Cofre(12);
console.log(cofre.abrir());
console.log(cofre.abrir());
```

Põe a classe a funcionar sem mudares o que ela faz. No fim, a consola não mostra nenhum erro, e as duas linhas mostram `12` e `0`: a primeira vez tira as 12 moedas, e a segunda encontra o cofre vazio. No fim do `exercicios.js`, um comentário diz, para cada um dos três erros:

- a mensagem que a consola mostra, com o número da linha, ou "nenhuma mensagem", e o tipo de erro: de escrita, de execução ou de lógica;
- a causa, numa frase;
- a linha que mudaste, e como ficou.

Rever: [A classe, o `constructor` e o `new`](../02-do-objeto-literal-a-classe.md#a-classe-o-constructor-e-o-new) e [Quando a página não faz o que devia](../01-primeira-pagina-com-javascript.md#quando-a-página-não-faz-o-que-devia).

<details>
<summary>Pista</summary>

O browser para no primeiro erro de escrita que encontra, e por isso cada correção pode fazer aparecer o seguinte. Quando a consola deixar de mostrar erros e o resultado continuar errado, escreve na consola `new Cofre(12)` e vê que propriedades tem um cofre acabado de criar.

</details>

## Desafios

### Desafio 1: As moedas da equipa

A equipa do jogo tem três personagens, guardadas num array:

```js partial
const equipa = [new Personagem("Aria", 40), new Personagem("Bruno", 90), new Personagem("Carla", 70)];
equipa[0].apanharMoedas(3);
equipa[1].apanharMoedas(5);
```

Com um `for...of`, escreve um programa que mostre na consola a descrição de cada personagem da equipa e, no fim, `Moedas da equipa: ` seguido do total das moedas. O programa tem de dar o total certo também com uma equipa vazia: para a experimentar, troca as três linhas dadas por `const equipa = [];`.

Rever: [Os ciclos `for` do JavaScript](../01-primeira-pagina-com-javascript.md#os-ciclos-for-do-javascript) e [O mesmo método serve os dois artigos](../02-do-objeto-literal-a-classe.md#o-mesmo-método-serve-os-dois-artigos).

<details>
<summary>Pista</summary>

Em cada volta do ciclo, a variável do `for...of` é uma personagem inteira. O que lhe podes pedir, e que propriedade dela tem as moedas?

</details>

### Desafio 2: Curar até ao fim

Acrescenta à classe `Personagem` um método `curarTotalmente()`, com JSDoc, que põe a vida da personagem nos 100 e devolve a vida. O método usa o `beberPocao` e não volta a escrever a regra dos 100. Testa-o com uma personagem com 30 pontos de vida e com outra com 100.

Rever: [O mesmo método serve os dois artigos](../02-do-objeto-literal-a-classe.md#o-mesmo-método-serve-os-dois-artigos).

<details>
<summary>Pista</summary>

Dentro de um método, o objeto que recebeu o pedido é o `this`. Um método também pode fazer um pedido a esse objeto.

</details>

### Desafio 3: A página da equipa

Queremos uma página com duas personagens: a Aria, que começa com 40 pontos de vida, e o Bruno, com 90. Cada clique num botão dá ao seu personagem uma poção com os pontos de cura do campo. As três saídas aparecem logo que a página abre. Mostram a descrição da Aria, a do Bruno e uma frase `Mais vida: ` seguida do nome de quem tem mais vida, ou de `empate`. A página não precisa de recusar curas impossíveis, como `abc` ou `-60`.

Cria a pasta `equipa`, dentro da `ficha-02`, com este `index.html` e um `equipa.js`, para onde copias a tua classe `Personagem`:

```html
<!doctype html>
<html lang="pt-PT">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>A equipa</title>
    <script src="equipa.js" defer></script>
  </head>
  <body>
    <main>
      <h1>A equipa</h1>
      <p>
        <label for="cura">Pontos de cura</label>
        <input id="cura" type="text">
      </p>
      <p>
        <button id="botao-aria" type="button">A Aria bebe</button>
        <button id="botao-bruno" type="button">O Bruno bebe</button>
      </p>
      <p>
        <output id="saida-aria"></output>
      </p>
      <p>
        <output id="saida-bruno"></output>
      </p>
      <p>
        <output id="saida-mais-vida"></output>
      </p>
    </main>
  </body>
</html>
```

A frase da terceira saída vem de uma função `quemTemMaisVida(primeira, segunda)`, com JSDoc, que recebe duas personagens e devolve o nome da que tem mais vida, ou `empate`. Testa a página sem recarregar: ao abrir, depois `50` para a Aria, depois `5` para o Bruno, depois `25` para a Aria.

Rever: [Exemplo guiado: o caderno e a pasta na mesma página](../02-do-objeto-literal-a-classe.md#exemplo-guiado-o-caderno-e-a-pasta-na-mesma-página).

<details>
<summary>Pista</summary>

Uma função pode receber objetos como parâmetros, e ler as propriedades deles com o ponto, como no `caderno.quantidade` do guia.

</details>

## Critérios de conclusão

- O objeto `heroi` do exercício 1 tem o método com JSDoc e dá o resultado certo nos quatro pedidos e no fim.
- A classe `Personagem` do exercício 2 tem JSDoc na classe, no `constructor` e em cada método, e dá o resultado certo nos três pedidos e nas duas descrições.
- No exercício 3, cada linha em que falhaste tem um comentário com a razão.
- No exercício 4, cada situação tem a escolha e a razão, e o objeto da situação 1 está no `exercicios.js`.
- A classe do exercício 5 corre sem erros e mostra `12` e `0`. O comentário do fim do `exercicios.js` tem os três erros, cada um com a mensagem ou "nenhuma mensagem", a linha, o tipo, a causa e a correção.

![Rodapé](../../imagens/rodape.png)

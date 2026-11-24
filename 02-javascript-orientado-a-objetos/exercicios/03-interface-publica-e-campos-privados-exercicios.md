![Cabeçalho](../../imagens/cabecalho.png)

# Ficha de exercícios: Interface pública e campos privados

Praticas o campo privado, o getter e o setter que recusa com um erro, o método `static`, o `try` e o `catch`, e a procura de erros numa classe protegida. Os exercícios 1 a 5 são obrigatórios. Entregas a pasta `ficha-03` pelo meio que o professor indicar. Cada resposta escrita vai para um comentário no fim do `exercicios.js`, começado pelo número do exercício. Para rever: o [guia do tema](../03-interface-publica-e-campos-privados.md) e o [laboratório](../laboratorios/03-interface-publica-e-campos-privados-laboratorio.md).

## O cenário

É o jogo de aventura das fichas anteriores. A vida de uma personagem é um número inteiro de 0 a 100. Em todos os exercícios, o resultado certo de cada caso tira-se das regras do enunciado, e não do teu código.

Cria a pasta `ficha-03`, com este `index.html`, a página de treino:

```html
<!doctype html>
<html lang="pt-PT">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Ficha do tema 03</title>
    <script src="exercicios.js" defer></script>
  </head>
  <body>
    <main>
      <h1>Ficha do tema 03</h1>
      <p>Os resultados dos exercícios aparecem na consola.</p>
    </main>
  </body>
</html>
```

E um `exercicios.js` que começa por esta classe, que ainda não protege nada:

```js
// exercicios.js: a ficha do tema 03.

/**
 * Uma personagem do jogo, com nome e pontos de vida.
 */
class Personagem {
  /**
   * Cria uma personagem com o nome e a vida que recebe.
   * @param {string} nome o nome da personagem, como "Aria"
   * @param {number} vida os pontos de vida com que começa
   */
  constructor(nome, vida) {
    this.nome = nome;
    this.vida = vida;
  }

  /**
   * Devolve o texto que descreve a personagem, com o nome e a vida.
   * @returns {string} o texto da personagem, como "Aria: vida 40"
   */
  descrever() {
    return this.nome + ": vida " + this.vida;
  }
}
```

Os exercícios 1 a 3 mudam esta classe. O código de teste de cada exercício vai por baixo dela. Quando passas ao exercício seguinte, o código de teste do anterior fica com `//` no início de cada linha, com o `Toggle Line Comment` do menu `Edit`. Um erro que ninguém apanha para o script: por isso, os casos que dão erro, sem `try`, experimentam-se na consola, um de cada vez.

## Exercício 1: A vida protegida

Protege a vida da personagem. Guarda-a num campo privado `#vida`, com um getter `vida` e um setter que só aceita um número inteiro de 0 a 100. Para outro valor, o setter lança um erro com a mensagem `A vida tem de ser um número inteiro de 0 a 100.`. A personagem também não pode nascer com uma vida impossível. Atualiza o JSDoc da classe e do `constructor`, e escreve o do getter e do setter.

Experimenta na consola, um de cada vez: criar a Aria com 40, com 0, com 100, com -1, com 101 e com 50.5. Escreve num comentário, para cada caso, se a personagem foi criada ou recusada, e quais são as duas fronteiras da regra.

Rever: [O campo privado guarda a quantidade](../03-interface-publica-e-campos-privados.md#o-campo-privado-guarda-a-quantidade), [O setter recusa com um erro](../03-interface-publica-e-campos-privados.md#o-setter-recusa-com-um-erro) e [Uma construção inválida não cria nenhum artigo](../03-interface-publica-e-campos-privados.md#uma-construção-inválida-não-cria-nenhum-artigo).

<details>
<summary>Pista</summary>

A regra tem duas fronteiras, uma em cada ponta. Para cada uma, procura o último valor aceite e o primeiro recusado entre os casos do enunciado.

</details>

## Exercício 2: O dano

Acrescenta à classe um método `sofrerDano(pontos)`, com JSDoc, que tira os pontos à vida e devolve a vida que fica. Os pontos de dano têm de ser um número inteiro, 1 ou mais. Para outro valor, o método lança um erro com a mensagem `Os pontos de dano têm de ser um número inteiro, 1 ou mais.`, e a vida fica como estava. Um golpe maior do que a vida que resta não é recusado: a personagem fica com 0 de vida.

Cria a Aria, com 40 de vida. Por baixo, faz-lhe estes golpes, por esta ordem, cada um no seu `try`: 15, 0, 2.5, 1 e 30. Num golpe aceite, mostra a vida que fica. Num golpe recusado, mostra `Golpe recusado. ` seguido da mensagem do erro.

Rever: [O pedido verifica-se no método](../03-interface-publica-e-campos-privados.md#o-pedido-verifica-se-no-método).

<details>
<summary>Pista</summary>

O setter recusa uma vida negativa. Se o golpe for maior do que a vida, que valor tem o método de entregar ao setter?

</details>

## Exercício 3: O validador da vida

Passa a regra da vida para um método `static` `vidaValida(valor)`, com JSDoc, que devolve `true` se o valor servir para vida e `false` se não servir. O setter passa a usá-lo.

Depois, usa o validador antes de criar personagens. Escreve um programa que percorre com um `for...of` as vidas `[40, 0, -1, 100, 101, 2.5]`. Para cada vida que serve, cria uma personagem chamada `Teste` com essa vida e mostra a descrição dela. Para cada vida que não serve, mostra a vida seguida de ` não serve para vida`, sem criar nenhuma personagem e sem usar o `try`.

Rever: [O validador `static`](../03-interface-publica-e-campos-privados.md#o-validador-static) e [Os ciclos `for` do JavaScript](../01-primeira-pagina-com-javascript.md#os-ciclos-for-do-javascript).

<details>
<summary>Pista</summary>

O validador responde sem precisar de nenhuma personagem. Dentro do ciclo, a pergunta vem antes do `new`.

</details>

## Exercício 4: Uma personagem que não chega a existir

Com a tua classe dos exercícios 1 a 3, copia este código para o fim do `exercicios.js`, com os testes dos exercícios anteriores comentados:

```js partial
// Ficha 03, exercício 4: uma personagem que não chega a existir.

let heroi = null;
try {
  heroi = new Personagem("Dino", 120);
  console.log("Criada: " + heroi.descrever());
} catch (erro) {
  console.log("Recusada: " + erro.message);
}
console.log(heroi);

try {
  heroi = new Personagem("Eva", 100);
  console.log("Criada: " + heroi.descrever());
} catch (erro) {
  console.log("Recusada: " + erro.message);
}
console.log(heroi.vida);
```

Descobre, sem correr, o que a consola mostra, linha a linha. Recarrega a página e confirma-o na consola. Para cada linha em que falhaste, escreve a razão num comentário, numa frase.

Rever: [Quem faz o pedido apanha a recusa](../03-interface-publica-e-campos-privados.md#quem-faz-o-pedido-apanha-a-recusa).

<details>
<summary>Pista</summary>

Quando o `new` lança um erro, a atribuição `heroi = …` chega a acontecer? E que linhas do `try` correm depois de um `throw`?

</details>

## Exercício 5: Três erros na classe do escudo

Um colega escreveu a classe de um escudo do jogo, com uma resistência que é um número inteiro de 0 a 50, e o código tem três erros. Copia-o para o fim do `exercicios.js`.

```js partial
// Ficha 03, exercício 5: a classe Escudo do colega, que tem três erros.

/**
 * Um escudo do jogo, com uma resistência de 0 a 50.
 */
class Escudo {
  #resistencia;

  /**
   * Cria um escudo com a resistência que recebe.
   * @param {number} resistencia a resistência inicial, um número inteiro de 0 a 50
   */
  constructor(resistencia) {
    this.resistencia = resistencia;
  }

  /**
   * Getter: devolve a resistência atual.
   * @returns {number} a resistência do escudo
   */
  get resistencia() {
    return this.#resistencia;
  }

  /**
   * Setter: guarda a resistência, se for válida; senão, lança um erro.
   * @param {number} valor a nova resistência
   */
  set resistencia(valor) {
    if (!resistenciaValida(valor)) {
      new Error("A resistência tem de ser um número inteiro de 0 a 50.");
    }
    this.#resistencia = valor;
  }

  /**
   * Diz se um valor serve para resistência: um número inteiro de 0 a 50.
   * @param {number} valor o valor a verificar
   * @returns {boolean} true se o valor serve, false se não serve
   */
  static resistenciaValida(valor) {
    return Number.isInteger(valor) && valor >= 0 && valor <= 50;
  }

  /**
   * Devolve o texto que descreve o escudo.
   * @returns {string} o texto do escudo, como "Escudo com resistência 30"
   */
  descrever() {
    return "Escudo com resistência " + this.resistencia();
  }
}

const escudo = new Escudo(30);
console.log(escudo.descrever());
```

Corrige a classe sem mudares o que ela faz. No fim, a consola não mostra nenhum erro e mostra `Escudo com resistência 30`. Na consola, `new Escudo(80)` é recusado com a mensagem `A resistência tem de ser um número inteiro de 0 a 50.`. Para cada um dos três erros, o comentário do fim do ficheiro diz:

- a mensagem da consola e a linha dela, ou "nenhuma mensagem", e o tipo de erro (de escrita, de execução ou de lógica);
- a causa, numa frase;
- a linha que mudaste, e como ficou.

Rever: [O validador `static`](../03-interface-publica-e-campos-privados.md#o-validador-static) e [Quando a página não faz o que devia](../01-primeira-pagina-com-javascript.md#quando-a-página-não-faz-o-que-devia).

<details>
<summary>Pista</summary>

Cada correção pode fazer aparecer o erro seguinte. Quando a consola deixar de mostrar erros, experimenta o `new Escudo(80)`. Se o escudo for criado, segue o 80 pelo `constructor` e pelo setter, linha a linha.

</details>

## Desafios

### Desafio 1: As moedas e a loja

A personagem guarda moedas numa bolsa com lugar para 20. Acrescenta à classe um campo privado `#moedas`, que começa em 0, com um getter e um setter que só aceitam um número inteiro de 0 a 20. Acrescenta dois métodos, com JSDoc, que devolvem as moedas que ficam:

- `apanharMoedas(quantidade)`: recusa com um erro uma quantidade que não seja um número inteiro, 1 ou mais. As moedas que não cabem na bolsa perdem-se, sem erro;
- `comprarPocao()`: gasta 8 moedas e cura 25 pontos de vida, sem a vida passar de 100. Sem moedas suficientes, recusa com um erro e não muda nem as moedas nem a vida.

Cria o Dino, com 50 de vida, e testa por esta ordem: apanhar 15, apanhar 10, comprar uma poção e comprar outra. Depois, na consola, experimenta comprar uma terceira poção e apanhar 0 moedas.

Rever: [O pedido verifica-se no método](../03-interface-publica-e-campos-privados.md#o-pedido-verifica-se-no-método).

<details>
<summary>Pista</summary>

A compra muda duas coisas. Antes de mudar a primeira, confirma que as duas podem mudar.

</details>

### Desafio 2: A página da personagem

Queremos uma página com a Aria, que começa com 40 de vida. A página tem um campo "Pontos de dano", com o seu rótulo, um botão "Sofrer dano", uma saída com a descrição da Aria e uma saída para as mensagens. A descrição aparece logo que a página abre. Um golpe recusado mostra `Golpe recusado. ` seguido da razão, e a vida fica igual. Um golpe aceite apaga a mensagem, mas, quando a vida fica em 0, a mensagem diz `A Aria foi derrotada.`. Com a Aria já derrotada, um golpe é aceite, e a mensagem continua a dizer `A Aria foi derrotada.`.

Cria a página na pasta `pagina-aria`, dentro da `ficha-03`, com um `index.html` e um `aria.js`, para onde copias a tua classe. Testa sem recarregar, com `15`, `abc`, `5`, `30` e `5`.

Rever: [Exemplo guiado: a página diz porque recusou](../03-interface-publica-e-campos-privados.md#exemplo-guiado-a-página-diz-porque-recusou).

<details>
<summary>Pista</summary>

A derrota não é uma recusa. Quando o golpe é aceite, em que parte do `try` e do `catch` está o programa?

</details>

### Desafio 3: Duas formas de recusar

Escreve na classe um segundo método, `sofrerDanoComMensagem(pontos)`, que faz o mesmo que o `sofrerDano`, mas sem lançar erros. Devolve um texto vazio quando o golpe é aceite, ou a mensagem da recusa. Testa-o com uma personagem com 40 de vida, com um golpe de 15 e outro de 0. Depois de cada golpe, mostra o texto devolvido entre parênteses retos, como `[` e `]`, e a vida a seguir.

Num comentário, responde: o que acontecia na página do desafio 2, se usasses este método e te esquecesses de ver o texto que ele devolve?

Rever: [Quem faz o pedido apanha a recusa](../03-interface-publica-e-campos-privados.md#quem-faz-o-pedido-apanha-a-recusa).

## Critérios de conclusão

- A classe `Personagem` guarda a vida num campo privado, com getter e setter, cada um com o seu JSDoc. O comentário do exercício 1 tem os seis casos e as duas fronteiras.
- O `sofrerDano` do exercício 2 tem JSDoc, e os cinco golpes, cada um no seu `try`, mostram a vida certa ou a recusa, com a mensagem do enunciado.
- O `vidaValida` do exercício 3 é `static`, tem JSDoc e é usado pelo setter, e o programa do `for...of` cria só as personagens com vida válida, sem `try`.
- No exercício 4, cada linha em que falhaste tem um comentário com a razão.
- A classe do exercício 5 corre sem erros e recusa o `new Escudo(80)`. O comentário do fim do ficheiro descreve os três erros, com a mensagem ou "nenhuma mensagem", a linha, o tipo, a causa e a correção.

![Rodapé](../../imagens/rodape.png)

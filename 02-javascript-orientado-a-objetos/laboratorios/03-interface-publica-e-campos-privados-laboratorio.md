![Cabeçalho](../../imagens/cabecalho.png)

# Laboratório: Interface pública e campos privados

## O que vais construir

Proteges a quantidade da classe `Artigo` da página do inventário. A quantidade passa para um campo privado, com um getter e um setter que recusa os valores impossíveis, e o `retirar` passa a recusar os pedidos inválidos com um erro. No fim, a página apanha cada recusa e diz porque não aceitou o pedido.

![A página do inventário no browser: o título Inventário da sala, o parágrafo, o rótulo Unidades a retirar com 2.5 escrito no campo, os botões Retirar do caderno e Retirar da pasta e, por baixo, a mensagem Pedido recusado. As unidades a retirar têm de ser um número inteiro, 1 ou mais., e as frases A01 Caderno, quantidade: 6 e A02 Pasta, quantidade: 2.](../../imagens/interface-publica-e-campos-privados-resultado.png)

No fim, a pasta `inventario-protegido` tem os mesmos três ficheiros do tema anterior. O `estilos.css` não muda, o `index.html` ganha uma saída para as mensagens, e o `inventario.js` muda em todas as fases.

```text
inventario-protegido/
├── index.html
├── estilos.css
└── inventario.js
```

1. [Fase 1: O campo privado guarda a quantidade](#fase-1-o-campo-privado-guarda-a-quantidade)
2. [Fase 2: O setter recusa com um erro](#fase-2-o-setter-recusa-com-um-erro)
3. [Fase 3: O validador `static`](#fase-3-o-validador-static)
4. [Fase 4: O pedido verifica-se no método](#fase-4-o-pedido-verifica-se-no-método)
5. [Fase 5: Quem faz o pedido apanha a recusa](#fase-5-quem-faz-o-pedido-apanha-a-recusa)

## O que precisas

- O VS Code e o browser dos laboratórios anteriores. As mensagens de erro deste texto são as que o Chrome e o Edge mostram.
- A pasta `inventario-objetos`, do [laboratório do tema anterior](02-do-objeto-literal-a-classe-laboratorio.md), com a página a funcionar. Se não a tiveres, usa o ponto de partida [inventario-objetos](../../exemplos/javascript-orientado-a-objetos/inventario-objetos/README.md), como diz o passo 1 de [Preparar o projeto](#preparar-o-projeto).

## Preparar o projeto

1. Faz uma cópia da página do tema anterior, para ela ficar como está. Na janela de ficheiros do computador, copia a pasta `inventario-objetos` e cola-a na mesma pasta onde ela está. A cópia aparece com outro nome: muda-o para `inventario-protegido`, sem espaços nem acentos. Se não tiveres a pasta `inventario-objetos`, cria a pasta `inventario-protegido` e abre-a no VS Code, como no passo 2. Lá dentro, cria os três ficheiros do [ponto de partida](../../exemplos/javascript-orientado-a-objetos/inventario-objetos/README.md) e copia-lhes o conteúdo, como explica o "Como correr" do README.

2. Abre a pasta no VS Code. No menu `File`, escolhe `Open Folder...` e seleciona a pasta `inventario-protegido`. O que deves ver: no `Explorer`, o nome da pasta em maiúsculas e, por baixo, o `estilos.css`, o `index.html` e o `inventario.js`.

3. Antes de mudares alguma coisa, confirma que a página funciona. Abre o `index.html` com duplo clique, na janela de ficheiros, e abre a consola. O que deves ver: `A01 Caderno, quantidade: 6` e `A02 Pasta, quantidade: 2`, e a consola sem erros. Compara também o teu `inventario.js` com o do ponto de partida: a classe tem só o `constructor`, o `retirar` e o `descrever`, e há só duas funções de clique. O JSDoc do `descrever` pode ser o teu ou o do ponto de partida. Se tiver mais, como o código de um desafio do laboratório anterior, troca o conteúdo dos três ficheiros pelo do ponto de partida.

## Fase 1: O campo privado guarda a quantidade

Passas a quantidade para um campo privado, que só a classe lê e muda, e dás ao resto do programa um getter para a ler. Rever: [O campo privado guarda a quantidade](../03-interface-publica-e-campos-privados.md#o-campo-privado-guarda-a-quantidade).

1. Declara o campo privado. No `inventario.js`, logo a seguir à linha `class Artigo {`, acrescenta:

   ```js partial
     // O # torna o campo privado: só o código de dentro da classe o lê ou o muda.
     #quantidade;

   ```

   O campo declara-se no início da classe, antes do `constructor`, com o nome começado por `#`.

2. Põe a classe a escrever no campo privado. No `constructor`, substitui a linha `this.quantidade = quantidade;` por esta:

   ```js partial
       this.#quantidade = quantidade;
   ```

   No método `retirar`, substitui a linha `this.quantidade = this.quantidade - unidades;` por esta:

   ```js partial
         this.#quantidade = this.quantidade - unidades;
   ```

   Guarda e recarrega. O que deves ver: `A01 Caderno, quantidade: undefined` e `A02 Pasta, quantidade: undefined`. A quantidade está guardada no `#quantidade`, mas o `descrever` lê `this.quantidade`, que já não existe. Falta dar ao resto do programa uma forma de a ler.

3. Acrescenta o getter. A seguir ao `constructor`, depois da chaveta que o fecha, acrescenta:

   ```js partial

     /**
      * Getter: devolve a quantidade atual, sem a mudar.
      * @returns {number} as unidades que existem
      */
     get quantidade() {
       return this.#quantidade;
     }
   ```

   Guarda e recarrega. O que deves ver: `A01 Caderno, quantidade: 6` e `A02 Pasta, quantidade: 2`. O `this.quantidade` do `descrever` e do `retirar` chama agora o getter, que devolve o `#quantidade`. Escreve `2` no campo e carrega em "Retirar do caderno". O que deves ver: `A01 Caderno, quantidade: 4`, como no tema anterior.

4. Experimenta escrever na quantidade a partir de fora da classe. Antes de experimentares, prevê: com o caderno com 4, com que quantidade fica ele depois de `caderno.quantidade = -5`? Na consola, escreve `caderno.quantidade = -5` e carrega em Enter. Depois escreve `caderno.quantidade` e carrega em Enter.

   O que deves ver: a consola repete o `-5` que escreveste, mas `caderno.quantidade` continua a dar `4`. A classe não tem nenhum método para escrever na quantidade, e a atribuição de fora não muda nada. Escreve também `caderno` e carrega em Enter: aparece `Artigo {#quantidade: 4, codigo: 'A01', nome: 'Caderno'}`, com o campo privado à vista, porque a consola é uma ferramenta de quem procura erros.

5. Provoca um erro de propósito: na função `mostrarArtigos`, muda a linha `saidaCaderno.textContent = caderno.descrever();` para `saidaCaderno.textContent = caderno.#quantidade;`. Guarda e recarrega.

   O que deves ver: as duas saídas vazias, e na consola, apontada à linha da `mostrarArtigos` que mudaste (a 68, com o ficheiro do ponto de partida):

   ```text
   Uncaught SyntaxError: Private field '#quantidade' must be declared in an enclosing class
   ```

   A mensagem quer dizer que o campo privado tem de estar declarado numa classe que envolva essa linha. A função `mostrarArtigos` está fora da classe, e por isso não pode usar o `#quantidade`. É um erro de escrita: o browser recusou o script inteiro. Volta a pôr `caderno.descrever()`, guarda e recarrega.

### Paragem 1

A página funciona como no tema anterior, mas a quantidade está num campo privado, e o código de fora só a lê, pelo getter.

A classe `Artigo` completa, como deve estar agora. O resto do ficheiro não mudou:

```js partial
/**
 * Um artigo do inventário da sala: um material com código, nome e quantidade.
 */
class Artigo {
  // O # torna o campo privado: só o código de dentro da classe o lê ou o muda.
  #quantidade;

  /**
   * Cria um artigo com os três dados que recebe.
   * @param {string} codigo o código do artigo, como "A01"
   * @param {string} nome o nome do artigo, como "Caderno"
   * @param {number} quantidade as unidades que existem
   */
  constructor(codigo, nome, quantidade) {
    this.codigo = codigo;
    this.nome = nome;
    this.#quantidade = quantidade;
  }

  /**
   * Getter: devolve a quantidade atual, sem a mudar.
   * @returns {number} as unidades que existem
   */
  get quantidade() {
    return this.#quantidade;
  }

  /**
   * Retira unidades a este artigo, se o pedido for possível, e devolve a quantidade que fica.
   * Um pedido impossível deixa a quantidade como estava.
   * @param {number} unidades as unidades que se querem retirar
   * @returns {number} a quantidade que fica depois do pedido
   */
  retirar(unidades) {
    if (unidades > 0 && unidades <= this.quantidade) {
      this.#quantidade = this.quantidade - unidades;
    }
    return this.quantidade;
  }

  /**
   * Devolve o texto que descreve este artigo, com o código, o nome e a quantidade.
   * @returns {string} o texto do artigo, como "A01 Caderno, quantidade: 6"
   */
  descrever() {
    return this.codigo + " " + this.nome + ", quantidade: " + this.quantidade;
  }
}
```

O campo privado está declarado no início, o `constructor` e o `retirar` escrevem nele, e o getter devolve-o. O JSDoc do `descrever` é o do guia do tema anterior; no teu ficheiro está o que escreveste.

Pensa antes de continuares: a classe ainda aceita o `2.5`? A resposta: aceita. O `retirar` ainda tem a condição do tema anterior, que deixa passar o `2.5`, e escreve no campo privado sem verificar nada. O campo privado impede o código de fora de escrever, mas não verifica os valores que a própria classe guarda.

## Fase 2: O setter recusa com um erro

Acrescentas um setter, que verifica cada valor antes de o guardar e recusa os impossíveis com o `throw`, e pões o `constructor` a passar por ele. Rever: [O setter recusa com um erro](../03-interface-publica-e-campos-privados.md#o-setter-recusa-com-um-erro) e [Uma construção inválida não cria nenhum artigo](../03-interface-publica-e-campos-privados.md#uma-construção-inválida-não-cria-nenhum-artigo).

1. Acrescenta o setter. A seguir ao getter, depois da chaveta que o fecha, acrescenta:

   ```js partial

     /**
      * Setter: guarda a quantidade, se for um número inteiro, 0 ou mais; senão, lança um erro.
      * @param {number} valor a nova quantidade
      */
     set quantidade(valor) {
       // O throw para o setter aqui: com um valor inválido, a linha que guarda nunca corre.
       if (!Number.isInteger(valor) || valor < 0) {
         throw new Error("A quantidade tem de ser um número inteiro, 0 ou mais.");
       }
       this.#quantidade = valor;
     }
   ```

   O setter tem o mesmo nome do getter, com `set` antes. O `Number.isInteger` dá `true` só para um número inteiro, e o `throw` lança o erro com a mensagem.

2. Põe o `constructor` a passar pelo setter. No `constructor`, substitui a linha `this.#quantidade = quantidade;` por estas duas:

   ```js partial
       // Sem o #, passa pelo setter: um artigo com uma quantidade inválida nunca chega a existir.
       this.quantidade = quantidade;
   ```

   Guarda e recarrega. O que deves ver: a página como antes, com 6 e 2, porque as duas quantidades iniciais são válidas.

3. Experimenta as fronteiras da regra na consola. Escreve cada linha da tabela, pela ordem, com Enter:

   | Na consola | O que deves ver |
   | --- | --- |
   | `caderno.quantidade = 10` | `10` |
   | `caderno.quantidade = 0` | `0` |
   | `caderno.quantidade = -1` | `Uncaught Error: A quantidade tem de ser um número inteiro, 0 ou mais.` |
   | `caderno.quantidade = 2.5` | O mesmo erro |
   | `caderno.quantidade = "6"` | O mesmo erro |
   | `caderno.quantidade` | `0` |

   O 0 é aceite e o -1 é recusado: são as duas fronteiras da regra. Depois das três recusas, a quantidade continua a ser 0, o último valor aceite. A página ainda mostra 6, porque só muda quando a função `mostrarArtigos` corre. Recarrega a página, para o caderno voltar a ter as 6 unidades que a página mostra.

4. Provoca um erro de propósito: na linha da pasta, troca o `2` por `-2`, para ficar `const pasta = new Artigo("A02", "Pasta", -2);`. Guarda e recarrega.

   O que deves ver: as duas saídas vazias, e na consola, apontada à linha 39:

   ```text
   Uncaught Error: A quantidade tem de ser um número inteiro, 0 ou mais.
   ```

   O `new` da pasta chamou o `constructor`, o `constructor` chamou o setter, e o setter recusou o -2. A pasta nunca chegou a existir, e o script parou ali, antes de mostrar os artigos. É um erro de execução: o script começou a correr e parou na linha da pasta. A linha da mensagem é a do `throw`, dentro do setter, mas a causa está na linha da pasta. Volta a pôr o `2`, guarda e recarrega.

### Paragem 2

A página funciona como na paragem 1. Agora, qualquer escrita na quantidade passa pelo setter, também a do `constructor`, e um valor impossível é recusado com um erro.

A classe `Artigo` completa, como deve estar agora:

```js partial
/**
 * Um artigo do inventário da sala: um material com código, nome e quantidade.
 */
class Artigo {
  // O # torna o campo privado: só o código de dentro da classe o lê ou o muda.
  #quantidade;

  /**
   * Cria um artigo com os três dados que recebe.
   * @param {string} codigo o código do artigo, como "A01"
   * @param {string} nome o nome do artigo, como "Caderno"
   * @param {number} quantidade as unidades que existem
   */
  constructor(codigo, nome, quantidade) {
    this.codigo = codigo;
    this.nome = nome;
    // Sem o #, passa pelo setter: um artigo com uma quantidade inválida nunca chega a existir.
    this.quantidade = quantidade;
  }

  /**
   * Getter: devolve a quantidade atual, sem a mudar.
   * @returns {number} as unidades que existem
   */
  get quantidade() {
    return this.#quantidade;
  }

  /**
   * Setter: guarda a quantidade, se for um número inteiro, 0 ou mais; senão, lança um erro.
   * @param {number} valor a nova quantidade
   */
  set quantidade(valor) {
    // O throw para o setter aqui: com um valor inválido, a linha que guarda nunca corre.
    if (!Number.isInteger(valor) || valor < 0) {
      throw new Error("A quantidade tem de ser um número inteiro, 0 ou mais.");
    }
    this.#quantidade = valor;
  }

  /**
   * Retira unidades a este artigo, se o pedido for possível, e devolve a quantidade que fica.
   * Um pedido impossível deixa a quantidade como estava.
   * @param {number} unidades as unidades que se querem retirar
   * @returns {number} a quantidade que fica depois do pedido
   */
  retirar(unidades) {
    if (unidades > 0 && unidades <= this.quantidade) {
      this.#quantidade = this.quantidade - unidades;
    }
    return this.quantidade;
  }

  /**
   * Devolve o texto que descreve este artigo, com o código, o nome e a quantidade.
   * @returns {string} o texto do artigo, como "A01 Caderno, quantidade: 6"
   */
  descrever() {
    return this.codigo + " " + this.nome + ", quantidade: " + this.quantidade;
  }
}
```

O setter ficou entre o getter e o `retirar`. O `constructor` escreve pelo setter, e o `retirar` ainda escreve diretamente no campo privado.

Pensa antes de continuares: dentro do setter, porque é que a última linha escreve `this.#quantidade = valor;`, com o `#`, e não `this.quantidade = valor;`? A resposta: `this.quantidade = valor;` chamava o próprio setter outra vez, que voltava a chamar-se, sem fim, até o browser parar com `RangeError: Maximum call stack size exceeded`. Por isso, dentro do setter, a escrita vai direta ao campo privado, com o `#`.

## Fase 3: O validador `static`

Passas a pergunta "este valor serve para quantidade?" para um método `static`, que pertence à classe, e o setter passa a usá-lo. Rever: [O validador `static`](../03-interface-publica-e-campos-privados.md#o-validador-static).

1. Vê na consola um método `static` do próprio JavaScript. Escreve, uma linha de cada vez, com Enter: `Number.isInteger(4)`, `Number.isInteger(2.5)` e `Number.isInteger("4")`.

   O que deves ver: `true`, `false` e `false`. O `isInteger` chama-se com o nome `Number` antes do ponto, e não num número: pertence à classe `Number`.

2. Escreve o validador da classe. A seguir ao setter, depois da chaveta que o fecha, acrescenta:

   ```js partial

     /**
      * Diz se um valor serve para quantidade de um artigo: um número inteiro, 0 ou mais.
      * É static: pertence à classe, e chama-se com o nome dela, como Artigo.quantidadeValida(4).
      * @param {number} valor o valor a verificar
      * @returns {boolean} true se o valor serve, false se não serve
      */
     static quantidadeValida(valor) {
       return Number.isInteger(valor) && valor >= 0;
     }
   ```

3. Põe o setter a usar o validador. No setter, substitui a linha `if (!Number.isInteger(valor) || valor < 0) {` por esta:

   ```js partial
       if (!Artigo.quantidadeValida(valor)) {
   ```

   A condição lê-se "se o valor não serve para quantidade". O comentário do `throw`, por cima, fica como está. Guarda e recarrega. O que deves ver: a página como antes, com 6 e 2.

4. Experimenta o validador na consola. Escreve, uma linha de cada vez, com Enter: `Artigo.quantidadeValida(4)`, `Artigo.quantidadeValida(-1)` e `caderno.quantidadeValida(4)`.

   O que deves ver: `true`, `false` e, na terceira, `Uncaught TypeError: caderno.quantidadeValida is not a function`. A mensagem quer dizer que `caderno.quantidadeValida` não é uma função. O método `static` está na classe, e não em cada artigo, e chama-se sempre com o nome `Artigo` antes do ponto.

### Paragem 3

A página funciona como na paragem 2. A regra da quantidade está escrita uma só vez, no validador, e o setter pergunta-lhe se o valor serve.

O setter e o validador, como devem estar agora. O resto da classe não mudou:

```js partial
  /**
   * Setter: guarda a quantidade, se for um número inteiro, 0 ou mais; senão, lança um erro.
   * @param {number} valor a nova quantidade
   */
  set quantidade(valor) {
    // O throw para o setter aqui: com um valor inválido, a linha que guarda nunca corre.
    if (!Artigo.quantidadeValida(valor)) {
      throw new Error("A quantidade tem de ser um número inteiro, 0 ou mais.");
    }
    this.#quantidade = valor;
  }

  /**
   * Diz se um valor serve para quantidade de um artigo: um número inteiro, 0 ou mais.
   * É static: pertence à classe, e chama-se com o nome dela, como Artigo.quantidadeValida(4).
   * @param {number} valor o valor a verificar
   * @returns {boolean} true se o valor serve, false se não serve
   */
  static quantidadeValida(valor) {
    return Number.isInteger(valor) && valor >= 0;
  }
```

O validador vem logo a seguir ao setter, que é quem o usa. Dentro da classe, também se chama com o nome `Artigo`, porque é um método da classe.

Pensa antes de continuares: o validador podia usar `this.quantidade`? A resposta: não. Um método `static` chama-se na classe, `Artigo.quantidadeValida(4)`, e não há nenhum artigo antes do ponto, nem quantidade nenhuma para ler. O validador só trabalha com o valor que recebe.

## Fase 4: O pedido verifica-se no método

Trocas o `retirar` por um com contrato, que verifica as regras do pedido e recusa com um erro, e que muda a quantidade pelo setter. Rever: [O pedido verifica-se no método](../03-interface-publica-e-campos-privados.md#o-pedido-verifica-se-no-método).

1. Substitui o método `retirar` inteiro, com o JSDoc dele, por este:

   ```js partial
     /**
      * Retira unidades a este artigo e devolve a quantidade que fica.
      * Lança um erro, sem mudar nada, se o pedido não for um número inteiro de 1 ou mais,
      * ou se não houver unidades suficientes.
      * @param {number} unidades as unidades que se querem retirar
      * @returns {number} a quantidade que fica depois do pedido
      */
     retirar(unidades) {
       if (!Number.isInteger(unidades) || unidades < 1) {
         throw new Error("As unidades a retirar têm de ser um número inteiro, 1 ou mais.");
       }
       if (unidades > this.quantidade) {
         throw new Error("Não há unidades suficientes.");
       }
       // A quantidade muda pelo setter, que guarda a invariante.
       this.quantidade = this.quantidade - unidades;
       return this.quantidade;
     }
   ```

   As duas verificações são as regras do pedido, e vêm antes de qualquer mudança.

2. Guarda e recarrega. Faz um pedido de `2` ao caderno, e depois um de `5`.

   O que deves ver: o pedido de 2 deixa `A01 Caderno, quantidade: 4`. O de 5 deixa a página igual, e a consola mostra, apontada à linha 66:

   ```text
   Uncaught Error: Não há unidades suficientes.
   ```

   O `retirar` recusou o pedido, e ninguém apanhou o erro. A função do clique parou na linha do `retirar`, antes de chamar `mostrarArtigos`, e a página não mostra mensagem nenhuma. É um erro de execução.

3. Experimenta o `2.5`, que o tema anterior aceitava, e o `abc`, que recusava sem dizer nada. Faz um pedido de `2.5` ao caderno, e depois um de `abc`.

   O que deves ver: as quantidades iguais, e na consola a mesma mensagem nos dois pedidos, `Uncaught Error: As unidades a retirar têm de ser um número inteiro, 1 ou mais.`. A consola pode juntá-las numa só linha, com um 2 à esquerda. O `2.5` não é um número inteiro, e o `abc` dá `NaN` no `Number`, que também não é.

### Paragem 4

A classe protege a quantidade e recusa os pedidos inválidos, mas a página ainda não diz nada: as recusas só aparecem na consola.

A classe `Artigo` completa, já com o `retirar` novo:

```js partial
/**
 * Um artigo do inventário da sala: um material com código, nome e quantidade.
 */
class Artigo {
  // O # torna o campo privado: só o código de dentro da classe o lê ou o muda.
  #quantidade;

  /**
   * Cria um artigo com os três dados que recebe.
   * @param {string} codigo o código do artigo, como "A01"
   * @param {string} nome o nome do artigo, como "Caderno"
   * @param {number} quantidade as unidades que existem
   */
  constructor(codigo, nome, quantidade) {
    this.codigo = codigo;
    this.nome = nome;
    // Sem o #, passa pelo setter: um artigo com uma quantidade inválida nunca chega a existir.
    this.quantidade = quantidade;
  }

  /**
   * Getter: devolve a quantidade atual, sem a mudar.
   * @returns {number} as unidades que existem
   */
  get quantidade() {
    return this.#quantidade;
  }

  /**
   * Setter: guarda a quantidade, se for um número inteiro, 0 ou mais; senão, lança um erro.
   * @param {number} valor a nova quantidade
   */
  set quantidade(valor) {
    // O throw para o setter aqui: com um valor inválido, a linha que guarda nunca corre.
    if (!Artigo.quantidadeValida(valor)) {
      throw new Error("A quantidade tem de ser um número inteiro, 0 ou mais.");
    }
    this.#quantidade = valor;
  }

  /**
   * Diz se um valor serve para quantidade de um artigo: um número inteiro, 0 ou mais.
   * É static: pertence à classe, e chama-se com o nome dela, como Artigo.quantidadeValida(4).
   * @param {number} valor o valor a verificar
   * @returns {boolean} true se o valor serve, false se não serve
   */
  static quantidadeValida(valor) {
    return Number.isInteger(valor) && valor >= 0;
  }

  /**
   * Retira unidades a este artigo e devolve a quantidade que fica.
   * Lança um erro, sem mudar nada, se o pedido não for um número inteiro de 1 ou mais,
   * ou se não houver unidades suficientes.
   * @param {number} unidades as unidades que se querem retirar
   * @returns {number} a quantidade que fica depois do pedido
   */
  retirar(unidades) {
    if (!Number.isInteger(unidades) || unidades < 1) {
      throw new Error("As unidades a retirar têm de ser um número inteiro, 1 ou mais.");
    }
    if (unidades > this.quantidade) {
      throw new Error("Não há unidades suficientes.");
    }
    // A quantidade muda pelo setter, que guarda a invariante.
    this.quantidade = this.quantidade - unidades;
    return this.quantidade;
  }

  /**
   * Devolve o texto que descreve este artigo, com o código, o nome e a quantidade.
   * @returns {string} o texto do artigo, como "A01 Caderno, quantidade: 6"
   */
  descrever() {
    return this.codigo + " " + this.nome + ", quantidade: " + this.quantidade;
  }
}
```

A classe tem agora, por esta ordem, o campo privado, o `constructor`, o getter, o setter, o validador, o `retirar` e o `descrever`. Só o setter escreve no campo privado.

Pensa antes de continuares: com 4 unidades no caderno, um pedido de 4 é aceite? A resposta: é. As duas regras do pedido deixam passar o 4, que é inteiro e não passa do que existe, e o setter aceita o 0 que fica. Retirar tudo esgota o material, e um artigo com 0 unidades está num estado válido.

## Fase 5: Quem faz o pedido apanha a recusa

Dás à página uma saída para as mensagens, e cada função de clique passa a fazer o pedido dentro de um `try`. O `catch` mostra a razão da recusa. Rever: [Quem faz o pedido apanha a recusa](../03-interface-publica-e-campos-privados.md#quem-faz-o-pedido-apanha-a-recusa).

1. Dá à página uma saída para as mensagens. No `index.html`, a seguir ao parágrafo dos dois botões, acrescenta:

   ```html
         <p>
           <output id="mensagem"></output>
         </p>
   ```

   No `inventario.js`, a seguir à linha `const botaoPasta = document.querySelector("#botao-pasta");`, acrescenta:

   ```js partial
   const saidaMensagem = document.querySelector("#mensagem");
   ```

   Guarda os dois ficheiros e recarrega. O que deves ver: a página como antes, porque a saída nova começa vazia.

2. Põe a função do caderno a apanhar a recusa. Substitui a função `aoCarregarNoCaderno` inteira, com o JSDoc dela, por esta:

   ```js partial
   /**
    * Trata o clique no botão do caderno: tenta retirar ao caderno as unidades do campo.
    * Não devolve nada: muda a quantidade do caderno, ou mostra porque o pedido foi recusado.
    */
   function aoCarregarNoCaderno() {
     const unidades = Number(campoUnidades.value);
     try {
       caderno.retirar(unidades);
       saidaMensagem.textContent = "";
     } catch (erro) {
       // O retirar recusou o pedido: o erro traz a mensagem que o throw escreveu.
       saidaMensagem.textContent = "Pedido recusado. " + erro.message;
     }
     mostrarArtigos();
   }
   ```

   Guarda e recarrega. Antes de experimentares, prevê: com `5` no campo e o caderno com 6, o que acontece quando carregas em "Retirar do caderno" duas vezes seguidas? Experimenta.

   O que deves ver: o primeiro clique deixa o caderno com 1, e a mensagem vazia. O segundo mostra `Pedido recusado. Não há unidades suficientes.`, e o caderno continua com 1. A consola não mostra nenhum erro: o `catch` apanhou-o.

3. Põe também a função da pasta a apanhar a recusa. Substitui a função `aoCarregarNaPasta` inteira, com o JSDoc dela, por esta:

   ```js partial
   /**
    * Trata o clique no botão da pasta: tenta retirar à pasta as unidades do campo.
    * Não devolve nada: muda a quantidade da pasta, ou mostra porque o pedido foi recusado.
    */
   function aoCarregarNaPasta() {
     const unidades = Number(campoUnidades.value);
     try {
       pasta.retirar(unidades);
       saidaMensagem.textContent = "";
     } catch (erro) {
       saidaMensagem.textContent = "Pedido recusado. " + erro.message;
     }
     mostrarArtigos();
   }
   ```

4. Guarda e recarrega. Faz esta sequência de pedidos, sem recarregar entre eles, e confirma a mensagem e as duas saídas depois de cada um:

   | Pedido | Escreves no campo | Carregas em | A mensagem | O caderno | A pasta |
   | --- | --- | --- | --- | --- | --- |
   | 1 | `2.5` | Retirar do caderno | `Pedido recusado. As unidades a retirar têm de ser um número inteiro, 1 ou mais.` | `A01 Caderno, quantidade: 6` | `A02 Pasta, quantidade: 2` |
   | 2 | `2` | Retirar do caderno | vazia | `A01 Caderno, quantidade: 4` | `A02 Pasta, quantidade: 2` |
   | 3 | `3` | Retirar da pasta | `Pedido recusado. Não há unidades suficientes.` | `A01 Caderno, quantidade: 4` | `A02 Pasta, quantidade: 2` |
   | 4 | `abc` | Retirar da pasta | `Pedido recusado. As unidades a retirar têm de ser um número inteiro, 1 ou mais.` | `A01 Caderno, quantidade: 4` | `A02 Pasta, quantidade: 2` |
   | 5 | `2` | Retirar da pasta | vazia | `A01 Caderno, quantidade: 4` | `A02 Pasta, quantidade: 0` |

   Cada recusa diz a sua razão, e as quantidades ficam como estavam. Um pedido aceite apaga a mensagem do pedido anterior.

5. Provoca um erro de propósito: na função `aoCarregarNaPasta`, troca `erro.message` por `erro.mensagem`. Guarda, recarrega e faz um pedido de `3` à pasta.

   O que deves ver: `Pedido recusado. undefined`, e nenhuma mensagem na consola. A propriedade do erro com a mensagem chama-se `message`, em inglês, e uma propriedade que não existe dá `undefined`. É um erro de lógica. Volta a pôr `erro.message`, guarda e recarrega.

### Paragem 5

A página está completa: protege as quantidades e diz porque recusa cada pedido.

O ficheiro `index.html` completo, como deve estar agora:

```html
<!doctype html>
<html lang="pt-PT">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Inventário da sala</title>
    <link rel="stylesheet" href="estilos.css">
    <script src="inventario.js" defer></script>
  </head>
  <body>
    <main>
      <h1>Inventário da sala</h1>
      <p>O caderno A01 começa com 6 unidades, e a pasta A02 com 2. Escreve quantas unidades queres retirar e carrega no botão do artigo.</p>
      <p>
        <label for="unidades">Unidades a retirar</label>
        <input id="unidades" type="text">
      </p>
      <p>
        <button id="botao-caderno" type="button">Retirar do caderno</button>
        <button id="botao-pasta" type="button">Retirar da pasta</button>
      </p>
      <p>
        <output id="mensagem"></output>
      </p>
      <p>
        <output id="saida-caderno"></output>
      </p>
      <p>
        <output id="saida-pasta"></output>
      </p>
    </main>
  </body>
</html>
```

O ficheiro `inventario.js` completo. No teu, o JSDoc do `descrever` pode ser o que escreveste no laboratório anterior:

```js
// inventario.js: o comportamento da página do inventário.
// Cada artigo é um objeto da classe Artigo, e cada botão retira unidades a um deles.

/**
 * Um artigo do inventário da sala: um material com código, nome e quantidade.
 */
class Artigo {
  // O # torna o campo privado: só o código de dentro da classe o lê ou o muda.
  #quantidade;

  /**
   * Cria um artigo com os três dados que recebe.
   * @param {string} codigo o código do artigo, como "A01"
   * @param {string} nome o nome do artigo, como "Caderno"
   * @param {number} quantidade as unidades que existem
   */
  constructor(codigo, nome, quantidade) {
    this.codigo = codigo;
    this.nome = nome;
    // Sem o #, passa pelo setter: um artigo com uma quantidade inválida nunca chega a existir.
    this.quantidade = quantidade;
  }

  /**
   * Getter: devolve a quantidade atual, sem a mudar.
   * @returns {number} as unidades que existem
   */
  get quantidade() {
    return this.#quantidade;
  }

  /**
   * Setter: guarda a quantidade, se for um número inteiro, 0 ou mais; senão, lança um erro.
   * @param {number} valor a nova quantidade
   */
  set quantidade(valor) {
    // O throw para o setter aqui: com um valor inválido, a linha que guarda nunca corre.
    if (!Artigo.quantidadeValida(valor)) {
      throw new Error("A quantidade tem de ser um número inteiro, 0 ou mais.");
    }
    this.#quantidade = valor;
  }

  /**
   * Diz se um valor serve para quantidade de um artigo: um número inteiro, 0 ou mais.
   * É static: pertence à classe, e chama-se com o nome dela, como Artigo.quantidadeValida(4).
   * @param {number} valor o valor a verificar
   * @returns {boolean} true se o valor serve, false se não serve
   */
  static quantidadeValida(valor) {
    return Number.isInteger(valor) && valor >= 0;
  }

  /**
   * Retira unidades a este artigo e devolve a quantidade que fica.
   * Lança um erro, sem mudar nada, se o pedido não for um número inteiro de 1 ou mais,
   * ou se não houver unidades suficientes.
   * @param {number} unidades as unidades que se querem retirar
   * @returns {number} a quantidade que fica depois do pedido
   */
  retirar(unidades) {
    if (!Number.isInteger(unidades) || unidades < 1) {
      throw new Error("As unidades a retirar têm de ser um número inteiro, 1 ou mais.");
    }
    if (unidades > this.quantidade) {
      throw new Error("Não há unidades suficientes.");
    }
    // A quantidade muda pelo setter, que guarda a invariante.
    this.quantidade = this.quantidade - unidades;
    return this.quantidade;
  }

  /**
   * Devolve o texto que descreve este artigo, com o código, o nome e a quantidade.
   * @returns {string} o texto do artigo, como "A01 Caderno, quantidade: 6"
   */
  descrever() {
    return this.codigo + " " + this.nome + ", quantidade: " + this.quantidade;
  }
}

// O new cria um objeto novo da classe e chama o constructor com estes três valores.
const caderno = new Artigo("A01", "Caderno", 6);
const pasta = new Artigo("A02", "Pasta", 2);

const campoUnidades = document.querySelector("#unidades");
const botaoCaderno = document.querySelector("#botao-caderno");
const botaoPasta = document.querySelector("#botao-pasta");
const saidaMensagem = document.querySelector("#mensagem");
const saidaCaderno = document.querySelector("#saida-caderno");
const saidaPasta = document.querySelector("#saida-pasta");

/**
 * Mostra na página a descrição dos dois artigos, cada uma na sua saída.
 * Não devolve nada: muda o texto das duas saídas.
 */
function mostrarArtigos() {
  saidaCaderno.textContent = caderno.descrever();
  saidaPasta.textContent = pasta.descrever();
}

/**
 * Trata o clique no botão do caderno: tenta retirar ao caderno as unidades do campo.
 * Não devolve nada: muda a quantidade do caderno, ou mostra porque o pedido foi recusado.
 */
function aoCarregarNoCaderno() {
  const unidades = Number(campoUnidades.value);
  try {
    caderno.retirar(unidades);
    saidaMensagem.textContent = "";
  } catch (erro) {
    // O retirar recusou o pedido: o erro traz a mensagem que o throw escreveu.
    saidaMensagem.textContent = "Pedido recusado. " + erro.message;
  }
  mostrarArtigos();
}

/**
 * Trata o clique no botão da pasta: tenta retirar à pasta as unidades do campo.
 * Não devolve nada: muda a quantidade da pasta, ou mostra porque o pedido foi recusado.
 */
function aoCarregarNaPasta() {
  const unidades = Number(campoUnidades.value);
  try {
    pasta.retirar(unidades);
    saidaMensagem.textContent = "";
  } catch (erro) {
    saidaMensagem.textContent = "Pedido recusado. " + erro.message;
  }
  mostrarArtigos();
}

// Cada botão recebe uma função que lê o campo e faz o pedido, e não o método: assim o this é o artigo.
botaoCaderno.addEventListener("click", aoCarregarNoCaderno);
botaoPasta.addEventListener("click", aoCarregarNaPasta);

// As saídas começam vazias no HTML; esta chamada mostra os dois artigos ao abrir.
mostrarArtigos();
```

A classe protegida vem primeiro, e logo a seguir os dois artigos. Por baixo, os elementos, com a saída das mensagens, e as duas funções dos cliques, cada uma com o seu `try` e o seu `catch`.

Pensa antes de terminares: porque é que a chamada `mostrarArtigos();` está depois do `catch`, e não dentro do `try`? A resposta: depois do `catch`, corre nos dois casos, aceite ou recusado. Dentro do `try`, uma recusa saltava-a, e a página não mudava, o que até dava certo, porque as quantidades não mudaram. Fora do `try`, a página mostra sempre o estado verdadeiro dos artigos, aconteça o que acontecer ao pedido.

## Se alguma coisa falhar

1. A barra lateral do VS Code mostra `INVENTARIO-PROTEGIDO`? Se mostrar outra pasta, abre esta como no passo 2 de [Preparar o projeto](#preparar-o-projeto).
2. Guardaste os ficheiros? Se o separador de um ficheiro tem uma bola no lugar da cruz, falta guardá-lo.
3. Recarregaste a página, na janela do browser? A página não muda sozinha. O endereço do separador tem de acabar em `inventario-protegido/index.html`, e não na página do tema anterior.
4. Há erros na consola? Procura a mensagem a vermelho nos problemas de baixo.
5. Desfizeste o último erro provocado? Os passos seguintes contam com os ficheiros sem o erro provocado. Se não souberes onde estás, copia a última classe ou o último ficheiro completo do laboratório e refaz os passos seguintes.

### A consola mostra `Uncaught SyntaxError: Private field '#quantidade' must be declared in an enclosing class`

O nome `#quantidade` está a ser usado onde não pode. Ou está fora da classe, numa função como a `mostrarArtigos`, ou falta a linha que o declara, `#quantidade;`, no início da classe, como no passo 1 da fase 1. Fora da classe, a quantidade lê-se com `caderno.quantidade`, sem o `#`.

### A consola mostra `Uncaught TypeError: Cannot set property quantidade of #<Artigo> which has only a getter`

A mensagem quer dizer que não se pode dar um valor à propriedade `quantidade`, porque ela só tem getter. Uma linha da classe escreve `this.quantidade = …` antes de existir o setter. Na fase 1, o `constructor` e o `retirar` escrevem com o `#`, como no passo 2. Da fase 2 em diante, confirma que o setter está escrito e se chama `quantidade`, como o getter.

### A consola mostra `Uncaught RangeError: Maximum call stack size exceeded`

A mensagem quer dizer que se passou o tamanho máximo da pilha de chamadas. A última linha do setter escreve `this.quantidade = valor;`, sem o `#`, e o setter chama-se a si próprio sem parar. Escreve `this.#quantidade = valor;`.

### A consola mostra `Uncaught Error: A quantidade tem de ser um número inteiro, 0 ou mais.`, ao abrir a página

Um dos `new Artigo` tem uma quantidade impossível, como o `-2` do passo 4 da fase 2. A mensagem aponta para o `throw` do setter, mas a causa está na linha do `new`. Confirma que o caderno tem `6` e a pasta tem `2`.

### Um pedido recusado mostra `Uncaught Error` na consola, e a página não diz nada

Depois da fase 5, isto quer dizer que a função desse botão ainda não tem o `try` e o `catch`. Confirma as duas funções dos cliques com as dos passos 2 e 3 da fase 5.

### A consola mostra `Uncaught TypeError: Cannot set properties of null (setting 'textContent')`, ao carregar num botão

O script não encontrou a saída das mensagens: o `index.html` não tem o `<output id="mensagem">` do passo 1 da fase 5, ou não foi guardado. O pedido pode ter mudado a quantidade antes do erro, mesmo que a página não o mostre. Confirma o `index.html` com o da paragem 5, guarda e recarrega.

### A mensagem diz `Pedido recusado. undefined`

O `catch` escreve `erro.mensagem`, em português. A mensagem do erro está em `erro.message`, em inglês.

### Todos os pedidos são recusados, mesmo o `2`

A função do clique passa ao `retirar` o texto do campo, como `"2"`, que não é um número inteiro. Confirma que a primeira linha da função é `const unidades = Number(campoUnidades.value);`.

### A consola mostra `Uncaught TypeError: caderno.quantidadeValida is not a function`

O validador é `static`, e chama-se com o nome da classe: `Artigo.quantidadeValida(4)`, e não `caderno.quantidadeValida(4)`.

## Desafios

1. Acertar a contagem. Depois de contar o que está no armário, alguém precisa de corrigir a quantidade do caderno. Acrescenta à página um botão "Acertar o caderno", que usa o mesmo campo e põe o caderno com essa quantidade, pelo setter. Uma quantidade impossível é recusada, com a mensagem na saída das mensagens. Testa com `10`, `-1`, `2.5` e `0`. Pista: o setter já recusa com um erro; falta apanhá-lo, como nas funções de retirar.
2. O `adicionar` com contrato. Acrescenta à classe um método `adicionar(unidades)`, com JSDoc, que soma unidades ao artigo e devolve a quantidade que fica. Recusa com um erro, e com uma mensagem própria, um pedido que não seja um número inteiro de 1 ou mais. Testa-o na consola nos dois artigos, com `3`, `0` e `2.5`. Pista: as unidades a adicionar têm a mesma regra que as unidades a retirar, mas não há limite de cima.
3. A mensagem de um pedido aceite. Num pedido aceite, a saída das mensagens fica vazia. Muda as duas funções dos cliques para que, num pedido aceite, a mensagem diga `Pedido aceite. Quantidade do caderno: 4.`, ou da pasta, com a quantidade que fica. Pista: o `retirar` devolve a quantidade que fica.

## Antes de terminares

- [ ] A pasta `inventario-protegido` tem o `index.html`, o `estilos.css` e o `inventario.js`, e a página abre com um duplo clique.
- [ ] A página abre sem erros na consola.
- [ ] Na consola, `caderno.quantidade = -1` dá `Uncaught Error`, e a quantidade fica como estava.
- [ ] A sequência do passo 4 da fase 5 dá as mensagens e as saídas da tabela.
- [ ] Sabes que tipo de erro é cada um dos que provocaste: o `#quantidade` fora da classe, a pasta com -2, o pedido de 5 sem `try` e o `erro.mensagem`.
- [ ] Sabes explicar porque é que o `constructor` passa pelo setter, e porque é que o validador é `static`.

![Rodapé](../../imagens/rodape.png)

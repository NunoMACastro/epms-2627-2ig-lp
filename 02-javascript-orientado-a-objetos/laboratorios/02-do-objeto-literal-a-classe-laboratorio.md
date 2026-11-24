![Cabeçalho](../../imagens/cabecalho.png)

# Laboratório: Do objeto literal à classe

## O que vais construir

Transformas a página do inventário do tema anterior. O caderno passa a ser um objeto, primeiro literal e depois da classe `Artigo`, e a pasta A02 entra na página, com o seu botão e a sua saída. No fim, cada botão retira unidades a um artigo, e o outro fica como estava.

![A página do inventário no browser: o título Inventário da sala, o parágrafo, o rótulo Unidades a retirar com o campo, os botões Retirar do caderno e Retirar da pasta, azul-escuros com letras brancas, e, por baixo, as frases A01 Caderno, quantidade: 6 e A02 Pasta, quantidade: 2.](../../imagens/do-objeto-literal-a-classe-resultado.png)

No fim, a pasta `inventario-objetos` tem os mesmos três ficheiros da página do tema anterior. O `estilos.css` não muda, e o `index.html` e o `inventario.js` mudam ao longo das fases.

```text
inventario-objetos/
├── index.html
├── estilos.css
└── inventario.js
```

1. [Fase 1: Um objeto literal junta os dados do artigo](#fase-1-um-objeto-literal-junta-os-dados-do-artigo)
2. [Fase 2: O método do objeto e o `this`](#fase-2-o-método-do-objeto-e-o-this)
3. [Fase 3: A classe, o `constructor` e o `new`](#fase-3-a-classe-o-constructor-e-o-new)
4. [Fase 4: O mesmo método serve os dois artigos](#fase-4-o-mesmo-método-serve-os-dois-artigos)
5. [Fase 5: O método separado do objeto perde o `this`](#fase-5-o-método-separado-do-objeto-perde-o-this)

## O que precisas

- O VS Code e o browser do [laboratório do tema anterior](01-primeira-pagina-com-javascript-laboratorio.md). As mensagens de erro que este laboratório mostra são as do Chrome e do Edge.
- A pasta `primeira-pagina`, desse laboratório, com a página a funcionar. Se não a tiveres, usa o ponto de partida [primeira-pagina](../../exemplos/javascript-orientado-a-objetos/primeira-pagina/README.md), como diz o passo 1 de [Preparar o projeto](#preparar-o-projeto).

## Preparar o projeto

1. Faz uma cópia da página do tema anterior, para a página original ficar como está. Na janela de ficheiros do computador, copia a pasta `primeira-pagina` e cola-a na mesma pasta onde ela está. A cópia aparece com outro nome: muda-o para `inventario-objetos`, sem espaços nem acentos. Se não tiveres a pasta `primeira-pagina`, cria a pasta `inventario-objetos` e abre-a no VS Code, como no passo 2. Depois cria lá os três ficheiros do [ponto de partida](../../exemplos/javascript-orientado-a-objetos/primeira-pagina/README.md), com o conteúdo deles, como diz o "Como correr" do README.

2. Abre a pasta no VS Code. No menu `File`, escolhe `Open Folder...` e seleciona a pasta `inventario-objetos`. O que deves ver: à esquerda, no `Explorer`, o nome da pasta em maiúsculas e, por baixo, o `estilos.css`, o `index.html` e o `inventario.js`.

3. Confirma que a página funciona antes de mudares alguma coisa. Abre o `index.html` com duplo clique, na janela de ficheiros, e abre a consola: botão direito numa parte vazia da página, `Inspecionar` e o separador `Console`. O que deves ver: a página do tema anterior, com `Unidades do caderno A01: 6.`, e a consola sem erros. Um pedido de 2 deixa `Unidades do caderno A01: 4.`. Compara também o teu `inventario.js` com o do ponto de partida: tem de ter só isso. Se tiver mais, por exemplo de um desafio do laboratório anterior, substitui o conteúdo dos três ficheiros pelo do ponto de partida. Se aparecer outra coisa, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

## Fase 1: Um objeto literal junta os dados do artigo

Trocas a variável solta da quantidade por um objeto literal com o código, o nome e a quantidade do caderno, e a página passa a ler as propriedades dele. Rever: [Um objeto literal junta os dados do artigo](../02-do-objeto-literal-a-classe.md#um-objeto-literal-junta-os-dados-do-artigo).

1. Junta os dados do caderno num objeto. No `inventario.js`, substitui estas duas linhas:

   ```js partial
   // A quantidade muda a cada pedido aceite, por isso é let e não const.
   let quantidadeCaderno = 6;
   ```

   por estas:

   ```js partial
   // O caderno passa a ser um objeto: o código, o nome e a quantidade ficam juntos, num só nome.
   const caderno = {
     codigo: "A01",
     nome: "Caderno",
     quantidade: 6
   };
   ```

   Cada propriedade tem um nome, dois pontos e o valor, e as vírgulas separam as propriedades.

2. Põe a página a ler as propriedades do objeto, porque a variável `quantidadeCaderno` deixou de existir. Na função `mostrarQuantidade`, substitui a linha do `textContent` por esta:

   ```js partial
     saida.textContent = caderno.codigo + " " + caderno.nome + ", quantidade: " + caderno.quantidade;
   ```

   Na função `aoCarregarEmRetirar`, substitui a linha `quantidadeCaderno = retirar(quantidadeCaderno, unidades);` por esta:

   ```js partial
     caderno.quantidade = retirar(caderno.quantidade, unidades);
   ```

   A `retirar` continua a receber a quantidade e a devolver a que fica, e agora o resultado guarda-se na propriedade do caderno.

3. Guarda e recarrega a página. O que deves ver: a saída mostra `A01 Caderno, quantidade: 6`, com o código e o nome lidos do objeto.

4. O `caderno` está declarado com `const`, e um pedido aceite muda-lhe a quantidade. Antes de experimentares, prevê: o pedido de 2 vai dar `Assignment to constant variable.`, como no tema anterior? Escreve `2` no campo e carrega em "Retirar".

   O que deves ver: `A01 Caderno, quantidade: 4`, e a consola sem erros. O `const` só impede que o nome `caderno` passe a apontar para outro valor. O objeto continua a ser o mesmo, e as propriedades dele podem mudar.

5. Vê o objeto na consola. Escreve `caderno` e carrega em Enter. Depois escreve `caderno.preco` e carrega em Enter.

   O que deves ver: `{codigo: 'A01', nome: 'Caderno', quantidade: 4}`, com as três propriedades, e depois `undefined`. O objeto não tem a propriedade `preco`, e o JavaScript dá `undefined`, sem mensagem.

6. Provoca um erro de propósito: na função `mostrarQuantidade`, escreve `caderno.quantidde`, sem o "a" depois do "d". Guarda e recarrega.

   O que deves ver: `A01 Caderno, quantidade: undefined`, e nenhuma mensagem na consola. É um erro de lógica: a propriedade `quantidde` não existe, e o JavaScript dá `undefined` em vez de parar. Volta a escrever `caderno.quantidade`, guarda e recarrega.

### Paragem 1

A página abre com `A01 Caderno, quantidade: 6`, e os pedidos funcionam como no tema anterior.

O ficheiro `inventario.js` completo, como deve estar agora:

```js
// inventario.js: o comportamento da página do inventário.
// Guarda a quantidade do caderno A01 e retira unidades quando se carrega no botão.

/**
 * Devolve a quantidade que fica depois de um pedido de retirada.
 * Se o pedido for possível, devolve a quantidade menos as unidades pedidas.
 * Se não for possível, devolve a quantidade que recebeu, sem mudanças.
 * @param {number} quantidade as unidades que existem
 * @param {number} unidades as unidades que se querem retirar
 * @returns {number} a quantidade que fica depois do pedido
 */
function retirar(quantidade, unidades) {
  if (unidades > 0 && unidades <= quantidade) {
    return quantidade - unidades;
  }
  return quantidade;
}

// O caderno passa a ser um objeto: o código, o nome e a quantidade ficam juntos, num só nome.
const caderno = {
  codigo: "A01",
  nome: "Caderno",
  quantidade: 6
};

const campoUnidades = document.querySelector("#unidades");
const botaoRetirar = document.querySelector("#botao-retirar");
const saida = document.querySelector("#resultado");

/**
 * Mostra na saída da página a quantidade atual do caderno.
 * Não devolve nada: muda o texto do elemento de saída.
 */
function mostrarQuantidade() {
  saida.textContent = caderno.codigo + " " + caderno.nome + ", quantidade: " + caderno.quantidade;
}

/**
 * Trata o clique no botão Retirar: lê o campo, faz o pedido e mostra o resultado.
 * Não devolve nada: muda a quantidade do caderno e o texto da saída.
 */
function aoCarregarEmRetirar() {
  // O campo dá sempre texto, como "2", e a retirar espera um número: o Number converte-o no número 2.
  const unidades = Number(campoUnidades.value);
  caderno.quantidade = retirar(caderno.quantidade, unidades);
  mostrarQuantidade();
}

// Sem parênteses: o browser chama a função em cada clique, e não agora.
botaoRetirar.addEventListener("click", aoCarregarEmRetirar);

// A saída começa vazia no HTML; esta chamada mostra a quantidade inicial.
mostrarQuantidade();
```

A função `retirar`, os elementos e a ligação do botão ficaram iguais. Mudaram o estado do caderno, que passou a objeto, e as duas linhas que o usam.

Pensa antes de continuares: o que acontecia se escrevesses, dentro da função `aoCarregarEmRetirar`, a linha `caderno = 4;`? A resposta: o clique parava com `Uncaught TypeError: Assignment to constant variable.`. Essa linha tenta pôr o nome `caderno` a apontar para outro valor, e é isso que o `const` não deixa.

## Fase 2: O método do objeto e o `this`

Passas a regra da função `retirar` para dentro do caderno, como um método, que usa o `this` para chegar à quantidade do objeto. Rever: [O método do objeto e o `this`](../02-do-objeto-literal-a-classe.md#o-método-do-objeto-e-o-this).

1. Acrescenta o método ao objeto. No `inventario.js`, substitui o objeto `caderno`, do comentário que está por cima dele até à chaveta e ao ponto e vírgula do fim, por este:

   ```js partial
   const caderno = {
     codigo: "A01",
     nome: "Caderno",
     quantidade: 6,

     /**
      * Retira unidades a este artigo, se o pedido for possível, e devolve a quantidade que fica.
      * Um pedido impossível deixa a quantidade como estava.
      * @param {number} unidades as unidades que se querem retirar
      * @returns {number} a quantidade que fica depois do pedido
      */
     retirar(unidades) {
       // O this é o objeto que recebeu o pedido: aqui, o caderno.
       if (unidades > 0 && unidades <= this.quantidade) {
         this.quantidade = this.quantidade - unidades;
       }
       return this.quantidade;
     }
   };
   ```

   O `6` ganhou uma vírgula, porque o método fica ao lado das propriedades, e tudo o que está dentro do objeto se separa por vírgulas. A condição é a da função `retirar`, com `this.quantidade` no lugar do parâmetro.

2. Faz o pedido ao método. Na função `aoCarregarEmRetirar`, substitui a linha `caderno.quantidade = retirar(caderno.quantidade, unidades);` por esta:

   ```js partial
     caderno.retirar(unidades);
   ```

3. Apaga a função `retirar` do início do ficheiro, desde o `/**` do JSDoc até à chaveta que fecha a função, e a linha em branco que vem a seguir. A regra passou para o método, e a função já não é usada.

4. Guarda e recarrega. Antes de experimentares, prevê: a linha do passo 2 não guarda nada na quantidade. Um pedido de 2 muda a saída? Faz um pedido de 2 e, depois, um de 5.

   O que deves ver: `A01 Caderno, quantidade: 4` depois do pedido de 2, e o mesmo depois do de 5, que é recusado. A quantidade muda dentro do método, na linha `this.quantidade = this.quantidade - unidades;`, e por isso já não é preciso guardar o resultado.

5. Faz um pedido na consola. Escreve `caderno.retirar(1)` e carrega em Enter.

   O que deves ver: `3`, o valor que o método devolve. A saída da página continua com `4`, porque só muda quando a função `mostrarQuantidade` corre. Faz um pedido de 0 no botão: é recusado, e a saída passa a mostrar `A01 Caderno, quantidade: 3`.

6. Provoca um erro de propósito: na condição do método, apaga o `this.` de `unidades <= this.quantidade`, para ficar `unidades <= quantidade`. Guarda, recarrega e faz um pedido de 2.

   O que deves ver: a página abre bem, mas o clique mostra na consola, apontada à linha 17:

   ```text
   Uncaught ReferenceError: quantidade is not defined
   ```

   A saída fica igual. Sem o `this.`, o JavaScript procura uma variável chamada `quantidade`, e não a propriedade do objeto. É um erro de execução: só aparece quando o método corre, no clique. Volta a escrever `this.quantidade`, guarda e recarrega.

### Paragem 2

A página funciona como na paragem 1, e a regra está agora dentro do caderno.

O ficheiro `inventario.js` completo, como deve estar agora:

```js
// inventario.js: o comportamento da página do inventário.
// Guarda a quantidade do caderno A01 e retira unidades quando se carrega no botão.

const caderno = {
  codigo: "A01",
  nome: "Caderno",
  quantidade: 6,

  /**
   * Retira unidades a este artigo, se o pedido for possível, e devolve a quantidade que fica.
   * Um pedido impossível deixa a quantidade como estava.
   * @param {number} unidades as unidades que se querem retirar
   * @returns {number} a quantidade que fica depois do pedido
   */
  retirar(unidades) {
    // O this é o objeto que recebeu o pedido: aqui, o caderno.
    if (unidades > 0 && unidades <= this.quantidade) {
      this.quantidade = this.quantidade - unidades;
    }
    return this.quantidade;
  }
};

const campoUnidades = document.querySelector("#unidades");
const botaoRetirar = document.querySelector("#botao-retirar");
const saida = document.querySelector("#resultado");

/**
 * Mostra na saída da página a quantidade atual do caderno.
 * Não devolve nada: muda o texto do elemento de saída.
 */
function mostrarQuantidade() {
  saida.textContent = caderno.codigo + " " + caderno.nome + ", quantidade: " + caderno.quantidade;
}

/**
 * Trata o clique no botão Retirar: lê o campo, faz o pedido e mostra o resultado.
 * Não devolve nada: muda a quantidade do caderno e o texto da saída.
 */
function aoCarregarEmRetirar() {
  // O campo dá sempre texto, como "2", e a retirar espera um número: o Number converte-o no número 2.
  const unidades = Number(campoUnidades.value);
  caderno.retirar(unidades);
  mostrarQuantidade();
}

// Sem parênteses: o browser chama a função em cada clique, e não agora.
botaoRetirar.addEventListener("click", aoCarregarEmRetirar);

// A saída começa vazia no HTML; esta chamada mostra a quantidade inicial.
mostrarQuantidade();
```

O objeto `caderno` tem agora os dados e a operação, e a função do clique só lhe faz o pedido. O resto do ficheiro não mudou.

Pensa antes de continuares: dentro do método, porque se escreve `this.quantidade`, e não `caderno.quantidade`, se o objeto é o caderno? A resposta: com `caderno.quantidade`, o método só servia para o caderno. Se copiasses o objeto para fazer a pasta, o método da pasta continuava a mudar o caderno. O `this` é sempre o objeto que recebeu o pedido, seja ele qual for.

## Fase 3: A classe, o `constructor` e o `new`

Trocas o objeto literal pela classe `Artigo`, escrita uma vez para todos os artigos, e crias o caderno com o `new`. Rever: [A classe, o `constructor` e o `new`](../02-do-objeto-literal-a-classe.md#a-classe-o-constructor-e-o-new).

1. Escreve a classe. No `inventario.js`, substitui o objeto `caderno` inteiro, da linha do `const` até à chaveta e ao ponto e vírgula do fim, por isto:

   ```js partial
   /**
    * Um artigo do inventário da sala: um material com código, nome e quantidade.
    */
   class Artigo {
     /**
      * Cria um artigo com os três dados que recebe.
      * @param {string} codigo o código do artigo, como "A01"
      * @param {string} nome o nome do artigo, como "Caderno"
      * @param {number} quantidade as unidades que existem
      */
     constructor(codigo, nome, quantidade) {
       this.codigo = codigo;
       this.nome = nome;
       this.quantidade = quantidade;
     }

     /**
      * Retira unidades a este artigo, se o pedido for possível, e devolve a quantidade que fica.
      * Um pedido impossível deixa a quantidade como estava.
      * @param {number} unidades as unidades que se querem retirar
      * @returns {number} a quantidade que fica depois do pedido
      */
     retirar(unidades) {
       if (unidades > 0 && unidades <= this.quantidade) {
         this.quantidade = this.quantidade - unidades;
       }
       return this.quantidade;
     }
   }

   // O new cria um objeto novo da classe e chama o constructor com estes três valores.
   const caderno = new Artigo("A01", "Caderno", 6);
   ```

   O `constructor` guarda os três valores nas propriedades do objeto novo, como o `__init__` do Python. O método `retirar` é o da fase 2, sem a vírgula antes, porque numa classe os métodos não se separam por vírgulas. A classe fica antes da linha do `new`, porque só existe a partir da linha onde está escrita.

2. Guarda e recarrega. O que deves ver: a página abre com `A01 Caderno, quantidade: 6`, e um pedido de 2 deixa `A01 Caderno, quantidade: 4`, como antes. O resto do script não precisou de mudar, porque a instância tem as mesmas propriedades e o mesmo método do objeto literal.

3. Compara o objeto com o da fase 1. Na consola, escreve `caderno` e carrega em Enter.

   O que deves ver: `Artigo {codigo: 'A01', nome: 'Caderno', quantidade: 4}`. O `Artigo` antes das chavetas diz que o objeto foi feito com a classe `Artigo`.

4. Provoca um erro de propósito: na linha do `new`, apaga a palavra `new`, para ficar `const caderno = Artigo("A01", "Caderno", 6);`. Guarda e recarrega.

   O que deves ver: a saída fica vazia, e a consola mostra, apontada à linha 35:

   ```text
   Uncaught TypeError: Class constructor Artigo cannot be invoked without 'new'
   ```

   A mensagem quer dizer que a classe `Artigo` não pode ser chamada sem o `new`. É um erro de execução: o script parou nessa linha, e nada do que está por baixo correu, nem a quantidade inicial. Volta a pôr o `new`, guarda e recarrega.

### Paragem 3

A página funciona como na paragem 2, agora com o caderno feito a partir da classe `Artigo`.

O ficheiro `inventario.js` completo, como deve estar agora:

```js
// inventario.js: o comportamento da página do inventário.
// Guarda a quantidade do caderno A01 e retira unidades quando se carrega no botão.

/**
 * Um artigo do inventário da sala: um material com código, nome e quantidade.
 */
class Artigo {
  /**
   * Cria um artigo com os três dados que recebe.
   * @param {string} codigo o código do artigo, como "A01"
   * @param {string} nome o nome do artigo, como "Caderno"
   * @param {number} quantidade as unidades que existem
   */
  constructor(codigo, nome, quantidade) {
    this.codigo = codigo;
    this.nome = nome;
    this.quantidade = quantidade;
  }

  /**
   * Retira unidades a este artigo, se o pedido for possível, e devolve a quantidade que fica.
   * Um pedido impossível deixa a quantidade como estava.
   * @param {number} unidades as unidades que se querem retirar
   * @returns {number} a quantidade que fica depois do pedido
   */
  retirar(unidades) {
    if (unidades > 0 && unidades <= this.quantidade) {
      this.quantidade = this.quantidade - unidades;
    }
    return this.quantidade;
  }
}

// O new cria um objeto novo da classe e chama o constructor com estes três valores.
const caderno = new Artigo("A01", "Caderno", 6);

const campoUnidades = document.querySelector("#unidades");
const botaoRetirar = document.querySelector("#botao-retirar");
const saida = document.querySelector("#resultado");

/**
 * Mostra na saída da página a quantidade atual do caderno.
 * Não devolve nada: muda o texto do elemento de saída.
 */
function mostrarQuantidade() {
  saida.textContent = caderno.codigo + " " + caderno.nome + ", quantidade: " + caderno.quantidade;
}

/**
 * Trata o clique no botão Retirar: lê o campo, faz o pedido e mostra o resultado.
 * Não devolve nada: muda a quantidade do caderno e o texto da saída.
 */
function aoCarregarEmRetirar() {
  // O campo dá sempre texto, como "2", e a retirar espera um número: o Number converte-o no número 2.
  const unidades = Number(campoUnidades.value);
  caderno.retirar(unidades);
  mostrarQuantidade();
}

// Sem parênteses: o browser chama a função em cada clique, e não agora.
botaoRetirar.addEventListener("click", aoCarregarEmRetirar);

// A saída começa vazia no HTML; esta chamada mostra a quantidade inicial.
mostrarQuantidade();
```

A classe ocupa o início do ficheiro, e a linha do `new` cria o caderno logo a seguir. Por baixo, a parte da página ficou como na paragem 2.

Pensa antes de continuares: na fase 1, a consola mostrava o caderno com as três propriedades. Se tivesses escrito `caderno` na consola no fim da fase 2, aparecia também `retirar: ƒ`. Porque é que o caderno da classe não mostra o `retirar`? A resposta: no objeto literal, o método está dentro do próprio objeto. Numa instância, o método está na classe, escrito uma vez, e todos os artigos feitos com `new Artigo` o usam a partir de lá.

## Fase 4: O mesmo método serve os dois artigos

Crias o segundo artigo, a pasta A02, com a mesma classe, e pões a página a mostrar os dois artigos, com um botão para cada um. O mesmo método muda o artigo que estiver antes do ponto. Rever: [O mesmo método serve os dois artigos](../02-do-objeto-literal-a-classe.md#o-mesmo-método-serve-os-dois-artigos).

1. Dá à classe um método que descreve o artigo, para a página mostrar os dois da mesma maneira. Na classe `Artigo`, a seguir ao método `retirar` e antes da chaveta que fecha a classe, acrescenta:

   ```js partial

     /**
      * Escreve aqui o JSDoc deste método: o que ele faz, numa frase,
      * e o @returns, com o tipo e um exemplo do texto que devolve.
      */
     descrever() {
       return this.codigo + " " + this.nome + ", quantidade: " + this.quantidade;
     }
   ```

   O JSDoc fica para ti. Substitui as duas linhas do meio pela documentação do método, como a do `retirar`. Escreve o que o método faz, numa frase, e uma linha `@returns`, com o tipo do valor entre chavetas e um exemplo do texto. O método não tem parâmetros, por isso não leva `@param`.

2. Cria o segundo artigo, a pasta A02. A seguir à linha `const caderno = new Artigo("A01", "Caderno", 6);`, acrescenta:

   ```js partial
   const pasta = new Artigo("A02", "Pasta", 2);
   ```

   Guarda e recarrega. O que deves ver: a página igual, porque ainda nada mostra a pasta.

3. Experimenta o mesmo método nos dois objetos. Antes de experimentares, prevê: depois de `pasta.retirar(1)`, o que mostram `caderno.descrever()` e `pasta.descrever()`? Escreve as três linhas na consola, uma de cada vez, com Enter.

   O que deves ver: `1`, depois `'A01 Caderno, quantidade: 6'` e `'A02 Pasta, quantidade: 1'`. No pedido, o `this` era a pasta, e só a quantidade dela mudou. No `descrever`, o `this` foi primeiro o caderno e depois a pasta, e o mesmo método deu o texto de cada um.

4. Põe a página a mostrar os dois artigos, cada um na sua saída. No `index.html`, substitui o parágrafo da saída, `<p>` com o `output` dentro, por estes dois:

   ```html
         <p>
           <output id="saida-caderno"></output>
         </p>
         <p>
           <output id="saida-pasta"></output>
         </p>
   ```

   No `inventario.js`, substitui a linha `const saida = document.querySelector("#resultado");` por estas duas:

   ```js partial
   const saidaCaderno = document.querySelector("#saida-caderno");
   const saidaPasta = document.querySelector("#saida-pasta");
   ```

   Ainda no `inventario.js`, substitui a função `mostrarQuantidade` inteira, com o JSDoc dela, por esta, que mostra os dois artigos:

   ```js partial
   /**
    * Mostra na página a descrição dos dois artigos, cada uma na sua saída.
    * Não devolve nada: muda o texto das duas saídas.
    */
   function mostrarArtigos() {
     saidaCaderno.textContent = caderno.descrever();
     saidaPasta.textContent = pasta.descrever();
   }
   ```

   A função mudou de nome, por isso muda também as duas chamadas. Na função `aoCarregarEmRetirar`, `mostrarQuantidade();` passa a `mostrarArtigos();`. No fim do ficheiro, substitui as duas últimas linhas, o comentário e a chamada, por estas:

   ```js partial
   // As saídas começam vazias no HTML; esta chamada mostra os dois artigos ao abrir.
   mostrarArtigos();
   ```

   Guarda os dois ficheiros e recarrega. O que deves ver: duas linhas, `A01 Caderno, quantidade: 6` e `A02 Pasta, quantidade: 2`. Um pedido de 2 no botão muda só a do caderno, porque a função do clique ainda só faz pedidos ao caderno.

5. Acrescenta o botão da pasta. No `index.html`, substitui o parágrafo do botão por este, com um botão para cada artigo:

   ```html
         <p>
           <button id="botao-caderno" type="button">Retirar do caderno</button>
           <button id="botao-pasta" type="button">Retirar da pasta</button>
         </p>
   ```

   No mesmo ficheiro, substitui a linha do primeiro parágrafo, a que começa por `<p>O caderno A01 começa com 6 unidades.`, por esta, que fala dos dois artigos:

   ```html
         <p>O caderno A01 começa com 6 unidades, e a pasta A02 com 2. Escreve quantas unidades queres retirar e carrega no botão do artigo.</p>
   ```

   No `inventario.js`, substitui a linha `const botaoRetirar = document.querySelector("#botao-retirar");` por estas duas:

   ```js partial
   const botaoCaderno = document.querySelector("#botao-caderno");
   const botaoPasta = document.querySelector("#botao-pasta");
   ```

   Ainda não recarregues: o fim do script ainda liga o `botaoRetirar`, que deixou de existir, e o passo seguinte trata disso.

6. Dá a cada botão a sua função. No `inventario.js`, substitui a função `aoCarregarEmRetirar` inteira, com o JSDoc dela, por estas duas:

   ```js partial
   /**
    * Trata o clique no botão do caderno: retira ao caderno as unidades escritas no campo.
    * Não devolve nada: muda a quantidade do caderno e o texto das saídas.
    */
   function aoCarregarNoCaderno() {
     const unidades = Number(campoUnidades.value);
     // O caderno está antes do ponto, por isso é o this do método: só a quantidade dele muda.
     caderno.retirar(unidades);
     mostrarArtigos();
   }

   /**
    * Trata o clique no botão da pasta: retira à pasta as unidades escritas no campo.
    * Não devolve nada: muda a quantidade da pasta e o texto das saídas.
    */
   function aoCarregarNaPasta() {
     const unidades = Number(campoUnidades.value);
     pasta.retirar(unidades);
     mostrarArtigos();
   }
   ```

   Depois, substitui as duas linhas que ligam o botão, o comentário e o `addEventListener`, por estas três:

   ```js partial
   // Cada botão recebe uma função que lê o campo e faz o pedido, e não o método: assim o this é o artigo.
   botaoCaderno.addEventListener("click", aoCarregarNoCaderno);
   botaoPasta.addEventListener("click", aoCarregarNaPasta);
   ```

   Por fim, a segunda linha do início do ficheiro ainda fala só do caderno. Substitui-a por esta:

   ```js partial
   // Cada artigo é um objeto da classe Artigo, e cada botão retira unidades a um deles.
   ```

7. Guarda os dois ficheiros e recarrega. Faz esta sequência de pedidos, sem recarregar entre eles, e confirma as duas saídas depois de cada um:

   | Pedido | Escreves no campo | Carregas em | A saída do caderno | A saída da pasta |
   | --- | --- | --- | --- | --- |
   | 1 | `2` | Retirar do caderno | `A01 Caderno, quantidade: 4` | `A02 Pasta, quantidade: 2` |
   | 2 | `2` | Retirar da pasta | `A01 Caderno, quantidade: 4` | `A02 Pasta, quantidade: 0` |
   | 3 | `1` | Retirar da pasta | `A01 Caderno, quantidade: 4` | `A02 Pasta, quantidade: 0` |
   | 4 | `5` | Retirar do caderno | `A01 Caderno, quantidade: 4` | `A02 Pasta, quantidade: 0` |
   | 5 | `4` | Retirar do caderno | `A01 Caderno, quantidade: 0` | `A02 Pasta, quantidade: 0` |

   Os pedidos 3 e 4 são recusados. Em cada pedido, só a saída do artigo do botão pode mudar, porque cada função faz o pedido a um artigo só.

### Paragem 4

A página mostra os dois artigos, e cada botão retira unidades ao seu. Os pedidos impossíveis deixam as quantidades iguais.

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
        <output id="saida-caderno"></output>
      </p>
      <p>
        <output id="saida-pasta"></output>
      </p>
    </main>
  </body>
</html>
```

O ficheiro `inventario.js` completo. No teu, as duas linhas do meio do JSDoc do `descrever` já têm a tua documentação:

```js
// inventario.js: o comportamento da página do inventário.
// Cada artigo é um objeto da classe Artigo, e cada botão retira unidades a um deles.

/**
 * Um artigo do inventário da sala: um material com código, nome e quantidade.
 */
class Artigo {
  /**
   * Cria um artigo com os três dados que recebe.
   * @param {string} codigo o código do artigo, como "A01"
   * @param {string} nome o nome do artigo, como "Caderno"
   * @param {number} quantidade as unidades que existem
   */
  constructor(codigo, nome, quantidade) {
    this.codigo = codigo;
    this.nome = nome;
    this.quantidade = quantidade;
  }

  /**
   * Retira unidades a este artigo, se o pedido for possível, e devolve a quantidade que fica.
   * Um pedido impossível deixa a quantidade como estava.
   * @param {number} unidades as unidades que se querem retirar
   * @returns {number} a quantidade que fica depois do pedido
   */
  retirar(unidades) {
    if (unidades > 0 && unidades <= this.quantidade) {
      this.quantidade = this.quantidade - unidades;
    }
    return this.quantidade;
  }

  /**
   * Escreve aqui o JSDoc deste método: o que ele faz, numa frase,
   * e o @returns, com o tipo e um exemplo do texto que devolve.
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
 * Trata o clique no botão do caderno: retira ao caderno as unidades escritas no campo.
 * Não devolve nada: muda a quantidade do caderno e o texto das saídas.
 */
function aoCarregarNoCaderno() {
  const unidades = Number(campoUnidades.value);
  // O caderno está antes do ponto, por isso é o this do método: só a quantidade dele muda.
  caderno.retirar(unidades);
  mostrarArtigos();
}

/**
 * Trata o clique no botão da pasta: retira à pasta as unidades escritas no campo.
 * Não devolve nada: muda a quantidade da pasta e o texto das saídas.
 */
function aoCarregarNaPasta() {
  const unidades = Number(campoUnidades.value);
  pasta.retirar(unidades);
  mostrarArtigos();
}

// Cada botão recebe uma função que lê o campo e faz o pedido, e não o método: assim o this é o artigo.
botaoCaderno.addEventListener("click", aoCarregarNoCaderno);
botaoPasta.addEventListener("click", aoCarregarNaPasta);

// As saídas começam vazias no HTML; esta chamada mostra os dois artigos ao abrir.
mostrarArtigos();
```

A classe vem primeiro, com os três métodos, e logo a seguir os dois artigos. Por baixo, os elementos, a função que mostra os artigos e as duas funções dos cliques, e no fim as ligações e a chamada que mostra os artigos ao abrir.

Pensa antes de continuares: as duas funções dos cliques têm as mesmas três linhas, e só muda o objeto antes do ponto. Onde está escrita a regra de um pedido, e quantas vezes? A resposta: uma só vez, no método `retirar` da classe. As duas funções só dizem a que artigo se faz o pedido, e o `this` faz o resto.

## Fase 5: O método separado do objeto perde o `this`

Separas o método do seu objeto, na consola e no botão da pasta, e vês o `this` deixar de ser o artigo. Rever: [O método separado do objeto perde o `this`](../02-do-objeto-literal-a-classe.md#o-método-separado-do-objeto-perde-o-this).

1. Separa o método do caderno, na consola. Recarrega a página e escreve, uma linha de cada vez, com Enter:

   ```js partial
   const retirarSolto = caderno.retirar;
   retirarSolto(2);
   ```

   O que deves ver, depois da segunda linha:

   ```text
   Uncaught TypeError: Cannot read properties of undefined (reading 'quantidade')
   ```

   A mensagem quer dizer que não se conseguem ler propriedades de `undefined`, e que se queria ler a `quantidade`. O `retirarSolto` é o método, mas sem o caderno: na chamada não há nada antes do ponto, e o `this` fica `undefined`.

2. Agora dá o método diretamente ao botão da pasta, um engano frequente. No `inventario.js`, muda a linha `botaoPasta.addEventListener("click", aoCarregarNaPasta);` para esta:

   ```js partial
   botaoPasta.addEventListener("click", pasta.retirar);
   ```

   Guarda e recarrega. Escreve `1` no campo. Antes de experimentares, prevê: o que acontece quando carregas em "Retirar da pasta"? Experimenta.

   O que deves ver: a saída da pasta continua com `A02 Pasta, quantidade: 2`, e a consola não mostra mensagem nenhuma. Na consola, `pasta.quantidade` dá `2`: o pedido não mudou a pasta. É um erro de lógica: não há mensagem, e o resultado está errado.

3. Descobre o que o método recebe nesse clique, com a rotina da depuração. A hipótese: o `this` do método não é a pasta. No método `retirar`, logo a seguir à linha `retirar(unidades) {`, acrescenta esta linha, que mostra o `this` e as `unidades`:

   ```js partial
       console.log(this, unidades);
   ```

   Guarda, recarrega e carrega em "Retirar da pasta".

   O que deves ver: a consola mostra o botão, `<button id="botao-pasta" type="button">Retirar da pasta</button>`, e, a seguir, um objeto `PointerEvent`, com a informação do clique. Quando há um clique, é o browser que chama o método. Dá-lhe como `this` o botão e, como `unidades`, o próprio clique, e não o número do campo, que ninguém leu. A condição dá `false` logo em `unidades > 0`, e nenhum artigo muda. Carrega também em "Retirar do caderno": a consola mostra o objeto do caderno e o `1`. A função `aoCarregarNoCaderno` lê o campo e chama o método com o caderno antes do ponto.

4. Desfaz as duas alterações. Apaga a linha do `console.log(this, unidades);` e volta a pôr `botaoPasta.addEventListener("click", aoCarregarNaPasta);`. Guarda e recarrega. O que deves ver: um pedido de 1 na pasta deixa `A02 Pasta, quantidade: 1`.

### Paragem 5

A página está completa, e os ficheiros estão como na paragem 4. Cada botão chama uma função tua, e essa função faz o pedido ao artigo, com ele antes do ponto.

Pensa antes de terminares: porque é que a função `aoCarregarNaPasta` resolve o problema do passo 2? A resposta: o browser chama a função, e não o método. A função lê o campo e faz o pedido com a pasta antes do ponto, na linha `pasta.retirar(unidades);`. Por isso, o `this` do método é a pasta, e `unidades` é o número escrito.

## Se alguma coisa falhar

1. O VS Code tem aberta a pasta `inventario-objetos`, e não a `primeira-pagina`? A barra lateral mostra o nome da pasta, em maiúsculas. Se for outra, abre a certa como no passo 2 de [Preparar o projeto](#preparar-o-projeto).
2. Guardaste os dois ficheiros? Nos passos que mudam o `index.html` e o `inventario.js`, os dois têm de ficar guardados antes de recarregares. Um separador com uma bola no lugar da cruz tem alterações por guardar.
3. Recarregaste a página, na janela do browser? A página não muda sozinha. O endereço do separador tem de acabar em `inventario-objetos/index.html`, e não na página do tema anterior.
4. A consola mostra algum erro? Lê a mensagem a vermelho e procura-a nos problemas desta secção.
5. Desfizeste o último erro provocado? Cada passo conta com os ficheiros sem o erro. Se não souberes onde estás, copia o último ficheiro completo do laboratório e refaz os passos seguintes.

### A consola mostra `Uncaught SyntaxError: Unexpected identifier`

É um erro de escrita: o script não corre nenhuma linha. A mensagem diz, entre plicas, o nome que o browser não esperava, como `'retirar'`. Num objeto literal, falta quase sempre a vírgula no fim da propriedade que vem antes desse nome. Se o nome for o de um método, procura a última propriedade antes do JSDoc dele, como o `6` da fase 2.

### A consola mostra `Uncaught ReferenceError: Cannot access 'Artigo' before initialization`

A linha do `new` está acima da classe. Uma classe só existe a partir da linha onde está escrita. Põe a classe no início do ficheiro, como na paragem 3, e as linhas do `new` logo a seguir.

### A consola mostra `Uncaught TypeError: Class constructor Artigo cannot be invoked without 'new'`

Falta o `new` antes de `Artigo`, na linha que a mensagem indica. Escreve-o, como em `new Artigo("A01", "Caderno", 6)`.

### A consola mostra `Uncaught ReferenceError: quantidade is not defined`, ao carregar num botão

Dentro do método `retirar`, falta o `this.` antes de `quantidade`. Põe o `this.` antes de cada `quantidade` do método.

### A consola mostra `Uncaught ReferenceError`, com um nome antigo, como `mostrarQuantidade is not defined`

Na fase 4, quatro nomes mudaram: `saida`, `botaoRetirar`, `mostrarQuantidade` e `aoCarregarEmRetirar`. Ficou uma linha com o nome antigo, que a mensagem indica. Com `botaoRetirar`, as duas saídas ficam vazias, porque o script para antes de as mostrar. Com `mostrarQuantidade`, a mensagem aparece ao abrir a página, se for a última linha do ficheiro, ou ao carregar no botão, se for a função do clique. Troca o nome antigo pelo novo, como nos passos 4 a 6 da fase 4.

### A consola mostra `Uncaught TypeError: Cannot read properties of null` ou `Cannot set properties of null`

O `querySelector` de um elemento não o encontrou e devolveu `null`. Na fase 4, os `id` mudaram nos dois ficheiros. Confirma que guardaste o `index.html` e que cada seletor do script, como `"#saida-pasta"`, é igual ao `id` do HTML, letra a letra. Na consola, o nome do `const`, como `saidaPasta`, mostra `null` quando o elemento não foi encontrado.

### A consola mostra `Uncaught TypeError: caderno.retira is not a function`

O nome do método, na chamada, não é igual ao da classe. Compara-os letra a letra: `retirar` e `descrever`, com as letras todas.

### Um botão não faz nada, e a consola não mostra erros

Confirma primeiro que o pedido é possível: um pedido recusado deixa a saída igual. Se o pedido devia ser aceite, vê a linha do `addEventListener` desse botão. Tem de receber o nome de uma das tuas funções, sem parênteses, e não o método de um artigo, como `pasta.retirar`.

### A saída mostra `undefined`

Uma propriedade está mal escrita, no `descrever` ou na linha do `textContent`, como `quantidde` em vez de `quantidade`. O JavaScript não para por causa de uma propriedade que não existe: dá `undefined`. Compara o nome com o da propriedade onde ela é criada: no objeto literal ou no `constructor`.

## Desafios

1. Um terceiro artigo. Acrescenta à página a régua A03, que começa com 10 unidades, com o seu botão e a sua saída. Depois responde, num comentário no fim do `inventario.js`: o que tiveste de acrescentar à classe, e o que tiveste de acrescentar fora dela? Compara com o que acrescentaste, ou terias de acrescentar, para a pasta no desafio 3 do laboratório do tema anterior. Pista: conta as linhas novas dentro da chaveta da classe e as linhas novas fora dela.
2. O método `adicionar`. Acrescenta à classe um método `adicionar(unidades)`, com JSDoc, que soma unidades ao artigo, só quando o pedido é positivo, e devolve a quantidade que fica. Testa-o na consola nos dois artigos, com um pedido de 3, um de 0 e um de -2, antes de lhe ligares um botão "Adicionar ao caderno". Pista: o `retirar` tem uma condição com duas partes, e este método só precisa de uma delas.
3. Uma função para os dois botões. As funções `aoCarregarNoCaderno` e `aoCarregarNaPasta` repetem as mesmas linhas. Escreve uma função `retirarDoCampo(artigo)`, com JSDoc, que recebe um artigo, lê o campo, faz-lhe o pedido e mostra os artigos. Muda as duas funções dos cliques para que cada uma seja só uma chamada a `retirarDoCampo`, com o seu artigo. A página tem de dar a mesma sequência do passo 7 da fase 4. Pista: dentro da função nova, o artigo que recebe é o que fica antes do ponto, na chamada ao método.

## Antes de terminares

- [ ] A pasta `inventario-objetos` tem o `index.html`, o `estilos.css` e o `inventario.js`, e a página abre com um duplo clique.
- [ ] A página do tema anterior, na pasta `primeira-pagina`, continua como estava.
- [ ] A consola não mostra erros depois de a página abrir.
- [ ] A sequência do passo 7 da fase 4 dá as saídas da tabela, com cada botão a mudar só o seu artigo.
- [ ] O método `descrever` tem o JSDoc que escreveste, com o que faz e o `@returns`.
- [ ] Sabes que tipo de erro é cada um dos que provocaste: a propriedade mal escrita, o `this` esquecido, o `new` em falta e o método dado ao botão.
- [ ] Sabes explicar, com a pasta e o caderno, quem é o `this` em cada pedido e porque é que um botão recebe uma função tua, e não o método.

![Rodapé](../../imagens/rodape.png)

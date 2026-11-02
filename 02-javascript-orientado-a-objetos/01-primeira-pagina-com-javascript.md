![Cabeçalho](../imagens/cabecalho.png)

# A primeira página com JavaScript

Módulo M11, Introdução à Linguagem de Programação Orientada por Objetos. Neste guia fazes a tua primeira página web e escreves o teu primeiro programa em JavaScript, a partir do que já sabes de Python. Lês o guia ao teu ritmo, de preferência em mais do que uma vez, e o que não acabares na aula acabas em casa ou na aula seguinte. Para praticar, há o [laboratório](01-primeira-pagina-com-javascript-laboratorio.md) e a [ficha de exercícios](01-primeira-pagina-com-javascript-exercicios.md) deste tema.

No M10, os teus programas de Python corriam no editor e mostravam texto com o `print`. Neste tema, o programa ganha uma página, com um campo para escrever e um botão para carregar, e passa a correr no browser. A linguagem que dá comportamento à página é o JavaScript. O JavaScript não vem substituir o Python, nem é uma versão mais difícil dele: é outra ferramenta, feita para correr dentro das páginas que o browser mostra. Este tema ainda não usa classes em JavaScript, que são o assunto do tema 02. A página também ainda não recusa números decimais, o que fica para o tema 03.

## Neste guia

1. O que vais aprender
2. O que já sabes e vais usar
3. O que muda quando o programa corre no browser
4. O HTML dá a estrutura da página
5. Rótulo, campo, botão e saída
6. O CSS dá a apresentação
7. Contraste e foco visível
8. O JavaScript entra pela etiqueta `script`
9. Variáveis com `const` e `let`
10. Números, textos e valores lógicos
11. Operadores
12. Decisões com `if` e `else`
13. Funções com `function` e `return`
14. Ciclos: `for`, `while` e `for...of`
15. Comentários que explicam a intenção
16. Ligar um botão a uma função
17. Quando a página não faz o que devia
18. Exemplo guiado: retirar unidades do caderno na página
19. Erros frequentes
20. Palavras novas deste guia
21. Verificar o que aprendeste
22. O que vem a seguir
23. Para saber mais

## O que vais aprender

No fim deste guia, consegues:

- dizer o que fazem o editor, o browser, o HTML, o CSS e o JavaScript numa página, e onde corre cada coisa;
- escrever uma página em HTML com um título, um parágrafo, um campo com o seu rótulo, um botão e uma saída;
- dar à página um aspeto legível com uma folha de estilos, com bom contraste e com o foco visível para quem usa o teclado;
- ligar um ficheiro de JavaScript à página e ler, na consola do browser, os resultados e as mensagens de erro;
- traduzir para JavaScript uma função que já conheces em Python, com `const`, `let`, operadores, `if` e ciclos;
- fazer um botão da página chamar uma função tua e mostrar o resultado na página.

## O que já sabes e vais usar

- Variáveis e atribuição, números, textos entre aspas e o `print`: do 10.º ano.
- Os operadores aritméticos (`+`, `-`, `*`, `/`, `//`, `%`, `**`), os de comparação (`==`, `!=`, `<`, `>`, `<=`, `>=`) e as palavras `and`, `or` e `not`: do 10.º ano.
- As condições com `if`, `elif` e `else`: do 10.º ano.
- Os ciclos `for` e `while`, e o `range`: do 10.º ano.
- As listas, com os valores entre parênteses retos, o índice a começar em 0 e o `len`: do 10.º ano.
- As funções com `def`, os parâmetros e o `return`: do 10.º ano, e revistas no guia [01 Entidades, estado e ações](../01-programacao-orientada-objetos/01-entidades-estado-acoes.md), em "Duas maneiras de organizar um programa".
- A docstring, o texto que explica o que uma função faz: guia [01 Entidades, estado e ações](../01-programacao-orientada-objetos/01-entidades-estado-acoes.md), na mesma secção.
- A função `retirar(quantidade, unidades)` e os dois pedidos ao caderno A01, que começa com 6 unidades. Retirar 2 deixa 4, e a seguir um pedido de 5 é recusado e deixa as 4. Guia [01 Entidades, estado e ações](../01-programacao-orientada-objetos/01-entidades-estado-acoes.md), na mesma secção.
- O artigo do inventário, com código, nome e quantidade: guia [02 Objetos, classes e instâncias](../01-programacao-orientada-objetos/02-objetos-classes-instancias.md), em "O que estamos a representar".
- O `None`, o valor que uma função de Python devolve quando não tem `return`: [laboratório 01 do M10](../01-programacao-orientada-objetos/01-entidades-estado-acoes-laboratorio.md), em "Problemas frequentes".
- Os três tipos de erro, de escrita, de execução e de lógica: guia [03 Encapsulamento e contratos](../01-programacao-orientada-objetos/03-encapsulamento-contratos.md), em "Nada impede uma quantidade impossível".
- Criar uma pasta e um ficheiro, dar-lhes um nome sem espaços nem acentos e guardar o ficheiro: dos laboratórios do M10.

Do HTML, do CSS e do JavaScript, este guia não dá nada por sabido. Explica tudo desde o princípio.

## O que muda quando o programa corre no browser

Até aqui, escrevias um programa de Python num ficheiro `.py`, mandavas executá-lo e lias o resultado no editor. O mesmo programa fazia tudo: guardava os dados, fazia as contas e mostrava o texto. Uma página web divide esse trabalho por três ficheiros, cada um escrito numa linguagem diferente.

A página que vais construir neste tema, no exemplo guiado e no laboratório, é o inventário da sala, com o caderno A01. Tem esta árvore de pastas:

```text
primeira-pagina/
├── index.html
├── estilos.css
└── inventario.js
```

Cada ficheiro tem um papel:

- O `index.html` está escrito em **HTML** e diz o que a página tem: um título, um parágrafo, um campo, um botão. É a estrutura da página.
- O `estilos.css` está escrito em **CSS** e diz como a página se apresenta: o tipo de letra, as cores, os espaços. É a apresentação.
- O `inventario.js` está escrito em **JavaScript** e diz o que a página faz quando alguém a usa: ler o campo, fazer a conta, mostrar o resultado. É o comportamento.

Pensa numa ficha de inscrição em papel, na secretaria da escola. O que está impresso na ficha, os títulos e os espaços para preencher, é o HTML. O tipo de letra, as cores e a arrumação da folha são o CSS. O que a pessoa da secretaria faz quando lhe entregas a ficha, verificar os dados e dar-te uma resposta, é o JavaScript.

Para trabalhar com estes ficheiros usas dois programas diferentes. O **editor** é o programa onde escreves e guardas os ficheiros, como o VS Code. O editor não mostra a página como ela fica, nem corre o JavaScript dela. O **browser** (em português, navegador) é o programa que abre páginas, como o Chrome, o Edge ou o Firefox. O browser lê os três ficheiros, mostra a página e corre o JavaScript. É no browser que o teu programa de JavaScript corre, e não no editor.

### Abrir a página

Para abrir a página, fazes duplo clique no ficheiro `index.html`, na janela de ficheiros do computador: o Explorador de Ficheiros, no Windows, ou o Finder, no macOS. O computador abre o ficheiro no browser. Repara que o duplo clique no nome do ficheiro dentro do VS Code faz outra coisa: abre o ficheiro para o editares. No VS Code, para encontrares a pasta na janela de ficheiros, carregas com o botão direito no nome do ficheiro e escolhes `Reveal in File Explorer`, no Windows, ou `Reveal in Finder`, no macOS.

Com a página aberta, a barra de endereço do browser mostra um endereço que começa por `file:///`, seguido do caminho da pasta no teu computador. A palavra `file` (em inglês, ficheiro) quer dizer que o browser está a mostrar um ficheiro deste computador. A página não foi para a internet, e ninguém mais a vê.

### Editar, guardar e recarregar

Quando mudas um ficheiro no editor, a página aberta no browser não muda sozinha. Há sempre três passos:

1. Mudas o ficheiro no editor.
2. Guardas o ficheiro, com Ctrl+S no Windows ou Cmd+S no macOS. No VS Code, o separador de um ficheiro por guardar mostra uma bola branca no lugar da cruz de fechar.
3. Recarregas a página no browser, com F5 ou Ctrl+R no Windows, ou com Cmd+R no macOS.

O browser mostra os ficheiros tal como estavam guardados no momento em que carregaste a página. Se te esqueceres de guardar ou de recarregar, vês a versão antiga e pensas que a tua alteração não fez nada.

Recarregar a página tem outro efeito, parecido com executar outra vez um programa de Python. O JavaScript da página volta a correr desde a primeira linha, com os valores iniciais que estão escritos no ficheiro. Se o caderno começa com 6 unidades e já retiraste algumas, ao recarregar volta a ter 6.

### Os nomes e os caminhos dos ficheiros

Os nomes dos ficheiros escrevem-se em minúsculas, sem espaços e sem acentos, para não darem problemas em nenhum computador. A extensão, a parte depois do ponto, diz ao computador que tipo de ficheiro é: `.html`, `.css` ou `.js`. Cria os ficheiros sempre no VS Code, que mostra o nome inteiro, com a extensão. Alguns programas de texto acrescentam `.txt` sem avisar, e um ficheiro chamado `index.html.txt` não é uma página: o computador abre-o como texto.

A página vai precisar de dizer onde estão os outros dois ficheiros. Escreve-o com um **caminho relativo**, um caminho que parte da pasta onde está a página. O caminho `estilos.css`, sozinho, quer dizer "o ficheiro `estilos.css` que está na mesma pasta que esta página". Se o ficheiro estivesse numa pasta `css`, ao lado da página, o caminho seria `css/estilos.css`. O nome no caminho tem de ser exatamente o nome do ficheiro, letra a letra.

## O HTML dá a estrutura da página

O browser precisa de saber o que é cada parte do texto que vai mostrar: um título, um parágrafo, um campo. Num ficheiro de texto simples, tudo é texto igual. O HTML resolve isto marcando cada parte com o que ela é.

Uma parte marcada chama-se um **elemento**. Um elemento escreve-se com uma **etiqueta** de abertura, o conteúdo e uma etiqueta de fecho. A etiqueta de abertura é o nome do elemento entre `<` e `>`, como `<h1>`. A de fecho tem uma barra antes do nome, como `</h1>`. O elemento `<h1>Inventário da sala</h1>` diz ao browser que "Inventário da sala" é o título principal da página. Em inglês, a etiqueta diz-se *tag*, e vais ver muitas vezes essa palavra.

Antes de abrires esta página no browser, tenta prever: que texto aparece no separador do browser, lá em cima, e que texto aparece dentro da página?

```html
<!doctype html>
<html lang="pt-PT">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Inventário da sala</title>
  </head>
  <body>
    <main>
      <h1>Inventário da sala</h1>
      <p>O caderno A01 começa com 6 unidades.</p>
    </main>
  </body>
</html>
```

O resultado é este. No separador do browser aparece "Inventário da sala". Dentro da página aparece o título "Inventário da sala", em letra grande e grossa, e por baixo o parágrafo "O caderno A01 começa com 6 unidades.", em letra normal. Nada do que está dentro de `<head>` aparece na página, porque o `head` guarda informação sobre a página, e não conteúdo.

Leitura guiada: lê a página de fora para dentro, como caixas dentro de caixas.

- A primeira linha, `<!doctype html>`, diz ao browser que a página usa o HTML atual. Escreve-se sempre igual, no início.
- O elemento `html` contém a página inteira. O `lang="pt-PT"` diz que a página está em português de Portugal. Os programas que leem a página em voz alta usam esta informação para pronunciar bem as palavras.
- O `head` (em inglês, cabeça) guarda informação sobre a página, que não aparece no meio dela. O `meta charset="utf-8"` diz como estão guardadas as letras, e é o que faz os acentos aparecerem bem. O `meta name="viewport"` faz um telemóvel mostrar a página à largura do ecrã, em vez de a mostrar em miniatura. O `title` é o texto do separador.
- O `body` (em inglês, corpo) contém o que aparece na página.
- O `main` (em inglês, principal) marca o conteúdo principal da página.
- O `h1` é o título principal. O `h` vem de *heading* (título), e o `1` diz que é o título de primeiro nível. Há `h2` para os subtítulos, e assim por diante.
- O `p` é um parágrafo.

Dentro da etiqueta de abertura podem vir **atributos**: informação extra sobre o elemento, na forma `nome="valor"`. No exemplo, `lang="pt-PT"` é um atributo do elemento `html`, e `charset="utf-8"` é um atributo do `meta`. O elemento `meta` não tem conteúdo nem etiqueta de fecho. Há poucos elementos assim, e este guia diz sempre quando aparece um.

Repara em duas diferenças em relação ao Python. A primeira é a indentação. No HTML, os espaços no início das linhas servem só para as pessoas verem que caixa está dentro de que caixa: o browser ignora-os. Escrevemo-los na mesma, porque sem eles uma página fica muito difícil de ler. A segunda diferença é mais importante. O Python para e mostra uma mensagem quando encontra um erro de escrita. O browser não faz isso com o HTML: tenta mostrar a página na mesma, como conseguir. Se te esqueceres de uma etiqueta de fecho, não aparece nenhuma mensagem, e a página simplesmente fica diferente do que esperavas. É por isso que vale a pena prever o que vais ver antes de abrires a página.

## Rótulo, campo, botão e saída

A página do inventário tem de perguntar quantas unidades se querem retirar e de mostrar o que fica. Para isso, o HTML tem elementos próprios para receber e mostrar informação. O campo e o botão são **controlos**, as partes da página com que a pessoa interage. O rótulo e a saída acompanham-nos.

Este excerto entra dentro do `main` da página anterior, por baixo do parágrafo. Não é uma página completa: no exemplo guiado vês a página inteira.

```html
<p>
  <label for="unidades">Unidades a retirar</label>
  <input id="unidades" type="text">
</p>
<p>
  <button id="botao-retirar" type="button">Retirar</button>
</p>
<p>
  <output id="resultado"></output>
</p>
```

Antes de experimentares, tenta prever duas coisas: o que acontece quando clicas no texto "Unidades a retirar", e o que acontece quando carregas no botão "Retirar". A resposta: ao clicares no texto, o cursor aparece dentro do campo, pronto para escreveres. Ao carregares no botão, não acontece nada. Ninguém disse ainda à página o que fazer com o botão: isso é o trabalho do JavaScript.

Leitura guiada: lê o excerto elemento a elemento.

- O `input` (em inglês, entrada) é o **campo**: a caixa onde a pessoa escreve. Também não tem etiqueta de fecho: nunca se escreve `</input>`. O atributo `type="text"` diz que aceita qualquer texto. Há outros tipos de campo, por exemplo para números, mas cada browser trata-os de maneira um pouco diferente. Com `type="text"`, todos os browsers se comportam da mesma maneira, e é o JavaScript que converte o texto em número.
- O atributo `id` (de identificador) dá ao elemento um nome único dentro da página. Dois elementos da mesma página nunca têm o mesmo `id`. Escreve-o em minúsculas e sem espaços, com hífen entre as palavras, como os nomes dos ficheiros.
- O `label` (em inglês, rótulo) é o **rótulo** do campo: o texto que diz o que se escreve lá. O atributo `for` (em inglês, para) liga o rótulo ao campo: o valor de `for` é o `id` do campo. É esta ligação que faz o clique no rótulo pôr o cursor no campo. Faz também outra coisa, que não se vê. Um **leitor de ecrã**, o programa que lê a página em voz alta a quem não vê bem, diz o texto do rótulo quando a pessoa chega ao campo. Sem a ligação, a pessoa ouve apenas "campo de texto" e não sabe o que escrever.
- O `button` é o **botão**: um elemento que faz uma ação na página. O atributo `type="button"` diz que é um botão simples, que só faz o que o JavaScript mandar.
- O `output` (em inglês, saída) é a **saída**: o sítio da página onde aparece um resultado. Começa vazio. Muitos browsers avisam o leitor de ecrã quando o texto da saída muda, e por isso quem não vê a página fica a saber o resultado.
- Cada `p` põe a sua parte numa linha própria, com um espaço por cima e por baixo. Sem os `p`, o rótulo, o campo, o botão e a saída apareciam todos seguidos na mesma linha.

### Usar a página só com o teclado

Há pessoas que não usam o rato, por escolha ou por necessidade. Uma página tem de se poder usar só com o teclado. O elemento que recebe as teclas que carregas, num dado momento, tem o **foco**. A tecla Tab passa o foco para o controlo seguinte, e Shift+Tab volta ao anterior. Com o foco no campo, o que escreves entra no campo. Com o foco no botão, a tecla Enter ou a barra de espaço carregam no botão. Os elementos `input` e `button` já fazem tudo isto sem nenhum trabalho teu. É uma das razões para usar cada elemento pela sua função: um botão a sério, e não um parágrafo com aspeto de botão.

Um erro frequente é pôr a explicação dentro do campo, com o atributo `placeholder`, em vez de um rótulo. O `placeholder` mostra um texto cinzento dentro do campo, que desaparece logo que se começa a escrever. Quem se distrai perde a explicação, e muitos leitores de ecrã não a leem. O rótulo fica sempre à vista.

### O formulário

Numa ficha de inscrição, os campos vão todos juntos para a secretaria. O HTML tem um elemento para isso, o `form` (em inglês, formulário), que junta vários campos para serem enviados de uma vez. Quando se carrega no botão de um formulário, o browser envia o formulário e recarrega a página. O que estava escrito desaparece, e o JavaScript volta a correr desde o início.

A página deste tema não usa um formulário. Tem um só campo, e o JavaScript responde ao botão sem enviar nada. O `type="button"` garante que o botão nunca envia nada, mesmo que um dia fique dentro de um formulário. Tratar o envio de um formulário com JavaScript é o assunto do tema 06.

## O CSS dá a apresentação

Uma página só com HTML funciona, mas tem o aspeto que o browser escolhe. O texto fica encostado à margem da janela, os campos e os botões têm uma letra mais pequena do que a do resto, e os botões são cinzentos. O CSS serve para escolheres a apresentação.

O CSS escreve-se num ficheiro à parte, a **folha de estilos**, que a página carrega. A ligação faz-se no `head`, com o elemento `link`, que também não tem etiqueta de fecho:

```html
<link rel="stylesheet" href="estilos.css">
```

Esta linha não mostra nada na página: só diz ao browser onde está a folha de estilos. O `rel="stylesheet"` diz que o ficheiro ligado é uma folha de estilos. O `href` diz onde ela está, com um caminho relativo.

Uma folha de estilos é feita de **regras**. Cada regra escolhe um ou mais elementos e diz como devem aparecer. Antes de leres a explicação, tenta prever: depois de a página carregar esta folha, o que muda no texto e na página?

```css
/* estilos.css: a apresentação da página do inventário. */

body {
  font-family: system-ui, sans-serif;
  line-height: 1.5;
  color: #1f1f1f;
  background-color: #ffffff;
  margin: 2rem;
}

input,
button {
  font: inherit;
  padding: 0.5rem;
}

button {
  color: #ffffff;
  background-color: #1f4e8c;
}
```

O resultado é este. A letra passa a ser a do sistema operativo, com mais espaço entre as linhas. A página ganha uma margem à volta, e o texto deixa de estar encostado à janela. O campo e o botão passam a usar a mesma letra do resto da página, com espaço por dentro. O botão fica azul-escuro, com letras brancas.

Leitura guiada: lê cada regra pela ordem em que está escrita.

- A primeira linha é um comentário de CSS, entre `/*` e `*/`. Diz o que é o ficheiro. O browser ignora-a.
- Uma regra começa pelo **seletor**, que escolhe os elementos. O seletor `body` escolhe o elemento `body`. Depois, entre chavetas, vêm as **propriedades**, cada uma com o seu **valor**, na forma `propriedade: valor;`. O ponto e vírgula fecha cada propriedade.
- O `font-family` é o tipo de letra. O valor `system-ui` pede a letra do sistema operativo. O `sans-serif` é a alternativa, se a primeira não existir: uma letra sem serifas, os pequenos traços nas pontas das letras.
- O `line-height: 1.5` faz cada linha ocupar uma vez e meia a altura da letra, o que deixa espaço entre as linhas e torna os parágrafos mais fáceis de ler.
- O `color` é a cor do texto, e o `background-color` é a cor do fundo. As cores escrevem-se aqui com um `#` seguido de três pares de símbolos, para o vermelho, o verde e o azul. Cada par é um número escrito em hexadecimal, uma forma de escrever números que usa os algarismos de 0 a 9 e as letras de `a` a `f`. Cada par vai de `00`, nada dessa cor, a `ff`, o máximo. O `#ffffff` é branco, e o `#1f1f1f` é um cinzento quase preto.
- O `margin` é o espaço por fora de um elemento. A unidade `rem` vale o tamanho da letra normal do browser, que quase sempre é 16 píxeis. Por isso, `2rem` são cerca de 32 píxeis. Se a pessoa aumentar o tamanho da letra nas definições do browser, o `rem` aumenta também, e a margem acompanha.
- A segunda regra tem dois seletores, separados por uma vírgula: `input` e `button`. As propriedades valem para os dois. Os campos e os botões usam, por omissão, uma letra mais pequena do que o resto da página. O `font: inherit` (em inglês, herdar) manda-os usar a letra do elemento que os contém. O `padding` é o espaço por dentro de um elemento, entre o texto e a borda.
- A terceira regra dá ao botão a cor do texto e a do fundo.

Repara numa coisa sobre a cor do texto. O `body` diz que o texto é quase preto, e essa cor passa para os elementos que estão dentro dele, como o `h1` e o `p`. A isto chama-se **herança**: uma propriedade dada a um elemento passa para os elementos que estão dentro dele. Mas o botão também está dentro do `body`, e o texto dele fica branco. Fica branco porque a regra `button` escolhe o botão diretamente, e um valor dado diretamente a um elemento ganha sempre ao valor que ele herdaria.

Para veres que regras se aplicam a um elemento, carrega com o botão direito nele e escolhe `Inspecionar` (no browser em inglês, `Inspect`). Abre-se uma parte do browser com o HTML da página e, ao lado, as regras de CSS desse elemento. Uma propriedade que perdeu para outra aparece riscada. Uma propriedade mal escrita, como `colr`, também aparece riscada, com um sinal de aviso. Tal como no HTML, o browser não mostra nenhuma mensagem por causa de um erro no CSS: ignora a propriedade e continua.

O CSS tem muitas mais propriedades e outros tipos de seletores. Para esta página, bastam os seletores pelo nome do elemento.

## Contraste e foco visível

Uma página que algumas pessoas não conseguem ler não serve a essas pessoas. Um texto cinzento-claro num fundo branco lê-se mal num ecrã ao sol, com o brilho baixo ou com uma vista mais fraca. Por isso, as cores escolhem-se também pelo contraste.

O **contraste** é a diferença de luminosidade entre a cor do texto e a do fundo. Mede-se com um número, a razão de contraste, que vai de 1 para 1, quando as duas cores são iguais, a 21 para 1, que é o preto no branco. As regras de acessibilidade usadas em todo o mundo pedem pelo menos 4,5 para 1 no texto de tamanho normal. As cores desta página foram escolhidas assim:

| Texto | Fundo | Razão de contraste | Chega aos 4,5 para 1? |
| --- | --- | ---: | --- |
| `#1f1f1f`, quase preto | `#ffffff`, branco | 16,5 para 1 | Sim |
| `#ffffff`, branco | `#1f4e8c`, azul-escuro | 8,3 para 1 | Sim |
| `#777777`, cinzento médio | `#ffffff`, branco | 4,48 para 1 | Não, por pouco |
| `#999999`, cinzento-claro | `#ffffff`, branco | 2,85 para 1 | Não |

A terceira linha mostra que o olho engana: o cinzento médio parece legível, e fica abaixo do mínimo. Para medir, usa uma calculadora de contraste, como a que está em "Para saber mais", ou o inspetor do browser. No Chrome e no Edge, inspeciona um texto e clica no quadrado da cor ao lado de `color`. O browser mostra a razão de contraste dessa cor com o fundo.

Outra regra da acessibilidade vem do mesmo problema. A informação nunca depende só da cor. Uma mensagem de erro não fica apenas vermelha: tem também um texto que diz o que está errado, para quem não distingue bem as cores.

### O foco visível

Quem usa o teclado precisa de ver onde está o foco. Os browsers desenham uma linha à volta do controlo que tem o foco, o **contorno**, mas o contorno do browser pode ser fino ou difícil de ver com algumas cores. Esta regra torna-o mais grosso e com uma cor própria:

```css
input:focus-visible,
button:focus-visible {
  outline: 3px solid #b35c00;
  outline-offset: 2px;
}
```

Leitura guiada: o `:focus-visible`, colado ao nome do elemento, escolhe o elemento só quando ele tem o foco e o browser mostraria o contorno. É o que acontece quando se chega lá com a tecla Tab. O `outline` (em inglês, contorno) é uma linha contínua (`solid`) com `3px` de grossura, ou seja, três píxeis. A cor é um laranja escuro, `#b35c00`, que tem um contraste de 4,7 para 1 com o fundo branco. O `outline-offset` afasta o contorno 2 píxeis do elemento, para não se colar à borda. O resultado vê-se carregando na tecla Tab: o campo e o botão, quando têm o foco, ficam rodeados por uma linha laranja grossa.

Um erro frequente é apagar o contorno, com `outline: none`, porque não se gosta do aspeto dele. Quem usa o teclado fica sem saber onde está. Se não gostares do contorno do browser, troca-o por outro, como esta regra faz, e nunca o tires sem pôr outro no lugar.

## O JavaScript entra pela etiqueta `script`

A página tem estrutura e apresentação, mas ainda não faz nada. Para lhe dar comportamento, a página carrega um ficheiro de JavaScript. Carrega-o com o elemento `script`, que se escreve no `head`, a seguir ao `link`:

```html
<script src="inventario.js" defer></script>
```

Esta linha não mostra nada na página: só diz ao browser onde está o script. O `src` (de *source*, em inglês, origem) é o caminho do ficheiro, como o `href` do `link`. O `script` precisa sempre da etiqueta de fecho, `</script>`, mesmo sem nada lá dentro.

O atributo `defer` (em inglês, adiar) não tem valor: basta escrevê-lo. Diz ao browser que pode ir buscar o ficheiro logo, mas que só o deve correr depois de ler o HTML todo. Faz falta porque o script vai procurar elementos da página, como o campo e o botão. Sem o `defer`, um script escrito no `head` corria antes de o browser ter lido o `body`, e não encontrava nenhum desses elementos.

### A consola do browser

Um primeiro ficheiro `inventario.js` pode ser só isto. Antes de abrires a página, tenta prever onde aparece o texto deste programa.

```js
// inventario.js: o comportamento da página do inventário.

console.log("O script está a correr.");
console.log(6 - 2);
```

A resposta pode surpreender: dentro da página não aparece nada de novo. O texto aparece na consola do browser:

```text
O script está a correr.
4
```

A **consola** faz parte das **ferramentas do programador**, uma parte do browser feita para quem constrói páginas. Em inglês chamam-se *DevTools*, de *developer tools*. Para as abrires, carrega em F12 no Windows, ou em Cmd+Option+I no macOS, e escolhe o separador `Console` (num browser em português, pode aparecer `Consola`). Também as abres com o botão direito numa parte vazia da página e `Inspecionar`.

Leitura guiada: a primeira linha é um comentário de JavaScript, que começa por `//` e vai até ao fim da linha, como o `#` do Python. O `console.log(...)` faz o que o `print` fazia em Python: mostra os valores que recebe. A diferença está no sítio. O `print` mostrava os resultados numa janela do editor. O `console.log` mostra-os na consola do browser, que é outra coisa, e que a pessoa que usa a página normalmente não vê. Serve a quem programa, para confirmar valores enquanto constrói a página. Cada instrução acaba com um ponto e vírgula, `;`.

A consola serve também para escrever JavaScript e ver logo o resultado. Escreve `6 - 2` na linha de baixo da consola e carrega em Enter: aparece `4`. Escreve `console.log("olá")` e carrega em Enter: aparece `olá` e, por baixo, `undefined`. A consola mostra sempre o valor da instrução que escreveste. O `console.log` mostra o texto e não devolve valor nenhum, e em JavaScript a ausência de valor chama-se **`undefined`** (em inglês, não definido). É o que o `None` era em Python.

Quando o valor de uma instrução é um texto, a consola mostra-o entre plicas, como `'Caderno'`, ou entre aspas, conforme o browser. As plicas dizem-te que o valor é um texto, e não fazem parte dele. Escreve sempre à mão o que pões na consola: o Chrome e o Edge, por segurança, não deixam colar código na consola na primeira vez, e mostram um aviso.

A consola conhece as funções do script da página e as variáveis que estão fora das funções. Uma variável declarada dentro de uma função só existe enquanto a função corre, e a consola não a conhece. Depois de a página carregar, podes chamar na consola uma função do teu ficheiro, com valores à tua escolha, e ver o que ela devolve. No exemplo guiado vais usar isto para testar a função `retirar`.

É também na consola que o browser escreve as mensagens de erro do JavaScript. Quando a página não faz o que devia, a consola é o primeiro sítio onde vais olhar.

### Onde corre este JavaScript

O JavaScript desta página corre dentro do browser, com a página aberta. É lá que existe a página, e é com ela que o script trabalha. Se tentares executar o ficheiro `inventario.js` no editor, como fazias com os ficheiros de Python, não vais ter a página. Em "Erros frequentes" vês o que aparece nesse caso. O JavaScript também corre fora do browser, num programa chamado Node, e vais usá-lo mais tarde para outras coisas, como ler ficheiros. Para já, abre sempre a página no browser.

## Variáveis com `const` e `let`

Em Python, uma variável nascia na primeira atribuição: `quantidade = 6` criava-a. Em JavaScript, uma variável nova anuncia-se com uma palavra antes do nome. A isto chama-se **declarar** a variável. Há duas palavras para isso:

- `const` (de constante) declara um nome que recebe um valor uma vez e fica com ele até ao fim;
- `let` (em inglês, deixa ser) declara um nome que pode receber outro valor mais tarde.

Antes de correres este programa, tenta prever o que mostra o `console.log`.

```js
const codigo = "A01";
let quantidade = 6;

quantidade = quantidade - 2;
console.log(codigo, quantidade);
```

O resultado é `A01 4`. O `console.log` mostra os valores separados por um espaço, como o `print` com vários valores.

Leitura guiada: a primeira linha declara `codigo` com `const`, porque o código do artigo nunca muda. A segunda declara `quantidade` com `let`, porque a quantidade vai mudar. A terceira dá um valor novo a `quantidade`. Repara que não leva `let` outra vez: declara-se uma só vez, e as atribuições seguintes usam só o nome. A conta faz-se primeiro, `6 - 2`, e só depois o resultado fica guardado, como em Python.

Se tentares dar outro valor a um `const`, com `codigo = "A02";`, o programa para com a mensagem `TypeError: Assignment to constant variable.` (em português, atribuição a uma variável constante). É um erro de execução. O `const` serve precisamente para isso: protege os nomes que não deviam mudar. Quem lê o código sabe que aquele nome tem o mesmo valor em todo o lado. Por isso, nesta disciplina usa-se o `const` sempre que se pode, e o `let` só quando a variável recebe mesmo outro valor.

Se te esqueceres da palavra e escreveres só `quantidade = 6`, numa variável que ainda não existe, o browser aceita sem nenhum aviso. Parece que funciona, mas a variável fica criada de uma forma que esconde enganos, como um nome mal escrito. Declara sempre as variáveis novas com `const` ou com `let`.

### Os nomes em JavaScript

Em Python, um nome com várias palavras escrevia-se com um traço por baixo: `quantidade_caderno`. Em JavaScript, a convenção é juntar as palavras e começar cada palavra nova por maiúscula: `quantidadeCaderno`. Esta forma chama-se *camelCase*, porque as maiúsculas no meio do nome lembram as bossas de um camelo. Os dois estilos funcionam nas duas linguagens, mas seguir a convenção de cada uma torna o código mais fácil de ler para quem a conhece. Os nomes continuam em português e sem acentos.

O JavaScript distingue as maiúsculas das minúsculas, como o Python. Para ele, `quantidade` e `Quantidade` são dois nomes diferentes.

## Números, textos e valores lógicos

Os valores do JavaScript têm tipos, como os do Python. Os três tipos que este tema usa são estes:

- **`number`**: os números. Em Python havia o `int`, para os inteiros, e o `float`, para os números com parte decimal. Em JavaScript há um só tipo para os dois: `6` e `2.5` são ambos `number`. A parte decimal escreve-se com ponto, como em Python.
- **`string`**: os textos, entre aspas. Nesta disciplina usamos aspas duplas: `"Caderno"`.
- **`boolean`**: os valores lógicos, `true` (verdadeiro) e `false` (falso). Escrevem-se em minúsculas, ao contrário do `True` e do `False` do Python.

Para saberes o tipo de um valor, usa o `typeof`. Antes de correres este programa, tenta prever as quatro palavras que aparecem.

```js
console.log(typeof 6, typeof 2.5, typeof "6", typeof true);
```

O resultado é `number number string boolean`. O `"6"` é um texto, porque está entre aspas, mesmo sendo feito de um algarismo.

### O `+` com textos

O `+` entre dois textos junta-os, como em Python: `"Cader" + "no"` dá `"Caderno"`. A diferença está no `+` entre um texto e um número. O Python recusava, com um `TypeError`. O JavaScript converte o número em texto e junta os dois. Antes de correres este programa, tenta prever as três linhas.

```js
console.log("Caderno: " + 6 + " unidades");
console.log("2" + 3);
console.log("Caderno: " + 6 + 1);
```

O resultado é este:

```text
Caderno: 6 unidades
23
Caderno: 61
```

Leitura guiada: a primeira linha faz o que se quer: junta o texto, o número convertido em texto e outro texto. A segunda dá `23`, e não `5`, porque o `"2"` é um texto, e o `+` com um texto junta em vez de somar. A terceira é a mais traiçoeira. O JavaScript faz os `+` da esquerda para a direita. Primeiro junta `"Caderno: "` com `6`, e fica com o texto `"Caderno: 6"`. Depois junta esse texto com `1`, e fica `"Caderno: 61"`. Para somar primeiro, usa parênteses: `"Caderno: " + (6 + 1)` dá `"Caderno: 7"`.

Esta conversão automática facilita escrever mensagens, mas é a origem de muitos erros de lógica. Quando um resultado tem algarismos colados, como `23` em vez de `5`, desconfia de um texto no meio da conta.

## Operadores

A maior parte dos operadores é igual nas duas linguagens. Esta tabela mostra os que este tema usa, com os do Python ao lado:

| Python | JavaScript | Exemplo em JavaScript | Resultado |
| --- | --- | --- | --- |
| `+`, `-`, `*` | `+`, `-`, `*` | `6 - 2` | `4` |
| `/` | `/` | `7 / 2` | `3.5` |
| `//` | não existe: `//` começa um comentário | `7 // 2` | `7` |
| `%` | `%` | `7 % 2` | `1` |
| `**` | `**` | `2 ** 3` | `8` |
| `==` | `===` | `6 === 6` | `true` |
| `!=` | `!==` | `6 !== 2` | `true` |
| `<`, `>`, `<=`, `>=` | `<`, `>`, `<=`, `>=` | `2 <= 6` | `true` |
| `and` | `&&` | `true && false` | `false` |
| `or` | `\|\|` | `true \|\| false` | `true` |
| `not` | `!` | `!true` | `false` |

Repara na linha do `//`. Quem vem do Python e escreve `7 // 2` não vê nenhum erro: o JavaScript lê o `7` e trata o resto da linha como um comentário. A diferença que mais conta está na comparação. O JavaScript tem dois operadores de igualdade, o `==` e o `===`. O `==` converte os valores para o mesmo tipo antes de comparar: `"7" == 7` dá `true`, porque converte o texto `"7"` no número 7. O `===` compara sem converter: `"7" === 7` dá `false`, porque um texto nunca é igual a um número. A conversão do `==` esconde enganos, e por isso nesta disciplina usamos sempre o `===` e o `!==`.

Os operadores lógicos escrevem-se com símbolos: `&&` é o "e", `||` é o "ou" e `!` é o "não". O `||` são duas barras verticais. No teclado português dos computadores com Windows, a barra vertical escreve-se com Shift e a tecla à esquerda do 1.

Antes de correres este programa, tenta prever as três linhas.

```js
const quantidade = 6;
const unidades = 2;

console.log(unidades > 0 && unidades <= quantidade);
console.log(unidades === "2");
console.log(!(unidades > quantidade));
```

O resultado é `true`, `false` e `true`, uma em cada linha. Leitura guiada: na primeira, as duas perguntas têm resposta verdadeira, e o `&&` só dá `true` quando as duas são verdadeiras. É a condição do pedido de retirada do guia 01 do M10. Na segunda, o número 2 não é igual ao texto `"2"`, porque o `===` não converte. Na terceira, `unidades > quantidade` é falso, e o `!` troca-o por verdadeiro.

## Decisões com `if` e `else`

O `if` faz a mesma coisa nas duas linguagens: escolhe o que fazer conforme uma condição. Muda a forma de o escrever. Este programa de Python, que já sabes ler, verifica um pedido:

```python
quantidade = 6
unidades = 8

if unidades > quantidade:
    print("Não há unidades suficientes.")
elif unidades <= 0:
    print("O pedido tem de ser positivo.")
else:
    print("Pedido aceite.")
```

Antes de correres a versão em JavaScript, tenta prever o que ela mostra com 8 unidades.

```js
const quantidade = 6;
const unidades = 8;

if (unidades > quantidade) {
  console.log("Não há unidades suficientes.");
} else if (unidades <= 0) {
  console.log("O pedido tem de ser positivo.");
} else {
  console.log("Pedido aceite.");
}
```

O resultado é `Não há unidades suficientes.`, porque 8 é maior do que 6, e as outras partes já não se verificam.

Leitura guiada: compara as duas versões linha a linha. Em JavaScript, a condição vai sempre entre parênteses, `(unidades > quantidade)`. Não há dois pontos no fim. As instruções de cada parte ficam entre **chavetas**, `{` e `}`, e são as chavetas que marcam onde a parte começa e acaba. O `elif` do Python escreve-se `else if`, com duas palavras.

Em Python, era a indentação que marcava o bloco. Em JavaScript, são as chavetas, e a indentação serve só para as pessoas. Mesmo assim, escrevemo-la sempre, com dois espaços por nível, porque sem ela não se vê que linhas estão dentro de que bloco. O VS Code ajuda: quando pões o cursor ao lado de uma chaveta, ele marca a chaveta que lhe corresponde.

## Funções com `function` e `return`

Em Python, uma função começava por `def`. Em JavaScript, começa por `function`. Antes de correres este programa, tenta prever as duas linhas que ele mostra.

```js
/**
 * Devolve o texto que descreve um artigo, com o nome e a quantidade.
 * @param {string} nome o nome do artigo, como "Caderno"
 * @param {number} quantidade as unidades disponíveis
 * @returns {string} o texto que descreve o artigo, como "Caderno: 6 unidades"
 */
function descreverArtigo(nome, quantidade) {
  return nome + ": " + quantidade + " unidades";
}

console.log(descreverArtigo("Caderno", 6));
console.log(descreverArtigo("Pasta", 2));
```

O resultado é este:

```text
Caderno: 6 unidades
Pasta: 2 unidades
```

Leitura guiada: começa pela linha `function descreverArtigo(nome, quantidade) {`. A palavra `function` anuncia uma função nova, a seguir vem o nome, e entre parênteses os parâmetros, como no `def`. O corpo da função fica entre chavetas, em vez de ficar indentado depois de dois pontos. O `return` funciona como em Python: entrega o valor a quem chamou e acaba a função. As duas últimas linhas chamam a função, cada uma com os seus argumentos, e mostram o valor devolvido.

Por cima da função está a documentação dela. Em JavaScript, a documentação de uma função escreve-se num comentário entre `/**` e `*/`, logo antes da função, e chama-se **JSDoc**. Faz o papel da docstring. A primeira frase diz para que serve a função. Cada `@param` descreve um parâmetro, com o tipo entre chavetas, o nome e o que quer dizer. O `@returns` diz o tipo e o significado do que a função devolve. O VS Code mostra este texto quando passas o rato por cima do nome da função, em qualquer sítio do ficheiro. Nesta disciplina, todas as funções levam JSDoc.

Há uma diferença que engana quem vem do Python. Se chamares `descreverArtigo("Caderno")`, sem a quantidade, o Python recusava a chamada com um `TypeError`. O JavaScript aceita: o parâmetro que ficou sem argumento recebe `undefined`, e a função devolve `"Caderno: undefined unidades"`. Não aparece nenhuma mensagem de erro. Quando vires `undefined` num resultado, procura um argumento em falta ou um nome mal escrito.

## Ciclos: `for`, `while` e `for...of`

Os ciclos do JavaScript repetem instruções, como os do Python. Há três formas que vais usar.

### O `for` com um contador

Em Python, `for i in range(1, 4):` repetia com `i` a valer 1, 2 e 3. Em JavaScript, o mesmo ciclo escreve-se assim. Antes de correres, tenta prever o que aparece na consola.

```js
for (let i = 1; i <= 3; i++) {
  console.log("Volta " + i);
}
```

O resultado é este:

```text
Volta 1
Volta 2
Volta 3
```

Leitura guiada: dentro dos parênteses do `for` há três partes, separadas por ponto e vírgula. A primeira, `let i = 1`, corre uma só vez, no início, e declara o contador. A segunda, `i <= 3`, é a condição: o ciclo repete enquanto ela for verdadeira. A terceira, `i++`, corre no fim de cada volta. O `i++` quer dizer "soma 1 ao `i`", e é uma forma curta de escrever `i = i + 1`. O contador é `let`, e não `const`, porque muda a cada volta.

Como é a primeira vez que vês este ciclo, segue-o passo a passo nesta tabela:

| Momento | `i` | `i <= 3` | O que aparece |
| --- | ---: | --- | --- |
| Início: `let i = 1` | 1 | `true` | `Volta 1` |
| Depois do primeiro `i++` | 2 | `true` | `Volta 2` |
| Depois do segundo `i++` | 3 | `true` | `Volta 3` |
| Depois do terceiro `i++` | 4 | `false` | nada: o ciclo acaba |

Repara que a condição se verifica antes de cada volta, também da primeira. O `i` chega a valer 4, mas com o 4 a condição é falsa, e a volta já não se faz. É o mesmo que o `range(1, 4)` fazia em Python: o 4 marca onde parar, e não entra.

### O `while`

O `while` repete enquanto uma condição for verdadeira, como em Python. A condição vai entre parênteses, e o corpo entre chavetas. Este programa conta quantos pedidos de 2 unidades cabem num caderno com 6. Antes de correres, tenta prever os dois números.

```js
let quantidade = 6;
let pedidos = 0;

while (quantidade >= 2) {
  quantidade = quantidade - 2;
  pedidos = pedidos + 1;
}

console.log(pedidos, quantidade);
```

O resultado é `3 0`: cabem três pedidos, e o caderno fica com 0 unidades. Leitura guiada: antes de cada volta, o `while` pergunta se ainda há pelo menos 2 unidades. Com 6, 4 e 2, há, e o corpo tira 2 e conta mais um pedido. Com 0, a condição é falsa e o ciclo acaba. As duas variáveis são `let`, porque mudam dentro do ciclo.

### Os arrays e o `for...of`

As listas do Python também existem em JavaScript, e chamam-se **arrays**. Escrevem-se da mesma maneira, com os valores entre parênteses retos, separados por vírgulas: `[2, 5, 1]`. O índice também começa em 0. O tamanho de um array lê-se com `.length` (em inglês, comprimento), escrito a seguir ao nome, em vez do `len` do Python.

Para percorrer os valores de um array, um a um, usa-se o `for...of`. É o que o `for pedido in pedidos:` fazia em Python. Este programa conta quantos pedidos são maiores do que 3 unidades. Antes de correres, tenta prever as duas linhas.

```js
const pedidos = [2, 5, 1];
let grandes = 0;

for (const pedido of pedidos) {
  if (pedido > 3) {
    grandes = grandes + 1;
  }
}

console.log("Pedidos: " + pedidos.length);
console.log("Maiores do que 3: " + grandes);
```

O resultado é este:

```text
Pedidos: 3
Maiores do que 3: 1
```

Leitura guiada: em cada volta, o `pedido` recebe o valor seguinte do array: 2, depois 5, depois 1. Só o 5 é maior do que 3, e por isso o `grandes` acaba com 1. O `pedido` é `const`, e isso não é um erro: em cada volta nasce um `pedido` novo, que não muda dentro dessa volta. O `pedidos.length` dá 3, o número de valores do array. O array é `const` porque o nome `pedidos` aponta sempre para o mesmo array.

A palavra entre o nome e o array é `of` (em inglês, de). Em JavaScript existe também um `for...in`, com `in`, como em Python, mas faz outra coisa. Em "Erros frequentes" vês o que acontece quando se troca o `of` pelo `in`.

## Comentários que explicam a intenção

Os comentários do JavaScript têm três formas. O `//` comenta até ao fim da linha, como o `#` do Python. O `/*` e o `*/` comentam tudo o que está entre eles, mesmo em várias linhas. E o `/**`, que já viste, abre a documentação JSDoc de uma função.

Um comentário serve para dizer o que o código não diz sozinho: porque é que uma linha existe, ou o que aconteceria sem ela. Um comentário que repete a instrução não acrescenta nada. Compara estes dois:

```js partial
// Soma 1 ao i.
i++;
```

```js partial
// A quantidade muda a cada pedido aceite, por isso é let e não const.
let quantidadeCaderno = 6;
```

São excertos, que não correm sozinhos. O primeiro comentário diz em palavras o que o `i++` já diz em código: quem sabe ler o `i++` não aprende nada com ele. O segundo explica uma escolha: porque se usou `let`. Daqui a uma semana, quando voltares ao código, é este o comentário que te vai fazer falta. Antes de escreveres um comentário, pergunta-te se ele responde a um "porquê" que o código não responde.

## Ligar um botão a uma função

Até aqui, o JavaScript escrevia na consola. Para a página reagir, o script tem de fazer quatro coisas. Tem de encontrar os elementos da página, ler o que a pessoa escreveu, escrever na página e saber quando alguém carrega no botão. Para isso usa quatro peças, que vês primeiro num exemplo pequeno: uma página que repete o nome de um artigo que alguém escreve.

Antes de experimentares, tenta prever o que aparece por baixo do botão quando escreves `<b>Pasta</b>` no campo e carregas em "Mostrar". O `<b>` é a etiqueta do HTML para texto em negrito.

Esta página de ensaio fica numa pasta nova, só dela, como `mostrar-nome`, para não escrever por cima da página do inventário. O ficheiro `index.html`, completo:

```html
<!doctype html>
<html lang="pt-PT">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Mostrar o nome</title>
    <script src="mostrar.js" defer></script>
  </head>
  <body>
    <main>
      <h1>Mostrar o nome</h1>
      <p>
        <label for="nome">Nome do artigo</label>
        <input id="nome" type="text">
      </p>
      <p>
        <button id="mostrar" type="button">Mostrar</button>
      </p>
      <p>
        <output id="resultado"></output>
      </p>
    </main>
  </body>
</html>
```

O ficheiro `mostrar.js`, na mesma pasta, completo:

```js
// mostrar.js: mostra na página o nome que se escreveu no campo.

const campoNome = document.querySelector("#nome");
const botaoMostrar = document.querySelector("#mostrar");
const saida = document.querySelector("#resultado");

/**
 * Trata o clique no botão Mostrar: copia o texto do campo para a saída.
 * Não devolve nada: muda o texto da saída da página.
 */
function aoCarregarEmMostrar() {
  saida.textContent = "Escreveste: " + campoNome.value;
}

botaoMostrar.addEventListener("click", aoCarregarEmMostrar);
```

O resultado é este. Com `Pasta` no campo, a saída mostra `Escreveste: Pasta`. Com `<b>Pasta</b>`, a saída mostra `Escreveste: <b>Pasta</b>`, com os sinais `<` e `>` à vista, e a palavra não fica em negrito. O browser não tratou o que escreveste como HTML. Mais abaixo vês porque é que isto é bom.

Leitura guiada: lê o script pela ordem em que o browser o corre, com as quatro peças.

1. As três primeiras instruções encontram os elementos. O **`document`** é a página, tal como o browser a guarda enquanto a mostra. O `document.querySelector("#nome")` procura na página o primeiro elemento que corresponde ao seletor entre aspas e devolve-o. O `#` antes do nome quer dizer "o elemento com este `id`". Assim, `#nome` é o campo com `id="nome"`. O elemento devolvido fica guardado num `const`, porque o campo é sempre o mesmo. Se nenhum elemento tiver esse `id`, o `querySelector` devolve **`null`**, um valor que quer dizer "nenhum objeto".
2. A função `aoCarregarEmMostrar` ainda não corre: fica só definida, como uma função de Python que ainda ninguém chamou.
3. A última linha liga o botão à função. Um **evento** é uma coisa que acontece na página, como um clique num botão. O `addEventListener` (em inglês, acrescenta quem ouve o evento) diz ao browser: "quando houver um clique neste botão, chama esta função". O primeiro argumento, `"click"`, é o nome do evento. O segundo é a função que trata o evento.
4. O browser fica à espera. Quando alguém carrega no botão, com o rato ou com o teclado, o browser chama `aoCarregarEmMostrar`.
5. Dentro da função, `campoNome.value` é o texto escrito no campo nesse momento. O **`value`** (em inglês, valor) de um campo é sempre um texto, uma `string`, mesmo quando lá se escreve um número.
6. O `saida.textContent = ...` muda o texto da saída. O **`textContent`** (em inglês, conteúdo de texto) é o texto que está dentro de um elemento. Dar-lhe um valor novo substitui o texto que lá estava.

Repara na última linha do script: `aoCarregarEmMostrar` vai sem parênteses. Com parênteses, `aoCarregarEmMostrar()` chamava a função logo ali, uma vez, quando a página carrega. Sem parênteses, dás a função ao browser, para ele a chamar mais tarde, em cada clique. É a diferença entre ligares tu a uma pessoa agora e deixares-lhe o teu número para ela te ligar quando precisar.

Agora o `<b>Pasta</b>`. O `textContent` escreve sempre texto simples: os sinais `<` e `>` aparecem como sinais, e o browser nunca os lê como etiquetas. Isto protege a página. O que uma pessoa escreve num campo nunca passa a fazer parte do HTML da página. Por isso, ninguém consegue meter na página, a partir de um campo, uma imagem ou um botão falso. Existe outra propriedade, `innerHTML`, que lê o texto como HTML, e que por isso nunca se usa com o que a pessoa escreveu. Nesta disciplina, o texto que vem do utilizador entra sempre com `textContent`.

### Converter o texto do campo em número

No inventário, o campo traz um número de unidades. Como o `value` é sempre texto, antes das contas converte-se o texto em número com o **`Number`**. Antes de correres este programa, tenta prever os cinco valores.

```js
console.log(Number("2"), Number("2.5"), Number(""), Number("abc"), Number("2,5"));
```

O resultado é `2 2.5 0 NaN NaN`. Leitura guiada: o `Number("2")` dá o número 2, e o `Number("2.5")` dá 2.5. O texto vazio, `""`, dá 0: um campo que ficou por preencher vale zero. O `"abc"` não é um número, e dá **`NaN`**, de *Not a Number* (em inglês, não é um número). O `NaN` é um valor do tipo `number` que quer dizer "isto não era um número". O `"2,5"` também dá `NaN`, porque o JavaScript escreve a parte decimal com ponto, e a vírgula não faz parte de um número.

O `NaN` tem uma característica útil: as comparações com `<`, `>`, `<=`, `>=` e `===` dão sempre `false` quando um dos lados é `NaN`. Tanto `NaN > 0` como `NaN <= 6` dão `false`. No exemplo guiado vais ver o que isto faz a um pedido de retirada.

As quatro peças desta secção são uma primeira vista. Os temas 05 e 06 voltam a elas com mais tempo: os elementos da página, as suas propriedades e os outros eventos.

## Quando a página não faz o que devia

Quando a página não faz o que esperavas, não mudes linhas ao acaso até ela funcionar. Segue sempre a mesma rotina, que serve para qualquer linguagem:

1. **Observar e reproduzir o erro.** Escreve o que fizeste, o que esperavas ver, tirado do enunciado e não do código, e o que viste. Abre a consola e diz que tipo de erro é. Um **erro de escrita** aparece logo ao carregar a página, como `SyntaxError` (erro de sintaxe), e nenhuma linha do script corre. Um **erro de execução** para o script a meio, numa linha, com mensagens como `TypeError` (erro de tipo) ou `ReferenceError` (erro de referência). Um **erro de lógica** não deixa nenhuma mensagem: a página funciona e dá o resultado errado.
2. **Formular uma hipótese.** Escreve uma explicação possível, numa frase que os valores possam confirmar ou desmentir. Por exemplo: "o `querySelector` não encontrou o botão, porque o `id` está escrito de outra maneira no HTML".
3. **Verificar a hipótese.** Segue os valores no caso mais curto que ainda mostra o erro. Na consola, escreve o nome de uma variável que esteja fora das funções e carrega em Enter para veres o valor dela. Para uma variável de dentro de uma função, acrescenta um `console.log` no script.
4. **Corrigir a causa.** Muda a instrução que produz o erro, uma de cada vez, e não o sítio onde ele se vê.
5. **Voltar a testar tudo.** Recarrega a página e repete todos os casos, também os que já funcionavam.

A mensagem de erro é uma pista, e não a resposta. Cada mensagem da consola diz o ficheiro e o número da linha onde o browser deu pelo erro, à direita, como `inventario.js:46`. Essa linha pode mostrar uma falha que nasceu antes. No exemplo guiado, um `id` mal escrito na linha 23 só rebenta na linha 46, onde o elemento é usado.

As mensagens deste guia são as do Chrome e do Edge, que escrevem igual. O Firefox usa outras palavras, mas as mensagens aparecem no mesmo sítio, com o ficheiro e a linha.

## Exemplo guiado: retirar unidades do caderno na página

O problema: a página do inventário mostra o caderno A01, que começa com 6 unidades. A pessoa escreve quantas unidades quer retirar e carrega em "Retirar". A página aplica as regras do guia 01 do M10. Um pedido positivo e não maior do que o que existe é aceite. Qualquer outro é recusado, sem mexer na quantidade. Depois de cada pedido, a página mostra a quantidade que fica. O programa tem de dar os mesmos resultados que o de Python: com 6 unidades, retirar 2 deixa 4; a seguir, um pedido de 5 deixa as 4.

### Passo 1: traduzir a função `retirar`

A regra do pedido já existe, escrita em Python, no guia 01 do M10. Não é preciso pensá-la outra vez: basta traduzi-la.

```python
def retirar(quantidade, unidades):
    """Devolve a quantidade que fica depois de um pedido de retirada.

    Se o pedido for possível, devolve a quantidade menos as unidades pedidas.
    Se não for possível, devolve a quantidade que recebeu, sem mudanças.
    """
    if unidades > 0 and unidades <= quantidade:
        return quantidade - unidades
    return quantidade
```

A tradução faz-se linha a linha, com o que viste nas secções anteriores:

| Python | JavaScript | O que mudou |
| --- | --- | --- |
| `def retirar(quantidade, unidades):` | `function retirar(quantidade, unidades) {` | `function` em vez de `def`; chaveta em vez de dois pontos |
| A docstring, entre três aspas | O JSDoc, entre `/**` e `*/`, antes da função | O sítio e a forma, com o tipo de cada parâmetro |
| `if unidades > 0 and unidades <= quantidade:` | `if (unidades > 0 && unidades <= quantidade) {` | Parênteses na condição; `&&` em vez de `and`; chaveta |
| `return quantidade - unidades` | `return quantidade - unidades;` | O ponto e vírgula, e a chaveta que fecha o `if` |
| `return quantidade` | `return quantidade;` | O ponto e vírgula, e a chaveta que fecha a função |

A função em JavaScript fica assim. É um excerto do ficheiro final, que está no passo 5:

```js partial
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
```

O nome da função e dos parâmetros ficou igual ao do Python, porque são palavras simples, sem traço por baixo. A lógica também não mudou: muda só a forma de a escrever. É por isso que se começa por uma função que já se conhece. A única coisa nova é a linguagem.

### Passo 2: testar a função com os casos do M10

Antes de ligar a função à página, confirma-se que dá os mesmos resultados que em Python. Para isso, a função fica no `inventario.js` de uma página que o carregue, como a da secção "O JavaScript entra pela etiqueta `script`". Com a página aberta, escreve-se na consola uma chamada de cada vez. Antes de leres a tabela, prevê o valor de cada chamada.

| Chamada na consola | O que se espera, pelas regras | O que a consola mostra |
| --- | --- | ---: |
| `retirar(6, 2)` | Pedido possível: ficam 4 | `4` |
| `retirar(4, 5)` | Pedido maior do que o que existe: fica tudo igual | `4` |
| `retirar(4, 4)` | Pedido igual ao que existe: é possível, e fica 0 | `0` |
| `retirar(6, 0)` | Pedido de zero: não é positivo, fica tudo igual | `6` |

Os dois primeiros casos são os do guia 01 do M10, e dão o mesmo. Os outros dois testam as fronteiras da condição. O `retirar(4, 4)` confirma que o `<=` deixa retirar tudo. O `retirar(6, 0)` confirma que o `> 0` recusa o zero. Só depois de os quatro casos darem o esperado é que a função passa para a página.

### Passo 3: a página

A página tem o título, uma frase que explica o que fazer, o campo com o rótulo, o botão e a saída. O ficheiro `index.html`, completo:

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
      <p>O caderno A01 começa com 6 unidades. Escreve quantas queres retirar e carrega em Retirar.</p>
      <p>
        <label for="unidades">Unidades a retirar</label>
        <input id="unidades" type="text">
      </p>
      <p>
        <button id="botao-retirar" type="button">Retirar</button>
      </p>
      <p>
        <output id="resultado"></output>
      </p>
    </main>
  </body>
</html>
```

A folha `estilos.css` é a das secções "O CSS dá a apresentação" e "Contraste e foco visível", com as quatro regras juntas no mesmo ficheiro. Os três `id` desta página, `unidades`, `botao-retirar` e `resultado`, são os nomes que o script vai procurar.

### Passo 4: o estado do caderno e os elementos

O programa precisa de guardar a quantidade do caderno entre um clique e o seguinte. Guarda-a numa variável fora de qualquer função, para não se perder quando uma função acaba. A variável é `let`, porque a quantidade muda a cada pedido aceite:

```js partial
let quantidadeCaderno = 6;
```

A seguir, o script encontra os três elementos com que vai trabalhar, como na secção "Ligar um botão a uma função". São `const`, porque cada um aponta sempre para o mesmo elemento da página:

```js partial
const campoUnidades = document.querySelector("#unidades");
const botaoRetirar = document.querySelector("#botao-retirar");
const saida = document.querySelector("#resultado");
```

### Passo 5: mostrar, tratar o clique e ligar

Mostrar a quantidade é uma tarefa que se faz em dois momentos: quando a página abre e depois de cada pedido. Por isso fica numa função, `mostrarQuantidade`, que se chama nos dois sítios. Tratar o clique é outra função, `aoCarregarEmRetirar`, que faz três coisas pela ordem: lê o campo e converte-o em número, pede a retirada e mostra o resultado. Por fim, liga-se o botão à função do clique e mostra-se a quantidade inicial.

O ficheiro `inventario.js`, completo:

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

// A quantidade muda a cada pedido aceite, por isso é let e não const.
let quantidadeCaderno = 6;

const campoUnidades = document.querySelector("#unidades");
const botaoRetirar = document.querySelector("#botao-retirar");
const saida = document.querySelector("#resultado");

/**
 * Mostra na saída da página a quantidade atual do caderno.
 * Não devolve nada: muda o texto do elemento de saída.
 */
function mostrarQuantidade() {
  saida.textContent = "Unidades do caderno A01: " + quantidadeCaderno + ".";
}

/**
 * Trata o clique no botão Retirar: lê o campo, faz o pedido e mostra o resultado.
 * Não devolve nada: muda a quantidade do caderno e o texto da saída.
 */
function aoCarregarEmRetirar() {
  // O campo dá sempre texto, como "2"; as contas e as comparações pedem o número 2.
  const unidades = Number(campoUnidades.value);
  quantidadeCaderno = retirar(quantidadeCaderno, unidades);
  mostrarQuantidade();
}

// Sem parênteses: o browser chama a função em cada clique, e não agora.
botaoRetirar.addEventListener("click", aoCarregarEmRetirar);

// A saída começa vazia no HTML; esta chamada mostra a quantidade inicial.
mostrarQuantidade();
```

Leitura guiada: segue o script pela ordem em que o browser o corre, depois de ler o HTML.

1. O browser lê a função `retirar` e as duas outras funções, sem as correr.
2. Cria a variável `quantidadeCaderno`, com 6, e os três `const` com os elementos da página.
3. Liga o botão à função `aoCarregarEmRetirar`.
4. Chama `mostrarQuantidade`, e a saída passa a mostrar `Unidades do caderno A01: 6.`
5. O script chegou ao fim, mas a página continua aberta. A partir daqui, cada clique no botão faz o browser chamar `aoCarregarEmRetirar`.

Dentro de `aoCarregarEmRetirar`, a linha `quantidadeCaderno = retirar(quantidadeCaderno, unidades);` é a mesma que, em Python, era `quantidade_caderno = retirar(quantidade_caderno, 2)`. Lê-se da direita para a esquerda: primeiro a função calcula o que fica, e só depois a atribuição guarda esse valor na variável. Sem o `quantidadeCaderno =` à esquerda, o resultado perdia-se, e o caderno ficava sempre com 6.

### Passo 6: testar a página com os mesmos casos

Com os três ficheiros guardados na mesma pasta, abre-se a página e faz-se esta sequência de pedidos, sem recarregar entre eles. Antes de leres a última coluna, prevê o que a saída mostra depois de cada pedido.

| Pedido | Escreves no campo | O que se espera | A saída mostra |
| --- | --- | --- | --- |
| Ao abrir a página | nada | O caderno com 6 | `Unidades do caderno A01: 6.` |
| 1 | `2` | Aceite: ficam 4 | `Unidades do caderno A01: 4.` |
| 2 | `5` | Recusado: ficam 4 | `Unidades do caderno A01: 4.` |
| 3 | `4` | Aceite: fica 0 | `Unidades do caderno A01: 0.` |
| 4 | `1` | Recusado: fica 0 | `Unidades do caderno A01: 0.` |

Os pedidos 1 e 2 dão o mesmo que o programa de Python do guia 01 do M10, e por isso a tradução está certa. Os pedidos 3 e 4 confirmam as fronteiras na página.

Falta experimentar o que alguém pode escrever por engano. Recarrega-se a página, para o caderno voltar às 6 unidades, e faz-se outra sequência:

| Pedido | Escreves no campo | `Number` dá | A saída mostra |
| --- | --- | --- | --- |
| 1 | `abc` | `NaN` | `Unidades do caderno A01: 6.` |
| 2 | nada | `0` | `Unidades do caderno A01: 6.` |
| 3 | `-1` | `-1` | `Unidades do caderno A01: 6.` |
| 4 | `2,5` | `NaN` | `Unidades do caderno A01: 6.` |
| 5 | `2.5` | `2.5` | `Unidades do caderno A01: 3.5.` |

Os quatro primeiros pedidos são recusados, e a quantidade fica igual. O `abc` e o `2,5` dão `NaN`, e as duas comparações da condição, com `>` e com `<=`, dão `false`. O campo vazio dá 0, e o `-1` também não é positivo.

O quinto pedido mostra o que esta página ainda não protege. O `2.5` é um número positivo e não maior do que 6, e por isso a condição aceita-o. O caderno fica com 3.5 unidades, uma quantidade impossível. É exatamente a limitação que o programa de Python do guia 01 do M10 também tinha: a função não verifica se o pedido é inteiro. Há outra limitação: quem faz um pedido recusado não fica a saber que foi recusado, porque a página mostra sempre a mesma frase. As duas resolvem-se no tema 03, quando a classe do artigo passar a proteger a regra da quantidade inteira não negativa, como fizeste em Python no M10.

## Erros frequentes

Para cada erro, o que se vê, porque acontece e como se corrige. Os erros da página quase sempre aparecem na consola: abre-a antes de mais nada.

### A página não muda depois de mudares o ficheiro

O que se vê: mudaste o HTML, o CSS ou o JavaScript, e o browser mostra a página como estava. Porque acontece: o ficheiro não foi guardado, ou a página não foi recarregada. Como se corrige: no VS Code, confirma que o separador do ficheiro não tem a bola branca de "por guardar", e guarda. Depois recarrega a página no browser, com F5 ou Ctrl+R no Windows, ou com Cmd+R no macOS.

### O ficheiro abre no editor, ou como texto, e não como página

O que se vê: o duplo clique abre o código, em vez da página. Porque acontece: fizeste o duplo clique dentro do VS Code, que abre os ficheiros para os editares. Ou o ficheiro chama-se, na verdade, `index.html.txt`. Como se corrige: abre a página pela janela de ficheiros do computador, como diz "Abrir a página". Se o nome tiver `.txt` no fim, muda-o no VS Code para `index.html`.

### A página aparece sem estilos

O que se vê: o texto volta à letra do browser, encostado à margem, e o botão fica cinzento. Na consola aparece `Failed to load resource: net::ERR_FILE_NOT_FOUND` (em português, falhou o carregamento do recurso: ficheiro não encontrado), com o caminho do ficheiro que o browser procurou. Porque acontece: o `href` do `link` não corresponde ao nome do ficheiro, por exemplo `estilo.css` em vez de `estilos.css`, ou o ficheiro está noutra pasta. Como se corrige: compara, letra a letra, o nome no `href` com o nome do ficheiro no VS Code.

### O botão não faz nada, e a consola diz que não encontrou o ficheiro do script

O que se vê: a saída fica vazia, mesmo ao abrir a página, e a consola mostra `Failed to load resource: net::ERR_FILE_NOT_FOUND` com o nome do ficheiro de JavaScript. Porque acontece: o `src` do `script` não corresponde ao nome do ficheiro. Como se corrige: compara o nome no `src` com o nome do ficheiro, letra a letra, e confirma que os dois ficheiros estão na mesma pasta.

### `Uncaught SyntaxError: Unexpected identifier 'unidades'`

O que se vê: a consola mostra esta mensagem logo ao abrir a página, e nada no script funciona, nem a quantidade inicial. O `Uncaught` (em inglês, não apanhado) quer dizer que ninguém tratou o erro. O `SyntaxError: Unexpected identifier` quer dizer erro de sintaxe: um nome inesperado. Porque acontece: é um erro de escrita, e o browser não corre nenhuma linha de um script com erros de escrita. É muitas vezes um hábito do Python, como `if unidades > 0 and unidades <= quantidade:`, sem parênteses, com `and` e com dois pontos. O nome entre plicas é o sítio onde o browser deixou de perceber o código. Como se corrige: vai à linha que a mensagem indica e escreve a condição em JavaScript: `if (unidades > 0 && unidades <= quantidade) {`.

### `Uncaught SyntaxError: Unexpected end of input`

O que se vê: esta mensagem logo ao abrir a página, a apontar para a última linha do script. Quer dizer erro de sintaxe: fim inesperado do texto. Porque acontece: falta fechar uma chaveta, ou um parêntese, e o browser chegou ao fim do ficheiro à espera dela. A linha indicada é a última, mas a chaveta em falta está antes. Como se corrige: percorre o ficheiro e confirma que cada `{` tem a sua `}`. Põe o cursor ao lado de cada chaveta, e o VS Code marca a que lhe corresponde.

### `Uncaught TypeError: Cannot read properties of null (reading 'addEventListener')`

O que se vê: a quantidade inicial não aparece, e o botão não faz nada. A mensagem quer dizer erro de tipo: não é possível ler propriedades de `null`, ao ler `addEventListener`. Porque acontece: é um erro de execução. O `querySelector` não encontrou nenhum elemento com aquele `id` e devolveu `null`. O script só rebenta mais abaixo, na linha que tenta usar esse `null`. A causa costuma ser um `id` escrito de maneira diferente nos dois ficheiros, como `#botao-retira` no script e `id="botao-retirar"` no HTML. Como se corrige: na consola, escreve o nome do `const` do elemento, como `botaoRetirar`, e carrega em Enter. Se aparecer `null`, compara o seletor do `querySelector` com o `id` do HTML, letra a letra.

### `Uncaught TypeError: Assignment to constant variable.`

O que se vê: a página abre bem, mas, ao carregar no botão, aparece esta mensagem, e a quantidade não muda. Quer dizer erro de tipo: atribuição a uma variável constante. Porque acontece: a variável que guarda a quantidade foi declarada com `const`, e a função do clique tenta dar-lhe outro valor. Como se corrige: declara-a com `let`, porque é uma variável que muda.

### `Uncaught ReferenceError: quantidade is not defined`

O que se vê: esta mensagem, a apontar para uma linha do script. Quer dizer erro de referência: `quantidade` não está definido. Porque acontece: o nome usado não existe, porque está mal escrito, com outra maiúscula ou com outras letras, ou porque ninguém o declarou. Como se corrige: compara o nome dessa linha com o nome da declaração, letra a letra. Lembra-te de que `quantidadeCaderno` e `quantidadecaderno` são nomes diferentes.

### O botão não faz nada, e a consola não mostra nenhum erro

O que se vê: a quantidade inicial aparece, mas os cliques não mudam nada, e a consola está limpa. Porque acontece: é um erro de lógica. Quase sempre, a função foi passada com parênteses: `addEventListener("click", aoCarregarEmRetirar())`. Com os parênteses, a função correu uma vez, ao carregar a página, e o que se deu ao browser foi o valor que ela devolveu, `undefined`. O browser não tem nenhuma função para chamar nos cliques. Como se corrige: tira os parênteses, e escreve só o nome da função.

### A saída mostra números colados, como `61` em vez de `7`

O que se vê: uma conta dá algarismos juntos, em vez de somar. Porque acontece: um dos valores da conta é um texto, como o `value` de um campo, e o `+` com um texto junta em vez de somar. Como se corrige: converte o texto em número com `Number` antes da conta. Numa mensagem, põe a conta entre parênteses: `"Total: " + (a + b)`.

### O `for` mostra `0`, `1` e `2` em vez dos valores do array

O que se vê: um ciclo sobre `[2, 5, 1]` mostra `0`, `1` e `2`. Porque acontece: escreveste `for (const pedido in pedidos)`, com `in`, como em Python. Em JavaScript, o `for...in` percorre as posições do array, e não os valores. Como se corrige: escreve `of` em vez de `in`.

### `ReferenceError: document is not defined`

O que se vê: tentaste executar o `inventario.js` no editor, como fazias com o Python, e aparece esta mensagem, ou o editor pergunta que programa usar para o correr. Porque acontece: o editor tenta correr o ficheiro fora do browser. Lá não há página nenhuma, e por isso o `document` não existe. Como se corrige: não corras o ficheiro no editor. Abre o `index.html` no browser, que carrega o script com a página.

## Palavras novas deste guia

- Editor: o programa onde escreves e guardas os ficheiros, como o VS Code.
- Browser (navegador): o programa que abre as páginas, mostra-as e corre o JavaScript delas.
- HTML: a linguagem que diz o que a página tem, a estrutura.
- CSS: a linguagem que diz como a página se apresenta.
- JavaScript: a linguagem que diz o que a página faz quando alguém a usa, o comportamento.
- Caminho relativo: um caminho que parte da pasta do ficheiro onde está escrito, como `estilos.css`.
- Elemento: uma parte da página marcada com o que é, como um título ou um parágrafo.
- Etiqueta (*tag*): a marca que abre ou fecha um elemento, como `<p>` e `</p>`.
- Atributo: informação extra dentro da etiqueta de abertura, na forma `nome="valor"`.
- Controlo: uma parte da página com que a pessoa interage, como um campo ou um botão.
- Campo: o elemento `input`, onde a pessoa escreve.
- `id`: o nome único de um elemento dentro da página.
- Rótulo: o elemento `label`, que diz o que se escreve num campo e se liga a ele pelo `for`.
- Leitor de ecrã: o programa que lê a página em voz alta a quem não vê bem.
- Botão: o elemento `button`, que faz uma ação na página.
- Saída: o elemento `output`, onde aparece um resultado.
- Foco: o elemento que, num dado momento, recebe as teclas que carregas.
- Folha de estilos: o ficheiro de CSS que a página carrega.
- Regra: um seletor e as propriedades que ele recebe, entre chavetas.
- Seletor: a parte da regra que escolhe os elementos, como `body` ou `button`.
- Propriedade e valor: o que se muda num elemento e como, na forma `color: #ffffff;`.
- Herança: uma propriedade dada a um elemento que passa para os elementos que estão dentro dele.
- Contraste: a diferença de luminosidade entre a cor do texto e a do fundo, medida de 1 para 1 a 21 para 1.
- Contorno: a linha à volta do elemento que tem o foco, o `outline`.
- Consola: a parte das ferramentas do programador onde aparecem os `console.log` e os erros do JavaScript.
- Ferramentas do programador (*DevTools*): a parte do browser para quem constrói páginas, que se abre com F12 ou Cmd+Option+I.
- `undefined`: o valor que quer dizer "sem valor", como o `None` do Python.
- Declarar: anunciar uma variável nova, com `const` ou com `let`.
- `const`: declara um nome que não recebe outro valor.
- `let`: declara um nome que pode receber outro valor.
- `number`, `string` e `boolean`: os tipos dos números, dos textos e dos valores lógicos.
- Chavetas: os sinais `{` e `}`, que marcam onde começa e acaba um bloco.
- JSDoc: a documentação de uma função, entre `/**` e `*/`, com `@param` e `@returns`.
- Array: a lista do JavaScript, com os valores entre parênteses retos.
- `document`: a página, tal como o browser a guarda enquanto a mostra.
- `null`: o valor que quer dizer "nenhum objeto", que o `querySelector` devolve quando não encontra o elemento.
- Evento: uma coisa que acontece na página, como um clique num botão.
- `value`: o texto escrito num campo, sempre do tipo `string`.
- `textContent`: o texto dentro de um elemento, escrito sempre como texto simples.
- `Number`: converte um texto num número.
- `NaN`: o valor que quer dizer "não era um número", que dá `false` nas comparações com `<`, `>`, `<=`, `>=` e `===`.

## Verificar o que aprendeste

1. Uma colega mudou a cor do botão no `estilos.css`, carregou em F5 e a página ficou igual. Diz duas causas possíveis e como confirmas cada uma.
2. Que ficheiro mudas para pôr um segundo parágrafo na página? E para mudar a cor desse parágrafo? E para o parágrafo mudar de texto quando se carrega no botão?
3. Num HTML, o rótulo tem `for="quantidade"` e o campo tem `id="qtd"`. O que deixa de funcionar, e para quem?
4. Porque é que o contorno de foco nunca se apaga sem pôr outro no lugar?
5. O que mostra a consola com `console.log("Total: " + 2 + 3)`? Como mudas a instrução para mostrar `Total: 5`?
6. Num programa, a variável `pedidos` conta os pedidos feitos e a variável `codigo` guarda o código do artigo. Qual declaras com `const` e qual com `let`? Porquê?
7. Traduz para JavaScript esta condição de Python: `if unidades <= 0 or unidades > quantidade:`.
8. Um script tem `const botao = document.querySelector("#guardar");`, e a consola mostra `Cannot read properties of null (reading 'addEventListener')`. Escreve uma hipótese para a causa e diz como a verificas na consola.
9. Na página do exemplo guiado, alguém escreve `3` duas vezes seguidas, sem recarregar. O que mostra a saída depois de cada pedido?
10. Explica, por palavras tuas, a diferença entre `addEventListener("click", aoCarregarEmRetirar)` e `addEventListener("click", aoCarregarEmRetirar())`.

## O que vem a seguir

Para praticar este tema, faz o [laboratório](01-primeira-pagina-com-javascript-laboratorio.md) e depois a [ficha de exercícios](01-primeira-pagina-com-javascript-exercicios.md). O tema seguinte é Do objeto literal à classe. Nele, o caderno deixa de estar espalhado por variáveis soltas e passa a ser um objeto, como fizeste em Python no M10, agora com as classes do JavaScript.

## Para saber mais

- [HTML, na MDN](https://developer.mozilla.org/en-US/docs/Web/HTML): a referência de todos os elementos e atributos do HTML, em inglês, com exemplos.
- [CSS, na MDN](https://developer.mozilla.org/en-US/docs/Web/CSS): a referência das propriedades e dos seletores do CSS, em inglês.
- [Guia de JavaScript, na MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide): o guia da linguagem, em inglês, com as variáveis, as condições, os ciclos e as funções explicados com mais pormenor.
- [Calculadora de contraste da WebAIM](https://webaim.org/resources/contrastchecker/): escreves duas cores em hexadecimal e vês a razão de contraste e se chega aos mínimos.

![Rodapé](../imagens/rodape.png)

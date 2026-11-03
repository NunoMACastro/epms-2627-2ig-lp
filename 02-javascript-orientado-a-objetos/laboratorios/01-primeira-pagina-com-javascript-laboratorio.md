![Cabeçalho](../../imagens/cabecalho.png)

# Laboratório: A primeira página com JavaScript

Laboratório do tema A primeira página com JavaScript, do módulo M11, Introdução à Linguagem de Programação Orientada por Objetos. Vais construir, a partir de uma pasta vazia, uma página onde se retiram unidades do caderno A01 do inventário, com um campo, um botão e o resultado na página. Cada passo diz o que fazer, porquê e o que deves ver, e avanças ao teu ritmo. O que não acabares na aula, acabas em casa ou na aula seguinte. Tudo o que precisas está aqui; o [guia do tema](../01-primeira-pagina-com-javascript.md) tem a teoria completa, para quem quiser saber mais.

## O que vais construir

No fim, tens uma pasta `primeira-pagina` com três ficheiros, cada um escrito numa linguagem diferente. O `index.html` diz o que a página tem, o `estilos.css` diz como ela se apresenta, e o `inventario.js` diz o que ela faz. A página mostra o caderno A01 com 6 unidades. Quando escreves um número no campo e carregas em "Retirar", a página aplica as regras do inventário e mostra o que fica. As regras são as do M10, e a função que as aplica é a `retirar` que escreveste em Python, agora traduzida para JavaScript.

Pelo caminho, ficas a saber abrir uma página no browser e ler a consola, onde aparecem os resultados e os erros do JavaScript. Ficas também a saber encontrar a causa dos erros mais comuns de uma página.

| Fase | O que muda | O que funciona no fim |
| --- | --- | --- |
| 1 | Crias o `index.html`, com o título e um parágrafo | A página abre no browser, com o título no separador |
| 2 | Acrescentas o rótulo, o campo, o botão e a saída | O rótulo põe o cursor no campo, e tudo se usa com o teclado; o botão ainda não faz nada |
| 3 | Crias o `estilos.css` e ligas-o à página | A página fica legível, com bom contraste e o foco bem visível |
| 4 | Crias o `inventario.js` e ligas-o à página | A consola mostra as primeiras mensagens do script |
| 5 | Traduzes a função `retirar` de Python para JavaScript | A consola mostra os mesmos resultados que o programa de Python |
| 6 | Ligas o botão à função | Cada clique retira unidades, e a página mostra o que fica |

```text
primeira-pagina/
├── index.html
├── estilos.css
└── inventario.js
```

Esta é a árvore da pasta no fim do laboratório.

Em todas as fases trabalhas da mesma maneira. Antes de abrires ou recarregares a página, pensa no que esperas ver. Depois compara. Quando o resultado for diferente da tua previsão, procura a razão da diferença antes de continuares. Várias fases pedem-te para provocares um erro de propósito: faz a alteração, observa e desfaz a alteração antes de seguires.

## Palavras que vais usar

- Editor: o programa onde escreves e guardas os ficheiros. Neste laboratório é o VS Code. Para saber mais, vê a secção "O que muda quando o programa corre no browser" do [guia](../01-primeira-pagina-com-javascript.md).
- Browser (navegador): o programa que abre as páginas, como o Chrome, o Edge ou o Firefox. É ele que mostra a página e corre o JavaScript dela.
- HTML: a linguagem que diz o que a página tem, como um título, um parágrafo ou um botão.
- CSS: a linguagem que diz como a página se apresenta: a letra, as cores, os espaços.
- JavaScript: a linguagem que diz o que a página faz quando alguém a usa.
- Elemento e etiqueta: um elemento é uma parte da página marcada com o que é. Escreve-se entre uma etiqueta de abertura, como `<p>`, e uma de fecho, como `</p>`. Em inglês, a etiqueta diz-se *tag*.
- Atributo: informação extra dentro da etiqueta de abertura, na forma `nome="valor"`, como `lang="pt-PT"`.
- `id`: o nome único de um elemento dentro da página.
- Campo e rótulo: o campo (`input`) é a caixa onde se escreve, e o rótulo (`label`) é o texto que diz o que se escreve lá.
- Botão e saída: o botão (`button`) faz uma ação, e a saída (`output`) é o sítio onde aparece um resultado.
- Foco: o elemento que, num dado momento, recebe as teclas que carregas. A tecla Tab passa-o para o elemento seguinte.
- Regra de CSS: um seletor, que escolhe os elementos, e as propriedades que eles recebem, entre chavetas.
- Contraste: a diferença de luminosidade entre a cor do texto e a do fundo. Mede-se de 1 para 1 a 21 para 1, e o texto normal precisa de pelo menos 4,5 para 1.
- Consola: a parte do browser onde aparecem as mensagens do JavaScript e os erros. Faz parte das ferramentas do programador, que em inglês se chamam *DevTools*.
- `const` e `let`: as duas palavras que declaram uma variável nova em JavaScript. O `const` é para um nome que não recebe outro valor, e o `let` para um que recebe.
- JSDoc: a documentação de uma função em JavaScript, entre `/**` e `*/`, logo antes dela. Faz o papel da docstring do Python.
- Evento: uma coisa que acontece na página, como um clique num botão.
- Mensagem de erro: o texto que o browser escreve na consola quando o JavaScript falha. Diz o tipo de erro e, à direita, o ficheiro e o número da linha.

## O que precisas

- O VS Code, para criar e escrever os três ficheiros. Confirma que o tens: abre-o, e no menu `Help` escolhe `About` (no macOS, o menu `Code` e `About Visual Studio Code`). Aparece uma janela com o número da versão, o que quer dizer que o editor está instalado.
- Um browser atual: o Chrome, o Edge ou o Firefox. Confirma que o tens abrindo-o. As mensagens de erro deste laboratório são as do Chrome e do Edge, que escrevem igual. O Firefox usa outras palavras, mas mostra as mensagens no mesmo sítio, com o ficheiro e a linha.

O laboratório começa de uma pasta vazia: não precisas de nenhum ficheiro anterior. A página abre-se com um duplo clique, e não precisas de instalar mais nada.

Os nomes dos menus e dos botões do VS Code estão em inglês, como aparecem no VS Code acabado de instalar. São os de 26 de outubro de 2026: uma versão mais recente pode mudar algum.

## Se alguma coisa falhar

1. Guardaste o ficheiro? O browser mostra o ficheiro tal como está guardado. No VS Code, um separador com uma bola branca no lugar da cruz tem alterações por guardar. Guarda com Ctrl+S no Windows ou Cmd+S no macOS.
2. Recarregaste a página? A página no browser não muda sozinha. Recarrega com F5 ou Ctrl+R no Windows, ou com Cmd+R no macOS.
3. A consola mostra algum erro? Abre-a, com F12 no Windows ou Cmd+Option+I no macOS, e escolhe o separador `Console`. Lê a mensagem a vermelho e procura-a em [Problemas frequentes](#problemas-frequentes).
4. Os três ficheiros estão na mesma pasta, com os nomes certos? Confirma no VS Code, na barra lateral, que estão os três dentro de `primeira-pagina`, escritos exatamente como o laboratório diz.
5. Desfizeste o erro provocado na fase anterior? Cada fase parte dos ficheiros como estavam na paragem anterior. Se te perderes, copia o último ficheiro que o laboratório mostra completo e refaz os passos que faltam.

## Preparar o projeto

1. Cria a pasta onde vai ficar a página. Na pasta onde guardas os trabalhos de LP, cria uma pasta nova chamada `primeira-pagina`, sem espaços nem acentos.
2. Abre a pasta no VS Code. No menu `File`, escolhe `Open Folder...` e seleciona a pasta `primeira-pagina`. Assim, o VS Code mostra na barra lateral, no `Explorer`, os ficheiros dessa pasta, e os ficheiros novos ficam lá dentro. Se o VS Code perguntar se confias nos autores dos ficheiros da pasta, escolhe `Yes, I trust the authors`: a pasta é tua e está vazia. O que deves ver: na barra lateral, o nome da pasta, em maiúsculas, sem ficheiros por baixo.

## Fase 1: A estrutura da página em HTML

Uma página web é um ficheiro de texto escrito em HTML. O HTML marca cada parte do texto com o que ela é: o título, um parágrafo. Cada parte marcada é um elemento, escrito entre uma etiqueta de abertura e uma de fecho. O browser lê essas marcas e mostra cada parte da maneira certa. Nesta fase escreves a estrutura mínima de uma página e abre-la no browser. Para saber mais, lê a secção "O HTML dá a estrutura da página" do [guia](../01-primeira-pagina-com-javascript.md).

1. Cria o ficheiro da página. No `Explorer` do VS Code, passa o rato por cima do nome da pasta e carrega no ícone `New File...`. Escreve `index.html` e carrega em Enter. O nome `index.html` é o que se dá, por costume, à página principal de uma pasta, e a extensão `.html` diz ao computador que o ficheiro é uma página. O que deves ver: o ficheiro na barra lateral, aberto e vazio à direita.

2. Escreve no `index.html` este conteúdo. É o ficheiro completo. Enquanto escreves, o VS Code fecha sozinho algumas etiquetas, chavetas e aspas: quando escreves `<h1>`, aparece logo `</h1>` a seguir. No fim, confirma que nada ficou a dobrar, como `</h1></h1>`.

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
         <p>O caderno A01 começa com 6 unidades. Escreve quantas queres retirar e carrega em Retirar.</p>
       </main>
     </body>
   </html>
   ```

   Leitura guiada: lê a página de fora para dentro, como caixas dentro de caixas. A primeira linha diz ao browser que é uma página do HTML atual. O elemento `html` contém tudo, e o atributo `lang="pt-PT"` diz a língua da página. Os leitores de ecrã, os programas que leem a página a quem não a vê bem, usam-na para pronunciar bem as palavras. O `head` guarda informação sobre a página, que não aparece no meio dela. O `meta charset="utf-8"` faz os acentos aparecerem bem, o `meta name="viewport"` faz um telemóvel mostrar a página à largura do ecrã, e o `title` é o texto do separador. Os dois `meta` não têm etiqueta de fecho. O `body` contém o que aparece na página: o `main`, que marca o conteúdo principal, com o título principal, `h1`, e um parágrafo, `p`. Os espaços no início das linhas servem só para se ver que caixa está dentro de que caixa: o browser ignora-os.

3. Guarda o ficheiro, com Ctrl+S no Windows ou Cmd+S no macOS. O que deves ver: a bola branca do separador volta a ser uma cruz.

4. Antes de abrires a página, prevê: que texto aparece no separador do browser, e que texto aparece dentro da página? Depois abre-a. No `Explorer` do VS Code, carrega com o botão direito em `index.html` e escolhe `Reveal in File Explorer`, no Windows, ou `Reveal in Finder`, no macOS. Abre-se a janela de ficheiros do computador, com o ficheiro selecionado. Faz duplo clique nele. O duplo clique tem de ser nesta janela: dentro do VS Code, o duplo clique abre o ficheiro para o editares, e não no browser.

   O que deves ver: o browser abre, com "Inventário da sala" no separador. Dentro da página aparece o mesmo texto em letra grande e grossa e, por baixo, o parágrafo em letra normal. A barra de endereço mostra um endereço que começa por `file:///`, o que quer dizer que o browser está a mostrar um ficheiro deste computador. A página não foi para a internet.

   Se o ficheiro abrir num programa de texto, ou se o browser mostrar o código em vez da página, vê [Problemas frequentes](#problemas-frequentes).

5. Experimenta o ciclo de trabalho de uma página. No VS Code, muda a palavra "sala" do `h1` para "escola", e não guardes. Olha para o browser. Depois guarda, e olha outra vez. Por fim, recarrega a página no browser, com F5 ou Ctrl+R no Windows, ou com Cmd+R no macOS.

   O que deves ver: a página só muda depois de guardares e de recarregares. O browser mostra o ficheiro como estava guardado no momento em que carregou a página. Volta a pôr "sala" no `h1`, guarda e recarrega.

### Paragem 1

A página abre no browser, com "Inventário da sala" no separador e no título, e o parágrafo por baixo. Sabes que cada mudança passa por três passos: mudar no editor, guardar e recarregar no browser.

Pensa antes de continuares: o texto "Inventário da sala" aparece duas vezes no ficheiro. Qual das duas é o separador do browser, e qual é o título dentro da página? A resposta: o do `title`, dentro do `head`, é o separador. O do `h1`, dentro do `body`, é o título da página. Se mudares só um deles, só uma das duas coisas muda.

## Fase 2: Os controlos da página

Para retirar unidades, a página tem de perguntar quantas, e de ter um sítio para o resultado. O HTML tem elementos próprios para isso. O campo, onde se escreve, e o botão, que faz a ação, são os controlos, as partes da página com que a pessoa interage. O rótulo diz o que se escreve no campo, e a saída é onde aparece o resultado. Nesta fase acrescentas os quatro. Ainda não funcionam juntos: o botão não faz nada até à fase 6. Para saber mais, lê a secção "Rótulo, campo, botão e saída" do [guia](../01-primeira-pagina-com-javascript.md).

1. Acrescenta os controlos à página. No `index.html`, a seguir à linha do parágrafo `<p>O caderno A01 ...</p>` e antes de `</main>`, acrescenta estas linhas:

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

   Leitura guiada: o `input` é o campo, e o `type="text"` diz que aceita qualquer texto. Como o `meta`, o `input` não tem etiqueta de fecho: nunca se escreve `</input>`. O `id="unidades"` dá ao campo um nome único dentro da página. O `label` é o rótulo, e o `for="unidades"` liga-o ao elemento cujo `id` é `unidades`, o campo. O `button` é o botão, com o `id` `botao-retirar`. O `type="button"` diz que é um botão simples, que só faz o que o JavaScript mandar. O `output` é a saída, com o `id` `resultado`, e começa vazia. Cada grupo fica dentro de um `p`, para aparecer numa linha própria. Os três `id`, `unidades`, `botao-retirar` e `resultado`, são os nomes que o JavaScript vai usar na fase 6 para encontrar estes elementos.

   O `index.html` completo, como deve estar agora:

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

2. Guarda e recarrega a página. Antes de experimentares, prevê duas coisas: o que acontece quando clicas no texto "Unidades a retirar", e o que acontece quando carregas no botão "Retirar".

   O que deves ver: o rótulo e o campo numa linha, o botão na linha de baixo, e a saída, ainda invisível porque está vazia. Ao clicares no texto do rótulo, o cursor aparece dentro do campo, pronto para escreveres: é a ligação do `for` ao `id`. Ao carregares no botão, não acontece nada, e está certo. Ninguém disse ainda à página o que fazer com ele.

3. Experimenta a página só com o teclado. Clica numa parte vazia da página e carrega na tecla Tab duas vezes, e depois em Shift+Tab. Se carregares mais vezes no Tab, o foco sai da página para a barra do browser: clica outra vez numa parte vazia da página para voltares.

   O que deves ver: com o Tab, o foco passa para o campo e depois para o botão. O browser desenha uma linha à volta do elemento que tem o foco. Com o foco no campo, o que escreves entra no campo. Com Shift+Tab, o foco volta para trás. Há pessoas que só usam o teclado, e estes elementos já funcionam assim sem nenhum trabalho teu. Num Mac, o Safari e o Firefox só levam o foco ao botão com o Tab se a navegação por teclado estiver ligada nas definições do sistema. Se o foco saltar o botão, é essa a razão.

4. Provoca um erro de propósito, para veres para que serve o `for`. No rótulo, muda `for="unidades"` para `for="unidade"`, sem o "s". Guarda, recarrega e clica no texto do rótulo.

   O que deves ver: o cursor já não vai para o campo, e não aparece nenhuma mensagem de erro. O `for` aponta agora para um `id` que não existe, e o browser não liga o rótulo a nada. Quem usa um leitor de ecrã, o programa que lê a página em voz alta, também deixa de ouvir o rótulo quando chega ao campo. Repara que o HTML não avisa dos erros: a página só fica diferente. Volta a pôr `for="unidades"`, guarda e recarrega.

### Paragem 2

A página tem o título, o parágrafo, o campo com o rótulo, o botão e a saída. Clicar no rótulo põe o cursor no campo, e o Tab percorre o campo e o botão. O botão ainda não faz nada.

Pensa antes de continuares: porque é que o `id` do campo e o `for` do rótulo têm de ser escritos exatamente da mesma maneira? A resposta: o browser liga o rótulo ao elemento cujo `id` é igual, letra a letra, ao valor do `for`. Uma letra diferente quer dizer outro nome, e o rótulo fica sem campo.

## Fase 3: A apresentação com uma folha de CSS

A página funciona, mas tem o aspeto que o browser escolhe. O texto fica encostado à margem, e o campo e o botão têm uma letra mais pequena do que a do resto. O CSS serve para escolher a apresentação. Escreve-se num ficheiro à parte, a folha de estilos, feito de regras. Cada regra tem um seletor, que escolhe os elementos, e propriedades, cada uma com o seu valor, que dizem como esses elementos aparecem. As cores escolhem-se também pelo contraste, para a página se ler bem. Para saber mais, lê as secções "O CSS dá a apresentação" e "Contraste e foco visível" do [guia](../01-primeira-pagina-com-javascript.md).

1. Cria a folha de estilos. No `Explorer`, com o rato sobre o nome da pasta, carrega em `New File...` e cria `estilos.css`. Escreve nele este conteúdo, que é o ficheiro completo:

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

   input:focus-visible,
   button:focus-visible {
     outline: 3px solid #b35c00;
     outline-offset: 2px;
   }
   ```

   Leitura guiada: a primeira linha é um comentário de CSS, entre `/*` e `*/`. Depois vêm quatro regras.

   - A regra `body` vale para a página toda. Escolhe a letra do sistema (`font-family`) e põe mais espaço entre as linhas (`line-height`). Dá ao texto um cinzento quase preto (`color`) num fundo branco (`background-color`). Põe também uma margem à volta (`margin`). As cores escrevem-se com um `#` e três pares de símbolos, para o vermelho, o verde e o azul. Cada par é um número em hexadecimal, uma forma de escrever números com os algarismos de 0 a 9 e as letras de `a` a `f`. Vai de `00`, nada dessa cor, a `ff`, o máximo. O `2rem` vale duas vezes o tamanho da letra normal do browser, cerca de 32 píxeis.
   - A regra `input, button` vale para o campo e para o botão. O `font: inherit` manda-os usar a letra da página, em vez da letra mais pequena que o browser lhes dá. O `padding` põe espaço por dentro, entre o texto e a borda.
   - A regra `button` pinta o botão de azul-escuro, com o texto branco.
   - A última regra só vale quando o campo ou o botão têm o foco e o browser mostra o contorno, como quando se chega lá com o Tab. Desenha um contorno (`outline`) laranja-escuro, contínuo e com 3 píxeis de grossura, afastado 2 píxeis do elemento.

   As cores foram escolhidas pelo contraste. O texto quase preto no branco tem 16,5 para 1, e o branco no azul-escuro tem 8,3 para 1. O contorno laranja no branco tem 4,7 para 1. Todos passam dos 4,5 para 1 que o texto normal pede.

2. Liga a folha à página. O browser só usa uma folha de estilos se a página lhe disser onde ela está. No `index.html`, dentro do `head`, a seguir à linha do `title`, acrescenta esta linha:

   ```html
       <link rel="stylesheet" href="estilos.css">
   ```

   Leitura guiada: o `link` liga outro ficheiro à página, e não tem etiqueta de fecho. O `rel="stylesheet"` diz que o ficheiro ligado é uma folha de estilos. O `href` é o caminho do ficheiro. O caminho `estilos.css`, sozinho, quer dizer "o ficheiro com este nome, na mesma pasta que a página".

3. Guarda os dois ficheiros. Antes de recarregares, prevê: o que muda no texto, no campo e no botão? Depois recarrega.

   O que deves ver: a letra muda para a do sistema operativo, com mais espaço entre as linhas, e a página tem uma margem à volta. O campo e o botão têm letra do mesmo tamanho que o resto, com espaço por dentro. O botão é azul-escuro, com letras brancas.

4. Confirma o foco visível. Clica numa parte vazia da página e carrega em Tab duas vezes. O que deves ver: o campo, e depois o botão, rodeados por uma linha laranja grossa, afastada da borda. Quem usa o teclado vê sempre onde está.

5. Vê que regras se aplicam ao botão. Carrega com o botão direito no botão "Retirar" e escolhe `Inspecionar` (num browser em inglês, `Inspect`). Abre-se, ao lado ou por baixo da página, uma parte do browser com o HTML da página, e o elemento `button` marcado. Ao lado do HTML, no separador `Styles` (ou `Estilos`), estão as regras de CSS do botão.

   O que deves ver: a regra `button`, com a cor branca, e a regra `input, button`, com o `font` e o `padding`. Mais abaixo, a cor quase preta do `body` aparece riscada, na parte das propriedades herdadas. O texto do `body` passa para os elementos que estão dentro dele, o que se chama herança. Mas a regra `button` escolhe o botão diretamente, e um valor dado diretamente ganha ao valor herdado. Fecha esta parte do browser com a cruz do canto, ou com F12 no Windows, ou com Cmd+Option+I no macOS.

6. Provoca um erro de propósito: no `link` do `index.html`, muda `href="estilos.css"` para `href="estilo.css"`, sem o "s". Guarda e recarrega.

   O que deves ver: a página volta ao aspeto da fase 2, sem margem, com a letra do browser e o botão cinzento. O browser procurou um ficheiro `estilo.css`, que não existe, e mostrou a página sem estilos. Na página não aparece nenhuma mensagem. Na fase seguinte vais ver onde o browser escreve estes avisos. Para corrigir, compara, letra a letra, o nome no `href` com o nome do ficheiro na barra lateral do VS Code. Volta a pôr `href="estilos.css"`, guarda e recarrega.

### Paragem 3

O `index.html` completo, como deve estar agora:

```html
<!doctype html>
<html lang="pt-PT">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Inventário da sala</title>
    <link rel="stylesheet" href="estilos.css">
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

A página tem margem, a letra do sistema e o botão azul-escuro com letras brancas. O Tab mostra o contorno laranja à volta do campo e do botão.

Pensa antes de continuares: uma colega quer o texto do parágrafo em cinzento `#999999`, porque acha mais elegante. O que lhe dizes? A resposta: o cinzento `#999999` num fundo branco tem um contraste de 2,85 para 1, longe dos 4,5 para 1 que o texto normal pede. Muitas pessoas iam ler mal o parágrafo, sobretudo num ecrã com pouco brilho. Uma calculadora de contraste mostra-o antes de se escolher a cor.

## Fase 4: O script e a consola do browser

A página tem estrutura e apresentação, mas o botão continua sem fazer nada. Quem dá comportamento à página é o JavaScript, escrito num terceiro ficheiro que a página carrega. O JavaScript corre dentro do browser, e não no editor. Para ver o que ele faz, usa-se a consola, uma parte do browser onde aparecem as mensagens do script e os erros. Para saber mais, lê a secção "O JavaScript entra pela etiqueta `script`" do [guia](../01-primeira-pagina-com-javascript.md).

1. Cria o ficheiro do script. No `Explorer`, cria `inventario.js` e escreve nele este conteúdo, que é o ficheiro completo:

   ```js
   // inventario.js: o comportamento da página do inventário.

   console.log("O script está a correr.");
   console.log(6 - 2);
   ```

   Leitura guiada: a primeira linha é um comentário de JavaScript, que começa por `//` e vai até ao fim da linha, como o `#` do Python. O `console.log(...)` faz o que o `print` fazia em Python: mostra os valores que recebe. Cada instrução acaba com um ponto e vírgula.

2. Liga o script à página. No `index.html`, dentro do `head`, a seguir à linha do `link`, acrescenta esta linha:

   ```html
       <script src="inventario.js" defer></script>
   ```

   Leitura guiada: o `script` carrega um ficheiro de JavaScript, e o `src` é o caminho dele, como o `href` do `link`. O `script` precisa sempre da etiqueta de fecho, mesmo vazio. O atributo `defer` (em inglês, adiar) não tem valor: diz ao browser que só deve correr o script depois de ler o HTML todo. Na fase 6 o script vai procurar o campo e o botão, e sem o `defer` corria antes de eles existirem.

3. Guarda os dois ficheiros. Antes de recarregares, prevê: onde vão aparecer as duas mensagens do script? Depois recarrega.

   O que deves ver: a página fica igual. As mensagens não aparecem na página, porque o `console.log` escreve na consola, e não na página.

4. Abre a consola. Carrega em F12 no Windows, ou em Cmd+Option+I no macOS. Abre-se a parte do browser que usaste na fase 3, as ferramentas do programador. Escolhe o separador `Console` (num browser em português, pode aparecer `Consola`). Se não vires as mensagens, recarrega a página com a consola aberta.

   O que deves ver:

   ```text
   O script está a correr.
   4
   ```

   A primeira linha quer dizer que o browser encontrou o ficheiro e correu o script. O `4` é o resultado da conta `6 - 2`. Ao lado de cada linha, à direita, aparece `inventario.js:3` e `inventario.js:4`: o ficheiro e a linha que escreveu cada mensagem.

5. Escreve JavaScript diretamente na consola. Na linha de baixo da consola, onde está o cursor, escreve `6 - 2` e carrega em Enter. Depois escreve `console.log("olá")` e carrega em Enter. Escreve sempre à mão o que pões na consola: o Chrome e o Edge, por segurança, não deixam colar código na consola na primeira vez, e mostram um aviso.

   O que deves ver: com `6 - 2`, aparece `4`. Com `console.log("olá")`, aparece `olá` e, por baixo, `undefined`. A consola mostra sempre o valor da instrução que escreveste. O `console.log` mostra o texto, mas não devolve valor nenhum, e em JavaScript a ausência de valor chama-se `undefined`. É o que o `None` era em Python. Vais usar a consola assim na fase 5, para testar uma função.

6. Provoca um erro de propósito: no `script` do `index.html`, muda `src="inventario.js"` para `src="inventaro.js"`, sem o "i" depois do "r". Guarda e recarrega, com a consola aberta.

   O que deves ver: as duas mensagens do script desaparecem, e no lugar delas aparece, a vermelho:

   ```text
   Failed to load resource: net::ERR_FILE_NOT_FOUND
   ```

   Ao lado, a mensagem mostra o caminho do ficheiro que o browser procurou, a acabar em `inventaro.js`. A mensagem quer dizer "falhou o carregamento do recurso: ficheiro não encontrado". O browser procurou um ficheiro com o nome do `src`, não o encontrou, e não correu nenhum script. É o mesmo que aconteceu na fase 3 com o `estilo.css`: o aviso vem para a consola, e não para a página. Para corrigir, compara o nome no `src` com o nome do ficheiro, letra a letra. Volta a pôr `src="inventario.js"`, guarda e recarrega. As duas mensagens voltam a aparecer.

### Paragem 4

O `head` do `index.html` tem agora o `title`, o `link` da folha de estilos e o `script`, por esta ordem:

```html
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Inventário da sala</title>
    <link rel="stylesheet" href="estilos.css">
    <script src="inventario.js" defer></script>
  </head>
```

É um excerto: o resto do `index.html` fica como na paragem 3. A consola mostra `O script está a correr.` e `4`, e sabes escrever JavaScript diretamente nela.

Pensa antes de continuares: o JavaScript desta página está num ficheiro do VS Code. Porque é que não o corres no VS Code, como fazias com os ficheiros de Python? A resposta: este JavaScript foi escrito para a página, e a página só existe no browser. É o browser que o corre, quando abre o `index.html`. Fora do browser não há página, e o script não teria campo nem botão para usar.

## Fase 5: Do Python ao JavaScript, a função `retirar`

No guia 01 do M10 escreveste em Python uma função que aplica as regras de um pedido de retirada. Um pedido positivo e não maior do que o que existe é aceite; qualquer outro é recusado, sem mexer na quantidade. A regra já está pensada e testada. Nesta fase traduze-la para JavaScript e confirmas que dá os mesmos resultados. Como a lógica é a mesma, a única coisa nova é a linguagem. Para saber mais, lê as secções de "Variáveis com `const` e `let`" a "Ciclos: `for`, `while` e `for...of`" do [guia](../01-primeira-pagina-com-javascript.md).

Esta é a função de Python, do guia 01 do M10:

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

1. Traduz a função e acrescenta os testes. No `inventario.js`, substitui todo o conteúdo por este, que é o ficheiro completo:

   ```js
   // inventario.js: o comportamento da página do inventário.
   // Por agora, a função retirar e os testes que a confirmam na consola.

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

   // Os dois casos do guia 01 do M10: em Python, davam 4 e 4.
   console.log(retirar(6, 2));
   console.log(retirar(4, 5));

   // Uma sequência de pedidos, como os cliques que a página vai receber.
   let quantidade = 6;
   const pedidos = [2, 5, 1];

   for (const pedido of pedidos) {
     quantidade = retirar(quantidade, pedido);
     console.log("Depois do pedido de " + pedido + ": ficam " + quantidade);
   }
   ```

   Leitura guiada: compara a função com a de Python, linha a linha.

   - O `def` passa a `function`. Os dois pontos no fim da primeira linha passam a uma chaveta, `{`. Em JavaScript, são as chavetas, e não a indentação, que marcam onde começa e acaba um bloco. A indentação continua lá, com dois espaços, para as pessoas verem os blocos.
   - A docstring passa a JSDoc, um comentário entre `/**` e `*/` que fica antes da função, e não dentro dela. A primeira parte diz o que a função faz, como a docstring. Cada `@param` descreve um parâmetro, com o tipo entre chavetas: `number` é o tipo dos números em JavaScript, inteiros ou com parte decimal. O `@returns` diz o que a função devolve. O VS Code mostra este texto quando passas o rato por cima do nome `retirar`.
   - No `if`, a condição vai entre parênteses, e o `and` passa a `&&`. Não há dois pontos: o bloco do `if` fica entre chavetas.
   - Os dois `return` são iguais, com um ponto e vírgula no fim.

   Depois da função vêm os testes. Os dois primeiros `console.log` chamam a função com os casos do guia 01 do M10. A seguir, uma variável nova declara-se com uma palavra antes do nome. O `let` declara a `quantidade`, que vai mudar a cada pedido. O `const` declara os `pedidos`, um nome que aponta sempre para o mesmo array. O array é a lista do Python, com os valores entre parênteses retos. O `for (const pedido of pedidos)` é o `for pedido in pedidos:` do Python. Em cada volta nasce um `pedido` novo, com o valor seguinte do array, e ele não muda dentro dessa volta: é por isso que pode ser `const`. Dentro do ciclo, a primeira linha é a mesma que em Python: a função calcula o que fica, e a atribuição guarda-o. A segunda junta texto e números com o `+`: o JavaScript converte os números em texto e junta tudo numa frase.

2. Guarda e, antes de recarregares, prevê as cinco linhas que a consola vai mostrar. Segue os pedidos 2, 5 e 1 a partir de 6, aplicando as regras. Depois recarrega, com a consola aberta.

   O que deves ver:

   ```text
   4
   4
   Depois do pedido de 2: ficam 4
   Depois do pedido de 5: ficam 4
   Depois do pedido de 1: ficam 3
   ```

   As duas primeiras linhas são as mesmas que o programa de Python dava, e por isso a tradução está certa. Na sequência, o pedido de 2 é aceite e deixa 4. O de 5 é maior do que 4, é recusado, e a quantidade fica em 4. O de 1 é aceite e deixa 3.

3. Testa as fronteiras na consola. A consola conhece as funções do script da página. Escreve cada uma destas chamadas e carrega em Enter. Antes de cada uma, prevê o resultado.

   | Escreves na consola | O que se espera, pelas regras | O que deves ver |
   | --- | --- | ---: |
   | `retirar(4, 4)` | Pedido igual ao que existe: é possível, e fica 0 | `0` |
   | `retirar(6, 0)` | Pedido de zero: não é positivo, fica tudo igual | `6` |
   | `retirar(6, -1)` | Pedido negativo: fica tudo igual | `6` |

   O primeiro caso confirma que o `<=` deixa retirar tudo o que existe. Os outros dois confirmam que o `> 0` recusa o zero e os negativos.

4. Provoca um erro de propósito, com um hábito do Python. Na linha 13, muda o `if` para a forma do Python, exatamente assim:

   ```js partial
     if unidades > 0 and unidades <= quantidade:
   ```

   É só a linha que muda; o resto do ficheiro fica igual. Guarda e recarrega, com a consola aberta.

   O que deves ver: nenhuma das cinco linhas da consola aparece. No lugar delas, a vermelho:

   ```text
   Uncaught SyntaxError: Unexpected identifier 'unidades'
   ```

   À direita aparece `inventario.js:13`. A mensagem quer dizer "erro de sintaxe não apanhado: nome inesperado, `unidades`". É um erro de escrita. O browser leu `if` e esperava um parêntese a seguir, mas encontrou o nome `unidades`. Quando um script tem um erro de escrita, o browser não corre nenhuma linha dele, nem as que estão antes do erro. Por isso as cinco linhas desapareceram todas. Repõe a linha 13 como estava, com os parênteses, o `&&` e a chaveta, guarda e recarrega. As cinco linhas voltam.

### Paragem 5

O `inventario.js` tem a função `retirar` em JavaScript, e a consola mostra `4`, `4` e a sequência 4, 4 e 3. Na consola, `retirar(4, 4)` dá `0` e `retirar(6, 0)` dá `6`.

Pensa antes de continuares: a `quantidade` foi declarada com `let`, e os `pedidos` com `const`. O que acontecia se a `quantidade` fosse `const`? A resposta: na primeira volta do ciclo, a linha `quantidade = retirar(quantidade, pedido);` tentava dar outro valor a uma constante. O script parava com a mensagem `Uncaught TypeError: Assignment to constant variable.` (em português, atribuição a uma variável constante). O `const` serve para os nomes que nunca recebem outro valor, e a quantidade recebe um a cada pedido aceite.

## Fase 6: O botão chama a função

Falta ligar a página à função. Quando alguém carrega no botão, o script tem de ler o número escrito no campo, pedir a retirada e mostrar o resultado na saída. Para isso usa quatro peças novas. A primeira encontra um elemento da página, a segunda lê o texto de um campo, e a terceira escreve o texto de um elemento. A quarta manda o browser chamar uma função quando há um clique. Para saber mais, lê a secção "Ligar um botão a uma função" do [guia](../01-primeira-pagina-com-javascript.md).

1. Liga o botão à função. No `inventario.js`, substitui tudo o que está a seguir à chaveta que fecha a função `retirar`, os testes da fase 5, pelo código da página. Muda também a segunda linha do comentário do início. O ficheiro completo fica assim:

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

   1. A função `retirar` fica como estava. O browser lê-a, e as outras duas funções, sem as correr.
   2. A variável `quantidadeCaderno` guarda o estado do caderno entre um clique e o seguinte. Está fora das funções, para não se perder quando uma função acaba. O nome junta as palavras com uma maiúscula no meio, em vez do traço por baixo do Python: é a convenção do JavaScript, a que se chama *camelCase*.
   3. As três linhas `document.querySelector(...)` encontram os elementos da página. O `document` é a página, tal como o browser a guarda. O `querySelector` procura o primeiro elemento que corresponde ao seletor entre aspas e devolve-o. O `#` quer dizer "o elemento com este `id`": `#unidades` é o campo, `#botao-retirar` é o botão e `#resultado` é a saída. Cada elemento fica num `const`, porque é sempre o mesmo. Se nenhum elemento tiver esse `id`, o `querySelector` devolve `null`, que quer dizer "nenhum objeto".
   4. A linha do `addEventListener` liga o botão à função `aoCarregarEmRetirar`. O `addEventListener` (em inglês, acrescenta quem ouve o evento) diz ao browser: "quando houver um clique neste botão, chama esta função". O `"click"` é o nome do evento. A função vai sem parênteses: dás a função ao browser, para ele a chamar em cada clique.
   5. A última linha chama `mostrarQuantidade`, que escreve na saída `Unidades do caderno A01: 6.` O `textContent` é o texto dentro de um elemento, e dar-lhe um valor novo substitui o que lá estava.
   6. O script acaba, mas a página continua aberta. A cada clique no botão, o browser chama `aoCarregarEmRetirar`. A função lê o `value` do campo, o texto que lá está escrito, e converte-o num número com o `Number`. O `value` é sempre um texto, mesmo quando se escreve um algarismo. Depois pede a retirada, com a mesma linha da fase 5, e volta a mostrar a quantidade.

2. Guarda e, antes de recarregares, prevê o que aparece na saída quando a página abre. Depois recarrega.

   O que deves ver: por baixo do botão, `Unidades do caderno A01: 6.`, e nenhum erro na consola. Esta frase foi escrita pelo JavaScript: no HTML, a saída está vazia.

3. Faz os pedidos do inventário. Escreve cada valor no campo e carrega em "Retirar", pela ordem da tabela, sem recarregar a página. Antes de cada pedido, prevê o que a saída vai mostrar.

   | Pedido | Escreves no campo | O que deves ver na saída |
   | --- | --- | --- |
   | 1 | `2` | `Unidades do caderno A01: 4.` |
   | 2 | `5` | `Unidades do caderno A01: 4.` |
   | 3 | `4` | `Unidades do caderno A01: 0.` |
   | 4 | `1` | `Unidades do caderno A01: 0.` |

   Os pedidos 1 e 2 dão o mesmo que o programa de Python. O 3 retira tudo, e o 4 é recusado, porque já não há unidades.

4. Faz os mesmos pedidos só com o teclado. Recarrega a página, para o caderno voltar às 6 unidades. Carrega em Tab até o foco chegar ao campo e escreve `2`. Carrega em Tab outra vez, para o foco passar para o botão, e carrega em Enter.

   O que deves ver: a saída passa a `Unidades do caderno A01: 4.` O botão funciona com o teclado sem nenhuma linha a mais, porque é um `button` a sério.

5. Experimenta o que alguém pode escrever por engano. Recarrega a página e faz esta sequência, sem recarregar entre os pedidos. Antes de cada um, prevê se a quantidade muda.

   | Pedido | Escreves no campo | O que o `Number` dá | O que deves ver na saída |
   | --- | --- | --- | --- |
   | 1 | `abc` | `NaN` | `Unidades do caderno A01: 6.` |
   | 2 | nada | `0` | `Unidades do caderno A01: 6.` |
   | 3 | `2,5` | `NaN` | `Unidades do caderno A01: 6.` |
   | 4 | `2.5` | `2.5` | `Unidades do caderno A01: 3.5.` |

   O `NaN`, de *Not a Number* (em inglês, não é um número), é o que o `Number` dá quando o texto não é um número. As comparações da condição do `retirar`, com `>` e com `<=`, dão sempre `false` quando um dos lados é `NaN`, e por isso a condição recusa o pedido. O campo vazio dá 0, que também é recusado. O `2,5` dá `NaN` porque o JavaScript escreve a parte decimal com um ponto.

   O pedido 4 mostra o que a página ainda não protege. O `2.5` é positivo e não é maior do que 6, e a condição aceita-o. O caderno fica com 3.5 unidades, uma quantidade impossível. O programa de Python do guia 01 do M10 tinha a mesma falha, porque a função não verifica se o pedido é inteiro. A falha resolve-se no tema 03, com uma classe que protege a regra, como fizeste em Python.

6. Vê o que o `textContent` faz a um texto com etiquetas. Na consola, escreve esta instrução e carrega em Enter:

   ```js
   saida.textContent = "<b>Olá</b>";
   ```

   O que deves ver: a saída da página mostra `<b>Olá</b>`, com os sinais `<` e `>` à vista. A palavra não fica em negrito, apesar de `<b>` ser a etiqueta do HTML para o negrito. O `textContent` escreve sempre texto simples, e o browser nunca o lê como HTML. Assim, o que alguém escreve num campo nunca passa a fazer parte da página. Recarrega a página para voltares ao início.

7. Provoca um erro de propósito, num `id`. Na linha 23 do `inventario.js`, muda `"#botao-retirar"` para `"#botao-retira"`. Guarda e recarrega, com a consola aberta.

   O que deves ver: a saída fica vazia, e a consola mostra, a vermelho:

   ```text
   Uncaught TypeError: Cannot read properties of null (reading 'addEventListener')
   ```

   À direita aparece `inventario.js:46`. A mensagem quer dizer "erro de tipo não apanhado: não é possível ler propriedades de `null`, ao ler `addEventListener`". É um erro de execução: o script correu até à linha 46 e parou lá. Repara que a linha apontada não é a linha que mudaste. A causa está na linha 23: o `querySelector` não encontrou nenhum elemento com o `id` `botao-retira` e devolveu `null`. O erro só rebenta na linha 46, onde se tenta usar esse `null`. Como o script parou na linha 46, a última linha, que mostra a quantidade inicial, já não correu, e por isso a saída ficou vazia.

   Confirma a hipótese na consola: escreve `botaoRetirar` e carrega em Enter. Aparece `null`, o que confirma que o botão não foi encontrado. Repõe `"#botao-retirar"` na linha 23, guarda e recarrega.

8. Provoca outro erro de propósito, desta vez sem mensagem. Na linha 46, acrescenta parênteses ao nome da função, exatamente assim:

   ```js partial
   botaoRetirar.addEventListener("click", aoCarregarEmRetirar());
   ```

   Guarda, recarrega, escreve `2` no campo e carrega em "Retirar".

   O que deves ver: a saída mostra `Unidades do caderno A01: 6.`, mas o clique não muda nada, e a consola não mostra nenhum erro. Com os parênteses, a função foi chamada logo ali, uma vez, quando a página carregou. Nesse momento o campo estava vazio, e o pedido de 0 foi recusado. O que se deu ao browser foi o valor que a função devolveu, `undefined`, e o browser não tem nenhuma função para chamar nos cliques. É um erro de lógica: o script corre sem mensagens e não faz o que devia. Tira os parênteses, guarda, recarrega e confirma que o botão volta a funcionar.

### Paragem 6

A página está completa. Abre com `Unidades do caderno A01: 6.`, e cada pedido válido retira unidades, com o rato ou com o teclado. Os pedidos impossíveis deixam a quantidade igual. O `inventario.js` completo é o do passo 1 desta fase, e o `index.html` é o da paragem 3, com o `script` da paragem 4 no `head`.

Pensa antes de terminares: na linha `quantidadeCaderno = retirar(quantidadeCaderno, unidades);`, o que acontecia se tirasses o `quantidadeCaderno =` do princípio? A resposta: a função calculava o que fica e devolvia-o, mas o valor perdia-se, porque ninguém o guardava. A variável ficava sempre com 6, e a página mostrava sempre `Unidades do caderno A01: 6.`, sem nenhuma mensagem de erro. Era o mesmo erro de lógica que no guia 01 do M10: a função não muda a variável, quem a muda é a atribuição.

## Problemas frequentes

### O ficheiro abre num programa de texto, ou o browser mostra o código

Se o duplo clique foi no VS Code, o ficheiro abre para editar: abre a página pela janela de ficheiros do computador, como diz o passo 4 da fase 1. Se o nome do ficheiro acabar em `.txt`, como `index.html.txt`, o computador trata-o como texto. Muda o nome no VS Code, com o botão direito sobre o ficheiro e `Rename...`, para `index.html`.

### A página não muda depois de mudares o ficheiro

O ficheiro não foi guardado, ou a página não foi recarregada. Confirma que o separador do VS Code não tem a bola branca, guarda, e recarrega a página no browser.

### A página aparece sem estilos, e a consola mostra `Failed to load resource: net::ERR_FILE_NOT_FOUND`

O caminho do `href` não corresponde ao nome da folha de estilos. Compara-os letra a letra e confirma que o `estilos.css` está na mesma pasta que o `index.html`.

### A consola não mostra as mensagens do script, e mostra `Failed to load resource: net::ERR_FILE_NOT_FOUND`

O caminho do `src` não corresponde ao nome do ficheiro de JavaScript. Compara-os letra a letra e confirma que o `inventario.js` está na mesma pasta que o `index.html`.

### A consola está vazia, sem mensagens nem erros

Abriste a consola depois de a página carregar, e algumas versões dos browsers só mostram as mensagens que aparecem com ela aberta. Recarrega a página com a consola aberta. Se continuar vazia, confirma que o `script` está no `head` do `index.html`, como na paragem 4.

### `Uncaught SyntaxError: Unexpected identifier`

Um erro de escrita, e nada do script corre. Vai à linha que a mensagem indica, à direita, e procura um hábito do Python. Pode ser uma condição sem parênteses, um `and` em vez de `&&`, ou dois pontos no fim de uma linha. Se a linha parecer certa, olha também para a linha de cima.

### `Uncaught SyntaxError: Unexpected end of input`

Falta fechar uma chaveta ou um parêntese, e o browser chegou ao fim do ficheiro à espera dela. A mensagem aponta para a última linha, mas a falta está antes. Põe o cursor ao lado de cada `{`, e o VS Code marca a `}` que lhe corresponde.

### `Uncaught TypeError: Cannot read properties of null (reading 'addEventListener')`

O `querySelector` não encontrou o elemento e devolveu `null`. Na consola, escreve o nome do `const` do elemento, como `botaoRetirar`: se aparecer `null`, compara o seletor do script com o `id` do HTML, letra a letra. Confirma também que o `script` tem o `defer`.

### `Uncaught TypeError: Assignment to constant variable.`

O script tenta dar outro valor a uma variável declarada com `const`. Declara-a com `let`, se ela tiver mesmo de mudar.

### `Uncaught ReferenceError: quantidade is not defined`

O nome não existe: está mal escrito, com outra maiúscula, ou não foi declarado. Compara o nome da linha indicada com o da declaração. Para o JavaScript, `quantidadeCaderno` e `quantidadecaderno` são nomes diferentes.

### O botão não faz nada, e a consola não mostra erros

A função foi passada ao `addEventListener` com parênteses. Escreve só o nome da função, sem parênteses, como no passo 8 da fase 6.

### A saída mostra números colados, como `61`

Um dos valores da conta é um texto, e o `+` com um texto junta em vez de somar. Converte o texto em número com `Number` antes da conta. Numa mensagem, põe a soma entre parênteses, como em `"Total: " + (a + b)`, para o JavaScript somar primeiro e só depois juntar o resultado ao texto.

### O VS Code tenta correr o ficheiro de JavaScript e mostra `ReferenceError: document is not defined`

O JavaScript desta página não se corre no editor: fora do browser não há página, e o `document` não existe. Abre o `index.html` no browser, que carrega o script.

## Desafios

1. Avisar quando o pedido é recusado. Hoje, quem faz um pedido impossível vê a mesma frase de sempre e não fica a saber que o pedido foi recusado. Muda a página para que, num pedido recusado, a saída mostre `Pedido recusado. Unidades do caderno A01: 6.`, com a quantidade certa. Pista: guarda a quantidade antes do pedido numa variável e compara-a com a de depois.
2. Um botão para adicionar unidades. Acrescenta um segundo botão, "Adicionar", que usa o mesmo campo e soma unidades ao caderno. Escreve primeiro uma função `adicionar(quantidade, unidades)`, com JSDoc, que só aceita pedidos positivos e devolve a quantidade sem mudanças nos outros casos. Pista: testa a função na consola com 6 e 3, 6 e 0 e 6 e -2 antes de lhe ligares o botão.
3. A pasta A02. Acrescenta à página a pasta A02, que começa com 2 unidades, com o seu próprio campo, o seu botão e a sua saída. Responde, num comentário no fim do `inventario.js`: quantas variáveis, quantos `id` e quantas funções novas precisaste? Que problema do guia 01 do M10 voltou a aparecer? Pista: conta tudo o que tiveste de repetir para a pasta, e imagina o mesmo para cinquenta artigos.

## Antes de terminares

- [ ] A pasta `primeira-pagina` tem o `index.html`, o `estilos.css` e o `inventario.js`, e a página abre com um duplo clique.
- [ ] Clicar no rótulo põe o cursor no campo, e o Tab mostra o contorno laranja no campo e no botão.
- [ ] A consola abre-se, e não mostra erros com a página carregada.
- [ ] Na consola, `retirar(6, 2)` dá `4` e `retirar(4, 5)` dá `4`, como no programa de Python.
- [ ] Os pedidos 2, 5, 4 e 1, por esta ordem, deixam a saída com 4, 4, 0 e 0 unidades, com o rato e com o teclado.
- [ ] Sabes dizer que tipo de erro é cada um dos que provocaste: o `id` errado, os parênteses a mais e o `if` à maneira do Python.
- [ ] Consegues explicar, por palavras tuas, o que faz cada um dos três ficheiros e o caminho de um número desde o campo até à saída da página.

![Rodapé](../../imagens/rodape.png)

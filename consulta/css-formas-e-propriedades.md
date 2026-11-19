![Cabeçalho](../imagens/cabecalho.png)

# Consulta rápida de CSS

Aqui tens as três formas de pôr CSS numa página e como se escreve uma regra. A seguir vêm as propriedades que mais vais usar, com o que fazem e um exemplo de cada uma.

## Como se escreve uma regra

O CSS diz como aparecem os elementos da página. Escreve-se em **regras**. Cada regra começa por um **seletor**, que escolhe os elementos, e diz entre chavetas o que muda neles, uma propriedade por linha, na forma `propriedade: valor;`.

```css
/* Os parágrafos ficam azul-escuros e com letra maior. */
p {
  color: #1f4e8c;
  font-size: 18px;
}
```

- `p`: o seletor. Esta regra escolhe todos os parágrafos.
- `color` e `font-size`: as propriedades, o que muda.
- `#1f4e8c` e `18px`: os valores, como muda.
- `/* ... */`: um comentário, que o browser ignora.

Cada linha acaba em `;`. Se uma propriedade estiver mal escrita, o browser não mostra nenhum erro: ignora-a e continua.

## As três formas de pôr CSS numa página

### No atributo `style` (inline)

O CSS vai dentro da etiqueta de abertura, no atributo `style`. Só muda aquele elemento.

Exemplo:

```html
<p style="color: #b00020; font-weight: bold;">Esgotado</p>
```

Serve para experimentar depressa. Numa página a sério, evita-o: o mesmo estilo tem de se repetir em cada elemento, e mudar uma cor obriga a mudá-la em todos.

### Na etiqueta `<style>`

As regras vão dentro de uma etiqueta `<style>`, no `head`. Mudam a página toda, mas só essa página.

Exemplo:

```html
<head>
  <meta charset="utf-8">
  <title>Inventário da sala</title>
  <style>
    p {
      color: #1f4e8c;
    }
  </style>
</head>
```

### Num ficheiro à parte

As regras vão num ficheiro `.css`, a **folha de estilos**, e a página liga-o no `head` com a etiqueta `<link>`, que não tem etiqueta de fecho. O mesmo ficheiro serve todas as páginas que o ligam.

Exemplo, no `index.html`:

```html
<head>
  <meta charset="utf-8">
  <title>Inventário da sala</title>
  <link rel="stylesheet" href="estilos.css">
</head>
```

E no `estilos.css`, na mesma pasta:

```css
p {
  color: #1f4e8c;
}
```

O `rel="stylesheet"` diz que o ficheiro é uma folha de estilos, e o `href` diz onde ele está. É a forma mais usada, porque o HTML fica só com o conteúdo, e o estilo de todas as páginas muda num só sítio.

### As três lado a lado

| Forma | Onde se escreve | O que muda |
| --- | --- | --- |
| Inline | No atributo `style` da etiqueta | Só esse elemento |
| Etiqueta `<style>` | Dentro do `<style>`, no `head` | A página onde está |
| Ficheiro | Num ficheiro `.css`, ligado com `<link>` | Todas as páginas que o ligam |

Quando a mesma propriedade do mesmo elemento aparece em mais de um sítio, ganha o atributo `style`. Entre a etiqueta `<style>` e o ficheiro, com o mesmo seletor, ganha a regra que o browser lê por último, a que está mais abaixo no `head`.

## Os seletores

| Seletor | O que escolhe | Exemplo |
| --- | --- | --- |
| `p` | Todos os elementos dessa etiqueta | `p { color: navy; }` |
| `h1, h2` | Vários elementos, separados por vírgulas | `h1, h2 { color: navy; }` |
| `.aviso` | Os elementos com `class="aviso"` | `.aviso { color: red; }` |
| `#total` | O elemento com `id="total"` | `#total { font-weight: bold; }` |
| `nav a` | Os `a` que estão dentro de um `nav` | `nav a { color: white; }` |
| `a:hover` | Os `a` quando o rato está por cima | `a:hover { color: red; }` |

Uma `class` pode estar em vários elementos da página, e um `id` só pode estar num.

## As cores e as medidas

As cores escrevem-se de três maneiras:

| Forma | Exemplo | O que é |
| --- | --- | --- |
| Nome | `red`, `white`, `navy` | Uma cor com nome, em inglês |
| Hexadecimal | `#1f4e8c` | Um `#` e três pares de símbolos, para o vermelho, o verde e o azul, de `00` a `ff` |
| `rgb()` | `rgb(31, 78, 140)` | As mesmas três cores, de 0 a 255 |

As medidas levam sempre a unidade, colada ao número:

| Unidade | O que vale | Exemplo |
| --- | --- | --- |
| `px` | Píxeis do ecrã | `16px` |
| `rem` | O tamanho da letra normal do browser, quase sempre 16 píxeis | `2rem` |
| `%` | Uma parte do tamanho do elemento que o contém | `50%` |

## Texto

As propriedades do texto passam do elemento para os que estão dentro dele: uma `color` no `body` muda o texto da página toda. A isto chama-se **herança**.

### `color`

Muda a cor do texto.

Exemplo:

```css
body {
  color: #1f1f1f;
}
```

### `font-family`

Escolhe o tipo de letra. Leva uma lista separada por vírgulas, e o browser usa a primeira que tiver.

Exemplo:

```css
body {
  font-family: system-ui, sans-serif;
}
```

Valores:

- `system-ui`: a letra do sistema operativo.
- `sans-serif`: uma letra sem patilhas.
- `serif`: uma letra com patilhas, como a dos jornais.
- `monospace`: uma letra em que todas as letras têm a mesma largura, como no editor de código.

### `font-size`

Muda o tamanho da letra.

Exemplo:

```css
h1 {
  font-size: 2rem;
}
```

### `font-weight`

Põe a letra em negrito ou tira o negrito.

Exemplo:

```css
th {
  font-weight: normal;
}
```

Valores:

- `normal`: a letra normal.
- `bold`: negrito.

### `font-style`

Põe a letra em itálico ou tira o itálico.

Exemplo:

```css
em {
  font-style: normal;
}
```

Valores:

- `normal`: a letra normal.
- `italic`: itálico.

### `text-align`

Alinha o texto dentro do elemento.

Exemplo:

```css
h1 {
  text-align: center;
}
```

Valores:

- `left`: à esquerda.
- `center`: ao centro.
- `right`: à direita.
- `justify`: justificado, com as linhas todas do mesmo comprimento.

### `text-decoration`

Põe ou tira uma linha no texto.

Exemplo:

```css
a {
  text-decoration: none;
}
```

Valores:

- `none`: sem linha. Tira o sublinhado das ligações.
- `underline`: sublinhado.
- `line-through`: riscado.

### `line-height`

Muda a altura de cada linha. O valor `1.5` dá uma vez e meia o tamanho da letra.

Exemplo:

```css
body {
  line-height: 1.5;
}
```

## Fundo

### `background-color`

Muda a cor do fundo.

Exemplo:

```css
button {
  background-color: #1f4e8c;
}
```

### `background-image`

Põe uma imagem no fundo. O caminho vai dentro de `url()`. Com `background-size: cover`, a imagem estica até cobrir o elemento todo.

Exemplo:

```css
header {
  background-image: url("imagens/fundo.png");
  background-size: cover;
}
```

## A caixa de cada elemento

Cada elemento é uma caixa. De dentro para fora, tem o conteúdo, o espaço por dentro (`padding`), a borda (`border`) e o espaço por fora (`margin`).

```text
┌─────────────── margin ────────────────┐
│ ┌───────────── border ──────────────┐ │
│ │ ┌─────────── padding ───────────┐ │ │
│ │ │           conteúdo            │ │ │
│ │ └───────────────────────────────┘ │ │
│ └───────────────────────────────────┘ │
└───────────────────────────────────────┘
```

### `width` e `height`

Mudam a largura e a altura da caixa.

Exemplo:

```css
img {
  width: 300px;
  height: 200px;
}
```

### `padding`

Muda o espaço por dentro, entre o conteúdo e a borda. Com um valor, fica igual nos quatro lados. Com dois, o primeiro é para cima e para baixo, e o segundo para os lados. Para um lado só, há `padding-top`, `padding-right`, `padding-bottom` e `padding-left`.

Exemplo:

```css
button {
  padding: 0.5rem 1rem;
}
```

### `border`

Desenha uma borda à volta da caixa. Leva três valores: a grossura, o tipo de linha e a cor.

Exemplo:

```css
th, td {
  border: 1px solid #1f1f1f;
}
```

Valores do tipo de linha:

- `solid`: contínua.
- `dashed`: tracejada.
- `dotted`: pontilhada.

### `border-radius`

Arredonda os cantos da caixa.

Exemplo:

```css
button {
  border-radius: 8px;
}
```

### `margin`

Muda o espaço por fora, entre a caixa e as que estão à volta. Os valores funcionam como no `padding`, e há também `margin-top`, `margin-right`, `margin-bottom` e `margin-left`. Com `margin: 0 auto`, uma caixa com largura fica ao centro.

Exemplo:

```css
main {
  width: 600px;
  margin: 0 auto;
}
```

### `outline`

Desenha um contorno por fora da borda. O browser usa-o para mostrar onde está o foco de quem usa o teclado. Nunca o apagues com `outline: none` sem pores outro no lugar.

Exemplo:

```css
button:focus-visible {
  outline: 3px solid #b35c00;
}
```

## A disposição

### `display`

Diz como a caixa se arruma na página.

Exemplo:

```css
nav {
  display: flex;
}
```

Valores:

- `block`: ocupa a linha toda, e o elemento seguinte vai para baixo, como o `p` e o `h1`.
- `inline`: fica na mesma linha que o texto, como o `a` e o `strong`. Não aceita `width` nem `height`.
- `inline-block`: fica na mesma linha, mas aceita `width` e `height`.
- `none`: esconde o elemento.
- `flex`: põe lado a lado os elementos que estão dentro dele.
- `grid`: organiza os elementos de dentro numa grelha de linhas e colunas.

### `gap`

Com `display: flex` ou `display: grid`, muda o espaço entre os elementos de dentro.

Exemplo:

```css
nav {
  display: flex;
  gap: 1rem;
}
```

### `justify-content`

Com `display: flex`, arruma os elementos de dentro na horizontal.

Exemplo:

```css
nav {
  display: flex;
  justify-content: space-between;
}
```

Valores:

- `flex-start`: à esquerda.
- `center`: ao centro.
- `flex-end`: à direita.
- `space-between`: espalhados, com o espaço todo entre eles.

### `align-items`

Com `display: flex`, alinha os elementos de dentro na vertical.

Exemplo:

```css
header {
  display: flex;
  align-items: center;
}
```

Valores:

- `flex-start`: em cima.
- `center`: ao meio.
- `flex-end`: em baixo.

## A grelha com Grid

O Flexbox organiza elementos sobretudo numa direção, numa linha ou numa coluna. O Grid permite coordenar as linhas e as colunas ao mesmo tempo.

Aplica `display: grid` no elemento que contém o grupo. Os seus filhos diretos, os elementos imediatamente dentro dele, passam a ocupar as células da grelha.

### `grid-template-columns`

Define quantas colunas há e a largura de cada uma. A unidade `fr` representa uma parte do espaço disponível, depois de descontar os intervalos entre colunas.

Exemplo, no HTML:

```html
<div class="grelha">
  <div class="caixa">Caderno</div>
  <div class="caixa">Caneta</div>
  <div class="caixa">Borracha</div>
  <div class="caixa">Régua</div>
</div>
```

No CSS:

```css
.grelha {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.caixa {
  padding: 1rem;
  border: 1px solid #1f1f1f;
}
```

Ficam duas colunas com a mesma largura. O caderno e a caneta ficam na primeira linha; a borracha e a régua, na segunda.

O browser cria as linhas necessárias à medida que entram mais elementos. O `gap` deixa `1rem` entre as linhas e entre as colunas.

Outros valores para `grid-template-columns`:

| Valor | Resultado |
| --- | --- |
| `1fr 2fr` | Duas colunas; a segunda recebe o dobro do espaço da primeira |
| `200px 1fr` | A primeira tem 200 píxeis; a segunda recebe o espaço que sobra |
| `repeat(3, 1fr)` | Três colunas iguais; repete `1fr` três vezes |

### `grid-template-rows`

Define a altura das linhas indicadas. Sem esta propriedade, a altura das linhas do exemplo ajusta-se ao conteúdo.

Exemplo:

```css
.grelha {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 80px auto;
  gap: 1rem;
}
```

A primeira linha tem 80 píxeis de altura. A segunda ajusta-se ao conteúdo com `auto`. Se forem precisas mais linhas, o browser cria-as automaticamente.

### `gap`, `row-gap` e `column-gap`

Com um valor, o `gap` dá o mesmo intervalo às linhas e às colunas. Com dois, o primeiro é entre linhas e o segundo entre colunas.

Exemplo:

```css
.grelha {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem 2rem;
}
```

Aqui, há `1rem` entre linhas e `2rem` entre colunas. Para mudar só um deles, usa `row-gap` para as linhas ou `column-gap` para as colunas.

### `grid-column` e `grid-row`

Aplicam-se aos elementos de dentro da grelha. Permitem escolher a posição ou fazer um elemento ocupar várias células.

Exemplo, para uma caixa com `class="caixa destaque"`:

```css
.destaque {
  grid-column: span 2;
}
```

O `span 2` faz essa caixa ocupar duas colunas. Duas classes no mesmo elemento separam-se por um espaço.

Os números em `grid-column` referem-se aos limites verticais das colunas. Numa grelha de duas colunas, há três: à esquerda, ao meio e à direita.

O `1` indica o primeiro limite e o `-1` indica o último.

| Declaração | O que faz |
| --- | --- |
| `grid-column: span 2;` | Ocupa duas colunas |
| `grid-row: span 2;` | Ocupa duas linhas |
| `grid-column: 1 / -1;` | Ocupa todas as colunas, do primeiro ao último limite vertical |

### `justify-items` e `align-items`

No Grid, `justify-items` alinha cada elemento na horizontal dentro da sua célula. O `align-items` faz o mesmo na vertical.

Exemplo:

```css
.grelha {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 80px 80px;
  gap: 1rem;
  justify-items: center;
  align-items: center;
}
```

Cada caixa fica centrada na sua célula, nas duas direções.

Valores para as duas propriedades:

- `start`: no início, à esquerda ou em cima.
- `center`: ao centro.
- `end`: no fim, à direita ou em baixo.
- `stretch`: estica a caixa para preencher a célula, quando não tem uma dimensão fixa nessa direção.

## O posicionamento

Por omissão, cada elemento ocupa o seu lugar e influencia a posição dos seguintes. Esta organização chama-se **fluxo normal**.

### `position`

Escolhe como o elemento se posiciona e se mantém o seu espaço no fluxo normal.

| Valor | O que faz |
| --- | --- |
| `static` | Posição normal, por omissão. Não usa `top`, `right`, `bottom` nem `left` |
| `relative` | Desloca a caixa a partir da posição normal, mantendo o espaço original reservado |
| `absolute` | Retira a caixa do fluxo normal e posiciona-a em relação a uma caixa de referência |
| `fixed` | Numa página simples, fixa a caixa em relação à área visível do browser, sem reservar espaço |
| `sticky` | Mantém a caixa no fluxo e prende-a num limite durante o deslocamento, dentro do elemento que a contém |

Usa o Flexbox ou o Grid para organizar conjuntos de elementos. O posicionamento serve, por exemplo, para pôr uma etiqueta no canto de um cartão.

### `top`, `right`, `bottom` e `left`

Indicam os lados usados no posicionamento. O efeito depende do valor de `position`.

| Propriedade | Lado |
| --- | --- |
| `top` | Cima |
| `right` | Direita |
| `bottom` | Baixo |
| `left` | Esquerda |

Com `position: static`, estas propriedades não têm efeito. As medidas podem ser, por exemplo, `10px` ou `1rem`. O valor `0` não precisa de unidade.

### Deslocar com `relative`

O deslocamento parte do lugar onde a caixa estaria normalmente.

Exemplo, para um elemento com `class="aviso"`:

```css
.aviso {
  position: relative;
  top: 10px;
  left: 20px;
}
```

A caixa desce 10 píxeis e avança 20 píxeis para a direita. O espaço original fica reservado, por isso os elementos seguintes não ocupam esse lugar.

Com `right: 20px`, deslocava-se para a esquerda. Com `bottom: 10px`, subia. Estes deslocamentos podem fazer a caixa sobrepor-se a outra.

### Pôr uma etiqueta num canto com `absolute`

A caixa com `absolute` não reserva espaço no fluxo normal. Neste exemplo, a referência é o cartão, que tem `position: relative`.

No HTML:

```html
<div class="cartao">
  <p class="etiqueta">Novo</p>
  <p>Caderno azul de capa dura.</p>
</div>
```

No CSS:

```css
.cartao {
  position: relative;
  padding: 3rem 1rem 1rem;
  border: 1px solid #1f1f1f;
}

.etiqueta {
  position: absolute;
  top: 0.5rem;
  right: 0.5rem;
  margin: 0;
}
```

A etiqueta fica a `0.5rem` do topo e da direita, por dentro da borda do cartão. O `padding` do cartão deixa espaço para não tapar o texto.

Entre os elementos que contêm a etiqueta, o browser procura o mais próximo com `position` diferente de `static`. Não tem de ser o que a contém diretamente.

Numa página simples, se nenhum existir, a referência é a área inicial da página. O cartão com `position: relative`, sem deslocamentos, mantém a posição normal e serve de referência.

### Fixar ao ecrã com `fixed`

Numa página simples, a caixa fica no mesmo sítio da área visível do browser, mesmo quando deslocas a página.

Exemplo, para um botão com `class="ajuda"`:

```css
.ajuda {
  position: fixed;
  right: 1rem;
  bottom: 1rem;
}
```

O botão fica a `1rem` da direita e de baixo. Não reserva espaço e pode tapar conteúdo, sobretudo num ecrã pequeno.

### Prender durante o deslocamento com `sticky`

A caixa acompanha o conteúdo até chegar ao limite indicado. Aí fica presa, sem sair dos limites do elemento que a contém.

Exemplo, para um menu com `class="menu"`:

```css
.menu {
  position: sticky;
  top: 0;
  background-color: white;
}
```

O menu fica preso ao topo da zona que estás a deslocar. Mantém o seu espaço no fluxo normal.

Precisa de um limite, como `top: 0`, e de espaço no elemento que o contém para se deslocar.

### `z-index`

Ajuda a escolher qual das caixas sobrepostas aparece à frente. Nos casos simples, entre elementos posicionados ao mesmo nível, o maior valor fica à frente.

Exemplo, para dois elementos com `position: fixed`:

```css
.ajuda {
  position: fixed;
  right: 1rem;
  bottom: 1rem;
  z-index: 1;
}

.aviso {
  position: fixed;
  right: 1rem;
  bottom: 1rem;
  z-index: 2;
}
```

Se as duas caixas se sobrepuserem, o aviso aparece à frente do botão de ajuda.

## Listas e tabelas

### `list-style-type`

Muda a marca dos itens de uma lista.

Exemplo:

```css
ul {
  list-style-type: square;
}
```

Valores:

- `disc`: um ponto.
- `square`: um quadrado.
- `decimal`: números.
- `none`: sem marca.

### `border-collapse`

Junta as bordas das células de uma tabela numa só linha, em vez de duas.

Exemplo:

```css
table {
  border-collapse: collapse;
}
```

![Rodapé](../imagens/rodape.png)

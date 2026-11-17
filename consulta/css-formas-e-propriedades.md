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

### `gap`

Com `display: flex`, muda o espaço entre os elementos de dentro.

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

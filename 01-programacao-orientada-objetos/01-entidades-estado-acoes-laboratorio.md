![Cabeçalho](../imagens/cabecalho.png)

# Laboratório: um inventário em variáveis soltas

*M10 · Caderno 1 · Laboratório*

Este laboratório acompanha o [caderno 1](01-entidades-estado-acoes.md), e sobretudo a secção 6, "Duas maneiras de organizar um programa". Diz-te o que fazer, passo a passo, com o editor de Python aberto ao lado. As explicações do porquê estão no caderno: cada parte diz em que secção deves ter o caderno aberto. É um laboratório curto: conta com 40 a 45 minutos.

No fim deves ter um ficheiro `inventario.py` com três artigos guardados em variáveis e uma função `adicionar` escrita por ti. Pelo caminho vais prever, antes de executar, o que o programa mostra quando mudas os pedidos, e vais ver dois enganos que o Python deixa passar sem mostrar nenhuma mensagem de erro: uma atribuição esquecida e uma variável trocada.

## Antes de começar

Precisas do computador com o editor de Python que usas nas aulas, e de papel e caneta para as previsões, para os traços e para as respostas.

Antes do laboratório deves ter lido, no caderno 1, o exemplo guiado da secção 5 ("Exemplo guiado: seguir os valores passo a passo") e a secção 6 até ao fim de "O problema das variáveis soltas". O laboratório não repete essas explicações: aplica-as. Também não há aqui classes nem objetos, que são o assunto do caderno 2. Tudo o que vais escrever usa apenas o que a secção 6 usa: variáveis, uma função, uma condição e `print`.

A forma de trabalhar é sempre a mesma. Antes de executares, escreves no papel o que esperas ver. Depois executas e comparas. Quando o resultado é diferente do que previste, explica a diferença antes de continuares: é essa explicação que mais te ensina. Escrever a previsão antes de executar obriga-te a pensar no que o programa faz.

Há duas regras para todo o laboratório. A primeira: guarda o ficheiro e executa-o sempre inteiro. Cada execução começa do zero, com os valores iniciais das variáveis, e repete todos os pedidos pela ordem em que estão escritos. A segunda: em algumas partes vais mudar o programa de propósito, para veres o que acontece. Faz a alteração pedida, observa e desfaz a alteração antes de passares à parte seguinte. Se te perderes, copia outra vez do caderno o programa completo de onde a parte começa.

## Parte 1: preparar a pasta e o ficheiro (3 min)

1. Na pasta onde guardas os trabalhos de LP, cria uma pasta nova chamada `caderno-1`.
2. Dentro dessa pasta, cria um ficheiro novo chamado `inventario.py`. O nome tem de acabar em `.py` e não deve ter espaços nem acentos. Vais usar sempre este ficheiro.

## Parte 2: o primeiro programa e o traço (5 min)

Tem abertos o exemplo guiado da secção 5 e o primeiro programa da secção 6, em "A maneira habitual nos primeiros programas: programação estruturada".

1. Copia para o ficheiro o primeiro programa completo da secção 6, desde a linha `def retirar(quantidade, unidades):` até à última linha, `print(nome_caderno, quantidade_caderno)`. Guarda o ficheiro.
2. Antes de executares, escreve no papel as linhas que esperas ver. Ajuda-te com o traço do exemplo guiado, que faz os mesmos pedidos ao mesmo artigo.
3. Executa. Deves ver:

```text
Caderno 4
Caderno 4
```

4. Responde no papel. O traço do exemplo guiado tem quatro linhas (o início e três passos), e o programa mostrou só duas. A que passos do traço correspondem as duas linhas que apareceram? Em que linha do programa está o ponto de partida do traço, as 6 unidades?

## Parte 3: mudar os pedidos e prever (7 min)

Tem aberta a secção 5, com as regras e o parágrafo sobre as duas regras do zero.

1. Na primeira chamada, troca o 2 por 6, de modo que a linha fique assim:

```python partial
quantidade_caderno = retirar(quantidade_caderno, 6)
```

Esta linha não corre sozinha: substitui a linha correspondente do programa que já tens no ficheiro, e depende da função e das variáveis definidas antes dela. Deixa a segunda chamada como está, com o pedido de 5.

2. Antes de executares, faz no papel um traço com as colunas do exemplo guiado (passo, pedido, o que acontece, quantidade depois), a começar em 6, para os dois pedidos. Escreve as duas linhas que esperas ver. Depois executa e compara. Deves ver `Caderno 0` duas vezes.
3. Agora troca o 6 por 0, na mesma linha. Faz o traço no papel, escreve as duas linhas que esperas ver e executa. Deves ver:

```text
Caderno 6
Caderno 1
```

4. Responde no papel a duas perguntas.
   - O pedido de 5 foi recusado na experiência com o pedido de 6 e aceite na experiência com o pedido de 0. É o mesmo pedido: porque é que teve respostas diferentes? Usa a frase do exemplo guiado sobre o ponto de partida de cada linha do traço.
   - Olha só para a primeira linha da última execução, `Caderno 6`. Por essa linha, consegues saber se o pedido de 0 foi recusado? Relê o parágrafo da secção 6 que começa por "Este programa tem duas limitações".
5. Volta a pôr o 2 na primeira chamada. Executa e confirma que aparece outra vez `Caderno 4` duas vezes.

## Parte 4: a atribuição esquecida (6 min)

Tem aberto, na secção 6, o parágrafo que explica a linha `quantidade_caderno = retirar(quantidade_caderno, 2)`.

1. Na primeira chamada, apaga só a parte da esquerda, `quantidade_caderno =`, e deixa o resto. A linha fica assim:

```python partial
retirar(quantidade_caderno, 2)
```

Como na parte anterior, esta linha substitui a do ficheiro e depende do resto do programa. Não mexas na segunda chamada.

2. Antes de executares, relê a última frase desse parágrafo, a que começa por "Se escrevêssemos só", e escreve no papel as duas linhas que esperas ver.
3. Executa. Deves ver `Caderno 6` e `Caderno 1`, e nenhuma mensagem de erro.
4. Responde no papel a duas perguntas.
   - A função foi chamada e fez a conta? Que valor devolveu, e o que aconteceu a esse valor?
   - A saída é igual à da experiência com o pedido de 0, no passo 3 da parte 3, mas o que aconteceu dentro do programa não foi igual. Explica a diferença, dizendo em cada caso o que a função devolveu e o que foi feito com o valor devolvido.
5. O Python não mostrou nenhum erro, porque chamar uma função sem guardar o que ela devolve é uma instrução válida. Guarda as respostas desta parte: vão ajudar-te no exercício 4 da secção 7 do caderno.
6. Volta a escrever `quantidade_caderno =` no início da linha. Executa e confirma que aparece `Caderno 4` duas vezes.

## Parte 5: a variável trocada (6 min)

Tem aberto "O problema das variáveis soltas", na secção 6.

1. Substitui todo o conteúdo do ficheiro pelo segundo programa completo da secção 6, o que tem o caderno e a pasta. Executa e confirma que aparece o que o caderno mostra: `Caderno 6` e `Pasta 5`.
2. Encontra a linha com o engano: é a que está logo a seguir ao comentário que começa por `# Queríamos retirar 1 pasta`. Responde no papel: que variável está errada nessa linha, e que variável devia lá estar?
3. Corrige a linha, trocando só essa variável. O comentário que está por cima deixou de ser verdade, porque já não há engano para descrever: apaga-o. Antes de executares, escreve as duas linhas que esperas ver. Executa. Deves ver `Caderno 6` e `Pasta 1`.
4. Responde no papel: na versão com o engano, o Python mostrou alguma mensagem de erro? Se o comentário não existisse, como é que terias dado pelo engano? Pensa no que fizeste antes de cada execução, em todas as partes deste laboratório.

## Parte 6: um terceiro artigo e a operação adicionar, sozinho (15 min)

Nesta parte não há código para copiar. Continua no ficheiro corrigido da parte 5.

### 6.1: um terceiro artigo

1. Acrescenta um terceiro artigo, com o código `A04`, o nome `Borracha` e 5 unidades, guardado em três variáveis cujos nomes sigam o padrão das do caderno e da pasta. Escreve as três linhas a seguir às variáveis da pasta, separadas delas por uma linha em branco.
2. No fim do ficheiro, acrescenta dois pedidos para retirar 3 borrachas, um a seguir ao outro, cada um seguido de uma linha que mostre o nome e a quantidade da borracha. Escreve cada pedido como uma atribuição, à maneira das linhas da secção 6.
3. Antes de executares, faz o traço da borracha no papel e escreve as duas linhas novas que esperas ver. Executa e compara.

### 6.2: a operação adicionar

A secção 4 do caderno diz que faz sentido pedir três coisas a um artigo: consultar, adicionar e retirar. O programa só tem a função `retirar`. Vais escrever a função `adicionar`.

1. Antes de escreveres, decide no papel. O `if` da função `retirar` faz duas perguntas: `unidades > 0` e `unidades <= quantidade`. Qual delas faz sentido num pedido para adicionar, e qual não faz? Justifica com a regra dos pedidos da secção 5.
2. Escreve a função `adicionar(quantidade, unidades)` a seguir à função `retirar`, com duas linhas em branco antes e depois. Deve devolver a quantidade mais as unidades, se o pedido for aceite, e a quantidade que recebeu, sem mudanças, se o pedido for recusado. Escreve uma docstring, como a de `retirar`, que diga isto por palavras.
3. No fim do ficheiro, acrescenta dois pedidos à borracha, cada um seguido de uma linha que mostre o nome e a quantidade: adicionar 4 e, a seguir, adicionar 0.
4. Antes de executares, completa no papel o traço da borracha desde o início, com os quatro pedidos, e escreve as linhas que esperas ver. Executa e compara. No fim, o programa deve mostrar seis linhas: duas do caderno e da pasta, e quatro da borracha.

## Problemas frequentes neste laboratório

| O que aparece | O que costuma ser | Como resolver |
| --- | --- | --- |
| `NameError: name 'retirar' is not defined` | A função não foi copiada, ou ficou escrita depois das linhas que a usam | Confirma que a função está no início do ficheiro, antes de todas as chamadas. O mesmo vale para `adicionar` |
| `NameError: name 'quantidade_borrach' is not defined`, ou o mesmo com outro nome | Um nome de variável escrito de duas maneiras diferentes, por exemplo com uma letra a menos | Copia o nome da linha onde a variável recebeu o primeiro valor. As versões recentes do Python acrescentam uma sugestão, como `Did you mean: 'quantidade_borracha'?` |
| `TypeError: retirar() missing 1 required positional argument: 'unidades'` | A chamada tem só um valor dentro dos parênteses, e a função precisa de dois | Escreve os dois valores, separados por uma vírgula: primeiro a quantidade, depois as unidades |
| `SyntaxError`, muitas vezes com `expected ':'` | Falta o sinal de dois pontos no fim da linha do `def` ou do `if` | Acrescenta `:` no fim dessa linha. Em versões mais antigas do Python, a mensagem diz só `invalid syntax` |
| `IndentationError` | As linhas de dentro da função não estão mais afastadas da margem do que a linha do `def` | Compara a indentação com a da função `retirar`, linha a linha |
| Aparece `None` no lugar de uma quantidade, por exemplo `Borracha None` | A função `adicionar` não tem a última linha, a que devolve a quantidade quando o pedido é recusado | Acrescenta essa linha, como na função `retirar` |
| A quantidade não muda depois de um pedido, e não aparece nenhum erro | Falta a atribuição à esquerda da chamada (parte 4), ou o nome à esquerda do `=` tem um engano e o Python criou uma variável nova | Confirma que a linha começa exatamente pelo nome da variável que queres mudar, seguido de `=` |
| O programa mostra o mesmo que antes, apesar de teres mudado o código | O ficheiro não foi guardado antes de executar, ou estás a executar outro ficheiro | Guarda e confirma que estás a executar o `inventario.py` da pasta `caderno-1` |

## O que fica guardado

Guarda o ficheiro `inventario.py` com a parte 6 feita, e a folha com as previsões, os traços e as respostas das partes 2 a 6. Entrega-os pelo meio indicado pelo professor.

![Rodapé](../imagens/rodape.png)

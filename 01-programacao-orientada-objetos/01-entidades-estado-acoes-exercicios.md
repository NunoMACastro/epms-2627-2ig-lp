![Cabeçalho](../imagens/cabecalho.png)

# Ficha de exercícios: entidades, estado e comportamento

*M10 · Caderno 1 · Ficha de exercícios*

Esta ficha acompanha o [caderno 1](01-entidades-estado-acoes.md). É para praticares sozinho, depois de estudares o caderno e de fazeres o [laboratório](01-entidades-estado-acoes-laboratorio.md). Conta com cerca de 50 minutos para os cinco exercícios, e mais um quarto de hora se fizeres o desafio opcional do fim.

Os exercícios da secção 7 do caderno, "Agora experimenta", continuam a ser teus e o professor diz quando os fazer. Esta ficha não os repete: traz exercícios mais curtos, cada um a treinar uma coisa só, do mais direto para o que pede uma pequena decisão tua.

Quase tudo se faz em papel. O exercício 5 tem um programa completo, que podes executar no fim para confirmares as tuas previsões. Responde no caderno diário ou numa folha, com o número de cada exercício. Quando um exercício pede uma justificação, a justificação é a parte mais importante da resposta: uma escolha certa sem razão escrita vale pouco. Entrega as respostas pelo meio indicado pelo professor.

## Exercício 1: o que é entidade num torneio (8 min)

A associação de estudantes vai organizar um torneio de futsal entre as turmas da escola e quer um programa que responda a duas perguntas: que jogos estão marcados, com a data e as duas equipas de cada jogo; e quantos pontos tem cada equipa na classificação.

1. Para cada uma destas cinco coisas, diz se é uma entidade neste programa e justifica numa frase, a partir das duas perguntas: as equipas; os jogos; a bola; as bancadas do pavilhão; os jogadores de cada equipa.
2. Entre as coisas que marcaste como entidades, há alguma em que não se consiga tocar? Qual, e porque é que isso não a impede de ser uma entidade? (secção 2 do caderno)
3. A associação acrescenta uma terceira pergunta ao programa: quem é o melhor marcador do torneio, isto é, o jogador que marcou mais golos. Que resposta da alínea 1 muda? Explica porquê.

## Exercício 2: a ficha de um livro (12 min)

A turma montou uma pequena biblioteca na sala, com livros que os alunos trouxeram de casa. Há um só exemplar de cada livro. O programa da biblioteca tem de responder a uma pergunta: um certo livro está na estante ou está emprestado?

1. A ficha A01 da secção 1 guarda uma quantidade. Sabendo que há um só exemplar de cada livro, decide se a ficha de um livro precisa de uma quantidade, ou se outra informação responde melhor à pergunta do programa. Justifica em duas ou três frases.
2. Faz a ficha de um livro inventado por ti, com a informação que decidiste, numa tabela com as colunas "Informação" e "O que guardámos", como a ficha A01. Por baixo, escreve uma frase para cada linha, a dizer para que serve. Guarda só a informação de que o programa precisa: se uma linha não ajuda ninguém a responder à pergunta, não a ponhas.
3. Escreve as operações que fazem sentido para um livro desta biblioteca. Para cada uma, diz se só lê a ficha ou se a altera (secção 4 do caderno).

## Exercício 3: o pedido que falta (10 min)

A ficha A06, "Régua", começa com 5 unidades e recebe cinco pedidos, uns a seguir aos outros. É uma sequência, como no exemplo guiado da secção 5: cada linha começa na quantidade deixada pela linha anterior.

| Passo | Pedido | O que acontece | Quantidade depois |
| --- | --- | --- | ---: |
| Início | Nenhum | A ficha indica 5 unidades | 5 |
| 1 | Retirar 2 | A completar | A completar |
| 2 | Retirar 4 | A completar | A completar |
| 3 | Adicionar 3 | A completar | A completar |
| 4 | A completar | A completar | 0 |
| 5 | Retirar 1 | A completar | A completar |

1. Copia o traço e completa-o. No passo 4 falta o pedido: sabes apenas que, depois dele, a quantidade ficou em 0.
2. Explica porque é que, no passo 4, só há um pedido possível. Para isso, diz o que aconteceria com cada uma destas alternativas: adicionar unidades; retirar mais unidades do que as que existem; retirar 0.

## Exercício 4: os erros no traço de um colega (12 min)

Um colega fez o traço da ficha A10, "Cartolina", que começa com 4 unidades e recebe cinco pedidos em sequência. Enganou-se a aplicar as regras da secção 5 em duas linhas.

| Passo | Pedido | O que acontece | Quantidade depois |
| --- | --- | --- | ---: |
| Início | Nenhum | A ficha indica 4 unidades | 4 |
| 1 | Retirar 1 | 1 é um inteiro positivo e não passa de 4; fazemos 4 - 1 | 3 |
| 2 | Retirar 0 | 0 não passa de 3; fazemos 3 - 0 | 3 |
| 3 | Retirar 5 | 5 é mais do que 3; o pedido é recusado e a ficha fica vazia | 0 |
| 4 | Adicionar 2 | 2 é um inteiro positivo; fazemos 0 + 2 | 2 |
| 5 | Retirar 2 | 2 é um inteiro positivo e não passa de 2; fazemos 2 - 2 | 0 |

1. Encontra as duas linhas em que o colega aplicou mal as regras. Para cada uma, diz o que devia ter acontecido e porquê, com base na secção 5.
2. Numa das duas linhas erradas, a quantidade que o colega escreveu está certa. Qual é essa linha? Explica porque é que, mesmo assim, a linha está errada.
3. Faz o traço corrigido. Atenção: quando corriges uma linha, as linhas seguintes passam a começar noutra quantidade e podem mudar também, mesmo que o raciocínio delas estivesse certo.

## Exercício 5: de quem é cada variável (10 min)

Este programa completo usa a função `retirar` da secção 6 do caderno, mas as variáveis dos dois artigos têm nomes curtos e estão escritas por outra ordem: primeiro os dois códigos, depois os dois nomes e por fim as duas quantidades.

```python
def retirar(quantidade, unidades):
    """Devolve a quantidade que fica depois de um pedido de retirada.

    Se o pedido for possível, devolve a quantidade menos as unidades pedidas.
    Se não for possível, devolve a quantidade que recebeu, sem mudanças.
    """
    if unidades > 0 and unidades <= quantidade:
        return quantidade - unidades
    return quantidade


c1 = "A11"
c2 = "A12"
n1 = "Tesoura"
n2 = "Fita-cola"
q1 = 3
q2 = 8

q1 = retirar(q1, 4)
q2 = retirar(q2, 6)
print(n1, q1)
print(n2, q2)
```

1. Faz uma tabela com as seis variáveis, `c1`, `c2`, `n1`, `n2`, `q1` e `q2`. Para cada uma, escreve o artigo a que pertence (código e nome) e se guarda o código, o nome ou a quantidade.
2. Sem executar, prevê as duas linhas que o programa mostra. Para cada uma das duas chamadas a `retirar`, diz se o pedido é aceite ou recusado.
3. Escreve as duas linhas que terias de acrescentar no fim do programa para retirar 2 unidades de fita-cola e mostrar, a seguir, o nome e a quantidade da fita-cola. Prevê a linha nova que o programa passa a mostrar. Se tiveres o computador contigo, copia o programa com as tuas duas linhas, executa-o e confirma as previsões das alíneas 2 e 3.

## Desafio opcional: dois casos que enganam

Estes dois casos parecem simples e enganam muita gente. Faz primeiro o raciocínio no papel.

1. Uma ficha tem 0 unidades e chega o pedido "retirar 0". Um colega diz que o pedido é aceite, porque não se está a retirar mais do que existe. Outro colega diz que é recusado. Quem tem razão? Depois, sem executar, diz que valor devolve `retirar(0, 0)`, com a função da secção 6, e explica porque é que, só por esse valor, não se consegue saber quem tem razão.
2. Um colega quis retirar 3 cadernos no primeiro programa da secção 6, com o caderno a 6 unidades, mas escreveu os dois valores da chamada pela ordem trocada. Substituiu as quatro linhas que vêm depois das variáveis do caderno (as duas chamadas e os dois `print`) por estas duas:

```python partial
quantidade_caderno = retirar(3, quantidade_caderno)
print(nome_caderno, quantidade_caderno)
```

Estas duas linhas não correm sozinhas: dependem da função `retirar` e das três variáveis do caderno, que ficam como estão no programa da secção 6. O colega executou, viu `Caderno 3` e concluiu que a linha está certa, porque 6 - 3 = 3.

   - Segue a função com os valores que ela recebeu de facto, pela ordem em que os recebeu, e explica porque é que apareceu 3.
   - Propõe outro número de unidades para o pedido, com o qual o engano se veja no resultado. Diz o que o programa mostraria e o que devia mostrar.

## Antes de entregares

Revê as tuas respostas e confirma que em cada decisão escreveste a razão, e não só o resultado. Indica também um ponto desta ficha que ainda não consegues explicar sem voltar ao caderno: é por aí que deves começar a próxima revisão.

![Rodapé](../imagens/rodape.png)

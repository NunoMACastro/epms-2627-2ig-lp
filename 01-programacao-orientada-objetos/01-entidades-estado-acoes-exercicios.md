![Cabeçalho](../imagens/cabecalho.png)

# Ficha de exercícios: Entidades, estado e ações

Ficha do tema Entidades, estado e ações, do módulo M10, Introdução à Programação Orientada por Objetos. Praticas, um de cada vez, as entidades de um problema, a informação de uma ficha, as regras do inventário num traço e a leitura de variáveis soltas. Fazes sozinho, ao teu ritmo: o que não acabares na aula, acabas em casa ou na aula seguinte.

## O que precisas de saber

O [guia do tema](01-entidades-estado-acoes.md) e o [laboratório](01-entidades-estado-acoes-laboratorio.md). Cada exercício usa uma parte do guia:

- Exercício 1: a secção "Entidade: aquilo que escolhemos representar".
- Exercício 2: as secções "A informação que interessa guardar" e "Comportamento: o que podemos pedir que aconteça".
- Exercício 3: a secção "Uma operação tem de respeitar regras" e o exemplo guiado.
- Exercício 4: a mesma secção e o exemplo guiado.
- Exercício 5: a secção "Duas maneiras de organizar um programa", com o problema das variáveis soltas, e o laboratório.
- O desafio e os exercícios de "Para ires mais longe" usam as mesmas secções.

Se encravares, volta a essa parte do guia antes de olhares para o apoio, no fim da ficha.

## Como trabalhar

Os exercícios 1 a 5 são a parte obrigatória. Resolve-os pela ordem: cada um treina uma coisa só, do mais direto para o que pede mais decisões tuas.

| Exercício | O que treina |
| --- | --- |
| 1 | Decidir o que é entidade num problema novo |
| 2 | Escolher a informação de uma ficha de outro tipo |
| 3 | Deduzir um pedido a partir do estado, num traço |
| 4 | Encontrar e corrigir os erros do traço de um colega |
| 5 | Ler variáveis soltas com nomes curtos e prever o que um programa mostra |

O desafio opcional e os exercícios de "Para ires mais longe" são para quem acabar a parte obrigatória, ou para quando o professor os indicar.

Quase tudo se faz em papel. O exercício 5 tem um programa completo, que podes executar no fim para confirmares as tuas previsões. Responde no caderno diário ou numa folha, com o número de cada exercício. Cada exercício pede uma decisão que o exemplo guiado do guia não tomou por ti. Escreve o raciocínio, e não só a resposta final: é o raciocínio que o professor vai querer ouvir-te explicar. Quando um exercício pede uma justificação, a justificação é a parte mais importante da resposta: uma escolha certa sem razão escrita vale pouco. Entrega as respostas pelo meio indicado pelo professor.

## Exercício 1: As entidades de um torneio

A associação de estudantes vai organizar um torneio de futsal entre as turmas da escola. Quer um programa que responda a duas perguntas. Primeira: que jogos estão marcados, com a data e as duas equipas de cada jogo? Segunda: quantos pontos tem cada equipa na classificação?

1. Para cada uma destas cinco coisas, diz se é uma entidade neste programa: as equipas; os jogos; a bola; as bancadas do pavilhão; os jogadores de cada equipa. Justifica cada uma numa frase, a partir das duas perguntas.
2. Entre as coisas que marcaste como entidades, há alguma em que não se consiga tocar? Qual, e porque é que isso não a impede de ser uma entidade?
3. A associação acrescenta uma terceira pergunta ao programa: quem é o melhor marcador do torneio, isto é, o jogador que marcou mais golos? Que resposta da alínea 1 muda? Explica porquê.

## Exercício 2: A ficha de um livro

A turma montou uma pequena biblioteca na sala, com livros que os alunos trouxeram de casa. Há um só exemplar de cada livro. O programa da biblioteca tem de responder a uma pergunta: um certo livro está na estante ou está emprestado?

1. A ficha A01 do guia guarda uma quantidade. Há um só exemplar de cada livro. A ficha de um livro precisa de uma quantidade, ou outra informação responde melhor à pergunta do programa? Decide e justifica em duas ou três frases.
2. Faz a ficha de um livro inventado por ti, com a informação que decidiste, numa tabela com as colunas "Informação" e "O que guardámos", como a ficha A01. Por baixo, escreve uma frase para cada linha, a dizer para que serve. Guarda só a informação de que o programa precisa: se uma linha não ajuda ninguém a responder à pergunta, não a ponhas.
3. Escreve as operações que fazem sentido para um livro desta biblioteca. Para cada uma, diz se só lê a ficha ou se a altera.

## Exercício 3: O pedido que falta

A ficha A06, "Régua", começa com 5 unidades e recebe cinco pedidos, uns a seguir aos outros. É uma sequência, como no exemplo guiado do guia: cada linha começa na quantidade deixada pela linha anterior.

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

## Exercício 4: Os erros no traço de um colega

Um colega fez o traço da ficha A10, "Cartolina", que começa com 4 unidades e recebe cinco pedidos em sequência. Enganou-se a aplicar as regras do inventário em duas linhas.

| Passo | Pedido | O que acontece | Quantidade depois |
| --- | --- | --- | ---: |
| Início | Nenhum | A ficha indica 4 unidades | 4 |
| 1 | Retirar 1 | 1 é um inteiro positivo e não passa de 4; fazemos 4 - 1 | 3 |
| 2 | Retirar 0 | 0 não passa de 3; fazemos 3 - 0 | 3 |
| 3 | Retirar 5 | 5 é um inteiro positivo, mas só existem 3; o pedido é recusado | 3 |
| 4 | Adicionar 5 | 5 é mais do que 3; o pedido é recusado | 3 |
| 5 | Retirar 6 | 6 é um inteiro positivo, mas só existem 3; o pedido é recusado | 3 |

1. Encontra as duas linhas em que o colega aplicou mal as regras. Para cada uma, diz o que devia ter acontecido e porquê, com base nas regras do guia.
2. Numa das duas linhas erradas, a quantidade que o colega escreveu está certa. Qual é essa linha? Explica porque é que, mesmo assim, a linha está errada.
3. Faz o traço corrigido. Atenção: quando corriges uma linha, as linhas seguintes passam a começar noutra quantidade. Podem mudar também, mesmo que o raciocínio delas estivesse certo.

## Exercício 5: De quem é cada variável

Este programa completo usa a mesma função `retirar` do guia e do laboratório. Mas as variáveis dos dois artigos têm nomes curtos e estão escritas por outra ordem: primeiro os dois códigos, depois os dois nomes e por fim as duas quantidades.

```python
# Dois artigos guardados em variáveis soltas, com nomes curtos.


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

## Apoio

- Exercício 1: para cada coisa, pergunta que informação sobre ela o programa precisa de guardar para responder às duas perguntas.
- Exercício 2: escreve a resposta que o programa daria à pergunta da biblioteca para um livro. Depois pensa que informação da ficha dá essa resposta.
- Exercício 3: completa primeiro os passos 1 a 3 e escreve a quantidade antes do passo 4. Só depois pensa no pedido.
- Exercício 4: refaz cada linha a partir da quantidade da linha anterior, como no exemplo guiado. Compara a tua coluna "O que acontece" com a do colega, e não só os números.
- Exercício 5: para prever, segue a função com os valores que cada chamada lhe entrega, pela ordem em que os entrega.
- Desafio opcional: no primeiro caso, aplica as regras dos pedidos uma de cada vez. No segundo, escreve ao lado de cada parâmetro da função o valor que ele recebeu.
- Mais longe 1: para cada pedido, escreve as regras do guia que se aplicam, uma a uma.
- Mais longe 2: em cada linha, verifica as regras antes de mexer na quantidade, e não faças só a conta.
- Mais longe 3: decide a ordem dos três pedidos antes de escolher os números.

## Desafio opcional

Estes dois casos parecem simples e enganam muita gente. Faz primeiro o raciocínio no papel.

1. Uma ficha tem 0 unidades e chega o pedido "retirar 0". Um colega diz que o pedido é aceite, porque não se está a retirar mais do que existe. Outro colega diz que é recusado. Quem tem razão? Depois, segue `retirar(0, 0)` linha a linha, com a função do guia, sem executar: qual das duas perguntas do `if` decide, e que `return` se executa?
2. Um colega quis retirar 3 cadernos no primeiro programa do guia, que é também o da fase 1 do laboratório, com o caderno a 6 unidades. Mas escreveu os dois valores da chamada pela ordem trocada. Substituiu as quatro linhas que vêm depois das variáveis do caderno (as duas chamadas e os dois `print`) por estas duas:

   ```python partial
   quantidade_caderno = retirar(3, quantidade_caderno)
   print(nome_caderno, quantidade_caderno)
   ```

   Estas duas linhas não correm sozinhas: dependem da função `retirar` e das três variáveis do caderno, que ficam como estão no programa. O colega executou, viu `Caderno 3` e concluiu que a linha está certa, porque 6 - 3 = 3.

   - Segue a função com os valores que ela recebeu de facto, pela ordem em que os recebeu, e explica porque é que apareceu 3.
   - Propõe outro número de unidades para o pedido, com o qual o engano se veja no resultado. Diz o que o programa mostraria e o que devia mostrar.

## Para ires mais longe

Estes três exercícios aprofundam o tema. Faz-os quando o professor os indicar, ou se acabares o resto da ficha.

### Mais longe 1: Os casos que o exemplo não mostrou

A ficha A02, "Pasta", tem 3 unidades. Cada linha da tabela é um caso separado, que começa sempre com 3 unidades. Copia a tabela e completa-a. Na última coluna, indica que regra do guia usaste para decidir.

| Pedido | Aceite ou recusado | Quantidade depois | Regra usada |
| --- | --- | ---: | --- |
| Retirar 3 | A completar | A completar | A completar |
| Retirar 0 | A completar | A completar | A completar |
| Adicionar 4 | A completar | A completar | A completar |
| Retirar 1,5 | A completar | A completar | A completar |

Depois, em duas ou três frases, explica porque é que "retirar 3" e "retirar 0" têm respostas diferentes, apesar de o zero aparecer nos dois casos.

### Mais longe 2: A ordem dos pedidos

A ficha A03, "Caneta", tem 4 unidades. Vais construir dois traços, cada um a começar em 4.

No primeiro traço, os pedidos são, por esta ordem: adicionar 5 e depois retirar 7. No segundo traço, os mesmos pedidos aparecem pela ordem inversa: retirar 7 e depois adicionar 5.

Usa colunas iguais às do exemplo guiado do guia. Compara a quantidade final dos dois traços e explica porque são diferentes, se os pedidos são os mesmos. Termina com uma frase que explique a um colega porque é que, num traço, não se pode trocar a ordem das linhas.

### Mais longe 3: Uma ficha tua

Escolhe um material fictício da sala e cria a sua ficha, com código, nome e quantidade inicial. Não acrescentes outros campos.

Escreve uma sequência de três pedidos sobre essa ficha, a começar na quantidade inicial que escolheste. Um pedido tem de ser aceite, outro tem de ser recusado, e um deles tem de deixar a quantidade em zero. Vais ter de planear a ordem e os números antes de escrever o traço. Apresenta a sequência como um traço, com as colunas do exemplo guiado.

Por baixo do traço, explica a diferença entre aquilo que escolheste guardar na ficha e aquilo que escolheste fazer com esses dados.

## Critérios de conclusão

- Fizeste os exercícios 1 a 5, com a razão escrita em cada decisão, e não só o resultado.
- Nos teus traços, cada linha começa na quantidade deixada pela anterior, e as regras verificam-se antes da conta.
- No exercício 4, corrigiste as duas linhas erradas e as linhas que vêm depois delas.
- No exercício 5, confirmaste as previsões a executar o programa, se tiveste o computador contigo.

## Autoavaliação

1. Qual destas ideias ainda não consegues explicar sem voltar ao guia: entidade, estado, operação, as regras dos pedidos ou o traço? É por aí que deves começar a próxima revisão.
2. Em algum exercício confundiste o zero do pedido com o zero do estado? Em qual?
3. Relê as tuas respostas: em cada decisão escreveste a razão, e não só o resultado?

![Rodapé](../imagens/rodape.png)

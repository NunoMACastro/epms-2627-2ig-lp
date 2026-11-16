![Cabeçalho](../../imagens/cabecalho.png)

# Ficha de exercícios: Entidades, estado e ações

Decides o que é entidade num problema e que informação leva uma ficha, aplicas as regras do inventário em traços e lês um programa com variáveis soltas. Os exercícios 1 a 5 são obrigatórios. Respondes em papel, numa folha, com o número de cada exercício e a razão de cada decisão, e entregas a folha pelo meio que o professor indicar. Para rever: o [guia do tema](../01-entidades-estado-acoes.md) e o [laboratório](../laboratorios/01-entidades-estado-acoes-laboratorio.md).

## Exercício 1: As entidades de um torneio

A associação de estudantes vai organizar um torneio de futsal entre as turmas da escola. Quer um programa que responda a duas perguntas. Primeira: que jogos estão marcados, com a data e as duas equipas de cada jogo? Segunda: quantos pontos tem cada equipa na classificação?

1. Para cada uma destas cinco coisas, diz se é uma entidade neste programa: as equipas, os jogos, a bola, as bancadas do pavilhão e os jogadores de cada equipa. Justifica cada uma numa frase, a partir das duas perguntas.
2. Das coisas que são entidades, há alguma em que não se consiga tocar? Qual ou quais, e porque é que isso não as impede de ser entidades?
3. A associação acrescenta ao programa uma terceira pergunta: quem é o melhor marcador do torneio, isto é, o jogador que marcou mais golos? Que resposta da alínea 1 muda, e porquê?

Rever: [Entidade: aquilo que escolhemos representar](../01-entidades-estado-acoes.md#entidade-aquilo-que-escolhemos-representar).

<details>
<summary>Pista</summary>

Para cada coisa, procura que informação sobre ela o programa tem de guardar para responder às duas perguntas.

</details>

## Exercício 2: A ficha de um livro

A turma montou uma pequena biblioteca na sala, com livros que os alunos trouxeram de casa. Há um só exemplar de cada livro. O programa da biblioteca tem de responder a uma pergunta: um certo livro está na estante ou está emprestado?

1. A ficha A01 do guia guarda uma quantidade. A ficha de um livro precisa de uma quantidade, ou há outra informação que responde melhor à pergunta do programa? Decide e justifica em duas ou três frases.
2. Faz a ficha de um livro inventado por ti, numa tabela com as colunas "Informação" e "O que guardámos", como a ficha A01. Põe só a informação de que o programa precisa. Por baixo, escreve uma frase por linha, a dizer para que serve.
3. Escreve as operações que fazem sentido para um livro desta biblioteca, e diz se cada uma só lê a ficha ou se a altera.

Rever: [A informação que interessa guardar](../01-entidades-estado-acoes.md#a-informação-que-interessa-guardar) e [Comportamento: o que podemos pedir que aconteça](../01-entidades-estado-acoes.md#comportamento-o-que-podemos-pedir-que-aconteça).

<details>
<summary>Pista</summary>

Escreve as duas respostas que o programa pode dar à pergunta da biblioteca. Depois pensa que informação, guardada na ficha do livro, dá logo essas respostas.

</details>

## Exercício 3: O pedido que falta

A ficha A06, "Régua", começa com 5 unidades e recebe cinco pedidos, uns a seguir aos outros. Cada pedido encontra a quantidade que o anterior deixou.

| Passo | Pedido | O que acontece | Quantidade depois |
| --- | --- | --- | ---: |
| Início | Nenhum | A ficha indica 5 unidades | 5 |
| 1 | Retirar 2 | A completar | A completar |
| 2 | Retirar 4 | A completar | A completar |
| 3 | Adicionar 2 | A completar | A completar |
| 4 | A completar | A completar | 0 |
| 5 | Retirar 1 | A completar | A completar |

1. Na tua folha, escreve, para cada passo, o que acontece e a quantidade depois. No passo 4 falta também o pedido: sabes apenas que, depois dele, a quantidade ficou em 0.
2. Explica porque é que, no passo 4, só há um pedido possível.

Rever: [Uma operação tem de respeitar regras](../01-entidades-estado-acoes.md#uma-operação-tem-de-respeitar-regras) e [Exemplo guiado: seguir os valores passo a passo](../01-entidades-estado-acoes.md#exemplo-guiado-seguir-os-valores-passo-a-passo).

<details>
<summary>Pista</summary>

Faz primeiro os passos 1 a 3 e vê com quantas unidades a ficha chega ao passo 4. Só depois procura o pedido. Para a alínea 2, pensa no que aconteceria se adicionasses, se retirasses mais do que há ou se retirasses 0.

</details>

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

1. Encontra as duas linhas em que o colega aplicou mal as regras. Para cada uma, diz o que devia ter acontecido e porquê, pelas regras do guia.
2. Faz o traço corrigido.

Rever: [Uma operação tem de respeitar regras](../01-entidades-estado-acoes.md#uma-operação-tem-de-respeitar-regras) e [Exemplo guiado: seguir os valores passo a passo](../01-entidades-estado-acoes.md#exemplo-guiado-seguir-os-valores-passo-a-passo).

<details>
<summary>Pista</summary>

Para encontrar os erros, verifica cada linha do colega com a quantidade que ele escreveu na linha de cima. Olha para a coluna "O que acontece", e não só para os números. No traço corrigido, cada linha parte da quantidade da tua linha de cima.

</details>

## Exercício 5: De quem é cada variável

Este programa usa a mesma função `retirar` do guia. No guia, as três variáveis de cada artigo estavam juntas. Aqui, primeiro vêm os dois códigos, depois os dois nomes e por fim as duas quantidades.

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

1. Faz uma tabela com as seis variáveis, `c1`, `c2`, `n1`, `n2`, `q1` e `q2`. Para cada uma, escreve o artigo a que pertence, com o código e o nome, e se guarda o código, o nome ou a quantidade.
2. Descobre, sem executar, as duas linhas que o programa mostra. Diz também, para cada chamada a `retirar`, se o pedido é aceite ou recusado.
3. Escreve as duas linhas que, no fim do programa, retiram 2 unidades de fita-cola e mostram a seguir o nome e a quantidade da fita-cola. Escreve também a linha nova que o programa passa a mostrar.

Se tiveres o computador contigo, podes executar o programa com as tuas duas linhas e confirmar as alíneas 2 e 3.

Rever: [O problema das variáveis soltas](../01-entidades-estado-acoes.md#o-problema-das-variáveis-soltas), [A maneira habitual nos primeiros programas: programação estruturada](../01-entidades-estado-acoes.md#a-maneira-habitual-nos-primeiros-programas-programação-estruturada) e [A função devolve um valor, e a atribuição guarda-o](../01-entidades-estado-acoes.md#a-função-devolve-um-valor-e-a-atribuição-guarda-o).

<details>
<summary>Pista</summary>

Antes de cada chamada, vê que valor tem nesse momento a variável que vai para a função. Depois aplica o `if` a esse valor e às unidades pedidas.

</details>

## Desafios

### Desafio 1: Uma ficha tua

Escolhe um material da sala, diferente dos do guia, e faz a sua ficha, só com o código, o nome e a quantidade inicial. Depois, escreve o traço de três pedidos a essa ficha, com as colunas do exemplo guiado. Um dos pedidos tem de ser aceite, outro tem de ser recusado, e um deles tem de levar a quantidade a zero.

Por baixo do traço, diz o que, no teu trabalho, é o estado da ficha e o que é o comportamento.

Rever: [Exemplo guiado: seguir os valores passo a passo](../01-entidades-estado-acoes.md#exemplo-guiado-seguir-os-valores-passo-a-passo), [Estado: como está a informação neste momento](../01-entidades-estado-acoes.md#estado-como-está-a-informação-neste-momento) e [Comportamento: o que podemos pedir que aconteça](../01-entidades-estado-acoes.md#comportamento-o-que-podemos-pedir-que-aconteça).

<details>
<summary>Pista</summary>

Antes de escreveres o traço, decide a ordem dos três pedidos, e só depois escolhe os números.

</details>

### Desafio 2: Retirar 0 com 0 unidades

Uma ficha tem 0 unidades e chega o pedido "retirar 0". Um colega diz que o pedido é aceite, porque não se está a retirar mais do que existe. Outro colega diz que é recusado. Quem tem razão?

Depois, segue `retirar(0, 0)` linha a linha, com a função do guia, sem executar. Qual das duas condições do `if` decide, e que `return` se executa?

Rever: [Uma operação tem de respeitar regras](../01-entidades-estado-acoes.md#uma-operação-tem-de-respeitar-regras) e [A maneira habitual nos primeiros programas: programação estruturada](../01-entidades-estado-acoes.md#a-maneira-habitual-nos-primeiros-programas-programação-estruturada).

<details>
<summary>Pista</summary>

Vê, uma a uma, as regras do guia que se aplicam a um pedido de retirada. Depois, diz se cada condição do `if` é verdadeira ou falsa.

</details>

### Desafio 3: Os valores pela ordem trocada

Um colega quis retirar 3 unidades ao caderno A01, que tem 6, com a função `retirar` do guia. Mas escreveu os dois valores da chamada pela ordem trocada:

```python
# inventario.py: o artigo A01 e um pedido de 3 cadernos.


def retirar(quantidade, unidades):
    """Devolve a quantidade que fica depois de um pedido de retirada.

    Se o pedido for possível, devolve a quantidade menos as unidades pedidas.
    Se não for possível, devolve a quantidade que recebeu, sem mudanças.
    """
    if unidades > 0 and unidades <= quantidade:
        return quantidade - unidades
    return quantidade


codigo_caderno = "A01"
nome_caderno = "Caderno"
quantidade_caderno = 6

quantidade_caderno = retirar(3, quantidade_caderno)
print(nome_caderno, quantidade_caderno)
```

O colega executou, viu `Caderno 3` e concluiu que a linha está certa, porque 6 - 3 = 3.

1. Segue a função com os valores que ela recebeu de facto, pela ordem em que os recebeu, e explica porque é que apareceu 3.
2. Propõe outro número de unidades para o pedido, com o qual o engano se veja no resultado. Diz o que o programa mostraria e o que devia mostrar.

Rever: [A maneira habitual nos primeiros programas: programação estruturada](../01-entidades-estado-acoes.md#a-maneira-habitual-nos-primeiros-programas-programação-estruturada).

<details>
<summary>Pista</summary>

Escreve ao lado de cada parâmetro da função o valor que ele recebeu nesta chamada.

</details>

## Critérios de conclusão

- Fizeste os exercícios 1 a 5, com a razão de cada decisão escrita, e não só o resultado.
- Nos teus traços, cada linha parte da quantidade com que a anterior acabou, e cada pedido passa pelas regras antes de qualquer conta.
- No exercício 4, o traço corrigido segue as regras do inventário em todas as linhas.
- No exercício 5, a tabela liga cada variável ao seu artigo, e as duas linhas novas fazem o pedido à fita-cola e mostram-na.

![Rodapé](../../imagens/rodape.png)

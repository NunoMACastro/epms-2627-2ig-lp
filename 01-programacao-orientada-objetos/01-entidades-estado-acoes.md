![Cabeçalho](../imagens/cabecalho.png)

# Dos materiais da sala aos dados de um programa

*M10 · Caderno 1*

Imagina que és responsável pelos materiais de uma sala. Existem cadernos, pastas e canetas. Algumas unidades são usadas, outras chegam mais tarde. Quando alguém pergunta “ainda temos pastas?”, precisas de uma forma de responder sem fazer uma contagem de cada vez.

Podemos começar por um registo simples e, mais tarde, escrever um programa que nos ajude a mantê-lo. Neste caderno vamos perceber **que informação precisamos de guardar e que operações fazem sentido sobre ela**. Ainda não precisas de escrever JavaScript.

## Antes de começarmos

O professor vai propor um [diagnóstico de programação](../avaliacoes/diagnostico-inicial.md). Serve para perceber o que te recordas e onde precisas de apoio. Podes responder por palavras, desenhos, contas ou pseudocódigo; não tens de conhecer uma linguagem específica.

Depois trabalharás uma das actividades do [bridge de raciocínio](bridge-raciocinio.md), escolhida com o professor. “Bridge” significa aqui uma ponte: uma actividade curta para recuperar uma ideia necessária antes de avançar.

As explicações e exercícios seguintes ocupam a parte final deste primeiro bloco.

## 1. Que informação interessa guardar?

Uma ficha de material pode ter este aspecto:

| Informação | O que guardámos |
| --- | --- |
| Código | A01 |
| Nome | Caderno |
| Quantidade | 6 |

O **código** permite distinguir esta referência de outras. O **nome** descreve o material. A **quantidade** indica quantas unidades temos.

No nosso inventário, chamamos **artigo** a cada referência de material. A ficha A01 representa o artigo “Caderno”, do qual há seis unidades. Não representa um único caderno físico com seis unidades dentro dele, nem seis fichas diferentes.

Estamos a escolher uma representação simples para um problema simples. Se quiséssemos seguir cada equipamento individualmente, precisaríamos de outro tipo de registo. Aqui interessa-nos apenas consultar e alterar quantidades de materiais.

## 2. Entidade: aquilo que escolhemos representar

Ao analisar um problema, procuramos coisas ou ideias sobre as quais precisamos de guardar informação. Chamamos **entidade** a cada uma dessas coisas relevantes para o problema.

Neste caso, um artigo é uma entidade: queremos saber o seu código, o seu nome e a sua quantidade. A parede da sala existe, mas não precisamos de a representar para controlar estes materiais. Ser uma coisa real não basta para ter de entrar no programa; tem de ser relevante para o que queremos resolver.

Também podemos representar ideias que não são objectos físicos, como uma reserva ou uma tarefa. Por isso, “entidade” não significa apenas “algo em que conseguimos tocar”. Ao longo deste módulo vamos concentrar-nos nos artigos e no inventário que os reúne.

## 3. Estado: como está a informação neste momento

A ficha A01 diz que há 6 cadernos. Depois de alguém retirar 2, a quantidade deverá passar para 4.

Chamamos **estado** ao conjunto dos valores de uma entidade num certo momento. Podemos observar o estado antes e depois de uma operação:

| Informação | Antes de retirar | Depois de retirar 2 |
| --- | --- | --- |
| Código | A01 | A01 |
| Nome | Caderno | Caderno |
| Quantidade | 6 | 4 |

O artigo continua a ser A01. Mudou a quantidade, mas não estamos a falar de outro material. Esta distinção ajuda-nos a acompanhar o que uma operação fez realmente.

## 4. Comportamento: o que podemos pedir que aconteça

Além de guardar dados, um programa precisa de realizar operações. Para um artigo, podemos querer:

- **Consultar a quantidade:** saber o valor actual.
- **Adicionar unidades:** aumentar a quantidade quando chegam materiais.
- **Retirar unidades:** diminuir a quantidade quando são utilizados.

Estas operações descrevem **comportamentos**. “Quantidade 6” é uma informação sobre o estado. “Retirar 2” é um pedido de operação.

Consultar também é uma operação, mas não altera a quantidade. Se perguntas quantos cadernos existem e a resposta é 6, não passam a existir menos cadernos por teres feito a pergunta.

## 5. Uma operação tem de respeitar regras

Podes retirar 2 unidades quando existem 6. Mas não podes retirar 9: não há unidades suficientes. O programa deve recusar esse pedido e conservar a quantidade que existia.

Vamos adoptar regras simples: cada código identifica um artigo, o nome está preenchido e a quantidade é um número inteiro não negativo. “Inteiro” significa sem parte decimal; “não negativo” significa zero ou um número maior que zero.

**Ter zero unidades é possível:** o material esgotou. Neste percurso, uma operação de retirada pede um número inteiro positivo. Retirar zero não é um pedido aceite; retirar as últimas unidades pode deixar a quantidade em zero. A regra do pedido e a regra do estado não são a mesma coisa.

### Exemplo resolvido: seguir os valores passo a passo

Partimos de A01 com 6 unidades. Fazemos os pedidos seguintes pela ordem indicada:

| Passo | Pedido | O que acontece | Quantidade depois |
| --- | --- | --- | ---: |
| Início | Nenhum | A ficha indica 6 unidades | 6 |
| 1 | Consultar | Respondemos que existem 6; não alteramos a ficha | 6 |
| 2 | Retirar 2 | Há unidades suficientes; calculamos 6 − 2 | 4 |
| 3 | Retirar 5 | Só existem 4; o pedido é recusado | 4 |

A tabela chama-se um **traço**: um registo do que acontece em cada passo. Serve para explicar um programa e para encontrar erros. Repara que cada linha começa com a quantidade deixada pela linha anterior.

## 6. Como isto se relaciona com programação?

Talvez já tenhas escrito programas organizados em variáveis, condições, ciclos e funções. Por exemplo: ler uma quantidade, verificar um pedido e calcular um novo valor. Essa organização em passos e funções continua a ser útil.

Na programação orientada por objectos, procuramos também ligar os dados às operações que lhes dizem respeito. Perguntamos “que entidades vou representar?” e “o que deve cada uma saber fazer?”. Um artigo pode reunir os seus dados e as operações de consulta e alteração.

Não deixamos de usar condições nem funções. Estamos a acrescentar uma forma de organizar o programa em torno de responsabilidades. No próximo caderno vamos dar um nome mais preciso a essa unidade: **objecto**.

## 7. Vamos praticar

### Exercício 1: Distinguir informação de operação

A ficha A02 tem nome “Pasta” e quantidade 3. Lê as expressões: “A02”, “Pasta”, “quantidade 3”, “consultar a quantidade” e “retirar 1”.

Faz duas colunas: **informação que está na ficha** e **operação que podemos pedir**. Coloca cada expressão na coluna adequada. Explica uma das escolhas por uma frase.

### Exercício 2: Completar uma ficha depois de uma operação

Copia a ficha abaixo e completa a coluna final. O pedido é retirar uma unidade.

| Informação | Antes | Depois |
| --- | --- | --- |
| Código | A02 | A completar |
| Nome | Pasta | A completar |
| Quantidade | 3 | A completar |

Agora regressa ao estado inicial de 3 unidades e considera um pedido de 5. Escreve se o aceitarias e qual seria a quantidade final. São duas situações separadas, ambas com início em 3.

### Exercício 3: Construir um traço

Começa com 4 canetas na ficha A03. Por esta ordem, consulta a quantidade, retira 1 e tenta retirar 4. Faz uma tabela semelhante à da secção 5, com uma linha por pedido. Em cada linha explica se houve alteração.

### Exercício 4: Encontrar o passo que falta

Um programa tem uma ficha com 5 unidades. Recebe um pedido para retirar 2, verifica que o pedido é possível e apresenta “Pedido aceite”. No entanto, quando consultamos a quantidade, a resposta continua a ser 5.

O que devia ter acontecido à ficha? Escreve, por palavras, o passo que falta entre aceitar o pedido e apresentar a mensagem. Não precisas de escrever código.

### Exercício 5: Criar uma ficha tua

Escolhe um material interno fictício e cria uma ficha com código, nome e quantidade. Não precisas de acrescentar mais campos. Escreve um pedido de retirada possível e outro impossível, indicando sempre a quantidade inicial e a final.

Entrega a ficha e os dois casos. Quando explicares o trabalho, distingue aquilo que escolheste guardar daquilo que escolheste fazer com esses dados.

## O que deves levar deste caderno

Uma entidade é algo relevante que escolhemos representar. O estado descreve os seus valores num momento. O comportamento corresponde às operações que podemos pedir. Para verificar uma operação, não basta ler uma mensagem de sucesso: precisamos de acompanhar o que aconteceu aos dados.

![Rodapé](../imagens/rodape.png)

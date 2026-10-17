![Cabeçalho](../imagens/cabecalho.png)

# Ficha de recuperação: as bases do 10.º ano

Esta ficha ajuda-te a recuperar o raciocínio do 10.º ano antes de avançar no módulo Introdução à Programação Orientada por Objetos. Revês valores e condições, listas e ciclos, funções e ficheiros, sempre com o stock de um material como exemplo. É opcional e não tem entrega: fazes por tua conta, ao teu ritmo, e o que não acabares retomas noutro dia.

## O que precisas de saber

Esta ficha não ensina matéria nova. Usa o que aprendeste a programar no 10.º ano:

- as variáveis e a atribuição, que guarda um valor com um nome;
- as condições, com as comparações, como `>` e `<=`, e com o `e`, que junta duas condições;
- as listas e o ciclo que percorre uma lista;
- as funções, com os parâmetros e o valor que devolvem;
- as pastas e os ficheiros de um projeto.

Se fizeste o [diagnóstico](../avaliacoes/diagnostico-inicial.md), as tarefas em que paraste dizem-te por onde começar.

## Como trabalhar

A ficha tem um cenário comum, quatro exercícios à escolha, um para cada base, e um problema novo. Começa pelo cenário. Depois escolhe, dos exercícios 1 a 4, o da base que está menos firme:

| Se no diagnóstico paraste em | Faz primeiro |
| --- | --- |
| Tarefas 1 e 2: valores, operações e condições | Exercício 1 |
| Tarefas 3 e 5: listas, ciclos e somas | Exercício 2 |
| Tarefa 4: funções e parâmetros | Exercício 3 |
| Tarefa 6: ficheiros e pastas | Exercício 4 |

Se não fizeste o diagnóstico, escolhe a base de que te lembras pior. Não tens de completar os quatro exercícios. Se quiseres, faz um segundo. Se precisares de apoio, fica na primeira dificuldade até a perceberes, em vez de saltares para outra. Depois, faz o exercício 5, que junta as bases num problema novo. Se as quatro bases estão firmes, podes ir direto a ele.

Os algoritmos estão em pseudocódigo: uma forma de escrever os passos de um programa que serve para raciocinar, e não para executar num programa específico. Nesta notação, `=` dá um valor a uma variável e `==` compara dois valores, como em Python. `Escreve:` mostra um valor no ecrã, e `devolver` entrega o resultado de uma função. Os blocos marcam-se só pela indentação, também como em Python. Em Python, `Se` é `if`, `Senão` é `else:`, `Para cada x em lista` é `for x in lista:`, `Função` é `def`, `devolver` é `return`, `Escreve:` é `print` e `e` é `and`.

Responde em papel, por palavras, com tabelas ou em pseudocódigo. Escreve sempre a resposta antes de experimentares. Se passares um algoritmo para Python e o executares, compara o resultado com o que tinhas previsto.

A última alínea dos exercícios 1 a 4 é de encontrar o erro. Há um programa com um erro: tu escolhes valores, ou observas, o que mostra o erro, explicas a causa e corriges.

Não há entrega: as respostas ficam contigo. Se ficares preso, leva a dúvida ao professor numa aula.

## O cenário

Um programa transforma uma situação inicial seguindo instruções. Para perceberes o resultado, acompanha os valores pela ordem em que mudam. Seguir os valores assim, instrução a instrução, chama-se fazer o traço do algoritmo.

Três ideias ajudam a seguir os valores. Uma atribuição substitui o valor anterior da variável. Uma condição escolhe um caminho. Um ciclo repete passos. Antes de corrigires código, escreve o que esperas e compara com o que cada instrução faz.

O stock de um material diz quantas unidades existem, e cada pedido retira unidades. A regra é esta. Só é permitido retirar uma quantidade positiva que não ultrapasse o stock.

```text
stock = 6
pedido = 2
Se pedido > 0 e pedido <= stock
    stock = stock - pedido
Escreve: stock
```

O stock começa em 6. O pedido é positivo e não ultrapassa 6, por isso a atribuição é executada: 6 - 2 = 4. O programa mostra 4. Se o pedido fosse 9, a condição falhava e o stock continuava em 6.

A regra foi escrita antes do código. É ela que permite dizer se o resultado está certo.

## Exercício 1: valores e condições

Usa o algoritmo do cenário.

1. Repete o traço com o pedido 6, com o pedido 0 e com o pedido -1. Em cada caso, escreve se a condição é verdadeira ou falsa e qual é o stock final.
2. Explica porque é que `pedido > 0`, sozinho, não cumpre toda a regra.
3. Altera a condição para uma regra diferente: "é permitido retirar zero unidades, mas nunca uma quantidade negativa nem superior ao stock". Indica um pedido que uma das regras aceita e a outra recusa. Se o stock final não mostrar a diferença, acrescenta ao algoritmo uma instrução que a mostre.
4. Que tipo de valor é `stock`? E uma mensagem como `"Pedido aceite"`? E o resultado de `pedido > 0`?
5. Encontrar o erro: um colega escreveu `stock = pedido` na instrução que retira as unidades. Escolhe valores que tornem o erro visível e explica a correção.

## Exercício 2: listas e ciclos

Uma lista guarda vários valores. Um acumulador é uma variável que conserva um resultado entre as passagens de um ciclo. Um contador é um acumulador que soma 1 cada vez que uma condição se cumpre.

```text
quantidades = [2, 5, 0]
total = 0
Para cada quantidade em quantidades
    total = total + quantidade
Escreve: total
```

1. Faz uma tabela com a quantidade consultada e o total em cada passagem.
2. Altera a lista para ter dois zeros. Acrescenta um contador de artigos sem stock e decide onde ele começa.
3. Encontrar o erro: um colega começa o contador dentro do ciclo. Explica que informação se perde e escolhe uma lista que prove o problema.

## Exercício 3: funções, parâmetros e retorno

Uma função permite reutilizar um cálculo. O parâmetro dá nome à entrada dentro da função. O argumento é o valor que se dá na chamada. Devolver um resultado não o mostra no ecrã. Cuidado com a consola interativa do Python, a que mostra `>>>`: lá, uma expressão escrita sozinha mostra o seu valor, mesmo sem `print`. Num programa executado a partir de um ficheiro, só aparece o que mandas mostrar.

```text
Função unidadesEmCaixas(numeroCaixas, unidadesPorCaixa)
    devolver numeroCaixas * unidadesPorCaixa

total = unidadesEmCaixas(3, 4)
Escreve: total
```

1. Identifica os parâmetros, os argumentos e o valor devolvido.
2. Escreve uma segunda chamada, para cinco caixas de duas unidades.
3. Se tirasses a linha `Escreve: total`, o cálculo deixava de existir? Explica.
4. Encontrar o erro: um colega usa sempre 4 dentro da multiplicação e ignora `unidadesPorCaixa`. Escolhe um teste que detete o erro e corrige-o.

## Exercício 4: ficheiros e organização

Uma pasta organiza ficheiros. O código descreve instruções. Um ficheiro de dados guarda informação. As instruções de utilização ajudam outra pessoa a executar o trabalho.

Enquanto corre, um programa guarda os valores na memória do computador, que se perde quando ele acaba. Um valor alterado na memória só chega ao ficheiro se o programa o gravar.

1. Desenha uma pasta `stock` com `instrucoes.txt`, `programa.py` e uma subpasta `dados`, que contém `quantidades.txt`.
2. Escreve o caminho até ao ficheiro das quantidades, a partir da pasta `stock`.
3. Explica a sequência de três passos: ler o ficheiro, alterar os valores na memória e gravar. O que acontece ao ficheiro se faltar o último passo?
4. Encontrar o erro: o programa para logo ao começar, e a última linha da mensagem é `FileNotFoundError: [Errno 2] No such file or directory: 'dados/quantidade.txt'`. Em português: não existe nenhum ficheiro nem pasta com este nome. Escreve uma hipótese para a causa e o que observarias para a confirmar, antes de mudares o algoritmo. Depois, corrige.

## Exercício 5: os pedidos de uma equipa

Uma equipa tem quatro pedidos de material: `[2, 0, 3, 1]`. Neste exercício, um pedido é válido se for um número inteiro positivo. Não há controlo de stock nesta tarefa.

1. Decompõe a solução em passos que percorram os pedidos, contem os válidos e somem só as unidades dos pedidos válidos. Escreve os passos por palavras ou em pseudocódigo. Na condição, podes escrever "é inteiro" por palavras.
2. Faz o traço com os quatro pedidos.
3. Propõe um segundo conjunto de pedidos que mostre se o algoritmo soma só os válidos, e explica porque é que um zero não chega para isso.
4. Se fizeste o exercício 4, indica também que dados gravarias no fim. Não precisas de programar a leitura nem a escrita do ficheiro.

## Apoio

- Exercício 1: na alínea 3, faz o traço com o teu pedido nas duas regras e compara o que o algoritmo mostra no fim. Na alínea 5, faz o traço das duas versões, a certa e a do colega, lado a lado, com os mesmos valores.
- Exercício 2: na alínea 3, faz o traço da versão do colega com uma lista tua. Se as duas versões derem o mesmo, essa lista não prova nada: procura outra.
- Exercício 3: na alínea 4, calcula o resultado certo e o do colega para o teste que escolheres, antes de dizeres se ele mostra o erro.
- Exercício 4: na alínea 4, a mensagem diz o caminho que o programa procurou. Compara-o com a árvore que desenhaste na alínea 1.
- Exercício 5: antes de escreveres os passos, decide que valores tens de guardar enquanto percorres a lista, e com que valor começa cada um.

## Desafio opcional

Transforma o teste de validade do exercício 5 numa função. Explica os parâmetros dela e o que devolve.

## Critérios de conclusão

- Fizeste pelo menos um dos exercícios 1 a 4 e o exercício 5, com o traço.
- Para um erro que encontraste, escreveste uma frase com esta forma: "O erro era…; confirmei-o com…; corrigi-o porque…; voltei a testar com…".
- Consegues explicar a um colega, ou ao professor, uma alteração a um destes algoritmos, sem voltares a ler o cenário.

## Autoavaliação

1. Em que exercício a tua previsão falhou, e o que te fez mudar de ideias?
2. Se ainda não consegues explicar uma alteração sem voltares a ler o cenário, em que passo concreto precisas de apoio? Leva esse passo ao professor: é por aí que a recuperação continua.

![Rodapé](../imagens/rodape.png)

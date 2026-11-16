![Cabeçalho](../../imagens/cabecalho.png)

# Ficha de recuperação: as bases do 10.º ano

Revês, em pseudocódigo, as bases da programação do 10.º ano: valores e condições, listas e ciclos, funções, e ficheiros e pastas. A ficha é opcional e não tem entrega. Fazes o exercício da base que tens menos firme, de 1 a 4, e depois o exercício 5. Respondes em papel, por palavras, com tabelas ou em pseudocódigo. Depois de tentares, compara as tuas respostas com a [resolução](bridge-raciocinio-resolucoes.md). Se ficares preso, pergunta ao professor numa aula.

Para escolher o exercício, usa o [diagnóstico](../../avaliacoes/diagnostico-inicial.md):

| Paraste, ou a previsão falhou, em | Começa pelo |
| --- | --- |
| Tarefas 1 e 2: valores, operações e condições | Exercício 1 |
| Tarefa 3, ou tarefa 5, alíneas a e b: listas, ciclos e somas | Exercício 2 |
| Tarefa 4: funções e parâmetros | Exercício 3 |
| Tarefa 6: ficheiros e pastas | Exercício 4 |
| Nenhuma, ou só a tarefa 5, alínea c: decompor um problema | Exercício 5, direto |

Se não fizeste o diagnóstico, escolhe a base de que te lembras pior. Se quiseres treinar mais, faz depois outro dos exercícios 1 a 4.

## O cenário

Os exercícios usam o stock de materiais: quantas unidades existem e os pedidos que as retiram.

Os algoritmos estão em pseudocódigo, como no diagnóstico. Escrevem-se para raciocinar, e não para executar tal como estão. Uma variável recebe um valor com `=`, e dois valores comparam-se com `==`. O que pertence a um `Se`, a um `Para cada` ou a uma `Função` fica indentado por baixo dele. As outras palavras correspondem a estas do Python:

| Pseudocódigo | Python |
| --- | --- |
| `Se condição` | `if condição:` |
| `Senão` | `else:` |
| `Para cada x em lista` | `for x in lista:` |
| `Função nome(parâmetros)` | `def nome(parâmetros):` |
| `devolver valor` | `return valor` |
| `Escreve: valor` | `print(valor)` |
| `e` | `and` |

Fazer o **traço** de um algoritmo é seguir os valores das variáveis, instrução a instrução, pela ordem em que mudam. Para confirmares uma resposta, podes passar o algoritmo para Python e executá-lo.

## Exercício 1: Valores e condições

Um pedido só pode retirar uma quantidade positiva que não ultrapasse o stock. Este algoritmo aplica a regra a um pedido:

```text
stock = 8
pedido = 3
Se pedido > 0 e pedido <= stock
    stock = stock - pedido
Escreve: stock
```

| Pedido | A condição | Stock final |
| ---: | --- | ---: |
| 3 | Verdadeira | 5 |
| 8 | A completar | A completar |
| 0 | A completar | A completar |
| -2 | A completar | A completar |

1. Faz o traço com os pedidos 8, 0 e -2, e completa a tabela. A linha do pedido 3 já está feita.
2. Explica porque é que `pedido > 0`, sozinho, não cumpre toda a regra.
3. Altera a condição para outra regra: "é permitido retirar zero unidades, mas nunca uma quantidade negativa nem superior ao stock". Confirma a tua condição com os pedidos -1, 8 e 9. Indica um pedido que uma das regras aceita e a outra recusa. Se o stock final não mostrar a diferença, acrescenta ao algoritmo uma instrução que a mostre.
4. Que tipo de valor é `stock`? E uma mensagem como `"Pedido aceite"`? E o resultado de `pedido > 0`?
5. Mostrar o erro: um colega escreveu `stock = pedido` na instrução que retira as unidades. Escolhe um pedido que esconda o erro e outro que o mostre, e explica a correção.

<details>
<summary>Pista</summary>

O `e` só dá verdadeiro quando as duas comparações são verdadeiras. Quando a condição do `Se` é falsa, o algoritmo salta as linhas indentadas por baixo dele. Na alínea 5, faz o traço da versão certa e da do colega com os mesmos valores.

</details>

## Exercício 2: Listas e ciclos

Este algoritmo soma as quantidades de três artigos, guardadas numa lista:

```text
quantidades = [2, 5, 0]
total = 0
Para cada quantidade em quantidades
    total = total + quantidade
Escreve: total
```

1. Faz uma tabela com a quantidade consultada e o total em cada passagem do ciclo.
2. Muda a lista para ter dois zeros. Acrescenta ao algoritmo um contador dos artigos sem stock. Decide em que linha o contador recebe o primeiro valor, e que valor é esse.
3. Mostrar o erro: um colega dá o primeiro valor ao contador dentro do ciclo, logo no início de cada passagem. Explica que informação se perde e escolhe uma lista que prove o problema.

<details>
<summary>Pista</summary>

O `total` é um acumulador: guarda um resultado de uma passagem do ciclo para a seguinte. Um contador é um acumulador que soma 1 de cada vez que uma condição se cumpre. Na alínea 3, faz o traço da versão do colega e da tua com a mesma lista.

</details>

## Exercício 3: Funções, parâmetros e retorno

Esta função calcula quantas unidades há em várias caixas iguais:

```text
Função unidadesEmCaixas(numeroCaixas, unidadesPorCaixa)
    devolver numeroCaixas * unidadesPorCaixa

total = unidadesEmCaixas(3, 4)
Escreve: total
```

1. Identifica os parâmetros, os argumentos e o valor devolvido.
2. Escreve uma segunda chamada, para sete caixas de três unidades, e diz que valor recebe cada parâmetro.
3. Se tirasses a linha `Escreve: total`, o programa continuava a calcular o total? Explica.
4. Mostrar o erro: um colega usa sempre 4 dentro da multiplicação e ignora `unidadesPorCaixa`. Escolhe um teste que detete o erro e corrige-o.

<details>
<summary>Pista</summary>

Os parâmetros são os nomes que as entradas têm dentro da função. Os argumentos são os valores que vão na chamada, pela mesma ordem. O valor devolvido é o resultado que a função entrega à linha que a chamou. Na alínea 4, calcula o resultado certo e o do colega para o teste que escolheres, antes de dizeres se ele mostra o erro. Se experimentares na consola do Python, a das linhas com `>>>`, repara que ela mostra o valor de cada expressão escrita sozinha. Um ficheiro executado só mostra o que lhe mandas mostrar.

</details>

## Exercício 4: Ficheiros e organização

Um programa de stock guarda as quantidades num ficheiro de dados, numa pasta própria.

1. Desenha a árvore da pasta `stock`, com as pastas e os ficheiros uns dentro dos outros: `instrucoes.txt`, `programa.py` e uma subpasta `dados`, que contém `quantidades.txt`.
2. Escreve o caminho até ao ficheiro das quantidades, a partir da pasta `stock`.
3. Explica o que faz cada um destes três passos: ler o ficheiro, alterar os valores na memória e gravar. O que acontece ao ficheiro se faltar o último?
4. Encontrar o erro: o programa para logo ao começar, e a última linha da mensagem é esta:

   ```text
   FileNotFoundError: [Errno 2] No such file or directory: 'dados/quantidade.txt'
   ```

   Em português: não existe nenhum ficheiro nem pasta com este nome. Escreve uma hipótese para a causa e o que observarias para a confirmar. Depois, diz como corrigias.

<details>
<summary>Pista</summary>

Na alínea 3, a memória é onde o programa guarda os valores enquanto está a correr. Na alínea 4, o texto entre aspas simples (`'`), no fim da mensagem, é o caminho que o programa procurou.

</details>

## Exercício 5: Os pedidos de uma equipa

Queremos um algoritmo para os pedidos de material de uma equipa. O algoritmo percorre os pedidos e mostra, no fim, quantos pedidos são válidos e a soma das unidades desses pedidos. Um pedido é válido se for um número inteiro positivo. Os pedidos que não são válidos não se contam nem se somam. Neste exercício não se controla o stock.

Os pedidos da equipa são `[2, 0, 3, 1]`.

1. Escreve os passos do algoritmo, por palavras ou em pseudocódigo. Na condição, podes escrever "é inteiro" por palavras.
2. Faz o traço com os quatro pedidos, numa tabela com uma linha por pedido e uma coluna para cada valor que guardas.
3. Propõe outros pedidos com que somar só os válidos e somar todos deem resultados diferentes. Explica porque é que os pedidos da equipa não servem para isso.
4. Se fizeste o exercício 4: amanhã queres ver estes resultados sem voltar a fazer as contas. Que dados gravarias no fim? Não precisas de programar a leitura nem a escrita do ficheiro.

<details>
<summary>Pista</summary>

Antes de escreveres os passos, decide que valores tens de guardar enquanto percorres os pedidos, e com que valor começa cada um. Em Python, `type(pedido) == int` diz se um pedido é inteiro.

</details>

## Desafios

### Desafio 1: Uma função para a validade de um pedido

Transforma numa função a condição que diz se um pedido é válido, no exercício 5. Explica os parâmetros dela e o que devolve.

### Desafio 2: A condição do colega

Um colega escreveu a condição do exercício 5 só com `pedido > 0`. Com os pedidos da equipa, o algoritmo dele mostra os mesmos resultados que um algoritmo certo. Escolhe outros pedidos com que ele mostre resultados errados, e diz o que mostra e o que devia mostrar.

## Critérios de conclusão

- Fizeste o exercício 5 e, se tinhas uma base menos firme, o exercício dessa base, com os traços que pedem.
- Num erro que encontraste, escreveste o caso que o mostra, a causa e a correção, e confirmaste a correção com o mesmo caso.

![Rodapé](../../imagens/rodape.png)

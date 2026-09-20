# Bridge: recuperar o raciocínio antes de avançar

*M10 · actividades de apoio · 60 minutos*

## Como trabalhar

Usa 10 minutos para ler o exemplo comum, 20 para o percurso indicado pelo professor, 20 para o problema de transferência e 10 para explicar e rever. Não tens de completar todos os percursos. Se terminares um percurso cedo, escolhe um segundo; se precisares de apoio, mantém o foco na primeira dificuldade.

Neste documento, `←` guarda um valor, `=` compara, `DEVOLVER` entrega um resultado e `MOSTRAR` apresenta-o. O pseudocódigo serve para raciocinar, não para executar num programa específico.

## Ideia e exemplo comum (10 minutos)

Um programa transforma uma situação inicial seguindo instruções. Para perceber o resultado, acompanha os valores pela ordem em que mudam. Uma atribuição substitui o valor anterior; uma condição escolhe um caminho; um ciclo repete passos. Antes de corrigir código, escreve o que esperas e compara com o que cada instrução faz.

Regra: só é permitido retirar uma quantidade positiva que não ultrapasse o stock.

```pseudocode
stock ← 6
pedido ← 2
SE pedido > 0 E pedido <= stock ENTÃO
    stock ← stock - pedido
FIM SE
MOSTRAR stock
```

O stock começa em 6. O pedido é positivo e não ultrapassa 6, por isso a atribuição é executada: 6−2=4. O programa mostra 4. Se o pedido fosse 9, a condição falhava e o stock continuava em 6. A regra foi declarada antes do código; é ela que permite dizer se o resultado está certo.

## Percurso A: valores e condições

1. Repete o traço com pedido 6, pedido 0 e pedido −1. Escreve a condição e o stock final em cada caso.
2. Explica por que `pedido > 0` sozinho não cumpre toda a regra.
3. Altera a condição para uma regra diferente: “é permitido retirar zero unidades, mas nunca quantidade negativa nem superior ao stock”. Indica um teste que distingue as duas regras.
4. Debugging: alguém usa `stock ← pedido` na operação de retirada. Escolhe valores que tornem o erro visível e explica a correção.

## Percurso B: listas e ciclos

Uma lista guarda vários valores. Um acumulador conserva um resultado entre passagens; se regressar a zero em todas elas, perde o trabalho anterior.

```pseudocode
quantidades ← [2, 5, 0]
total ← 0
PARA CADA quantidade EM quantidades
    total ← total + quantidade
FIM PARA
MOSTRAR total
```

1. Faz uma tabela com a quantidade consultada e o total em cada passagem.
2. Altera a lista para ter dois zeros. Acrescenta um contador de artigos sem stock, iniciado antes do ciclo.
3. Debugging: um colega inicia o contador dentro do ciclo. Explica que informação perde e escolhe uma lista que prove o problema.

## Percurso C: funções, parâmetros e retorno

Uma função permite reutilizar um cálculo. O parâmetro dá nome à entrada dentro da função; o argumento é o valor fornecido na chamada. Devolver um resultado não o apresenta automaticamente no ecrã.

```pseudocode
FUNÇÃO unidadesEmCaixas(numeroCaixas, unidadesPorCaixa)
    DEVOLVER numeroCaixas × unidadesPorCaixa
FIM FUNÇÃO

total ← unidadesEmCaixas(3, 4)
MOSTRAR total
```

1. Identifica parâmetros, argumentos e valor devolvido.
2. Faz uma segunda chamada para cinco caixas de duas unidades.
3. Se retirasses `MOSTRAR total`, o cálculo deixava de existir? Explica.
4. Debugging: um colega usa sempre 4 dentro da multiplicação e ignora `unidadesPorCaixa`. Escolhe um teste que detete o erro e corrige-o.

## Percurso D: ficheiros e organização

Uma pasta organiza ficheiros. O código descreve instruções; um ficheiro de dados guarda informação; as instruções de utilização ajudam outra pessoa a executar o trabalho. Um valor alterado em memória só chega ao ficheiro se o programa o gravar.

1. Desenha uma pasta `stock` com `instrucoes.txt`, `programa.pseudo` e uma subpasta `dados` contendo `quantidades.txt`.
2. Escreve o caminho até ao ficheiro de quantidades a partir de `stock`.
3. Explica a sequência “ler ficheiro → alterar em memória → gravar”. O que acontece ao ficheiro se faltar o último passo?
4. Debugging: o programa procura `quantidade.txt`, mas o ficheiro chama-se `quantidades.txt`. Descreve como verificarias a causa antes de mudar o algoritmo.

## Transferência (20 minutos)

Uma equipa tem quatro pedidos de material: `[2, 0, 3, 1]`. Neste exercício, um pedido é válido se for um número inteiro positivo. Não existe controlo de stock disponível nesta tarefa.

Decompõe a solução em passos que permitam percorrer os pedidos, contar os válidos e somar apenas as unidades válidas. Escreve em palavras ou pseudocódigo. Mostra um traço e propõe um segundo conjunto de pedidos que inclua um caso inválido diferente de zero. Se trabalhaste ficheiros, indica também quais seriam os dados a gravar no final; não precisas de programar leitura/escrita.

Se acabares cedo, transforma o teste de validade numa função e explica os seus parâmetros e retorno. Não precisas de criar classes.

## Verificação de saída (10 minutos)

Entrega o percurso escolhido, o traço do problema e uma frase com “O erro era…; confirmei-o com…; corrigi-o porque…”. Explica ao professor uma alteração sem consultar o exemplo. Se ainda não conseguires, identifica o passo concreto em que precisas de apoio; essa informação define a recuperação seguinte.

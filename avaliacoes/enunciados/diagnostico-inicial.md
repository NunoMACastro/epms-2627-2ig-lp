# Diagnóstico inicial: raciocínio e programação estruturada

*M10 · diagnóstico inicial · 45 minutos · trabalho individual*

## Antes de começar (3 minutos)

Este diagnóstico serve para escolher o apoio de que precisas. Não exige JavaScript, Git, HTML ou CSS. Podes explicar por palavras, desenhar uma tabela ou usar pseudocódigo. Se não souberes, indica onde deixaste de compreender; essa informação também ajuda o professor.

No pseudocódigo, `←` significa guardar um valor; `=` compara valores; `MOSTRAR` apresenta um resultado; `DEVOLVER` entrega o resultado de uma função. Os índices das listas começam em zero. Um ciclo `PARA i DE a ATÉ b` inclui os dois limites. `E` exige que as duas condições sejam verdadeiras. Não existe execução automática destes blocos.

## 1. Valores e operações (6 minutos)

Uma equipa regista a quantidade de um material interno, a sua designação e se está disponível para utilização.

a) Escolhe um tipo de valor adequado para cada informação e dá um exemplo fictício.

b) Neste algoritmo, `quantidade` conta caixas e cada caixa contém cinco unidades. Lê o algoritmo e indica os valores finais de `quantidade` e `total`. Mostra as contas.

```pseudocode
quantidade ← 4
quantidade ← quantidade + 3
unidadesPorCaixa ← 5
total ← quantidade × unidadesPorCaixa
```

c) Explica a diferença entre guardar o número `4` e o texto `"4"`.

## 2. Decidir e ler código (7 minutos)

Regra do exercício: um pedido só é aceite se a quantidade pedida for positiva e não exceder o stock.

```pseudocode
SE pedido > 0 E pedido <= stock ENTÃO
    MOSTRAR "Pedido aceite"
SENÃO
    MOSTRAR "Verifica a quantidade"
FIM SE
```

a) Para cada caso, indica a mensagem e justifica-a: `(pedido=2, stock=5)`, `(pedido=0, stock=5)`, `(pedido=6, stock=5)`.

b) Escolhe um caso em que `pedido` seja igual a `stock`. Qual deve ser a decisão segundo a regra?

c) O algoritmo altera o stock? Apoia a resposta numa operação que exista ou falte no código.

## 3. Listas e ciclos (8 minutos)

```pseudocode
quantidades ← [3, 0, 5]
total ← 0
PARA i DE 0 ATÉ 2
    total ← total + quantidades[i]
FIM PARA
MOSTRAR total
```

a) Constrói uma tabela com o índice, o valor consultado e o total depois de cada passagem.

b) O que mudarias no limite do ciclo se a lista passasse a ter quatro elementos?

c) Descreve uma alteração que permita contar quantos artigos têm quantidade zero. Não precisas de escrever numa linguagem concreta.

## 4. Funções e parâmetros (7 minutos)

Uma equipa calcula o número de unidades contidas em caixas iguais. Cada chamada indica o número de caixas e as unidades por caixa.

```pseudocode
FUNÇÃO calcularUnidades(numeroCaixas, unidadesPorCaixa)
    DEVOLVER numeroCaixas × unidadesPorCaixa
FIM FUNÇÃO

resultadoA ← calcularUnidades(2, 3)
resultadoB ← calcularUnidades(5, 2)
```

a) Identifica o nome da função, os parâmetros e os argumentos da primeira chamada.

b) Indica os dois resultados e explica por que podem ser diferentes usando a mesma função.

c) A função mostra alguma coisa no ecrã? Explica a diferença entre devolver um valor e mostrá-lo.

## 5. Encontrar o erro e decompor (7 minutos)

Pretende-se somar todas as quantidades da lista.

```pseudocode
quantidades ← [2, 4, 1]
PARA CADA quantidade EM quantidades
    total ← 0
    total ← total + quantidade
FIM PARA
MOSTRAR total
```

a) Prevê o resultado que este algoritmo apresenta. Identifica a instrução que impede a soma pretendida.

b) Propõe uma correção e um teste pequeno que permita verificar se funcionou. Explica o resultado esperado desse teste.

c) Divide o problema “receber uma quantidade, validá-la e apresentar o novo stock” em três tarefas em que cada tarefa tenha uma função diferente. Explica por palavras o que faz cada uma.

## 6. Ficheiros e organização (7 minutos)

Um projeto tem estes ficheiros:

```text
inventario/
  instrucoes.txt
  programa.pseudo
  dados/
    artigos.txt
```

a) Distingue ficheiro de pasta usando dois exemplos da árvore.

b) Escreve o caminho de `artigos.txt` a partir da pasta `inventario`.

c) O programa altera uma quantidade apenas na sua memória e fecha sem gravar. Explica o que esperas encontrar no ficheiro de dados ao reabrir e porquê.

d) Onde colocarias as instruções para executar o projeto? Explica a utilidade de separar instruções, programa e dados.

## Entrega

Entrega as respostas identificadas de 1 a 6. Assinala um ponto que resolveste com confiança e outro em que precisas de apoio. Não uses dados pessoais reais nos exemplos. As respostas ficam no canal indicado pelo professor, não num repositório público.

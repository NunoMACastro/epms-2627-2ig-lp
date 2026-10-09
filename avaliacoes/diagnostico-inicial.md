![Cabeçalho](../imagens/cabecalho.png)

# Diagnóstico inicial: raciocínio e programação estruturada

*M10 · revisão opcional · cerca de 45 minutos*

## Antes de começar (3 minutos)

Este diagnóstico é uma revisão opcional da programação estruturada do 10.º ano, para fazeres por tua conta, quando quiseres. Não é recolhido nem corrigido em aula. Serve para perceberes como raciocinas e o que ainda dominas, e para escolheres o que te convém rever. Feito de seguida, demora cerca de 45 minutos; o tempo indicado em cada parte serve só para te orientares.

Não precisas de nenhuma linguagem em particular. Podes responder por palavras, com uma tabela, com um desenho, em pseudocódigo ou em Python. Escreve sempre a tua resposta antes de experimentares: se passares um dos algoritmos para Python e o executares, compara o resultado com o que tinhas previsto. Se não souberes responder, escreve onde deixaste de compreender, porque é aí que está o que vale a pena rever.

Os algoritmos estão em pseudocódigo. Nesta notação, `=` dá um valor a uma variável e `==` compara dois valores, como em Python. `Escreve:` mostra um valor no ecrã, e `devolver` entrega o resultado de uma função a quem a chamou. Os blocos marcam-se só pela indentação, também como em Python: as linhas mais à direita, por baixo de um `Se`, de um `Para` ou de uma `Função`, pertencem a esse bloco. Os índices das listas começam em zero, e um ciclo `Para i de 0 até 2` inclui os dois limites. `e` exige que as duas condições sejam verdadeiras. Estes algoritmos não se executam tal como estão escritos.

## 1. Valores e operações (6 minutos)

Uma equipa regista a quantidade de um material interno, a sua designação e se está disponível para utilização.

a) Escolhe um tipo de valor adequado para cada informação e dá um exemplo fictício.

b) Neste algoritmo, `quantidade` conta caixas e cada caixa contém cinco unidades. Lê o algoritmo e indica os valores finais de `quantidade` e `total`. Mostra as contas.

```pseudocode
quantidade = 4
quantidade = quantidade + 3
unidadesPorCaixa = 5
total = quantidade * unidadesPorCaixa
```

c) Explica a diferença entre guardar o número `4` e o texto `"4"`.

## 2. Decidir e ler código (7 minutos)

Regra do exercício: um pedido só é aceite se a quantidade pedida for positiva e não exceder o stock.

```pseudocode
Se pedido > 0 e pedido <= stock
    Escreve: "Pedido aceite"
Senão
    Escreve: "Verifica a quantidade"
```

a) Para cada caso, indica a mensagem e justifica-a: `(pedido=2, stock=5)`, `(pedido=0, stock=5)`, `(pedido=6, stock=5)`.

b) Escolhe um caso em que `pedido` seja igual a `stock`. Qual deve ser a decisão segundo a regra?

c) O algoritmo altera o stock? Apoia a resposta numa operação que exista ou falte no código.

## 3. Listas e ciclos (8 minutos)

```pseudocode
quantidades = [3, 0, 5]
total = 0
Para i de 0 até 2
    total = total + quantidades[i]
Escreve: total
```

a) Constrói uma tabela com o índice, o valor consultado e o total depois de cada passagem.

b) O que mudarias no limite do ciclo se a lista passasse a ter quatro elementos?

c) Descreve uma alteração que permita contar quantos artigos têm quantidade zero. Não precisas de escrever numa linguagem concreta.

## 4. Funções e parâmetros (7 minutos)

Uma equipa calcula o número de unidades contidas em caixas iguais. Cada chamada indica o número de caixas e as unidades por caixa.

```pseudocode
Função calcularUnidades(numeroCaixas, unidadesPorCaixa)
    devolver numeroCaixas * unidadesPorCaixa

resultadoA = calcularUnidades(2, 3)
resultadoB = calcularUnidades(5, 2)
```

a) Identifica o nome da função, os parâmetros e os argumentos da primeira chamada.

b) Indica os dois resultados e explica por que podem ser diferentes usando a mesma função.

c) A função mostra alguma coisa no ecrã? Explica a diferença entre devolver um valor e mostrá-lo.

## 5. Encontrar o erro e decompor (7 minutos)

Pretende-se somar todas as quantidades da lista.

```pseudocode
quantidades = [2, 4, 1]
Para cada quantidade em quantidades
    total = 0
    total = total + quantidade
Escreve: total
```

a) Prevê o resultado que este algoritmo apresenta. Identifica a instrução que impede a soma pretendida.

b) Propõe uma correção e um teste pequeno que permita verificar se funcionou. Explica o resultado esperado desse teste.

c) Divide o problema “receber uma quantidade, validá-la e apresentar o novo stock” em três tarefas em que cada tarefa tenha uma função diferente. Explica por palavras o que faz cada uma.

## 6. Ficheiros e organização (7 minutos)

Um projeto tem estes ficheiros:

```text
inventario/
  instrucoes.txt
  programa.py
  dados/
    artigos.txt
```

a) Distingue ficheiro de pasta usando dois exemplos da árvore.

b) Escreve o caminho de `artigos.txt` a partir da pasta `inventario`.

c) O programa altera uma quantidade apenas na sua memória e fecha sem gravar. Explica o que esperas encontrar no ficheiro de dados ao reabrir e porquê.

d) Onde colocarias as instruções para executar o projeto? Explica a utilidade de separar instruções, programa e dados.

## No fim

Não há entrega: as respostas ficam contigo. Assinala um ponto que resolveste com confiança e outro em que precisas de apoio, e compara cada previsão com o que aconteceu quando experimentaste. As partes em que paraste, ou em que a previsão falhou, mostram-te o que vale a pena rever; se quiseres, leva essas dúvidas ao professor numa aula. Não uses dados pessoais reais nos exemplos. Não confundas terminar depressa com compreender.

![Rodapé](../imagens/rodape.png)

![Cabeçalho](../imagens/cabecalho.png)

# Diagnóstico inicial: raciocínio e programação estruturada

Revisão opcional da programação estruturada do 10.º ano, antes do módulo Introdução à Programação Orientada por Objetos. Fazes por tua conta, quando quiseres, e as respostas ficam contigo.

## Para que serve este diagnóstico

Serve para perceberes como raciocinas e o que ainda dominas da programação do 10.º ano, e para escolheres o que te convém rever. Não é recolhido nem corrigido em aula, e não tem nota.

Se não souberes responder a uma pergunta, escreve onde deixaste de compreender. É aí que está o que vale a pena rever.

## O que precisas de saber antes

- Nada para estudar. O diagnóstico revê o que trazes do 10.º ano:
  - os valores e as operações;
  - as condições;
  - as listas e os ciclos;
  - as funções e os parâmetros;
  - os ficheiros e as pastas de um projeto.

## Como está organizado

O diagnóstico tem seis tarefas. Feito de seguida, demora cerca de 45 minutos, assim repartidos:

- ler estas instruções: 5 minutos;
- tarefa 1, valores e operações: 5 minutos;
- tarefa 2, decidir e ler código: 5 minutos;
- tarefa 3, listas e ciclos: 10 minutos;
- tarefa 4, funções e parâmetros: 5 minutos;
- tarefa 5, encontrar o erro e decompor: 10 minutos;
- tarefa 6, ficheiros e organização: 5 minutos.

O tempo de cada tarefa serve só para te orientares.

Não precisas de nenhuma linguagem em particular. Podes responder por palavras, com uma tabela, com um desenho, em pseudocódigo ou em Python. Escreve sempre a tua resposta antes de experimentares. Se passares um dos algoritmos para Python e o executares, compara o resultado com o que tinhas previsto.

Os algoritmos estão em pseudocódigo. Nesta notação, `=` dá um valor a uma variável e `==` compara dois valores, como em Python. `Escreve:` mostra um valor no ecrã, e `devolver` entrega o resultado de uma função a quem a chamou.

Os blocos marcam-se só pela indentação, também como em Python. As linhas mais à direita, por baixo de um `Se`, de um `Para` ou de uma `Função`, pertencem a esse bloco. Os índices das listas começam em zero, e um ciclo `Para i de 0 até 2` inclui os dois limites. `e` exige que as duas condições sejam verdadeiras. Estes algoritmos não se executam tal como estão escritos.

Se os passares para Python, `Se` é `if`, `Senão` é `else:`, `Para cada x em lista` é `for x in lista:`, `Função` é `def`, `devolver` é `return`, `Escreve:` é `print` e `e` é `and`. O ciclo `Para i de 0 até 2` escreve-se `for i in range(0, 3):`, porque o `range` não inclui o último número.

## Tarefa 1: valores e operações (5 minutos)

Uma equipa regista a quantidade de um material interno, a sua designação e se está disponível para utilização.

a) Escolhe um tipo de valor adequado para cada informação e dá um exemplo fictício.

b) Neste algoritmo, `quantidade` conta caixas e cada caixa contém cinco unidades. Lê o algoritmo e indica os valores finais de `quantidade` e `total`. Mostra as contas.

```text
quantidade = 4
quantidade = quantidade + 3
unidadesPorCaixa = 5
total = quantidade * unidadesPorCaixa
```

c) Explica a diferença entre guardar o número `4` e o texto `"4"`.

## Tarefa 2: decidir e ler código (5 minutos)

Regra desta tarefa: um pedido só é aceite se a quantidade pedida for positiva e não exceder o stock.

```text
Se pedido > 0 e pedido <= stock
    Escreve: "Pedido aceite"
Senão
    Escreve: "Verifica a quantidade"
```

a) Para cada caso, indica a mensagem e justifica-a: `(pedido=2, stock=5)`, `(pedido=0, stock=5)`, `(pedido=6, stock=5)`.

b) Escolhe um caso em que `pedido` seja igual a `stock`. Qual deve ser a decisão segundo a regra?

c) O algoritmo altera o stock? Apoia a resposta numa operação que exista ou falte no código.

## Tarefa 3: listas e ciclos (10 minutos)

```text
quantidades = [3, 0, 5]
total = 0
Para i de 0 até 2
    total = total + quantidades[i]
Escreve: total
```

a) Constrói uma tabela com o índice, o valor consultado e o total depois de cada passagem.

b) O que mudarias no limite do ciclo se a lista passasse a ter quatro elementos?

c) Descreve uma alteração que permita contar quantos artigos têm quantidade zero. Não precisas de escrever numa linguagem concreta.

## Tarefa 4: funções e parâmetros (5 minutos)

Uma equipa calcula o número de unidades contidas em caixas iguais. Cada chamada indica o número de caixas e as unidades por caixa.

```text
Função calcularUnidades(numeroCaixas, unidadesPorCaixa)
    devolver numeroCaixas * unidadesPorCaixa

resultadoA = calcularUnidades(2, 3)
resultadoB = calcularUnidades(5, 2)
```

a) Identifica o nome da função, os parâmetros e os argumentos da primeira chamada.

b) Indica os dois resultados e explica porque é que podem ser diferentes usando a mesma função.

c) A função mostra alguma coisa no ecrã? Explica a diferença entre devolver um valor e mostrá-lo.

Se experimentares em Python, cuidado com a consola interativa, a que mostra `>>>`: lá, uma expressão escrita sozinha mostra o seu valor, mesmo sem `print`. Num programa executado a partir de um ficheiro, só aparece o que mandas mostrar.

## Tarefa 5: encontrar o erro e decompor (10 minutos)

Pretende-se somar todas as quantidades da lista.

```text
quantidades = [2, 4, 1]
Para cada quantidade em quantidades
    total = 0
    total = total + quantidade
Escreve: total
```

a) Prevê o resultado que este algoritmo apresenta. Identifica a instrução que impede a soma pretendida.

b) Propõe uma correção e um teste pequeno que permita verificar se funcionou. Explica o resultado esperado desse teste.

c) Divide o problema "receber uma quantidade, validá-la e apresentar o novo stock" em três tarefas em que cada tarefa tenha uma função diferente. Explica por palavras o que faz cada uma.

## Tarefa 6: ficheiros e organização (5 minutos)

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

## Como é avaliado

Não é. O diagnóstico não tem nota e não conta para a classificação. Serve só para ti.

## Entrega

Não há entrega: as respostas ficam contigo. Assinala um ponto que resolveste com confiança e outro em que precisas de apoio, e compara cada previsão com o que aconteceu quando experimentaste.

As tarefas em que paraste, ou em que a previsão falhou, mostram-te o que vale a pena rever. A tabela do início da [ficha de recuperação](../01-programacao-orientada-objetos/bridge-raciocinio.md) diz que exercício fazer para cada tarefa. Se quiseres, leva essas dúvidas ao professor numa aula.

Não uses dados pessoais reais nos exemplos. Não confundas terminar depressa com compreender.

![Rodapé](../imagens/rodape.png)

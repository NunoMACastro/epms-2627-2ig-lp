![Cabeçalho](../imagens/cabecalho.png)

# Diagnóstico inicial das bases do 10.º ano: o stock de materiais

Revês, em seis tarefas, a programação do 10.º ano: valores, decisões, listas e ciclos, funções, encontrar um erro e dividir um problema, e ficheiros. É opcional: fazes por tua conta, quando quiseres, sem entrega e sem nota. No fim, sabes que exercício da [ficha de recuperação](../01-programacao-orientada-objetos/exercicios/bridge-raciocinio.md) te convém.

## O stock de materiais

Uma equipa controla o stock dos seus materiais: as unidades de cada artigo e os pedidos que as retiram.

## O que precisas de saber antes

- O Python do 10.º ano, sem nada para estudar antes.
- Para confirmares as respostas, um computador com o Python, como nas aulas.

## Como está organizado

O diagnóstico demora cerca de 60 minutos:

| Parte | Tempo |
| --- | ---: |
| Ler estas instruções | 5 minutos |
| Tarefa 1: valores e operações | 5 minutos |
| Tarefa 2: decidir e ler código | 5 minutos |
| Tarefa 3: listas e ciclos | 10 minutos |
| Tarefa 4: funções e parâmetros | 5 minutos |
| Tarefa 5: encontrar o erro e decompor | 10 minutos |
| Tarefa 6: ficheiros e organização | 5 minutos |
| Confirmar no Python | 15 minutos |

Os tempos servem só para te orientares. Respondes numa folha, por palavras, com uma tabela, um desenho, pseudocódigo ou Python. Primeiro respondes sem o computador, e só depois [confirmas as tuas respostas](#como-confirmas-as-tuas-respostas).

## O pseudocódigo

Como em Python, `=` dá um valor, `==` compara, e os blocos marcam-se pela indentação. As outras palavras passam para Python assim:

| Pseudocódigo | Python |
| --- | --- |
| `Se condição` | `if condição:` |
| `Senão` | `else:` |
| `Para cada x em lista` | `for x in lista:` |
| `Para i de 0 até 2` | `for i in range(0, 3):` |
| `Função nome(parâmetros)` | `def nome(parâmetros):` |
| `devolver valor` | `return valor` |
| `Escreve: valor` | `print(valor)` |
| `e` | `and` |

O `Para i de 0 até 2` inclui o 2. O `range(0, 3)` do Python dá 0, 1 e 2, porque para antes do 3. Por isso, o último número do `range` é o do `até` mais 1. Os índices de uma lista começam em 0.

## Tarefa 1: valores e operações (5 minutos)

Para cada artigo, a equipa regista a quantidade, o nome e se está disponível.

a) Escolhe um tipo de valor adequado para cada uma destas informações, com um exemplo inventado.

b) Neste algoritmo, `quantidade` conta caixas, e cada caixa tem cinco unidades. Indica os valores finais de `quantidade` e de `total`, e mostra as contas.

```text
quantidade = 4
quantidade = quantidade + 3
unidadesPorCaixa = 5
total = quantidade * unidadesPorCaixa
```

c) Explica a diferença entre guardar o número `4` e o texto `"4"`.

## Tarefa 2: decidir e ler código (5 minutos)

Um pedido só é aceite se a quantidade pedida for positiva e não passar o stock. O algoritmo decide assim:

```text
Se pedido > 0 e pedido <= stock
    Escreve: "Pedido aceite"
Senão
    Escreve: "Verifica a quantidade"
```

a) Que mensagem aparece em cada caso? Justifica. Os casos são: pedido 2 e stock 5; pedido 0 e stock 5; pedido 6 e stock 5.

b) Escolhe um caso em que o pedido é igual ao stock. Segundo a regra, qual deve ser a decisão?

c) O algoritmo altera o stock? Justifica com uma instrução que existe no algoritmo, ou que lhe falta.

## Tarefa 3: listas e ciclos (10 minutos)

```text
quantidades = [3, 0, 5]
total = 0
Para i de 0 até 2
    total = total + quantidades[i]
Escreve: total
```

a) Faz uma tabela com uma linha por passagem do ciclo: o índice, o valor consultado e o total depois dessa passagem.

b) Se a lista passasse a ter quatro valores, o que mudavas no limite do ciclo?

c) Descreve uma alteração ao algoritmo que conte quantos artigos têm a quantidade zero. Podes descrevê-la por palavras.

## Tarefa 4: funções e parâmetros (5 minutos)

A equipa usa uma função para saber quantas unidades há em caixas iguais. Cada chamada diz o número de caixas e as unidades de cada caixa.

```text
Função calcularUnidades(numeroCaixas, unidadesPorCaixa)
    devolver numeroCaixas * unidadesPorCaixa

resultadoA = calcularUnidades(2, 3)
resultadoB = calcularUnidades(5, 2)
```

a) Identifica o nome da função, os parâmetros e os argumentos da primeira chamada.

b) Indica os dois resultados. Porque é que a mesma função dá resultados diferentes?

c) A função mostra alguma coisa no ecrã? Explica a diferença entre devolver um valor e mostrá-lo.

## Tarefa 5: encontrar o erro e decompor (10 minutos)

Este algoritmo devia somar todas as quantidades da lista:

```text
quantidades = [2, 4, 1]
Para cada quantidade em quantidades
    total = 0
    total = total + quantidade
Escreve: total
```

a) Prevê o resultado que o algoritmo mostra. Indica a instrução que impede a soma.

b) Propõe uma correção e um teste pequeno que mostre se ela funcionou. Diz o resultado que esperas desse teste.

c) Queremos um programa que trate o pedido de um artigo e mostre o stock que fica depois dele. Divide este problema em três partes, cada uma com um trabalho diferente, e explica por palavras o que faz cada parte. Se te faltar uma regra, escolhe uma e escreve-a.

## Tarefa 6: ficheiros e organização (5 minutos)

Um projeto está organizado nesta árvore de pastas e ficheiros:

```text
inventario/
  instrucoes.txt
  programa.py
  dados/
    artigos.txt
```

a) Usa dois exemplos da árvore para explicar a diferença entre um ficheiro e uma pasta.

b) Escreve o caminho de `artigos.txt` para quem já está dentro da pasta `inventario`.

c) O programa altera uma quantidade só na memória e fecha sem gravar. O que esperas encontrar no ficheiro de dados quando o voltas a abrir? Porquê?

d) Onde punhas as instruções para executar o projeto? Para que serve separar as instruções, o programa e os dados?

## Como confirmas as tuas respostas

O diagnóstico não é recolhido nem corrigido. Os resultados dos algoritmos confirmas tu, no Python.

Nas tarefas com algoritmos, passa o algoritmo para Python pela tabela de [O pseudocódigo](#o-pseudocódigo). Executa-o e compara o que aparece com a tua resposta. Algumas ajudas:

- Quando o algoritmo não mostra o valor que queres confirmar (tarefa 1, alínea b; tarefa 2, alínea c; tarefa 4), executa-o primeiro como está. Depois, acrescenta no fim um `print` para cada valor.
- Na tarefa 1, alínea c, experimenta fazer a mesma conta com o `4` e com o `"4"`.
- Na tarefa 2, dá primeiro valores a `pedido` e a `stock`, um caso de cada vez.
- Para veres cada passagem de um ciclo, põe dentro dele, no fim, um `print` com o que queres seguir.
- Na tarefa 3, alínea b, escreve primeiro a linha nova em pseudocódigo. Só depois a passas para Python, com a regra do `range`: o número do `até` mais 1.
- Na tarefa 5, alínea b, corre o teu teste também na versão do enunciado, e compara.
- Executa sempre a partir de um ficheiro `.py`. Cuidado com a consola interativa, a que mostra `>>>`: lá, uma expressão escrita sozinha mostra o seu valor, mesmo sem `print`. Num ficheiro executado, só aparece o que mandas mostrar.

Se o Python mostrar outra coisa ou der um erro, confirma primeiro, linha a linha, que passaste o algoritmo pela tabela. Só depois contas a previsão como falhada.

A maior parte das respostas por palavras não se confirma no Python. Se não tens a certeza de uma, conta essa tarefa como uma em que paraste. Assim, vais ao exercício dessa base na ficha de recuperação, que tem uma resolução.

## Depois do diagnóstico

Não há entrega: as respostas ficam contigo. Paraste numa tarefa quando não soubeste responder ou ficaste preso. Marca as tarefas em que paraste e aquelas em que a previsão falhou. Na tarefa 5, marca as alíneas. Numa tarefa em que paraste, aponta onde deixaste de perceber. É isso que vale a pena rever.

A tabela do início da [ficha de recuperação](../01-programacao-orientada-objetos/exercicios/bridge-raciocinio.md) diz por que exercício começar, também se não marcaste nenhuma. Se só falhaste a alínea b da tarefa 3, a dos limites do ciclo, pergunta ao professor numa aula. A ficha não treina os limites. Se quiseres, leva também as outras dúvidas ao professor.

![Rodapé](../imagens/rodape.png)

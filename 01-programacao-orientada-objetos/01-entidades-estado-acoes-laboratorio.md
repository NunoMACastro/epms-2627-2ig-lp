![Cabeçalho](../imagens/cabecalho.png)

# Laboratório: Entidades, estado e ações

Laboratório do tema Entidades, estado e ações, do módulo M10, Introdução à Programação Orientada por Objetos. Vais escrever um pequeno inventário em Python, com os materiais guardados em variáveis soltas, e seguir os valores a cada pedido. Cada passo diz o que fazer, porquê e o que deves ver, e avanças ao teu ritmo. O que não acabares na aula, acabas na aula seguinte. Tudo o que precisas está aqui; o [guia do tema](01-entidades-estado-acoes.md) tem a teoria completa, para quem quiser saber mais.

## O que vais construir

No fim, tens um ficheiro `inventario.py` com dois materiais de uma sala, um caderno e uma pasta, guardados em variáveis. Tens também uma função, `retirar`, que aceita ou recusa cada pedido de unidades. Pelo caminho, vais prever no papel o que o programa mostra quando mudas os pedidos. E vais ver dois enganos que o Python deixa passar sem nenhuma mensagem de erro: uma atribuição esquecida e uma variável trocada.

Ficas a saber seguir os valores de um programa passo a passo, numa tabela. E ficas a saber dar por um engano comparando o que previste com o que aparece no ecrã.

A forma de trabalhar é sempre a mesma. Antes de executares, escreves no papel o que esperas ver. Depois executas e comparas. Quando o resultado é diferente do que previste, explica a diferença antes de continuares: é essa explicação que mais te ensina.

| Fase | O que muda | O que funciona no fim |
| --- | --- | --- |
| 1 | Copias o primeiro programa e segues os pedidos num traço | O programa mostra `Caderno 4` duas vezes, e sabes de que passo do traço vem cada linha |
| 2 | Mudas o primeiro pedido para 6 e depois para 0 | Prevês com um traço o que o programa mostra, e explicas porque é que o mesmo pedido tem respostas diferentes |
| 3 | Apagas a atribuição de uma chamada | Vês que a função calcula um valor que se perde, sem nenhuma mensagem de erro |
| 4 | Passas ao programa do caderno e da pasta e corriges uma variável trocada | O programa mostra `Caderno 6` e `Pasta 1` |

## Palavras que vais usar

- Artigo: cada material do inventário, com um código, um nome e uma quantidade, como o caderno A01 com 6 unidades. Para saber mais, vê a secção "A informação que interessa guardar" do [guia](01-entidades-estado-acoes.md).
- Estado: os valores de um artigo num certo momento. Depois de retirar 2 cadernos, a quantidade do caderno passa de 6 para 4, e o artigo continua a ser o A01. Para saber mais, vê a secção "Estado: como está a informação neste momento" do [guia](01-entidades-estado-acoes.md).
- Pedido: o que pedimos a um artigo, como "retirar 2". Um pedido pode ser aceite ou recusado.
- As regras do inventário: um pedido tem de ser um número inteiro positivo, isto é, 1 ou mais; e não se pode retirar mais do que existe. A quantidade nunca fica negativa, mas pode ficar em 0, que quer dizer que o material esgotou. Para saber mais, vê a secção "Uma operação tem de respeitar regras" do [guia](01-entidades-estado-acoes.md).
- Recusar: deixar a quantidade como estava. Um pedido recusado não põe a quantidade a zero nem apaga o artigo.
- Traço: uma tabela com uma linha por pedido, que diz o que acontece e com que quantidade fica o artigo depois. Para saber mais, vê o exemplo guiado do [guia](01-entidades-estado-acoes.md).
- Função: um bloco de código com nome, que recebe valores, os parâmetros, e devolve um resultado com `return`. Já a usaste no 10.º ano.
- Docstring (do inglês, texto de documentação): o texto entre três aspas logo a seguir ao `def`, que explica a pessoas o que a função faz. O Python não o executa.
- Atribuição: a instrução com `=`, que guarda um valor numa variável. Lê-se da direita para a esquerda: primeiro calcula-se o lado direito, depois guarda-se o resultado no nome da esquerda.
- Variáveis soltas: variáveis que guardam pedaços do mesmo artigo, como o código, o nome e a quantidade do caderno, sem nada no programa que as ligue umas às outras. Para saber mais, vê "O problema das variáveis soltas", no [guia](01-entidades-estado-acoes.md).
- Previsão: o que escreves no papel, antes de executar, que esperas ver no ecrã.

## O que precisas

- O Python 3, a partir da versão 3.10, que é a linguagem em que escreves o programa. Confirma a versão no terminal, com o comando `python3 --version` (no Windows, `py --version`). Deve aparecer `Python 3.` e um número igual ou maior do que 10, como `Python 3.12.4`. Se nunca usaste o terminal, pede ajuda ao professor: este laboratório não volta a precisar dele. Com uma versão mais antiga, o laboratório funciona na mesma, e só muda o texto de algumas mensagens de erro.
- O editor de Python das aulas, onde escreves, guardas e executas o ficheiro. Executar quer dizer correr o ficheiro inteiro, com o botão ou a tecla de executar do editor (em muitos editores, é a tecla F5). O que o programa mostra aparece numa janela do editor, a consola.
- Papel e caneta, para as previsões, para os traços e para as respostas.

## Se alguma coisa falhar

1. Guardaste o ficheiro antes de executar? Alguns editores executam a última versão guardada, e não a que está no ecrã. Guarda sempre antes de executar.
2. Estás a executar o ficheiro certo? Confirma que se chama `inventario.py` e que está na pasta `tema-01`.
3. Executas o ficheiro inteiro? Cada execução começa do zero, com os valores iniciais das variáveis, e repete todos os pedidos pela ordem em que estão escritos.
4. Mudaste uma linha de propósito e não a desfizeste? As fases 2 e 3 dizem, no fim, como voltar ao programa certo. Se te perderes, copia outra vez o programa completo da fase onde estás.
5. Apareceu uma mensagem de erro? Lê primeiro a última linha: diz o tipo de erro e a razão. Depois procura-a em [problemas frequentes](#problemas-frequentes).

## Preparar o projeto

1. Na pasta onde guardas os trabalhos de LP, cria uma pasta nova chamada `tema-01`. Uma pasta própria para este laboratório evita que executes por engano o ficheiro de outro trabalho.
2. Dentro dessa pasta, cria um ficheiro novo chamado `inventario.py`, no editor de Python das aulas. O nome tem de acabar em `.py`, para o editor saber que é um programa em Python, e não deve ter espaços nem acentos. Vais usar sempre este ficheiro.
3. Confirma que o editor executa o ficheiro. Escreve nele só esta linha, guarda e executa:

   ```python
   print("Olá")
   ```

   O que deves ver: `Olá` na consola. Quer dizer que o editor executa o ficheiro que tens aberto. Se aparecer outra coisa, ou nada, pede ajuda ao professor antes de continuares. Depois apaga a linha e guarda o ficheiro vazio.

## Fase 1: Um programa que retira unidades, seguido passo a passo

O inventário da sala tem um artigo, o caderno A01, com 6 unidades. Quando alguém pede para retirar cadernos, o programa tem de decidir se aceita ou recusa o pedido. Segue as regras do inventário: o pedido tem de ser 1 ou mais, e não pode passar do que existe. Neste programa, o código, o nome e a quantidade do caderno ficam em três variáveis separadas, e a decisão fica numa função. Para saber mais, lê a secção "A maneira habitual nos primeiros programas: programação estruturada" do [guia](01-entidades-estado-acoes.md).

1. Escreve o programa todo no ficheiro `inventario.py`, com este conteúdo, e guarda-o:

   ```python
   # inventario.py: o artigo A01 e uma função que retira unidades de uma quantidade.


   def retirar(quantidade, unidades):
       """Devolve a quantidade que fica depois de um pedido de retirada.

       Se o pedido for possível, devolve a quantidade menos as unidades pedidas.
       Se não for possível, devolve a quantidade que recebeu, sem mudanças.
       """
       if unidades > 0 and unidades <= quantidade:
           return quantidade - unidades
       return quantidade


   # O artigo A01 fica guardado em três variáveis separadas.
   codigo_caderno = "A01"
   nome_caderno = "Caderno"
   quantidade_caderno = 6

   quantidade_caderno = retirar(quantidade_caderno, 2)
   print(nome_caderno, quantidade_caderno)

   quantidade_caderno = retirar(quantidade_caderno, 5)
   print(nome_caderno, quantidade_caderno)
   ```

   Leitura guiada: o programa tem duas partes. A primeira, do `def` ao segundo `return`, define a função `retirar`, que recebe a quantidade que existe e as unidades pedidas. A linha do `if` verifica as duas regras de uma vez: `unidades > 0` (o pedido é positivo) e `unidades <= quantidade` (há unidades suficientes). O `and` (em português, "e") exige que as duas sejam verdadeiras. Se forem, a função devolve a conta; se não, devolve a quantidade que recebeu, sem mudanças. Definir a função não a executa: só a prepara. A segunda parte guarda o caderno em três variáveis e faz dois pedidos. Cada pedido é uma atribuição: a função calcula a quantidade nova, e o `=` guarda-a em `quantidade_caderno`. Cada `print` mostra o nome e a quantidade.

2. Antes de executares, escreve no papel as duas linhas que esperas ver. Aplica as regras do inventário a cada pedido, pela ordem em que estão no programa, e lembra-te de que o segundo pedido chega com a quantidade que o primeiro deixou.

3. Executa o ficheiro. O que deves ver:

   ```text
   Caderno 4
   Caderno 4
   ```

   Quer dizer que o pedido de 2 foi aceite e o de 5 foi recusado. Se aparecer outra coisa, compara o teu ficheiro com o bloco acima, linha a linha, ou vê os [problemas frequentes](#problemas-frequentes).

4. Confere a tua previsão com o traço dos pedidos ao caderno. Um traço é uma tabela com uma linha por pedido. Este começa com uma consulta, no passo 1, que só lê a quantidade: o programa não a faz, mas o traço mostra-a para se ver que consultar não muda nada.

   | Passo | Pedido | O que acontece | Quantidade depois |
   | --- | --- | --- | ---: |
   | Início | Nenhum | A ficha indica 6 unidades | 6 |
   | 1 | Consultar | Respondemos que existem 6; a ficha não muda | 6 |
   | 2 | Retirar 2 | 2 é um inteiro positivo e não passa de 6; fazemos 6 - 2 | 4 |
   | 3 | Retirar 5 | 5 é um inteiro positivo, mas só existem 4; o pedido é recusado | 4 |

   Lê-se de cima para baixo. Cada linha começa com a quantidade deixada pela linha anterior: o pedido de 5 chega quando já só há 4. Em cada linha, as regras verificam-se antes da conta. Um pedido recusado deixa a quantidade como estava. Se a tua previsão foi diferente, procura no traço a linha onde te afastaste.

### Paragem 1

O programa corre e mostra `Caderno 4` duas vezes.

Pensa antes de continuares: o traço tem quatro linhas, o início e três passos, e o programa mostrou só duas. A que passos do traço correspondem as duas linhas que apareceram? E em que linha do programa está o ponto de partida, as 6 unidades? A resposta: a primeira linha do ecrã é a quantidade depois do passo 2 (retirar 2, ficam 4). A segunda é a quantidade depois do passo 3 (retirar 5, recusado, ficam 4). O ponto de partida está na linha `quantidade_caderno = 6`. O passo 1, consultar, não tem uma chamada própria no programa. Os `print` fazem um papel parecido: mostram a quantidade sem a mudar.

## Fase 2: O mesmo pedido, com quantidades diferentes

Um pedido decide-se sempre com a quantidade que existe no momento em que chega. Por isso, o mesmo pedido pode ser aceite numa altura e recusado noutra. Nesta fase mudas o primeiro pedido e prevês, com um traço, o que acontece ao segundo. Há também dois zeros que não se podem confundir: ficar com 0 unidades é um estado válido, e pedir 0 unidades é um pedido recusado. Para saber mais, lê a secção "Uma operação tem de respeitar regras" do [guia](01-entidades-estado-acoes.md).

1. Na primeira chamada, troca o 2 por 6. A linha fica assim:

   ```python partial
   quantidade_caderno = retirar(quantidade_caderno, 6)
   ```

   Esta linha não corre sozinha: substitui a primeira chamada do programa que já tens no ficheiro, e depende da função e das variáveis definidas antes dela. Deixa a segunda chamada como está, com o pedido de 5.

2. Antes de executares, copia este traço para o papel e completa-o. Depois escreve as duas linhas que esperas ver.

   | Passo | Pedido | O que acontece | Quantidade depois |
   | --- | --- | --- | ---: |
   | Início | Nenhum | A ficha indica 6 unidades | 6 |
   | 1 | Retirar 6 | A completar | A completar |
   | 2 | Retirar 5 | A completar | A completar |

   Guarda e executa. O que deves ver: `Caderno 0` duas vezes. O traço completo é este:

   | Passo | Pedido | O que acontece | Quantidade depois |
   | --- | --- | --- | ---: |
   | Início | Nenhum | A ficha indica 6 unidades | 6 |
   | 1 | Retirar 6 | 6 é um inteiro positivo e não passa de 6; fazemos 6 - 6 | 0 |
   | 2 | Retirar 5 | 5 é um inteiro positivo, mas existem 0; o pedido é recusado | 0 |

   Repara que retirar 6 com 6 unidades é aceite: o pedido é válido, e ficar com zero unidades é um estado válido.

3. Agora troca o 6 por 0, na mesma linha. Desta vez, faz tu o traço no papel, com as mesmas quatro colunas, a começar em 6. Escreve as duas linhas que esperas ver, guarda e executa. O que deves ver:

   ```text
   Caderno 6
   Caderno 1
   ```

   O traço certo é este:

   | Passo | Pedido | O que acontece | Quantidade depois |
   | --- | --- | --- | ---: |
   | Início | Nenhum | A ficha indica 6 unidades | 6 |
   | 1 | Retirar 0 | 0 não é um inteiro positivo; o pedido é recusado | 6 |
   | 2 | Retirar 5 | 5 é um inteiro positivo e não passa de 6; fazemos 6 - 5 | 1 |

   Se previste `Caderno 0` na primeira linha, confundiste o zero do pedido com o zero do estado. Pedir 0 unidades é um pedido inválido, e um pedido recusado não mexe na quantidade.

4. Volta a pôr o 2 na primeira chamada, guarda e executa. O que deves ver: outra vez `Caderno 4` duas vezes. É o programa da fase 1.

### Paragem 2

O programa voltou a mostrar `Caderno 4` duas vezes, e tens no papel os dois traços.

Pensa antes de continuares: o pedido de 5 foi recusado na experiência com o pedido de 6, e aceite na experiência com o pedido de 0. Porque é que o mesmo pedido teve respostas diferentes? A resposta: o pedido é o mesmo, mas encontrou quantidades diferentes. Na primeira experiência, chegou depois de a quantidade ter ficado em 0, e não havia unidades suficientes. Na segunda, chegou com 6 unidades, porque o pedido de 0 foi recusado e não mexeu na quantidade. Cada linha do traço começa na quantidade deixada pela anterior, e as regras verificam-se com essa quantidade.

E mais uma: olha só para a primeira linha da última execução, `Caderno 6`. Por essa linha, consegues saber se o pedido de 0 foi recusado? A resposta: não. A função devolveu 6, e 6 também seria o valor devolvido se a função aceitasse o pedido de 0, porque 6 - 0 = 6. Quem chama a função recebe só um número, e não fica a saber se o pedido foi recusado. É uma limitação deste programa, que o guia 03 resolve.

## Fase 3: A atribuição esquecida

Na linha `quantidade_caderno = retirar(quantidade_caderno, 2)` há duas coisas a acontecer. Lê-se da direita para a esquerda. Primeiro, o Python chama a função com 6 e 2, e a função verifica o pedido e devolve 4. Só depois a atribuição guarda esse 4 na variável. A função, por si só, não muda a variável: recebe um número e devolve outro. Nesta fase vais ver o que acontece quando falta a atribuição. Para saber mais, lê a secção "A maneira habitual nos primeiros programas: programação estruturada" do [guia](01-entidades-estado-acoes.md).

1. Na primeira chamada, apaga só a parte da esquerda, `quantidade_caderno =`, com o espaço que vem a seguir ao `=`, e deixa o resto. A linha tem de começar junto à margem, como as outras linhas fora da função. Fica assim:

   ```python partial
   retirar(quantidade_caderno, 2)
   ```

   Como na fase anterior, esta linha substitui a primeira chamada do ficheiro e depende do resto do programa. Não mexas na segunda chamada.

2. Antes de executares, escreve no papel as duas linhas que esperas ver. Guarda e executa. O que deves ver, sem nenhuma mensagem de erro:

   ```text
   Caderno 6
   Caderno 1
   ```

3. Responde no papel: a função foi chamada e fez a conta? Que valor devolveu, e o que aconteceu a esse valor? A resposta: sim, a função foi chamada, verificou o pedido, fez a conta 6 - 2 e devolveu 4. Esse 4 não foi guardado em lado nenhum e perdeu-se. Por isso, `quantidade_caderno` continuou com 6, e o pedido de 5 foi verificado com 6 e aceite.

4. Responde também: a saída é igual à da experiência com o pedido de 0, no passo 3 da fase 2, mas o que aconteceu dentro do programa não foi igual. Qual é a diferença? A resposta: na fase 2, a função recusou o pedido de 0 e devolveu 6, e a atribuição guardou esse 6 na variável. Aqui, a função aceitou o pedido de 2 e devolveu 4, mas não havia atribuição, e o 4 perdeu-se. O mesmo ecrã pode ter causas diferentes. Para as distinguir, é preciso ler o código ou fazer o traço.

5. O Python não mostrou nenhum erro, porque chamar uma função sem guardar o que ela devolve é uma instrução válida. Volta a escrever `quantidade_caderno =` no início da linha, guarda e executa. O que deves ver: `Caderno 4` duas vezes.

### Paragem 3

O programa voltou a mostrar `Caderno 4` duas vezes.

Pensa antes de continuares: na linha `quantidade_caderno = retirar(quantidade_caderno, 2)`, que parte verifica o pedido e calcula, e que parte escreve o resultado na ficha? A resposta: a chamada, `retirar(quantidade_caderno, 2)`, verifica e calcula. A atribuição, `quantidade_caderno =`, escreve o resultado na variável, que faz o papel da ficha. Sem a atribuição, o pedido é verificado e calculado, mas a ficha nunca muda.

## Fase 4: A variável trocada

Até aqui o programa tinha um só artigo. Com dois artigos, cada um ocupa três variáveis, e a ligação entre as três variáveis de um artigo só existe nos nomes que lhes demos. O Python não sabe que `codigo_pasta`, `nome_pasta` e `quantidade_pasta` descrevem a mesma pasta: para ele, são só valores com nomes. Nesta fase vais ver o que isso permite. Para saber mais, lê "O problema das variáveis soltas", no [guia](01-entidades-estado-acoes.md).

1. Substitui todo o conteúdo do ficheiro por este programa, que acrescenta o artigo A02, "Pasta", com 2 unidades, e guarda:

   ```python
   # inventario.py: o caderno e a pasta, cada um guardado em três variáveis soltas.


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

   codigo_pasta = "A02"
   nome_pasta = "Pasta"
   quantidade_pasta = 2

   # Queríamos retirar 1 pasta, mas escrevemos a variável do caderno no pedido.
   quantidade_pasta = retirar(quantidade_caderno, 1)

   print(nome_caderno, quantidade_caderno)
   print(nome_pasta, quantidade_pasta)
   ```

   Leitura guiada: a função é a mesma da fase 1. Depois vêm os dois artigos, cada um em três variáveis, separados por uma linha em branco. A seguir há um só pedido, para a pasta, com um engano que o comentário de cima descreve. No fim, os dois `print` mostram os dois artigos.

2. Antes de executares, escreve no papel as duas linhas que esperas ver. Segue os valores que a linha do pedido usa de facto, e não o que o comentário diz que queríamos. Executa. O que deves ver:

   ```text
   Caderno 6
   Pasta 5
   ```

   A pasta tinha 2 unidades, pedimos para retirar 1, e ficou com 5. A função recebeu 6 e 1, fez a conta 6 - 1, e a atribuição guardou o 5 na variável da pasta.

3. Encontra a linha com o engano: é a que está logo a seguir ao comentário que começa por `# Queríamos retirar 1 pasta`. Responde no papel: que variável está errada nessa linha, e que variável devia lá estar? A resposta: está errada a `quantidade_caderno`, dentro dos parênteses. Devia lá estar a `quantidade_pasta`, porque o pedido é sobre a pasta.

4. Corrige a linha, trocando só essa variável. Fica assim:

   ```python partial
   quantidade_pasta = retirar(quantidade_pasta, 1)
   ```

   A linha depende da função e das variáveis do programa acima. O comentário que está por cima dela deixou de ser verdade, porque já não há engano para descrever: apaga-o. Antes de executares, escreve as duas linhas que esperas ver. Guarda e executa. O que deves ver:

   ```text
   Caderno 6
   Pasta 1
   ```

5. Responde no papel: na versão com o engano, o Python mostrou alguma mensagem de erro? Se o comentário não existisse, como é que terias dado pelo engano? A resposta: não houve nenhuma mensagem de erro. Sem o comentário, dás pelo engano comparando a previsão com o ecrã. Quem escreveu no papel que a pasta ia ficar com 1 unidade vê `Pasta 5` e sabe que alguma coisa está errada. É por isso que, em todas as fases, escreves a previsão antes de executar.

### Paragem 4

O programa mostra `Caderno 6` e `Pasta 1`. O ficheiro `inventario.py` completo, como deve estar agora:

```python
# inventario.py: o caderno e a pasta, cada um guardado em três variáveis soltas.


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

codigo_pasta = "A02"
nome_pasta = "Pasta"
quantidade_pasta = 2

quantidade_pasta = retirar(quantidade_pasta, 1)

print(nome_caderno, quantidade_caderno)
print(nome_pasta, quantidade_pasta)
```

Pensa antes de terminares: porque é que o Python não deu pela variável trocada? A resposta: para o Python, `quantidade_caderno` e `quantidade_pasta` são só dois números com dois nomes diferentes. A ligação entre as três variáveis da pasta só existe na cabeça de quem escreveu o programa. E a função `retirar` não sabe nada sobre artigos: recebe dois números e devolve um terceiro. No tema seguinte, cada artigo passa a ser uma só unidade, um objeto, que guarda os seus dados e faz as suas operações.

## Problemas frequentes

### `NameError: name 'retirar' is not defined`

`NameError` quer dizer erro de nome, e o resto da mensagem, em inglês, diz que o nome `retirar` não está definido. A função não foi copiada, ou ficou escrita depois das linhas que a usam. Confirma que a função está no início do ficheiro, antes de todas as chamadas. O mesmo vale para qualquer função que escrevas nos desafios.

### `NameError: name 'quantidade_past' is not defined`, ou o mesmo com outro nome

Um nome de variável está escrito de duas maneiras diferentes, por exemplo com uma letra a menos. Copia o nome da linha onde a variável recebeu o primeiro valor. As versões recentes do Python acrescentam uma sugestão, como `Did you mean: 'quantidade_pasta'?`, que quer dizer "Querias dizer `quantidade_pasta`?".

### `TypeError: retirar() missing 1 required positional argument: 'unidades'`

`TypeError` quer dizer erro de tipo. A chamada tem só um valor dentro dos parênteses, e a função precisa de dois: a mensagem diz que falta o valor de `unidades`. Escreve os dois valores, separados por uma vírgula: primeiro a quantidade, depois as unidades.

### `SyntaxError`, muitas vezes com `expected ':'`

`SyntaxError` quer dizer erro de sintaxe, isto é, de escrita. Falta o sinal de dois pontos no fim da linha do `def` ou do `if`, e a mensagem quer dizer "esperava `:`". Acrescenta `:` no fim dessa linha. Em versões mais antigas do Python, a mensagem diz só `invalid syntax`, que quer dizer "escrita inválida".

### `IndentationError`, com `expected an indented block`

`IndentationError` quer dizer erro de indentação, e `expected an indented block` quer dizer "esperava um bloco indentado". As linhas de dentro da função não estão mais afastadas da margem do que a linha do `def`. Compara a indentação com a da função `retirar`, linha a linha.

### `IndentationError: unexpected indent`

A mensagem quer dizer "indentação inesperada". Uma linha fora da função começa com espaços, por exemplo quando, na fase 3, se apaga `quantidade_caderno =` e fica o espaço que vinha a seguir. Fora de uma função ou de um `if`, as linhas começam junto à margem. Apaga os espaços do início dessa linha.

### Aparece `None` no lugar de uma quantidade

Uma função que escreveste não tem a última linha, a que devolve a quantidade quando o pedido é recusado. Uma função que acaba sem `return` devolve `None`, que em Python quer dizer "nada". Acrescenta essa linha, como na função `retirar`.

### A quantidade não muda depois de um pedido, e não aparece nenhum erro

Falta a atribuição à esquerda da chamada, como na fase 3. Ou o nome à esquerda do `=` tem um engano, e o Python criou uma variável nova com esse nome. Confirma que a linha começa exatamente pelo nome da variável que queres mudar, seguido de `=`.

### O programa mostra o mesmo que antes, apesar de teres mudado o código

O ficheiro não foi guardado antes de executar, ou estás a executar outro ficheiro. Guarda e confirma que estás a executar o `inventario.py` da pasta `tema-01`.

## Desafios

1. Um terceiro artigo. Continua no ficheiro da paragem 4. Acrescenta o artigo com o código `A04`, o nome `Borracha` e 5 unidades, guardado em três variáveis com nomes que sigam o padrão das do caderno e da pasta. Escreve as três linhas a seguir às variáveis da pasta, separadas delas por uma linha em branco. No fim do ficheiro, acrescenta dois pedidos para retirar 3 borrachas, um a seguir ao outro. Põe a seguir a cada um uma linha que mostre o nome e a quantidade da borracha. Escreve cada pedido como uma atribuição, como os da fase 4. Antes de executares, faz o traço da borracha no papel e escreve as duas linhas novas que esperas ver. Pista: o segundo pedido chega com a quantidade que o primeiro deixou.
2. A operação adicionar. O programa só sabe retirar unidades, e um inventário também precisa de as adicionar quando chega material. Escreve a função `adicionar(quantidade, unidades)` a seguir à função `retirar`, com duas linhas em branco antes e depois. Deve devolver a quantidade mais as unidades, se o pedido for aceite, e a quantidade que recebeu, sem mudanças, se o pedido for recusado. Escreve uma docstring, como a de `retirar`, que diga isto por palavras. Antes de escreveres, decide no papel: o `if` da função `retirar` faz duas perguntas, `unidades > 0` e `unidades <= quantidade`. Qual delas faz sentido num pedido para adicionar, e qual não faz? Depois, no fim do ficheiro, acrescenta dois pedidos à borracha, cada um seguido de uma linha que mostre o nome e a quantidade: adicionar 4 e, a seguir, adicionar 0. Completa no papel o traço da borracha desde o início, com os quatro pedidos, e escreve as linhas que esperas ver. No fim, o programa deve mostrar seis linhas: duas do caderno e da pasta, e quatro da borracha. Pista: relê as regras do inventário, em "Palavras que vais usar", palavra a palavra, e vê a que pedidos se aplica cada uma.

## Antes de terminares

- [ ] O ficheiro `inventario.py` da pasta `tema-01` corre e mostra `Caderno 6` e `Pasta 1`, como na paragem 4.
- [ ] Desfizeste as alterações que fizeste de propósito nas fases 2 e 3.
- [ ] Tens no papel as previsões, os traços da fase 2 e as respostas das fases 3 e 4.
- [ ] Guardaste o ficheiro e a folha, e entregaste-os pelo meio indicado pelo professor.
- [ ] Consegues explicar, por palavras tuas, porque é que o Python não deu pela variável trocada, e como é que deste pelo engano.

![Rodapé](../imagens/rodape.png)

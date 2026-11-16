![Cabeçalho](../../imagens/cabecalho.png)

# Laboratório: Entidades, estado e ações

## O que vais construir

Escreves em Python um pequeno inventário da sala: um caderno e uma pasta, guardados em variáveis, e a função `retirar`, que aceita ou recusa cada pedido de unidades. Pelo caminho, encontras dois enganos que o Python deixa passar sem nenhuma mensagem de erro.

No fim, o programa `inventario.py` mostra:

```text
Caderno 6
Pasta 1
```

1. [Fase 1: A maneira habitual nos primeiros programas: programação estruturada](#fase-1-a-maneira-habitual-nos-primeiros-programas-programação-estruturada)
2. [Fase 2: Uma operação tem de respeitar regras](#fase-2-uma-operação-tem-de-respeitar-regras)
3. [Fase 3: A função devolve um valor, e a atribuição guarda-o](#fase-3-a-função-devolve-um-valor-e-a-atribuição-guarda-o)
4. [Fase 4: O problema das variáveis soltas](#fase-4-o-problema-das-variáveis-soltas)

## O que precisas

- O Python 3.10 ou mais recente. Confirma no terminal com `python3 --version` (no Windows, `py --version`). Deve aparecer `Python 3.` e um número de 10 para cima, como `Python 3.12.4`. Numa versão mais antiga, o laboratório funciona, e só mudam algumas mensagens de erro. Se nunca usaste o terminal, pede ajuda ao professor: o laboratório só precisa dele para isto.
- O editor de Python das aulas, onde escreves, guardas e executas o ficheiro.

## Preparar o projeto

1. Cria uma pasta só para este laboratório, para não executares por engano o ficheiro de outro trabalho. Na pasta onde guardas os trabalhos de LP, cria uma pasta nova chamada `tema-01`.

2. Cria o ficheiro do programa. No editor, cria dentro da pasta `tema-01` um ficheiro novo chamado `inventario.py`. O `.py` diz ao editor que o ficheiro é um programa em Python, e o nome não leva espaços nem acentos.

3. Confirma que o editor executa o ficheiro. Escreve nele só esta linha:

   ```python
   print("Olá")
   ```

   Guarda e executa. Executar é correr o ficheiro inteiro, com o botão ou a tecla de executar do editor (em muitos editores, a tecla F5). O que o programa mostra aparece na consola, uma janela do editor.

   O que deves ver: `Olá` na consola. Isto quer dizer que o editor executa o ficheiro que tens aberto. Se aparecer outra coisa, ou nada, pede ajuda ao professor antes de continuares. Depois apaga a linha e guarda o ficheiro vazio.

## Fase 1: A maneira habitual nos primeiros programas: programação estruturada

Escreves o primeiro programa do inventário à maneira da programação estruturada: os dados do caderno ficam em variáveis, e a decisão de cada pedido fica numa função. No fim, segues os pedidos numa tabela, o traço. Rever: [A maneira habitual nos primeiros programas: programação estruturada](../01-entidades-estado-acoes.md#a-maneira-habitual-nos-primeiros-programas-programação-estruturada) e [Exemplo guiado: seguir os valores passo a passo](../01-entidades-estado-acoes.md#exemplo-guiado-seguir-os-valores-passo-a-passo).

1. Começa pela função que decide cada pedido de retirada. Escreve no `inventario.py` esta primeira versão:

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
   ```

   A função recebe dois valores: em `quantidade`, as unidades que existem, e em `unidades`, as que o pedido quer retirar. A docstring (do inglês, texto de documentação) é o texto entre três aspas por baixo do `def`. Diz a quem lê o código o que a função faz, e o Python não a executa.

   O `if` verifica as duas condições de um pedido de retirada. A primeira é a regra dos pedidos: o número de unidades tem de ser positivo, isto é, 1 ou mais (`unidades > 0`). A segunda é que não se pode retirar mais do que existe (`unidades <= quantidade`), porque a quantidade nunca pode ficar negativa. O `and` (em português, "e") só deixa passar o pedido quando as duas são verdadeiras.

   Guarda e executa. O que deves ver: o programa não mostra nada, e não aparece nenhuma mensagem de erro. Isto quer dizer que o Python leu a função mas não a correu, porque nenhuma linha a chamou. Se aparecer outra coisa, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

2. Acrescenta o caderno e o primeiro pedido. No fim do ficheiro, deixa duas linhas em branco a seguir à função e acrescenta:

   ```python
   # O artigo A01 fica guardado em três variáveis separadas.
   codigo_caderno = "A01"
   nome_caderno = "Caderno"
   quantidade_caderno = 6

   quantidade_caderno = retirar(quantidade_caderno, 2)
   print(nome_caderno, quantidade_caderno)
   ```

   As três variáveis guardam a ficha do caderno A01, um artigo do inventário: o código, o nome e a quantidade. A chamada a `retirar` é um pedido para retirar 2 unidades. Os valores entram pela ordem em que estão escritos: `quantidade_caderno` vai para `quantidade`, e o 2 vai para `unidades`. A função calcula a quantidade que fica, e a atribuição, o `=`, guarda-a em `quantidade_caderno`.

   Guarda e executa. O que deves ver: `Caderno 4`. Isto quer dizer que o pedido de 2 foi aceite, porque cumpre as duas condições, e 6 - 2 = 4. Se aparecer outra coisa, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

3. Acrescenta um segundo pedido, de 5 unidades. No fim do ficheiro, deixa uma linha em branco e acrescenta:

   ```python
   quantidade_caderno = retirar(quantidade_caderno, 5)
   print(nome_caderno, quantidade_caderno)
   ```

   Antes de executares, prevê a linha nova que vai aparecer. Este pedido chega com a quantidade que o primeiro deixou. Depois guarda e executa.

   O que deves ver:

   ```text
   Caderno 4
   Caderno 4
   ```

   Isto quer dizer que o pedido de 5 foi recusado, e a quantidade ficou em 4. Se aparecer outra coisa, compara o teu ficheiro com o da [paragem 1](#paragem-1), linha a linha.

4. Confere a tua previsão com o traço dos pedidos ao caderno. Um traço é uma tabela com uma linha por pedido: o que acontece e com quantas unidades fica a ficha depois. Este começa com uma consulta, que o teu programa não tem: só lê a quantidade e não a muda.

   | Passo | Pedido | O que acontece | Quantidade depois |
   | --- | --- | --- | ---: |
   | Início | Nenhum | A ficha indica 6 unidades | 6 |
   | 1 | Consultar | Respondemos que existem 6; a ficha não muda | 6 |
   | 2 | Retirar 2 | 2 é um inteiro positivo e não passa de 6; fazemos 6 - 2 | 4 |
   | 3 | Retirar 5 | 5 é um inteiro positivo, mas só existem 4; o pedido é recusado | 4 |

   Cada linha parte da quantidade com que a de cima acabou: o pedido de 5 chega quando já só há 4. As duas condições verificam-se antes da conta, e um pedido recusado deixa a quantidade como estava.

### Paragem 1

O programa mostra `Caderno 4` duas vezes. Confere o teu `inventario.py` com este, completo:

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

A função vem primeiro, porque o Python lê o ficheiro de cima para baixo e tem de a conhecer antes de a chamar. Por baixo ficam a ficha do caderno e os dois pedidos, cada um com o seu `print`.

Pensa antes de continuares: o traço tem o início e três passos, e o programa mostrou só duas linhas. A que passos do traço correspondem as duas linhas, e em que linha do programa estão as 6 unidades do início? A resposta: a primeira linha do ecrã é a quantidade depois do passo 2, retirar 2. A segunda é a quantidade depois do passo 3, retirar 5, que foi recusado. As 6 unidades estão em `quantidade_caderno = 6`. O passo 1, consultar, não tem chamada no programa, mas os `print` fazem um papel parecido: mostram a quantidade sem a mudar.

## Fase 2: Uma operação tem de respeitar regras

Mudas o número do primeiro pedido, para 6 e depois para 0, e segues o que acontece ao pedido de 5. Pelo caminho, encontras dois zeros: o da quantidade que fica e o do pedido. Rever: [Uma operação tem de respeitar regras](../01-entidades-estado-acoes.md#uma-operação-tem-de-respeitar-regras) e [Exemplo guiado: seguir os valores passo a passo](../01-entidades-estado-acoes.md#exemplo-guiado-seguir-os-valores-passo-a-passo).

1. Experimenta um pedido que leva tudo o que existe. Na primeira chamada, troca o 2 por 6, e deixa a segunda chamada como está. A linha fica assim:

   ```python partial
   quantidade_caderno = retirar(quantidade_caderno, 6)
   ```

   Guarda e executa. O que deves ver: `Caderno 0` duas vezes. O traço destes pedidos é este:

   | Passo | Pedido | O que acontece | Quantidade depois |
   | --- | --- | --- | ---: |
   | Início | Nenhum | A ficha indica 6 unidades | 6 |
   | 1 | Retirar 6 | 6 é um inteiro positivo e não passa de 6; fazemos 6 - 6 | 0 |
   | 2 | Retirar 5 | 5 é um inteiro positivo, mas existem 0; o pedido é recusado | 0 |

   Retirar 6 com 6 unidades é aceite, porque cumpre as duas condições. Ficar com 0 é um estado válido: as regras do inventário pedem uma quantidade de 0 para cima, e o 0 quer dizer que o caderno esgotou.

2. Experimenta agora um pedido de 0. Na mesma linha, troca o 6 por 0. Antes de executares, completa de cabeça este traço e prevê as duas linhas:

   | Passo | Pedido | O que acontece | Quantidade depois |
   | --- | --- | --- | ---: |
   | Início | Nenhum | A ficha indica 6 unidades | 6 |
   | 1 | Retirar 0 | A completar | A completar |
   | 2 | Retirar 5 | A completar | A completar |

   Guarda e executa. O que deves ver:

   ```text
   Caderno 6
   Caderno 1
   ```

   O traço completo:

   | Passo | Pedido | O que acontece | Quantidade depois |
   | --- | --- | --- | ---: |
   | Início | Nenhum | A ficha indica 6 unidades | 6 |
   | 1 | Retirar 0 | 0 não é um inteiro positivo; o pedido é recusado | 6 |
   | 2 | Retirar 5 | 5 é um inteiro positivo e não passa de 6; fazemos 6 - 5 | 1 |

   Se previste `Caderno 0` na primeira linha, confundiste o zero do pedido com o zero do estado. Pedir 0 não cumpre a regra dos pedidos, que exige 1 ou mais, e um pedido recusado não mexe na quantidade. Repara também que a linha `Caderno 6` não diz que o pedido foi recusado: se a função o aceitasse, 6 - 0 dava 6 na mesma. Quem chama a função recebe só um número.

3. Volta a pôr o 2 na primeira chamada. Guarda e executa. O que deves ver: `Caderno 4` duas vezes, como na paragem 1.

### Paragem 2

O programa voltou a ser o da paragem 1, e mostra `Caderno 4` duas vezes.

Pensa antes de continuares: o pedido de 5 foi recusado depois do pedido de 6, e aceite depois do pedido de 0. Porque é que o mesmo pedido teve respostas diferentes? A resposta: encontrou quantidades diferentes. Depois do pedido de 6, chegou com 0 unidades, e não havia unidades que chegassem. Depois do pedido de 0, que foi recusado, chegou com as 6 do início. Um pedido decide-se sempre com a quantidade que existe quando ele chega.

## Fase 3: A função devolve um valor, e a atribuição guarda-o

Tiras a atribuição da primeira chamada e vês o que acontece ao valor que a função devolve quando ninguém o guarda. Rever: [A função devolve um valor, e a atribuição guarda-o](../01-entidades-estado-acoes.md#a-função-devolve-um-valor-e-a-atribuição-guarda-o).

1. Provoca um engano de propósito. Na primeira chamada, apaga só `quantidade_caderno =` e o espaço que vem a seguir ao `=`. A linha tem de começar junto à margem, como as outras linhas fora da função. Fica assim:

   ```python partial
   retirar(quantidade_caderno, 2)
   ```

   Não mexas na segunda chamada.

2. Antes de executares, prevê as duas linhas. Depois guarda e executa. O que deves ver, sem nenhuma mensagem de erro:

   ```text
   Caderno 6
   Caderno 1
   ```

   A função foi chamada, verificou o pedido, fez a conta 6 - 2 e devolveu 4. Mas nenhuma atribuição guardou esse 4, e ele perdeu-se. O Python não mostrou nenhum erro, porque chamar uma função sem guardar o que ela devolve é uma instrução válida. Por isso a variável continuou com 6, e o pedido de 5 foi verificado com 6 e aceite. Se aparecer `IndentationError: unexpected indent`, vê [o problema com esse nome](#aparece-indentationerror-unexpected-indent).

3. Compara com a experiência do pedido de 0, no passo 2 da fase 2. A saída é a mesma, mas a causa não. Lá, a função recusou o pedido e devolveu 6, e a atribuição guardou o 6. Aqui, a função aceitou o pedido e devolveu 4, que ninguém guardou. Só pelo ecrã não sabes qual das duas aconteceu: é preciso ler o código ou fazer o traço.

4. Repõe a atribuição. Volta a escrever `quantidade_caderno =` e um espaço no início da linha, guarda e executa. O que deves ver: `Caderno 4` duas vezes.

### Paragem 3

O programa voltou a mostrar `Caderno 4` duas vezes.

Pensa antes de continuares: na linha `quantidade_caderno = retirar(quantidade_caderno, 2)`, que parte verifica o pedido e faz a conta, e que parte muda a quantidade guardada? A resposta: a chamada, `retirar(quantidade_caderno, 2)`, verifica e calcula. A atribuição, `quantidade_caderno =`, guarda o resultado na variável. Sem a atribuição, o pedido é verificado e a conta é feita, mas a quantidade fica igual.

## Fase 4: O problema das variáveis soltas

Acrescentas a pasta A02 ao programa, com uma variável trocada num pedido, e procuras o engano. Cada artigo passa a ocupar três variáveis soltas. Rever: [O problema das variáveis soltas](../01-entidades-estado-acoes.md#o-problema-das-variáveis-soltas).

1. Passa o programa para dois artigos, o caderno e a pasta. Muda a primeira linha do ficheiro para esta:

   ```python
   # inventario.py: o caderno e a pasta, cada um guardado em três variáveis soltas.
   ```

   Depois apaga tudo o que está a seguir à função `retirar`. No lugar, deixa duas linhas em branco e escreve:

   ```python
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

   O pedido da pasta tem um engano de propósito, que o comentário de cima descreve.

2. Antes de executares, prevê as duas linhas. Usa os valores que estão mesmo escritos na linha do pedido, e não o que o comentário diz que se queria. Depois guarda e executa. O que deves ver:

   ```text
   Caderno 6
   Pasta 5
   ```

   A pasta tinha 2 unidades, o pedido era de 1, e ficou com 5. A função recebeu 6 e 1, fez 6 - 1, e a atribuição guardou o 5 na variável da pasta. Se aparecer outra coisa, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

3. Encontra o engano. Está na linha a seguir ao comentário que começa por `# Queríamos retirar 1 pasta`. Que variável está errada nessa linha? A resposta: a `quantidade_caderno`, dentro dos parênteses. Devia lá estar a `quantidade_pasta`, porque o pedido é para a pasta.

4. Corrige o engano. Troca só essa variável, e a linha fica assim:

   ```python partial
   quantidade_pasta = retirar(quantidade_pasta, 1)
   ```

   Apaga também o comentário de cima, que deixou de ser verdade. Guarda e executa. O que deves ver:

   ```text
   Caderno 6
   Pasta 1
   ```

   Repara que, com o engano, o Python não mostrou nenhuma mensagem de erro. Sem o comentário, davas pelo engano comparando o ecrã com o que o programa devia mostrar. A pasta tinha 2 e o pedido era de 1, por isso devia aparecer `Pasta 1`.

### Paragem 4

O programa mostra `Caderno 6` e `Pasta 1`. O teu `inventario.py` deve estar assim:

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

A função é a da fase 1. Por baixo estão os dois artigos, cada um em três variáveis, o pedido corrigido e os dois `print`.

Pensa antes de terminares: porque é que o Python não deu pela variável trocada? A resposta: para o Python, `quantidade_caderno` e `quantidade_pasta` são só dois números com nomes diferentes. A ligação entre as três variáveis da pasta só existe na cabeça de quem escreveu o programa. E a função `retirar` só vê números: recebe dois e devolve um terceiro, sem saber de que artigo são. No tema seguinte, cada artigo passa a ser um objeto, que guarda os seus dados e faz as suas operações.

## Se alguma coisa falhar

1. Guardaste o ficheiro antes de executar? Alguns editores executam a última versão guardada, e não a que está no ecrã. Se o programa mostra o mesmo que antes, apesar de teres mudado o código, quase sempre é isto.
2. Estás a executar o ficheiro certo? Tem de ser o `inventario.py` da pasta `tema-01`.
3. Executaste o ficheiro inteiro, com o botão ou a tecla de executar, e não só uma linha selecionada? Cada execução começa do zero e repete todos os pedidos pela ordem em que estão escritos.
4. Desfizeste a última alteração feita de propósito? As fases 2 e 3 acabam por voltar ao programa da paragem 1. Se te perderes nas fases 1 a 3, copia o ficheiro da paragem 1 e refaz os passos da fase onde estás. Na fase 4, copia o mesmo ficheiro e refaz o passo 1.
5. Apareceu uma mensagem de erro? Lê primeiro a última linha, que diz o tipo de erro e a razão, e procura-a nos problemas desta secção.

### Aparece `NameError: name 'retirar' is not defined`

`NameError` quer dizer erro de nome: o nome `retirar` não está definido. A função falta no ficheiro, ou está escrita depois das linhas que a usam. Põe a função no início do ficheiro, antes de todas as chamadas. O mesmo vale para as funções que escreveres nos desafios.

### Aparece `NameError` com o nome de uma variável, como `quantidade_past`

O nome da variável está escrito de duas maneiras, por exemplo com uma letra a menos. Copia o nome da linha onde a variável recebeu o primeiro valor. Se o nome da mensagem é um texto, como `A02` ou `Caderno`, faltam as aspas à volta dele. Nas versões recentes do Python, a mensagem acaba com uma sugestão, como `Did you mean: 'quantidade_pasta'?` ("Querias dizer `quantidade_pasta`?").

### Aparece `TypeError: retirar() missing 1 required positional argument: 'unidades'`

`TypeError` quer dizer erro de tipo. A chamada tem só um valor dentro dos parênteses, e falta o das `unidades`. Escreve os dois valores, separados por uma vírgula: primeiro a quantidade, depois as unidades.

### Aparece `SyntaxError`

`SyntaxError` quer dizer erro de escrita: o Python não consegue ler uma linha. Com `expected ':'` ("esperava `:`"), falta o sinal de dois pontos no fim da linha do `def` ou do `if`. No Python 3.9, a mesma falta dá só `invalid syntax`, isto é, escrita inválida. Com outra mensagem, compara letra a letra a linha que a mensagem aponta, e a de cima, com a do laboratório. Pode faltar uma vírgula, um parêntese, uma aspa ou uma das três aspas da docstring, ou haver uma palavra mal escrita, como `retrun`.

### Aparece `IndentationError: expected an indented block`

Quer dizer "erro de indentação: esperava um bloco indentado". As linhas de dentro da função ou do `if` não estão mais afastadas da margem do que a linha do `def` ou do `if`. Compara a indentação, linha a linha, com a da função `retirar` da paragem 1.

### Aparece `IndentationError: unexpected indent`

Quer dizer "indentação inesperada". Uma linha fora da função começa com espaços, como acontece na fase 3 se fica o espaço que vinha a seguir ao `=`. Fora da função, as linhas começam junto à margem: apaga os espaços do início dessa linha.

### Aparece `None` no lugar de uma quantidade

Uma função que escreveste acaba sem `return` quando recusa o pedido, e uma função sem `return` devolve `None`, que em Python quer dizer "nada". Acrescenta a última linha, a que devolve a quantidade sem mudanças, como na função `retirar`.

### A quantidade não muda depois de um pedido, e não aparece nenhum erro

Falta a atribuição à esquerda da chamada, como na fase 3. Ou o nome à esquerda do `=` tem um engano, e o Python criou uma variável nova com esse nome. A linha do pedido tem de começar pelo nome exato da variável que queres mudar, seguido de `=`. Se a linha do pedido estiver certa, falta o `return` na linha a seguir ao `if` da função.

## Desafios

1. Um terceiro artigo. No ficheiro da paragem 4, acrescenta a borracha, com o código `A04`, o nome `Borracha` e 5 unidades. Guarda-a em três variáveis com nomes no padrão das do caderno e da pasta, a seguir às variáveis da pasta e separadas delas por uma linha em branco. No fim do ficheiro, acrescenta dois pedidos para retirar 3 borrachas, um a seguir ao outro. Escreve cada pedido como uma atribuição e põe a seguir a cada um uma linha que mostre o nome e a quantidade da borracha. Antes de executares, segue de cabeça o traço da borracha e prevê as duas linhas novas. Pista: o segundo pedido chega com a quantidade que o primeiro deixou.
2. A operação adicionar. Quando chega material, o inventário também precisa de adicionar unidades. Escreve a função `adicionar(quantidade, unidades)` a seguir à função `retirar`, com duas linhas em branco antes e depois. Se o pedido for aceite, devolve a quantidade mais as unidades; se for recusado, devolve a quantidade que recebeu, sem mudanças. Dá-lhe uma docstring, como a de `retirar`. Antes de escreveres, decide: das duas condições do `if` de `retirar`, `unidades > 0` e `unidades <= quantidade`, qual faz sentido num pedido para adicionar, e qual não faz? Depois, no fim do ficheiro, faz dois pedidos à borracha, adicionar 4 e, a seguir, adicionar 0, cada um seguido de uma linha que mostre o nome e a quantidade. Segue de cabeça o traço da borracha desde o início, com os quatro pedidos, e prevê as linhas que vão aparecer. No fim, o programa mostra seis linhas: duas do caderno e da pasta, e quatro da borracha. Pista: relê as duas condições de um pedido de retirada, no passo 1 da fase 1, palavra a palavra, e vê a que pedidos se aplica cada uma.

## Antes de terminares

- [ ] O `inventario.py` da pasta `tema-01` corre e mostra primeiro `Caderno 6` e `Pasta 1`, como na paragem 4.
- [ ] Guardaste o ficheiro e entregaste-o pelo meio que o professor indicar.
- [ ] Consegues explicar, por palavras tuas, porque é que o Python não deu pela variável trocada, e como se dá pelo engano sem o comentário.

![Rodapé](../../imagens/rodape.png)

![Cabeçalho](../imagens/cabecalho.png)

# Laboratório: Objetos, classes e instâncias

Laboratório do tema Objetos, classes e instâncias, do módulo M10, Introdução à Programação Orientada por Objetos. Vais criar e usar os primeiros objetos: escreves tu a classe `Artigo`, crias dois artigos e pedes-lhes operações. Cada passo diz o que fazer, porquê e o que deves ver, e avanças ao teu ritmo. O que não acabares na aula, acabas em casa ou na aula seguinte. Tudo o que precisas está aqui; o [guia do tema](02-objetos-classes-instancias.md) tem a teoria completa, para quem quiser saber mais.

## O que vais construir

No fim, tens um ficheiro `artigos.py` com a classe `Artigo` a funcionar, escrita por ti. O ficheiro tem os dois artigos da sala, o caderno e a pasta, e um método para lhes retirar unidades. Pelo caminho, vês com os teus próprios olhos três coisas. Vês quando é que o construtor trabalha e o que acontece a um objeto quando falta o `self.` numa linha do construtor. Vês também o que quer dizer dar dois nomes ao mesmo objeto.

| Fase | O que muda | O que funciona no fim |
| --- | --- | --- |
| 1 | Escreves a classe `Artigo` e crias dois artigos | O programa mostra os dados dos dois artigos |
| 2 | Uma linha provisória no construtor | Vês quantas vezes e quando o construtor trabalha |
| 3 | Mostras um objeto inteiro com `print` | Sabes o que o Python mostra de um objeto, e porquê |
| 4 | Tiras o `self.` de uma linha, de propósito | Sabes o que o `self.` guarda no objeto |
| 5 | Acrescentas o método `retirar` | O caderno perde duas unidades e a pasta fica igual |
| 6 | Dás um segundo nome ao caderno | Sabes distinguir um segundo nome de um objeto novo |

Em todas as fases trabalhas da mesma maneira. Antes de executares, escreves no papel o que esperas ver. Depois executas e comparas. Quando o resultado é diferente do que previste, explica a diferença antes de continuares: é essa explicação que mais te ensina.

Executa sempre o ficheiro inteiro. Cada execução começa do zero. O Python lê a classe, cria os artigos outra vez com os valores escritos no programa e repete todas as instruções, pela ordem em que estão. Em várias fases vais mudar o programa de propósito, para veres o que acontece. Faz a alteração pedida, observa, e desfaz a alteração antes de passares à fase seguinte.

## Palavras que vais usar

- Classe: a descrição comum de todos os objetos de um tipo, com os dados que têm e as operações que aceitam. Para saber mais, vê a secção "Classe: a descrição comum" do [guia](02-objetos-classes-instancias.md).
- Objeto, ou instância: um artigo concreto, criado a partir da classe, com os seus próprios valores. Para saber mais, vê "Classe e instância" no [guia](02-objetos-classes-instancias.md).
- Atributo: um dado guardado num objeto, com um nome e um valor, como `quantidade` e `6`.
- Construtor: o método `__init__`, que o Python executa sozinho sempre que se cria um objeto, para lhe dar os valores iniciais.
- `self`: dentro de um método, o nome do objeto sobre o qual o método está a trabalhar.
- Método: uma operação que pertence a um objeto e se escreve dentro da classe, como `retirar`.
- Parâmetro e argumento: o parâmetro é o nome que, dentro do método, espera um valor, como `unidades`. O argumento é o valor que chega na chamada, como o `2` de `caderno.retirar(2)`.
- Devolver: entregar um valor a quem chamou o método, com `return`. Não é o mesmo que mostrar no ecrã, que é o que o `print` faz.
- Mensagem de erro: o texto que o Python mostra quando para por causa de um erro. Quando o erro acontece com o programa a correr, a primeira linha é `Traceback (most recent call last)`, que quer dizer "o caminho até ao erro, com a chamada mais recente no fim". Num erro de escrita, como um `SyntaxError` ou um `IndentationError`, o Python nem começa a correr o programa. A mensagem abre logo com o ficheiro e o número da linha. Nos dois casos, a última linha diz o tipo de erro e o que aconteceu.
- `is`: a palavra que pergunta se dois nomes apontam para o mesmo objeto. Dá `True` (verdadeiro) ou `False` (falso).

## O que precisas

- O editor de Python que usas nas aulas, para escrever e executar os programas. Confirma que funciona: num ficheiro de ensaio, escreve `print("Olá")` e executa. Deve aparecer `Olá`, o que quer dizer que o editor está a executar programas de Python.
- O Python 3, a partir da versão 3.10. Nas versões mais antigas, algumas mensagens de erro são um pouco diferentes, e o laboratório diz onde.
- Papel e caneta, para as previsões, os traços e as respostas.

O laboratório começa de uma pasta vazia: não precisas de nenhum ficheiro do laboratório anterior.

## Se alguma coisa falhar

1. Guardaste o ficheiro antes de executar? O editor executa o que está guardado no disco. Guarda e executa outra vez.
2. Estás a executar o ficheiro certo? Confirma que o separador aberto é o `artigos.py` da pasta `tema-02`.
3. Apareceu uma mensagem de erro? Lê a última linha: diz o tipo de erro e o que aconteceu. Procura essa linha em [Problemas frequentes](#problemas-frequentes). Os erros de escrita são normais quando se escreve um programa pela primeira vez, e encontrá-los a partir da mensagem faz parte do trabalho.
4. Desfizeste a alteração da fase anterior? Cada fase parte do ficheiro como estava na paragem anterior. Se te perderes, copia o último ficheiro que o laboratório mostra completo: o da fase 1, o da paragem 5 ou o da paragem 6. A partir daí, refaz os passos que faltam.

## Preparar o projeto

1. Na pasta onde guardas os trabalhos de LP, cria uma pasta nova chamada `tema-02`. É aí que ficam os ficheiros deste laboratório.
2. Dentro dela, cria um ficheiro novo chamado `artigos.py`. O nome tem de acabar em `.py`, para o editor o reconhecer como um programa de Python, e não deve ter espaços nem acentos. Vais usar este ficheiro da fase 1 à fase 6, mudando o conteúdo de fase para fase.

## Fase 1: Uma classe e dois objetos

Na sala há dois artigos: A01, o caderno, com 6 unidades, e A02, a pasta, com 2. Cada artigo vai ser um objeto do Python, com os seus próprios valores. Os dois têm a mesma organização (código, nome e quantidade), e por isso escreve-se uma só descrição comum, a classe `Artigo`. Dentro da classe, o construtor `__init__` prepara cada artigo novo, guardando nele os três valores que recebe. Cada linha `Artigo(...)` cria um objeto a partir dessa descrição. Para saber mais, lê a secção "A classe Artigo em Python" do [guia](02-objetos-classes-instancias.md).

1. Escreve em `artigos.py` o programa seguinte. Desta vez não copies nem coles: escreve-o tu, letra a letra, porque ao escrever reparas em pormenores que uma cópia esconde. É o ficheiro completo:

   ```python
   # artigos.py: a classe Artigo e os artigos da sala, do laboratório do tema 02.

   class Artigo:
       """Descreve um artigo do inventário: um material com código, nome e quantidade."""

       def __init__(self, codigo, nome, quantidade):
           """Prepara um artigo acabado de criar, guardando os três dados recebidos."""
           self.codigo = codigo
           self.nome = nome
           self.quantidade = quantidade


   caderno = Artigo("A01", "Caderno", 6)
   pasta = Artigo("A02", "Pasta", 2)

   print(caderno.codigo, caderno.nome, caderno.quantidade)
   print(pasta.codigo, pasta.nome, pasta.quantidade)
   ```

   Repara nestes pormenores enquanto escreves:

   - os dois pontos no fim das linhas `class Artigo:` e `def __init__(self, codigo, nome, quantidade):`;
   - os dois sublinhados antes e os dois depois de `init`;
   - a indentação: quatro espaços dentro da classe e oito dentro do construtor;
   - as duas linhas em branco antes de `caderno = ...`.

   O comentário do topo e as docstrings, o texto entre três aspas, podem ficar como aqui ou com palavras tuas.

   Leitura guiada: a parte de cima, do `class` até às duas linhas em branco, é a descrição comum, e só é usada quando alguém cria um artigo. Lê depois as duas linhas `caderno = Artigo(...)` e `pasta = Artigo(...)`. Cada uma cria um objeto: o Python chama o construtor, com o `self` a ser o objeto novo e os três valores entre parênteses nos três parâmetros. Na linha `self.codigo = codigo`, o `codigo` da direita é o valor que chegou, e o `self.codigo` da esquerda é o atributo que fica guardado no objeto. Os dois `print` do fim consultam os atributos com o ponto: `caderno.nome` é o atributo `nome` do objeto `caderno`.

2. Antes de executares, escreve no papel as duas linhas que esperas ver.

3. Executa. O que deves ver:

   ```text
   A01 Caderno 6
   A02 Pasta 2
   ```

   Isto quer dizer que o Python criou dois objetos, cada um com os seus três atributos, e que os consultou pelo nome. Se em vez disso aparecer uma mensagem de erro, lê a última linha e procura-a em [Problemas frequentes](#problemas-frequentes).

### Paragem 1

O programa mostra os dados dos dois artigos, e o ficheiro tem a classe escrita por ti.

Pensa antes de continuares: escreveste três valores dentro de cada `Artigo(...)`, mas o construtor tem quatro parâmetros. Quem preenche o quarto? A resposta: o Python. O primeiro parâmetro, `self`, recebe o objeto novo, e é o próprio Python que o põe lá. Por isso, na chamada `Artigo(...)`, o `self` não se escreve.

## Fase 2: Quando é que o construtor trabalha

Para criar um artigo não escreves `__init__`: escreves `Artigo(...)`, e é o Python que chama o construtor, sozinho, sempre que uma linha `Artigo(...)` é executada. Vais tornar isso visível com uma linha provisória, que escreve uma mensagem no ecrã de cada vez que o construtor trabalha. Para saber mais, lê "O construtor `__init__`" no [guia](02-objetos-classes-instancias.md).

1. Em `artigos.py`, dentro do construtor, logo a seguir à docstring e antes de `self.codigo = codigo`, acrescenta esta linha. É uma alteração: a linha vai para dentro do construtor, com a mesma indentação das linhas que começam por `self.`:

   ```python partial
           print("A preparar o artigo", codigo)
   ```

   Leitura guiada: a linha mostra o texto e o valor do parâmetro `codigo`, que nesse momento é o código do artigo que está a ser criado. Como está dentro do construtor, só é executada quando o construtor é executado.

2. Antes de executares, responde no papel: quantas vezes vai aparecer a frase "A preparar o artigo"? Vai aparecer antes ou depois da linha `A01 Caderno 6`?

3. Executa. O que deves ver:

   ```text
   A preparar o artigo A01
   A preparar o artigo A02
   A01 Caderno 6
   A02 Pasta 2
   ```

   A resposta: a frase aparece duas vezes, uma por cada `Artigo(...)`. Aparece antes de `A01 Caderno 6`, porque as duas linhas que criam os artigos vêm antes dos `print`.

4. Agora muda só a ordem das linhas do fim do programa. Põe a linha `print(caderno.codigo, caderno.nome, caderno.quantidade)` logo a seguir a `caderno = Artigo("A01", "Caderno", 6)`, antes de `pasta = Artigo("A02", "Pasta", 2)`. As linhas do fim ficam assim:

   ```python partial
   caderno = Artigo("A01", "Caderno", 6)
   print(caderno.codigo, caderno.nome, caderno.quantidade)
   pasta = Artigo("A02", "Pasta", 2)

   print(pasta.codigo, pasta.nome, pasta.quantidade)
   ```

   Antes de executares, escreve no papel a ordem em que esperas ver as quatro linhas. Depois executa. O que deves ver:

   ```text
   A preparar o artigo A01
   A01 Caderno 6
   A preparar o artigo A02
   A02 Pasta 2
   ```

   Isto quer dizer que o construtor trabalha no momento em que a linha `Artigo(...)` é executada. Não trabalha no início do programa, nem quando o Python lê a classe.

5. Responde no papel: nunca escreveste `__init__` nas linhas do fim do programa. Que linhas fizeram o construtor trabalhar, e quantas vezes trabalhou? A resposta: as linhas `caderno = Artigo("A01", "Caderno", 6)` e `pasta = Artigo("A02", "Pasta", 2)`, uma vez cada. O construtor está definido uma vez, na classe, e foi chamado duas vezes.

6. Apaga a linha provisória do construtor e volta a pôr as linhas do fim pela ordem da fase 1. Executa para confirmares que voltas a ver só as duas linhas da fase 1. O construtor serve para preparar o objeto, e não para escrever no ecrã: a linha só lá esteve para veres quando é que ele trabalha.

### Paragem 2

O ficheiro está outra vez como no fim da fase 1, e o programa mostra `A01 Caderno 6` e `A02 Pasta 2`.

Pensa antes de continuares: se acrescentasses ao programa uma terceira linha, `regua = Artigo("A06", "Régua", 10)`, quantas vezes trabalharia o construtor? A resposta: três vezes, uma por cada `Artigo(...)`. O número de vezes que o construtor trabalha é o número de objetos criados.

## Fase 3: O que mostra um objeto inteiro

Até agora pediste ao Python cada atributo pelo nome, com o ponto. Nesta fase vês o que acontece quando pedes o objeto inteiro, sem dizer que atributo queres. Para saber mais, lê "Consultar atributos" no [guia](02-objetos-classes-instancias.md).

1. Acrescenta no fim do ficheiro esta linha:

   ```python partial
   print(caderno)
   ```

   Antes de executares, escreve no papel o que achas que vai aparecer.

2. Executa. Além das duas linhas de sempre, aparece uma terceira linha parecida com esta, com outro número no fim:

   ```text
   <__main__.Artigo object at 0x105535fd0>
   ```

   Esta linha diz três coisas:

   - que se trata de um objeto (em inglês, `object`) da classe `Artigo`;
   - que essa classe foi definida no programa que mandaste executar, que é o que quer dizer `__main__`;
   - onde é que o objeto está guardado na memória do computador, que é o número depois de `at`.

   Esse número começa por `0x` porque está escrito em base 16, a forma habitual de escrever posições de memória. Não precisas de o saber ler.

3. Executa outra vez e compara o número com o da primeira execução. Em geral muda, pelo menos em parte, porque cada execução começa do zero e o objeto pode ficar guardado noutro sítio.

4. Acrescenta no fim a linha `print(pasta)` e executa. Responde no papel: os números do caderno e da pasta são iguais ou diferentes? O que te diz isso sobre o número de objetos que o programa criou? A resposta: são diferentes. São dois objetos, guardados em dois sítios da memória. Vais precisar desta resposta na fase 6.

5. Responde também: para mostrar o nome do material, porque é que o programa escreve `print(caderno.nome)`, e não `print(caderno)`? A resposta: o Python não adivinha quais dos atributos queremos ver. Por isso, pede-se cada atributo pelo nome, com o ponto.

6. Apaga as linhas `print(caderno)` e `print(pasta)`.

### Paragem 3

O ficheiro está outra vez como no fim da fase 1. Sabes que o `print` de um objeto inteiro mostra a classe e o sítio da memória, e não os atributos.

Pensa antes de continuares: se executares o programa amanhã, o número de memória do caderno vai ser o mesmo de hoje? A resposta: provavelmente não. O número diz onde o objeto ficou guardado nesta execução, e cada execução começa do zero.

## Fase 4: O `self.` decide o que fica no objeto

Na linha `self.nome = nome`, há duas coisas com o nome `nome`. Do lado direito, `nome` é o parâmetro: o valor que chegou na chamada, que só existe enquanto o construtor está a ser executado. Do lado esquerdo, `self.nome` é o atributo do objeto, que fica guardado depois de o construtor terminar. Nesta fase vais tirar o `self.` de propósito, para veres o que acontece ao objeto. Para saber mais, lê "O parâmetro `self`" no [guia](02-objetos-classes-instancias.md).

1. No construtor, na linha `self.nome = nome`, apaga `self.`, de modo que a linha fique `nome = nome`. Não mexas em mais nada.

2. Antes de executares, responde no papel: o Python vai queixar-se da linha `nome = nome`? O que vai acontecer quando o programa pedir `caderno.nome`?

3. Executa. O programa para sem mostrar nenhuma das duas linhas, e mostra uma mensagem de erro parecida com esta:

   ```text
   Traceback (most recent call last):
     File ".../tema-02/artigos.py", line 16, in <module>
       print(caderno.codigo, caderno.nome, caderno.quantidade)
                             ^^^^^^^^^^^^
   AttributeError: 'Artigo' object has no attribute 'nome'
   ```

   O caminho do ficheiro, no lugar dos três pontos, é o do teu computador. A linha com os sinais `^` aponta para a parte da instrução onde o erro aconteceu; nas versões do Python anteriores à 3.11, não aparece. A última linha quer dizer: o objeto do tipo `Artigo` não tem nenhum atributo chamado `nome`. Um `AttributeError` ("erro de atributo") é o erro que aparece quando se pede a um objeto um atributo que ele não tem.

4. Responde no papel: em que linha do ficheiro aparece o erro? Em que linha está a causa? Porque é que o Python não se queixou da linha `nome = nome`, e o que é que essa linha fez, afinal?

   A resposta: o erro aparece na linha 16, a do primeiro `print`, se escreveste o programa exatamente como está na fase 1. A causa está no construtor, na linha `nome = nome`, que é a linha 9. O Python não se queixou porque `nome = nome` é uma atribuição válida. Guarda o valor do parâmetro `nome` no próprio nome `nome`, que é uma variável do construtor e desaparece quando o construtor termina. Nada foi guardado no objeto, que nasceu com `codigo` e `quantidade`, mas sem `nome`. O erro só aparece quando alguém pede ao objeto o atributo que ele não tem, várias linhas depois da causa.

5. Para confirmares que só falta o nome, muda provisoriamente os dois `print` do fim para mostrarem só o código e a quantidade:

   ```python partial
   print(caderno.codigo, caderno.quantidade)
   print(pasta.codigo, pasta.quantidade)
   ```

   Executa. O que deves ver:

   ```text
   A01 6
   A02 2
   ```

   Isto quer dizer que os dois objetos foram criados e têm os outros dois atributos. Só lhes falta aquele em que tiraste o `self.`.

6. Volta a pôr `self.nome = nome` no construtor e os dois `print` como estavam. Executa para confirmares que aparecem outra vez as duas linhas da fase 1.

### Paragem 4

O ficheiro está outra vez como no fim da fase 1, e o programa mostra `A01 Caderno 6` e `A02 Pasta 2`.

Pensa antes de continuares: o Python mostrou o erro na linha 16, mas o engano estava na linha 9. O que te ensina isto sobre a forma de procurar a causa de um erro? A resposta: a linha que a mensagem aponta é onde o erro se viu, e não sempre onde nasceu. A mensagem é uma pista: daí, sobe no programa até à instrução que devia ter guardado o atributo.

## Fase 5: Um método, retirar

Um método é uma operação que pertence a um objeto, como retirar unidades. Escreve-se dentro da classe, como o construtor, e também tem o `self` como primeiro parâmetro. Na chamada `caderno.retirar(2)`, o objeto que está antes do ponto, o `caderno`, é o que vai ocupar o `self`. O `2` é o argumento, que ocupa o parâmetro `unidades`. O método muda a quantidade do artigo e devolve, com `return`, a quantidade que fica. Para saber mais, lê "O método retirar em Python" no [guia](02-objetos-classes-instancias.md).

1. Em `artigos.py`, acrescenta à classe o método `retirar`, a seguir ao construtor, com uma linha em branco entre os dois. A linha `def retirar(self, unidades):` fica com a mesma indentação de `def __init__`, e as linhas de dentro do método ficam com mais quatro espaços. É uma alteração; o método é este:

   ```python partial
       def retirar(self, unidades):
           """Retira unidades a este artigo e devolve a quantidade que fica.

           Esta primeira versão ainda não verifica se o pedido é possível.
           Neste laboratório só fazemos pedidos que sabemos serem válidos.
           """
           self.quantidade = self.quantidade - unidades
           return self.quantidade
   ```

   Leitura guiada: a linha `self.quantidade = self.quantidade - unidades` lê-se da direita para a esquerda. O Python consulta a quantidade deste artigo, tira-lhe as unidades pedidas e guarda o resultado no mesmo atributo. Depois, o `return` entrega a quantidade que ficou a quem chamou o método.

2. Substitui as linhas que vêm depois da classe, a partir de `caderno = ...`, por estas:

   ```python partial
   caderno = Artigo("A01", "Caderno", 6)
   pasta = Artigo("A02", "Pasta", 2)

   print("Antes:", caderno.quantidade, pasta.quantidade)
   restante = caderno.retirar(2)
   print("Depois:", caderno.quantidade, pasta.quantidade)
   print("Devolvido:", restante)
   ```

   Leitura guiada: o primeiro `print` mostra as duas quantidades antes do pedido. A linha `restante = caderno.retirar(2)` pede ao caderno que retire duas unidades e guarda, na variável `restante`, o valor que o método devolve. Os dois últimos `print` mostram as quantidades depois do pedido e o valor devolvido.

3. Escreve no papel as três linhas que esperas ver. Depois executa. O que deves ver:

   ```text
   Antes: 6 2
   Depois: 4 2
   Devolvido: 4
   ```

   Isto quer dizer que o pedido chegou só ao caderno, que passou de 6 para 4, e que o método devolveu o 4 que ficou.

4. Agora uma experiência sobre o `self`. A chamada `caderno.retirar(2)` dá exatamente o mesmo que `Artigo.retirar(caderno, 2)`: "executa o método `retirar` da classe `Artigo`, com `self` igual a `caderno` e `unidades` igual a 2". Nesta forma longa, o objeto que ocupa o `self` vai em primeiro lugar entre parênteses. Vais confirmá-lo. Na linha `restante = caderno.retirar(2)`, troca `caderno.retirar(2)` por `Artigo.retirar(caderno, 2)`. Prevê as três linhas e executa.

   A resposta: a saída não muda. Continuas a ver `Antes: 6 2`, `Depois: 4 2` e `Devolvido: 4`, porque as duas formas pedem exatamente a mesma coisa.

5. Troca agora `Artigo.retirar(caderno, 2)` por `Artigo.retirar(pasta, 2)`. Antes de executares, responde no papel: qual dos dois artigos vai ficar com menos unidades? Qual dos dois objetos vai ser o `self` dentro do método? Executa. O que deves ver:

   ```text
   Antes: 6 2
   Depois: 6 0
   Devolvido: 0
   ```

   A resposta: fica com menos unidades a pasta, que passa de 2 para 0. O `self` dentro do método é a pasta, porque é o primeiro valor entre parênteses. Ficar com zero unidades é um estado válido, e não há nada de errado nesta chamada.

6. Responde numa frase: na forma curta, `caderno.retirar(2)`, onde está escrito o objeto que vai ocupar o `self`? A resposta: antes do ponto.

7. Volta a pôr `restante = caderno.retirar(2)` e executa, para confirmares a saída do passo 3. A forma longa serviu só para veres que dá exatamente o mesmo que a curta, com o objeto do `self` escrito em primeiro lugar. Nas duas formas, o método é o mesmo e trabalha sobre um objeto; só muda a maneira de o chamar. Nos programas escreve-se sempre a forma curta, que é a que toda a gente espera ler.

### Paragem 5

O programa mostra `Antes: 6 2`, `Depois: 4 2` e `Devolvido: 4`. O ficheiro `artigos.py` completo, como deve estar agora:

```python
# artigos.py: a classe Artigo e os artigos da sala, do laboratório do tema 02.

class Artigo:
    """Descreve um artigo do inventário: um material com código, nome e quantidade."""

    def __init__(self, codigo, nome, quantidade):
        """Prepara um artigo acabado de criar, guardando os três dados recebidos."""
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade

    def retirar(self, unidades):
        """Retira unidades a este artigo e devolve a quantidade que fica.

        Esta primeira versão ainda não verifica se o pedido é possível.
        Neste laboratório só fazemos pedidos que sabemos serem válidos.
        """
        self.quantidade = self.quantidade - unidades
        return self.quantidade


caderno = Artigo("A01", "Caderno", 6)
pasta = Artigo("A02", "Pasta", 2)

print("Antes:", caderno.quantidade, pasta.quantidade)
restante = caderno.retirar(2)
print("Depois:", caderno.quantidade, pasta.quantidade)
print("Devolvido:", restante)
```

Pensa antes de continuares: se apagasses a palavra `restante =` e deixasses só `caderno.retirar(2)`, com que quantidade ficava o caderno? A resposta: ficava com 4 na mesma. A alteração do atributo acontece dentro do método. O que se perdia era só o valor devolvido. A linha `print("Devolvido:", restante)` deixava de funcionar: o programa parava aí com `NameError: name 'restante' is not defined` ("o nome `restante` não está definido"), porque a variável `restante` já não existia.

## Fase 6: Dois nomes para o mesmo objeto

Uma variável não contém o objeto: é um nome que aponta para ele, como uma etiqueta colada numa caixa. A linha `mesmo_caderno = caderno` não tem `Artigo(...)`, e por isso não cria nenhum artigo. Cola uma segunda etiqueta na caixa do caderno. A palavra `is` pergunta se dois nomes apontam para o mesmo objeto. Para saber mais, lê "Cada instância é um objeto diferente" no [guia](02-objetos-classes-instancias.md).

1. Substitui as linhas que vêm depois da classe por estas. A classe fica igual, com o construtor e o `retirar`:

   ```python partial
   caderno = Artigo("A01", "Caderno", 6)
   pasta = Artigo("A02", "Pasta", 2)
   mesmo_caderno = caderno

   mesmo_caderno.retirar(1)

   print("Caderno:", caderno.quantidade)
   print("Pasta:", pasta.quantidade)
   print(caderno is mesmo_caderno)
   print(caderno is pasta)
   ```

   Leitura guiada: das três primeiras linhas, só duas têm `Artigo(...)`. A terceira dá um segundo nome a um objeto que já existe. O pedido `mesmo_caderno.retirar(1)` vai para o objeto para onde esse nome aponta. Os dois primeiros `print` mostram as quantidades, e os dois últimos perguntam, com `is`, se dois nomes apontam para o mesmo objeto.

2. Escreve no papel as quatro linhas que esperas ver e executa. O que deves ver:

   ```text
   Caderno: 5
   Pasta: 2
   True
   False
   ```

   Isto quer dizer que a unidade retirada através de `mesmo_caderno` saiu do caderno, porque os dois nomes apontam para o mesmo objeto. `caderno is mesmo_caderno` dá `True`, e `caderno is pasta` dá `False`.

3. Agora troca a linha `mesmo_caderno = caderno` por esta:

   ```python partial
   mesmo_caderno = Artigo("A01", "Caderno", 6)
   ```

   E acrescenta no fim do ficheiro esta linha:

   ```python partial
   print("Mesmo caderno:", mesmo_caderno.quantidade)
   ```

4. Antes de executares, responde no papel: quantos objetos do tipo `Artigo` existem agora? A qual deles vai ser retirada a unidade? O que vai mostrar `caderno is mesmo_caderno`? Executa. O que deves ver:

   ```text
   Caderno: 6
   Pasta: 2
   False
   False
   Mesmo caderno: 5
   ```

   A resposta: passam a existir três objetos, porque há três chamadas a `Artigo(...)`. A unidade é retirada ao objeto novo, o que tem o nome `mesmo_caderno`, e por isso o caderno fica com 6. `caderno is mesmo_caderno` dá `False`, porque os dois nomes apontam para objetos diferentes.

5. Responde no papel: os objetos a que chamámos `caderno` e `mesmo_caderno` começaram com exatamente os mesmos valores. Porque é que `caderno is mesmo_caderno` dá agora `False`? Relaciona a tua resposta com o que viste na fase 3, quando o caderno e a pasta apareceram com números de memória diferentes.

   A resposta: `is` pergunta se os dois nomes apontam para o mesmo objeto, e não se os objetos têm os mesmos valores. São duas caixas diferentes, com o mesmo conteúdo escrito lá dentro, criadas por duas chamadas a `Artigo(...)`. Na fase 3, o caderno e a pasta tinham números de memória diferentes pela mesma razão: cada `Artigo(...)` cria um objeto novo, num sítio seu.

6. Repara também que o programa passou a ter dois artigos com o código A01. O Python aceitou-o sem se queixar. Mas a primeira regra do inventário, na secção "Uma operação tem de respeitar regras" do guia 01, diz que cada código identifica um único artigo. O Python não conhece as regras do nosso inventário: faz o que o programa lhe pede, e quem escreve o programa é que tem de as respeitar.

7. Volta a pôr `mesmo_caderno = caderno`, apaga a última linha que acrescentaste e executa, para confirmares a saída do passo 2.

### Paragem 6

O programa mostra `Caderno: 5`, `Pasta: 2`, `True` e `False`. O ficheiro `artigos.py` completo, como deve estar no fim do laboratório:

```python
# artigos.py: a classe Artigo e os artigos da sala, do laboratório do tema 02.

class Artigo:
    """Descreve um artigo do inventário: um material com código, nome e quantidade."""

    def __init__(self, codigo, nome, quantidade):
        """Prepara um artigo acabado de criar, guardando os três dados recebidos."""
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade

    def retirar(self, unidades):
        """Retira unidades a este artigo e devolve a quantidade que fica.

        Esta primeira versão ainda não verifica se o pedido é possível.
        Neste laboratório só fazemos pedidos que sabemos serem válidos.
        """
        self.quantidade = self.quantidade - unidades
        return self.quantidade


caderno = Artigo("A01", "Caderno", 6)
pasta = Artigo("A02", "Pasta", 2)
mesmo_caderno = caderno

mesmo_caderno.retirar(1)

print("Caderno:", caderno.quantidade)
print("Pasta:", pasta.quantidade)
print(caderno is mesmo_caderno)
print(caderno is pasta)
```

Pensa antes de continuares: se, a seguir a `mesmo_caderno.retirar(1)`, escrevesses `caderno.retirar(1)`, com que quantidade ficava o caderno? A resposta: com 4. Os dois pedidos chegam ao mesmo objeto, um através de cada nome, e cada um tira uma unidade.

## Problemas frequentes

### `SyntaxError: expected ':'`

Em português: erro de sintaxe, esperava-se `:`. Nas versões do Python anteriores à 3.10, a mensagem é só `SyntaxError: invalid syntax`. Faltam os dois pontos no fim de uma linha `class` ou `def`. Acrescenta `:` no fim da linha que a mensagem mostra.

### `IndentationError`

Em português: erro de indentação. Com `expected an indented block` ("esperava-se um bloco indentado"), há um `class` ou um `def` cujo bloco ficou sem indentação: as linhas de dentro, incluindo a docstring, ficaram com a mesma indentação dele. A partir do Python 3.10, a última linha acaba em `on line` e um número, que é a linha desse `class` ou `def`. Com `unexpected indent` ("indentação inesperada"), uma linha tem espaços a mais. Dentro da classe, o `def` leva quatro espaços; dentro de um método, todas as linhas levam oito, incluindo a docstring. Compara com o último ficheiro completo, linha a linha.

### `NameError: name 'codigo' is not defined`

As três linhas que começam por `self.` ficaram com quatro espaços, a mesma indentação do `def`, e só a docstring ficou dentro do construtor. Essas linhas deixaram de pertencer ao método, e fora dele o parâmetro `codigo` não existe. Põe as três linhas com oito espaços, como a docstring.

### `TypeError: Artigo() takes no arguments`

Em português: `Artigo()` não aceita argumentos. Um `TypeError` ("erro de tipo") é o erro que o Python dá quando uma operação recebe valores que não aceita. O nome do construtor está mal escrito, por exemplo `_init_`, com um só sublinhado de cada lado, ou `__innit__`, com um `n` a mais. O Python não o reconhece como construtor, e a classe fica sem nenhum construtor que aceite valores. O nome escreve-se `__init__`: dois sublinhados, a palavra `init` e mais dois sublinhados.

### `TypeError: Artigo.retirar() takes 1 positional argument but 2 were given`

Nas versões do Python anteriores à 3.10, a mensagem começa por `retirar()`, sem `Artigo.`. Em português: o método `retirar` aceita 1 argumento posicional, mas recebeu 2. Compara a linha do `def retirar` com a do ficheiro da paragem 5.

### `NameError: name 'artigo' is not defined`

As versões recentes do Python acrescentam `Did you mean: 'Artigo'?`, isto é, "querias dizer `Artigo`?". A classe foi escrita com maiúscula e a chamada com minúscula, ou ao contrário. Escreve o nome da classe sempre da mesma maneira: `Artigo`, com maiúscula.

### `AttributeError: 'Artigo' object has no attribute 'quantidade'`

As versões recentes do Python podem acrescentar uma sugestão, como `Did you mean: 'quantiade'?`. O construtor guardou o atributo com outro nome, por um erro de escrita como `self.quantiade`, ou sem o `self.` à frente. Confirma que o nome depois de `self.` é exatamente o mesmo que usas no resto do programa.

### `AttributeError: 'Artigo' object has no attribute 'retirar'`

O método ficou fora da classe, com o `def` encostado à margem. O Python aceita-o como uma função solta, e os objetos `Artigo` não o têm. Põe o `def` com quatro espaços e as linhas de dentro com oito.

## Desafios

1. Escrever a classe de cor. Fecha o guia e o ficheiro `artigos.py`. Na pasta `tema-02`, cria um ficheiro novo chamado `memoria.py`. Sem olhar para nada, escreve a classe `Artigo`, com o construtor e o método `retirar`. Por baixo, escreve as linhas para criar um artigo à tua escolha, retirar-lhe unidades e mostrar a quantidade que fica. Executa e, se aparecer um erro, corrige-o a partir da última linha da mensagem. Só depois abre o `artigos.py` e compara, linha a linha. Escreve no papel todas as diferenças, mesmo as pequenas, e separa as que faziam o programa falhar das que não faziam diferença. Pista: um sublinhado a menos, dois pontos esquecidos e um `self.` que ficou por escrever são diferenças pequenas que mudam muito.

2. Uma classe para outra coisa da escola. Cada sala da escola tem um projetor, e a lâmpada de um projetor tem de ser trocada ao fim de um certo número de horas de uso. Para saber quando, a escola quer registar, para cada projetor, um código, a sala onde está e as horas de uso que já acumulou. Num ficheiro `projetor.py`, escreve:

   - uma classe `Projetor`, com um construtor que guarde o código, a sala e as horas de uso em três atributos: `codigo`, `sala` e `horas_uso`. A sala guarda-se como texto, por exemplo `"Sala 12"`;
   - um método `usar`, com um parâmetro `horas`, que acrescente as horas recebidas às horas de uso e devolva o total que fica. Ainda não precisa de verificar se o pedido é válido;
   - as docstrings da classe, do construtor e do método.

   Depois da classe, cria dois projetores: o P01, na Sala 12, com 150 horas de uso, e o P02, na Sala 7, acabado de comprar, com 0 horas. Usa o P01 durante 3 horas, depois o P02 durante 2 horas e depois o P01 durante 1 hora, e guarda numa variável o valor devolvido pela última chamada. No fim, mostra numa só linha as horas de uso dos dois projetores e o valor que guardaste. Antes de executares, faz o traço no papel, com uma linha por chamada, e escreve a linha que esperas ver. No fim, responde: porque é que aqui faz sentido uma classe nova, e não a classe `Artigo`? Pista: compara os dados e as operações de um projetor com os de um artigo.

## Antes de terminares

- [ ] O ficheiro `artigos.py` executa e mostra `Caderno: 5`, `Pasta: 2`, `True` e `False`.
- [ ] Desfizeste todas as alterações provisórias: o ficheiro está igual ao da paragem 6.
- [ ] Tens no papel as previsões e as respostas de cada fase.
- [ ] Guardaste o `artigos.py`, a folha e, se fizeste os desafios, o `memoria.py` e o `projetor.py`, e entregaste-os pelo meio indicado pelo professor.
- [ ] Sabes dizer quando é que o construtor trabalha, e quem é o `self` em `caderno.retirar(2)`.
- [ ] Sabes dizer porque é que `mesmo_caderno = caderno` não cria um artigo novo.
- [ ] Consegues explicar, por palavras tuas, a diferença entre a classe `Artigo` e os objetos `caderno` e `pasta`.

![Rodapé](../imagens/rodape.png)

![Cabeçalho](../imagens/cabecalho.png)

# Laboratório: Composição e modelação

Laboratório do tema Composição e modelação, do módulo M10, Introdução à Programação Orientada por Objetos. Vais construir o inventário em Python: uma classe `Inventario` que cria os artigos, os guarda e lhes passa os pedidos. Cada passo diz o que fazer, porquê e o que deves ver, e avanças ao teu ritmo. O que não acabares na aula, acabas em casa ou na aula seguinte. Tudo o que precisas está aqui; o [guia do tema](04-composicao-modelacao.md) tem a teoria completa, para quem quiser saber mais.

## O que vais construir

No fim, tens um ficheiro `inventario.py` com duas classes a funcionar: a classe `Artigo`, que já conheces do tema 03, e a classe `Inventario`, escrita por ti. O inventário garante uma regra que nenhum artigo consegue garantir sozinho: não há dois artigos com o mesmo código. Pelo caminho, provocas de propósito uma recusa que atravessa vários métodos e lês o caminho que ela fez.

Antes de escrever código, descreve-se por palavras o que vais construir. Em cada classe, diz-se o que cada objeto guarda e o que se lhe pode pedir; no fim, diz-se como as duas classes se ligam. É o modelo do programa:

- A classe `Artigo`. Cada artigo guarda um código, um nome e uma quantidade, que é sempre um número inteiro não negativo. Um artigo cria-se com esses três valores. A um artigo pode pedir-se que adicione unidades, com `adicionar(unidades)`, e que retire unidades, com `retirar(unidades)`.
- A classe `Inventario`. Cada inventário guarda os seus artigos, e nunca dois com o mesmo código. Um inventário cria-se vazio. A um inventário pode pedir-se que registe um artigo novo, com `registar(codigo, nome, quantidade)`; que diga a quantidade de um artigo, com `quantidade_de(codigo)`; e que retire unidades de um artigo, com `retirar(codigo, unidades)`.
- A relação entre as duas. Um inventário tem artigos, e é o próprio inventário que cria os seus artigos e os guarda. Cada artigo pertence a um só inventário e não faz sentido sem ele. Esta relação chama-se **composição**.

Entre parênteses estão os valores que cada pedido recebe, os parâmetros do método. O `self` não se escreve, porque todos os métodos o têm. A descrição também não fala do sítio onde o inventário guarda os artigos: isso decide-se no código, na fase 1.

| Fase | O que muda | O que funciona no fim |
| --- | --- | --- |
| 1 | Escreves a classe `Inventario` com o construtor | Um inventário vazio, com a sua lista de artigos |
| 2 | Acrescentas os métodos `_procurar` e `registar` | O inventário cria artigos, encontra-os pelo código e recusa um código repetido |
| 3 | Acrescentas os métodos `quantidade_de` e `retirar` | O programa completo responde a oito pedidos, e confere com o traço |
| 4 | Fazes um pedido impossível fora de um `try` | Lês, no ecrã, o caminho que a recusa fez até parar o programa |

Em todas as fases trabalhas da mesma maneira. Antes de executares o programa, escreves no papel o que esperas ver. Depois executas e comparas. Quando o resultado é diferente do que previste, explica a diferença antes de continuares: é essa explicação que mais te ensina. Escrever primeiro obriga-te a pensar; executar primeiro só te mostra o que o Python fez.

Executa sempre o ficheiro inteiro. Cada execução começa do zero: cria um inventário novo e repete todos os pedidos, pela ordem em que estão escritos.

## Palavras que vais usar

- Inventário: o objeto que reúne os artigos de uma sala e responde às perguntas sobre o conjunto, como "já existe um artigo com o código A01?". Para saber mais, vê a secção "Artigos soltos: o que nenhum artigo consegue garantir" do [guia](04-composicao-modelacao.md).
- Modelo: a descrição, por palavras, das classes de um programa, do que cada uma guarda e faz, e das relações entre elas. Escreve-se antes do código. Para saber mais, vê "O inventário descrito por palavras" no [guia](04-composicao-modelacao.md).
- Composição: a relação em que o todo cria as suas partes e as guarda, e as partes não fazem sentido sem ele. Aqui, o inventário cria os artigos. Para saber mais, vê "Dois graus de "tem": composição e agregação" no [guia](04-composicao-modelacao.md).
- Lista: um valor que guarda vários valores por ordem, escrito entre parênteses retos; `[]` é uma lista vazia. `len(lista)` (do inglês *length*, "comprimento") dá o número de elementos. `lista.append(valor)` (*append*, "acrescentar") junta um elemento no fim.
- Ciclo `for`: repete o bloco indentado por baixo dele uma vez por cada elemento de uma lista. `for artigo in artigos:` lê-se "para cada artigo na lista artigos".
- Atributo interno e método interno: um nome com um sublinhado no início, como `_artigos` ou `_procurar`. Avisa que só a própria classe o deve usar.
- Propriedade, getter e setter: a `quantidade` de um artigo lê-se e escreve-se como um atributo. Cada leitura passa por um método, o getter (do inglês *get*, obter). Cada escrita passa por outro, o setter (de *set*, pôr), que recusa os valores inválidos. Vem do tema 03.
- Exceção: um sinal de que alguma coisa correu mal, que interrompe o funcionamento normal do programa. `raise` lança uma exceção. `ValueError` ("erro de valor") é a exceção que usamos para recusar um valor ou um pedido. `try` e `except` apanham-na, para o programa continuar. Vem do tema 03.
- Encaminhamento: o inventário recebe um pedido, encontra o artigo que sabe cumpri-lo e passa-lho, sem verificar nada sobre as unidades.
- Traço: a tabela que regista, passo a passo, o que acontece em cada instrução ou em cada pedido, e como fica o estado depois dele. Faz-se no papel, antes de executar, para comparar com o que o programa mostra.
- Cadeia de chamadas: os métodos que estão parados, cada um à espera do seguinte, desde o programa principal até ao sítio onde o Python está a trabalhar.
- Mensagem de erro: o texto que o Python mostra quando para por causa de um erro. Quando o erro acontece com o programa a correr, a primeira linha é `Traceback (most recent call last)`, que quer dizer "o rasto, com a chamada mais recente no fim". Num erro de escrita, como um `SyntaxError` ("erro de sintaxe") ou um `IndentationError` ("erro de indentação"), o Python nem começa a correr o programa. Nos dois casos, a última linha diz o tipo de erro e o que aconteceu.

## O que precisas

- O editor de Python que usas nas aulas, para escrever e executar os programas. Confirma que funciona: num ficheiro de ensaio, escreve `print("Olá")` e executa. Deve aparecer `Olá`, o que quer dizer que o editor está a executar programas de Python.
- O Python 3, a partir da versão 3.10. Nas versões mais antigas, algumas mensagens de erro são um pouco diferentes, e o laboratório diz onde.
- Papel e caneta, para as previsões, o traço e as respostas.

O laboratório começa de uma pasta vazia. Não precisas de nenhum ficheiro do laboratório anterior: a classe `Artigo` do tema 03 está toda aqui.

## Se alguma coisa falhar

1. Guardaste o ficheiro antes de executar? O editor executa o que está guardado no disco. Guarda e executa outra vez.
2. Estás a executar o ficheiro certo? Confirma que o separador aberto é o `inventario.py` da pasta `tema-04`.
3. Apareceu uma mensagem de erro? Lê a última linha: diz o tipo de erro e o que aconteceu. Procura essa linha em [Problemas frequentes](#problemas-frequentes).
4. Apagaste as linhas de teste da fase anterior? Cada fase diz que linhas apagar no fim. Se te perderes nas fases 1 ou 2, recomeça o ficheiro com a classe `Artigo` de "Preparar o projeto" e refaz as fases desde a 1. Se te perderes na fase 3 ou na 4, copia o ficheiro completo da [paragem 3](#paragem-3): é o ponto de partida da fase 4.

## Preparar o projeto

1. Na pasta onde guardas os trabalhos de LP, cria uma pasta nova chamada `tema-04`. É aí que fica o ficheiro deste laboratório.
2. Dentro dela, cria um ficheiro novo chamado `inventario.py`. O nome tem de acabar em `.py`, para o editor o reconhecer como um programa de Python, e não deve ter espaços nem acentos.
3. Copia para `inventario.py` o conteúdo seguinte. É a classe `Artigo` do fim do tema 03, com as docstrings mais curtas; as instruções são as mesmas. É o ficheiro completo, por agora:

   ```python
   # inventario.py: as classes Artigo e Inventario, do laboratório do tema 04.

   class Artigo:
       """Artigo do inventário: código, nome e uma quantidade sempre válida.

       É a classe final do guia 03, com as docstrings encurtadas.
       """

       def __init__(self, codigo, nome, quantidade):
           """Cria o artigo. A quantidade inicial passa pelo setter."""
           self.codigo = codigo
           self.nome = nome
           self.quantidade = quantidade

       @property
       def quantidade(self):
           """Getter: devolve a quantidade atual, sem a alterar."""
           return self._quantidade

       @quantidade.setter
       def quantidade(self, valor):
           """Setter: guarda o valor se for um inteiro não negativo; senão, lança ValueError."""
           if not isinstance(valor, int):
               raise ValueError("A quantidade tem de ser um número inteiro.")
           if valor < 0:
               raise ValueError("A quantidade não pode ser negativa.")
           self._quantidade = valor

       def adicionar(self, unidades):
           """Acrescenta unidades (inteiro, 1 ou mais); senão, lança ValueError."""
           if not isinstance(unidades, int):
               raise ValueError("As unidades a adicionar têm de ser um número inteiro.")
           if unidades <= 0:
               raise ValueError("As unidades a adicionar têm de ser 1 ou mais.")
           self.quantidade = self.quantidade + unidades

       def retirar(self, unidades):
           """Retira unidades (inteiro, 1 ou mais, até ao que existe); senão, lança ValueError."""
           if not isinstance(unidades, int):
               raise ValueError("As unidades a retirar têm de ser um número inteiro.")
           if unidades <= 0:
               raise ValueError("As unidades a retirar têm de ser 1 ou mais.")
           # A falta de unidades é recusada pelo setter: o resultado seria negativo.
           self.quantidade = self.quantidade - unidades
   ```

   Leitura guiada: a quantidade é uma propriedade. O `@property` faz do primeiro `def quantidade` o getter, que devolve o valor guardado em `_quantidade`. O `@quantidade.setter` faz do segundo o setter, que verifica o valor antes de o guardar. O construtor e os métodos `adicionar` e `retirar` escrevem na propriedade, e por isso todas as escritas passam pelo setter. Os dois métodos verificam primeiro o pedido: as unidades têm de ser um inteiro (`isinstance(unidades, int)` pergunta isso) e têm de ser 1 ou mais. Quando faltam unidades numa retirada, quem recusa é o setter, porque o resultado seria negativo.

4. Guarda e executa o ficheiro. O que deves ver: nada. O ficheiro só define uma classe, e definir uma classe não mostra nada no ecrã, tal como escrever uma receita não faz nenhum bolo. Se aparecer uma mensagem de erro, lê a última linha. Um `IndentationError` quer dizer que alguma linha ficou com a indentação errada na cópia: compara-a com o bloco acima. Um `SyntaxError` quer dizer, quase sempre, que ficou uma linha cortada a meio.

## Fase 1: Uma lista para guardar os artigos

Um artigo conhece os seus próprios dados, e só esses. Para saber se um código já está a ser usado, ou para encontrar o artigo com o código A02, é preciso conhecer todos os artigos. É por isso que precisamos de um objeto novo, o inventário, que os guarda todos. Vai guardá-los numa lista, que nasce vazia no construtor. Cada inventário tem a sua própria lista, porque o construtor é executado uma vez por cada inventário criado, e cada execução cria uma lista nova. O nome da lista começa por sublinhado, `_artigos`, porque é um assunto interno da classe. Se o código de fora juntasse artigos à lista diretamente, saltava a verificação do código único, que vais escrever na fase 2. Para saber mais, lê o passo 2 do exemplo guiado do [guia](04-composicao-modelacao.md).

1. Depois da classe `Artigo`, deixa duas linhas em branco e acrescenta a classe `Inventario`, só com o construtor. Escreve-a à mão, em vez de a copiares: escrever obriga-te a reparar em cada pormenor, como o sublinhado de `_artigos` e os dois pontos no fim de cada `def`.

   ```python partial
   class Inventario:
       """Inventário que cria, guarda e controla os seus artigos."""

       def __init__(self):
           """Cria um inventário vazio, ainda sem artigos."""
           self._artigos = []
   ```

   Leitura guiada: o construtor só tem o parâmetro `self`. Por isso, um inventário cria-se com `Inventario()`, sem argumentos. A única tarefa do construtor é dar ao inventário novo uma lista vazia, `[]`, guardada no atributo `_artigos`.

2. No fim do ficheiro, encostadas à margem, acrescenta estas duas linhas:

   ```python partial
   inventario = Inventario()
   print(inventario._artigos)
   ```

3. Antes de executares, escreve no papel o que esperas ver. Depois executa. O que deves ver:

   ```text
   []
   ```

   É a lista vazia que o construtor criou. Isto quer dizer que o inventário existe e tem a sua lista. Estamos a espreitar a lista interna só para confirmar que o construtor funciona, enquanto construímos a classe. Na fase 2 voltas a espreitá-la, pela mesma razão. No programa final, o código de fora não mexe na lista: quem quer registar um artigo pede ao inventário.

4. Apaga a linha do `print`. Mantém a linha `inventario = Inventario()`.

### Paragem 1

O ficheiro tem as duas classes, e o programa cria um inventário vazio sem mostrar nada.

Pensa antes de continuares: se criasses dois inventários, `a = Inventario()` e `b = Inventario()`, e juntasses um artigo à lista de `a`, a lista de `b` mudava? A resposta: não. O construtor é executado uma vez para `a` e outra vez para `b`, e cada execução cria uma lista nova. Cada inventário tem a sua.

## Fase 2: O inventário cria os artigos e encontra-os pelo código

O inventário vai fazer duas coisas que só ele pode fazer, porque é o único que conhece todos os artigos.

A primeira é encontrar um artigo a partir do código. Quase todos os pedidos ao inventário começam por aí, e por isso a procura fica num método próprio, `_procurar`. O sublinhado no nome diz que é um método interno: serve os outros métodos do inventário, e o código de fora não o usa.

A segunda é registar um artigo novo, com o método `registar`. É aqui que está a composição: é o inventário, dentro de um método seu, que cria o artigo, com `Artigo(...)`. Antes de o criar, verifica que o código ainda não está a ser usado. Primeiro verifica, só depois altera. Para saber mais, lê os passos 3 e 4 do exemplo guiado do [guia](04-composicao-modelacao.md).

1. Dentro da classe `Inventario`, a seguir ao construtor e com a mesma indentação dele, escreve o método `_procurar`:

   ```python partial
       def _procurar(self, codigo):
           """Método interno: devolve o artigo com este código.

           Falha: lança ValueError se não houver nenhum artigo com este código.
           """
           for artigo in self._artigos:
               if artigo.codigo == codigo:
                   return artigo
           raise ValueError("Não existe nenhum artigo com o código " + codigo + ".")
   ```

   Leitura guiada: o ciclo percorre a lista, um artigo de cada vez, e compara o código de cada um com o código procurado. O `return`, dentro do ciclo, termina o método assim que encontra o artigo certo: as voltas que faltavam já não se fazem. O `raise` está depois do ciclo, encostado à indentação do `for`. Só se chega a ele se o ciclo acabar todas as voltas sem nenhum `return`, isto é, se nenhum artigo tiver o código procurado. A mensagem junta textos com `+`: com o código `"A07"`, fica "Não existe nenhum artigo com o código A07.".

2. A seguir a `_procurar`, com a mesma indentação, escreve o método `registar`:

   ```python partial
       def registar(self, codigo, nome, quantidade):
           """Cria um artigo novo e guarda-o no inventário.

           Recebe: o código, o nome e a quantidade inicial do artigo.
           Devolve: nada (None).
           Falha: lança ValueError se já existir um artigo com este código, ou
           se a quantidade inicial for inválida (quem a recusa é o setter do
           artigo). Em qualquer falha, o inventário fica como estava.
           """
           for artigo in self._artigos:
               if artigo.codigo == codigo:
                   raise ValueError("Já existe um artigo com o código " + codigo + ".")
           novo = Artigo(codigo, nome, quantidade)
           self._artigos.append(novo)
   ```

   Leitura guiada: o método faz três coisas, por esta ordem. Primeiro percorre os artigos e, se algum já tiver o código pedido, lança `ValueError`. É o mesmo ciclo de `_procurar`, mas com a decisão ao contrário: aqui, encontrar o código é a falha. Depois cria o artigo, com `Artigo(codigo, nome, quantidade)`. A quantidade não é verificada aqui: quem a verifica é o setter do artigo, chamado pelo construtor dele. Por fim, e só por fim, junta o artigo à lista com `append`. Se alguma coisa falhar antes, a linha do `append` nunca chega a ser executada, e a lista fica como estava.

3. No fim do ficheiro, a seguir a `inventario = Inventario()`, acrescenta:

   ```python partial
   inventario.registar("A01", "Caderno", 6)
   inventario.registar("A02", "Pasta", 2)
   print(len(inventario._artigos))
   print(inventario._procurar("A02").nome)
   ```

4. Prevê as duas linhas que vão aparecer. Depois executa. O que deves ver:

   ```text
   2
   Pasta
   ```

   A primeira linha diz que a lista tem dois artigos, os dois que o inventário criou. A segunda lê-se da esquerda para a direita: `_procurar("A02")` devolve o artigo com esse código, e `.nome` consulta o nome desse artigo. Mais uma vez, estamos a usar de fora duas coisas internas, a lista e o método `_procurar`, só para testar a construção. Vais apagar estas linhas no fim desta fase.

5. Agora vais ver o inventário recusar um código repetido. Acrescenta no fim do ficheiro, fora de qualquer `try`:

   ```python partial
   inventario.registar("A01", "Cola", 3)
   ```

6. Executa. Depois das duas linhas de antes, o programa para com uma mensagem de erro. A última linha deve ser esta:

   ```text
   ValueError: Já existe um artigo com o código A01.
   ```

   Lê também, logo acima, a linha que diz em que método o erro foi lançado. Começa por `File`, com o caminho do teu ficheiro e o número da linha, e deve terminar em `in registar`. A linha de código mostrada por baixo dela é a do `raise` do método `registar`. Isto quer dizer que foi o inventário que recusou, porque é ele que conhece todos os códigos.

7. Apaga as três linhas de teste desta fase: o `print(len(...))`, o `print(inventario._procurar(...).nome)` e o registo da cola. Mantém a criação do inventário e os dois primeiros registos.

### Paragem 2

O inventário regista o caderno e a pasta sem mostrar nada, e já recusou um código repetido.

Pensa antes de continuares: se registasses `inventario.registar("A03", "Caneta", -5)`, quem recusava, e a caneta ficava na lista? A resposta: recusava o setter do artigo, com "A quantidade não pode ser negativa.". O `registar` chama `Artigo(...)`, o construtor do artigo escreve na propriedade, e o setter recusa o -5. O `registar` é interrompido nessa linha, antes do `append`, e a lista continua com dois artigos.

## Fase 3: O inventário passa os pedidos aos artigos

Falta consultar e retirar unidades a partir do código. Os dois métodos começam da mesma maneira: encontrar o artigo com `_procurar`. Depois fazem o pedido a esse artigo. O inventário não verifica se as unidades são um inteiro, se são positivas nem se chegam: essas regras são do artigo, que já as verifica. Chama-se **encaminhamento** a esta forma de colaborar: o inventário encontra o artigo que sabe cumprir o pedido e passa-lho.

Repara numa forma nova. Para um método do inventário usar outro método do mesmo inventário, escreve `self._procurar(codigo)`. Dentro de um método, o `self` é o próprio objeto, aqui o inventário. Assim como de fora se escreve `inventario.registar(...)`, de dentro escreve-se `self._procurar(...)`. Para saber mais, lê o passo 5 do exemplo guiado do [guia](04-composicao-modelacao.md).

1. Dentro da classe `Inventario`, a seguir ao método `registar` e com a mesma indentação, escreve os métodos `quantidade_de` e `retirar`:

   ```python partial
       def quantidade_de(self, codigo):
           """Devolve a quantidade do artigo com este código, sem a alterar.

           Falha: lança ValueError se não houver nenhum artigo com este código.
           """
           artigo = self._procurar(codigo)
           return artigo.quantidade

       def retirar(self, codigo, unidades):
           """Encaminha um pedido de retirada para o artigo com este código.

           Recebe: o código do artigo e as unidades a retirar.
           Devolve: nada (None).
           Falha: lança ValueError se não houver nenhum artigo com este código,
           ou se o próprio artigo recusar o pedido, pelas regras do seu método
           retirar. Em qualquer falha, nenhuma quantidade muda.
           """
           artigo = self._procurar(codigo)
           artigo.retirar(unidades)
   ```

   Leitura guiada: cada método tem duas linhas. A primeira encontra o artigo: se o código não existir, `_procurar` lança `ValueError`, e o método para logo ali. A segunda faz o pedido ao artigo encontrado. `quantidade_de` lê a propriedade e devolve o valor. `retirar` chama o `retirar` do artigo, com as mesmas unidades. Há agora dois métodos chamados `retirar`, de classes diferentes. `inventario.retirar("A01", 2)` recebe um código e um número. `artigo.retirar(2)` recebe só um número, porque o artigo já sabe quem é. O objeto antes do ponto diz de que classe é o método.

2. Substitui todas as linhas que estão depois das duas classes, a partir de `inventario = Inventario()`, por estas:

   ```python partial
   inventario = Inventario()
   inventario.registar("A01", "Caderno", 6)
   inventario.registar("A02", "Pasta", 2)

   try:
       inventario.registar("A01", "Cola", 3)
   except ValueError as erro:
       print("Registo de A01 recusado:", erro)

   try:
       inventario.registar("A03", "Caneta", -5)
   except ValueError as erro:
       print("Registo de A03 recusado:", erro)

   try:
       print(inventario.quantidade_de("A03"))
   except ValueError as erro:
       print("Consulta de A03 recusada:", erro)

   inventario.retirar("A01", 2)
   print("A01 depois de retirar 2:", inventario.quantidade_de("A01"))

   try:
       inventario.retirar("A01", 9)
   except ValueError as erro:
       print("Retirar 9 de A01 recusado:", erro)

   try:
       inventario.retirar("A07", 1)
   except ValueError as erro:
       print("Retirar de A07 recusado:", erro)

   print("A01 no fim:", inventario.quantidade_de("A01"))
   print("A02 no fim:", inventario.quantidade_de("A02"))
   ```

   Leitura guiada: são os oito pedidos do traço e, pelo meio e no fim, três consultas que mostram as quantidades. Os pedidos que podem ser recusados estão dentro de um `try`, e o `except` mostra a mensagem de quem recusou. O programa principal nunca escreve `Artigo(...)` nem guarda um artigo num nome seu: fala sempre com o inventário, usando os códigos.

3. Antes de executares, faz o traço dos oito pedidos no papel. Cada linha começa no estado deixado pela anterior. As quatro primeiras linhas estão feitas; copia a tabela e completa as que têm um ponto de interrogação.

   | Pedido | Quem responde | Resposta | Artigos no inventário depois |
   | --- | --- | --- | --- |
   | `registar("A01", "Caderno", 6)` | Inventário: código livre; setter do artigo: 6 é válido | Aceite | A01 com 6 |
   | `registar("A02", "Pasta", 2)` | Inventário e setter do artigo | Aceite | A01 com 6, A02 com 2 |
   | `registar("A01", "Cola", 3)` | Inventário: A01 já existe | `ValueError`, antes de criar o artigo | A01 com 6, A02 com 2 |
   | `registar("A03", "Caneta", -5)` | Inventário: código livre; setter do artigo: -5 é negativo | `ValueError`, ao criar o artigo, antes do `append` | A01 com 6, A02 com 2 |
   | `quantidade_de("A03")` | ? | ? | ? |
   | `retirar("A01", 2)` | ? | ? | ? |
   | `retirar("A01", 9)` | ? | ? | ? |
   | `retirar("A07", 1)` | ? | ? | ? |

   A resposta, para as quatro linhas que faltavam:

   | Pedido | Quem responde | Resposta | Artigos no inventário depois |
   | --- | --- | --- | --- |
   | `quantidade_de("A03")` | `_procurar` do inventário: A03 não existe | `ValueError` | A01 com 6, A02 com 2 |
   | `retirar("A01", 2)` | Inventário encontra A01; o artigo aceita | Aceite | A01 com 4, A02 com 2 |
   | `retirar("A01", 9)` | Inventário encontra A01; setter do artigo: 4 - 9 = -5 | `ValueError` | A01 com 4, A02 com 2 |
   | `retirar("A07", 1)` | `_procurar` do inventário: A07 não existe | `ValueError` | A01 com 4, A02 com 2 |

   A consulta de A03 falha, e isso prova que o registo recusado da caneta não deixou nada para trás: o artigo nunca chegou à lista.

4. A partir do traço, escreve no papel as linhas que o programa vai mostrar. Os pedidos aceites não mostram nada; só as recusas e as consultas escrevem uma linha. Depois executa. O que deves ver:

   ```text
   Registo de A01 recusado: Já existe um artigo com o código A01.
   Registo de A03 recusado: A quantidade não pode ser negativa.
   Consulta de A03 recusada: Não existe nenhum artigo com o código A03.
   A01 depois de retirar 2: 4
   Retirar 9 de A01 recusado: A quantidade não pode ser negativa.
   Retirar de A07 recusado: Não existe nenhum artigo com o código A07.
   A01 no fim: 4
   A02 no fim: 2
   ```

   Cada mensagem diz quem recusou. "Já existe um artigo..." e "Não existe nenhum artigo..." vêm do inventário, e "A quantidade não pode ser negativa." vem do setter do artigo. As duas últimas linhas confirmam que, depois de cinco pedidos recusados, as quantidades são as do traço.

5. Se alguma linha for diferente, procura a primeira que é diferente e não olhes para as outras por agora. Uma diferença cedo no programa costuma provocar as seguintes. Depois pergunta-te que método produziu essa linha, e relê esse método, comparando-o com o ficheiro da paragem 3. Os enganos mais comuns estão em [Problemas frequentes](#problemas-frequentes). São estes: um `raise` dentro do `for`; uma linha de um método que ficou fora da classe; e um nome escrito de duas maneiras, como `_artigos` e `_artigo`.

### Paragem 3

O programa mostra as oito linhas do passo 4, e o traço que fizeste confere com elas.

O ficheiro `inventario.py` completo, como deve estar agora:

```python
# inventario.py: as classes Artigo e Inventario, do laboratório do tema 04.

class Artigo:
    """Artigo do inventário: código, nome e uma quantidade sempre válida.

    É a classe final do guia 03, com as docstrings encurtadas.
    """

    def __init__(self, codigo, nome, quantidade):
        """Cria o artigo. A quantidade inicial passa pelo setter."""
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade

    @property
    def quantidade(self):
        """Getter: devolve a quantidade atual, sem a alterar."""
        return self._quantidade

    @quantidade.setter
    def quantidade(self, valor):
        """Setter: guarda o valor se for um inteiro não negativo; senão, lança ValueError."""
        if not isinstance(valor, int):
            raise ValueError("A quantidade tem de ser um número inteiro.")
        if valor < 0:
            raise ValueError("A quantidade não pode ser negativa.")
        self._quantidade = valor

    def adicionar(self, unidades):
        """Acrescenta unidades (inteiro, 1 ou mais); senão, lança ValueError."""
        if not isinstance(unidades, int):
            raise ValueError("As unidades a adicionar têm de ser um número inteiro.")
        if unidades <= 0:
            raise ValueError("As unidades a adicionar têm de ser 1 ou mais.")
        self.quantidade = self.quantidade + unidades

    def retirar(self, unidades):
        """Retira unidades (inteiro, 1 ou mais, até ao que existe); senão, lança ValueError."""
        if not isinstance(unidades, int):
            raise ValueError("As unidades a retirar têm de ser um número inteiro.")
        if unidades <= 0:
            raise ValueError("As unidades a retirar têm de ser 1 ou mais.")
        # A falta de unidades é recusada pelo setter: o resultado seria negativo.
        self.quantidade = self.quantidade - unidades


class Inventario:
    """Inventário que cria, guarda e controla os seus artigos."""

    def __init__(self):
        """Cria um inventário vazio, ainda sem artigos."""
        self._artigos = []

    def _procurar(self, codigo):
        """Método interno: devolve o artigo com este código.

        Falha: lança ValueError se não houver nenhum artigo com este código.
        """
        for artigo in self._artigos:
            if artigo.codigo == codigo:
                return artigo
        raise ValueError("Não existe nenhum artigo com o código " + codigo + ".")

    def registar(self, codigo, nome, quantidade):
        """Cria um artigo novo e guarda-o no inventário.

        Recebe: o código, o nome e a quantidade inicial do artigo.
        Devolve: nada (None).
        Falha: lança ValueError se já existir um artigo com este código, ou
        se a quantidade inicial for inválida (quem a recusa é o setter do
        artigo). Em qualquer falha, o inventário fica como estava.
        """
        for artigo in self._artigos:
            if artigo.codigo == codigo:
                raise ValueError("Já existe um artigo com o código " + codigo + ".")
        novo = Artigo(codigo, nome, quantidade)
        self._artigos.append(novo)

    def quantidade_de(self, codigo):
        """Devolve a quantidade do artigo com este código, sem a alterar.

        Falha: lança ValueError se não houver nenhum artigo com este código.
        """
        artigo = self._procurar(codigo)
        return artigo.quantidade

    def retirar(self, codigo, unidades):
        """Encaminha um pedido de retirada para o artigo com este código.

        Recebe: o código do artigo e as unidades a retirar.
        Devolve: nada (None).
        Falha: lança ValueError se não houver nenhum artigo com este código,
        ou se o próprio artigo recusar o pedido, pelas regras do seu método
        retirar. Em qualquer falha, nenhuma quantidade muda.
        """
        artigo = self._procurar(codigo)
        artigo.retirar(unidades)


inventario = Inventario()
inventario.registar("A01", "Caderno", 6)
inventario.registar("A02", "Pasta", 2)

try:
    inventario.registar("A01", "Cola", 3)
except ValueError as erro:
    print("Registo de A01 recusado:", erro)

try:
    inventario.registar("A03", "Caneta", -5)
except ValueError as erro:
    print("Registo de A03 recusado:", erro)

try:
    print(inventario.quantidade_de("A03"))
except ValueError as erro:
    print("Consulta de A03 recusada:", erro)

inventario.retirar("A01", 2)
print("A01 depois de retirar 2:", inventario.quantidade_de("A01"))

try:
    inventario.retirar("A01", 9)
except ValueError as erro:
    print("Retirar 9 de A01 recusado:", erro)

try:
    inventario.retirar("A07", 1)
except ValueError as erro:
    print("Retirar de A07 recusado:", erro)

print("A01 no fim:", inventario.quantidade_de("A01"))
print("A02 no fim:", inventario.quantidade_de("A02"))
```

Pensa antes de continuares: na classe `Inventario`, onde está a verificação de que as unidades a retirar são 1 ou mais? A resposta: em lado nenhum. Essa regra é do artigo, e está no `retirar` da classe `Artigo`. O inventário só encontra o artigo e encaminha o pedido. Se a regra mudar, muda-se num só sítio.

## Fase 4: O caminho de uma recusa

Quando um método chama outro, fica parado à espera dele. Se o segundo chamar um terceiro, ficam dois à espera, e assim por diante: é a cadeia de chamadas. Quando um método lança uma exceção com `raise`, ela sobe por essa cadeia, do método onde nasceu para o que o chamou. Continua a subir até encontrar um `try` com o `except` certo. Cada método que ela atravessa sem um `try` que a apanhe é abandonado no ponto onde estava. Na fase 3, o pedido para retirar 9 unidades de A01 estava dentro de um `try`, e a exceção foi apanhada no programa principal. Agora vais vê-la subir até ao fim, sem que ninguém a apanhe: o programa para, e o Python mostra o caminho que ela fez. Para saber mais, lê o passo 8 do exemplo guiado do [guia](04-composicao-modelacao.md).

1. No fim do ficheiro, depois de todas as outras linhas e fora de qualquer `try`, acrescenta:

   ```python partial
   inventario.retirar("A01", 9)
   ```

2. Antes de executares, escreve no papel a lista dos métodos por onde achas que o pedido passa até ao erro, do primeiro ao último.

3. Executa. As oito linhas do programa aparecem, como antes, e no fim aparece um traceback.

   O traceback tem quatro entradas. Cada entrada tem uma linha que começa por `File`, com o caminho do teu ficheiro, o número da linha e o nome do sítio onde o Python estava. Por baixo vem o código dessa linha. Os caminhos e os números das linhas dependem do teu ficheiro. Algumas versões do Python acrescentam, por baixo do código, uma linha com sinais `^` ou `~` a apontar para a parte da linha que falhou. O que interessa são os nomes no fim de cada linha `File` e o código que aparece por baixo:

   | Entrada | Termina em | Código mostrado por baixo |
   | --- | --- | --- |
   | Primeira | `in <module>` | `inventario.retirar("A01", 9)` |
   | Segunda | `in retirar` | `artigo.retirar(unidades)` |
   | Terceira | `in retirar` | `self.quantidade = self.quantidade - unidades` |
   | Quarta | `in quantidade` | `raise ValueError("A quantidade não pode ser negativa.")` |

   A última linha de todas é `ValueError: A quantidade não pode ser negativa.`.

4. Responde no papel, a olhar para o teu traceback. Cada pergunta tem a resposta logo a seguir; escreve a tua antes de a leres.

   1. `<module>` (do inglês, "módulo") é o nome que o Python dá ao programa principal, o código que está encostado à margem. Porque é que esta é a primeira entrada?

      A resposta: é onde a cadeia começa. Foi a linha `inventario.retirar("A01", 9)` do programa principal que chamou o primeiro método. O traceback escreve a cadeia de cima para baixo, do primeiro método chamado até ao sítio onde a exceção nasceu.

   2. Há duas entradas que terminam em `in retirar`. Qual delas é o `retirar` do inventário, e qual é o do artigo? Decide pelo código mostrado por baixo de cada uma, e não pela ordem.

      A resposta: a segunda entrada, com `artigo.retirar(unidades)`, é o `retirar` do inventário, porque é essa a linha do inventário que chama o artigo. A terceira, com `self.quantidade = self.quantidade - unidades`, é o `retirar` do artigo. Os dois métodos têm o mesmo nome, e por isso o que decide é o código mostrado.

   3. A quarta entrada termina em `in quantidade`. Que método da classe `Artigo` é este? Porque é que o nome não é `retirar`?

      A resposta: é o setter da propriedade `quantidade`. O Python mostra o nome do método onde estava, e o setter é um método chamado `quantidade`, o segundo `def quantidade` da classe. Não aparece `retirar` porque a exceção não foi lançada no `retirar`: foi lançada no setter, que o `retirar` chamou ao escrever na propriedade.

   4. Compara a tua lista do passo 2 com as quatro entradas. Acertaste na ordem?

      A resposta: o pedido passa pelo programa principal, pelo `retirar` do inventário, por `_procurar`, pelo `retirar` do artigo e pelo setter. Se puseste `_procurar` na tua lista, acertaste no caminho do pedido. Mas o traceback só mostra quatro entradas, e a pergunta seguinte explica porquê.

   5. Este pedido também chamou o método `_procurar`. Aparece no traceback? Porquê?

      A resposta: não aparece, porque já tinha terminado quando a exceção foi lançada. Encontrou o artigo, devolveu-o com o `return` e saiu. O traceback só mostra as chamadas que ainda estavam a meio, paradas à espera de outra. É essa a cadeia por onde a exceção sobe.

   O traceback é a cadeia de chamadas, escrita pelo Python: de cima para baixo, do programa principal até ao sítio onde a exceção nasceu. É por isso que se lê de baixo para cima quando se procura a causa: a última entrada é onde o erro começou.

5. Apaga a linha que acrescentaste nesta fase e executa outra vez. Deves ver as oito linhas da paragem 3, sem nenhum traceback.

### Paragem 4

O ficheiro está outra vez igual ao da paragem 3, e já leste no ecrã o caminho de uma recusa.

Pensa antes de continuares: porque é que o `retirar` do inventário não tem um `try` para apanhar a recusa do artigo? A resposta: quem lança a exceção decide se o pedido é válido, e quem a apanha decide o que fazer com a recusa. O inventário não sabe o que fazer com ela: não sabe se o programa escreve num terminal, mostra uma página ou regista o pedido num ficheiro. Por isso deixa-a passar, e o programa principal decide mostrar a mensagem. Se o inventário a apanhasse e não fizesse nada, a recusa perdia-se, e quem fez o pedido ficava convencido de que ele tinha sido cumprido.

## Problemas frequentes

### `NameError: name 'Artigo' is not defined`

Em português: o nome `Artigo` não está definido. Um `NameError` ("erro de nome") aparece quando se usa um nome que o Python não conhece. A classe `Artigo` não está no ficheiro, ou ficou com outro nome. Confirma que copiaste a classe em "Preparar o projeto" e que o nome começa por maiúscula.

### `NameError: name '_procurar' is not defined`

Dentro de um método do inventário, a chamada ficou escrita `_procurar(codigo)`, sem o `self.` à frente. O Python procura uma função solta com esse nome, e não a encontra. Escreve `self._procurar(codigo)`: dentro da classe, os métodos do próprio objeto alcançam-se através do `self`. As versões recentes do Python acrescentam à mensagem `Did you mean: 'self._procurar'?`, isto é, "querias dizer `self._procurar`?".

### `AttributeError: 'Inventario' object has no attribute '_artigos'`

Em português: o objeto `Inventario` não tem o atributo `_artigos`. Um `AttributeError` ("erro de atributo") aparece quando se pede a um objeto um atributo que ele não tem. O nome da lista está escrito de maneiras diferentes no construtor e noutro método. Procura todas as linhas com `_artigo` e usa o mesmo nome em todas. As versões recentes do Python acrescentam uma sugestão, como `Did you mean: '_artigo'?`.

### `AttributeError: 'Inventario' object has no attribute 'registar'`

O método ficou fora da classe, com o `def` encostado à margem. O Python aceita-o como uma função solta, e o inventário não o tem. As versões recentes do Python podem sugerir outro nome, como `Did you mean: 'retirar'?`; aqui, a sugestão não ajuda, porque o método existe, mas fora da classe. Indenta todas as linhas do método quatro espaços, para ficarem dentro da classe: o `def` com quatro espaços e as linhas de dentro com oito.

### `TypeError: can only concatenate str (not "int") to str`

Em português: só se pode juntar texto a texto, e não um número inteiro. Um `TypeError` ("erro de tipo") aparece quando uma operação recebe um valor de um tipo que não aceita; `str` é o texto e `int` o número inteiro. Foi passado um número como código, por exemplo `quantidade_de(7)`. Nenhum artigo tem esse código, e a mensagem do `raise` não conseguiu juntar o texto ao número. Como não é um `ValueError`, o `except ValueError` não o apanha. Neste inventário, os códigos são textos, entre aspas: `quantidade_de("A07")`.

### `ValueError: Não existe nenhum artigo com o código A02.`

A pasta foi registada, mas a procura não a encontra, e o programa para na última linha. O `raise` de `_procurar` ficou com a indentação do `if`, dentro do ciclo. Na primeira volta, se o primeiro artigo não for o procurado, o método lança logo a exceção, sem olhar para os outros. Põe o `raise` encostado à indentação do `for`, depois do ciclo, como no ficheiro da paragem 3.

### `IndentationError: expected an indented block after 'if' statement on line`

Em português: esperava-se um bloco indentado a seguir à instrução `if` da linha indicada. Nas versões anteriores ao Python 3.10, a mensagem é só `IndentationError: expected an indented block`. O programa nem chega a correr, e não aparece nenhuma linha da saída. O `return` de `_procurar` ficou com a indentação do próprio `if`, e o `if` ficou sem nenhuma instrução por baixo. O `return` tem de ficar quatro espaços mais à direita do que o `if`.

### O programa mostra menos linhas do que devia

Um `return` ou um `raise` com a indentação errada terminou um método antes do tempo. Compara a indentação de cada linha do método com o ficheiro da paragem 3.

## Desafios

1. Adicionar unidades a um artigo. Escreve, dentro da classe `Inventario`, o método `adicionar(codigo, unidades)`, com este contrato. Recebe o código de um artigo e as unidades a adicionar. Não devolve nada. Falha, com `ValueError`, se não houver nenhum artigo com esse código, ou se o próprio artigo recusar o pedido pelas regras do seu método `adicionar`. Em qualquer falha, nenhuma quantidade muda. Escreve-lhe uma docstring.

   Antes de escreveres o método, responde no papel: que regras sobre as unidades vai verificar o método do inventário, e quais vai deixar ao artigo?

   Depois escolhe tu os testes. Escreve três pedidos de adição, cada um no seu `try`, depois das linhas que já estão no fim do ficheiro. Um tem de ser aceite, outro recusado pelo inventário, e o terceiro recusado pelo artigo. Para cada pedido, escreve antes de executar se vai ser aceite ou recusado, quem recusa, com que mensagem e como ficam as quantidades. No fim, mostra com `quantidade_de` a quantidade de cada artigo existente que usaste nos testes.

   Pista: para escolheres os testes, pensa em que regras verifica cada objeto e por que ordem o pedido passa por eles.

2. O total de unidades do inventário. Escreve o método `total_unidades()`, que devolve a soma das quantidades de todos os artigos do inventário. Não recebe nada além do `self`, não muda nenhuma quantidade e não falha.

   Antes de escreveres, decide e escreve no papel duas coisas. Porque é que este método pertence ao `Inventario`, e não ao `Artigo`? E o que deve devolver um inventário que ainda não tem nenhum artigo?

   Para somar, usa um acumulador: uma variável preparada antes de um ciclo `for` sobre a lista interna, que em cada volta junta a quantidade de um artigo. Testa com dois casos. Mostra o total do inventário do teu programa, e depois cria um inventário novo, vazio, e mostra o total dele. Antes de executares, calcula à mão o total do primeiro, a partir das quantidades que os artigos têm nesse momento.

   Pista: pensa bem no valor com que o acumulador deve começar, e em que sítio do método ficam a linha que o prepara e o `return`.

3. Os artigos esgotados. Escreve o método `esgotados()`, que devolve uma lista com os códigos dos artigos que têm quantidade 0. Se nenhum artigo estiver esgotado, devolve uma lista vazia. Testa-o duas vezes: uma com o inventário tal como está, e outra depois de retirares todas as unidades de um dos artigos. Antes de cada teste, escreve a lista que esperas ver.

4. A descrição com as operações novas. No papel, escreve de novo a descrição da classe `Inventario` de "O que vais construir", agora com os métodos que acrescentaste nos desafios. Depois responde numa frase: a descrição da relação entre as duas classes mudou com as operações novas? Porquê?

## Antes de terminares

- [ ] O ficheiro `inventario.py` executa e mostra as oito linhas da paragem 3.
- [ ] Apagaste as linhas de teste das fases 1, 2 e 4: o ficheiro está igual ao da paragem 3, mais o que fizeste nos desafios.
- [ ] Tens no papel as previsões, o traço da fase 3 e as respostas da fase 4.
- [ ] Guardaste o `inventario.py` e a folha e, se fizeste o desafio 4, a descrição, e entregaste-os pelo meio indicado pelo professor.
- [ ] Sabes dizer quem recusa cada um dos pedidos da fase 3, e porquê.
- [ ] Sabes dizer porque é que `_procurar` não aparece no traceback da fase 4.
- [ ] Consegues explicar, por palavras tuas, porque é que é o inventário, e não o artigo, que garante que não há dois artigos com o mesmo código.

![Rodapé](../imagens/rodape.png)

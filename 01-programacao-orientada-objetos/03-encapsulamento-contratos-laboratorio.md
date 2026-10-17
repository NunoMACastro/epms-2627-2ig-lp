![Cabeçalho](../imagens/cabecalho.png)

# Laboratório: Encapsulamento e contratos

Laboratório do tema Encapsulamento e contratos, do módulo M10, Introdução à Programação Orientada por Objetos. Vais proteger a quantidade de um artigo: começas com uma classe que aceita quantidades impossíveis e acabas com uma classe que as recusa. Cada passo diz o que fazer, porquê e o que deves ver, e avanças ao teu ritmo. O que não acabares na aula, acabas em casa ou na aula seguinte. Tudo o que precisas está aqui; o [guia do tema](03-encapsulamento-contratos.md) tem a teoria completa, para quem quiser saber mais.

## O que vais construir

No fim, tens um ficheiro `artigo.py` com a classe `Artigo` final do tema. A quantidade é uma propriedade, que recusa valores inválidos, e os métodos `adicionar` e `retirar` verificam cada pedido antes de mexer na quantidade. Quando um pedido é recusado, a quantidade fica exatamente como estava.

Pelo caminho, provocas de propósito os erros de que mais vais precisar de reconhecer, e aprendes a ler a mensagem que o Python mostra em cada um.

| Fase | O que muda | O que funciona no fim |
| --- | --- | --- |
| 1 | O programa de partida: a classe do tema 02 e três alterações impossíveis | Vês um estado inválido aceite sem queixa, e o erro que ele provoca mais tarde |
| 2 | Métodos get e set, com um set que recusa com `print` | Vês o que o set resolve e os dois problemas que deixa por resolver |
| 3 | O atributo `_quantidade` e o `raise` | O set recusa a sério, e sabes ler a mensagem de erro de baixo para cima |
| 4 | `try` e `except` no fim do programa | O programa apanha a recusa e continua |
| 5 | A propriedade `quantidade` | Lês e escreves a quantidade como um atributo, e cada escrita é verificada |
| 6 | O construtor e o setter | Sabes porque é que o construtor também passa pelo setter |
| 7 | Os métodos `adicionar` e `retirar`, com contrato | A classe final, conferida com um traço |

Em todas as fases trabalhas da mesma maneira. Antes de executares, escreves no papel o que esperas ver. Depois executas e comparas. Quando o resultado é diferente do que previste, explica a diferença antes de continuares: é essa explicação que mais te ensina.

Executa sempre o ficheiro inteiro: cada execução começa do zero, com os valores escritos no programa. Em várias fases vais estragar o programa de propósito, para veres um erro acontecer. Faz a alteração pedida, observa, e desfaz a alteração antes de passares à fase seguinte.

## Palavras que vais usar

- Estado válido: o estado de um objeto em que todos os valores cumprem as regras do problema. Aqui, a regra é que a quantidade é um número inteiro, 0 ou mais.
- Invariante: uma regra que se tem de manter verdadeira enquanto o programa funciona, antes e depois de cada operação.
- Encapsulamento: o objeto reúne o estado e as operações, e fica responsável por manter o estado válido: é ele que verifica cada pedido antes de mudar os seus dados. Para saber mais, vê "Quem deve proteger a quantidade" no [guia](03-encapsulamento-contratos.md).
- Método get e método set: o get devolve o valor de um atributo, e o set muda-o, depois de o verificar. Em inglês, *get* quer dizer obter e *set* quer dizer definir. Para saber mais, vê a secção "Primeiro passo: métodos get e set" do [guia](03-encapsulamento-contratos.md).
- Atributo privado por convenção: um atributo cujo nome começa por sublinhado, como `_quantidade`. É um aviso de que o código de fora da classe não o deve usar, mas o Python não o impede.
- Exceção: um sinal de que alguma coisa correu mal, que interrompe o funcionamento normal do programa.
- `ValueError`: o erro de valor, a exceção que se usa quando um valor não é aceitável.
- `raise`: a instrução que lança uma exceção. Em inglês quer dizer levantar.
- Mensagem de erro e traceback: quando o programa para a meio por causa de uma exceção, o Python escreve várias linhas. A primeira é `Traceback (most recent call last):`, "o caminho até ao erro, com a chamada mais recente no fim". A última diz o tipo de erro e o que aconteceu. Um erro de escrita, como um `IndentationError`, é encontrado antes de o programa começar. A mensagem dele não tem a linha `Traceback`: abre logo com o ficheiro e o número da linha.
- `try` e `except`: dois blocos que tentam um pedido e dizem o que fazer se ele lançar uma exceção. *Try* quer dizer "tenta" e *except* quer dizer "exceto".
- Propriedade, getter e setter: uma propriedade lê-se e escreve-se como um atributo, mas a leitura executa um método, o getter, e a escrita executa outro, o setter. Para saber mais, vê "Propriedades: `@property`" no [guia](03-encapsulamento-contratos.md).
- Decorador: uma linha que começa por `@`, imediatamente antes de um `def`, e muda a maneira como esse método é usado.
- Contrato: o que uma operação recebe, o que devolve, quando falha e o que acontece ao estado em cada caso. Para saber mais, vê "Adicionar: uma operação com contrato" no [guia](03-encapsulamento-contratos.md).
- `None`: o valor especial do Python que quer dizer "nada". Em inglês, *none* quer dizer nenhum. É o que devolve um método que não tem `return`.
- Traço: a tabela que regista, passo a passo, o que acontece em cada pedido e o estado que fica depois dele.

## O que precisas

- O editor de Python que usas nas aulas, para escrever e executar os programas. Confirma que funciona: num ficheiro de ensaio, escreve `print("Olá")` e executa. Deve aparecer `Olá`, o que quer dizer que o editor está a executar programas de Python.
- O Python 3, a partir da versão 3.10. Nas versões mais antigas, algumas mensagens de erro são um pouco diferentes, e o laboratório diz onde.
- Papel e caneta, para as previsões, o traço e as respostas.

O laboratório começa de uma pasta vazia: não precisas de nenhum ficheiro do laboratório anterior.

## Se alguma coisa falhar

1. Guardaste o ficheiro antes de executar? O editor executa o que está guardado no disco. Guarda e executa outra vez.
2. Estás a executar o ficheiro certo? Confirma que o separador aberto é o `artigo.py` da pasta `tema-03`.
3. Apareceu uma mensagem de erro que não esperavas? Lê a última linha: diz o tipo de erro e o que aconteceu. Procura essa linha em [Problemas frequentes](#problemas-frequentes).
4. Desfizeste a alteração provocada no passo anterior? Cada fase parte do ficheiro como estava na paragem anterior. Se te perderes, copia o programa completo do início da fase, ou o ficheiro completo da última paragem, e continua daí.

## Preparar o projeto

1. Na pasta onde guardas os trabalhos de LP, cria uma pasta nova chamada `tema-03`. É aí que ficam os ficheiros deste laboratório.
2. Dentro dela, cria um ficheiro novo chamado `artigo.py`. O nome tem de acabar em `.py`, para o editor o reconhecer como um programa de Python, e não deve ter espaços nem acentos. Vais usar este ficheiro em todas as fases, mudando o conteúdo de fase para fase.

## Fase 1: Um estado inválido aceite sem queixa

No inventário, a quantidade de um artigo é um número inteiro, 0 ou mais: não se podem ter -3 cadernos, nem dois cadernos e meio. Um artigo cujos valores cumprem todas as regras está num estado válido. A classe `Artigo` do tema 02 ainda não verifica nada: aceita qualquer valor. Nesta fase vês o que isso provoca. Para saber mais, lê a secção "Nada impede uma quantidade impossível" do [guia](03-encapsulamento-contratos.md).

1. Copia para `artigo.py` este programa. É o ficheiro completo:

   ```python
   # artigo.py: a classe do tema 02 e três alterações impossíveis, do laboratório do tema 03.

   class Artigo:
       """Descreve um artigo do inventário: um material com código, nome e quantidade."""

       def __init__(self, codigo, nome, quantidade):
           """Prepara um artigo acabado de criar, guardando os três dados recebidos."""
           self.codigo = codigo
           self.nome = nome
           self.quantidade = quantidade

       def retirar(self, unidades):
           """Retira unidades a este artigo e devolve a quantidade que fica (sem verificar)."""
           self.quantidade = self.quantidade - unidades
           return self.quantidade


   caderno = Artigo("A01", "Caderno", 6)

   caderno.retirar(9)
   print("Depois de retirar 9:", caderno.quantidade)

   caderno.quantidade = 2.5
   print("Depois de escrever 2.5:", caderno.quantidade)

   caderno.quantidade = "muitos"
   print("Depois de escrever muitos:", caderno.quantidade)
   ```

   Leitura guiada: a classe é a do tema 02, com o construtor e o `retirar`, que subtrai sem verificar. Depois da classe, cria-se o caderno com 6 unidades. Seguem-se três blocos de duas linhas, cada um com uma alteração e um `print`. O primeiro pede ao `retirar` mais unidades do que as que existem. Os outros dois escrevem diretamente no atributo, com o ponto e o sinal `=`, sem passar por nenhum método.

2. Antes de executares, escreve no papel: o Python vai aceitar as três alterações? Que três linhas esperas ver? Depois executa. O que deves ver:

   ```text
   Depois de retirar 9: -3
   Depois de escrever 2.5: 2.5
   Depois de escrever muitos: muitos
   ```

   A resposta: o Python aceitou as três, sem uma queixa. A conta 6 - 9 = -3 está certa, mas -3 não é uma quantidade de material, e 2.5 e "muitos" também não. O artigo ficou num estado inválido por dois caminhos: um método que não verifica o pedido, e a escrita direta no atributo, de fora da classe.

3. Agora vais ver o problema que este estado inválido esconde. Acrescenta no fim do ficheiro esta linha:

   ```python partial
   caderno.retirar(1)
   ```

   Antes de executares, responde no papel: o que achas que vai acontecer, e porquê?

4. Executa. As três linhas aparecem, e depois o programa para com uma mensagem de erro parecida com esta:

   ```text
   Traceback (most recent call last):
     File ".../tema-03/artigo.py", line 28, in <module>
       caderno.retirar(1)
       ~~~~~~~~~~~~~~~^^^
     File ".../tema-03/artigo.py", line 14, in retirar
       self.quantidade = self.quantidade - unidades
                         ~~~~~~~~~~~~~~~~^~~~~~~~~~
   TypeError: unsupported operand type(s) for -: 'str' and 'int'
   ```

   O caminho do ficheiro, no lugar dos três pontos, é o do teu computador. As linhas com os sinais `~` e `^` apontam a parte da instrução onde o erro aconteceu; nas versões do Python anteriores à 3.11, não aparecem.

   Esta mensagem chama-se traceback. A primeira linha, `Traceback (most recent call last):`, quer dizer "o caminho até ao erro, com a chamada mais recente no fim". A última linha diz o tipo de erro e o que aconteceu. As linhas `File` dizem onde: o fim de cada uma diz onde estava essa linha, `in <module>` no programa principal e `in retirar` dentro do método `retirar`. `TypeError` quer dizer erro de tipo. O resto da linha diz: tipos não suportados na operação `-`, entre um `str` e um `int`. `str` é o nome que o Python dá aos textos, e `int` aos números inteiros. O Python não sabe subtrair um número a um texto.

5. Responde no papel: em que linha do programa aparece o erro? Em que linha está a causa? Porque é que um estado inválido costuma rebentar longe do sítio onde foi criado?

   A resposta: o erro aparece na linha 28, `caderno.retirar(1)`, se copiaste o programa exatamente como está, e rebenta dentro do método `retirar`, na linha 14. A causa está na linha 26, `caderno.quantidade = "muitos"`, duas linhas acima. Um estado inválido rebenta longe porque o programa aceita guardá-lo sem se queixar. O problema só aparece quando outra operação tenta usar o valor como se fosse válido. O erro está onde o valor é usado, e a causa está onde foi guardado.

### Paragem 1

O programa mostra as três linhas e para com o `TypeError` da linha 28. O ficheiro é o do passo 1, com a linha `caderno.retirar(1)` no fim.

Pensa antes de continuares: o -3 e o `TypeError` são dois erros diferentes. Qual deles avisou alguém? A resposta: só o `TypeError`. É um erro de execução: para o programa a meio, com uma mensagem. Guardar -3 é um erro de lógica: o programa continua a correr, dá um resultado errado, e ninguém é avisado. Um erro de lógica é o mais traiçoeiro, porque só se dá por ele quando alguém repara no valor errado.

## Fase 2: Um set que verifica, mas não obriga

Para impedir valores inválidos, uma ideia é mudar a quantidade só através de um método, que verifica o valor antes de o guardar. Esse método chama-se set, e o que devolve o valor chama-se get. Para verificar se um valor é inteiro, o set usa a função `isinstance(valor, int)`, que responde `True` ou `False`. O nome junta as palavras inglesas *is instance*, "é instância de": lê-se "o valor é um `int`?". Com 4 responde `True`; com 2.5, ou com o texto `"4"`, responde `False`. Para saber mais, lê "Primeiro passo: métodos get e set" no [guia](03-encapsulamento-contratos.md).

1. Substitui todo o conteúdo de `artigo.py` por este programa. É o ficheiro completo:

   ```python
   # artigo.py: os métodos get e set, com um set que recusa com print.

   class Artigo:
       """Artigo do inventário, com métodos get e set para a quantidade."""

       def __init__(self, codigo, nome, quantidade):
           """Guarda os dados iniciais do artigo."""
           self.codigo = codigo
           self.nome = nome
           self.quantidade = quantidade

       def get_quantidade(self):
           """Devolve a quantidade atual, sem a alterar."""
           return self.quantidade

       def set_quantidade(self, valor):
           """Muda a quantidade, mas só se o valor for um inteiro não negativo."""
           if isinstance(valor, int) and valor >= 0:
               self.quantidade = valor
           else:
               print("Valor recusado:", valor)


   caderno = Artigo("A01", "Caderno", 6)

   caderno.set_quantidade(-3)
   print("Depois do set com -3:", caderno.get_quantidade())

   caderno.quantidade = -3
   print("Depois da escrita direta:", caderno.get_quantidade())
   ```

   Leitura guiada: a classe tem dois métodos novos. O `get_quantidade` só devolve o valor do atributo. O `set_quantidade` tem um `if`: se o valor for inteiro e não for negativo, guarda-o; se não, mostra uma mensagem e não guarda nada. Depois da classe, o programa faz um pedido ao set e, a seguir, escreve diretamente no atributo.

2. Escreve no papel as três linhas que esperas ver. Depois executa. O que deves ver:

   ```text
   Valor recusado: -3
   Depois do set com -3: 6
   Depois da escrita direta: -3
   ```

   Isto quer dizer que o set funciona: recusou o -3, e a quantidade continuou 6. Mas a escrita direta, `caderno.quantidade = -3`, passou ao lado da verificação. É o primeiro problema do set: nada obriga a usá-lo.

3. Acrescenta no fim do ficheiro estas duas linhas:

   ```python partial
   resposta = caderno.set_quantidade(-1)
   print("O set respondeu:", resposta)
   ```

   Prevê o que aparece e executa. As três linhas de antes aparecem, e depois estas:

   ```text
   Valor recusado: -1
   O set respondeu: None
   ```

   `None` é o valor especial do Python que quer dizer "nada". É o que devolve um método que não tem `return`, como o `set_quantidade`.

4. Responde no papel: com o que o set devolve, consegue o código que o chamou saber que o pedido foi recusado?

   A resposta: não. O set devolve `None` quer aceite quer recuse, por isso o código que o chamou não tem nada que distinga os dois casos. A mensagem "Valor recusado" é para uma pessoa a olhar para o ecrã, e não para o programa. É o segundo problema do set: a recusa não chega a quem fez o pedido.

### Paragem 2

O programa mostra as cinco linhas, de `Valor recusado: -3` a `O set respondeu: None`.

Pensa antes de continuares: se o set aceitasse o valor, por exemplo com `caderno.set_quantidade(4)`, o que devolvia? A resposta: também `None`. O método não tem `return` em nenhum dos dois caminhos do `if`.

## Fase 3: Recusar a sério, com raise

Esta fase resolve os dois problemas do set.

Para o primeiro, o atributo passa a chamar-se `_quantidade`, com um sublinhado no início. Em Python, um nome que começa por sublinhado quer dizer, por convenção, "isto é interno da classe; o código de fora não o deve usar". É um aviso entre programadores, e não uma fechadura.

Para o segundo, o set passa a recusar com uma exceção, que o código que fez o pedido não pode ignorar. A instrução `raise ValueError("A quantidade não pode ser negativa.")` cria uma exceção do tipo `ValueError`, com essa mensagem. Num método sem `try`, como todos os deste laboratório, o `raise` para o método nessa linha. As linhas que estão abaixo, dentro do método, não são executadas. A exceção é enviada para trás, para o código que chamou o método. Se ninguém a tratar, o programa para e o Python mostra a mensagem. Para saber mais, lê "Recusar a sério: `ValueError` e `raise`" no [guia](03-encapsulamento-contratos.md).

1. Substitui todo o conteúdo de `artigo.py` por este programa. É o ficheiro completo:

   ```python
   # artigo.py: o atributo _quantidade e um set que recusa com raise.

   class Artigo:
       """Artigo do inventário; a quantidade fica num atributo interno, _quantidade."""

       def __init__(self, codigo, nome, quantidade):
           """Guarda os dados iniciais do artigo."""
           self.codigo = codigo
           self.nome = nome
           self._quantidade = quantidade

       def get_quantidade(self):
           """Devolve a quantidade atual, sem a alterar."""
           return self._quantidade

       def set_quantidade(self, valor):
           """Muda a quantidade; se o valor for inválido, lança ValueError e não muda nada."""
           if not isinstance(valor, int):
               raise ValueError("A quantidade tem de ser um número inteiro.")
           if valor < 0:
               raise ValueError("A quantidade não pode ser negativa.")
           self._quantidade = valor


   caderno = Artigo("A01", "Caderno", 6)
   caderno.set_quantidade(4)
   print("Quantidade:", caderno.get_quantidade())
   caderno.set_quantidade(-3)
   print("Esta linha já não é executada.")
   ```

   Leitura guiada: na classe, o construtor guarda a quantidade em `_quantidade`, e o get lê-a daí. O set tem duas verificações, cada uma com o seu `raise`, e só no fim a linha que guarda. `if not isinstance(valor, int):` lê-se "se o valor não for inteiro": o `not` inverte a resposta do `isinstance`. Depois da classe, há dois pedidos ao set, um com 4 e outro com -3.

2. Antes de executares, escreve no papel as linhas que esperas ver, incluindo a última linha da mensagem de erro. Depois executa. O que deves ver:

   ```text
   Quantidade: 4
   Traceback (most recent call last):
     File ".../tema-03/artigo.py", line 28, in <module>
       caderno.set_quantidade(-3)
       ~~~~~~~~~~~~~~~~~~~~~~^^^^
     File ".../tema-03/artigo.py", line 21, in set_quantidade
       raise ValueError("A quantidade não pode ser negativa.")
   ValueError: A quantidade não pode ser negativa.
   ```

   `ValueError` quer dizer erro de valor. O pedido de 4 foi aceite e o de -3 foi recusado, desta vez a sério: o programa parou.

3. Um traceback lê-se de baixo para cima. Responde no papel: qual é o tipo do erro, e qual é a mensagem? Em que método foi lançado? Que linha do programa fez o pedido? A linha `print("Esta linha já não é executada.")` apareceu? Porquê?

   A resposta: o tipo é `ValueError`, e a mensagem é "A quantidade não pode ser negativa.". Foi lançado no método `set_quantidade`, na linha 21, a do `raise`, como mostra a entrada logo acima da última linha. O pedido veio da linha 28, `caderno.set_quantidade(-3)`, na entrada de cima. A linha do `print` final não apareceu, porque a exceção chegou ao programa principal, ninguém a tratou, e o programa parou.

4. Agora, a ordem das verificações. No método `set_quantidade`, troca a ordem dos dois `if`, com o `raise` que está dentro de cada um, de modo que a verificação `valor < 0` venha primeiro. Depois substitui as linhas que vêm depois da classe, a partir de `caderno = ...`, por estas duas:

   ```python partial
   caderno = Artigo("A01", "Caderno", 6)
   caderno.set_quantidade("muitos")
   ```

   Prevê o que acontece e executa. A última linha da mensagem passa a ser esta:

   ```text
   TypeError: '<' not supported between instances of 'str' and 'int'
   ```

   Em português: o `<` não é suportado entre um texto (`str`) e um número inteiro (`int`). O Python tentou comparar `"muitos" < 0` antes de saber se o valor era um número.

5. Compara esta mensagem com a que o set daria com a ordem de antes: "A quantidade tem de ser um número inteiro.". Qual das duas ajuda mais quem está a usar a classe?

   A resposta: a do set. Diz, em português, o que está errado no pedido. A do Python fala de uma comparação que quem usa a classe nem sabe que existe. É por isso que o tipo se verifica primeiro: a comparação com 0 só se faz quando já se sabe que o valor é um inteiro.

6. Volta a pôr os dois `if` pela ordem do passo 1, e as linhas do fim também. Executa para confirmares que vês outra vez a saída do passo 2.

### Paragem 3

O ficheiro está outra vez como no passo 1. O programa mostra `Quantidade: 4` e para com `ValueError: A quantidade não pode ser negativa.`.

Pensa antes de continuares: se escrevesses no fim do programa, fora da classe, a linha `caderno._quantidade = -3`, o Python aceitava? A resposta: aceitava, e guardava o -3. O sublinhado é uma convenção, e o Python não tem atributos privados a sério. Mas uma linha destas, fora da classe, salta à vista de quem lê o código: toda a gente sabe que ali se passou ao lado da classe de propósito.

## Fase 4: Tratar a recusa com try e except

Um programa não pode parar de cada vez que alguém se engana num número. Para continuar depois de uma recusa, usa-se `try` e `except`. O Python executa as linhas do bloco `try` uma a uma. Se uma delas lançar a exceção que o `except` indica, abandona o bloco `try` nesse ponto e salta para o bloco `except`. Depois continua normalmente, na linha a seguir. Para saber mais, lê "Tratar a recusa: `try` e `except`" no [guia](03-encapsulamento-contratos.md).

1. Em `artigo.py`, substitui as linhas que vêm depois da classe, a partir de `caderno = ...`, por estas. A classe fica igual:

   ```python partial
   caderno = Artigo("A01", "Caderno", 6)

   try:
       caderno.set_quantidade(-3)
       print("Esta linha só é executada se o set aceitar o valor.")
   except ValueError as erro:
       print("Pedido recusado:", erro)

   print("Quantidade:", caderno.get_quantidade())
   ```

   Leitura guiada: o bloco `try` tem o pedido e uma linha que só interessa se o pedido for aceite. O bloco `except ValueError as erro` diz o que fazer se o pedido lançar um `ValueError`. A palavra `as` quer dizer "como": o nome `erro` passa a referir a exceção apanhada, e o `print` mostra a sua mensagem. A última linha, fora dos dois blocos, mostra a quantidade.

2. Prevê as linhas e executa. O que deves ver:

   ```text
   Pedido recusado: A quantidade não pode ser negativa.
   Quantidade: 6
   ```

   Isto quer dizer que o set recusou o -3, o `except` apanhou a recusa, e o programa continuou até ao fim. A frase "Esta linha só é executada..." não apareceu, porque o Python abandonou o bloco `try` na linha do pedido. A quantidade continua 6. Para confirmar que uma recusa funcionou, ver a mensagem não chega: é preciso confirmar também que o estado não mudou.

3. Uma experiência sobre o tipo da exceção. Na linha `except ValueError as erro:`, troca `ValueError` por `TypeError`. Antes de executares, escreve no papel o que achas que vai acontecer.

4. Executa. O programa para com uma mensagem de erro que acaba em `ValueError: A quantidade não pode ser negativa.`, como se não houvesse `try`. Responde: porque é que o `except` não apanhou a exceção? O que diz a linha `except` sobre as exceções que apanha?

   A resposta: o `except` diz o tipo de exceção que apanha. Um `except TypeError` deixa passar um `ValueError`, e um `except ValueError` deixa passar um `TypeError`. Este dizia `TypeError`, e a exceção era um `ValueError`, por isso passou ao lado. A linha `except ValueError as erro:` diz duas coisas: que tipo de exceção apanha e que nome dá à exceção apanhada.

5. Volta a pôr `ValueError` no `except` e executa, para confirmares que o programa volta a continuar depois da recusa.

### Paragem 4

O programa mostra `Pedido recusado: A quantidade não pode ser negativa.` e `Quantidade: 6`. O ficheiro `artigo.py` completo, como deve estar agora:

```python
# artigo.py: o atributo _quantidade e um set que recusa com raise.

class Artigo:
    """Artigo do inventário; a quantidade fica num atributo interno, _quantidade."""

    def __init__(self, codigo, nome, quantidade):
        """Guarda os dados iniciais do artigo."""
        self.codigo = codigo
        self.nome = nome
        self._quantidade = quantidade

    def get_quantidade(self):
        """Devolve a quantidade atual, sem a alterar."""
        return self._quantidade

    def set_quantidade(self, valor):
        """Muda a quantidade; se o valor for inválido, lança ValueError e não muda nada."""
        if not isinstance(valor, int):
            raise ValueError("A quantidade tem de ser um número inteiro.")
        if valor < 0:
            raise ValueError("A quantidade não pode ser negativa.")
        self._quantidade = valor


caderno = Artigo("A01", "Caderno", 6)

try:
    caderno.set_quantidade(-3)
    print("Esta linha só é executada se o set aceitar o valor.")
except ValueError as erro:
    print("Pedido recusado:", erro)

print("Quantidade:", caderno.get_quantidade())
```

Pensa antes de continuares: o set lança a exceção e não mostra nada no ecrã. Quem decide mostrar a mensagem "Pedido recusado"? Porque é que é melhor assim? A resposta: decide o código que usa a classe, no `except`. A classe decide se o valor é válido; quem a usa decide o que fazer com a recusa. A classe não sabe onde vai ser usada: hoje é um programa que escreve no terminal, amanhã pode ser uma página web, onde um `print` nem seria visto.

## Fase 5: A propriedade quantidade

O get e o set obrigam a escrever `caderno.get_quantidade()` e `caderno.set_quantidade(4)`. Uma propriedade deixa escrever `caderno.quantidade` e `caderno.quantidade = 4`, como num atributo normal, mas cada leitura executa um método, o getter, e cada escrita executa outro, o setter. Os dois métodos têm o mesmo nome, `quantidade`, e cada um leva por cima um decorador: `@property` no getter e `@quantidade.setter` no setter. O valor fica guardado em `_quantidade`, com sublinhado. Para saber mais, lê "Propriedades: `@property`" no [guia](03-encapsulamento-contratos.md).

1. Substitui todo o conteúdo de `artigo.py` por este programa. É o ficheiro completo:

   ```python
   # artigo.py: a propriedade quantidade, com getter e setter.

   class Artigo:
       """Artigo do inventário: código, nome e uma quantidade sempre válida.

       A quantidade é uma propriedade. Lê-se e escreve-se como um atributo
       normal (artigo.quantidade), mas cada escrita passa pelo setter, que
       recusa valores inválidos com ValueError.
       """

       def __init__(self, codigo, nome, quantidade):
           """Cria o artigo. A quantidade inicial passa pelo setter, como qualquer outra."""
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


   caderno = Artigo("A01", "Caderno", 6)
   print("Início:", caderno.quantidade)

   caderno.quantidade = 10
   print("Depois de acertar para 10:", caderno.quantidade)

   try:
       caderno.quantidade = 2.5
   except ValueError as erro:
       print("Recusado:", erro)
   print("Depois da tentativa com 2.5:", caderno.quantidade)

   try:
       caneta = Artigo("A03", "Caneta", -5)
   except ValueError as erro:
       print("Artigo não criado:", erro)
   ```

   Leitura guiada: começa pelos dois métodos `quantidade`. O primeiro, com `@property`, é o getter e só devolve o valor de `_quantidade`. O segundo, com `@quantidade.setter`, é o setter, com as duas verificações do set da fase 3 e, no fim, a linha que guarda. Repara depois que o construtor escreve `self.quantidade`, sem sublinhado. As linhas depois da classe usam `caderno.quantidade` como se fosse um atributo normal.

2. Prevê as cinco linhas. Pensa sobretudo nas duas tentativas que estão dentro de um `try`. Depois executa. O que deves ver:

   ```text
   Início: 6
   Depois de acertar para 10: 10
   Recusado: A quantidade tem de ser um número inteiro.
   Depois da tentativa com 2.5: 10
   Artigo não criado: A quantidade não pode ser negativa.
   ```

   Isto quer dizer que a escrita `caderno.quantidade = 2.5` passou pelo setter, que a recusou, e a quantidade ficou 10. A última linha mostra que até a criação da caneta com -5 foi recusada. Vais ver porquê na fase 6.

3. Primeiro perigo: o nome igual. Na última linha do setter, troca `self._quantidade = valor` por `self.quantidade = valor`, sem sublinhado. Antes de executares, responde no papel: escrever em `self.quantidade` executa que método? O que vai acontecer?

4. Executa. O programa para logo na criação do primeiro artigo. A mensagem repete três vezes a entrada da linha `self.quantidade = valor` e diz quantas vezes mais se repetiu, numa linha como esta:

   ```text
     [Previous line repeated 995 more times]
   ```

   Em português: a linha anterior repetiu-se mais 995 vezes. O número pode ser outro, conforme a versão do Python. A última linha é esta:

   ```text
   RecursionError: maximum recursion depth exceeded
   ```

   Nas versões mais antigas do Python, a última linha acrescenta mais umas palavras no fim, como `while calling a Python object`, "ao chamar um objeto do Python". `RecursionError` quer dizer erro de recursão, e a mensagem diz: excedida a profundidade máxima de recursão. Recursão é o nome que se dá a uma função que se chama a si própria.

5. Responde no papel: porque é que o setter se chama a si próprio? Porque é que o Python acaba por parar?

   A resposta: a última linha do setter escreve na propriedade `quantidade`, e escrever na propriedade é executar o setter. Cada execução do setter chega a essa linha e executa outra vez o setter, sem fim. O Python tem um limite para o número de chamadas que podem estar a meio ao mesmo tempo, perto de mil. Quando o ultrapassa, para com um `RecursionError`. É por isso que a propriedade e o atributo onde o valor fica têm de ter nomes diferentes: `quantidade` e `_quantidade`.

6. Volta a pôr o sublinhado, `self._quantidade = valor`, e executa, para confirmares que vês outra vez as cinco linhas do passo 2.

### Paragem 5

O ficheiro está outra vez como no passo 1, e o programa mostra as cinco linhas, de `Início: 6` a `Artigo não criado: A quantidade não pode ser negativa.`.

Pensa antes de continuares: na linha `print("Início:", caderno.quantidade)`, que método é executado? E na linha `caderno.quantidade = 10`? A resposta: na primeira, o getter, porque o programa lê a propriedade. Na segunda, o setter, porque o programa escreve nela, e o 10 chega ao setter no parâmetro `valor`.

## Fase 6: O construtor também passa pelo setter

A invariante da quantidade diz que ela é sempre válida, enquanto o artigo existir. "Sempre" inclui o momento em que o artigo nasce. O construtor escreve `self.quantidade = quantidade`, sem sublinhado: é uma escrita na propriedade, por isso o valor inicial também passa pelo setter. Nesta fase vês o que acontece quando o construtor salta o setter. Para saber mais, lê "O construtor também passa pelo setter" no [guia](03-encapsulamento-contratos.md).

1. No construtor, troca `self.quantidade = quantidade` por `self._quantidade = quantidade`, com sublinhado. Prevê o que vai acontecer à última linha que o programa mostrava, a da caneta com -5. Executa. O que deves ver:

   ```text
   Início: 6
   Depois de acertar para 10: 10
   Recusado: A quantidade tem de ser um número inteiro.
   Depois da tentativa com 2.5: 10
   ```

   A linha "Artigo não criado: ..." desapareceu. Com o sublinhado, o construtor escreve diretamente no atributo interno e passa ao lado do setter. A caneta com -5 unidades foi criada sem que ninguém verificasse nada.

2. Para veres a caneta, acrescenta no fim do ficheiro, fora de qualquer `try`, esta linha:

   ```python partial
   print("A caneta nasceu com:", caneta.quantidade)
   ```

   Executa. A última linha passa a ser `A caneta nasceu com: -5`. Repara também na terceira linha, `Recusado: ...`. A tentativa com 2.5 continua a ser recusada, porque as escritas feitas depois da criação passam pelo setter. Um teste que só experimente escritas depois da criação não apanha este erro: é preciso experimentar também a criação com um valor inválido.

3. Volta a pôr o construtor como estava, `self.quantidade = quantidade`, mas deixa ficar a linha que acrescentaste no passo 2. Antes de executares, prevê: o que vai mostrar essa linha?

4. Executa. As cinco linhas da fase 5 aparecem, e depois o programa para com uma mensagem de erro que acaba assim:

   ```text
   NameError: name 'caneta' is not defined
   ```

   `NameError` quer dizer erro de nome, e a mensagem diz: o nome `caneta` não está definido. Responde no papel: porque é que o nome `caneta` não existe?

   A resposta: na linha `caneta = Artigo("A03", "Caneta", -5)`, o construtor chamou o setter, e o setter lançou `ValueError`. A exceção interrompeu o construtor e também a atribuição ao nome `caneta`, que não chegou a acontecer. O artigo inválido não ficou disponível para o resto do programa, e é isso que queremos.

5. Apaga a linha `print("A caneta nasceu com:", caneta.quantidade)` e executa, para confirmares que vês só as cinco linhas.

### Paragem 6

O ficheiro está outra vez como na paragem 5, e o programa mostra as mesmas cinco linhas.

Pensa antes de continuares: o construtor não escreve `_quantidade` em lado nenhum. Então, quem cria o atributo `_quantidade` de cada artigo? A resposta: o setter, na primeira vez que é executado com um valor válido, quando o construtor escreve a quantidade inicial. Se esse primeiro valor for inválido, o atributo não chega a ser criado.

## Fase 7: Adicionar e retirar, com contrato

Falta escrever as operações do inventário: adicionar e retirar unidades. Antes de escrever uma operação, escreve-se o seu contrato, na docstring: o que recebe, o que devolve, quando falha e o que acontece ao estado em cada caso. Cada método verifica primeiro o pedido, pela ordem do setter: o tipo, depois o valor. O pedido tem de ser um número inteiro positivo, 1 ou mais. Só depois altera a quantidade, escrevendo na propriedade, para a escrita passar pelo setter. Para saber mais, lê "Adicionar: uma operação com contrato" e "Exemplo guiado: construir o método retirar" no [guia](03-encapsulamento-contratos.md).

1. Em `artigo.py`, acrescenta à classe o método `adicionar`, a seguir ao setter, com uma linha em branco antes. A linha `def adicionar(self, unidades):` fica com a mesma indentação dos outros `def`. É uma alteração; o método é este:

   ```python partial
       def adicionar(self, unidades):
           """Acrescenta unidades ao artigo.

           Recebe: unidades, um número inteiro positivo (1 ou mais).
           Devolve: nada (None).
           Falha: lança ValueError se unidades não for um número inteiro ou
           não for positivo. Nesse caso, a quantidade fica como estava.
           """
           if not isinstance(unidades, int):
               raise ValueError("As unidades a adicionar têm de ser um número inteiro.")
           if unidades <= 0:
               raise ValueError("As unidades a adicionar têm de ser 1 ou mais.")
           self.quantidade = self.quantidade + unidades
   ```

   Leitura guiada: lê primeiro a docstring, que é o contrato, e depois as três linhas que o cumprem. As duas verificações recusam o pedido antes de qualquer alteração. A última linha lê a quantidade pelo getter, soma as unidades e escreve o resultado pelo setter.

2. Substitui as linhas que vêm depois da classe por estas:

   ```python partial
   caderno = Artigo("A01", "Caderno", 6)

   caderno.adicionar(3)
   print("Depois de adicionar 3:", caderno.quantidade)

   try:
       caderno.adicionar(0)
   except ValueError as erro:
       print("Recusado:", erro)
   print("Depois da tentativa com 0:", caderno.quantidade)

   resposta = caderno.adicionar(1)
   print("O que adicionar devolveu:", resposta)
   print("Quantidade final:", caderno.quantidade)
   ```

   Prevê as cinco linhas e executa. O que deves ver:

   ```text
   Depois de adicionar 3: 9
   Recusado: As unidades a adicionar têm de ser 1 ou mais.
   Depois da tentativa com 0: 9
   O que adicionar devolveu: None
   Quantidade final: 10
   ```

   Isto quer dizer que o pedido de 0 foi recusado pelo próprio método, sem mexer na quantidade, e que o `adicionar` não devolve nada, como o contrato diz.

3. Acrescenta à classe o método `retirar`, a seguir ao `adicionar`, com uma linha em branco antes. É uma alteração; o método é este:

   ```python partial
       def retirar(self, unidades):
           """Retira unidades ao artigo.

           Recebe: unidades, um número inteiro positivo (1 ou mais).
           Devolve: nada (None).
           Falha: lança ValueError se unidades não for um número inteiro, se
           não for positivo, ou se não houver unidades suficientes. Esta última
           regra é verificada pelo setter da quantidade, que recusa qualquer
           valor negativo. Em todos os casos de falha, a quantidade fica como
           estava.
           """
           if not isinstance(unidades, int):
               raise ValueError("As unidades a retirar têm de ser um número inteiro.")
           if unidades <= 0:
               raise ValueError("As unidades a retirar têm de ser 1 ou mais.")
           # A falta de unidades é recusada pelo setter: o resultado seria negativo.
           self.quantidade = self.quantidade - unidades
   ```

   Leitura guiada: as duas verificações são as do `adicionar`, com outras mensagens. O método não verifica se há unidades suficientes. Quando faltam, a subtração dá um número negativo, e é o setter que o recusa, antes de guardar. Assim, a regra da quantidade fica escrita num só sítio, o setter.

4. Substitui as linhas que vêm depois da classe por estas:

   ```python partial
   caderno = Artigo("A01", "Caderno", 6)
   pasta = Artigo("A02", "Pasta", 2)

   caderno.retirar(2)
   print("Depois de retirar 2:", caderno.quantidade)

   try:
       caderno.retirar(9)
   except ValueError as erro:
       print("Retirar 9 recusado:", erro)

   try:
       caderno.retirar(0)
   except ValueError as erro:
       print("Retirar 0 recusado:", erro)

   try:
       caderno.retirar(-3)
   except ValueError as erro:
       print("Retirar -3 recusado:", erro)

   print("Caderno no fim:", caderno.quantidade)
   print("Pasta no fim:", pasta.quantidade)
   ```

5. Antes de executares, faz o traço dos quatro pedidos ao caderno, que começa com 6 unidades. Cada linha começa na quantidade deixada pela anterior. Copia a tabela para o papel e preenche as duas últimas colunas:

   | Pedido | Verificações do método | O setter recebe | Resposta | Quantidade depois |
   | --- | --- | --- | --- | ---: |
   | `retirar(2)` | inteiro e positivo: passa | 6 - 2 = 4, que é válido | | |
   | `retirar(9)` | inteiro e positivo: passa | 4 - 9 = -5, que é negativo | | |
   | `retirar(0)` | não é positivo: `ValueError` | Não chega a ser chamado | | |
   | `retirar(-3)` | não é positivo: `ValueError` | Não chega a ser chamado | | |

6. Executa e compara as seis linhas com o teu traço. O que deves ver:

   ```text
   Depois de retirar 2: 4
   Retirar 9 recusado: A quantidade não pode ser negativa.
   Retirar 0 recusado: As unidades a retirar têm de ser 1 ou mais.
   Retirar -3 recusado: As unidades a retirar têm de ser 1 ou mais.
   Caderno no fim: 4
   Pasta no fim: 2
   ```

   A resposta, nas duas colunas: o pedido de 2 é aceite, sem erro, e deixa 4. O de 9 é recusado com `ValueError` lançado pelo setter, e os de 0 e de -3 com `ValueError` lançado pelo método. Depois de cada recusa, a quantidade continua 4. A pasta, a quem não se fez nenhum pedido, continua com 2.

7. Muda o comentário do topo do ficheiro para esta linha, porque a classe já não é só a propriedade:

   ```python partial
   # artigo.py: a classe Artigo final do tema 03, com a propriedade e os métodos com contrato.
   ```

8. Acrescenta no fim do ficheiro, fora de qualquer `try`, estas duas linhas:

   ```python partial
   caderno.retirar(4)
   print("Caderno depois de retirar 4:", caderno.quantidade)
   ```

   Prevê: há erro? Que quantidade fica? Executa. A última linha é `Caderno depois de retirar 4: 0`. Retirar todas as unidades que existem é aceite, e zero é um estado válido: quer dizer que o material esgotou. Pedir para retirar 0 é que é recusado, porque não é um pedido de nada. O zero do estado e o zero do pedido são perguntas diferentes.

### Paragem 7

O programa mostra as seis linhas do passo 6 e, no fim, `Caderno depois de retirar 4: 0`. O ficheiro `artigo.py` completo, como deve estar no fim do laboratório:

```python
# artigo.py: a classe Artigo final do tema 03, com a propriedade e os métodos com contrato.

class Artigo:
    """Artigo do inventário: código, nome e uma quantidade sempre válida.

    A quantidade é uma propriedade. Lê-se e escreve-se como um atributo
    normal (artigo.quantidade), mas cada escrita passa pelo setter, que
    recusa valores inválidos com ValueError.
    """

    def __init__(self, codigo, nome, quantidade):
        """Cria o artigo. A quantidade inicial passa pelo setter, como qualquer outra."""
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
        """Acrescenta unidades ao artigo.

        Recebe: unidades, um número inteiro positivo (1 ou mais).
        Devolve: nada (None).
        Falha: lança ValueError se unidades não for um número inteiro ou
        não for positivo. Nesse caso, a quantidade fica como estava.
        """
        if not isinstance(unidades, int):
            raise ValueError("As unidades a adicionar têm de ser um número inteiro.")
        if unidades <= 0:
            raise ValueError("As unidades a adicionar têm de ser 1 ou mais.")
        self.quantidade = self.quantidade + unidades

    def retirar(self, unidades):
        """Retira unidades ao artigo.

        Recebe: unidades, um número inteiro positivo (1 ou mais).
        Devolve: nada (None).
        Falha: lança ValueError se unidades não for um número inteiro, se
        não for positivo, ou se não houver unidades suficientes. Esta última
        regra é verificada pelo setter da quantidade, que recusa qualquer
        valor negativo. Em todos os casos de falha, a quantidade fica como
        estava.
        """
        if not isinstance(unidades, int):
            raise ValueError("As unidades a retirar têm de ser um número inteiro.")
        if unidades <= 0:
            raise ValueError("As unidades a retirar têm de ser 1 ou mais.")
        # A falta de unidades é recusada pelo setter: o resultado seria negativo.
        self.quantidade = self.quantidade - unidades


caderno = Artigo("A01", "Caderno", 6)
pasta = Artigo("A02", "Pasta", 2)

caderno.retirar(2)
print("Depois de retirar 2:", caderno.quantidade)

try:
    caderno.retirar(9)
except ValueError as erro:
    print("Retirar 9 recusado:", erro)

try:
    caderno.retirar(0)
except ValueError as erro:
    print("Retirar 0 recusado:", erro)

try:
    caderno.retirar(-3)
except ValueError as erro:
    print("Retirar -3 recusado:", erro)

print("Caderno no fim:", caderno.quantidade)
print("Pasta no fim:", pasta.quantidade)

caderno.retirar(4)
print("Caderno depois de retirar 4:", caderno.quantidade)
```

Pensa antes de continuares: o setter já recusa quantidades negativas. Se apagasses as duas verificações do `adicionar`, o que fazia `caderno.adicionar(-3)` a um caderno com 6 unidades? A resposta: fazia 6 + (-3) = 3. O setter recebia 3, que é uma quantidade válida, e aceitava-a. Um pedido para adicionar teria retirado três unidades, sem ninguém dar por isso. O setter protege o estado, mas não sabe o que um pedido significa; quem o sabe é o método.

## Problemas frequentes

### `IndentationError`

`IndentationError` quer dizer erro de indentação: uma linha ficou com a indentação errada. Com `unexpected indent`, "indentação inesperada", a linha tem espaços a mais. Com `expected an indented block`, "esperava-se um bloco indentado", um `if` ou um `def` não tem nenhuma linha indentada por baixo. Com `unindent does not match any outer indentation level`, "o recuo não corresponde a nenhum nível de indentação", a linha recuou para uma indentação que não é a de nenhuma linha de cima. Dentro da classe, os `def` e os decoradores levam quatro espaços; dentro de um método, todas as linhas levam oito, e as de dentro de um `if` levam doze. Compara com o ficheiro da última paragem, linha a linha.

### `AttributeError: 'Artigo' object has no attribute 'adicionar'`

`AttributeError` quer dizer erro de atributo. Em português: o objeto do tipo `Artigo` não tem nenhum atributo chamado `adicionar`. O Python usa a palavra atributo também para os métodos. O método ficou fora da classe, com o `def` encostado à margem, e o Python aceitou-o como uma função solta. Põe o `def` com quatro espaços e as linhas de dentro com oito, como no setter.

### `NameError: name 'ValueErrror' is not defined`

Ou o mesmo com outro nome parecido, como `valueError`. As versões recentes do Python acrescentam `Did you mean: 'ValueError'?`, isto é, "querias dizer `ValueError`?". O nome da exceção escreve-se exatamente `ValueError`, com as duas maiúsculas. Este erro só aparece quando a linha do `raise` é executada, isto é, quando um valor é recusado: enquanto só experimentares valores válidos, o programa parece certo.

### `AttributeError: 'Artigo' object has no attribute '_quantidade'`

O objeto do tipo `Artigo` não tem nenhum atributo `_quantidade`. As versões recentes do Python podem acrescentar uma sugestão, como `Did you mean: 'quantidade'?`. O setter nunca guardou o valor. O construtor escreve num nome com um engano, como `self.quantiade`, ou o setter guarda noutro nome. O construtor escreve em `self.quantidade` e o setter guarda em `self._quantidade`, exatamente com estes nomes. A sugestão do Python é uma pista, e não a resposta. Se a seguires no getter e escreveres `return self.quantidade`, o getter chama-se a si próprio, e o programa para com um `RecursionError`.

### `AttributeError: 'function' object has no attribute 'setter'`

Em português: um objeto do tipo função não tem nenhum atributo `setter`. O erro aparece logo quando o Python lê a classe, na linha `@quantidade.setter`. Falta a linha `@property` antes do primeiro `def quantidade`. Escreve-a na linha imediatamente antes desse `def`.

### Valores inválidos aceites sem nenhuma recusa

O artigo aceita -5 ou 2.5, e não aparece nenhuma mensagem. Falta a linha `@quantidade.setter` antes do segundo `def quantidade`, e o setter deixou de ser um setter: a escrita guarda o valor num atributo normal, sem verificação. Escreve `@quantidade.setter` na linha imediatamente antes do segundo `def quantidade`.

### `AttributeError: property 'quantidade' of 'Artigo' object has no setter`

Em português: a propriedade `quantidade` não tem setter. Nas versões mais antigas do Python, a mensagem é outra, como `AttributeError: can't set attribute`, "não é possível definir o atributo". O segundo método tem outro nome, por exemplo `def guardar_quantidade(self, valor):`. Os dois métodos da propriedade têm de se chamar `quantidade`, porque é o nome que os liga à mesma propriedade.

### `TypeError: 'int' object is not callable`

Em português: um objeto do tipo `int` não se pode chamar. Escreveste `caderno.quantidade()`, com parênteses, como se fosse um método. Uma propriedade lê-se sem parênteses: `caderno.quantidade`.

### O programa não para no erro que esperavas

Há um `try` à volta da linha, com um `except` do tipo dessa exceção, e é isso que faz o programa continuar. Procura o `try` acima da linha.

## Desafios

1. Um limite máximo. Diz-se que, quando uma regra muda, só é preciso mudar a classe, e o resto do programa continua a fazer os mesmos pedidos. Vais comprová-lo. A regra nova: a quantidade de um artigo não pode passar de 100 unidades. Pode ser 100, mas não 101. Parte do ficheiro da paragem 7.

   Antes de mexer no código, decide e escreve no papel três coisas. Em que método da classe vais escrever a regra, e porquê? Em que posição, em relação às verificações que já lá estão? Que mensagem vais usar? Escreve a regra. Depois, confirma que não precisaste de mudar o construtor, o `adicionar` nem o `retirar`.

   Depois substitui as linhas que vêm depois da classe por testes teus, cada um no seu `try` quando puder ser recusado, que mostrem estes quatro casos:

   - criar um artigo com 150 unidades;
   - a um caderno com 6 unidades, adicionar 95;
   - ao mesmo caderno, adicionar 94;
   - acertar a quantidade do caderno para 101.

   Para cada caso, escreve antes de executar se vai ser aceite ou recusado, quem recusa e a quantidade do caderno depois. Executa e compara. No fim, responde numa frase: porque é que o `adicionar` passou a respeitar o limite, se não lhe tocaste? Pista: segue, no `adicionar`, o caminho do valor novo até ao sítio onde é guardado.

2. Perguntar se está esgotado. Acrescenta à classe um método `esgotado()`, que responde `True` se a quantidade for zero e `False` se não for. Escreve primeiro o contrato na docstring, com as quatro partes: o que recebe, o que devolve, quando falha e o que acontece ao estado. Depois testa-o com um artigo, antes e depois de lhe retirares todas as unidades. Pista: pensa se este método precisa de verificar algum valor, ou se só consulta.

## Antes de terminares

- [ ] O ficheiro `artigo.py` executa e mostra as seis linhas do passo 6 da fase 7 e `Caderno depois de retirar 4: 0`.
- [ ] Desfizeste todas as alterações provocadas de propósito: o ficheiro está igual ao da paragem 7.
- [ ] Tens no papel as previsões, as respostas de cada fase e o traço da fase 7.
- [ ] Guardaste o `artigo.py` e a folha e, se fizeste os desafios, a versão com os desafios, e entregaste-os pelo meio indicado pelo professor.
- [ ] Sabes ler um traceback de baixo para cima e dizer onde o erro aparece e onde está a causa.
- [ ] Sabes dizer porque é que o setter guarda em `_quantidade`, e porque é que o construtor escreve em `quantidade`.
- [ ] Consegues explicar, por palavras tuas, porque é que o artigo verifica cada pedido antes de mexer na quantidade, e o que fica igual quando recusa.

![Rodapé](../imagens/rodape.png)

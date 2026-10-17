![Cabeçalho](../imagens/cabecalho.png)

# Encapsulamento e contratos

Módulo M10, Introdução à Programação Orientada por Objetos. Neste guia aprendes a proteger a quantidade de um artigo: o próprio objeto passa a recusar um pedido impossível e, quando recusa, deixa os seus dados exatamente como estavam. Lês o guia ao teu ritmo, de preferência em mais do que uma vez, e o que não acabares na aula acabas em casa ou na aula seguinte. Para praticar, há o [laboratório](03-encapsulamento-contratos-laboratorio.md) e a [ficha de exercícios](03-encapsulamento-contratos-exercicios.md) deste tema.

No guia anterior, [Objetos, classes e instâncias](02-objetos-classes-instancias.md), pedimos a um artigo com 6 unidades que retirasse 2. O método fez a subtração e ficaram 4. Escolhemos de propósito um pedido que sabíamos ser possível, e avisámos que o método ainda não verificava nada. Um programa verdadeiro, porém, recebe pedidos errados: números a mais, números negativos, números com casas decimais, e até texto onde se esperava um número.

Este guia parte de um erro simples para mostrar porque é que um objeto deve controlar as alterações aos seus próprios dados. Essa ideia chama-se encapsulamento. Depois vemos, um passo de cada vez, as ferramentas que o Python oferece para a pôr em prática:

- os métodos get e set;
- o atributo com sublinhado;
- os erros do tipo `ValueError`, que um método lança para recusar um pedido;
- as propriedades, que são a forma de fazer o get e o set que já usaste nas aulas.

No fim, escrevemos as operações de adicionar e de retirar com um contrato claro.

Um bloco de código apresentado como programa completo pode ser copiado para um ficheiro novo, com a extensão `.py`. Depois executas esse ficheiro no editor de Python que usas nas aulas, como nos guias anteriores. Os programas funcionam com o Python 3, a partir da versão 3.10. Executa sempre o ficheiro inteiro: cada execução começa do zero, com os valores escritos no programa. Os blocos apresentados como excerto não correm sozinhos, e o texto diz de que outro código dependem.

## Neste guia

1. O que vais aprender
2. O que já sabes e vais usar
3. Nada impede uma quantidade impossível
4. As regras que devem continuar verdadeiras
5. Quem deve proteger a quantidade
6. Interface pública: aquilo que o objeto deixa usar
7. Primeiro passo: métodos get e set
8. O sublinhado: um atributo privado por convenção
9. Recusar a sério: `ValueError` e `raise`
10. Tratar a recusa: `try` e `except`
11. Propriedades: `@property`
12. O construtor também passa pelo setter
13. Adicionar: uma operação com contrato
14. Exemplo guiado: construir o método retirar
15. Erros frequentes
16. Palavras novas deste guia
17. Verificar o que aprendeste
18. O que vem a seguir

## O que vais aprender

No fim deste guia, consegues:

- explicar porque é que um objeto deve controlar as alterações aos seus dados, com o exemplo de uma quantidade negativa;
- distinguir um estado válido de um pedido válido, também quando o valor é zero;
- dizer o que são o encapsulamento, a ocultação de informação e a interface pública, e porque é que juntar dados e métodos numa classe não chega;
- recusar um valor inválido com `raise`, antes de alterar o estado, e tratar a recusa com `try` e `except`;
- escrever uma propriedade, com getter e setter, que guarda o valor num atributo com sublinhado e por onde passa também o construtor;
- escrever o contrato de uma operação e um método que o cumpre, e ler a mensagem de erro de uma recusa.

## O que já sabes e vais usar

- A classe `Artigo`, com o construtor `__init__`, o `self` e os atributos `codigo`, `nome` e `quantidade`: guia [02 Objetos, classes e instâncias](02-objetos-classes-instancias.md), em "A classe Artigo em Python".
- O método `retirar`, que ainda não verifica nada, e a chamada `caderno.retirar(2)`, em que o objeto antes do ponto ocupa o `self`: guia [02](02-objetos-classes-instancias.md), em "O método retirar em Python".
- Devolver e mostrar: o `return` entrega um valor a quem chamou o método, e o `print` mostra-o no ecrã. Guia [02](02-objetos-classes-instancias.md), em "O método retirar em Python".
- As regras do inventário: a quantidade é um número inteiro não negativo, e um pedido para adicionar ou para retirar é um inteiro positivo, por isso pedir 0 é recusado. Guia [01 Entidades, estado e ações](01-entidades-estado-acoes.md), em "Uma operação tem de respeitar regras".
- O traço, a tabela que regista o estado depois de cada passo: guia [01](01-entidades-estado-acoes.md), em "Exemplo guiado: seguir os valores passo a passo".
- A docstring, o texto entre três aspas que explica o que uma função ou um método faz: guia [01](01-entidades-estado-acoes.md), em "Duas maneiras de organizar um programa".
- Ler primeiro a última linha de uma mensagem de erro, a que diz o tipo de erro e o que aconteceu: guia [02](02-objetos-classes-instancias.md), em "Erros frequentes".
- Variáveis e atribuição, texto entre aspas e números, comentários com `#` e o `print` com vários valores: do 10.º ano.
- As condições com `if` e `else`, as comparações, como `<` e `<=`, o `and`, o `not` e os valores `True` e `False`: do 10.º ano.
- A conversão de um texto num número inteiro com `int`, como em `int("12")`: do 10.º ano.
- Executar um programa de Python no editor das aulas: do 10.º ano e dos guias 01 e 02.

## Nada impede uma quantidade impossível

Começamos com a classe do segundo programa do guia 02, com as mesmas instruções; só a docstring do `retirar` ficou mais curta. Com ela, fazemos três coisas que não deviam ser possíveis.

Antes de correres este programa, tenta prever: o Python vai aceitar as três alterações? Que três linhas aparecem no ecrã?

```python
# A classe do guia 02 e três coisas que não deviam ser possíveis: o primeiro programa do guia 03.

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

O programa mostra:

```text
Depois de retirar 9: -3
Depois de escrever 2.5: 2.5
Depois de escrever muitos: muitos
```

Leitura guiada: a classe é a do guia 02, e por isso começa-se pelas linhas que vêm depois dela. Cria-se o caderno com 6 unidades. Seguem-se três blocos de duas linhas, cada um com uma alteração e um `print` que mostra o resultado. O primeiro bloco faz um pedido ao método `retirar`. Os outros dois escrevem diretamente no atributo, com o ponto e o sinal `=`, sem chamar nenhum método.

O Python aceitou as três alterações sem uma queixa. A conta 6 - 9 = -3 está matematicamente certa, mas -3 não é uma quantidade de material: não se podem ter menos três cadernos no armário. Duas unidades e meia também não fazem sentido, e a palavra "muitos" nem sequer é um número.

Repara que o estado ficou inválido por dois caminhos diferentes. O primeiro é um método que não verifica o pedido antes de mexer na quantidade. O segundo é o código de fora da classe escrever diretamente no atributo, com `caderno.quantidade = ...`, sem passar por método nenhum.

Há ainda um problema escondido. Se acrescentares no fim do programa a linha `caderno.retirar(1)`, o programa mostra as três linhas e depois para, com uma mensagem de erro que acaba assim:

```text
TypeError: unsupported operand type(s) for -: 'str' and 'int'
```

`TypeError` quer dizer erro de tipo. Em português, a mensagem diz: tipos não suportados na operação `-`, entre um `str` e um `int`. `str` é o nome que o Python dá aos textos, e `int` aos números inteiros. O Python não sabe subtrair um número a um texto.

O erro aparece na linha `caderno.retirar(1)`, mas a causa está mais acima, na linha que guardou "muitos". Um estado inválido raramente rebenta no sítio onde foi criado. Rebenta mais tarde, noutro sítio, e é isso que torna estes erros difíceis de encontrar.

Este programa mostra dois tipos de erro. Guardar -3 é um **erro de lógica**: o programa continua a correr, mas dá um resultado errado, e ninguém é avisado. O `TypeError` é um **erro de execução**: o programa para a meio, com uma mensagem. Há ainda um terceiro tipo, os erros de escrita, que o Python recusa antes de começar, como os dois pontos esquecidos no fim de um `def`. Um erro de lógica é o mais traiçoeiro, porque só se dá por ele quando alguém repara no valor errado.

Também não resolve nada mostrar uma mensagem de erro depois de guardar -3. Nessa altura, a informação já está errada. A regra que vamos seguir em todo o guia tem três partes:

1. verificar primeiro;
2. alterar só se estiver tudo bem;
3. quando o pedido é recusado, deixar os dados exatamente como estavam.

## As regras que devem continuar verdadeiras

Uma quantidade do inventário é um número inteiro não negativo: 0, 1, 2, 3 e assim por diante. Não usamos -3 nem 2,5 como quantidade de um material.

Dizemos que um artigo está num **estado válido** quando todos os seus valores cumprem as regras do problema. Um artigo com quantidade 4 está num estado válido; um artigo com quantidade -3 não está.

A regra da quantidade tem de ser verdadeira antes e depois de cada operação, durante toda a vida do artigo. Uma regra que se tem de manter verdadeira enquanto o programa funciona chama-se uma **invariante**. Neste caso, a invariante é "a quantidade de um artigo é sempre um inteiro maior ou igual a zero". A palavra vem de "não variar": os valores mudam, mas a regra não deixa de ser cumprida.

Também precisamos de decidir que pedidos aceitamos. Neste inventário, há três operações sobre a quantidade:

- adicionar exige um número inteiro positivo de unidades;
- retirar exige um número inteiro positivo que não ultrapasse a quantidade disponível;
- consultar apenas informa da quantidade, sem a alterar.

### Zero no estado e zero no pedido

Com 6 unidades, retirar 6 é possível. A quantidade passa a zero, o que quer dizer que o material esgotou, e zero é um estado válido.

Com 6 unidades, pedir para retirar 0 é recusado, pela regra que escolhemos no guia 01, em "Uma operação tem de respeitar regras". Um pedido de zero unidades não é uma retirada, e quase sempre é um engano de quem o escreveu. A validade do estado e a validade do pedido são perguntas diferentes, e esta distinção vai ser precisa quando escrevermos os métodos.

## Quem deve proteger a quantidade

Se várias partes de um programa puderem alterar diretamente a quantidade, cada uma tem de se lembrar das mesmas verificações. Num programa grande, a quantidade pode ser alterada em vários sítios: onde se registam encomendas, onde se registam requisições, onde se corrigem enganos de contagem. Basta uma dessas partes esquecer-se de uma verificação para o artigo ficar num estado inválido.

Podemos organizar o programa de outra maneira. O artigo guarda a quantidade e oferece operações para a consultar e alterar. Quem precisa de retirar material faz o pedido ao artigo, e é o próprio artigo que decide se pode cumprir esse pedido. Assim, as verificações ficam escritas num único sítio, dentro da classe, e as outras partes do programa já não têm de se lembrar delas: basta pedirem ao artigo.

Esta organização é a ideia central do **encapsulamento**: reunir o estado e as operações numa unidade, o objeto, que fica responsável por manter esse estado válido. Pôr dados e métodos dentro da mesma classe é o primeiro passo, mas não chega. A classe do início deste guia já juntava dados e métodos, e mesmo assim deixava guardar -3. Só há encapsulamento quando os métodos controlam as alterações e fazem cumprir as regras.

A **ocultação de informação** completa esta ideia. A forma como a quantidade é guardada dentro do objeto passa a ser um assunto interno da classe. O código de fora não escreve nela diretamente: usa as operações que a classe disponibiliza e confia que elas respeitam as regras.

Pensa na pessoa responsável pelo armário da sala. Podes pedir-lhe duas pastas ou perguntar-lhe quantas restam, mas não abres a folha de registo dela para mudares o número por tua conta. Se toda a gente escrevesse no registo, bastava uma pessoa distraída para o registo deixar de ser verdadeiro. Como só a responsável escreve, e verifica cada pedido antes de o fazer, o registo mantém-se certo.

Há uma vantagem que só se nota com o tempo. Imagina que um dia a regra muda e o inventário passa a ter um limite máximo por artigo. Só é preciso mudar a classe. O resto do programa continua a fazer os mesmos pedidos, da mesma maneira.

## Interface pública: aquilo que o objeto deixa usar

Chamamos **interface pública** ao conjunto de operações e de dados que um objeto disponibiliza a quem o usa. A palavra "interface" não quer dizer aqui um ecrã com botões. Quer dizer a fronteira entre o objeto e o resto do programa: aquilo que se pode pedir ao objeto, no código.

No fim deste guia, a interface pública de um artigo vai ter estas operações:

| Operação | Informação recebida | O que responde | Altera a quantidade? |
| --- | --- | --- | --- |
| Consultar a quantidade | Nenhuma | A quantidade atual | Não |
| Acertar a quantidade | O novo valor | Nada, ou uma recusa | Só se o valor for válido |
| Adicionar unidades | Quantas unidades adicionar | Nada, ou uma recusa | Só se o pedido for válido |
| Retirar unidades | Quantas unidades retirar | Nada, ou uma recusa | Só se o pedido for válido |

Acertar a quantidade serve, por exemplo, para corrigir o valor depois de alguém contar à mão o que está no armário.

Quem usa estas operações precisa de saber o que cada uma faz e quando é recusada. Não precisa de saber onde, nem com que nome, a quantidade está guardada dentro do objeto. Ao longo das próximas secções vais ver o que quer dizer "uma recusa" em Python.

## Primeiro passo: métodos get e set

Nas aulas, fizeste o get e o set com propriedades, a forma que a secção "Propriedades: `@property`" explica. Esta secção mostra primeiro o get e o set escritos como dois métodos normais. É a forma mais antiga, e a que vais encontrar noutras linguagens. É também nela que se vê melhor o que uma propriedade faz por baixo. Podes lê-la como uma ponte para a secção das propriedades.

Um método **get** devolve o valor de um atributo; um método **set** muda o valor de um atributo. Os nomes vêm do inglês: *get* quer dizer obter, e *set* quer dizer definir. A vantagem de mudar a quantidade através de um método set é que o método pode verificar o valor antes de o guardar.

Para verificar, o set do programa seguinte usa uma função do Python que ainda não conheces. A função `isinstance(valor, int)` pergunta se o valor é um número inteiro, e responde `True` ou `False`. O nome junta as palavras inglesas *is instance*, "é instância de": `isinstance(valor, int)` lê-se "o valor é um `int`?". Com 4 responde `True`; com 2.5, ou com o texto `"4"`, responde `False`. A condição completa, `isinstance(valor, int) and valor >= 0`, só é verdadeira quando o valor é inteiro e, além disso, maior ou igual a zero.

Antes de correres este programa, tenta prever: o -3 do set vai ser guardado? E o -3 da última alteração?

```python
# Os métodos get e set, com um set que recusa com print: o segundo programa do guia 03.

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

O programa mostra:

```text
Valor recusado: -3
Depois do set com -3: 6
Depois da escrita direta: -3
```

Leitura guiada: na classe, o construtor é o do guia 02, e há dois métodos novos. O `get_quantidade` só devolve o valor do atributo. O `set_quantidade` tem um `if`: se o valor passar na condição, guarda-o; se não passar, mostra uma mensagem e não guarda nada. Depois da classe, a primeira metade do programa faz um pedido ao set, e a segunda escreve diretamente no atributo.

A primeira metade do programa mostra que o set funciona: o -3 foi recusado e a quantidade continuou 6. A segunda metade mostra dois problemas que o set, sozinho, não resolve.

O primeiro problema é que nada obriga a usar o set. A linha `caderno.quantidade = -3` escreve diretamente no atributo e passa ao lado da verificação. Para o Python, o método `set_quantidade` é só uma possibilidade; o atributo continua aberto a quem quiser escrever nele.

O segundo problema é mais subtil. Quando o set recusa um valor, mostra uma mensagem no ecrã, e o programa continua como se nada fosse. Uma pessoa que esteja a olhar para o ecrã vê a mensagem. Mas o código que chamou `set_quantidade` não fica a saber de nada: não tem maneira de perceber que o pedido falhou, nem de reagir a isso.

As duas secções seguintes resolvem um problema cada uma.

## O sublinhado: um atributo privado por convenção

Para resolver o primeiro problema, mudamos o nome do atributo onde a quantidade fica guardada para `_quantidade`, com um sublinhado no início.

Em Python, um nome que começa por sublinhado quer dizer, por convenção, "isto é interno da classe; o código de fora não o deve usar". Um atributo com um nome destes chama-se **atributo privado por convenção**. A classe continua a usá-lo à vontade, dentro dos seus métodos; quem está fora usa os métodos que a classe oferece.

É preciso perceber bem a palavra "convenção". O Python não tem atributos privados a sério. Nada impede alguém de escrever `caderno._quantidade = -3` fora da classe: o Python aceita e guarda o -3. O sublinhado é um aviso entre programadores, e não uma fechadura. Funciona como a placa "Reservado a funcionários" numa porta que não está trancada: quem entra consegue entrar, mas sabe que está a desrespeitar uma regra.

Mesmo assim, o sublinhado ajuda. Uma linha como `caderno._quantidade = -3`, escrita fora da classe, salta à vista de quem lê o código: toda a gente sabe que ali se passou ao lado da classe de propósito. O engano deixa de ser acidental.

Outras linguagens fazem de outra maneira. O JavaScript, que vais estudar no módulo seguinte, tem campos privados que a própria linguagem impede de usar fora da classe. O Python escolheu confiar nos programadores. Existe ainda em Python uma forma com dois sublinhados no início do nome. Torna o acesso de fora mais difícil, mas também não o impede, e não a vamos usar neste módulo.

## Recusar a sério: `ValueError` e `raise`

Para resolver o segundo problema, precisamos de uma forma de recusar que o código que fez o pedido não possa ignorar. Em Python, essa forma são as exceções.

Provavelmente já viste uma. Se escreveres `int("abc")`, o Python não consegue transformar o texto "abc" num número inteiro. Para o programa com uma mensagem que termina assim:

```text
ValueError: invalid literal for int() with base 10: 'abc'
```

Isto é uma **exceção**: um sinal de que alguma coisa correu mal, que interrompe o funcionamento normal do programa. `ValueError` quer dizer erro de valor. É o tipo de exceção que o Python usa quando um valor não é aceitável para a operação pedida. O texto depois dos dois pontos é a mensagem, que explica o que aconteceu. Aqui diz: valor inválido para `int()` na base 10, `'abc'`.

As nossas classes podem lançar as suas próprias exceções, com a instrução `raise`, que em inglês quer dizer levantar. A linha `raise ValueError("A quantidade não pode ser negativa.")` faz isto, por esta ordem:

1. Cria uma exceção do tipo `ValueError`, com a mensagem que está entre parênteses.
2. Num método sem `try`, como todos os deste guia, o `raise` para o método nessa linha. Nenhuma das linhas que estão abaixo, dentro do método, é executada.
3. Envia a exceção para trás, para o código que chamou o método.
4. Se esse código não a tratar, a exceção continua a subir para quem o chamou a ele. Se ninguém a tratar até ao programa principal, o programa para e o Python mostra a mensagem.

É o ponto 2 que protege o estado. Se a verificação e o `raise` estiverem antes da linha que guarda o valor, a recusa para o método antes dessa linha. A linha que guarda não chega a ser executada, e a quantidade fica exatamente como estava. É assim que se escreve em Python a regra "verificar primeiro, alterar depois".

Neste módulo usamos `ValueError` para todos os valores inválidos, incluindo os que nem sequer são números, para termos um único tipo de erro a tratar. O Python tem outros tipos de exceção. Já viste o `TypeError`, o erro de tipo, que aparece quando uma operação recebe um valor do tipo errado, como ao tentar subtrair um número a um texto.

O programa seguinte tem as duas correções: o atributo passa a `_quantidade` e o set passa a lançar `ValueError`. Antes de correres este programa, tenta prever: que linhas aparecem no ecrã? A última linha do programa chega a mostrar a sua frase?

```python
# O atributo _quantidade e um set que recusa com raise: o terceiro programa do guia 03.

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

O programa mostra primeiro `Quantidade: 4`, e depois uma mensagem de erro parecida com esta:

```text
Quantidade: 4
Traceback (most recent call last):
  File ".../guia03.py", line 28, in <module>
    caderno.set_quantidade(-3)
  File ".../guia03.py", line 21, in set_quantidade
    raise ValueError("A quantidade não pode ser negativa.")
ValueError: A quantidade não pode ser negativa.
```

Leitura guiada: na classe, o construtor guarda a quantidade em `_quantidade`, e o get lê-a daí. O set tem duas verificações, cada uma com o seu `raise`, e só no fim a linha que guarda. Depois da classe, o programa faz dois pedidos ao set: um com 4, que passa nas duas verificações, e outro com -3, que não passa na segunda.

Quando o programa para a meio por causa de uma exceção, o Python escreve várias linhas. A primeira é `Traceback (most recent call last):`, que quer dizer "o caminho até ao erro, com a chamada mais recente no fim". Chama-se a estas linhas o **traceback**. Cada par de linhas indica o ficheiro, o número da linha envolvida e o código dessa linha. O caminho do ficheiro, no lugar dos três pontos, é o do teu computador. A partir do Python 3.11, aparecem também linhas com os sinais `~` e `^` por baixo de algumas linhas de código, a apontar a parte da instrução envolvida. O aspeto das linhas de cima varia um pouco de uma versão para outra. Neste caso, como a mensagem é a do nosso `raise`, a última linha é igual em todas.

Um traceback lê-se de baixo para cima. A última linha diz que tipo de erro aconteceu e porquê. As linhas de cima dizem onde: neste caso, na chamada `caderno.set_quantidade(-3)`, na linha 28, e, dentro do método, na linha 21, a do `raise`. O fim de cada linha `File` diz onde estava essa linha: `in <module>` quer dizer no programa principal, fora de qualquer função, e `in set_quantidade` quer dizer dentro desse método. A última instrução do programa, que devia mostrar "Esta linha já não é executada.", não foi executada, porque o programa parou antes.

Repara em três pormenores do set.

O primeiro é o `not`. `isinstance(valor, int)` dá `True` quando o valor é inteiro, e `not` inverte a resposta. Por isso, `if not isinstance(valor, int):` lê-se "se o valor não for inteiro".

O segundo é que há duas verificações separadas, cada uma com a sua mensagem. Quem recebe o erro fica a saber exatamente qual das regras falhou.

O terceiro é a ordem das verificações. Primeiro verificamos se o valor é inteiro, e só depois se é negativo. Imagina a ordem inversa, com o valor "muitos". A comparação `"muitos" < 0` faria o próprio Python parar com um `TypeError`, com uma mensagem muito menos clara do que a nossa. Verificando o tipo primeiro, a comparação só é feita quando já sabemos que o valor é um inteiro.

## Tratar a recusa: `try` e `except`

Um programa não pode parar de cada vez que alguém se engana num número. Quando queremos que o programa continue depois de uma recusa, por exemplo para mostrar uma mensagem e seguir em frente, usamos `try` e `except`. `try` quer dizer "tenta", e `except` quer dizer "exceto" ou "a não ser que".

O programa seguinte tem a mesma classe do anterior; só mudam as linhas do fim. Antes de correres este programa, tenta prever: a frase "Esta linha só é executada..." aparece? Com que quantidade fica o caderno?

```python
# A recusa apanhada com try e except: o quarto programa do guia 03.

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

O programa mostra:

```text
Pedido recusado: A quantidade não pode ser negativa.
Quantidade: 6
```

Leitura guiada: depois da classe e da criação do caderno, há dois blocos. O bloco `try` tem o pedido e uma linha que só interessa se o pedido for aceite. O bloco `except ValueError as erro` diz o que fazer se o pedido for recusado. A última linha, fora dos dois blocos, mostra a quantidade.

O Python executa as linhas do bloco `try` uma a uma. Se nenhuma lançar uma exceção, o bloco `except` é ignorado. Se alguma lançar um `ValueError`, o Python abandona o bloco `try` nesse ponto, sem executar as linhas que faltavam, e salta para o bloco `except ValueError`. Foi o que aconteceu aqui: a mensagem "Esta linha só é executada..." não apareceu.

Em `except ValueError as erro`, a palavra `as` quer dizer "como": o nome `erro` passa a referir a exceção que foi apanhada, e `print` mostra a sua mensagem. Depois do bloco `except`, o programa continua normalmente, na linha seguinte.

A última linha é a prova de que a recusa funcionou: a quantidade continua 6. Para verificar uma operação recusada, ver a mensagem de recusa não chega. É preciso confirmar também que o estado não mudou.

Repara na divisão de tarefas. A classe decide se um valor é válido e, se não for, lança a exceção. O código que usa a classe decide o que fazer com a recusa: mostrar uma mensagem, pedir outro valor, ou outra coisa qualquer. A classe não mostra nada no ecrã, porque não sabe onde vai ser usada. Hoje é num programa que escreve no terminal. No módulo seguinte, a mesma ideia vai ser usada numa página web, onde uma mensagem escrita com `print` nem sequer seria vista.

## Propriedades: `@property`

Os métodos get e set resolvem o problema, mas obrigam a escrever `caderno.get_quantidade()` e `caderno.set_quantidade(4)` em vez de `caderno.quantidade` e `caderno.quantidade = 4`. Além de ser mais comprido, isso obriga a mudar todo o código que já usava o atributo. O Python oferece uma solução que junta as duas coisas: por fora escreve-se como se fosse um atributo, e por dentro passa-se pelos métodos que verificam. É a forma de fazer o get e o set que já usaste nas aulas; aqui vais ver porque existe e o que acontece por baixo.

Uma **propriedade** é um atributo aparente: lê-se e escreve-se como um atributo, mas cada leitura e cada escrita passam por um método. O **getter** é o método executado quando o programa lê o valor. O **setter** é o método executado quando o programa escreve um valor novo. Em inglês, *property* quer dizer propriedade, e *getter* e *setter* vêm de *get* e *set*.

Antes de correres este programa, tenta prever as cinco linhas. Pensa sobretudo nas duas tentativas que estão dentro de um `try`: a do 2.5 e a da caneta com -5.

```python
# A propriedade quantidade, com getter e setter: o quinto programa do guia 03.

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

O programa mostra:

```text
Início: 6
Depois de acertar para 10: 10
Recusado: A quantidade tem de ser um número inteiro.
Depois da tentativa com 2.5: 10
Artigo não criado: A quantidade não pode ser negativa.
```

Leitura guiada: na classe, começa pelos dois métodos com o nome `quantidade`, cada um com uma linha que começa por `@` por cima. O primeiro é o getter e o segundo é o setter, com as verificações do set da secção anterior. Depois lê o construtor, que escreve `self.quantidade`, sem sublinhado. No fim, as linhas depois da classe usam `caderno.quantidade` como se fosse um atributo normal.

Uma linha que começa por `@` e fica imediatamente antes de um `def` chama-se **decorador**. Um decorador muda a maneira como o método que vem a seguir é usado. Não precisas de saber como funciona por dentro; neste guia só precisas de conhecer o efeito destes dois.

`@property`, antes do primeiro `def quantidade`, transforma esse método no getter de uma propriedade chamada `quantidade`. A partir daí, quando o programa lê `caderno.quantidade`, sem parênteses, o Python executa este método e usa o valor que ele devolve. Na linha `print("Início:", caderno.quantidade)` e nas seguintes é isso que acontece: o getter devolve o que está guardado em `_quantidade`.

`@quantidade.setter`, antes do segundo `def quantidade`, diz: "este método é o setter da propriedade `quantidade`". Quando o programa escreve `caderno.quantidade = algum_valor`, o Python executa este método, e o valor que está à direita do `=` chega no parâmetro `valor`. O corpo do setter é igual ao do `set_quantidade` da secção anterior: as mesmas verificações, os mesmos `raise`, e só no fim a linha que guarda o valor.

Os dois métodos têm o mesmo nome, `quantidade`, e tem de ser assim: é esse nome que liga o getter e o setter à mesma propriedade. O `@property` tem de vir primeiro, porque é ele que cria a propriedade. O `@quantidade.setter` acrescenta-lhe depois o setter.

O valor, esse, fica guardado em `_quantidade`, com sublinhado. A propriedade chama-se `quantidade`, o atributo onde o valor vive chama-se `_quantidade`, e os dois nomes têm de ser diferentes. Pensa no que aconteceria se a última linha do setter fosse `self.quantidade = valor`. Essa linha é uma escrita na propriedade, por isso chamava outra vez o setter. O setter chegava de novo à mesma linha, que o chamava outra vez, e assim sem fim. O Python acabaria por parar o programa com um `RecursionError`, um erro de recursão. Recursão é o nome que se dá a uma função que se chama a si própria. Com o sublinhado, a escrita vai para o atributo interno e o ciclo não existe.

Por fim, repara que, para quem usa a classe, nada mudou em relação ao guia 02: continua a escrever `caderno.quantidade` para consultar e `caderno.quantidade = 10` para acertar. A diferença é que agora cada escrita é verificada.

## O construtor também passa pelo setter

Olha com atenção para a última linha do construtor: `self.quantidade = quantidade`, sem sublinhado. É uma escrita na propriedade, por isso o valor inicial passa pelo setter e é verificado, como qualquer outro.

Se o construtor escrevesse `self._quantidade = quantidade`, com sublinhado, passava ao lado do setter. `Artigo("A03", "Caneta", -5)` criaria uma caneta com -5 unidades, e a regra só começaria a valer na primeira alteração. A invariante diz que a quantidade é sempre válida, e "sempre" inclui o momento em que o artigo nasce.

A última linha que o programa mostrou confirma isto. Na linha `caneta = Artigo("A03", "Caneta", -5)`, o construtor chamou o setter, o setter lançou `ValueError`, e o construtor foi interrompido. A exceção interrompeu também a atribuição ao nome `caneta`, que não chegou a acontecer: o artigo inválido não ficou disponível para o resto do programa.

Há um pormenor curioso. O construtor não escreve `_quantidade` em lado nenhum. Quem cria o atributo `_quantidade` é o setter, na primeira vez que é executado com um valor válido. Se o primeiro valor for inválido, o atributo não chega a ser criado.

O código e o nome continuam a ser atributos normais, sem proteção. Na ficha deste tema, um dos exercícios de "Para ires mais longe" pede-te para pensares nas regras do nome.

## Adicionar: uma operação com contrato

As propriedades protegem o estado. Falta escrever as operações que dão sentido ao inventário: adicionar e retirar unidades. Antes de escrever uma operação, vamos escrever o que ela promete.

Um **contrato** de uma operação é uma descrição clara de quatro coisas. São o que a operação recebe, o que devolve, quando falha, e o que acontece ao estado em cada caso. O contrato serve quem escreve o método, porque diz o que tem de ser programado. Serve também quem o usa, porque diz o que pode esperar sem ter de ler o código.

O contrato de adicionar é este:

- recebe o número de unidades a adicionar, que tem de ser um inteiro positivo;
- não devolve nada;
- falha, com `ValueError`, se as unidades não forem um inteiro ou não forem positivas, e nesse caso a quantidade fica exatamente como estava;
- quando não falha, a quantidade aumenta o número de unidades pedido.

Em Python, o contrato fica escrito na docstring do método. O programa seguinte acrescenta o método `adicionar` à classe da secção das propriedades. Antes de correres este programa, tenta prever as cinco linhas. Na quarta, lê na docstring o que o contrato diz que o método devolve.

```python
# O método adicionar, com o contrato na docstring: o sexto programa do guia 03.

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

O programa mostra:

```text
Depois de adicionar 3: 9
Recusado: As unidades a adicionar têm de ser 1 ou mais.
Depois da tentativa com 0: 9
O que adicionar devolveu: None
Quantidade final: 10
```

Leitura guiada: na classe, só o método `adicionar` é novo. Lê primeiro a docstring, que é o contrato, e depois as três linhas de código, que o cumprem. Depois da classe, há três pedidos: adicionar 3, adicionar 0 dentro de um `try`, e adicionar 1, com o valor devolvido guardado em `resposta`.

O método começa por verificar o pedido, com duas verificações pela mesma ordem do setter: primeiro o tipo, depois o valor. Se uma delas falhar, o `raise` para o método antes da última linha, e a quantidade não é tocada.

A última linha, `self.quantidade = self.quantidade + unidades`, faz duas coisas. Do lado direito lê a quantidade, e essa leitura passa pelo getter. Do lado esquerdo escreve a nova quantidade, e essa escrita passa pelo setter. Com as regras desta classe, somar um inteiro positivo a uma quantidade válida dá uma quantidade válida, e o setter não tem nada a recusar aqui. Mesmo assim, escrevemos na propriedade e não em `_quantidade`. Se um dia a regra da quantidade mudar, adicionar passa a respeitá-la sem que seja preciso tocar neste método. A regra vive num só sítio.

Podias perguntar para que serve a verificação `unidades <= 0`, se o setter já protege a quantidade. Experimenta pensar em `caderno.adicionar(-3)` sem essa verificação. Com 6 unidades, a conta daria 3, que é uma quantidade válida, e o setter aceitava-a. Um pedido para adicionar teria retirado três unidades, sem ninguém dar por isso. O setter protege o estado, mas não sabe nada sobre o significado do pedido. Quem conhece o significado do pedido é o método.

Quanto ao que devolve: um método que não tem `return` devolve `None`, um valor especial do Python que quer dizer "nada". Em inglês, *none* quer dizer nenhum. É o que mostra a linha `O que adicionar devolveu: None`. No guia 02, o `retirar` devolvia a quantidade que ficava. Aqui escolhemos outro contrato: o método não devolve nada, e quem quiser saber a quantidade consulta a propriedade. O nome de um método não diz o que ele devolve; quem o diz é o contrato, e é por isso que o contrato fica escrito.

## Exemplo guiado: construir o método retirar

Vamos agora escrever o método `retirar`, a partir do contrato e usando o que já está na classe. Acompanha o raciocínio passo a passo, porque é o raciocínio, e não só o código final, que interessa.

### Passo 1: escrever o contrato

O contrato de retirar é este:

- recebe o número de unidades a retirar, que tem de ser um inteiro positivo;
- não devolve nada;
- falha, com `ValueError`, em três casos: se as unidades não forem um inteiro, se não forem positivas, ou se não houver unidades suficientes;
- em qualquer dos três casos de falha, a quantidade fica como estava; quando não falha, a quantidade diminui o número de unidades pedido.

### Passo 2: separar regras do pedido e regras do estado

Das três razões para falhar, duas são sobre o pedido e uma é sobre o estado que resultaria dele.

"As unidades têm de ser um inteiro" e "as unidades têm de ser positivas" são regras sobre o pedido. Dizem que pedidos fazem sentido, seja qual for a quantidade que existe.

"Tem de haver unidades suficientes" é, no fundo, uma regra sobre o estado. Se houver 4 unidades e alguém pedir 9, a nova quantidade seria 4 - 9 = -5. Não haver unidades suficientes é o mesmo que a nova quantidade ser negativa. E a classe já tem uma peça que recusa quantidades negativas: o setter.

### Passo 3: verificar o pedido no próprio método

Podíamos ser tentados a deixar tudo ao setter. Na secção do `adicionar` vimos que o setter protege o estado mas não conhece o significado do pedido, e no `retirar` passa-se o mesmo. Vejamos o que aconteceria, com 6 unidades, se o método fosse apenas a linha da subtração:

- `retirar(-3)` faria 6 - (-3) = 9. O setter aceitava 9, que é uma quantidade válida, e um pedido para retirar teria acrescentado três unidades;
- `retirar(0)` faria 6 - 0 = 6. O setter aceitava 6, e um pedido que a nossa regra recusa teria sido aceite em silêncio;
- `retirar("2")` tentaria subtrair um texto a um número, e o próprio Python pararia com um `TypeError`, em vez da nossa mensagem.

Nos três casos, o setter não tem culpa: o estado que recebe é válido, ou nem chega a recebê-lo. O problema está no pedido, e só o método sabe o que um pedido de retirada significa. Por isso, o método começa com as duas verificações do pedido, pela mesma ordem do setter e do `adicionar`: primeiro o tipo, depois o valor.

### Passo 4: alterar através da propriedade

Depois de o pedido passar as duas verificações, fazemos a alteração escrevendo na propriedade:

```python partial
self.quantidade = self.quantidade - unidades
```

Esta linha é um excerto do método e não corre sozinha. Se houver unidades suficientes, o resultado é zero ou mais, o setter guarda-o, e o pedido foi cumprido. Se não houver, o resultado é negativo, e o setter lança `ValueError` antes de chegar à sua última linha, a que guarda o valor. Como o `_quantidade` não foi tocado, a quantidade fica como estava, exatamente como o contrato promete.

A decisão aqui é não repetir no `retirar` uma regra que já vive no setter. Se escrevêssemos a mesma regra em dois sítios, teríamos de nos lembrar de mudar os dois sempre que ela mudasse. Assim, a regra do estado está num só sítio, e o método ocupa-se apenas do que só ele sabe: o significado do pedido.

A consequência é que, quando faltam unidades, a mensagem que se lê é a do setter, "A quantidade não pode ser negativa.". A mensagem explica a recusa: a quantidade ficaria negativa se o pedido fosse cumprido. A exceção nasce no setter, atravessa o `retirar`, que não a trata, e chega a quem fez o pedido.

### Passo 5: o método completo e o traço

O método completo, com o contrato na docstring, fica assim. É um excerto: pertence à classe e não corre sozinho, mas no passo 6 está o programa completo.

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

Antes de executar, fazemos o traço de quatro pedidos seguidos ao caderno, que começa com 6 unidades. Cada linha começa na quantidade deixada pela anterior.

| Pedido | Verificações do método | O setter recebe | Resposta | Quantidade depois |
| --- | --- | --- | --- | ---: |
| `retirar(2)` | inteiro e positivo: passa | 6 - 2 = 4, que é válido | Aceite, sem erro | 4 |
| `retirar(9)` | inteiro e positivo: passa | 4 - 9 = -5, que é negativo | `ValueError` lançado pelo setter | 4 |
| `retirar(0)` | não é positivo: `ValueError` | Não chega a ser chamado | `ValueError` lançado pelo método | 4 |
| `retirar(-3)` | não é positivo: `ValueError` | Não chega a ser chamado | `ValueError` lançado pelo método | 4 |

### Passo 6: executar e comparar com o traço

Este é o programa completo, com a classe final deste guia. Os pedidos são os quatro do traço, e há ainda uma pasta, a quem não se faz nenhum pedido. Antes de correres, escreve as seis linhas que esperas ver, a partir do traço.

```python
# A classe final do guia 03, com o método retirar do exemplo guiado.

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
```

O programa mostra:

```text
Depois de retirar 2: 4
Retirar 9 recusado: A quantidade não pode ser negativa.
Retirar 0 recusado: As unidades a retirar têm de ser 1 ou mais.
Retirar -3 recusado: As unidades a retirar têm de ser 1 ou mais.
Caderno no fim: 4
Pasta no fim: 2
```

Compara linha a linha com o traço do passo 5. O pedido de 2 foi aceite e deixou 4. Os três pedidos seguintes foram recusados: o de 9 pelo setter, e os de 0 e -3 pelo próprio método, cada um com a sua mensagem. As duas últimas linhas confirmam o que o contrato promete. Depois de três recusas, o caderno continua com 4, e a pasta, a quem não foi feito nenhum pedido, continua com 2.

Em todas as operações a ordem foi a mesma: verificar, alterar, responder. Verificar é o trabalho das condições do método e do setter. Alterar é a última linha do setter, a única que escreve em `_quantidade`. Responder é terminar sem erro, quando o pedido foi cumprido, ou lançar `ValueError`, quando foi recusado.

A interface pública do artigo ficou assim:

- `codigo` e `nome`, que ainda são atributos simples;
- a propriedade `quantidade`, para consultar e acertar;
- os métodos `adicionar` e `retirar`.

O atributo `_quantidade` é interno e fica fora da interface.

## Erros frequentes

O erro típico de cada ideia está na secção dela:

- mostrar uma mensagem depois de guardar o valor errado, em "Nada impede uma quantidade impossível";
- verificar o valor antes do tipo, em "Recusar a sério: `ValueError` e `raise`";
- o setter que guarda em `self.quantidade` e se chama a si próprio, em "Propriedades: `@property`";
- o construtor que escreve em `_quantidade` e salta o setter, em "O construtor também passa pelo setter";
- o pedido negativo que o setter não apanha, em "Adicionar: uma operação com contrato".

Ficam aqui os erros que aparecem quando se escreve uma propriedade ou uma exceção pela primeira vez. Em cada um, lê primeiro a última linha da mensagem.

### O Python diz que um número não se pode chamar

O que se vê: `TypeError: 'int' object is not callable`. Em português: um objeto do tipo `int` não se pode chamar.

Porque acontece: alguém escreveu `caderno.quantidade()`, com parênteses, como se a propriedade fosse um método get. O getter já foi executado ao ler `caderno.quantidade` e devolveu um número. Os parênteses pedem ao Python que chame esse número, e um número não é uma função.

Como se corrige: uma propriedade lê-se sem parênteses, `caderno.quantidade`, como um atributo.

### A classe falha antes de haver qualquer artigo

O que se vê: `AttributeError: 'function' object has no attribute 'setter'`. `AttributeError` quer dizer erro de atributo. Em português, a mensagem diz que um objeto do tipo função não tem nenhum atributo chamado `setter`. A mensagem aponta a linha `@quantidade.setter` e aparece logo quando o Python lê a classe, antes de se criar qualquer artigo.

Porque acontece: falta a linha `@property` antes do primeiro `def quantidade`. Sem ela, `quantidade` é um método normal, uma função, e uma função não tem setter.

Como se corrige: escreve `@property` na linha imediatamente antes do primeiro `def quantidade`.

### Valores inválidos aceites sem nenhuma recusa

O que se vê: nenhuma mensagem de erro, mas o artigo aceita -5 ou 2.5 como quantidade.

Porque acontece: falta a linha `@quantidade.setter` antes do segundo `def quantidade`. Sem ela, esse segundo `def` é um método normal, que ocupa o lugar da propriedade. A escrita `self.quantidade = ...` passa a guardar o valor num atributo normal, sem passar por nenhuma verificação.

Como se corrige: escreve `@quantidade.setter` na linha imediatamente antes do segundo `def quantidade`.

### O nome da exceção mal escrito

O que se vê: `NameError: name 'ValueErrror' is not defined`, ou o mesmo com `valueError`. `NameError` quer dizer erro de nome, e a mensagem diz que o nome não está definido. A partir do Python 3.10, acrescenta uma sugestão: `Did you mean: 'ValueError'?`, isto é, "querias dizer `ValueError`?".

Porque acontece: o nome da exceção tem de ser escrito exatamente `ValueError`, com as duas maiúsculas. Repara que este erro só aparece quando a linha do `raise` é executada, isto é, quando um valor é recusado. Enquanto só experimentares valores válidos, o programa parece certo.

Como se corrige: escreve `ValueError` e experimenta também um valor inválido, para a linha do `raise` ser executada.

### O `except` não apanha a recusa

O que se vê: o programa para com um traceback que acaba em `ValueError`, apesar de o pedido estar dentro de um `try`.

Porque acontece: o `except` diz outro tipo de exceção, como `except TypeError`. Um `except TypeError` deixa passar um `ValueError`, e um `except ValueError` deixa passar um `TypeError`. A exceção que o `except` não diz passa ao lado, como se não houvesse `try`.

Como se corrige: escreve no `except` o tipo de exceção que o método lança, aqui `except ValueError`.

## Palavras novas deste guia

- Estado válido: o estado de um objeto em que todos os valores cumprem as regras do problema.
- Invariante: uma regra que se tem de manter verdadeira enquanto o programa funciona, antes e depois de cada operação.
- Erro de lógica: um erro em que o programa continua a correr, mas dá um resultado errado.
- Erro de execução: um erro que para o programa a meio, com uma mensagem.
- Erro de escrita: um erro que o Python encontra antes de o programa começar, como os dois pontos esquecidos no fim de um `def`.
- Encapsulamento: reunir o estado e as operações num objeto, que fica responsável por manter esse estado válido.
- Ocultação de informação: a forma como um valor é guardado dentro do objeto é assunto interno da classe; o código de fora usa as operações.
- Interface pública: o conjunto de operações e de dados que um objeto disponibiliza a quem o usa.
- Método get: um método que devolve o valor de um atributo.
- Método set: um método que muda o valor de um atributo, e que pode verificá-lo antes de o guardar.
- `isinstance`: a função que pergunta se um valor é de um certo tipo, como em `isinstance(valor, int)`.
- Atributo privado por convenção: um atributo cujo nome começa por sublinhado, como `_quantidade`, que o código de fora não deve usar.
- Exceção: um sinal de que alguma coisa correu mal, que interrompe o funcionamento normal do programa.
- `ValueError`: o erro de valor, a exceção que se usa quando um valor não é aceitável.
- `TypeError`: o erro de tipo, que aparece quando uma operação recebe um valor do tipo errado.
- `raise`: a instrução que lança uma exceção. Num método sem `try`, como todos os deste guia, para o método nessa linha.
- Traceback: as linhas que o Python escreve quando o programa para a meio por causa de uma exceção, com o caminho até ao erro.
- `try` e `except`: os dois blocos que tentam um pedido e dizem o que fazer se ele lançar uma exceção de um certo tipo.
- Propriedade: um atributo aparente, que se lê e escreve como um atributo, mas passa pelo getter e pelo setter.
- Getter: o método de uma propriedade que é executado quando se lê o valor.
- Setter: o método de uma propriedade que é executado quando se escreve um valor novo.
- Decorador: uma linha que começa por `@`, antes de um `def`, e muda a maneira como o método é usado.
- Recursão: uma função que se chama a si própria.
- `RecursionError`: o erro de recursão, que aparece quando uma função se chama a si própria sem fim.
- Contrato: a descrição do que uma operação recebe, do que devolve, de quando falha e do que acontece ao estado em cada caso.
- `None`: o valor especial do Python que quer dizer "nada", e que um método sem `return` devolve.

## Verificar o que aprendeste

Tenta responder sem olhar para o texto. Se uma pergunta te deixar com dúvidas, volta à secção indicada. As perguntas 7 e 8 pedem que executes um programa. Escreve a previsão antes; se a execução der outra coisa, procura a explicação em vez de mudar a previsão.

1. Porque é que mostrar uma mensagem depois de guardar -3 não resolve nada? ("Nada impede uma quantidade impossível")
2. Qual é a diferença entre juntar dados e métodos numa classe e ter encapsulamento? ("Quem deve proteger a quantidade")
3. Porque é que `_quantidade` é privado só por convenção? ("O sublinhado: um atributo privado por convenção")
4. O que acontece às linhas que estão depois de um `raise`, dentro do mesmo método? Porque é que isso protege o estado? ("Recusar a sério: `ValueError` e `raise`")
5. Porque é que o setter guarda o valor em `_quantidade`, e não em `quantidade`? ("Propriedades: `@property`")
6. No `retirar` do exemplo guiado, que parte das regras é verificada pelo método e que parte é verificada pelo setter? Porquê? ("Exemplo guiado: construir o método retirar")
7. Copia o programa do passo 6 do exemplo guiado e substitui as linhas que vêm depois da classe (a partir de `caderno = ...`) por estas, que são um excerto:

   ```python partial
   caneta = Artigo("A03", "Caneta", 4)
   caneta.adicionar(2)
   try:
       caneta.retirar(0)
   except ValueError as erro:
       print(erro)
   try:
       caneta.retirar(10)
   except ValueError as erro:
       print(erro)
   print(caneta.quantidade)
   ```

   Sem executar, responde:

   1. Quantas vezes é executado o setter da quantidade neste excerto? Para cada vez, diz que valor recebe e se o guarda ou lança uma exceção.
   2. Há um pedido em que o setter não chega a ser executado. Qual é, e porquê?
   3. Que linhas aparecem no ecrã, e por que ordem?

   Para confirmares a resposta 1, acrescenta temporariamente esta linha no início do setter, logo a seguir à docstring, e executa: `print("setter recebeu", valor)`. Depois de confirmares, apaga-a.
8. Com o mesmo programa, substitui as linhas que vêm depois da classe por estas, que são um excerto:

   ```python partial
   caderno = Artigo("A01", "Caderno", 6)
   caderno._quantidade = -1
   print(caderno.quantidade)
   caderno.adicionar(3)
   print(caderno.quantidade)
   ```

   1. Antes de executar, escreve o que esperas ver nas duas linhas do ecrã.
   2. Porque é que o Python aceitou a segunda linha do excerto?
   3. Depois de `adicionar(3)`, que quantidade ficou, e é válida? Isso quer dizer que o artigo esteve num estado válido do princípio ao fim? Explica, usando a palavra invariante.
   4. Numa frase, explica a diferença entre uma convenção e uma proteção, usando este excerto como exemplo.

Se ainda confundes o que o método verifica com o que o setter verifica, volta ao passo 3 do exemplo guiado. Refaz, de cabeça, os três pedidos que o setter não apanharia sozinho.

## O que vem a seguir

Para praticar este tema, faz o [laboratório](03-encapsulamento-contratos-laboratorio.md) e depois a [ficha de exercícios](03-encapsulamento-contratos-exercicios.md). A ficha acaba com exercícios para ires mais longe, que fazes quando quiseres aprofundar ou quando o professor os indicar.

O tema seguinte é [Composição e modelação](04-composicao-modelacao.md). Lá, os artigos deixam de estar sozinhos: um inventário vai reunir vários artigos e encaminhar pedidos para eles, e vais ver o que cabe a cada um fazer.

![Rodapé](../imagens/rodape.png)

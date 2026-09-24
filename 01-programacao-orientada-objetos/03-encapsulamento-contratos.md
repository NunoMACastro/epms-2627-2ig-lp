![Cabeçalho](../imagens/cabecalho.png)

# Proteger a quantidade de um artigo: encapsulamento e contratos

*M10 · Caderno 3*

No caderno anterior, pedimos a um artigo com 6 unidades que retirasse 2. O método fez a subtração e ficaram 4. Escolhemos de propósito um pedido que sabíamos ser possível, e avisámos que o método ainda não verificava nada. Um programa verdadeiro, porém, recebe pedidos errados: números a mais, números negativos, números com casas decimais, e até texto onde se esperava um número.

Este caderno parte de um erro simples para mostrar porque é que um objeto deve controlar as alterações aos seus próprios dados. Essa ideia chama-se encapsulamento. Depois vemos, um passo de cada vez, as ferramentas que o Python oferece para a pôr em prática: os métodos get e set que já viste nas aulas, o atributo com sublinhado, os erros do tipo `ValueError` e as propriedades. No fim, escrevemos as operações de adicionar e de retirar com um contrato claro.

Os programas completos correm sozinhos, como nos cadernos anteriores: copia-os para um ficheiro `.py` e executa o ficheiro inteiro. Os excertos estão sempre assinalados.

## 1. Nada impede uma quantidade impossível

Começamos com a classe do caderno 2, sem nenhuma alteração, e fazemos três coisas que não deviam ser possíveis. Programa completo:

```python
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

O Python aceitou as três alterações sem uma queixa. A conta 6 - 9 = -3 está matematicamente certa, mas -3 não é uma quantidade de material: não se podem ter menos três cadernos no armário. Duas unidades e meia também não fazem sentido, e a palavra "muitos" nem sequer é um número.

Repara que o estado ficou inválido por dois caminhos diferentes. O primeiro é um método que não verifica o pedido antes de mexer na quantidade. O segundo é o código de fora da classe escrever diretamente no atributo, com `caderno.quantidade = ...`, sem passar por método nenhum.

Há ainda um problema escondido. Depois de a quantidade passar a "muitos", uma chamada como `caderno.retirar(1)` fazia o programa parar com um erro, porque o Python não sabe subtrair um número a um texto. O erro apareceria nessa linha, mas a causa estaria duas linhas acima, onde alguém guardou "muitos". Um estado inválido raramente rebenta no sítio onde foi criado: rebenta mais tarde, noutro sítio, e é isso que torna estes erros difíceis de encontrar.

Também não resolve nada mostrar uma mensagem de erro depois de guardar -3. Nessa altura a informação já está errada. A regra que vamos seguir em todo o caderno é esta: verificar primeiro, alterar só se estiver tudo bem, e, quando o pedido é recusado, deixar os dados exatamente como estavam.

## 2. As regras que devem continuar verdadeiras

Uma quantidade do inventário é um número inteiro não negativo: 0, 1, 2, 3 e assim por diante. Não usamos -3 nem 2,5 como quantidade de um material.

Dizemos que um artigo está num **estado válido** quando todos os seus valores cumprem as regras do problema. Um artigo com quantidade 4 está num estado válido; um artigo com quantidade -3 não está.

A regra da quantidade tem de ser verdadeira antes e depois de cada operação, durante toda a vida do artigo. Uma regra que tem de se manter sempre verdadeira enquanto o programa funciona chama-se uma **invariante**. Neste caso, a invariante é "a quantidade de um artigo é sempre um inteiro maior ou igual a zero". A palavra vem de "não variar": os valores mudam, mas a regra não deixa de ser cumprida.

Também precisamos de decidir que pedidos aceitamos. Neste inventário, adicionar exige um número inteiro positivo de unidades; retirar exige um número inteiro positivo que não ultrapasse a quantidade disponível; e consultar apenas informa da quantidade, sem a alterar.

### Zero no estado e zero no pedido

Com 6 unidades, retirar 6 é possível. A quantidade passa a zero, o que quer dizer que o material esgotou, e zero é um estado válido.

Com 6 unidades, pedir para retirar 0 é recusado, segundo a regra que escolhemos no caderno 1. Um pedido de zero unidades não é uma retirada, e quase sempre é um engano de quem o escreveu. A validade do estado e a validade do pedido são perguntas diferentes, e esta distinção vai ser precisa quando escrevermos os métodos.

## 3. Quem deve proteger a quantidade

Se várias partes de um programa puderem alterar diretamente a quantidade, cada uma tem de se lembrar das mesmas verificações. Num programa grande, a quantidade pode ser alterada no sítio onde se registam encomendas, no sítio onde se registam requisições, no sítio onde se corrigem enganos de contagem. Basta uma dessas partes esquecer-se de uma verificação para o artigo ficar num estado inválido.

Podemos organizar o programa de outra maneira. O artigo guarda a quantidade e oferece operações para a consultar e alterar. Quem precisa de retirar material faz o pedido ao artigo, e é o próprio artigo que decide se pode cumprir esse pedido. Assim, as verificações ficam escritas num único sítio, dentro da classe, e nenhuma parte do programa se pode esquecer delas.

Esta organização é a ideia central do **encapsulamento**: reunir o estado e as operações numa unidade, o objeto, que fica responsável por manter esse estado válido. Pôr dados e métodos dentro da mesma classe é o primeiro passo, mas não chega. A classe do início deste caderno já juntava dados e métodos, e mesmo assim deixava guardar -3. Só há encapsulamento quando os métodos controlam as alterações e fazem cumprir as regras.

A **ocultação de informação** completa esta ideia. A forma como a quantidade é guardada dentro do objeto passa a ser um assunto interno da classe. O código de fora não escreve nela diretamente; usa as operações que a classe disponibiliza e confia que elas respeitam as regras.

Pensa na pessoa responsável pelo armário da sala. Podes pedir-lhe duas pastas ou perguntar-lhe quantas restam, mas não abres o caderno de registo dela para mudares o número por tua conta. Se toda a gente escrevesse no registo, bastava uma pessoa distraída para o registo deixar de ser verdadeiro. Como só a responsável escreve, e verifica cada pedido antes de o fazer, o registo mantém-se certo.

Há uma vantagem que só se nota com o tempo. Se um dia a regra mudar, por exemplo, se o inventário passar a ter um limite máximo por artigo, só é preciso mudar a classe. O resto do programa continua a fazer os mesmos pedidos da mesma maneira.

## 4. Interface pública: aquilo que o objeto deixa usar

Chamamos **interface pública** ao conjunto de operações e de dados que um objeto disponibiliza a quem o usa. A palavra "interface" não quer dizer aqui um ecrã com botões. Quer dizer a fronteira entre o objeto e o resto do programa: aquilo que se pode pedir ao objeto, no código.

No fim deste caderno, a interface pública de um artigo vai ter estas operações:

| Operação | Informação recebida | O que responde | Altera a quantidade? |
| --- | --- | --- | --- |
| Consultar a quantidade | Nenhuma | A quantidade atual | Não |
| Acertar a quantidade | O novo valor | Nada, ou uma recusa | Só se o valor for válido |
| Adicionar unidades | Quantas unidades adicionar | Nada, ou uma recusa | Só se o pedido for válido |
| Retirar unidades | Quantas unidades retirar | Nada, ou uma recusa | Só se o pedido for válido |

Acertar a quantidade serve, por exemplo, para corrigir o valor depois de alguém contar à mão o que está no armário.

Quem usa estas operações precisa de saber o que cada uma faz e quando é recusada. Não precisa de saber onde, nem com que nome, a quantidade está guardada dentro do objeto. Ao longo das próximas secções vais ver o que quer dizer "uma recusa" em Python.

## 5. Primeiro passo: métodos get e set

Nas aulas já usaste métodos **get** e **set**. Um método get devolve o valor de um atributo; um método set muda o valor de um atributo. Os nomes vêm do inglês: *get* quer dizer obter, e *set* quer dizer definir. A vantagem de mudar a quantidade através de um método set é que o método pode verificar o valor antes de o guardar.

Programa completo:

```python
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

A função `isinstance(valor, int)` pergunta se o valor é um número inteiro, e responde `True` ou `False`. Com 4 responde `True`; com 2.5, ou com o texto `"4"`, responde `False`. A condição completa, `isinstance(valor, int) and valor >= 0`, só é verdadeira quando o valor é inteiro e, além disso, maior ou igual a zero.

A primeira metade do programa mostra que o set funciona: o -3 foi recusado e a quantidade continuou 6. A segunda metade mostra dois problemas que o set, sozinho, não resolve.

O primeiro problema é que nada obriga a usar o set. A linha `caderno.quantidade = -3` escreve diretamente no atributo e passa ao lado da verificação. Para o Python, o método `set_quantidade` é só uma possibilidade; o atributo continua aberto a quem quiser escrever nele.

O segundo problema é mais subtil. Quando o set recusa um valor, mostra uma mensagem no ecrã, e o programa continua como se nada fosse. Uma pessoa que esteja a olhar para o ecrã vê a mensagem, mas o código que chamou `set_quantidade` não fica a saber de nada. Não tem maneira de perceber que o pedido falhou, nem de reagir a isso.

As duas secções seguintes resolvem um problema cada uma.

## 6. O sublinhado: um atributo privado por convenção

Para resolver o primeiro problema, mudamos o nome do atributo onde a quantidade fica guardada para `_quantidade`, com um sublinhado no início.

Em Python, um nome que começa por sublinhado quer dizer, por convenção, "isto é interno da classe; o código de fora não o deve usar". Um atributo com um nome destes chama-se **atributo privado por convenção**. A classe continua a usá-lo à vontade, dentro dos seus métodos; quem está fora usa os métodos que a classe oferece.

É preciso perceber bem a palavra "convenção". O Python não tem atributos privados a sério. Nada impede alguém de escrever `caderno._quantidade = -3` fora da classe: o Python aceita e guarda o -3. O sublinhado é um aviso entre programadores, e não uma fechadura. Funciona como a placa "Reservado a funcionários" numa porta que não está trancada: quem entra consegue entrar, mas sabe que está a desrespeitar uma regra.

Mesmo assim, o sublinhado ajuda. Uma linha como `caderno._quantidade = -3`, escrita fora da classe, salta à vista de quem lê o código: toda a gente sabe que ali se passou ao lado da classe de propósito. O engano deixa de ser acidental.

Outras linguagens fazem de outra maneira. O JavaScript, que vais estudar no módulo seguinte, tem campos privados que a própria linguagem impede de usar fora da classe. O Python escolheu confiar nos programadores. Existe ainda em Python uma forma com dois sublinhados no início do nome, que torna o acesso de fora mais difícil, mas também não o impede; não a vamos usar neste módulo.

## 7. Recusar a sério: `ValueError` e `raise`

Para resolver o segundo problema, precisamos de uma forma de recusar que o código que fez o pedido não possa ignorar. Em Python, essa forma são as exceções.

Provavelmente já viste uma. Se escreveres `int("abc")`, o Python não consegue transformar o texto "abc" num número inteiro e para o programa com uma mensagem que termina assim: `ValueError: invalid literal for int() with base 10: 'abc'`. Isto é uma **exceção**: um sinal de que alguma coisa correu mal, que interrompe o funcionamento normal do programa. `ValueError` é o tipo de exceção que o Python usa quando um valor não é aceitável para a operação pedida. O texto depois dos dois pontos é a mensagem, que explica o que aconteceu.

As nossas classes podem lançar as suas próprias exceções, com a instrução `raise`. A linha `raise ValueError("A quantidade não pode ser negativa.")` faz quatro coisas, por esta ordem:

1. Cria uma exceção do tipo `ValueError`, com a mensagem que está entre parênteses.
2. Para o método nessa linha. Nenhuma das linhas que estão abaixo, dentro do método, é executada.
3. Envia a exceção para trás, para o código que chamou o método.
4. Se esse código não tratar a exceção, o programa para e o Python mostra a mensagem.

O ponto 2 é o mais importante para nós. Se a verificação e o `raise` estiverem antes da linha que guarda o valor, então, quando o valor é recusado, essa linha nunca chega a ser executada, e a quantidade fica exatamente como estava. É assim que se escreve em Python a regra "verificar primeiro, alterar depois".

Neste módulo usamos `ValueError` para todos os valores inválidos, incluindo os que nem sequer são números, para termos um único tipo de erro a tratar. O Python tem outros tipos de exceção, como `TypeError`, que aparece quando uma operação recebe um valor do tipo errado, como ao tentar subtrair um texto a um número. Vais encontrá-lo em algumas mensagens de erro.

Eis a classe com as duas correções: o atributo passa a `_quantidade` e o set passa a lançar `ValueError`. Programa completo:

```python
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

O programa mostra primeiro:

```text
Quantidade: 4
```

A seguir, o Python escreve várias linhas que começam por `Traceback (most recent call last):`. Essas linhas indicam o caminho que a exceção percorreu: o ficheiro, o número de cada linha envolvida e o código dessa linha. O aspeto exato varia um pouco de uma versão do Python para outra, mas a última linha é sempre esta:

```text
ValueError: A quantidade não pode ser negativa.
```

Uma mensagem de erro do Python lê-se de baixo para cima. A última linha diz que tipo de erro aconteceu e porquê. As linhas de cima dizem onde: neste caso, na chamada `caderno.set_quantidade(-3)` e, dentro do método, na linha do `raise`. A última instrução do programa, que devia mostrar "Esta linha já não é executada.", não foi executada, porque o programa parou antes.

Repara em três pormenores do set.

O primeiro é o `not`. `isinstance(valor, int)` dá `True` quando o valor é inteiro; `not` inverte a resposta. Por isso, `if not isinstance(valor, int):` lê-se "se o valor não for inteiro".

O segundo é que há duas verificações separadas, cada uma com a sua mensagem. Quem recebe o erro fica a saber exatamente qual das regras falhou.

O terceiro é a ordem das verificações. Primeiro verificamos se o valor é inteiro, e só depois se é negativo. Se a ordem fosse a inversa e o valor fosse o texto "muitos", a comparação `"muitos" < 0` faria o próprio Python parar com um `TypeError`, com uma mensagem muito menos clara do que a nossa. Verificando o tipo primeiro, a comparação só é feita quando já sabemos que o valor é um inteiro.

## 8. Tratar a recusa: `try` e `except`

Um programa não pode parar sempre que alguém se engana num número. Quando queremos que o programa continue depois de uma recusa, por exemplo para mostrar uma mensagem e seguir em frente, usamos `try` e `except`. Programa completo, com a mesma classe da secção 7:

```python
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

`try` quer dizer "tenta". O Python executa as linhas do bloco `try` uma a uma. Se nenhuma lançar uma exceção, o bloco `except` é ignorado. Se alguma lançar um `ValueError`, o Python abandona o bloco `try` nesse ponto, sem executar as linhas que faltavam, e salta para o bloco `except ValueError`. Foi o que aconteceu aqui: a mensagem "Esta linha só é executada..." não apareceu.

Em `except ValueError as erro`, o nome `erro` passa a referir a exceção que foi apanhada, e `print` mostra a sua mensagem. Depois do bloco `except`, o programa continua normalmente, na linha seguinte.

A última linha é a prova de que a recusa funcionou: a quantidade continua 6. Para verificar uma operação recusada, nunca basta ver a mensagem de recusa. É preciso confirmar também que o estado não mudou.

Repara na divisão de tarefas. A classe decide se um valor é válido e, se não for, lança a exceção. O código que usa a classe decide o que fazer com a recusa: mostrar uma mensagem, pedir outro valor, ou outra coisa qualquer. A classe não mostra nada no ecrã, porque não sabe onde vai ser usada. Hoje é num programa que escreve no terminal; no módulo seguinte, a mesma ideia vai ser usada numa página web, onde uma mensagem escrita com `print` nem sequer seria vista.

## 9. Propriedades: `@property`

Os métodos get e set resolvem o problema, mas obrigam a escrever `caderno.get_quantidade()` e `caderno.set_quantidade(4)` em vez de `caderno.quantidade` e `caderno.quantidade = 4`. Além de ser mais comprido, isso obriga a mudar todo o código que já usava o atributo. O Python oferece uma solução que junta as duas coisas: por fora escreve-se como se fosse um atributo, e por dentro passa-se pelos métodos que verificam.

Uma **propriedade** é um atributo aparente, cujo valor é lido e escrito através de dois métodos: um **getter**, executado quando alguém lê o valor, e um **setter**, executado quando alguém escreve um valor novo. Programa completo:

```python
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

Vamos por partes.

Uma linha que começa por `@` e fica imediatamente antes de um `def` chama-se **decorador**. Um decorador muda a maneira como o método que vem a seguir é usado. Não precisas de saber como funciona por dentro; neste caderno só precisas de conhecer o efeito destes dois.

`@property`, antes do primeiro `def quantidade`, transforma esse método no getter de uma propriedade chamada `quantidade`. A partir daí, sempre que alguém escreve `caderno.quantidade`, sem parênteses, o Python executa este método e usa o valor que ele devolve. Nas linhas `print("Início:", caderno.quantidade)` e seguintes é isso que acontece: o getter devolve o que está guardado em `_quantidade`.

`@quantidade.setter`, antes do segundo `def quantidade`, diz: "este método é o setter da propriedade `quantidade`". Sempre que alguém escreve `caderno.quantidade = algum_valor`, o Python executa este método, e o valor que está à direita do `=` chega no parâmetro `valor`. O corpo do setter é igual ao do `set_quantidade` da secção 7: as mesmas verificações, os mesmos `raise`, e só no fim a linha que guarda o valor.

Os dois métodos têm o mesmo nome, `quantidade`, e isso é obrigatório: é esse nome que liga o getter e o setter à mesma propriedade. O `@property` tem de vir primeiro, porque é ele que cria a propriedade à qual o `@quantidade.setter` depois acrescenta o setter.

O valor, esse, fica guardado em `_quantidade`, com sublinhado. A propriedade chama-se `quantidade` e o atributo onde o valor vive chama-se `_quantidade`, e os dois nomes têm de ser diferentes. Pensa no que aconteceria se a última linha do setter fosse `self.quantidade = valor`: essa linha é uma escrita na propriedade, por isso chamava outra vez o setter, que chegava de novo à mesma linha, que chamava outra vez o setter, e assim sem fim. O Python acabaria por parar o programa com um erro chamado `RecursionError`. Com o sublinhado, a escrita vai para o atributo interno e o ciclo não existe.

Por fim, repara que, para quem usa a classe, nada mudou em relação ao caderno 2: continua a escrever `caderno.quantidade` para consultar e `caderno.quantidade = 10` para acertar. A diferença é que agora cada escrita é verificada.

## 10. O construtor também passa pelo setter

Olha com atenção para a última linha do construtor: `self.quantidade = quantidade`, sem sublinhado. É uma escrita na propriedade, por isso o valor inicial passa pelo setter e é verificado, como qualquer outro.

Se o construtor escrevesse `self._quantidade = quantidade`, com sublinhado, passava ao lado do setter. `Artigo("A03", "Caneta", -5)` criaria uma caneta com -5 unidades, e a regra só começaria a valer na primeira alteração. A regra diz que a quantidade é sempre válida, e "sempre" inclui o momento em que o artigo nasce.

A última linha que o programa mostrou confirma isto. Na linha `caneta = Artigo("A03", "Caneta", -5)`, o construtor chamou o setter, o setter lançou `ValueError`, e o construtor foi interrompido. A exceção interrompeu também a atribuição ao nome `caneta`, que nunca chegou a acontecer: o artigo inválido não chegou a existir para o resto do programa.

Há um pormenor curioso. O construtor não escreve `_quantidade` em lado nenhum. Quem cria o atributo `_quantidade` é o setter, na primeira vez que é executado com um valor válido. Se o primeiro valor for inválido, o atributo nunca chega a ser criado.

O código e o nome continuam a ser atributos normais, sem proteção. No exercício 5 vais pensar nas regras do nome.

## 11. Adicionar: uma operação com contrato

As propriedades protegem o estado. Falta escrever as operações que dão sentido ao inventário: adicionar e retirar unidades. Antes de escrever uma operação, vamos escrever o que ela promete.

Um **contrato** de uma operação é uma descrição clara de quatro coisas: o que a operação recebe, o que devolve, quando falha, e o que acontece ao estado em cada caso. O contrato serve quem escreve o método, porque diz o que tem de ser programado, e serve quem o usa, porque diz o que pode esperar sem ter de ler o código.

O contrato de adicionar é este. Recebe o número de unidades a adicionar, que tem de ser um inteiro positivo. Não devolve nada. Falha, com `ValueError`, se as unidades não forem um inteiro ou não forem positivas, e nesse caso a quantidade fica exatamente como estava. Quando não falha, a quantidade aumenta o número de unidades pedido.

Em Python, o contrato fica escrito na docstring do método. Programa completo:

```python
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

O método começa por verificar o pedido, com duas verificações pela mesma ordem do setter: primeiro o tipo, depois o valor. Se uma delas falhar, o `raise` para o método antes da última linha, e a quantidade não é tocada.

A última linha, `self.quantidade = self.quantidade + unidades`, faz duas coisas. Do lado direito lê a quantidade, e essa leitura passa pelo getter. Do lado esquerdo escreve a nova quantidade, e essa escrita passa pelo setter. Somar um inteiro positivo a uma quantidade válida dá sempre uma quantidade válida, por isso o setter nunca recusa nada aqui. Mesmo assim, escrevemos na propriedade e não em `_quantidade`: se um dia a regra da quantidade mudar, adicionar passa a respeitá-la sem que seja preciso tocar neste método. A regra vive num só sítio.

Podias perguntar para que serve a verificação `unidades <= 0`, se o setter já protege a quantidade. Experimenta pensar em `caderno.adicionar(-3)` sem essa verificação: com 6 unidades, a conta daria 3, que é uma quantidade válida, e o setter aceitava-a. Um pedido para adicionar teria retirado três unidades, sem ninguém dar por isso. O setter protege o estado; não sabe nada sobre o significado do pedido. Quem conhece o significado do pedido é o método.

Quanto ao que devolve: um método que não tem `return` devolve `None`, um valor especial do Python que quer dizer "nada". É o que mostra a linha `O que adicionar devolveu: None`. No caderno 2, o `retirar` devolvia a quantidade que ficava. Aqui escolhemos outro contrato: o método não devolve nada, e quem quiser saber a quantidade consulta a propriedade. O nome de um método não diz o que ele devolve; quem o diz é o contrato, e é por isso que o contrato fica escrito.

## 12. Exemplo guiado: construir o método retirar

Vamos agora escrever o método `retirar`, a partir do contrato e usando o que já está na classe. Acompanha o raciocínio passo a passo, porque é o raciocínio, e não só o código final, que interessa.

### Passo 1: escrever o contrato

Recebe o número de unidades a retirar, que tem de ser um inteiro positivo. Não devolve nada. Falha, com `ValueError`, em três casos: se as unidades não forem um inteiro, se não forem positivas, ou se não houver unidades suficientes. Em qualquer dos três casos, a quantidade fica como estava. Quando não falha, a quantidade diminui o número de unidades pedido.

### Passo 2: separar regras do pedido e regras do estado

Das três razões para falhar, duas são sobre o pedido e uma é sobre o estado que resultaria dele.

"As unidades têm de ser um inteiro" e "as unidades têm de ser positivas" são regras sobre o pedido: dizem que pedidos fazem sentido, seja qual for a quantidade que existe.

"Tem de haver unidades suficientes" é, no fundo, uma regra sobre o estado. Se houver 4 unidades e alguém pedir 9, a nova quantidade seria 4 - 9 = -5. Não haver unidades suficientes é o mesmo que a nova quantidade ser negativa. E a classe já tem uma peça que recusa quantidades negativas: o setter.

### Passo 3: verificar o pedido no próprio método

Podíamos ser tentados a deixar tudo ao setter. Na secção 11 vimos, com o `adicionar`, que o setter protege o estado mas não conhece o significado do pedido, e no `retirar` passa-se o mesmo. Vejamos o que aconteceria, com 6 unidades, se o método fosse apenas a linha da subtração:

- `retirar(-3)` faria 6 - (-3) = 9. O setter aceitava 9, que é uma quantidade válida, e um pedido para retirar teria acrescentado três unidades;
- `retirar(0)` faria 6 - 0 = 6. O setter aceitava 6, e um pedido que a nossa regra recusa teria sido aceite em silêncio;
- `retirar("2")` tentaria subtrair um texto a um número, e o próprio Python pararia com um `TypeError`, em vez da nossa mensagem.

Nos três casos, o setter não tem culpa: o estado que recebe é válido, ou nem chega a recebê-lo. O problema está no pedido, e só o método sabe o que um pedido de retirada significa. Por isso, o método começa com as duas verificações do pedido, pela mesma ordem de sempre: primeiro o tipo, depois o valor.

### Passo 4: alterar através da propriedade

Depois de o pedido passar as duas verificações, fazemos a alteração escrevendo na propriedade:

```python partial
self.quantidade = self.quantidade - unidades
```

Esta linha é um excerto do método e não corre sozinha. Se houver unidades suficientes, o resultado é zero ou mais, o setter guarda-o, e o pedido foi cumprido. Se não houver, o resultado é negativo, e o setter lança `ValueError` antes de chegar à sua última linha, a que guarda o valor. Como o `_quantidade` não foi tocado, a quantidade fica como estava, exatamente como o contrato promete.

A decisão aqui é não repetir no `retirar` uma regra que já vive no setter. Se escrevêssemos a mesma regra em dois sítios, teríamos de nos lembrar de mudar os dois sempre que ela mudasse. Assim, a regra do estado está num só sítio, e o método ocupa-se apenas do que só ele sabe: o significado do pedido. A consequência é que, quando faltam unidades, a mensagem que se lê é a do setter, "A quantidade não pode ser negativa.", que explica a recusa: a quantidade ficaria negativa se o pedido fosse cumprido.

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

Programa completo, com a classe final deste caderno:

```python
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

Compara linha a linha com o traço do passo 5. O pedido de 2 foi aceite e deixou 4. Os três pedidos seguintes foram recusados: o de 9 pelo setter, e os de 0 e -3 pelo próprio método, cada um com a sua mensagem. As duas últimas linhas confirmam o que o contrato promete: depois de três recusas o caderno continua com 4, e a pasta, a quem nunca foi feito nenhum pedido, continua com 2.

Em todas as operações a ordem foi a mesma: verificar, alterar, responder. Verificar é o trabalho das condições do método e do setter. Alterar é a última linha do setter, a única que escreve em `_quantidade`. Responder é terminar sem erro, quando o pedido foi cumprido, ou lançar `ValueError`, quando foi recusado.

A interface pública do artigo ficou assim: `codigo` e `nome`, que ainda são atributos simples; a propriedade `quantidade`, para consultar e acertar; e os métodos `adicionar` e `retirar`. O atributo `_quantidade` é interno e fica fora da interface.

## 13. Agora experimenta

Todos os exercícios usam a classe final do passo 6 do exemplo guiado, exceto quando o enunciado diz outra coisa. Para cada excerto, copia esse programa completo e substitui as linhas que vêm depois da classe (a partir de `caderno = ...`) pelas linhas do exercício. Escreve sempre a tua previsão antes de executar, e entrega as respostas pelo meio indicado pelo professor.

### Exercício 1: Decidir antes de executar

Cada linha da tabela é um caso separado, que começa com um artigo acabado de criar: `artigo = Artigo("A07", "Marcador", 5)`. A última linha não usa esse artigo: cria um artigo novo.

| Instrução | Aceite ou recusada | Quem recusa: o método, o setter ou ninguém | Quantidade depois | Mensagem, se houver |
| --- | --- | --- | ---: | --- |
| `artigo.retirar(5)` | A completar | A completar | A completar | A completar |
| `artigo.adicionar(1.5)` | A completar | A completar | A completar | A completar |
| `artigo.quantidade = 7.0` | A completar | A completar | A completar | A completar |
| `artigo.quantidade = 0` | A completar | A completar | A completar | A completar |
| `artigo.retirar(2.0)` | A completar | A completar | A completar | A completar |
| `Artigo("A09", "Agrafador", 0)` | A completar | A completar | A completar | A completar |

Preenche a tabela primeiro e só depois escreve um programa que confirme cada caso, com um `try` e um `except` para cada instrução. Por fim, responde: 7.0 e 2.0 têm o valor de números inteiros, mas o Python recusa-os. Achas que a regra devia aceitá-los? Justifica a tua posição, pensando no que o inventário guarda.

### Exercício 2: Quantas vezes corre o setter

Excerto para colocar depois da classe final:

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

1. Quantas vezes é executado o setter da quantidade neste excerto? Para cada vez, indica que valor recebe e se o guarda ou lança uma exceção.
2. Há um pedido em que o setter não chega a ser executado. Qual é, e porquê?
3. Que linhas aparecem no ecrã, e por que ordem?

Para confirmares a resposta 1, acrescenta temporariamente esta linha no início do setter, logo a seguir à docstring, e executa: `print("setter recebeu", valor)`. Depois de confirmares, apaga-a.

### Exercício 3: Quando alguém ignora o sublinhado

Excerto para colocar depois da classe final:

```python partial
caderno = Artigo("A01", "Caderno", 6)
caderno._quantidade = -1
print(caderno.quantidade)
caderno.adicionar(3)
print(caderno.quantidade)
```

1. Antes de executar, escreve o que esperas ver nas duas linhas do ecrã.
2. Porque é que o Python aceitou a segunda linha do excerto?
3. Depois de `adicionar(3)`, a quantidade é válida. Isso quer dizer que o artigo esteve sempre num estado válido? Explica, usando a palavra invariante.
4. Numa frase, explica a diferença entre uma convenção e uma proteção, usando este excerto como exemplo.

### Exercício 4: Um erro de ordem

Um colega escreveu esta versão do `retirar`. É um excerto: para a experimentar, substitui o `retirar` da classe final por este.

```python partial
    def retirar(self, unidades):
        """Retira unidades ao artigo (versão com erro)."""
        if not isinstance(unidades, int):
            raise ValueError("As unidades a retirar têm de ser um número inteiro.")
        if unidades <= 0:
            raise ValueError("As unidades a retirar têm de ser 1 ou mais.")
        self._quantidade = self._quantidade - unidades
        if self._quantidade < 0:
            raise ValueError("Não há unidades suficientes.")
```

Com um caderno de 6 unidades, o colega chama `caderno.retirar(9)` dentro de um `try`, vê a mensagem "Não há unidades suficientes." e fica convencido de que o método funciona.

1. Que quantidade ficou guardada no caderno? Confirma executando.
2. Explica porque é que a mensagem de recusa não resolve o erro.
3. Há dois problemas nesta versão: um é a ordem das instruções e o outro é o sítio onde se escreve o valor. Explica os dois por palavras.
4. Escreve, por palavras, a ordem correta das decisões e da alteração.

### Exercício 5: O nome também tem regras

No projeto do inventário, o nome de um artigo não pode ser vazio. Com a classe final, `Artigo("A08", "", 3)` é aceite sem problemas.

1. Escreve o contrato de uma propriedade `nome`, com as quatro partes da secção 11: o que recebe, o que devolve quem a consulta, quando falha e o que acontece ao estado em cada caso.
2. Antes de escreveres o contrato, tens de tomar duas decisões que o exemplo não tomou por ti. Um nome só com espaços, como `"   "`, conta como vazio? E se alguém passar um número como nome, por exemplo `123`? Decide e justifica cada escolha numa frase.
3. Escreve a propriedade `nome`, com getter e setter, guardando o valor em `_nome`, e faz o construtor passar pelo setter. Se decidires que um nome só com espaços é vazio, vai-te ser útil saber que `"   Caneta ".strip()` dá `"Caneta"`: o método `strip` dos textos devolve o texto sem os espaços do início e do fim.
4. Testa a tua classe com um nome válido, com um nome vazio e com o caso da tua decisão na pergunta 2, mostrando em cada caso a mensagem ou o nome guardado.
5. Achas que o código do artigo também devia ser uma propriedade protegida? Com que regra? Pensa no que um artigo sozinho sabe e no que só um inventário, que conhece todos os artigos, poderia saber.

## Antes de passares ao caderno 4

Tenta responder a estas perguntas sem olhar para o texto. Se alguma te deixar com dúvidas, volta à secção indicada.

- Consegues explicar porque é que mostrar uma mensagem depois de guardar -3 não resolve nada? (secção 1)
- Consegues explicar a diferença entre juntar dados e métodos numa classe e ter encapsulamento? (secção 3)
- Consegues explicar porque é que `_quantidade` é privado só por convenção? (secção 6)
- Consegues dizer o que acontece às linhas que estão depois de um `raise`, e porque é que isso protege o estado? (secção 7)
- Consegues explicar porque é que o setter guarda o valor em `_quantidade` e não em `quantidade`? (secção 9)
- Consegues dizer que parte das regras do `retirar` é verificada pelo método e que parte é verificada pelo setter, e porquê? (secção 12)

No próximo caderno, os artigos deixam de estar sozinhos: um inventário vai reunir vários artigos e encaminhar pedidos para eles, e vais ver o que cabe a cada um fazer.

![Rodapé](../imagens/rodape.png)

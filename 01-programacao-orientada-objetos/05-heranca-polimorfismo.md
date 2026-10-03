![Cabeçalho](../imagens/cabecalho.png)

# Herança, polimorfismo e abstração: a mesma operação, maneiras diferentes de a realizar

*M10 · Caderno 5*

No caderno 4 estudámos a relação "tem": um inventário tem artigos, uma playlist tem músicas. Neste caderno estudamos a outra relação que aprendeste a distinguir, a relação "é um": um carro é um veículo, uma bicicleta também é um veículo. Em programação, esta relação escreve-se com a **herança**, e é dela que nascem duas ideias muito usadas em programação orientada a objetos, o polimorfismo e a abstração.

Para estudar estas ideias vamos sair do inventário e usar um exemplo à parte, o das notificações. Uma notificação é uma mensagem preparada para ser apresentada a alguém, como "Contagem concluída" ou "A02 esgotou". Há notificações que se apresentam de maneiras diferentes: umas só com o texto, outras com um aviso antes, outras com o nome de quem as enviou. Não vamos enviar mensagens a ninguém: os programas só preparam o texto de cada notificação e mostram-no no ecrã.

Porque um exemplo à parte? Porque o inventário não precisa de herança. Artigos e inventário relacionam-se por "tem", e forçar uma relação "é um" onde ela não existe estraga o modelo, como vais ver na secção 10. Um exemplo em que a relação "é um" é verdadeira permite estudar a herança sem deformar o que já construímos.

## Antes de começares

Este caderno usa o que aprendeste nos cadernos 2, 3 e 4: classes, construtor e `self`; a função `isinstance`, os decoradores como `@property`, as exceções como `ValueError`, tratadas com `try` e `except` (caderno 3, secções 7 e 8), o contrato de um método e o valor `None` (caderno 3, secções 11 e 12); as listas, o ciclo `for`, o operador `+` para juntar textos, a diferença entre "tem" e "é um", as duas árvores, as caixas e linhas da UML leve e a agregação da playlist (caderno 4, secção 12). Se alguma destas ideias estiver pouco firme, volta à secção indicada quando ela aparecer no texto. Tudo o resto é explicado aqui.

Os programas completos correm sozinhos, como nos cadernos anteriores: copia-os para um ficheiro `.py` e executa o ficheiro inteiro. Os excertos estão sempre assinalados. O [laboratório](05-heranca-polimorfismo-laboratorio.md) acompanha-te, passo a passo, na construção das notificações no computador, e a [ficha de exercícios](05-heranca-polimorfismo-exercicios.md) serve para praticares sozinho depois de estudares este caderno.

## 1. Duas classes quase iguais

Começamos com duas maneiras de apresentar uma notificação: a breve, que mostra só o texto, e a detalhada, que acrescenta "Aviso interno: " antes do texto. Escrevemos uma classe para cada uma, com o que já sabemos. Programa completo:

```python
class NotificacaoBreve:
    """Notificação que apresenta só o texto."""

    def __init__(self, texto):
        """Guarda o texto da notificação."""
        self.texto = texto

    def apresentar(self):
        """Devolve o texto tal como está guardado."""
        return self.texto


class NotificacaoDetalhada:
    """Notificação que apresenta o texto com um aviso antes."""

    def __init__(self, texto):
        """Guarda o texto da notificação."""
        self.texto = texto

    def apresentar(self):
        """Devolve o texto com "Aviso interno: " antes."""
        return "Aviso interno: " + self.texto


breve = NotificacaoBreve("Contagem concluída")
detalhada = NotificacaoDetalhada("Contagem concluída")

print(breve.apresentar())
print(detalhada.apresentar())
```

O programa mostra:

```text
Contagem concluída
Aviso interno: Contagem concluída
```

O programa funciona, mas olha para as duas classes lado a lado. Os construtores são exatamente iguais: recebem um texto e guardam-no no atributo `texto`. Os dois métodos chamam-se `apresentar`, não recebem nada além do `self` e devolvem um texto. A única diferença está numa linha: a forma como o método `apresentar` constrói o texto que devolve.

Esta repetição tem dois custos. O primeiro já o conheces do caderno 3: uma regra escrita em dois sítios. Se amanhã decidirmos que o texto de uma notificação não pode ser vazio, temos de acrescentar a mesma verificação aos dois construtores, e a cada construtor de cada variante nova que aparecer. Basta esquecer um para o programa ficar incoerente.

O segundo custo é menos visível. Para nós, as duas classes descrevem notificações. Para o Python, são duas classes sem nenhuma relação, que por acaso têm métodos com o mesmo nome. Não há nada no programa que diga "uma notificação breve e uma notificação detalhada são as duas notificações". Não há um sítio onde fique escrito o que todas as notificações têm e sabem fazer, nem uma classe comum a que se possa perguntar, com o `isinstance` do caderno 3, se um objeto é uma notificação. E quem escrever uma terceira variante tem de adivinhar, a partir das outras duas, o que ela deve ter.

O que as duas classes têm em comum é geral: todas as notificações têm um texto e sabem apresentar-se. O que as distingue é particular: cada uma apresenta-se à sua maneira. É esta separação entre o geral e o particular que vamos escrever a seguir.

## 2. Especialização: do geral para o particular

Diz as frases em voz alta, como aprendeste no caderno 4, secção 3:

- "Uma notificação breve é uma notificação." Verdadeira.
- "Uma notificação detalhada é uma notificação." Verdadeira.

Aplica também o teste mais cuidadoso: se A é um B, tudo o que B tem e faz tem de fazer sentido para A. Uma notificação tem um texto e sabe apresentar-se. Uma notificação breve tem um texto e sabe apresentar-se; uma detalhada também. O teste passa nas duas.

Chamamos **especialização** a esta relação entre um tipo geral e um tipo particular: o tipo particular é um caso do geral, conserva tudo o que o geral descreve e acrescenta ou concretiza alguma coisa. A notificação detalhada conserva o texto e a capacidade de se apresentar, e concretiza a maneira de o fazer, com o aviso antes.

Podemos desenhar a relação com uma árvore de especialização, igual à dos veículos do caderno 4, secção 4:

```text
Notificacao
├── NotificacaoBreve
└── NotificacaoDetalhada
```

Lê-se de baixo para cima com "é um": `NotificacaoBreve` é uma `Notificacao`. Em cima está o tipo geral e em baixo os tipos particulares. Os nomes estão escritos como nomes de classes Python, sem espaços nem acentos, porque vão ser isso mesmo.

Este vocabulário vai aparecer muitas vezes:

| Termo | O que quer dizer | No exemplo |
| --- | --- | --- |
| Classe base, ou superclasse | A classe geral, de onde as outras partem | `Notificacao` |
| Classe derivada, ou subclasse | A classe particular, definida a partir da base | `NotificacaoBreve`, `NotificacaoDetalhada` |
| Herdar | Receber da classe base os atributos e os métodos que ela descreve | As duas derivadas herdam o texto e o construtor |

## 3. Herança em Python

A **herança** é o mecanismo que permite definir uma classe a partir de outra. A classe derivada recebe da classe base todos os seus métodos, incluindo o construtor, e pode acrescentar métodos novos ou substituir os que recebeu por versões suas. Em Python, a herança escreve-se pondo o nome da classe base entre parênteses, a seguir ao nome da classe derivada:

```python partial
class NotificacaoBreve(Notificacao):
```

Esta linha é um excerto e lê-se "a classe `NotificacaoBreve`, que é uma `Notificacao`". Vejamos o exemplo da secção 1 reescrito com herança. Programa completo:

```python
class Notificacao:
    """Uma mensagem preparada para ser apresentada a alguém."""

    def __init__(self, texto):
        """Guarda o texto da notificação."""
        self.texto = texto

    def apresentar(self):
        """Devolve o texto da notificação, pronto a mostrar."""
        return self.texto


class NotificacaoBreve(Notificacao):
    """Notificação que apresenta só o texto: faz tudo como a classe base."""


class NotificacaoDetalhada(Notificacao):
    """Notificação que apresenta o texto com um aviso antes."""

    def apresentar(self):
        """Devolve o texto com "Aviso interno: " antes."""
        return "Aviso interno: " + self.texto


breve = NotificacaoBreve("Contagem concluída")
detalhada = NotificacaoDetalhada("Material em falta")

print(breve.texto)
print(detalhada.texto)
print(breve.apresentar())
print(detalhada.apresentar())

print(isinstance(breve, NotificacaoBreve))
print(isinstance(breve, Notificacao))
print(isinstance(breve, NotificacaoDetalhada))
```

O programa mostra:

```text
Contagem concluída
Material em falta
Contagem concluída
Aviso interno: Material em falta
True
True
False
```

Vamos ler o programa por partes.

A classe `Notificacao` é uma classe como as que já escreveste: tem um construtor, que guarda o texto, e um método `apresentar`, que devolve o texto. É aqui que fica escrito tudo o que é comum a todas as notificações.

A classe `NotificacaoBreve(Notificacao)` só tem a docstring. Não escreve construtor nem métodos, e mesmo assim os seus objetos têm um texto e sabem apresentar-se: herdaram tudo da classe base. Em Python, o corpo de uma classe não pode ficar vazio, e a docstring conta como conteúdo; é por isso que esta classe pode ter só a docstring.

A classe `NotificacaoDetalhada(Notificacao)` escreve só o método `apresentar`, com a sua maneira de apresentar. O construtor, esse, herda-o da base.

A linha `breve = NotificacaoBreve("Contagem concluída")` cria um objeto da classe derivada. O Python procura o construtor `__init__` na classe `NotificacaoBreve`, não o encontra e usa o da classe base, com `self` a apontar para o objeto novo. É por isso que `breve.texto` existe e vale "Contagem concluída". O mesmo acontece com a notificação detalhada, que também herda o construtor.

As três últimas linhas usam a função `isinstance` do caderno 3, secção 5. Lá perguntava se um valor era um número inteiro; aqui pergunta se um objeto é de uma certa classe. A notificação breve é uma `NotificacaoBreve`, como esperávamos. É também uma `Notificacao`, e é esta a resposta que mostra a herança: o Python sabe que um objeto de uma classe derivada é, ao mesmo tempo, um objeto da classe base. E não é uma `NotificacaoDetalhada`, porque as duas classes derivadas são "irmãs": ambas são notificações, mas nenhuma é a outra.

Há um erro típico a evitar. Herdar não quer dizer partilhar valores. As duas notificações do programa têm textos diferentes, e duas notificações breves também podem ter textos diferentes, tal como dois artigos da mesma classe têm quantidades diferentes. A herança é uma relação entre classes: diz que a descrição da classe derivada inclui a descrição da base. Os valores continuam a pertencer a cada objeto.

### A herança em UML

No diagrama de classes, a herança desenha-se com uma linha que sai da classe derivada e termina num **triângulo vazio** encostado à classe base. O triângulo aponta sempre para a classe mais geral:

![Diagrama: Notificacao, com o atributo texto e o método apresentar(); por baixo, NotificacaoBreve, sem nada nas zonas de atributos e métodos, e NotificacaoDetalhada, com o método apresentar(); de cada uma sai uma linha que termina num triângulo vazio encostado a Notificacao](../imagens/uml-heranca-notificacoes.svg)

Repara no que cada caixa derivada mostra. A caixa de `NotificacaoBreve` tem as duas zonas vazias, porque a classe não acrescenta nem muda nada: tudo o que tem vem da base, e isso já está dito pelo triângulo. A caixa de `NotificacaoDetalhada` mostra `apresentar()`, porque a classe escreve a sua própria versão desse método. As caixas derivadas mostram só o que acrescentam ou mudam.

Não confundas o triângulo com o losango do caderno 4. O losango fica encostado ao todo e diz "tem". O triângulo fica encostado à classe base e diz "é um". São relações diferentes, e por isso têm pontas diferentes.

## 4. Redefinir um método: onde o Python procura

A classe `NotificacaoDetalhada` recebeu da base um método `apresentar`, mas escreveu o seu. Quando uma classe derivada escreve um método com o mesmo nome de um método da base, dizemos que o **redefine**. Em inglês diz-se *override*, e vais encontrar a palavra em muitos textos.

Para perceber o que acontece numa chamada, é preciso saber onde é que o Python vai buscar o método. A regra é esta: quando se chama um método sobre um objeto, o Python procura-o primeiro na classe do objeto. Se o encontrar lá, usa esse. Se não o encontrar, procura na classe base. Se também não estiver na base, procura na base da base, e assim por diante.

Aplicada às chamadas do programa da secção 3:

| Chamada | Classe do objeto | Essa classe escreve `apresentar`? | Onde o Python encontra o método | Resultado |
| --- | --- | --- | --- | --- |
| `breve.apresentar()` | `NotificacaoBreve` | Não | Na classe base, `Notificacao` | `Contagem concluída` |
| `detalhada.apresentar()` | `NotificacaoDetalhada` | Sim | Na própria classe | `Aviso interno: Material em falta` |

O mesmo vale para o construtor. `NotificacaoDetalhada("Material em falta")` procura `__init__` na classe `NotificacaoDetalhada`, não o encontra e usa o da base.

Redefinir não apaga o método da base. O `apresentar` da classe `Notificacao` continua lá, e continua a ser usado pelas notificações breves, que não o redefiniram. A versão da classe derivada só tapa a da base para os objetos da classe derivada.

Falta uma pergunta. Quando `breve.apresentar()` executa o método escrito na classe `Notificacao`, quem é o `self`? É a notificação breve, o objeto que está antes do ponto, exatamente como aprendeste no caderno 2. O método foi escrito na base, mas trabalha sobre o objeto que recebeu o pedido. É por isso que `self.texto` devolve o texto desta notificação, e não um texto "geral" que não existe.

## 5. Acrescentar dados numa classe derivada: `super()`

Até agora, as classes derivadas só mudaram a maneira de apresentar. Mas uma especialização também pode acrescentar dados. Imagina uma notificação que diz, no fim, quem a enviou: "Encomenda recebida (enviada por: Secretaria)". Além do texto, precisa de guardar a origem, e por isso o construtor tem de receber dois valores. Programa completo:

```python
class Notificacao:
    """Uma mensagem preparada para ser apresentada a alguém."""

    def __init__(self, texto):
        """Guarda o texto da notificação."""
        self.texto = texto

    def apresentar(self):
        """Devolve o texto da notificação, pronto a mostrar."""
        return self.texto


class NotificacaoAssinada(Notificacao):
    """Notificação que diz, no fim, quem a enviou."""

    def __init__(self, texto, origem):
        """Guarda o texto, através do construtor da classe base, e a origem."""
        super().__init__(texto)
        self.origem = origem

    def apresentar(self):
        """Devolve o texto seguido da origem, entre parênteses."""
        return self.texto + " (enviada por: " + self.origem + ")"


assinada = NotificacaoAssinada("Encomenda recebida", "Secretaria")

print(assinada.texto)
print(assinada.origem)
print(assinada.apresentar())
```

O programa mostra:

```text
Encomenda recebida
Secretaria
Encomenda recebida (enviada por: Secretaria)
```

A classe `NotificacaoAssinada` redefine o construtor, porque precisa de um parâmetro a mais. Pela regra da secção 4, o construtor da classe derivada tapa o da base: quando se cria uma notificação assinada, é este `__init__` que é executado, e o da base não é executado sozinho. Mas o construtor da base sabe fazer uma parte do trabalho, guardar o texto, e queremos aproveitá-lo.

É isso que faz a linha `super().__init__(texto)`. `super()` dá acesso às versões da classe base dos métodos, para este mesmo objeto. A linha lê-se "executa o construtor da classe base, com este texto, sobre este objeto". Depois dela, o objeto já tem o atributo `texto`, guardado exatamente como a base o guarda. A linha seguinte acrescenta o que é próprio da notificação assinada, a origem.

Podias perguntar porque não escrevemos simplesmente `self.texto = texto` no construtor da classe derivada. Hoje funcionaria. Mas pensa no que acontece se, amanhã, o construtor da base passar a verificar que o texto não é vazio, com um `ValueError`, como fizemos com a quantidade no caderno 3. As notificações assinadas saltariam essa verificação, porque nunca passariam pelo construtor da base. Com `super().__init__(texto)`, qualquer regra que a base venha a ter também se aplica às classes derivadas. É outra vez a ideia de a regra viver num só sítio.

E se te esqueceres da linha do `super()`? O construtor da classe derivada é executado, guarda a origem e termina. O da base nunca é executado, e o objeto fica sem o atributo `texto`. Nada se queixa no momento da criação. O erro só aparece mais tarde, quando algum método tentar usar o texto, com uma última linha como esta:

```text
AttributeError: 'NotificacaoAssinada' object has no attribute 'texto'
```

É o tipo de erro do caderno 3, secção 1: aparece longe da causa. A mensagem diz que falta o texto, mas o engano está no construtor, onde faltou chamar a base. Quando a classe base tem um construtor e a classe derivada escreve o seu, a primeira linha do construtor da derivada deve ser, quase sempre, a chamada `super().__init__(...)`, com os valores de que o construtor da base precisa. Se a classe base não escrever construtor nenhum, não há nenhum construtor da base para aproveitar, e essa linha não faz falta.

## 6. Polimorfismo: a mesma chamada, comportamentos diferentes

Temos agora três variantes de notificação, todas derivadas da mesma base. Vamos guardá-las numa lista e apresentá-las todas. Programa completo:

```python
class Notificacao:
    """Uma mensagem preparada para ser apresentada a alguém."""

    def __init__(self, texto):
        """Guarda o texto da notificação."""
        self.texto = texto

    def apresentar(self):
        """Devolve o texto da notificação, pronto a mostrar."""
        return self.texto


class NotificacaoBreve(Notificacao):
    """Notificação que apresenta só o texto: faz tudo como a classe base."""


class NotificacaoDetalhada(Notificacao):
    """Notificação que apresenta o texto com um aviso antes."""

    def apresentar(self):
        """Devolve o texto com "Aviso interno: " antes."""
        return "Aviso interno: " + self.texto


class NotificacaoAssinada(Notificacao):
    """Notificação que diz, no fim, quem a enviou."""

    def __init__(self, texto, origem):
        """Guarda o texto, através do construtor da classe base, e a origem."""
        super().__init__(texto)
        self.origem = origem

    def apresentar(self):
        """Devolve o texto seguido da origem, entre parênteses."""
        return self.texto + " (enviada por: " + self.origem + ")"


avisos = [
    NotificacaoBreve("Contagem concluída"),
    NotificacaoDetalhada("Material em falta"),
    NotificacaoAssinada("Encomenda recebida", "Secretaria"),
]

for aviso in avisos:
    print(aviso.apresentar())
```

O programa mostra:

```text
Contagem concluída
Aviso interno: Material em falta
Encomenda recebida (enviada por: Secretaria)
```

A lista é escrita de uma maneira que talvez ainda não tenhas visto: os três objetos são criados dentro dos parênteses retos, separados por vírgulas, um por linha. É o mesmo que criar a lista vazia e fazer três `append`, só que mais curto. Repara também na vírgula depois do último objeto. É opcional: o Python aceita a lista com ela ou sem ela. Escreve-se para que, quando se acrescenta mais um elemento numa linha nova, não seja preciso mexer na linha de cima para lhe pôr a vírgula.

Olha agora para o ciclo. Tem uma única linha de trabalho, `print(aviso.apresentar())`, e essa linha é exatamente a mesma nas três voltas. Mesmo assim, cada volta produz um resultado de forma diferente, porque o nome `aviso` aponta, em cada volta, para um objeto de uma classe diferente, e o Python encontra, pela regra da secção 4, o `apresentar` dessa classe:

| Volta | `aviso` aponta para um objeto da classe | `apresentar` usado | Resultado |
| --- | --- | --- | --- |
| 1 | `NotificacaoBreve` | O da base, `Notificacao` | `Contagem concluída` |
| 2 | `NotificacaoDetalhada` | O de `NotificacaoDetalhada` | `Aviso interno: Material em falta` |
| 3 | `NotificacaoAssinada` | O de `NotificacaoAssinada` | `Encomenda recebida (enviada por: Secretaria)` |

Chamamos **polimorfismo** a esta capacidade: o mesmo pedido, feito da mesma maneira, funciona com objetos de classes diferentes, e cada objeto responde à sua maneira. A palavra vem do grego e quer dizer "muitas formas". O ciclo não sabe, nem precisa de saber, de que variante é cada notificação. Só conta com que cada uma saiba apresentar-se.

Há um pormenor do Python que convém saberes desde já. Quando executa `aviso.apresentar()`, o Python não pergunta se o objeto é uma `Notificacao`. Limita-se a procurar um método chamado `apresentar`, pela regra da secção 4: primeiro na classe do objeto, depois nas classes de onde ela herda. Por isso, este mesmo ciclo também funcionaria com as duas classes soltas da secção 1, sem herança nenhuma, desde que cada uma tivesse o seu `apresentar`. Em Python, o que o polimorfismo exige é que cada objeto saiba responder ao pedido que lhe fazem.

Então, o que ganhámos com a herança? Ganhámos o que faltava na secção 1. O código comum, como o construtor, está escrito uma só vez, na classe base, e uma regra que lá se acrescente vale para todas as variantes. Há um tipo comum, `Notificacao`, que o `isinstance` reconhece, que o diagrama mostra e que diz, num só sítio, o que todas as notificações têm e sabem fazer. E, como vais ver na secção 8, a classe base pode passar a obrigar cada variante a escrever o seu `apresentar`, o que duas classes soltas nunca conseguiriam garantir.

Para perceberes o que o polimorfismo poupa, compara com a maneira de fazer o mesmo sem ele. Este excerto depende das classes do programa acima e mostra o ciclo escrito por alguém que decide, ele próprio, como apresentar cada variante:

```python partial
for aviso in avisos:
    if isinstance(aviso, NotificacaoDetalhada):
        print("Aviso interno: " + aviso.texto)
    elif isinstance(aviso, NotificacaoAssinada):
        print(aviso.texto + " (enviada por: " + aviso.origem + ")")
    else:
        print(aviso.texto)
```

Mostra o mesmo, mas tem três problemas. O primeiro é que a forma de apresentar cada variante saiu da classe e veio parar ao ciclo, que passou a ter uma responsabilidade que não é dele: é a pergunta "quem sabe o quê?" do caderno 4, secção 2. O segundo é que cada variante nova obriga a mudar este ciclo, e todos os outros sítios do programa que apresentem notificações. O terceiro é que é fácil esquecer um caso: uma variante nova que ninguém acrescentou à cadeia cai no `else` e é apresentada como breve, sem nenhum erro a avisar. Com polimorfismo, uma variante nova é uma classe nova, e o ciclo não muda uma única linha. O exemplo guiado da secção 9 vai mostrar isso mesmo.

## 7. O contrato comum

O polimorfismo só funciona se todas as variantes cumprirem a mesma promessa. Ter um método com o nome certo não chega. O ciclo da secção 6 conta com três coisas: que `apresentar` possa ser chamado sem argumentos, que devolva um texto e que não mude a notificação.

Tal como fizemos no caderno 3 para `adicionar` e `retirar`, escrevemos o contrato de `apresentar`:

> `apresentar()` não recebe nada além do `self`, devolve um texto pronto a mostrar e não altera a notificação. Não mostra nada no ecrã: quem decide o que fazer com o texto é quem o pediu.

A última frase é a divisão de tarefas do caderno 3, secção 8, e do caderno 4, secção 11. A notificação prepara o texto; quem o recebe decide se o mostra no terminal, numa página web ou noutro sítio qualquer.

Vejamos o que acontece quando uma variante tem o nome certo mas não cumpre o contrato. Programa completo:

```python
class Notificacao:
    """Uma mensagem preparada para ser apresentada a alguém."""

    def __init__(self, texto):
        """Guarda o texto da notificação."""
        self.texto = texto

    def apresentar(self):
        """Devolve o texto da notificação, pronto a mostrar."""
        return self.texto


class NotificacaoBreve(Notificacao):
    """Notificação que apresenta só o texto: faz tudo como a classe base."""


class NotificacaoMalFeita(Notificacao):
    """Variante que não cumpre o contrato: mostra o texto em vez de o devolver."""

    def apresentar(self):
        """Mostra o texto no ecrã (e por isso não devolve nada)."""
        print("AVISO: " + self.texto)


avisos = [
    NotificacaoBreve("Contagem concluída"),
    NotificacaoMalFeita("Material em falta"),
]

for aviso in avisos:
    print(aviso.apresentar())
```

O programa mostra:

```text
Contagem concluída
AVISO: Material em falta
None
```

A primeira linha está certa. A segunda foi escrita pelo próprio método `apresentar` da variante mal feita, com o seu `print`. A terceira é o `print` do ciclo a mostrar o que o método devolveu: como o método não tem `return`, devolveu `None`, o "nada" do Python que conheceste no caderno 3, secção 11. O ciclo não tem culpa. Fez exatamente o mesmo pedido que fazia às outras variantes; foi a variante que não cumpriu o que prometia. Num programa que mostrasse as notificações numa página web, o `print` da variante não apareceria em lado nenhum, e a página mostraria "None".

Há outras maneiras de quebrar o contrato com o nome certo. Uma variante cujo `apresentar` devolvesse o texto e depois o apagasse, com `self.texto = ""`, funcionaria na primeira chamada e devolveria um texto vazio na segunda: mudou o estado, e o contrato diz que não muda. Uma variante cujo `apresentar` exigisse um argumento obrigatório faria o ciclo parar com um erro na chamada `aviso.apresentar()`.

A ideia de fundo tem nome: **princípio da substituição**. Um objeto de uma classe derivada tem de poder ser usado em qualquer sítio onde se espera um objeto da classe base, sem surpresas para quem o usa. É o teste "é um" do caderno 4, aplicado ao comportamento, e não só aos dados. Uma classe que tem o nome certo, herda da base certa e mesmo assim não cumpre o contrato continua a ser uma `Notificacao` para o Python: o `isinstance` dá `True`. Quem a usa é que é apanhado de surpresa, porque ela não se comporta como as outras notificações. O `isinstance` só olha para a herança, e cumprir o contrato fica a cargo de quem escreve cada variante.

## 8. Abstração, classes abstratas e o módulo `abc`

### Abstrair é escolher o essencial

**Abstração** é escolher o que é essencial para o problema e deixar de fora o resto. Já o fizeste várias vezes. No caderno 1, quando decidimos que um artigo tem código, nome e quantidade, que não se faz uma ficha por cada caderno físico e que a cor das paredes da sala não entra no programa, estávamos a abstrair: "representar um problema é sempre escolher o que interessa".

Na classe `Notificacao`, o essencial é que todas as notificações têm um texto e sabem apresentar-se. A maneira de se apresentarem não é essencial à ideia de notificação: é um pormenor de cada variante.

### O problema da nossa classe base

Olha outra vez para a classe `Notificacao` que usámos até aqui. O seu `apresentar` devolve só o texto. Isso levanta dois problemas.

O primeiro é que se pode criar uma notificação "geral", com `Notificacao("Contagem concluída")`, e ela apresenta-se da maneira breve. Mas uma notificação geral não tem uma maneira definida de se apresentar. A maneira breve é uma das variantes, e só foi parar à base porque era a mais simples de escrever.

O segundo é que nada obriga uma variante nova a escrever o seu `apresentar`. Se alguém criar uma variante e se esquecer do método, a variante apresenta-se como breve, sem nenhum aviso. É o mesmo tipo de esquecimento silencioso do `else` da secção 6.

### Classe abstrata e método abstrato

Uma **classe abstrata** é uma classe que descreve o que é comum a um grupo de classes, mas que não serve para criar objetos diretamente. Serve de base às classes derivadas, que são as que se usam para criar objetos. Às classes de onde se podem criar objetos chamamos **classes concretas**.

Um **método abstrato** é um método declarado numa classe abstrata com o nome e o contrato, mas sem instruções. Diz "todas as classes derivadas têm de saber fazer isto", sem dizer como. Cada classe derivada concreta tem de o escrever.

No nosso exemplo, `Notificacao` deve ser uma classe abstrata, e `apresentar` deve ser um método abstrato.

### Como se escreve em Python

O Python não tem uma palavra-chave própria para "abstrato". Usa um módulo que vem com a própria linguagem, o módulo `abc`. A sigla vem do inglês *Abstract Base Classes*, "classes base abstratas". Programa completo, com a base abstrata e as três variantes:

```python
from abc import ABC, abstractmethod


class Notificacao(ABC):
    """Uma mensagem preparada para ser apresentada a alguém.

    Classe abstrata: diz o que todas as notificações têm (um texto) e o que
    todas sabem fazer (apresentar-se), mas não diz como se apresentam.
    Não se criam objetos desta classe; criam-se objetos das variantes.
    """

    def __init__(self, texto):
        """Guarda o texto da notificação."""
        self.texto = texto

    @abstractmethod
    def apresentar(self):
        """Contrato: não recebe nada além do self, devolve um texto pronto
        a mostrar e não altera a notificação. Cada variante escreve como."""


class NotificacaoBreve(Notificacao):
    """Notificação que apresenta só o texto."""

    def apresentar(self):
        """Devolve o texto tal como está guardado."""
        return self.texto


class NotificacaoDetalhada(Notificacao):
    """Notificação que apresenta o texto com um aviso antes."""

    def apresentar(self):
        """Devolve o texto com "Aviso interno: " antes."""
        return "Aviso interno: " + self.texto


class NotificacaoAssinada(Notificacao):
    """Notificação que diz, no fim, quem a enviou."""

    def __init__(self, texto, origem):
        """Guarda o texto, através do construtor da classe base, e a origem."""
        super().__init__(texto)
        self.origem = origem

    def apresentar(self):
        """Devolve o texto seguido da origem, entre parênteses."""
        return self.texto + " (enviada por: " + self.origem + ")"


class NotificacaoEsquecida(Notificacao):
    """Variante que se esqueceu de escrever o método apresentar."""


try:
    geral = Notificacao("Contagem concluída")
except TypeError:
    print("Não se pode criar um objeto da classe abstrata Notificacao.")

try:
    esquecida = NotificacaoEsquecida("Contagem concluída")
except TypeError:
    print("Nem de uma variante que não escreveu o método apresentar.")

breve = NotificacaoBreve("Contagem concluída")
print(breve.apresentar())
print(isinstance(breve, Notificacao))
```

O programa mostra:

```text
Não se pode criar um objeto da classe abstrata Notificacao.
Nem de uma variante que não escreveu o método apresentar.
Contagem concluída
True
```

Vamos ler as partes novas uma a uma.

A primeira linha, `from abc import ABC, abstractmethod`, vai buscar ao módulo `abc` duas ferramentas: `ABC` e `abstractmethod`. Um **módulo** é um ficheiro de código Python que outros programas podem usar; este já vem instalado com o Python. Não confundas com os módulos da disciplina, como o M10 que estás a estudar: são duas coisas diferentes que têm o mesmo nome. A linha lê-se "do módulo `abc`, importa `ABC` e `abstractmethod`". Depois dela, os dois nomes podem ser usados no resto do programa.

A linha `class Notificacao(ABC):` diz que `Notificacao` herda de `ABC`. É a herança que acabaste de aprender, usada para uma coisa útil: `ABC` é uma classe que o Python fornece, e herdar dela é o que dá a `Notificacao` a capacidade de ter métodos abstratos. Esta herança não pode faltar. Sem ela, o decorador `@abstractmethod`, que vamos ver a seguir, não tem efeito nenhum: o Python deixa criar objetos da classe base e das variantes que se esqueceram do método, sem nenhum aviso, e o `apresentar` sem instruções devolve `None`.

A linha `@abstractmethod`, antes do `def apresentar`, é um decorador, como o `@property` do caderno 3, secção 9. Marca o método que vem a seguir como abstrato. O corpo do método tem só a docstring, que é o contrato. Não tem instruções, porque não há uma maneira geral de apresentar uma notificação: cada variante escreve a sua. Tal como numa classe, a docstring chega para o corpo de um método não ficar vazio.

Repara que a classe abstrata não está vazia: tem um construtor concreto, que guarda o texto, e que todas as variantes herdam. Abstrata não quer dizer vazia. Quer dizer incompleta de propósito: há uma parte, o método abstrato, que só as classes derivadas completam.

Agora, os dois `try`. Quando se tenta criar um objeto da classe abstrata, com `Notificacao("Contagem concluída")`, o Python recusa e lança uma exceção do tipo `TypeError`. É outro tipo de exceção, que se apanha da mesma maneira que o `ValueError`, com um `except` que diz o tipo. Se a exceção não fosse apanhada, o programa parava, e a última linha do traceback, em inglês, diria que não é possível criar um objeto da classe abstrata `Notificacao` porque o método abstrato `apresentar` não foi escrito. O texto exato dessa mensagem muda de uma versão do Python para outra; nas versões mais recentes começa por `TypeError: Can't instantiate abstract class Notificacao without an implementation for abstract method 'apresentar'`.

A segunda recusa é a mais útil. `NotificacaoEsquecida` é uma classe derivada que não escreveu o `apresentar`. Por isso continua a ter um método abstrato por completar, e é, ela também, uma classe abstrata: o Python recusa criar objetos dela. Lembras-te do segundo problema da nossa base antiga, a variante que se esquece do método e se apresenta como breve sem ninguém dar por isso? Desapareceu. O esquecimento passa a ser detetado no momento em que se tenta criar o objeto, e não muito mais tarde, quando alguém repara que as mensagens estão a sair com o formato errado. Um erro que aparece o mais cedo possível, perto da causa, é muito mais fácil de corrigir.

Por fim, a notificação breve cria-se sem problemas e apresenta-se como antes. Repara que, nesta versão, `NotificacaoBreve` tem de escrever o seu próprio `apresentar`: a base deixou de ter uma versão concreta para ela herdar.

### A classe abstrata em UML

Em UML, o nome de uma classe abstrata escreve-se em itálico, e o de um método abstrato também. Como o itálico é difícil de fazer à mão, acrescenta-se muitas vezes a indicação `{abstract}` por baixo do nome da classe:

![Diagrama: Notificacao, com o nome em itálico e {abstract}, o atributo texto e o método apresentar() em itálico; por baixo, NotificacaoBreve, NotificacaoDetalhada e NotificacaoAssinada, esta com o atributo origem, todas com o método apresentar(); as três ligam-se a Notificacao por linhas que se juntam num triângulo vazio](../imagens/uml-notificacao-abstrata.svg)

Quando há várias classes derivadas da mesma base, as linhas costumam juntar-se numa só antes de chegar ao triângulo, como neste desenho. Significa exatamente o mesmo que três linhas com três triângulos: cada uma das três classes é uma `Notificacao`.

### Escrever o contrato abstrato no papel

Não precisas de código para descrever uma classe abstrata. Chega dizer o que todas as classes derivadas têm e o que cada uma tem de concretizar. Uma forma possível, organizada por indentação, como no pseudocódigo:

```text
Classe abstrata Notificacao
    Todas têm: um texto, guardado quando a notificação é criada
    Todas sabem: apresentar()   (abstrato: cada variante escreve como)
        não recebe nada
        devolve um texto pronto a mostrar
        não altera a notificação e não mostra nada no ecrã
```

Não há uma forma única de o escrever. O que conta é que se perceba o que é comum a todas as variantes e o que cada uma tem de completar, com o contrato do método abstrato por inteiro.

## 9. Exemplo guiado: acrescentar uma variante nova

O responsável do armário da sala quer que os avisos de material esgotado chamem a atenção. Pede uma notificação que se apresente com "URGENTE: " antes do texto, e com o texto todo em maiúsculas. Vamos acrescentá-la ao programa da secção 8, acompanhando o raciocínio de cada passo.

### Passo 1: confirmar a relação "é um"

"Uma notificação urgente é uma notificação." Tem um texto e sabe apresentar-se. O teste de substituição também passa, se tivermos o cuidado de cumprir o contrato: onde se usa uma notificação qualquer, deve poder usar-se uma urgente. A nova classe vai, portanto, herdar de `Notificacao`.

### Passo 2: decidir o que muda

A notificação urgente não precisa de dados novos: só do texto, que a base já guarda. Por isso não precisa de construtor próprio, nem de `super()`: herda o construtor da base, como a breve e a detalhada. O que muda é só a maneira de se apresentar, e é isso que vamos escrever. Como `apresentar` é abstrato na base, somos obrigados a escrevê-lo; se nos esquecêssemos, a classe seria abstrata e não conseguiríamos criar notificações urgentes, como vimos na secção 8.

### Passo 3: cumprir o contrato

Para pôr o texto em maiúsculas, os textos do Python têm um método, `upper`: `"A02 esgotou".upper()` devolve `"A02 ESGOTOU"`. O ponto importante para o nosso contrato é este: `upper` devolve um texto novo, e o texto original fica como estava. Os textos do Python nunca mudam depois de criados: nenhum método dos textos muda o texto original, e os que produzem um texto, como o `strip` que aparece no exercício 5 do caderno 3 e este `upper`, devolvem um texto novo.

Isso permite-nos cumprir a regra "não altera a notificação". O método vai devolver `"URGENTE: " + self.texto.upper()`, que é um texto novo, e o atributo `texto` continua com as minúsculas originais. Se escrevêssemos `self.texto = self.texto.upper()` dentro do método, estaríamos a mudar o estado, e o contrato seria quebrado.

### Passo 4: escrever a classe

Excerto, que se acrescenta ao programa da secção 8, depois das outras variantes, e não corre sozinho:

```python partial
class NotificacaoUrgente(Notificacao):
    """Notificação que pede atenção imediata: o texto aparece em maiúsculas."""

    def apresentar(self):
        """Devolve "URGENTE: " seguido do texto em maiúsculas, sem alterar o texto guardado."""
        return "URGENTE: " + self.texto.upper()
```

### Passo 5: prever as chamadas antes de executar

Vamos pôr uma notificação de cada variante numa lista e apresentá-las com o mesmo ciclo da secção 6. Antes de executar, prevemos, para cada volta, a classe do objeto, o `apresentar` que o Python vai usar e o resultado:

| Volta | Objeto | `apresentar` usado | Resultado previsto |
| --- | --- | --- | --- |
| 1 | `NotificacaoBreve("Contagem concluída")` | O de `NotificacaoBreve` | `Contagem concluída` |
| 2 | `NotificacaoDetalhada("Material em falta")` | O de `NotificacaoDetalhada` | `Aviso interno: Material em falta` |
| 3 | `NotificacaoAssinada("Encomenda recebida", "Secretaria")` | O de `NotificacaoAssinada` | `Encomenda recebida (enviada por: Secretaria)` |
| 4 | `NotificacaoUrgente("A02 esgotou")` | O de `NotificacaoUrgente` | `URGENTE: A02 ESGOTOU` |

Na versão abstrata, cada variante escreve o seu `apresentar`, e por isso a coluna do meio aponta sempre para a própria classe. Nenhuma chamada usa o `apresentar` da base, que é abstrato e não tem instruções.

Prevemos também uma linha extra, que confirma o contrato: depois de apresentada, a notificação urgente continua a guardar o texto "A02 esgotou", em minúsculas.

### Passo 6: executar e comparar

Programa completo:

```python
from abc import ABC, abstractmethod


class Notificacao(ABC):
    """Uma mensagem preparada para ser apresentada a alguém.

    Classe abstrata: diz o que todas as notificações têm (um texto) e o que
    todas sabem fazer (apresentar-se), mas não diz como se apresentam.
    Não se criam objetos desta classe; criam-se objetos das variantes.
    """

    def __init__(self, texto):
        """Guarda o texto da notificação."""
        self.texto = texto

    @abstractmethod
    def apresentar(self):
        """Contrato: não recebe nada além do self, devolve um texto pronto
        a mostrar e não altera a notificação. Cada variante escreve como."""


class NotificacaoBreve(Notificacao):
    """Notificação que apresenta só o texto."""

    def apresentar(self):
        """Devolve o texto tal como está guardado."""
        return self.texto


class NotificacaoDetalhada(Notificacao):
    """Notificação que apresenta o texto com um aviso antes."""

    def apresentar(self):
        """Devolve o texto com "Aviso interno: " antes."""
        return "Aviso interno: " + self.texto


class NotificacaoAssinada(Notificacao):
    """Notificação que diz, no fim, quem a enviou."""

    def __init__(self, texto, origem):
        """Guarda o texto, através do construtor da classe base, e a origem."""
        super().__init__(texto)
        self.origem = origem

    def apresentar(self):
        """Devolve o texto seguido da origem, entre parênteses."""
        return self.texto + " (enviada por: " + self.origem + ")"


class NotificacaoUrgente(Notificacao):
    """Notificação que pede atenção imediata: o texto aparece em maiúsculas."""

    def apresentar(self):
        """Devolve "URGENTE: " seguido do texto em maiúsculas, sem alterar o texto guardado."""
        return "URGENTE: " + self.texto.upper()


avisos = [
    NotificacaoBreve("Contagem concluída"),
    NotificacaoDetalhada("Material em falta"),
    NotificacaoAssinada("Encomenda recebida", "Secretaria"),
    NotificacaoUrgente("A02 esgotou"),
]

for aviso in avisos:
    print(aviso.apresentar())

print("Texto guardado na urgente:", avisos[3].texto)
```

O programa mostra:

```text
Contagem concluída
Aviso interno: Material em falta
Encomenda recebida (enviada por: Secretaria)
URGENTE: A02 ESGOTOU
Texto guardado na urgente: A02 esgotou
```

As quatro primeiras linhas coincidem com a coluna "Resultado previsto" do passo 5. A última confirma o contrato: o texto guardado continua em minúsculas, porque `upper` devolveu um texto novo e o atributo não foi tocado. `avisos[3]` é o quarto elemento da lista, porque os índices começam em 0, como viste no caderno 4.

Agora repara no que não mudou. O ciclo `for` é, letra a letra, o da secção 6. Para acrescentar uma maneira nova de apresentar notificações, escrevemos uma classe nova e não tocámos em nenhuma linha do código que as usa. É isto que o polimorfismo permite, e é a resposta ao segundo problema da cadeia de `if` da secção 6.

## 10. Herança ou composição

### Duas maneiras de reaproveitar

Tens agora duas maneiras de construir uma classe a partir de outras. A herança diz "é um": a classe derivada é um caso particular da base e recebe tudo o que ela descreve. A composição, no sentido largo do caderno 4, secção 7, diz "tem": o objeto guarda outros objetos e usa-os para fazer o seu trabalho.

A decisão começa, como sempre, pela frase em voz alta. Só há herança se a frase "A é um B" for verdadeira e se A puder cumprir tudo o que B promete, isto é, se passar o teste de substituição da secção 7. Quando houver dúvida, a composição é quase sempre a escolha mais segura. Um objeto que guarda outro pode trocá-lo mais tarde por outro diferente, e não fica obrigado a receber atributos e métodos que não fazem sentido para ele, que é o que acontece com uma herança mal escolhida.

### Heranças sem sentido

Estes três exemplos parecem razoáveis à primeira vista e estão todos errados:

- `class Inventario(Artigo):`. A frase "um inventário é um artigo" é falsa, como viste no caderno 4, secção 3. Com esta herança, o inventário receberia a propriedade `quantidade` e os métodos `adicionar(unidades)` e `retirar(unidades)`, que não fazem sentido para um conjunto de artigos: retirar 2 unidades de quê?
- `class Inventario(Notificacao):`, com o argumento de que o inventário também produz avisos. O inventário usaria notificações, mas não é uma. Com esta herança, teria um atributo `texto` e um método `apresentar`, e ninguém saberia dizer que texto é esse. A relação certa seria "o inventário tem uma caixa de avisos", uma composição.
- `class Caderno(Artigo):` e `class Pasta(Artigo):`. A frase "um caderno é um artigo" até é verdadeira, mas o caderno 2, secção 4, já mostrou que estas classes não fazem falta: cadernos e pastas guardam os mesmos dados e aceitam as mesmas operações. Uma classe derivada só se justifica quando acrescenta ou muda alguma coisa. Uma árvore de classificação não obriga a criar classes, como avisámos no caderno 4, secção 4.

O inventário dos cadernos 3 e 4 não usa herança nenhuma, e está bem assim. Um programa não fica melhor por usar herança. Fica melhor quando cada relação é a certa.

### As duas relações no mesmo programa

Para veres a herança e a composição a trabalhar juntas, vamos criar uma caixa de avisos: um objeto que recebe notificações de qualquer variante e devolve as suas apresentações, pela ordem de chegada. Programa completo, com as classes do passo 6:

```python
from abc import ABC, abstractmethod


class Notificacao(ABC):
    """Uma mensagem preparada para ser apresentada a alguém.

    Classe abstrata: diz o que todas as notificações têm (um texto) e o que
    todas sabem fazer (apresentar-se), mas não diz como se apresentam.
    Não se criam objetos desta classe; criam-se objetos das variantes.
    """

    def __init__(self, texto):
        """Guarda o texto da notificação."""
        self.texto = texto

    @abstractmethod
    def apresentar(self):
        """Contrato: não recebe nada além do self, devolve um texto pronto
        a mostrar e não altera a notificação. Cada variante escreve como."""


class NotificacaoBreve(Notificacao):
    """Notificação que apresenta só o texto."""

    def apresentar(self):
        """Devolve o texto tal como está guardado."""
        return self.texto


class NotificacaoDetalhada(Notificacao):
    """Notificação que apresenta o texto com um aviso antes."""

    def apresentar(self):
        """Devolve o texto com "Aviso interno: " antes."""
        return "Aviso interno: " + self.texto


class NotificacaoAssinada(Notificacao):
    """Notificação que diz, no fim, quem a enviou."""

    def __init__(self, texto, origem):
        """Guarda o texto, através do construtor da classe base, e a origem."""
        super().__init__(texto)
        self.origem = origem

    def apresentar(self):
        """Devolve o texto seguido da origem, entre parênteses."""
        return self.texto + " (enviada por: " + self.origem + ")"


class NotificacaoUrgente(Notificacao):
    """Notificação que pede atenção imediata: o texto aparece em maiúsculas."""

    def apresentar(self):
        """Devolve "URGENTE: " seguido do texto em maiúsculas, sem alterar o texto guardado."""
        return "URGENTE: " + self.texto.upper()


class CaixaDeAvisos:
    """Reúne notificações já criadas e devolve as suas apresentações.

    Agrega notificações de qualquer variante. Só precisa de saber que todas
    cumprem o contrato de apresentar; não sabe, nem precisa de saber, de que
    variante é cada uma.
    """

    def __init__(self):
        """Cria uma caixa vazia."""
        self._avisos = []

    def receber(self, notificacao):
        """Junta à caixa uma notificação criada fora dela."""
        self._avisos.append(notificacao)

    def textos(self):
        """Devolve uma lista com a apresentação de cada notificação, pela ordem de chegada."""
        resultado = []
        for aviso in self._avisos:
            resultado.append(aviso.apresentar())
        return resultado


caixa = CaixaDeAvisos()
caixa.receber(NotificacaoBreve("Contagem concluída"))
caixa.receber(NotificacaoUrgente("A02 esgotou"))
caixa.receber(NotificacaoAssinada("Encomenda recebida", "Secretaria"))

for linha in caixa.textos():
    print(linha)
```

O programa mostra:

```text
Contagem concluída
URGENTE: A02 ESGOTOU
Encomenda recebida (enviada por: Secretaria)
```

A classe `CaixaDeAvisos` usa as duas relações ao mesmo tempo, e cada uma no seu lugar.

A caixa tem notificações. As notificações são criadas fora dela, no programa principal, e entregues já feitas ao método `receber`, tal como as músicas da playlist do caderno 4, secção 12. É uma agregação: a notificação faz sentido sem a caixa, e não é a caixa que a cria.

Cada variante é uma notificação. É a herança, com o triângulo apontado para a classe abstrata.

E o método `textos` usa o polimorfismo: pede a cada notificação que se apresente, com a mesma linha para todas, sem perguntar de que variante é. A caixa não conhece `NotificacaoBreve`, nem `NotificacaoUrgente`, nem nenhuma outra variante. Só conta com o contrato que a classe `Notificacao` fixa para todas: cada notificação sabe apresentar-se. Por isso, uma variante que venha a ser escrita no próximo ano também cabe na caixa, sem mudar uma linha da classe `CaixaDeAvisos`.

O diagrama mostra as duas relações:

![Diagrama: CaixaDeAvisos, com os métodos receber(notificacao) e textos(), ligada à classe abstrata Notificacao por uma linha com um losango vazio junto da caixa e 0..* nas duas pontas; por baixo de Notificacao, as quatro variantes, ligadas a ela por linhas que se juntam num triângulo vazio](../imagens/uml-caixa-de-avisos.svg)

Repara onde chega a linha do losango: à classe `Notificacao`, e não a cada variante. É assim que o diagrama diz o que acabámos de ver no código. A caixa trabalha com qualquer notificação, e o triângulo diz quais são as notificações que existem hoje. As multiplicidades `0..*` dizem que uma caixa pode ter qualquer número de notificações e que a mesma notificação pode ser entregue a mais do que uma caixa, porque as notificações são criadas fora delas.

Se um dia o inventário precisasse de avisar quando um artigo esgota, poderia ter uma caixa de avisos, guardada num atributo seu, e entregar-lhe uma `NotificacaoUrgente` sempre que a quantidade de um artigo chegasse a zero. Seria uma composição no sentido largo: o inventário tem uma caixa de avisos. Não o vamos fazer, porque o inventário deste módulo não precisa, mas é assim que as duas partes deste caderno se ligariam ao que construíste no caderno 4.

### As quatro linhas do diagrama de classes

Com este caderno, ficas a conhecer as quatro ligações da UML leve que usamos neste módulo:

![Diagrama com quatro linhas entre uma caixa A e uma caixa B: associação, uma linha simples, A conhece ou usa B; agregação, losango vazio junto de A, A tem B e B existe sem A; composição, losango cheio junto de A, A tem B e B só existe dentro de A; herança, triângulo vazio junto de B, A é um B](../imagens/uml-tipos-de-relacao.svg)

Os losangos encostam ao todo e dizem "tem". O triângulo encosta à classe base e diz "é um". A linha simples diz só que os objetos se conhecem ou se usam, sem dizer mais nada. Antes de escolheres uma destas pontas, diz a frase em voz alta.

## Antes de passares ao caderno 6

Tenta responder a estas perguntas sem olhar para o texto. Se alguma te deixar com dúvidas, volta à secção indicada.

- Consegues explicar os dois custos de ter duas classes quase iguais sem herança? (secção 1)
- Consegues dizer o que uma classe derivada herda e o que acontece quando se cria um objeto de uma classe derivada que não escreveu construtor? (secção 3)
- Consegues explicar porque é que `isinstance(breve, Notificacao)` dá `True`? (secção 3)
- Consegues dizer onde é que o Python procura um método, e por que ordem? (secção 4)
- Consegues explicar o que faz `super().__init__(texto)` e o que acontece se for esquecido? (secção 5)
- Consegues explicar o que é o polimorfismo usando o ciclo da secção 6, dizer o que ele poupa em relação à cadeia de `if` e o que a herança acrescenta a esse ciclo? (secção 6)
- Consegues escrever o contrato de `apresentar` e dar um exemplo de uma variante que o quebra? (secção 7)
- Consegues explicar o que é uma classe abstrata, porque é que não se criam objetos dela e o que o Python faz a uma variante que se esquece do método abstrato? (secção 8)
- Consegues prever o resultado de cada volta do ciclo do exemplo guiado, dizendo o `apresentar` que o Python usa? (secção 9)
- Consegues dar um exemplo de herança sem sentido e dizer a relação certa? (secção 10)

No [laboratório](05-heranca-polimorfismo-laboratorio.md) vais construir as notificações no computador, passo a passo, provocar de propósito os erros deste caderno e criar duas variantes tuas. Na [ficha de exercícios](05-heranca-polimorfismo-exercicios.md) vais praticar sozinho a leitura de hierarquias, a previsão de chamadas, a escolha entre herança e composição e a escrita de contratos.

No módulo seguinte, M11, vais reencontrar estas ideias em JavaScript. As palavras mudam um pouco, mas as perguntas são as mesmas: é um ou tem? Que promete o método? Onde vive cada regra?

![Rodapé](../imagens/rodape.png)

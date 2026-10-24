![Cabeçalho](../imagens/cabecalho.png)

# Herança e polimorfismo

Módulo M10, Introdução à Programação Orientada por Objetos. Neste guia aprendes a escrever em Python a relação "é um", com a herança, e as duas ideias que nascem dela: o polimorfismo e a abstração. Lês o guia ao teu ritmo, de preferência em mais do que uma vez, e o que não acabares na aula acabas em casa ou na aula seguinte. Para praticar, há o [laboratório](05-heranca-polimorfismo-laboratorio.md) e a [ficha de exercícios](05-heranca-polimorfismo-exercicios.md) deste tema.

Sobre duas classes podem fazer-se duas perguntas: "uma tem a outra?" e "uma é um caso da outra?". A primeira é a relação "tem": um inventário tem artigos, e uma playlist, a lista de músicas que alguém escolhe numa aplicação de música, tem músicas. É o assunto do guia 04, [Composição e modelação](04-composicao-modelacao.md). Este guia trata da segunda, a relação "é um": um carro é um veículo, e uma bicicleta também é um veículo. Em programação, esta relação escreve-se com a **herança**. Dela nascem duas ideias muito usadas na programação orientada a objetos: o polimorfismo e a abstração.

Este guia usa algumas ideias do guia 04. Se ainda não o leste, não faz mal. Cada ideia do guia 04 que aqui se usa explica-se em poucas linhas, no sítio onde aparece pela primeira vez. A lista está em "O que já sabes e vais usar", com a secção do guia 04 onde podes saber mais.

Para estudar estas ideias vamos sair do inventário e usar um exemplo à parte, o das notificações. Uma notificação é uma mensagem preparada para ser apresentada a alguém, como "Contagem concluída" ou "A02 esgotou". Há notificações que se apresentam de maneiras diferentes: umas só com o texto, outras com um aviso antes, outras com o nome de quem as enviou. Não vamos enviar mensagens a ninguém. Os programas só preparam o texto de cada notificação e mostram-no no ecrã.

Porque um exemplo à parte? Porque o inventário não precisa de herança. Artigos e inventário relacionam-se por "tem", e forçar uma relação "é um" onde ela não existe estraga o modelo, como vais ver em "Herança ou composição". Um exemplo em que a relação "é um" é verdadeira permite estudar a herança sem deformar o que já construímos.

Os programas completos correm sozinhos, como nos guias anteriores: copia-os para um ficheiro `.py` e executa o ficheiro inteiro, no editor de Python que usas nas aulas. Funcionam com o Python 3, a partir da versão 3.10. Cada execução começa do zero, com os valores escritos no programa. Os excertos estão sempre assinalados, e o texto diz de que outro código dependem.

## Neste guia

1. O que vais aprender
2. O que já sabes e vais usar
3. Duas classes quase iguais
4. Especialização: do geral para o particular
5. Herança em Python
6. Redefinir um método: onde o Python procura
7. Acrescentar dados numa classe derivada: `super()`
8. Polimorfismo: a mesma chamada, comportamentos diferentes
9. O contrato comum
10. Abstração e classes abstratas
11. Herança ou composição
12. Exemplo guiado: acrescentar uma variante nova
13. Erros frequentes
14. Palavras novas deste guia
15. Verificar o que aprendeste
16. O que vem a seguir

## O que vais aprender

No fim deste guia, consegues:

- explicar porque é que duas classes quase iguais são um problema;
- confirmar uma relação "é um" pela análise do seu significado e pelo teste do "tudo o que B tem e faz";
- escrever em Python uma classe derivada, que herda de uma classe base, redefine um método e, quando guarda dados novos, chama o construtor da base com `super()`;
- dizer onde é que o Python procura um método, e prever o resultado de cada chamada;
- explicar o polimorfismo com um ciclo que faz o mesmo pedido a objetos de classes diferentes, e escrever o contrato que todos têm de cumprir;
- explicar o que são uma classe abstrata e um método abstrato, e escrever o contrato de uma classe abstrata no papel e na docstring da classe base;
- decidir entre herança e composição, e justificar a escolha com a frase "é um" ou "tem".

## O que já sabes e vais usar

- Classe, instância, o construtor `__init__` e a chamada de um método com o ponto. Estão no guia [02 Objetos, classes e instâncias](02-objetos-classes-instancias.md), de "Classe: a descrição comum" a "O método retirar em Python".
- O `self`, que é o objeto que está antes do ponto na chamada: guia [02](02-objetos-classes-instancias.md), em "A classe Artigo em Python".
- Uma classe nova só se justifica quando os objetos têm dados ou operações diferentes. Por isso não há uma classe `Caderno` e outra `Pasta`. Guia [02](02-objetos-classes-instancias.md), em "Classe: a descrição comum".
- Representar um problema é escolher o que interessa e deixar de fora o resto: guia [01 Entidades, estado e ações](01-entidades-estado-acoes.md), em "A informação que interessa guardar".
- A docstring, o texto entre três aspas que explica uma função, uma classe ou um método: guia [01](01-entidades-estado-acoes.md), em "Duas maneiras de organizar um programa".
- Os três tipos de erro (de escrita, de execução e de lógica), o `TypeError` (o erro de tipo) e o erro que aparece longe da causa. Estão no guia [03 Encapsulamento e contratos](03-encapsulamento-contratos.md), em "Nada impede uma quantidade impossível".
- A função `isinstance` (do inglês *is instance*, "é instância de"), que pergunta se um valor é de um certo tipo: guia [03](03-encapsulamento-contratos.md), em "Primeiro passo: métodos get e set".
- O sublinhado no início de um nome, como em `_quantidade`, que avisa que o nome é interno da classe: guia [03](03-encapsulamento-contratos.md), em "O sublinhado: um atributo privado por convenção".
- A exceção `ValueError`, lançada com `raise`, e a mensagem de erro que se lê de baixo para cima: guia [03](03-encapsulamento-contratos.md), em "Recusar a sério: `ValueError` e `raise`".
- O `try` e o `except`, e a divisão de tarefas. Quem lança a exceção decide se o pedido é válido, e quem a apanha decide o que fazer com a recusa. Guia [03](03-encapsulamento-contratos.md), em "Tratar a recusa: `try` e `except`".
- Uma regra escrita num só sítio, para não ter de a mudar em dois: guia [03](03-encapsulamento-contratos.md), no passo 4 de "Exemplo guiado: construir o método retirar".
- O contrato de uma operação: o que recebe, o que devolve, quando falha e o que acontece ao estado. E o valor `None`, que um método sem `return` devolve. Guia [03](03-encapsulamento-contratos.md), em "Adicionar: uma operação com contrato".
- As listas, com o `append`, o índice a contar de 0 e o `len`, e o ciclo `for`: do 10.º ano. O guia 04 recorda-os em "Recordar as listas e o ciclo `for`".
- As condições com `if`, `elif` e `else`, e as funções com `def` e `return`: do 10.º ano.
- O texto entre aspas, o `+` que junta textos e o `print` com vários valores: do 10.º ano.

Do guia [04 Composição e modelação](04-composicao-modelacao.md), este guia usa as ideias seguintes. Se ainda não o leste, cada uma explica-se aqui, em poucas linhas, onde aparece pela primeira vez. Para saber mais, lê a secção indicada do guia 04.

- A relação "tem" e a relação "é um", com o teste "se A é um B, tudo o que B tem e faz tem de fazer sentido para A". Aqui, em "Especialização: do geral para o particular". Para saber mais: "Duas perguntas sobre duas classes: "tem" e "é um"".
- A árvore de especialização, que se lê de baixo para cima com "é um". Aqui, na mesma secção. Para saber mais: "Duas árvores que se parecem e dizem coisas diferentes".
- "Quem sabe o quê": cada tarefa fica com a classe que tem a informação para a fazer. Aqui, em "Polimorfismo: a mesma chamada, comportamentos diferentes". Para saber mais: "Quem sabe o quê: responsabilidades".
- A composição no sentido largo e os dois graus de "tem", a composição e a agregação. Aqui, em "Herança ou composição". Para saber mais: "Dois graus de "tem": composição e agregação".
- O modelo, a descrição das classes de um programa e das relações entre elas, escrita antes do código. Aqui, em "Abstração e classes abstratas". Para saber mais: "O inventário descrito por palavras".
- Um objeto que guarda numa lista outros objetos, criados fora dele, e o acumulador. Aqui, no passo 7 do exemplo guiado. Para saber mais: "Agregação em Python: a playlist e as músicas".

## Duas classes quase iguais

Começamos com duas maneiras de apresentar uma notificação: a breve, que mostra só o texto, e a detalhada, que acrescenta "Aviso interno: " antes do texto. Escrevemos uma classe para cada uma, com o que já sabemos. É um programa completo.

Antes de correres, tenta prever as duas linhas que o programa mostra.

```python
# Duas notificações escritas sem herança: o primeiro programa do guia 05.

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

Leitura guiada: começa pelas duas classes, de cima para baixo. Cada uma tem um construtor, que guarda o texto, e um método `apresentar`, que devolve um texto. Depois lê as quatro linhas do programa principal. As duas primeiras criam uma notificação de cada classe, com o mesmo texto. As duas últimas mostram o que cada uma devolve quando lhe pedimos que se apresente.

O programa funciona, mas olha para as duas classes lado a lado. Os construtores são exatamente iguais: recebem um texto e guardam-no no atributo `texto`. Os dois métodos chamam-se `apresentar`, não recebem nada além do `self` e devolvem um texto. A única diferença está numa linha: a forma como o método `apresentar` constrói o texto que devolve.

Esta repetição tem dois custos. O primeiro já o conheces do guia 03: uma regra escrita em dois sítios. Imagina que amanhã decidimos que o texto de uma notificação não pode ser vazio. Temos de acrescentar a mesma verificação aos dois construtores, e ao construtor de cada variante nova que aparecer. Basta esquecer um para o programa ficar incoerente.

O segundo custo é menos visível. Para nós, as duas classes descrevem notificações. Para o Python, são duas classes sem nenhuma relação, que por acaso têm métodos com o mesmo nome. Nada no programa diz que uma notificação breve e uma notificação detalhada são as duas notificações. Não há um sítio onde fique escrito o que todas as notificações têm e sabem fazer. Também não há uma classe comum a que se possa perguntar, com o `isinstance` do guia 03, se um objeto é uma notificação. E quem escrever uma terceira variante tem de adivinhar, a partir das outras duas, o que ela deve ter.

O que as duas classes têm em comum é geral: todas as notificações têm um texto e sabem apresentar-se. O que as distingue é particular: cada uma apresenta-se à sua maneira. É esta separação entre o geral e o particular que vamos escrever a seguir.

## Especialização: do geral para o particular

Antes de escrevermos o que é comum, temos de dizer que relação há entre as classes. Sobre duas classes podem fazer-se duas perguntas diferentes.

A primeira é "uma tem a outra?". Um inventário tem artigos. Uma turma tem alunos. É a relação **"tem"**, entre um todo e as partes que ele guarda e usa.

A segunda é "uma é um caso da outra?". Um carro é um veículo. Uma bicicleta também é um veículo. É a relação **"é um"**, entre um tipo particular e um tipo mais geral. Tudo o que é verdade para qualquer veículo, como deslocar-se de um sítio para outro, também é verdade para um carro.

Ter coisas lá dentro não faz de ninguém uma dessas coisas: uma mochila tem cadernos, mas não é um caderno. Para decidir, analisa a relação entre as duas classes e verifica se a frase é verdadeira. O guia 04 trata da relação "tem" com pormenor, em "Duas perguntas sobre duas classes: "tem" e "é um"". Este guia trata da relação "é um".

Analisa as relações entre os tipos de notificação:

- "Uma notificação breve é uma notificação." Verdadeira.
- "Uma notificação detalhada é uma notificação." Verdadeira.

Às vezes a frase "é um" parece quase verdadeira, e é preciso um teste mais cuidadoso. O teste é este: se A é um B, então tudo o que um B tem e tudo o que um B faz tem de fazer sentido para A. Uma notificação tem um texto e sabe apresentar-se. Uma notificação breve tem um texto e sabe apresentar-se, e uma detalhada também. O teste passa nas duas.

Vê também um caso em que o teste falha: "um inventário é um artigo". Um artigo tem uma quantidade e aceita o pedido "retirar 2 unidades". O inventário tem artigos com quantidades de materiais diferentes, e não há um número que seja "a quantidade do inventário". Retirar 2 unidades de um inventário, sem dizer de que artigo, não quer dizer nada. O teste falha, e por isso o inventário não é um artigo: tem artigos.

Chamamos **especialização** a esta relação entre um tipo geral e um tipo particular. O tipo particular é um caso do geral: conserva tudo o que o geral descreve, e acrescenta ou concretiza alguma coisa. A notificação detalhada conserva o texto e a capacidade de se apresentar, e concretiza a maneira de o fazer, com o aviso antes.

Podemos desenhar a relação com uma **árvore de especialização**, também chamada árvore de classificação ou hierarquia de especialização. Cada ramo liga um tipo geral a um tipo mais particular:

```text
Notificacao
├── NotificacaoBreve
└── NotificacaoDetalhada
```

Lê-se de baixo para cima, com a frase "é um": `NotificacaoBreve` é uma `Notificacao`. Em cima está o tipo geral, e em baixo os tipos particulares. Tudo o que o tipo de cima descreve continua a ser verdade para os de baixo. Os nomes estão escritos como nomes de classes Python, sem espaços nem acentos, porque vão ser isso mesmo. Há outras árvores parecidas que dizem outra coisa, como a das partes de um todo, que se lê de cima para baixo com "tem". O guia 04 compara as duas em "Duas árvores que se parecem e dizem coisas diferentes".

Este vocabulário vai aparecer muitas vezes:

| Termo | O que quer dizer | No exemplo |
| --- | --- | --- |
| Classe base, ou superclasse | A classe geral, de onde as outras partem | `Notificacao` |
| Classe derivada, ou subclasse | A classe particular, definida a partir da base | `NotificacaoBreve`, `NotificacaoDetalhada` |
| Herdar | Receber da classe base os seus métodos, incluindo o construtor | As duas derivadas herdam o construtor, que dá a cada objeto o seu texto, e o método `apresentar` |

## Herança em Python

A **herança** é o mecanismo que permite definir uma classe a partir de outra. A classe derivada recebe da classe base todos os seus métodos, incluindo o construtor. Pode acrescentar métodos novos, ou substituir os que recebeu por versões suas. Em Python, a herança escreve-se pondo o nome da classe base entre parênteses, a seguir ao nome da classe derivada:

```python partial
class NotificacaoBreve(Notificacao):
```

Esta linha é um excerto e não corre sozinha. Lê-se "a classe `NotificacaoBreve`, que é uma `Notificacao`". Vejamos o exemplo de "Duas classes quase iguais" reescrito com herança. É um programa completo.

Antes de correres, tenta prever as sete linhas. Repara sobretudo nas três últimas, que perguntam de que classe é a notificação breve.

```python
# A classe base Notificacao e duas classes derivadas: o segundo programa do guia 05.

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

Leitura guiada: começa pelas três classes, de cima para baixo, e repara no que cada uma escreve e no que não escreve. Depois lê o programa principal, em três grupos: duas criações, quatro linhas que mostram textos e três perguntas com `isinstance`.

A classe `Notificacao` é uma classe como as que já escreveste. Tem um construtor, que guarda o texto, e um método `apresentar`, que devolve o texto. É aqui que fica escrito tudo o que é comum a todas as notificações.

A classe `NotificacaoBreve(Notificacao)` só tem a docstring. Não escreve construtor nem métodos, e mesmo assim os seus objetos têm um texto e sabem apresentar-se: herdaram tudo da classe base. Em Python, o corpo de uma classe não pode ficar vazio, e a docstring conta como conteúdo. É por isso que esta classe pode ter só a docstring.

A classe `NotificacaoDetalhada(Notificacao)` escreve só o método `apresentar`, com a sua maneira de apresentar. O construtor, esse, herda-o da base.

A linha `breve = NotificacaoBreve("Contagem concluída")` cria um objeto da classe derivada. O Python procura o construtor `__init__` na classe `NotificacaoBreve`, não o encontra e usa o da classe base, com o `self` a apontar para o objeto novo. É por isso que `breve.texto` existe e vale "Contagem concluída". O mesmo acontece com a notificação detalhada, que também herda o construtor.

As três últimas linhas usam a função `isinstance` do guia 03. Lá perguntava se um valor era um número inteiro; aqui pergunta se um objeto é de uma certa classe. A notificação breve é uma `NotificacaoBreve`, como esperávamos. É também uma `Notificacao`, e é esta resposta que mostra a herança. O Python sabe que um objeto de uma classe derivada é, ao mesmo tempo, um objeto da classe base. E a breve não é uma `NotificacaoDetalhada`, porque as duas classes derivadas são "irmãs": ambas são notificações, mas nenhuma é a outra.

Há um erro típico a evitar: pensar que herdar quer dizer partilhar valores. As duas notificações do programa têm textos diferentes. Duas notificações breves também podem ter textos diferentes, tal como dois artigos da mesma classe têm quantidades diferentes. A herança é uma relação entre classes: diz que a descrição da classe derivada inclui a descrição da base. Os valores continuam a pertencer a cada objeto.

## Redefinir um método: onde o Python procura

A classe `NotificacaoDetalhada` recebeu da base um método `apresentar`, mas escreveu o seu. Quando uma classe derivada escreve um método com o mesmo nome de um método da base, dizemos que o **redefine**. Em inglês diz-se *override*, "sobrepor", e vais encontrar a palavra em muitos textos.

Para perceber o que acontece numa chamada, é preciso saber onde é que o Python vai buscar o método. A regra é esta. Quando se chama um método sobre um objeto, o Python procura-o primeiro na classe do objeto. Se o encontrar lá, usa esse. Se não o encontrar, procura na classe base. Se também não estiver na base, procura na base da base, e assim por diante.

Aplicada às chamadas do programa de "Herança em Python":

| Chamada | Classe do objeto | Essa classe escreve `apresentar`? | Onde o Python encontra o método | Resultado |
| --- | --- | --- | --- | --- |
| `breve.apresentar()` | `NotificacaoBreve` | Não | Na classe base, `Notificacao` | `Contagem concluída` |
| `detalhada.apresentar()` | `NotificacaoDetalhada` | Sim | Na própria classe | `Aviso interno: Material em falta` |

O mesmo vale para o construtor. `NotificacaoDetalhada("Material em falta")` procura `__init__` na classe `NotificacaoDetalhada`, não o encontra e usa o da base.

Redefinir não apaga o método da base. O `apresentar` da classe `Notificacao` continua lá, e continua a ser usado pelas notificações breves, que não o redefiniram. A versão da classe derivada só tapa a da base para os objetos da classe derivada.

Falta uma pergunta. Quando `breve.apresentar()` executa o método escrito na classe `Notificacao`, quem é o `self`? É a notificação breve, o objeto que está antes do ponto, exatamente como aprendeste no guia 02. O método foi escrito na base, mas trabalha sobre o objeto que recebeu o pedido. É por isso que `self.texto` devolve o texto desta notificação, e não um texto "geral" que não existe.

## Acrescentar dados numa classe derivada: `super()`

Até agora, as classes derivadas só mudaram a maneira de apresentar. Mas uma especialização também pode acrescentar dados. Imagina uma notificação que diz, no fim, quem a enviou: "Encomenda recebida (enviada por: Secretaria)". Além do texto, precisa de guardar a origem, e por isso o construtor tem de receber dois valores. É um programa completo.

Antes de correres, tenta prever as três linhas.

```python
# Uma classe derivada com um dado novo e super(): o terceiro programa do guia 05.

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

Leitura guiada: começa pelo construtor da classe `NotificacaoAssinada`, que é a parte nova, e lê as suas duas linhas por ordem. Depois lê o `apresentar`, que junta três textos com o `+`. No programa principal, a criação passa dois valores, e as três linhas mostram o texto, a origem e a apresentação.

A classe `NotificacaoAssinada` redefine o construtor, porque precisa de um parâmetro a mais. Pela regra de "Redefinir um método: onde o Python procura", o construtor da classe derivada tapa o da base. Quando se cria uma notificação assinada, é este `__init__` que é executado, e o da base não é executado sozinho. Mas o construtor da base sabe fazer uma parte do trabalho, guardar o texto, e queremos aproveitá-lo.

É isso que faz a linha `super().__init__(texto)`. O `super()` dá acesso às versões da classe base dos métodos, para este mesmo objeto. O nome vem de superclasse, o outro nome da classe base. A linha lê-se "executa o construtor da classe base, com este texto, sobre este objeto". Depois dela, o objeto já tem o atributo `texto`, guardado exatamente como a base o guarda. A linha seguinte acrescenta o que é próprio da notificação assinada, a origem.

Repara em duas maneiras diferentes de escrever `__init__`. Para criar uma notificação assinada, escreves o nome da classe, `NotificacaoAssinada("Encomenda recebida", "Secretaria")`, e não `__init__`: é o Python que chama o construtor, como no guia 02. A linha `super().__init__(texto)` é outra coisa. Está dentro de um construtor, e serve para esse construtor pedir ao da base que faça a sua parte, sobre o mesmo objeto.

E quando é que uma classe derivada escreve o seu próprio `__init__`? Quando tem de fazer, na criação, alguma coisa que o construtor da base não faz, como guardar a origem. Se não tiver nada a acrescentar, não o escreve, e herda o da base. É o caso da notificação breve e da detalhada.

Podias perguntar porque não escrevemos simplesmente `self.texto = texto` no construtor da classe derivada. Hoje funcionaria. Mas imagina que, amanhã, o construtor da base passa a verificar que o texto não é vazio, com um `ValueError`, como o setter do guia 03 verifica a quantidade. As notificações assinadas saltariam essa verificação, porque nunca passariam pelo construtor da base. Com `super().__init__(texto)`, qualquer regra que a base venha a ter também se aplica às classes derivadas. É outra vez a ideia de a regra viver num só sítio.

E se te esqueceres da linha do `super()`? O construtor da classe derivada é executado, guarda a origem e termina. O da base nunca é executado, e o objeto fica sem o atributo `texto`. Nada se queixa no momento da criação. O erro só aparece mais tarde, quando alguma linha tentar usar o texto: aqui, logo no `print(assinada.texto)`; num ciclo, dentro do `apresentar`. A última linha da mensagem é esta:

```text
AttributeError: 'NotificacaoAssinada' object has no attribute 'texto'
```

Em português: o objeto do tipo `NotificacaoAssinada` não tem o atributo `texto`. Um `AttributeError` ("erro de atributo") aparece quando se pede a um objeto um atributo que ele não tem. É o tipo de erro de "Nada impede uma quantidade impossível", no guia 03: aparece longe da causa. A mensagem diz que falta o texto, mas o engano está no construtor, onde faltou chamar a base.

Fica então esta regra. Quando a classe base tem um construtor e a classe derivada escreve o seu, a primeira linha do construtor da derivada deve ser, quase sempre, a chamada `super().__init__(...)`. Leva os valores de que o construtor da base precisa. Se a classe base não tiver construtor, nem escrito nem herdado, não há nenhum para aproveitar, e essa linha não faz falta.

## Polimorfismo: a mesma chamada, comportamentos diferentes

Temos agora três variantes de notificação, todas derivadas da mesma base. Vamos guardá-las numa lista e apresentá-las todas. É um programa completo.

Antes de correres, tenta prever as três linhas. Para cada uma, pensa de que classe é o objeto e que `apresentar` o Python vai encontrar.

```python
# Três variantes numa lista e o mesmo pedido a todas: o quarto programa do guia 05.

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

Leitura guiada: as quatro classes são as dos programas anteriores, juntas no mesmo ficheiro. O que é novo está depois delas: uma lista com três notificações e um ciclo `for` que lhes pede, uma a uma, que se apresentem.

Uma lista pode guardar objetos, tal como guarda números ou textos. Aqui, cada elemento da lista é uma notificação. Em cada volta do `for`, o nome `aviso` aponta para um desses objetos.

A lista é escrita de uma maneira que talvez ainda não tenhas visto. Os três objetos são criados dentro dos parênteses retos, separados por vírgulas, um por linha. É o mesmo que criar a lista vazia e fazer três `append`, só que mais curto. Repara também na vírgula depois do último objeto. É opcional: o Python aceita a lista com ela ou sem ela. Escreve-se para que, quando se acrescenta mais um elemento numa linha nova, não seja preciso mexer na linha de cima para lhe pôr a vírgula.

Olha agora para o ciclo. Tem uma única linha de trabalho, `print(aviso.apresentar())`, e essa linha é exatamente a mesma nas três voltas. Mesmo assim, cada volta produz um resultado de forma diferente. O nome `aviso` aponta, em cada volta, para um objeto de uma classe diferente. E o Python encontra, pela regra de "Redefinir um método: onde o Python procura", o `apresentar` que vale para essa classe: o dela, se o escreveu, ou o da base.

| Volta | `aviso` aponta para um objeto da classe | `apresentar` usado | Resultado |
| --- | --- | --- | --- |
| 1 | `NotificacaoBreve` | O da base, `Notificacao` | `Contagem concluída` |
| 2 | `NotificacaoDetalhada` | O de `NotificacaoDetalhada` | `Aviso interno: Material em falta` |
| 3 | `NotificacaoAssinada` | O de `NotificacaoAssinada` | `Encomenda recebida (enviada por: Secretaria)` |

Chamamos **polimorfismo** a esta capacidade: o mesmo pedido, feito da mesma maneira, funciona com objetos de classes diferentes, e cada objeto responde à sua maneira. A palavra vem do grego e quer dizer "muitas formas". O ciclo não sabe, nem precisa de saber, de que variante é cada notificação. Só conta com que cada uma saiba apresentar-se.

Quando executa `aviso.apresentar()`, o Python não pergunta se o objeto é uma `Notificacao`. Limita-se a procurar um método chamado `apresentar`, pela regra de procura: primeiro na classe do objeto, depois nas classes de onde ela herda. Por isso, este mesmo ciclo também funcionaria com as duas classes soltas de "Duas classes quase iguais", sem herança nenhuma, desde que cada uma tivesse o seu `apresentar`. Em Python, o que o polimorfismo exige é que cada objeto saiba responder ao pedido que lhe fazem.

Então, o que ganhámos com a herança? Ganhámos o que faltava em "Duas classes quase iguais". O código comum, como o construtor, está escrito uma só vez, na classe base, e uma regra que lá se acrescente vale para todas as variantes. Há um tipo comum, `Notificacao`, que o `isinstance` reconhece e que está no topo da árvore de especialização. Diz, num só sítio, o que todas as notificações têm e sabem fazer. E a classe base é o sítio onde fica escrito o contrato que todas as variantes cumprem, como vais ver em "O contrato comum" e em "Abstração e classes abstratas". Duas classes soltas não têm esse sítio.

Para perceberes o que o polimorfismo poupa, compara com a maneira de fazer o mesmo sem ele. Este excerto depende das classes e da lista do programa acima. Mostra o ciclo escrito por alguém que decide, ele próprio, como apresentar cada variante:

```python partial
for aviso in avisos:
    if isinstance(aviso, NotificacaoDetalhada):
        print("Aviso interno: " + aviso.texto)
    elif isinstance(aviso, NotificacaoAssinada):
        print(aviso.texto + " (enviada por: " + aviso.origem + ")")
    else:
        print(aviso.texto)
```

Mostra o mesmo, mas tem três problemas.

O primeiro é que a forma de apresentar cada variante saiu da classe e veio parar ao ciclo. O ciclo passou a ter uma responsabilidade que não é dele. Uma tarefa deve ficar com quem tem a informação necessária para a fazer. Quem sabe como se apresenta uma notificação assinada é a própria classe `NotificacaoAssinada`. É a pergunta "quem sabe o quê?", que o guia 04 desenvolve em "Quem sabe o quê: responsabilidades".

O segundo é que cada variante nova obriga a mudar este ciclo, e todos os outros sítios do programa que apresentem notificações.

O terceiro é que é fácil esquecer um caso. Uma variante nova que ninguém acrescentou à cadeia cai no `else` e é apresentada como breve, sem nenhum erro a avisar.

Com polimorfismo, uma variante nova é uma classe nova, e o ciclo não muda uma única linha. O exemplo guiado, no fim da matéria, vai mostrar isso mesmo.

## O contrato comum

O polimorfismo só dá o resultado certo se todas as variantes cumprirem a mesma promessa. Ter um método com o nome certo não chega. O ciclo de "Polimorfismo: a mesma chamada, comportamentos diferentes" conta com três coisas: que `apresentar` possa ser chamado sem argumentos, que devolva um texto e que não mude a notificação.

Tal como fizemos no guia 03 para `adicionar` e `retirar`, escrevemos o contrato de `apresentar`:

> `apresentar()` não recebe nada além do `self`, devolve um texto pronto a mostrar e não altera a notificação. Não mostra nada no ecrã: quem decide o que fazer com o texto é quem o pediu.

A última frase é a divisão de tarefas do guia 03, em "Tratar a recusa: `try` e `except`". Lá, quem apanha a exceção decide o que fazer com a recusa. Aqui, a notificação prepara o texto, e quem o recebe decide se o mostra no terminal, numa página na internet ou noutro sítio qualquer.

Vejamos o que acontece quando uma variante tem o nome certo mas não cumpre o contrato. É um programa completo.

Antes de correres, tenta prever quantas linhas aparecem e o que diz cada uma.

```python
# Uma variante que não cumpre o contrato: o quinto programa do guia 05.

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

Leitura guiada: a classe nova é a `NotificacaoMalFeita`, e o seu `apresentar` tem um `print` e nenhum `return`. O ciclo é o de sempre. Por isso, lê as três linhas da saída a perguntar, para cada uma, que `print` a escreveu: o do ciclo ou o do método.

A primeira linha está certa. A segunda foi escrita pelo próprio método `apresentar` da variante mal feita, com o seu `print`. A terceira é o `print` do ciclo a mostrar o que o método devolveu. Como o método não tem `return`, devolveu `None`, o "nada" do Python que conheceste no guia 03, em "Adicionar: uma operação com contrato". O ciclo não tem culpa. Fez exatamente o mesmo pedido que fazia às outras variantes; foi a variante que não cumpriu o que prometia. Num programa que mostrasse as notificações numa página na internet, o `print` da variante não apareceria em lado nenhum, e a página mostraria "None".

Há outras maneiras de quebrar o contrato com o nome certo. Imagina uma variante cujo `apresentar` guardasse o texto numa variável, apagasse o atributo com `self.texto = ""` e devolvesse a variável. Na primeira chamada, devolvia o texto certo; na segunda, um texto vazio. Mudou o estado, e o contrato diz que não muda. E uma variante cujo `apresentar` exigisse um argumento obrigatório faria o ciclo parar com um erro na chamada `aviso.apresentar()`.

A ideia de fundo tem nome: **princípio da substituição**. Um objeto de uma classe derivada tem de poder ser usado em qualquer sítio onde se espera um objeto da classe base, sem surpresas para quem o usa. É o teste "é um" de "Especialização: do geral para o particular", aplicado ao comportamento, e não só aos dados.

Uma classe que tem o nome certo, herda da base certa e mesmo assim não cumpre o contrato continua a ser uma `Notificacao` para o Python: o `isinstance` dá `True`. Quem a usa é que é apanhado de surpresa, porque ela não se comporta como as outras notificações. O `isinstance` não verifica o contrato: cumpri-lo fica a cargo de quem escreve cada variante.

## Abstração e classes abstratas

### Abstrair é escolher o essencial

**Abstração** é escolher o que é essencial para o problema e deixar de fora o resto. Já o fizeste várias vezes. No guia 01, decidimos que um artigo tem código, nome e quantidade. Decidimos também que não se faz uma ficha por cada caderno físico, e que a cor das paredes da sala não entra no programa. Estávamos a abstrair, e o guia 01 di-lo numa frase: "representar um problema é sempre escolher o que interessa".

Na classe `Notificacao`, o essencial é que todas as notificações têm um texto e sabem apresentar-se. A maneira de se apresentarem não é essencial à ideia de notificação: é um pormenor de cada variante.

### Uma notificação geral não tem maneira própria de se apresentar

Olha outra vez para a classe `Notificacao` que usámos até aqui. O seu `apresentar` devolve só o texto. Por isso, pode criar-se uma notificação "geral", com `Notificacao("Contagem concluída")`, e ela apresenta-se da maneira breve. Mas, na ideia de notificação, uma notificação geral não tem uma maneira definida de se apresentar. A maneira breve é uma das variantes, e só foi parar à base porque era a mais simples de escrever.

Há uma segunda dificuldade, do lado de quem escreve uma variante nova. Essa pessoa tem de saber o que a variante promete, sem o adivinhar a partir das outras. E, se se esquecer de escrever o `apresentar`, a variante apresenta-se da maneira breve, sem nenhum aviso. É o mesmo tipo de esquecimento silencioso do `else` da cadeia de `isinstance`.

### Classe abstrata e método abstrato

Uma **classe abstrata** é uma classe que descreve o que é comum a um grupo de classes, mas que não serve para criar objetos diretamente. Serve de base às classes derivadas, que são as que se usam para criar objetos. Às classes de onde se podem criar objetos chamamos **classes concretas**.

Um **método abstrato** é um método de uma classe abstrata que tem o nome e o contrato, mas não tem instruções. Diz "todas as classes derivadas têm de saber fazer isto", sem dizer como. Cada classe derivada concreta tem de o escrever.

No nosso exemplo, a ideia de notificação é uma classe abstrata, e `apresentar` é um método abstrato. Todas as notificações têm um texto e sabem apresentar-se, mas só cada variante sabe como se apresenta.

Uma classe abstrata é uma decisão do modelo. Chamamos **modelo** à descrição das classes de um programa, do que cada uma guarda e faz, e das relações entre elas, escrita antes do código. A árvore de especialização das notificações já é uma parte do modelo delas. Decidir que a ideia de notificação é abstrata é uma escolha do mesmo género das do guia 01: o que interessa representar, e como. A classe abstrata escreve-se primeiro no papel, como contrato. Depois, o contrato passa para o código, na docstring da classe base. São as duas partes que se seguem.

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

Não há uma forma única de o escrever. O que conta é que se perceba o que é comum a todas as variantes e o que cada uma tem de completar. O contrato do método abstrato tem de lá estar por inteiro.

Repara que a classe abstrata não está vazia. A primeira linha do contrato diz o que todas as notificações têm, um texto guardado na criação, e isso é igual em todas. Abstrata não quer dizer vazia. Quer dizer incompleta de propósito: há uma parte, o método abstrato, que só as classes derivadas completam.

### O contrato na docstring da classe base

No modelo, a `Notificacao` é uma classe abstrata. Nos programas deste guia, continua a ser uma classe concreta: o Python deixa criar objetos dela, e o seu `apresentar` devolve o texto, da maneira breve. Por isso, a `NotificacaoBreve` não escreve o seu `apresentar`. Herda o da base, que já se apresenta da maneira breve, e só as variantes que se apresentam de outra maneira o redefinem. O que passa do papel para o código é o contrato. Fica escrito na docstring da classe base e na do seu método `apresentar`, que é onde quem escreve uma variante nova o vai procurar.

Uma docstring pode ter várias linhas. A primeira diz, numa frase, o que a classe ou o método é. Segue-se uma linha em branco e o resto da explicação, e as três aspas que fecham ficam numa linha sozinhas.

Segue-se um programa completo, com a classe base e o contrato, uma variante que o cumpre e outra que se esqueceu do seu `apresentar`. A esquecida devia apresentar o texto entre parênteses retos, como diz a docstring dela.

Antes de correres, tenta prever as três linhas. Pensa sobretudo na terceira: o que mostra uma variante que não escreveu o seu `apresentar`?

```python
# A classe base com o contrato na docstring: o sexto programa do guia 05.

class Notificacao:
    """Uma mensagem preparada para ser apresentada a alguém.

    No modelo, é uma classe abstrata: os objetos criam-se das variantes.
    Todas as notificações guardam um texto e sabem apresentar-se. Uma
    variante que se apresente de outra maneira redefine apresentar().
    """

    def __init__(self, texto):
        """Guarda o texto da notificação."""
        self.texto = texto

    def apresentar(self):
        """Devolve o texto da notificação, pronto a mostrar.

        Contrato: não recebe nada além do self, devolve um texto pronto a
        mostrar e não altera a notificação. Não mostra nada no ecrã.
        """
        return self.texto


class NotificacaoDetalhada(Notificacao):
    """Notificação que apresenta o texto com um aviso antes."""

    def apresentar(self):
        """Devolve o texto com "Aviso interno: " antes."""
        return "Aviso interno: " + self.texto


class NotificacaoEsquecida(Notificacao):
    """Notificação que devia apresentar o texto entre parênteses retos."""


geral = Notificacao("Contagem concluída")
detalhada = NotificacaoDetalhada("Material em falta")
esquecida = NotificacaoEsquecida("A02 esgotou")

print(geral.apresentar())
print(detalhada.apresentar())
print(esquecida.apresentar())
```

O programa mostra:

```text
Contagem concluída
Aviso interno: Material em falta
A02 esgotou
```

Leitura guiada: começa pela classe `Notificacao`. As instruções são as de sempre, e o que mudou foram as duas docstrings, que agora levam o contrato. A detalhada já a conheces. A `NotificacaoEsquecida` só tem a docstring, que diz o que ela devia fazer. No fim, o programa cria três notificações e pede a cada uma que se apresente.

A primeira linha vem da notificação geral. A docstring da base diz que, no modelo, a `Notificacao` é abstrata e que os objetos se criam das variantes. Mesmo assim, o Python criou a notificação geral sem se queixar, e ela apresentou-se da maneira breve. O Python não lê as docstrings para decidir o que pode criar: para ele, `Notificacao` é uma classe como outra qualquer.

A terceira linha é a mais importante. A docstring da `NotificacaoEsquecida` promete o texto entre parênteses retos, e o contrato da base diz que uma variante que se apresenta de outra maneira redefine `apresentar`. Mas a variante não o escreveu. Pela regra de procura, o Python foi buscar o `apresentar` da base, e a notificação saiu da maneira breve, sem nenhum aviso.

Fica então claro o que a docstring faz e o que não faz. Explica o contrato a quem escreve uma variante, no sítio onde ele o vai procurar. Mas não obriga ninguém a cumpri-lo: o Python não verifica se as variantes fazem o que as docstrings dizem. É o que já viste em "O contrato comum", com o `isinstance`. Cumprir o contrato fica a cargo de quem escreve cada variante.

Por isso, o contrato tem de estar escrito por inteiro, e a previsão antes de executar ganha outra importância. Quem leu a docstring da `NotificacaoEsquecida` e previu `[A02 esgotou]` para a terceira linha dá logo pelo esquecimento. É a previsão escrita, comparada com o que o programa mostra, que apanha uma variante que não cumpre o contrato.

## Herança ou composição

### Duas maneiras de reaproveitar

Tens agora duas maneiras de construir uma classe a partir de outras. A herança diz "é um": a classe derivada é um caso particular da base e recebe tudo o que ela descreve. A **composição de objetos**, no sentido largo, diz "tem": o objeto guarda outros objetos e usa-os para fazer o seu trabalho. É a relação "tem" de "Especialização: do geral para o particular".

A palavra composição tem também um sentido mais estreito, que separa dois graus de "tem". No sentido estreito, a composição é a forma mais forte da relação "tem": a parte só existe dentro do todo. Numa encomenda feita numa loja na internet, cada linha, como "2 camisolas", só faz sentido dentro dela. Quando a parte existe sem o todo, a relação chama-se **agregação**. As músicas continuam a existir se a playlist for apagada, e a playlist só as junta. Neste guia, a palavra composição quer dizer o sentido largo, qualquer relação "tem", a não ser quando se diz o contrário. O guia 04 explica a diferença entre os dois graus em "Dois graus de "tem": composição e agregação".

A decisão começa pela análise da relação entre as duas classes. Só há herança se a frase "A é um B" for verdadeira e se A puder cumprir tudo o que B promete. Isto é, se passar o teste de substituição de "O contrato comum". Quando houver dúvida, a composição é quase sempre a escolha mais segura. Um objeto que guarda outro pode trocá-lo mais tarde por outro diferente. E não fica obrigado a receber atributos e métodos que não fazem sentido para ele, que é o que acontece com uma herança mal escolhida.

### Heranças sem sentido

Estes três exemplos parecem razoáveis à primeira vista e estão todos errados:

- `class Inventario(Artigo):`. A frase "um inventário é um artigo" é falsa, como viste com o teste em "Especialização: do geral para o particular". Com esta herança, o inventário receberia a propriedade `quantidade` e os métodos `adicionar(unidades)` e `retirar(unidades)`. Não fazem sentido para um conjunto de artigos: retirar 2 unidades de quê?
- `class Inventario(Notificacao):`, com o argumento de que o inventário também produz avisos. O inventário usaria notificações, mas não é uma. Com esta herança, teria um atributo `texto` e um método `apresentar`, e ninguém saberia dizer que texto é esse. A relação certa seria "o inventário tem uma caixa de avisos", uma composição. A caixa de avisos aparece no passo 7 do exemplo guiado.
- `class Caderno(Artigo):` e `class Pasta(Artigo):`. A frase "um caderno é um artigo" até é verdadeira. Mas o guia 02, em "Classe: a descrição comum", já mostrou que estas classes não fazem falta: cadernos e pastas guardam os mesmos dados e aceitam as mesmas operações. Uma classe derivada só se justifica quando acrescenta ou muda alguma coisa. Uma árvore de especialização não obriga a criar uma classe por cada nome. E a `NotificacaoBreve` de "Herança em Python", que também só tem a docstring? "Breve" é uma maneira de se apresentar, um comportamento, e no contrato abstrato é uma variante como as outras. Só não escreve nada porque, nos programas deste guia, a base já se apresenta dessa maneira. Um caderno e uma pasta não se comportam de maneira diferente: só têm valores diferentes.

O inventário deste módulo não usa herança nenhuma, e está bem assim. Um programa não fica melhor por usar herança. Fica melhor quando cada relação é a certa.

## Exemplo guiado: acrescentar uma variante nova

O responsável do armário da sala quer que os avisos de material esgotado chamem a atenção. Pede uma notificação que se apresente com "URGENTE: " antes do texto, e com o texto todo em maiúsculas. Depois quer juntar numa caixa os avisos que vão chegando, de qualquer variante, e ver os textos todos pela ordem de chegada.

Vamos acrescentar a variante nova ao programa de "Polimorfismo: a mesma chamada, comportamentos diferentes", acompanhando o raciocínio de cada passo. A classe base é a de "O contrato na docstring da classe base", com o contrato escrito. No fim, juntamos a variante nova às outras numa caixa de avisos.

### Passo 1: confirmar a relação "é um"

"Uma notificação urgente é uma notificação." Tem um texto e sabe apresentar-se. O teste de substituição também passa, se tivermos o cuidado de cumprir o contrato: onde se usa uma notificação qualquer, deve poder usar-se uma urgente. A nova classe vai, portanto, herdar de `Notificacao`.

### Passo 2: decidir o que muda

A notificação urgente não precisa de dados novos, só do texto, que a base já guarda. Por isso não precisa de construtor próprio, nem de `super()`. Herda o construtor da base, como a breve e a detalhada. O que muda é só a maneira de se apresentar, e é isso que vamos escrever. É o que pede o contrato da base: uma variante que se apresente de outra maneira redefine `apresentar`. Se nos esquecêssemos, nenhum erro avisaria. A urgente apresentava-se da maneira breve, como a `NotificacaoEsquecida` de "O contrato na docstring da classe base", e só a previsão do passo 5 daria pelo esquecimento.

### Passo 3: cumprir o contrato

Para pôr o texto em maiúsculas, os textos do Python têm um método, `upper` (do inglês, "de cima", como nas letras maiúsculas). `"A02 esgotou".upper()` devolve `"A02 ESGOTOU"`. O `upper` devolve um texto novo, e o texto original fica como estava. Um texto do Python não muda depois de criado: nenhum método dos textos o altera. Os que produzem um texto, como este `upper`, devolvem um texto novo. Se fizeste o Mais longe 3 da ficha do tema 03, já viste outro, o `strip`.

Isso permite-nos cumprir a regra "não altera a notificação". O método vai devolver `"URGENTE: " + self.texto.upper()`, que é um texto novo, e o atributo `texto` continua com as minúsculas originais. Se escrevêssemos `self.texto = self.texto.upper()` dentro do método, estaríamos a mudar o estado: o atributo passava a apontar para o texto novo, em maiúsculas. O contrato seria quebrado.

### Passo 4: escrever a classe

É um excerto, que se acrescenta ao programa de "Polimorfismo: a mesma chamada, comportamentos diferentes", depois das outras variantes, e não corre sozinho:

```python partial
class NotificacaoUrgente(Notificacao):
    """Notificação que pede atenção imediata: o texto aparece em maiúsculas."""

    def apresentar(self):
        """Devolve "URGENTE: " seguido do texto em maiúsculas, sem alterar o texto guardado."""
        return "URGENTE: " + self.texto.upper()
```

### Passo 5: prever as chamadas antes de executar

Vamos pôr uma notificação de cada variante numa lista e apresentá-las com o mesmo ciclo de "Polimorfismo: a mesma chamada, comportamentos diferentes". Antes de executar, prevemos, para cada volta, a classe do objeto, o `apresentar` que o Python vai usar e o resultado:

| Volta | Objeto | `apresentar` usado | Resultado previsto |
| --- | --- | --- | --- |
| 1 | `NotificacaoBreve("Contagem concluída")` | O da base, `Notificacao` | `Contagem concluída` |
| 2 | `NotificacaoDetalhada("Material em falta")` | O de `NotificacaoDetalhada` | `Aviso interno: Material em falta` |
| 3 | `NotificacaoAssinada("Encomenda recebida", "Secretaria")` | O de `NotificacaoAssinada` | `Encomenda recebida (enviada por: Secretaria)` |
| 4 | `NotificacaoUrgente("A02 esgotou")` | O de `NotificacaoUrgente` | `URGENTE: A02 ESGOTOU` |

A notificação breve não escreve `apresentar`, e por isso o Python encontra o da base. As outras três escrevem o seu, e o Python encontra-o na própria classe, pela regra de procura.

Prevemos também uma linha extra, que confirma o contrato: depois de apresentada, a notificação urgente continua a guardar o texto "A02 esgotou", em minúsculas.

### Passo 6: executar e comparar

É o programa completo. Compara cada linha do que ele mostra com a coluna "Resultado previsto" do passo 5.

```python
# Exemplo guiado do guia 05: a notificação urgente, com o mesmo ciclo.

class Notificacao:
    """Uma mensagem preparada para ser apresentada a alguém.

    No modelo, é uma classe abstrata: os objetos criam-se das variantes.
    Todas as notificações guardam um texto e sabem apresentar-se. Uma
    variante que se apresente de outra maneira redefine apresentar().
    """

    def __init__(self, texto):
        """Guarda o texto da notificação."""
        self.texto = texto

    def apresentar(self):
        """Devolve o texto da notificação, pronto a mostrar.

        Contrato: não recebe nada além do self, devolve um texto pronto a
        mostrar e não altera a notificação. Não mostra nada no ecrã.
        """
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

As quatro primeiras linhas coincidem com a coluna "Resultado previsto" do passo 5. A última confirma o contrato: o texto guardado continua em minúsculas, porque `upper` devolveu um texto novo e o atributo não foi tocado. `avisos[3]` é o quarto elemento da lista, porque os índices começam em 0.

Agora repara no que não mudou. O ciclo `for` é, letra a letra, o de "Polimorfismo: a mesma chamada, comportamentos diferentes". Para acrescentar uma maneira nova de apresentar notificações, escrevemos uma classe nova e não tocámos em nenhuma linha do código que as usa. É isto que o polimorfismo permite, e é a resposta ao segundo problema da cadeia de `isinstance`.

### Passo 7: juntar os avisos numa caixa

Falta a segunda parte do pedido: uma caixa que junte os avisos que vão chegando e devolva os seus textos pela ordem de chegada. A caixa não é uma notificação. Tem notificações: "uma caixa de avisos tem notificações" é a frase verdadeira, e "uma caixa de avisos é uma notificação" é falsa. Por isso, a classe `CaixaDeAvisos` não herda de nada. Guarda as notificações numa lista.

Antes de correres, tenta prever as três linhas. Repara na ordem em que as notificações são entregues à caixa.

```python
# Exemplo guiado do guia 05: a caixa de avisos, com herança e agregação.

class Notificacao:
    """Uma mensagem preparada para ser apresentada a alguém.

    No modelo, é uma classe abstrata: os objetos criam-se das variantes.
    Todas as notificações guardam um texto e sabem apresentar-se. Uma
    variante que se apresente de outra maneira redefine apresentar().
    """

    def __init__(self, texto):
        """Guarda o texto da notificação."""
        self.texto = texto

    def apresentar(self):
        """Devolve o texto da notificação, pronto a mostrar.

        Contrato: não recebe nada além do self, devolve um texto pronto a
        mostrar e não altera a notificação. Não mostra nada no ecrã.
        """
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

Leitura guiada: as cinco classes de notificações são as do passo 6. Começa pela classe `CaixaDeAvisos`, que é a nova, e lê os seus três métodos por ordem. Depois lê o programa principal: uma caixa vazia, três notificações entregues à caixa e um ciclo que mostra os textos que a caixa devolve.

O construtor dá a cada caixa uma lista vazia, `_avisos`. O sublinhado do guia 03 avisa que é um nome interno da classe: quem usa a caixa entrega notificações com `receber`, e não mexe na lista. O método `receber` junta à lista uma notificação que já existe. O método `textos` prepara, antes do ciclo, uma lista vazia, `resultado`. Em cada volta, junta-lhe a apresentação de uma notificação, e só depois de o ciclo acabar é que a devolve. A uma variável assim, preparada antes de um ciclo e que vai juntando uma parte do resultado em cada volta, chama-se **acumulador**.

A classe `CaixaDeAvisos` usa as duas relações ao mesmo tempo, e cada uma no seu lugar.

A caixa tem notificações. As notificações são criadas fora dela, no programa principal, e entregues já feitas ao método `receber`. Em lado nenhum da classe `CaixaDeAvisos` aparece `NotificacaoBreve(...)` ou outra criação. É uma agregação: a notificação faz sentido sem a caixa, e não é a caixa que a cria. O guia 04 tem outro exemplo, as músicas de uma playlist, em "Agregação em Python: a playlist e as músicas".

Cada variante é uma notificação: a `NotificacaoUrgente` é uma `Notificacao`, e as outras três também. É a herança.

E o método `textos` usa o polimorfismo: pede a cada notificação que se apresente, com a mesma linha para todas, sem perguntar de que variante é. A caixa não conhece `NotificacaoBreve`, nem `NotificacaoUrgente`, nem nenhuma outra variante. Só conta com o contrato que a classe `Notificacao` fixa para todas: cada notificação sabe apresentar-se. Por isso, uma variante que venha a ser escrita no próximo ano também cabe na caixa, sem mudar uma linha da classe `CaixaDeAvisos`.

Por palavras, as classes deste programa e as relações entre elas descrevem-se assim. Uma caixa de avisos tem notificações, que recebe já criadas, e devolve os seus textos pela ordem de chegada. Cada notificação tem um texto e sabe apresentar-se. A breve, a detalhada, a assinada e a urgente são notificações, e cada uma apresenta-se à sua maneira. A assinada guarda também a origem. Repara que a descrição da caixa fala de notificações, e não de cada variante. A caixa trabalha com qualquer notificação, e as variantes que existem hoje são as classes que herdam dela.

Se um dia o inventário precisasse de avisar quando um artigo esgota, poderia ter uma caixa de avisos, guardada num atributo seu. Entregava-lhe uma `NotificacaoUrgente` sempre que a quantidade de um artigo chegasse a zero. Seria uma composição no sentido largo: o inventário tem uma caixa de avisos. Não o vamos fazer, porque o inventário deste módulo não precisa. Mas é assim que as notificações deste guia se ligariam ao inventário que se constrói no guia 04.

## Erros frequentes

O erro típico de cada ideia está na secção dela:

- pensar que herdar é partilhar valores, em "Herança em Python";
- esquecer a linha do `super().__init__`, em "Acrescentar dados numa classe derivada: `super()`";
- uma variante que mostra o texto em vez de o devolver, em "O contrato comum";
- uma variante que se esqueceu do seu `apresentar` e sai da maneira breve, em "O contrato na docstring da classe base";
- as heranças sem sentido, em "Herança ou composição";
- mudar o texto guardado dentro do `apresentar`, no passo 3 do exemplo guiado.

Ficam aqui os erros que aparecem quando se escreve, pela primeira vez, uma classe que herda de outra. Quando há uma mensagem de erro, lê primeiro a última linha: é a que diz o que aconteceu. O último erro não tem mensagem nenhuma.

### O Python não conhece a classe base

O que se vê: o programa para logo na linha `class NotificacaoBreve(Notificacao):`, antes de criar qualquer objeto. A última linha da mensagem é `NameError: name 'Notificacao' is not defined`. Em português: o nome `Notificacao` não está definido. Um `NameError` ("erro de nome") aparece quando se usa um nome que o Python não conhece. Se houver no ficheiro um nome parecido, as versões recentes do Python acrescentam uma sugestão, como `Did you mean: 'Notificacoes'?`, isto é, "querias dizer `Notificacoes`?".

Porque acontece: a classe derivada foi escrita antes da classe base, ou a base tem outro nome, por exemplo com uma letra trocada. O Python lê o ficheiro de cima para baixo. Quando chega à linha da classe derivada, tem de conhecer já a classe que está entre parênteses.

Como se corrige: escreve a classe base antes de todas as classes que herdam dela, e confirma que o nome entre parênteses é exatamente o da base.

### Uma classe derivada sem nada por baixo

O que se vê: o programa nem começa. A última linha da mensagem é `IndentationError: expected an indented block after class definition on line`, seguida de um número. Um `IndentationError` é um "erro de indentação", e a mensagem diz "esperava-se um bloco indentado a seguir à definição de classe da linha" indicada. Nas versões anteriores ao Python 3.10, a última linha diz só `IndentationError: expected an indented block`.

Porque acontece: uma classe derivada que não acrescenta nada ficou sem nenhuma linha por baixo, nem sequer a docstring. O corpo de uma classe não pode ficar vazio. É um erro de escrita, e o Python recusa o ficheiro antes de executar a primeira linha.

Como se corrige: escreve a docstring da classe, indentada quatro espaços, a dizer o que a classe é. É o que faz a `NotificacaoBreve` de "Herança em Python".

### Uma variante criada com valores a menos

O que se vê: `TypeError: NotificacaoAssinada.__init__() missing 1 required positional argument: 'origem'`. Em português: falta ao construtor de `NotificacaoAssinada` um argumento obrigatório, a `origem`. Nas versões anteriores ao Python 3.10, a mensagem começa por `__init__()`, sem o nome da classe à frente.

Porque acontece: a notificação foi criada com menos valores do que o seu construtor pede, como `NotificacaoAssinada("Encomenda recebida")`. A classe derivada redefiniu o construtor, e o construtor dela pede dois valores, mesmo que o da base só peça um.

Como se corrige: vê quantos valores o construtor da classe recebe, sem contar o `self`, e passa-os todos, pela mesma ordem.

### O `super().__init__` sem o texto

O que se vê: o programa para ao criar a notificação assinada, na linha do `super()`, com `TypeError: Notificacao.__init__() missing 1 required positional argument: 'texto'`. Em português: falta ao construtor de `Notificacao` o argumento `texto`. Nas versões anteriores ao Python 3.10, a mensagem começa por `__init__()`.

Porque acontece: a linha ficou `super().__init__()`, com os parênteses vazios. O construtor da base também precisa dos seus valores, e quem lhos dá é a classe derivada, nessa chamada. Repara que a mensagem fala do construtor de `Notificacao`, e não do de `NotificacaoAssinada`: é o da base que se queixa.

Como se corrige: passa ao `super().__init__` os valores de que o construtor da base precisa, aqui `super().__init__(texto)`.

### O método da variante escrito com outro nome

O que se vê: nenhuma mensagem de erro. Uma variante que escreveste apresenta-se como a base, só com o texto, como se não tivesse o seu `apresentar`. Por exemplo, a notificação detalhada mostra `Material em falta`, sem o aviso antes.

Porque acontece: o método da variante tem outro nome, como `apresenta` ou `Apresentar`. Para o Python, é um método novo, que ninguém chama. Quando o ciclo pede `apresentar`, o Python segue a regra de procura, não o encontra na variante e usa o da base. Também acontece quando o `def` ficou encostado à margem, fora da classe: o método deixa de pertencer à variante.

Como se corrige: confirma, letra a letra, que o método se chama exatamente como o da base, e que o `def` está indentado dentro da classe. O Python não avisa deste erro. Quem dá por ele é a previsão escrita antes de executar.

## Palavras novas deste guia

- Relação "tem": a relação entre um todo e as partes que ele guarda e usa, como entre um inventário e os seus artigos.
- Relação "é um": a relação entre um tipo particular e um tipo mais geral, como entre o carro e o veículo.
- Especialização: a relação entre um tipo geral e um tipo particular, que conserva tudo o que o geral descreve e acrescenta ou concretiza alguma coisa.
- Árvore de especialização, árvore de classificação ou hierarquia de especialização: um desenho em que cada ramo liga um tipo geral a um tipo mais particular. Lê-se de baixo para cima, com "é um".
- Herança: o mecanismo que permite definir uma classe a partir de outra, que lhe dá os seus métodos, incluindo o construtor.
- Classe base, ou superclasse: a classe geral, de onde as outras partem.
- Classe derivada, ou subclasse: a classe particular, definida a partir da base.
- Herdar: receber da classe base os seus métodos, incluindo o construtor.
- Classes irmãs: duas classes derivadas da mesma base; as duas são casos da base, mas nenhuma é a outra.
- Redefinir um método (em inglês, *override*): escrever, numa classe derivada, um método com o mesmo nome de um método da base.
- Regra de procura: o Python procura um método primeiro na classe do objeto, depois na base, depois na base da base.
- `super()`: dá acesso às versões da classe base dos métodos, para o mesmo objeto, como em `super().__init__(texto)`.
- Polimorfismo: o mesmo pedido, feito da mesma maneira, funciona com objetos de classes diferentes, e cada um responde à sua maneira.
- Princípio da substituição: um objeto de uma classe derivada tem de poder ser usado onde se espera um da base, sem surpresas.
- Abstração: escolher o que é essencial para o problema e deixar de fora o resto.
- Modelo: a descrição das classes de um programa, do que cada uma guarda e faz, e das relações entre elas, escrita antes do código.
- Classe abstrata: uma classe que descreve o que é comum a um grupo de classes, mas de onde não se criam objetos diretamente. O seu contrato escreve-se no papel e na docstring da classe base.
- Classe concreta: uma classe de onde se podem criar objetos.
- Método abstrato: um método com o nome e o contrato, mas sem instruções, que cada classe derivada concreta tem de escrever.
- `upper`: o método dos textos que devolve um texto novo, todo em maiúsculas, sem alterar o original.
- Composição de objetos: no sentido largo, construir um objeto a partir de outros objetos que ele guarda e usa; é a relação "tem".
- Agregação: a relação "tem" em que a parte existe sem o todo, como as músicas de uma playlist.
- Composição, no sentido estreito: a relação "tem" em que a parte só existe dentro do todo, como as linhas de uma encomenda.
- Acumulador: uma variável preparada antes de um ciclo, que vai juntando, volta a volta, uma parte do resultado.

## Verificar o que aprendeste

Tenta responder sem olhar para o texto. Se uma pergunta te deixar com dúvidas, volta à secção indicada.

1. Quais são os dois custos de ter duas classes quase iguais, sem herança? ("Duas classes quase iguais")
2. Que diferença há entre a relação "tem" e a relação "é um"? Aplica o teste "tudo o que B tem e faz tem de fazer sentido para A" à frase "uma notificação detalhada é uma notificação". ("Especialização: do geral para o particular")
3. O que herda uma classe derivada? O que acontece quando se cria um objeto de uma classe derivada que não escreveu construtor? ("Herança em Python")
4. Porque é que `isinstance(breve, Notificacao)` dá `True`, e `isinstance(breve, NotificacaoDetalhada)` dá `False`? ("Herança em Python")
5. Onde é que o Python procura um método, e por que ordem? ("Redefinir um método: onde o Python procura")
6. O que faz `super().__init__(texto)`, quando é que uma classe derivada a escreve, e o que acontece se for esquecida? ("Acrescentar dados numa classe derivada: `super()`")
7. Usa o ciclo das três variantes para explicar o que é o polimorfismo. O que é que ele poupa em relação à cadeia de `isinstance`, e o que lhe acrescenta a herança? ("Polimorfismo: a mesma chamada, comportamentos diferentes")
8. Escreve o contrato de `apresentar` e dá um exemplo de uma variante que o quebra, mesmo com o nome certo. ("O contrato comum")
9. O que são uma classe abstrata e um método abstrato? Escreve no papel o contrato abstrato de `Notificacao`. O que faz a docstring da classe base, e o que não faz? ("Abstração e classes abstratas")
10. Dá um exemplo de uma herança sem sentido e diz qual é a relação certa. ("Herança ou composição")
11. Prevê o resultado de cada volta do ciclo do exemplo guiado, dizendo o `apresentar` que o Python usa em cada uma. (Exemplo guiado, passo 5)

## O que vem a seguir

Para praticar este tema, faz o [laboratório](05-heranca-polimorfismo-laboratorio.md) e depois a [ficha de exercícios](05-heranca-polimorfismo-exercicios.md). No laboratório constróis as notificações no computador, passo a passo, provocas de propósito os erros deste guia e escreves variantes tuas. Na ficha praticas sozinho a leitura de hierarquias, a previsão de chamadas, a escolha entre herança e composição e a escrita de contratos.

O tema seguinte é [Síntese](06-sintese.md). Volta ao inventário, sem herança, e junta o que aprendeste sobre objetos, contratos e composição.

No módulo seguinte, o M11, vais reencontrar estas ideias em JavaScript. As palavras mudam um pouco, mas as perguntas são as mesmas: é um ou tem? Que promete o método? Onde vive cada regra?

![Rodapé](../imagens/rodape.png)

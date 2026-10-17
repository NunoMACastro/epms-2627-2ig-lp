![Cabeçalho](../imagens/cabecalho.png)

# Objetos, classes e instâncias

Módulo M10, Introdução à Programação Orientada por Objetos. Neste guia vês como o Python junta os dados de um artigo e as operações que lhe dizem respeito numa só unidade, o objeto. Vês também como uma classe descreve todos os objetos do mesmo tipo: uma descrição comum, vários artigos. Lês o guia ao teu ritmo, de preferência em mais do que uma vez, e o que não acabares na aula acabas em casa ou na aula seguinte. Para praticar, há o [laboratório](02-objetos-classes-instancias-laboratorio.md) e a [ficha de exercícios](02-objetos-classes-instancias-exercicios.md) deste tema.

No guia anterior, [Entidades, estado e ações](01-entidades-estado-acoes.md), organizaste a informação sobre os materiais de uma sala e viste o problema das variáveis soltas. O programa guardava o código, o nome e a quantidade de cada artigo em variáveis separadas. Nada impedia que a quantidade de um artigo fosse entregue a outro por engano. Este guia acompanha as aulas sobre classes, objetos, atributos, o construtor e o `self`. Aqui encontras essas ideias escritas por extenso, uma de cada vez, com programas que podes executar. Os métodos deste guia ainda não verificam se um pedido é possível: é o assunto do guia seguinte.

Um bloco de código apresentado como programa completo pode ser copiado para um ficheiro novo, com a extensão `.py`. Depois executas esse ficheiro no editor de Python que usas nas aulas, tal como no guia 01. Os programas funcionam com o Python 3, a partir da versão 3.10. Executa sempre o ficheiro inteiro: cada execução começa do zero, com os valores iniciais escritos no programa. Os blocos apresentados como excerto não correm sozinhos, e o texto diz sempre de que outro código dependem.

## Neste guia

1. O que vais aprender
2. O que já sabes e vais usar
3. O que estamos a representar
4. Um objeto reúne dados e operações
5. Método: uma operação que pertence ao objeto
6. Classe: a descrição comum
7. Classe e instância
8. A classe Artigo em Python
9. O método retirar em Python
10. Cada instância é um objeto diferente
11. Exemplo guiado: retirar duas unidades a um dos artigos
12. Erros frequentes
13. Palavras novas deste guia
14. Verificar o que aprendeste
15. O que vem a seguir

## O que vais aprender

No fim deste guia, consegues:

- dizer o que é um objeto, um atributo e o estado de um objeto, com o exemplo de dois artigos do inventário;
- explicar o que é um método e a diferença entre definir um método e chamá-lo;
- explicar o que é uma classe e o que é uma instância, e dizer quando se justifica uma classe nova;
- escrever em Python uma classe com o construtor `__init__`, criar instâncias dela e consultar os seus atributos;
- explicar o que é o `self` numa chamada como `caderno.retirar(2)`, e distinguir o parâmetro, o argumento e o valor devolvido;
- reconhecer quando dois nomes apontam para o mesmo objeto, e confirmá-lo com `is`.

## O que já sabes e vais usar

- O artigo do inventário: uma referência de material, com código, nome e quantidade, em que a quantidade é um número escrito dentro da ficha. Explicado no guia [01 Entidades, estado e ações](01-entidades-estado-acoes.md), em "A informação que interessa guardar".
- A entidade, o estado e o comportamento, e a diferença entre consultar o estado e mudá-lo: guia [01](01-entidades-estado-acoes.md), nas três secções com esses nomes.
- As três regras do inventário: o código não se repete, o nome está preenchido e a quantidade é um número inteiro não negativo. Guia [01](01-entidades-estado-acoes.md), em "Uma operação tem de respeitar regras".
- O traço, a tabela que regista o estado depois de cada passo: guia [01](01-entidades-estado-acoes.md), em "Exemplo guiado: seguir os valores passo a passo".
- O problema das variáveis soltas, e a ideia de pedir ao próprio artigo que retire unidades: guia [01](01-entidades-estado-acoes.md), em "Duas maneiras de organizar um programa".
- A docstring, o texto entre três aspas que explica o que uma função faz: guia [01](01-entidades-estado-acoes.md), em "Duas maneiras de organizar um programa".
- Variáveis e atribuição, texto entre aspas e números, e o `print` com vários valores: do 10.º ano.
- Funções com `def`, parâmetros e `return`: do 10.º ano, e revistas no guia [01](01-entidades-estado-acoes.md), em "Duas maneiras de organizar um programa".
- As condições e os valores `True` e `False`: do 10.º ano.
- Executar um programa de Python no editor das aulas: do 10.º ano e do guia [01](01-entidades-estado-acoes.md).

## O que estamos a representar

Imagina uma sala onde estão guardados cadernos e pastas. Para saber o que existe, fazemos este registo:

| Código | Nome do material | Quantidade disponível |
| --- | --- | ---: |
| A01 | Caderno | 6 |
| A02 | Pasta | 2 |

Como viste no guia 01, um artigo é uma referência de material no inventário. A ficha A01 representa o material "Caderno", do qual existem seis unidades. Não estamos a criar uma ficha para cada um dos seis cadernos físicos. A ficha A02 representa outro material, "Pasta".

Temos, portanto, dois artigos, apesar de existirem oito unidades físicas ao todo. Se a quantidade de cadernos passar de 6 para 5, continuamos a ter a mesma ficha A01, agora com um valor atualizado.

O programa não vê a sala nem o armário. Só conhece a informação que lhe damos. Temos, por isso, de lhe dizer o que interessa guardar sobre cada artigo e o que deve ser possível fazer com essa informação.

## Um objeto reúne dados e operações

Em programação, um **objeto** é uma unidade que reúne dados sobre uma coisa e as operações que trabalham sobre esses dados. No nosso exemplo, vamos usar um objeto para representar a ficha do artigo A01, e outro objeto para representar a ficha do artigo A02.

Os dados de um objeto respondem a perguntas como "qual é o código?", "qual é o nome?" e "quantas unidades existem?". As operações respondem a pedidos como "retira duas unidades".

Os dados de um objeto são guardados em **atributos**. Um atributo tem um nome e um valor:

| Nome do atributo | Valor no artigo A01 | O que nos diz |
| --- | --- | --- |
| `codigo` | `"A01"` | Qual é a referência do material |
| `nome` | `"Caderno"` | Como se chama o material |
| `quantidade` | `6` | Quantas unidades existem neste momento |

Repara na diferença entre o atributo `quantidade` e o valor `6`. O atributo é o sítio onde se guarda uma certa informação; o valor é o que lá está guardado neste momento. Depois de retirar duas unidades, o atributo continua a chamar-se `quantidade`, mas o seu valor passa a ser `4`. É como uma gaveta com etiqueta: a etiqueta "quantidade" fica sempre igual, e o que está dentro da gaveta pode mudar.

Repara também nas aspas. `"A01"` e `"Caderno"` estão entre aspas porque são texto. `6` não tem aspas porque é um número, e só com números se podem fazer contas como 6 - 2.

No guia 01 chamaste estado ao conjunto dos valores de uma entidade num certo momento. Num objeto é igual: o **estado de um objeto** é o conjunto dos valores dos seus atributos num dado momento. Código A01, nome Caderno e quantidade 6 descrevem um estado. Código A01, nome Caderno e quantidade 4 descrevem um estado posterior do mesmo objeto.

Uma nota sobre vocabulário. Em muitos livros, e noutras linguagens de programação, os atributos também se chamam propriedades. Em Python, a palavra propriedade tem um sentido mais preciso, que vais estudar no guia 03. Por isso, nestes guias dizemos sempre atributo para os dados guardados num objeto.

## Método: uma operação que pertence ao objeto

Um **método** é uma operação que pertence a um objeto. Tal como uma função, um método tem um nome, pode receber valores, executa instruções e pode devolver um resultado. A diferença é a ligação ao objeto: um método trabalha sobre os dados do objeto a que pertence.

Por exemplo, o método `retirar` representa a operação de retirar unidades. Dizer apenas "retirar" não chega. Precisamos de dizer a que artigo e quantas unidades. Um pedido completo seria:

> Ao artigo A01, pede para retirar duas unidades.

Se A01 tinha 6 unidades, passa a ter 4. O artigo A02 não recebeu esse pedido e continua com 2. Sempre que um método for usado, vamos acompanhar estas três coisas: quem recebe o pedido, que operação se pede e com que valor.

Definir um método e chamar um método são momentos diferentes. Para **definir** um método, escrevem-se as instruções que dizem como a operação funciona, e isso faz-se uma vez. Para **chamar** um método, pede-se que essas instruções sejam executadas agora, sobre um objeto concreto. Uma chamada pode acontecer muitas vezes, ou nenhuma. Ter uma operação definida não significa que ela já tenha acontecido. Guardar no telemóvel o número de um amigo também não quer dizer que já lhe ligaste: ligas quando quiseres, as vezes que quiseres, ou nenhuma.

Nem todos os métodos alteram dados. Um método que consulte a quantidade fornece informação, mas não precisa de modificar o estado. Já viste no guia 01 que consultar também é uma operação.

## Classe: a descrição comum

Olha outra vez para as duas linhas do inventário. Os valores são diferentes, mas a organização é igual: ambos os artigos têm código, nome e quantidade. Também faz sentido retirar unidades de qualquer um deles, e a operação faz-se da mesma maneira nos dois: subtrai-se o pedido à quantidade.

Em vez de descrevermos esta organização de novo para cada artigo, escrevemos uma descrição comum, uma só vez. Essa descrição é uma **classe**: diz que dados e que operações têm todos os objetos de um certo tipo. A classe `Artigo` vai dizer três coisas:

- cada artigo tem um código, um nome e uma quantidade;
- cada artigo é criado com esses três valores;
- a cada artigo podemos pedir que retire unidades.

A classe não é uma linha preenchida do inventário. Descreve como são os artigos, mas não é, ela própria, o artigo A01 nem o artigo A02. A diferença é parecida com a que existe entre um impresso em branco e cada impresso depois de preenchido. O impresso em branco tem os campos "código", "nome" e "quantidade" por preencher.

Esta comparação com um impresso ajuda a perceber os dados, mas fica aquém num ponto importante: um impresso não faz nada, e uma classe também descreve as operações. Uma comparação mais completa é a de uma receita. A receita de um bolo diz que ingredientes são precisos e que passos seguir. Com a mesma receita podes fazer vários bolos, cada um no seu prato, e comer uma fatia de um não tira nenhuma fatia ao outro. A classe é a receita; cada artigo concreto é um bolo feito a partir dela, com o seu próprio estado.

Quando dizemos que um objeto é do tipo `Artigo`, estamos a dizer que foi feito a partir dessa descrição. Por isso, tem os dados e as operações de um artigo. "Artigo" não é o nome de um material. "Caderno" e "Pasta" são valores guardados no atributo `nome` de dois artigos concretos.

O erro típico aqui é pensar que precisamos de uma classe `Caderno` e de outra classe `Pasta`, porque são materiais diferentes. Não precisamos. Uma classe nova só se justifica quando os objetos precisam de dados ou de operações diferentes. Neste problema, cadernos e pastas guardam exatamente a mesma informação e aceitam exatamente as mesmas operações. O que muda é o valor do nome e da quantidade.

## Classe e instância

Uma **instância** de uma classe é um objeto concreto criado a partir dessa classe. "Objeto" é o termo geral; "instância de Artigo" é o mesmo objeto, dito de forma a sublinhar de que classe veio. O ato de criar um objeto a partir de uma classe chama-se **instanciar**.

Lê este esquema de cima para baixo. A parte de cima mostra a descrição comum. As duas colunas de baixo mostram objetos concretos, com valores preenchidos:

```text
                 Classe Artigo
        Dados: codigo, nome, quantidade
        Operação: retirar
                ↓                ↓
         Uma instância       Outra instância
         codigo: A01         codigo: A02
         nome: Caderno       nome: Pasta
         quantidade: 6       quantidade: 2
```

As setas representam a relação entre a descrição e os objetos feitos a partir dela. Não representam pedidos de retirada nem unidades a circular de um lado para o outro.

Temos uma classe e duas instâncias. A classe foi escrita uma vez; as instâncias podem ser tantas quantas os artigos do inventário. Cada instância tem os seus próprios atributos: o 6 está guardado na instância do caderno, e o 2 na instância da pasta.

## A classe Artigo em Python

Este é o primeiro programa completo do guia. Define a classe `Artigo`, cria as duas instâncias da tabela do início e mostra os seus atributos.

Antes de correres este programa, tenta prever: que duas linhas aparecem no ecrã? Olha para as duas últimas linhas do programa e para os valores escritos nas duas linhas que criam os artigos.

```python
# A classe Artigo e os dois artigos da sala: o primeiro programa do guia 02.

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

O programa mostra:

```text
A01 Caderno 6
A02 Pasta 2
```

Cada linha do ecrã mostra os três atributos de um artigo, pela ordem em que os pedimos no `print`.

Leitura guiada: começa pelas duas linhas que criam os artigos, `caderno = Artigo(...)` e `pasta = Artigo(...)`. Cada uma usa a descrição que está em cima, a classe, para criar um objeto. A classe só é usada quando uma destas linhas a chama. Depois vêm os dois `print`, que consultam os atributos de cada objeto. As subsecções seguintes leem o programa devagar, porque cada linha traz uma ideia nova.

### A linha `class Artigo:`

A primeira linha do programa é um comentário, que diz o que o programa é. A palavra `class` diz ao Python que vamos escrever a descrição de um tipo de objeto. `Artigo` é o nome da classe, e os dois pontos no fim da linha anunciam que a descrição vem a seguir. Tudo o que estiver indentado por baixo desta linha pertence à classe. Quando a indentação volta à margem, como na linha `caderno = ...`, a classe acabou.

Em Python, os nomes das classes escrevem-se com maiúscula inicial, e os nomes das variáveis com minúsculas. Não é obrigatório para o Python, mas toda a gente segue esta convenção porque ajuda a ler. `Artigo`, com maiúscula, é a descrição; `caderno`, com minúscula, é um artigo concreto.

A primeira linha dentro da classe é a sua docstring, o texto entre três aspas que explica para que serve a classe.

### O construtor `__init__`

Dentro da classe está definido um método com um nome especial: `__init__`, com dois sublinhados antes e dois depois. O Python reconhece um conjunto de nomes com esta forma, e cada um tem um papel fixo. Este é o **construtor**: o método que o Python executa automaticamente sempre que se cria um novo objeto da classe. A tarefa do construtor é preparar o objeto acabado de nascer, dando valores iniciais aos seus atributos.

Para criar um artigo não escreves `__init__`: escreves `Artigo(...)`, e é o Python que chama o construtor. É por isso que o construtor existe: garante que nenhum artigo começa a existir sem código, sem nome e sem quantidade.

### O parâmetro `self`

O construtor tem quatro parâmetros: `self`, `codigo`, `nome` e `quantidade`. Os três últimos são os dados do artigo. O primeiro, `self`, é diferente e aparece em todos os métodos de uma classe.

`self` é o nome que, dentro de um método, se refere ao objeto sobre o qual o método está a trabalhar. No construtor, `self` é o objeto que está a ser criado. Precisamos deste nome porque a classe é escrita uma única vez para todos os artigos. Quando escrevemos a classe, não sabemos se o método vai trabalhar sobre o caderno, sobre a pasta ou sobre um artigo que ainda nem existe. `self` quer dizer "este artigo, seja ele qual for".

Olha agora para a linha `self.codigo = codigo`. Os dois lados têm a palavra `codigo`, mas referem-se a coisas diferentes:

- à direita, `codigo` é o parâmetro, o valor que chegou na chamada, como `"A01"`. Tal como o parâmetro de uma função, só existe enquanto o construtor está a ser executado;
- à esquerda, `self.codigo` é o atributo `codigo` do objeto que está a ser criado. Fica guardado no objeto depois de o construtor terminar, e é por isso que mais tarde podemos escrever `caderno.codigo`.

A linha lê-se assim: "guarda no atributo `codigo` deste objeto o valor que chegou no parâmetro `codigo`". Os nomes são iguais porque é prático e habitual, mas podiam ser diferentes. O que decide que se trata de um atributo é o `self.` à frente.

A palavra `self` não é uma palavra reservada do Python; é uma convenção seguida por toda a gente. Usa sempre `self`, porque qualquer pessoa que leia o teu código espera encontrá-lo.

### Criar as instâncias

A linha `caderno = Artigo("A01", "Caderno", 6)` cria uma instância. O Python faz quatro coisas, por esta ordem:

1. Cria um objeto novo, do tipo `Artigo`, ainda sem atributos.
2. Chama o construtor com `self` a referir esse objeto novo, `codigo` igual a `"A01"`, `nome` igual a `"Caderno"` e `quantidade` igual a `6`.
3. O construtor guarda os três valores em três atributos do objeto novo.
4. O objeto, já preparado, fica associado ao nome `caderno`.

Repara que escrevemos três valores entre parênteses, mas o construtor tem quatro parâmetros. O que falta é o primeiro da lista, o `self`, e é o Python que o preenche com o objeto novo. Na chamada `Artigo(...)`, o `self` não se escreve.

A linha seguinte, `pasta = Artigo("A02", "Pasta", 2)`, repete os quatro passos e cria um segundo objeto, com os seus próprios atributos. O construtor foi executado duas vezes, uma por cada objeto. Esta tabela mostra, em cada execução, a linha que a provoca e o valor de cada parâmetro:

| Execução do construtor | Linha que a provoca | `self` | `codigo` | `nome` | `quantidade` |
| --- | --- | --- | --- | --- | --- |
| Primeira | `caderno = Artigo("A01", "Caderno", 6)` | O objeto novo que vai ficar com o nome `caderno` | `"A01"` | `"Caderno"` | `6` |
| Segunda | `pasta = Artigo("A02", "Pasta", 2)` | O objeto novo que vai ficar com o nome `pasta` | `"A02"` | `"Pasta"` | `2` |

### Consultar atributos

`caderno.nome` lê-se "o atributo `nome` do objeto `caderno`". O ponto liga o objeto ao atributo que queremos consultar. `print` recebe vários valores separados por vírgulas e mostra-os na mesma linha, com um espaço entre eles.

Se experimentares escrever `print(caderno)`, o Python mostra uma linha parecida com `<__main__.Artigo object at 0x...>`, com um número no fim que muda de execução para execução. Essa linha diz que se trata de um objeto do tipo `Artigo` e o sítio da memória onde está guardado. O `__main__` quer dizer que a classe foi definida no programa que mandaste executar. O Python não adivinha quais dos atributos queremos ver; por isso, pedimos cada atributo pelo nome.

## O método retirar em Python

Agora acrescentamos à classe o método `retirar` e fazemos, em Python, o pedido que viste em "Método: uma operação que pertence ao objeto": ao artigo A01, retira duas unidades. É outro programa completo.

Antes de correres, tenta prever: que três linhas aparecem no ecrã? Pensa sobretudo na quantidade da pasta na linha `Depois:`.

```python
# A classe Artigo com o método retirar: o segundo programa do guia 02.

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
        Nos programas deste guia só fazemos pedidos que sabemos serem válidos.
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

O programa mostra:

```text
Antes: 6 2
Depois: 4 2
Devolvido: 4
```

O caderno passou de 6 para 4, a pasta ficou com 2, e o método devolveu o 4 que ficou no caderno.

Leitura guiada: começa pela linha `restante = caderno.retirar(2)`, que é o pedido. Depois sobe ao método `retirar`, para veres o que esse pedido faz ao caderno. Por fim, lê os três `print`, que mostram o estado antes e depois do pedido e o valor que o método devolveu. Os parágrafos seguintes seguem esta ordem.

O método `retirar` escreve-se dentro da classe, com a mesma indentação do construtor. Tem dois parâmetros: `self`, o artigo que recebe o pedido, e `unidades`, quantas unidades se querem retirar. `unidades` é um **parâmetro**: um nome que, dentro do método, representa um valor que só vai ser conhecido no momento da chamada. Graças a ele, o método não fica preso a retirar sempre duas unidades.

Na chamada `caderno.retirar(2)` há três peças. `caderno` é o objeto que recebe o pedido, `retirar` é o método e `2` é o **argumento**, o valor concreto que vai ocupar o parâmetro `unidades`. O Python põe o objeto `caderno` no parâmetro `self` e o `2` no parâmetro `unidades`. Na chamada `caderno.retirar(2)`, o `self` não se escreve entre parênteses: o objeto que está antes do ponto é o que vai ocupar o `self`.

A chamada `caderno.retirar(2)` dá exatamente o mesmo que `Artigo.retirar(caderno, 2)`. Nesta forma longa, o objeto que ocupa o `self` vai em primeiro lugar entre parênteses. Ou seja, "executa o método `retirar` da classe `Artigo`, com `self` igual a `caderno` e `unidades` igual a 2".

Vejamos o que acontece dentro do método nessa chamada. Na linha `self.quantidade = self.quantidade - unidades`, o Python calcula primeiro o lado direito. Como `self` é o caderno, `self.quantidade` vale 6, e `6 - 2` dá 4. Depois guarda esse 4 no atributo `quantidade` do caderno. O atributo da pasta nunca é lido nem escrito, porque em nenhum momento o `self` foi a pasta.

A linha `return self.quantidade` **devolve** o valor 4 a quem chamou o método. Devolver não é o mesmo que mostrar no ecrã. `return` entrega o valor ao programa, que pode guardá-lo, usá-lo numa conta ou ignorá-lo. `print` mostra um valor a uma pessoa. No programa, guardamos o valor devolvido na variável `restante` e só depois o mostramos com `print`. Se tivéssemos escrito apenas `caderno.retirar(2)`, sem guardar o resultado, o 4 devolvido perdia-se. O caderno ficava com 4 na mesma, porque a alteração do atributo aconteceu dentro do método.

Acompanha a execução pela ordem das mensagens:

| Mensagem | Significado |
| --- | --- |
| `Antes: 6 2` | Quantidades de A01 e A02 antes da chamada |
| `Depois: 4 2` | Quantidades depois de retirar 2 a A01; A02 ficou igual |
| `Devolvido: 4` | Valor que o método entregou a quem o chamou |

Por enquanto, escolhemos apenas retiradas que sabemos serem possíveis. Este método ainda não verifica nada: se pedíssemos a um caderno com 6 unidades que retirasse 9, guardaria -3. No guia 03 vais ver porque é que essa verificação tem de fazer parte do próprio objeto, e como se escreve em Python.

## Cada instância é um objeto diferente

Cada vez que escreves `Artigo(...)`, nasce um objeto novo, com os seus próprios atributos. Mas nem todas as linhas que parecem criar um objeto o fazem. Este programa completo mostra a diferença. As duas últimas linhas usam a palavra `is`, que pergunta se dois nomes apontam para o mesmo objeto. A resposta é `True` (verdadeiro) ou `False` (falso).

Antes de correres, tenta prever as quatro linhas: com que quantidade fica o caderno, com que quantidade fica a pasta, e o que responde cada `is`?

```python
# Dois nomes para o mesmo artigo: o terceiro programa do guia 02.

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
        Nos programas deste guia só fazemos pedidos que sabemos serem válidos.
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

O programa mostra:

```text
Caderno: 5
Pasta: 2
True
False
```

O pedido foi feito através do nome `mesmo_caderno`, e foi o caderno que perdeu uma unidade.

Leitura guiada: o que interessa está nas três linhas que vêm depois da classe, `caderno = ...`, `pasta = ...` e `mesmo_caderno = caderno`. Conta quantas delas têm `Artigo(...)`. Depois segue o pedido `mesmo_caderno.retirar(1)` até ao objeto que o recebe, e só no fim lê os quatro `print`.

A linha `mesmo_caderno = caderno` não cria nenhum artigo, porque não tem `Artigo(...)`. O que faz é dar um segundo nome ao objeto que já existia. Uma variável não contém o objeto: é um nome que aponta para ele. Imagina duas etiquetas coladas na mesma caixa. Retirar uma unidade usando o nome `mesmo_caderno` é retirá-la da única caixa que existe, e por isso `caderno.quantidade` passou a 5.

Desenhado com caixas e etiquetas, o fim do programa fica assim. Cada caixa é um objeto, e cada etiqueta é um nome que aponta para ele:

```text
caderno ─────────┐
                 ├──→ caixa 1: A01, Caderno, quantidade 5
mesmo_caderno ───┘

pasta ───────────────→ caixa 2: A02, Pasta, quantidade 2
```

`caderno is mesmo_caderno` dá `True`, porque as duas etiquetas estão na mesma caixa. `caderno is pasta` dá `False`, porque são duas caixas diferentes, criadas por duas chamadas a `Artigo(...)`.

Isto vai ser importante no guia 04, quando um inventário guardar uma lista de artigos. A lista não guarda cópias dos artigos: guarda os próprios objetos. Um pedido feito através da lista chega ao mesmo objeto que foi criado no início. O seu efeito vê-se por qualquer um dos nomes que apontam para ele.

## Exemplo guiado: retirar duas unidades a um dos artigos

Já viste todas as peças. Agora resolvemos um pedido do princípio ao fim: primeiro em papel, como no guia 01, e depois em Python.

O enunciado: na sala há dois artigos, A01 (Caderno, com 6 unidades) e A02 (Pasta, com 2 unidades). Pede-se ao artigo A01 que retire duas unidades. Com que quantidade fica cada artigo, e que valor devolve o pedido?

### Em papel

1. Identificamos o objeto que recebe o pedido: o artigo A01.
2. Consultamos a sua quantidade atual: 6.
3. Aplicamos a operação: 6 - 2 = 4.
4. Guardamos o resultado apenas na quantidade de A01.

| Momento | Quantidade de A01 | Quantidade de A02 |
| --- | ---: | ---: |
| Antes do pedido | 6 | 2 |
| Depois de retirar 2 a A01 | 4 | 2 |

A classe continua igual: nenhuma descrição mudou. A01 continua a ser o mesmo artigo, com o mesmo código e o mesmo nome. O que mudou foi um valor no estado dessa instância. A02 não foi tocado, porque o pedido não lhe foi feito. Usar a mesma classe não significa partilhar a mesma quantidade: cada instância tem os seus próprios atributos. O pedido devolve a quantidade que fica em A01, que é 4.

### Em Python

Cada passo do papel corresponde a uma parte da chamada `caderno.retirar(2)`, que viste em "O método retirar em Python":

| Passo em papel | Onde acontece em Python |
| --- | --- |
| 1. O objeto que recebe o pedido | `caderno`, antes do ponto, que ocupa o `self` |
| 2. A quantidade atual | `self.quantidade`, lido no lado direito da atribuição |
| 3. A operação | `self.quantidade - unidades`, com `unidades` igual a 2 |
| 4. Guardar só em A01 | `self.quantidade = ...`, com o `self` a ser o caderno |

O valor devolvido é o do `return self.quantidade`, lido depois do passo 4.

O papel diz também que o código e o nome de A01 ficaram iguais. Para o confirmar, juntamos ao segundo programa duas linhas que mostram cada artigo inteiro, atributo a atributo. Antes de correres, escreve as cinco linhas que esperas ver. As três primeiras já as conheces.

```python
# Exemplo guiado do guia 02: retirar duas unidades ao artigo A01.

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
        Nos programas deste guia só fazemos pedidos que sabemos serem válidos.
        """
        self.quantidade = self.quantidade - unidades
        return self.quantidade


caderno = Artigo("A01", "Caderno", 6)
pasta = Artigo("A02", "Pasta", 2)

print("Antes:", caderno.quantidade, pasta.quantidade)
restante = caderno.retirar(2)
print("Depois:", caderno.quantidade, pasta.quantidade)
print("Devolvido:", restante)
print(caderno.codigo, caderno.nome, caderno.quantidade)
print(pasta.codigo, pasta.nome, pasta.quantidade)
```

O programa mostra:

```text
Antes: 6 2
Depois: 4 2
Devolvido: 4
A01 Caderno 4
A02 Pasta 2
```

Leitura guiada: a classe e as linhas até `print("Devolvido:", restante)` são as do segundo programa. As duas linhas novas, no fim, consultam os três atributos de cada artigo, como no primeiro programa.

Para confirmar que o resultado está certo, compara cada linha com o papel:

- `Antes: 6 2` é a primeira linha da tabela, e `Depois: 4 2` é a segunda. A02 continua com 2, porque o `self` nunca foi a pasta.
- `Devolvido: 4` é o valor calculado no passo 3 e guardado no passo 4.
- `A01 Caderno 4` mostra o mesmo código e o mesmo nome de antes: é o mesmo artigo, e só mudou a quantidade.
- `A02 Pasta 2` mostra a pasta exatamente como foi criada.

Nenhuma linha do programa mexe na classe: o pedido mudou o estado de uma instância, e não a descrição comum.

## Erros frequentes

O erro típico de cada ideia está na secção dela:

- uma classe para cada material, em "Classe: a descrição comum";
- o `print` de um objeto inteiro, em "Consultar atributos";
- devolver e mostrar, e o pedido que deixa a quantidade negativa, em "O método retirar em Python";
- um segundo nome tomado por um objeto novo, em "Cada instância é um objeto diferente".

Ficam aqui os erros de escrita que aparecem quando se escreve uma classe pela primeira vez. Em cada um, lê a última linha da mensagem de erro: é a que diz o que aconteceu.

### O Python diz que a classe não aceita valores

O que se vê: o programa para na linha que cria o primeiro artigo, e a última linha da mensagem é `TypeError: Artigo() takes no arguments`. Em português: `Artigo()` não aceita argumentos. Um `TypeError` ("erro de tipo") é o erro que o Python dá quando uma operação recebe valores que não aceita.

Porque acontece: o nome do construtor está mal escrito, por exemplo `_init_`, com um só sublinhado de cada lado, ou `__innit__`, com um `n` a mais. O Python só reconhece como construtor um método chamado exatamente `__init__`. Com outro nome, a classe fica sem nenhum construtor que aceite valores. O método mal escrito continua a existir, mas ninguém o chama.

Como se corrige: escreve o nome como `__init__`, com dois sublinhados, a palavra `init` e mais dois sublinhados.

### O objeto não tem o método

O que se vê: `AttributeError: 'Artigo' object has no attribute 'retirar'`. Em português: o objeto do tipo `Artigo` não tem nenhum atributo chamado `retirar`. Um `AttributeError` ("erro de atributo") aparece quando se pede a um objeto um atributo que ele não tem, e o Python usa a palavra atributo também para os métodos.

Porque acontece: a linha `def retirar(self, unidades):` ficou encostada à margem, fora da classe. O Python aceita-a como uma função solta, e os objetos `Artigo` não a têm.

Como se corrige: põe o `def` com quatro espaços e as linhas de dentro do método com oito, como no construtor.

### O Python não conhece o nome da classe

O que se vê: `NameError: name 'artigo' is not defined`, em português "o nome `artigo` não está definido". Um `NameError` ("erro de nome") aparece quando se usa um nome que o Python não conhece. A partir do Python 3.10, a mensagem acrescenta uma sugestão: `Did you mean: 'Artigo'?`, isto é, "querias dizer `Artigo`?".

Porque acontece: a classe foi escrita com maiúscula, `Artigo`, e a chamada com minúscula, `artigo(...)`, ou ao contrário. Para o Python, são dois nomes diferentes.

Como se corrige: escreve o nome da classe sempre da mesma maneira, com maiúscula.

### As linhas do construtor sem indentação

O que se vê depende das linhas que ficaram sem a indentação certa.

Se todo o corpo do construtor, com a docstring, ficou com quatro espaços, a mesma indentação da linha `def __init__`, aparece um `IndentationError` ("erro de indentação"). No primeiro programa deste guia, a mensagem começa por `File "...", line 7`: é a linha onde o Python esperava o bloco indentado, a da docstring. A última linha é `IndentationError: expected an indented block after function definition on line 6`. Em português: esperava-se um bloco indentado a seguir à definição da função da linha 6. O `on line 6` do fim é a linha do `def`. Nas versões anteriores ao Python 3.10, a última linha acaba em `expected an indented block`, sem dizer a linha do `def`.

Se só as três linhas que começam por `self.` ficaram com quatro espaços, e a docstring ficou com oito, a mensagem é outra, e engana: `NameError: name 'codigo' is not defined`.

Porque acontece: o Python decide pela indentação que linhas pertencem ao método. No primeiro caso, não encontra nenhuma linha dentro do construtor. No segundo, o construtor fica só com a docstring, e as três linhas passam a pertencer à classe, fora do método. Aí, o parâmetro `codigo` não existe, e o Python queixa-se dele.

Como se corrige: põe o `def` com quatro espaços e as linhas de dentro do método com oito, incluindo a docstring.

## Palavras novas deste guia

- Objeto: uma unidade que reúne dados sobre uma coisa e as operações que trabalham sobre esses dados.
- Atributo: um dado guardado num objeto, com um nome e um valor, como `quantidade` e `6`.
- Estado de um objeto: o conjunto dos valores dos seus atributos num dado momento.
- Método: uma operação que pertence a um objeto e trabalha sobre os dados desse objeto.
- Definir um método: escrever as instruções que dizem como a operação funciona; faz-se uma vez.
- Chamar um método: pedir que essas instruções sejam executadas agora, sobre um objeto concreto.
- Classe: a descrição comum dos dados e das operações de todos os objetos de um certo tipo.
- Instância: um objeto concreto criado a partir de uma classe.
- Instanciar: criar um objeto a partir de uma classe.
- Construtor: o método `__init__`, que o Python executa sozinho sempre que se cria um objeto, para lhe dar os valores iniciais.
- `self`: o nome que, dentro de um método, se refere ao objeto sobre o qual o método está a trabalhar.
- Parâmetro: um nome que, dentro de um método, representa um valor que só se conhece no momento da chamada.
- Argumento: o valor concreto que ocupa um parâmetro numa chamada, como o `2` de `caderno.retirar(2)`.
- Devolver: entregar um valor a quem chamou o método, com `return`. Não é o mesmo que mostrar no ecrã.
- `is`: a palavra que pergunta se dois nomes apontam para o mesmo objeto.

## Verificar o que aprendeste

Tenta responder sem olhar para o texto. Se uma pergunta te deixar com dúvidas, volta à secção indicada. As perguntas 6 e 7 pedem que executes um programa. Escreve a previsão antes; se a execução der outra coisa, procura a explicação em vez de mudar a previsão.

1. Qual é a diferença entre a classe `Artigo` e o objeto `caderno`? ("Classe: a descrição comum" e "Classe e instância")
2. Quando é executado o construtor, e quem o chama? ("A classe Artigo em Python")
3. Na chamada `pasta.retirar(1)`, quem é o `self`? ("O método retirar em Python")
4. Na chamada `caderno.retirar(2)`, o que é o parâmetro e o que é o argumento? ("O método retirar em Python")
5. Porque é que `mesmo_caderno = caderno` não cria um artigo novo? ("Cada instância é um objeto diferente")
6. Lê este programa completo, sem o executar:

   ```python
   # A caneta e a borracha: a pergunta 6 do guia 02.

   class Artigo:
       """Descreve um artigo do inventário: um material com código, nome e quantidade."""

       def __init__(self, codigo, nome, quantidade):
           """Prepara um artigo acabado de criar, guardando os três dados recebidos."""
           self.codigo = codigo
           self.nome = nome
           self.quantidade = quantidade


   caneta = Artigo("A03", "Caneta", 8)
   borracha = Artigo("A04", "Borracha", 3)
   print(caneta.nome, borracha.quantidade)
   ```

   1. Escreve o nome da classe e os nomes das duas instâncias.
   2. Quantas vezes é executado o construtor, e em que linhas? Para cada execução, faz uma tabela com o valor de `self` (qual dos objetos), `codigo`, `nome` e `quantidade`.
   3. Escreve a linha que esperas ver no ecrã. Depois executa o programa e compara.
   4. Explica por que razão a quantidade 8 não significa que foram criadas oito instâncias para as canetas.
7. Acrescenta, no fim do primeiro programa de "A classe Artigo em Python", a linha seguinte. É um excerto, que precisa da classe desse programa:

   ```python partial
   lapis = Artigo("A05", "Lápis")
   ```

   Antes de executares, escreve o que achas que vai acontecer. Depois executa e lê a última linha da mensagem de erro que o Python mostra. A palavra inglesa `positional` quer dizer "posicional": um argumento posicional é um valor que vai para um parâmetro pela ordem em que está escrito.

   1. Que parâmetro está em falta, segundo a mensagem?
   2. A mensagem fala de `__init__`, mas a linha que escreveste não tem `__init__`. Explica porquê.
   3. Porque é que o Python não se queixa da falta do `self`, que também não foi escrito?

Se ainda confundes classe e instância, volta ao esquema de "Classe e instância". Pergunta-te se estás a olhar para a descrição comum ou para uma ficha com valores concretos.

## O que vem a seguir

Para praticar este tema, faz o [laboratório](02-objetos-classes-instancias-laboratorio.md) e depois a [ficha de exercícios](02-objetos-classes-instancias-exercicios.md). A ficha acaba com exercícios para ires mais longe, que fazes quando quiseres aprofundar ou quando o professor os indicar.

O tema seguinte é [Encapsulamento e contratos](03-encapsulamento-contratos.md). Lá vais impedir que uma operação deixe os valores de um artigo num estado inválido, como os -3 cadernos de um pedido impossível.

![Rodapé](../imagens/rodape.png)

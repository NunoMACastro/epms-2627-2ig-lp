![Cabeçalho](../imagens/cabecalho.png)

# Objetos e classes: uma descrição comum, vários artigos

*M10 · Caderno 2*

No [caderno anterior](01-entidades-estado-acoes.md) organizámos a informação sobre os materiais de uma sala e vimos o problema das variáveis soltas: o programa guardava o código, o nome e a quantidade de cada artigo em variáveis separadas, e nada impedia que a quantidade de um artigo fosse entregue a outro por engano. Neste caderno vamos ver como o Python junta os dados de um artigo e as operações que lhe dizem respeito numa só unidade, o objeto, e como uma classe descreve todos os objetos do mesmo tipo.

Este caderno acompanha as aulas em que trabalhaste classes, objetos, atributos, o construtor e o `self`. Aqui encontras essas ideias escritas por extenso, uma de cada vez, com programas que podes executar.

Os blocos de código apresentados como programa completo podem ser copiados para um ficheiro novo com a extensão `.py` e executados no editor de Python que usas nas aulas, tal como no caderno 1. Executa sempre o ficheiro inteiro: cada execução começa do zero, com os valores iniciais escritos no programa. Os blocos apresentados como excerto não correm sozinhos, e o texto diz sempre de que outro código dependem.

## 1. O que estamos a representar

Imagina uma sala onde estão guardados cadernos e pastas. Para saber o que existe, fazemos este registo:

| Código | Nome do material | Quantidade disponível |
| --- | --- | ---: |
| A01 | Caderno | 6 |
| A02 | Pasta | 2 |

Como vimos no caderno 1, um artigo é uma referência de material no inventário. A ficha A01 representa o material "Caderno", do qual existem seis unidades. Não estamos a criar uma ficha para cada um dos seis cadernos físicos. A ficha A02 representa outro material, "Pasta".

Temos, portanto, dois artigos, apesar de existirem oito unidades físicas ao todo. Se a quantidade de cadernos passar de 6 para 5, continuamos a ter a mesma ficha A01, agora com um valor atualizado.

O programa não vê a sala nem o armário. Só conhece a informação que lhe damos. Temos, por isso, de lhe dizer o que interessa guardar sobre cada artigo e o que deve ser possível fazer com essa informação.

## 2. Um objeto reúne dados e operações

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

No caderno 1 chamámos estado ao conjunto dos valores de uma entidade num certo momento. Num objeto é igual: o **estado de um objeto** é o conjunto dos valores dos seus atributos num dado momento. Código A01, nome Caderno e quantidade 6 descrevem um estado. Código A01, nome Caderno e quantidade 4 descrevem um estado posterior do mesmo objeto.

Uma nota sobre vocabulário. Em muitos livros, e noutras linguagens de programação, os atributos também se chamam propriedades. Em Python, a palavra propriedade tem um sentido mais preciso, que vais estudar no caderno 3. Por isso, nestes cadernos dizemos sempre atributo para os dados guardados num objeto.

## 3. Método: uma operação que pertence ao objeto

Um **método** é uma operação que pertence a um objeto. Tal como uma função, um método tem um nome, pode receber valores, executa instruções e pode devolver um resultado. A diferença é a ligação ao objeto: um método trabalha sobre os dados do objeto a que pertence.

Por exemplo, o método `retirar` representa a operação de retirar unidades. Dizer apenas "retirar" não chega. Precisamos de dizer a que artigo e quantas unidades. Um pedido completo seria:

> Ao artigo A01, pede para retirar duas unidades.

Se A01 tinha 6 unidades, passa a ter 4. O artigo A02 não recebeu esse pedido e continua com 2. Quem recebe o pedido, que operação se pede e com que valor: são estas três coisas que vamos acompanhar sempre que um método for usado.

Definir um método e chamar um método são momentos diferentes. **Definir** um método é escrever as instruções que dizem como a operação funciona; escreve-se uma vez. **Chamar** um método é pedir que essas instruções sejam executadas agora, sobre um objeto concreto; pode acontecer muitas vezes, ou nenhuma. Ter uma operação definida não significa que ela já tenha acontecido, da mesma maneira que uma receita escrita num livro não significa que o bolo já esteja feito.

Nem todos os métodos alteram dados. Um método que consulte a quantidade fornece informação, mas não precisa de modificar o estado. Já vimos no caderno 1 que consultar também é uma operação.

## 4. Classe: a descrição comum

Olha outra vez para as duas linhas do inventário. Os valores são diferentes, mas a organização é igual: ambos os artigos têm código, nome e quantidade. Também faz sentido retirar unidades de qualquer um deles, e a operação faz-se da mesma maneira nos dois: subtrai-se o pedido à quantidade.

Em vez de descrevermos esta organização de novo para cada artigo, escrevemos uma descrição comum, uma só vez. Essa descrição é uma **classe**: diz que dados e que operações têm todos os objetos de um certo tipo. A classe `Artigo` vai dizer três coisas: cada artigo tem um código, um nome e uma quantidade; cada artigo é criado com esses três valores; e a cada artigo podemos pedir que retire unidades.

A classe não é uma linha preenchida do inventário. Descreve como são os artigos, mas não é, ela própria, o artigo A01 nem o artigo A02. A diferença é parecida com a que existe entre um impresso em branco, com os campos "código", "nome" e "quantidade" por preencher, e cada impresso depois de preenchido.

Esta comparação com um impresso ajuda a perceber os dados, mas fica aquém num ponto importante: um impresso não faz nada, e uma classe também descreve as operações. Uma comparação mais completa é a de uma receita. A receita de um bolo diz que ingredientes são precisos e que passos seguir. Com a mesma receita podes fazer vários bolos, cada um no seu prato, e comer uma fatia de um não tira nenhuma fatia ao outro. A classe é a receita; cada artigo concreto é um bolo feito a partir dela, com o seu próprio estado.

Quando dizemos que um objeto é do tipo `Artigo`, estamos a dizer que foi feito a partir dessa descrição e que, por isso, tem os dados e as operações de um artigo. "Artigo" não é o nome de um material. "Caderno" e "Pasta" são valores guardados no atributo `nome` de dois artigos concretos.

O erro típico aqui é pensar que precisamos de uma classe `Caderno` e de outra classe `Pasta`, porque são materiais diferentes. Não precisamos. Uma classe nova só se justifica quando os objetos precisam de dados ou de operações diferentes. Neste problema, cadernos e pastas guardam exatamente a mesma informação e aceitam exatamente as mesmas operações; o que muda é o valor do nome e da quantidade.

## 5. Classe e instância

Uma **instância** de uma classe é um objeto concreto criado a partir dessa classe. "Objeto" é o termo geral; "instância de Artigo" é o mesmo objeto, dito de forma a sublinhar de que classe veio. O ato de criar um objeto a partir de uma classe chama-se instanciar.

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

Temos uma classe e duas instâncias. A classe foi escrita uma vez; as instâncias podem ser tantas quantas os artigos do inventário.

### Exemplo guiado: retirar duas unidades a um dos artigos

Vamos acompanhar o pedido "ao artigo A01, retira duas unidades", primeiro em papel e depois, nas secções 6 e 7, em Python.

1. Identificamos o objeto que recebe o pedido: o artigo A01.
2. Consultamos a sua quantidade atual: 6.
3. Aplicamos a operação: 6 - 2 = 4.
4. Guardamos o resultado apenas na quantidade de A01.

| Momento | Quantidade de A01 | Quantidade de A02 |
| --- | ---: | ---: |
| Antes do pedido | 6 | 2 |
| Depois de retirar 2 a A01 | 4 | 2 |

A classe continua igual: nenhuma descrição mudou. A01 continua a ser o mesmo artigo, com o mesmo código e o mesmo nome. O que mudou foi um valor no estado dessa instância. A02 não foi tocado, porque o pedido não lhe foi feito. Usar a mesma classe não significa partilhar a mesma quantidade: cada instância tem os seus próprios atributos.

## 6. A classe Artigo em Python

Este é o primeiro programa completo do caderno. Define a classe `Artigo`, cria as duas instâncias da tabela e mostra os seus atributos.

```python
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

Vamos ler este programa devagar, porque cada linha traz uma ideia nova.

### A linha `class Artigo:`

A palavra `class` diz ao Python que vamos escrever a descrição de um tipo de objeto. `Artigo` é o nome da classe, e os dois pontos no fim da linha anunciam que a descrição vem a seguir. Tudo o que estiver indentado por baixo desta linha pertence à classe. Quando a indentação volta à margem, como na linha `caderno = ...`, a classe acabou.

Em Python, os nomes das classes escrevem-se com maiúscula inicial, e os nomes das variáveis com minúsculas. Não é obrigatório para o Python, mas toda a gente segue esta convenção porque ajuda a ler: `Artigo`, com maiúscula, é a descrição; `caderno`, com minúscula, é um artigo concreto.

A primeira linha dentro da classe é a sua docstring, o texto entre três aspas que explica para que serve a classe.

### O construtor `__init__`

Dentro da classe está definido um método com um nome especial: `__init__`, com dois sublinhados antes e dois depois. Os nomes com esta forma são reconhecidos pelo próprio Python e têm um papel fixo. Este é o **construtor**: o método que o Python executa automaticamente sempre que se cria um novo objeto da classe. A tarefa do construtor é preparar o objeto acabado de nascer, dando valores iniciais aos seus atributos.

Nunca escrevemos `__init__` para o chamar. Quem o chama é o Python, no momento em que escrevemos `Artigo(...)`. É por isso que o construtor existe: garante que nenhum artigo começa a existir sem código, sem nome e sem quantidade.

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

Repara que escrevemos três valores entre parênteses, mas o construtor tem quatro parâmetros. O quarto, que é o primeiro da lista, é o `self`, e é o Python que o preenche com o objeto novo. Nunca se escreve o `self` na chamada.

A linha seguinte, `pasta = Artigo("A02", "Pasta", 2)`, repete os quatro passos e cria um segundo objeto, com os seus próprios atributos. O construtor foi executado duas vezes, uma por cada objeto.

### Consultar atributos

`caderno.nome` lê-se "o atributo `nome` do objeto `caderno`". O ponto liga o objeto ao atributo que queremos consultar. `print` recebe vários valores separados por vírgulas e mostra-os na mesma linha, com um espaço entre eles.

Se experimentares escrever `print(caderno)`, o Python mostra uma linha parecida com `<__main__.Artigo object at 0x...>`, com um número no fim que muda de execução para execução. Essa linha diz que se trata de um objeto do tipo `Artigo` e o sítio da memória onde está guardado. O Python não adivinha quais dos atributos queremos ver; por isso, pedimos cada atributo pelo nome.

## 7. O método retirar em Python

Agora acrescentamos à classe o método `retirar` e fazemos, em Python, o exemplo guiado da secção 5. É outro programa completo:

```python
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
        Nos programas deste caderno só fazemos pedidos que sabemos serem válidos.
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

O método `retirar` escreve-se dentro da classe, com a mesma indentação do construtor. Tem dois parâmetros: `self`, o artigo que recebe o pedido, e `unidades`, quantas unidades se querem retirar. `unidades` é um **parâmetro**: um nome que, dentro do método, representa um valor que só vai ser conhecido no momento da chamada. Graças a ele, o método não fica preso a retirar sempre duas unidades.

Na chamada `caderno.retirar(2)` há três peças: `caderno` é o objeto que recebe o pedido, `retirar` é o método e `2` é o **argumento**, o valor concreto que vai ocupar o parâmetro `unidades`. O Python põe o objeto `caderno` no parâmetro `self` e o `2` no parâmetro `unidades`. Tal como no construtor, o `self` não se escreve entre parênteses: o objeto que está antes do ponto é o que vai ocupar o `self`. É mesmo isto que o Python faz por dentro: a chamada `caderno.retirar(2)` é tratada como `Artigo.retirar(caderno, 2)`, ou seja, "executa o método `retirar` da classe `Artigo`, com `self` igual a `caderno` e `unidades` igual a 2".

Vejamos o que acontece dentro do método nessa chamada. Na linha `self.quantidade = self.quantidade - unidades`, o Python calcula primeiro o lado direito. Como `self` é o caderno, `self.quantidade` vale 6, e `6 - 2` dá 4. Depois guarda esse 4 no atributo `quantidade` do caderno. O atributo da pasta nunca é lido nem escrito, porque em nenhum momento o `self` foi a pasta.

A linha `return self.quantidade` **devolve** o valor 4 a quem chamou o método. Devolver não é o mesmo que mostrar no ecrã. `return` entrega o valor ao programa, que pode guardá-lo, usá-lo numa conta ou ignorá-lo. `print` mostra um valor a uma pessoa. No programa, guardamos o valor devolvido na variável `restante` e só depois o mostramos com `print`. Se tivéssemos escrito apenas `caderno.retirar(2)`, sem guardar o resultado, o 4 devolvido perdia-se, mas o caderno ficava com 4 na mesma, porque a alteração do atributo aconteceu dentro do método.

Acompanha a execução pela ordem das mensagens:

| Mensagem | Significado |
| --- | --- |
| `Antes: 6 2` | Quantidades de A01 e A02 antes da chamada |
| `Depois: 4 2` | Quantidades depois de retirar 2 a A01; A02 ficou igual |
| `Devolvido: 4` | Valor que o método entregou a quem o chamou |

Por enquanto, escolhemos apenas retiradas que sabemos serem possíveis. Este método ainda não verifica nada: se lhe pedíssemos para retirar 9 unidades ao caderno, guardaria -3. No caderno 3 vamos ver porque é que essa verificação tem de fazer parte do próprio objeto, e como se escreve em Python.

## 8. Cada instância é um objeto diferente

Cada vez que escreves `Artigo(...)`, nasce um objeto novo, com os seus próprios atributos. Mas nem todas as linhas que parecem criar um objeto o fazem. Este programa completo mostra a diferença:

```python
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
        Nos programas deste caderno só fazemos pedidos que sabemos serem válidos.
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

A linha `mesmo_caderno = caderno` não cria nenhum artigo, porque não tem `Artigo(...)`. O que faz é dar um segundo nome ao objeto que já existia. Uma variável não contém o objeto: é um nome que aponta para ele. Imagina duas etiquetas coladas na mesma caixa. Retirar uma unidade usando o nome `mesmo_caderno` é retirá-la da única caixa que existe, e por isso `caderno.quantidade` passou a 5.

A palavra `is` pergunta se dois nomes apontam para o mesmo objeto. `caderno is mesmo_caderno` dá `True` (verdadeiro), porque as duas etiquetas estão na mesma caixa. `caderno is pasta` dá `False` (falso), porque são duas caixas diferentes, criadas por duas chamadas a `Artigo(...)`.

Isto vai ser importante no caderno 4, quando um inventário guardar uma lista de artigos. A lista não guarda cópias dos artigos: guarda os próprios objetos. Um pedido feito através da lista chega ao mesmo objeto que foi criado no início, e o seu efeito vê-se por qualquer um dos nomes que apontam para ele.

## 9. Agora experimenta

Cada exercício pede uma decisão que o exemplo guiado não tomou por ti. Antes de executares qualquer programa, escreve a tua previsão; se a execução der outra coisa, procura a explicação em vez de mudar a previsão. Entrega as respostas pelo meio indicado pelo professor.

### Exercício 1: Ler um programa antes de o executar

Lê este programa completo, sem o executar:

```python
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

### Exercício 2: Um nome que muda de objeto

Este excerto não corre sozinho: precisa da classe `Artigo` com o método `retirar`, tal como está no programa da secção 7. Para o executares, copia esse programa e substitui as linhas que vêm depois da classe (a partir de `caderno = ...`) por estas:

```python partial
caneta = Artigo("A03", "Caneta", 8)
borracha = Artigo("A04", "Borracha", 3)
escolhido = borracha
caneta.retirar(2)
escolhido.retirar(1)
escolhido = caneta
escolhido.retirar(3)
print(caneta.quantidade, borracha.quantidade)
```

Constrói um traço com uma linha por instrução e três colunas: a quantidade da caneta, a quantidade da borracha e o objeto para o qual aponta o nome `escolhido` depois dessa instrução. Escreve a linha que esperas ver no ecrã e só depois executa. No fim, explica por palavras o que mudou na linha `escolhido = caneta` e o que não mudou.

### Exercício 3: Um método novo, adicionar

Acrescenta à classe `Artigo` do programa da secção 7 um método `adicionar`, que acrescenta unidades à quantidade de um artigo. Não precisas de verificar se o pedido é válido: isso fica para o caderno 3.

Antes de escreveres o método, tens de tomar uma decisão que o exemplo não tomou por ti: o que é que `adicionar` devolve? Pode devolver a quantidade que fica, como o `retirar`, ou pode não devolver nada. Escolhe uma das opções e justifica-a numa frase, a pensar em quem vai usar o método. Escreve a docstring do método de acordo com a tua escolha.

Depois escreve, no fim do programa, as linhas necessárias para adicionar 4 unidades à pasta e em seguida retirar-lhe 1, e para mostrar as quantidades dos dois artigos no fim. Prevê o que vai aparecer no ecrã e confirma executando.

### Exercício 4: Dois colegas, dois erros

Dois colegas escreveram versões diferentes do método `retirar`. Os excertos seguintes são só o método, e não correm sozinhos: para os experimentares, substitui o `retirar` do programa da secção 7 por cada um deles, à vez.

Versão do colega A:

```python partial
    def retirar(self, unidades):
        """Retira unidades a este artigo e devolve a quantidade que fica."""
        quantidade = self.quantidade - unidades
        return quantidade
```

Versão do colega B:

```python partial
    def retirar(self, unidades):
        """Retira unidades a este artigo e devolve a quantidade que fica."""
        self.quantidade = unidades
        return self.quantidade
```

Para cada versão, e para um caderno com 6 unidades a que se pede `caderno.retirar(2)`, responde:

1. Que valor devolve o método?
2. Com que quantidade fica o caderno depois da chamada?
3. Qual é o erro, explicado por palavras? No caso do colega A, a tua explicação tem de usar a palavra `self`.

Termina com esta pergunta: se só olhasses para o valor devolvido, qual das duas versões parecia estar certa? O que é que isso te ensina sobre a forma de verificar um método?

### Exercício 5: Ler uma mensagem de erro

Este excerto precisa da classe do programa da secção 6. Acrescenta-o no fim desse programa:

```python partial
lapis = Artigo("A05", "Lápis")
```

Antes de executares, escreve o que achas que vai acontecer. Depois executa e lê a última linha da mensagem de erro que o Python mostra. Responde:

1. Que parâmetro está em falta, segundo a mensagem?
2. A mensagem fala de `__init__`, mas a linha que escreveste não tem `__init__`. Explica porquê.
3. Porque é que o Python não se queixa da falta do `self`, que também não foi escrito?

### Exercício 6: A tua própria representação

Escolhe dois materiais internos fictícios, com código, nome e quantidade inicial. Escreve um programa completo, com a classe `Artigo` da secção 7, que crie as duas instâncias e faça uma sequência de três chamadas a `retirar`, todas possíveis, de forma que um dos artigos acabe com a quantidade exatamente em zero. Terás de escolher os números com cuidado antes de escrever as chamadas.

Antes de executares, escreve o traço da sequência, com a quantidade dos dois artigos depois de cada chamada. Depois executa, mostrando as quantidades no fim, e compara com o traço.

Por baixo do programa, escreve um parágrafo curto que responda a duas coisas: onde está a classe, onde estão as instâncias e que valores mudaram; e o que responderias a um colega que propusesse escrever uma classe diferente para cada um dos teus dois materiais.

## Antes de passares ao caderno 3

Tenta responder a estas perguntas sem olhar para o texto. Se alguma te deixar com dúvidas, volta à secção indicada.

- Consegues explicar a diferença entre a classe `Artigo` e o objeto `caderno`? (secções 4 e 5)
- Consegues dizer quando é executado o construtor, e quem o chama? (secção 6)
- Consegues explicar o que é o `self` na chamada `pasta.retirar(1)`? (secção 7)
- Consegues distinguir o parâmetro `unidades` do argumento `2`? (secção 7)
- Consegues explicar porque é que `mesmo_caderno = caderno` não cria um artigo novo? (secção 8)

Se ainda confundes classe e instância, volta ao esquema da secção 5 e pergunta-te se estás a olhar para a descrição comum ou para uma ficha com valores concretos. No próximo caderno vamos impedir que uma operação deixe esses valores num estado inválido.

![Rodapé](../imagens/rodape.png)

![Cabeçalho](../../imagens/cabecalho.png)

# Ficha de exercícios: Objetos, classes e instâncias

Praticas a diferença entre classe, instância e valor de atributo, e treinas o construtor, o `self`, o valor devolvido e os nomes que apontam para o mesmo objeto. Os exercícios 1 a 6 são obrigatórios. Cada exercício faz-se num script novo, na pasta `tema-02` do laboratório, com o nome que o enunciado indica, e as respostas escritas ficam em comentários nesse script. Entregas os scripts e a folha do desenho do exercício 3 pelo meio que o professor indicar. Para rever: o [guia do tema](../02-objetos-classes-instancias.md) e o [laboratório](../laboratorios/02-objetos-classes-instancias-laboratorio.md).

## Exercício 1: Classe, instância ou valor de atributo

Cada uma destas três linhas vem de um programa diferente, com uma classe que não aparece aqui. O construtor de cada classe guarda em atributos os valores que recebe, como o da classe `Artigo`.

```python partial
regua = Artigo("A06", "Régua", 10)
livro = Livro("L12", "Atlas escolar", 3)
cacifo_b = Cacifo(14, "Piso 1")
```

Cria o script `classificar.py` e responde só com comentários.

1. Classifica cada um destes nove itens como classe, nome de uma instância ou valor de atributo: `Livro`, `"Régua"`, `cacifo_b`, `14`, `Artigo`, `livro`, `"Atlas escolar"`, `regua` e `Cacifo`.
2. Escolhe uma das três linhas e descreve o que ela faz numa frase com as palavras classe, instância e valor de atributo.

Rever: [Classe e instância](../02-objetos-classes-instancias.md#classe-e-instância), [Um objeto reúne dados e operações](../02-objetos-classes-instancias.md#um-objeto-reúne-dados-e-operações) e [Cada instância é um objeto diferente](../02-objetos-classes-instancias.md#cada-instância-é-um-objeto-diferente).

<details>
<summary>Pista</summary>

Para cada item, decide se é a descrição comum, o nome que fica a apontar para um objeto acabado de criar, ou um valor que fica guardado dentro desse objeto. Uma variável não é o objeto: é a etiqueta colada nele.

</details>

## Exercício 2: Atributo ou parâmetro

A escola regista os cacifos dos alunos, com o número e o piso de cada um. Um colega escreveu a classe `Cacifo` com nomes curtos nos parâmetros do construtor:

```python
# Ficha 02, exercício 2: a classe Cacifo do colega, com nomes curtos.

class Cacifo:
    """Descreve um cacifo da escola: o número e o piso onde está."""

    def __init__(self, n, p):
        """Prepara um cacifo acabado de criar, guardando os dois dados recebidos."""
        self.numero = n
        self.piso = p


cacifo = Cacifo(14, "Piso 1")
print(cacifo.numero)
print(cacifo.n)
```

Copia o programa para o script `cacifo.py`. As respostas deste exercício ficam num comentário no fim do script.

1. Sem executar, diz o que acontece em cada uma das duas linhas do fim, e explica porquê numa frase. Executa depois para confirmares.
2. Com nomes compridos, o construtor seria `def __init__(self, numero, piso):`, com as linhas `self.numero = numero` e `self.piso = piso`, e faria o mesmo trabalho. Qual dos dois construtores preferias encontrar num programa escrito por outra pessoa, e porquê?

Rever: [O `self.` decide o que fica no objeto](../02-objetos-classes-instancias.md#o-self-decide-o-que-fica-no-objeto).

<details>
<summary>Pista</summary>

Em cada linha do construtor do colega, compara o que está à esquerda do `=` com o que está à direita. Qual dos dois fica no objeto quando o construtor acaba?

</details>

## Exercício 3: Quantos objetos, quantos nomes

Este programa usa a classe `Artigo` com o método `retirar`, como o segundo programa do guia.

```python
# Ficha 02, exercício 3: quantos objetos e quantos nomes.

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
        Nos programas deste tema só fazemos pedidos que sabemos serem válidos.
        """
        self.quantidade = self.quantidade - unidades
        return self.quantidade


a = Artigo("A13", "Compasso", 10)
b = Artigo("A14", "Esquadro", 4)
c = a
d = c
d.retirar(3)
b.retirar(1)

print(a.quantidade, b.quantidade, c.quantidade, d.quantidade)
print(a is d, b is c)
```

Copia o programa para o script `etiquetas.py`.

1. Sem executar, quantos objetos do tipo `Artigo` existem no fim do programa, e quantos nomes apontam para eles? Escreve os dois números num comentário no início do script. Depois desenha numa folha como ficam no fim do programa: uma caixa por objeto e uma etiqueta por nome, colada na caixa para onde o nome aponta.
2. A linha `d = c` não tem `Artigo(...)` e não usa o nome `a`. Para que objeto fica a apontar o nome `d`? Explica numa frase, num comentário junto dessa linha.
3. Que duas linhas mostra o programa? Descobre-as de cabeça, sem as escrever, e executa para confirmares.

Rever: [Cada instância é um objeto diferente](../02-objetos-classes-instancias.md#cada-instância-é-um-objeto-diferente) e [O método retirar em Python](../02-objetos-classes-instancias.md#o-método-retirar-em-python).

<details>
<summary>Pista</summary>

Desenha primeiro as caixas, uma por cada `Artigo(...)` do programa. Depois segue as linhas pela ordem e cola cada etiqueta na caixa para onde o nome aponta nesse momento.

</details>

## Exercício 4: O valor devolvido e o estado

Este programa usa a mesma classe do exercício 3, com um só artigo, o marcador.

```python
# Ficha 02, exercício 4: o marcador e o valor que o método devolve.

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
        Nos programas deste tema só fazemos pedidos que sabemos serem válidos.
        """
        self.quantidade = self.quantidade - unidades
        return self.quantidade


marcador = Artigo("A07", "Marcador", 12)
restam = marcador.retirar(5)
marcador.retirar(2)
print(restam, marcador.quantidade)
print(marcador.retirar(1))
print(marcador.quantidade)
```

Copia o programa para o script `marcador.py`.

1. Descobre de cabeça as três linhas que o programa mostra, e confirma-as a executar; não precisas de as escrever.
2. Explica os dois números da primeira linha do ecrã numa ou duas frases, num comentário no início do script, com as palavras "devolve" e "atributo".
3. A linha `print(marcador.retirar(1))` faz duas coisas. Diz quais, pela ordem em que acontecem, num comentário junto dessa linha.

Rever: [O método retirar em Python](../02-objetos-classes-instancias.md#o-método-retirar-em-python).

<details>
<summary>Pista</summary>

Segue o programa linha a linha com duas colunas: o atributo `quantidade` do marcador e a variável `restam`. Em cada linha, pergunta-te se ela muda o atributo, a variável `restam`, ou as duas.

</details>

## Exercício 5: Da saída para o código

Neste programa faltam as duas linhas que criam os artigos `primeiro` e `segundo`:

```python partial
# Ficha 02, exercício 5: da saída para o código.

class Artigo:
    """Descreve um artigo do inventário: um material com código, nome e quantidade."""

    def __init__(self, codigo, nome, quantidade):
        """Prepara um artigo acabado de criar, guardando os três dados recebidos."""
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade


# Aqui faltam as duas linhas que criam os artigos primeiro e segundo.

print(primeiro.nome, primeiro.quantidade)
print(segundo.codigo, segundo.nome)
```

Copia-o para o script `agrafador.py`. Com as duas linhas que faltam, o programa tem de mostrar exatamente isto:

```text
Agrafador 2
A08 Furador
```

1. Escreve as duas linhas. A saída não mostra todos os valores de que o construtor precisa. Os que faltam escolhes tu, com um código que ainda não exista e uma quantidade possível. Num comentário no início do script, explica numa frase porque é que tens de os escrever, se não aparecem no ecrã.
2. Um colega escreveu a primeira linha assim: `primeiro = Artigo("Agrafador", "A09", 2)`. Sem mudares o teu programa, diz o que mostraria a primeira linha do ecrã com a linha dele. No mesmo comentário, explica porque é que o Python não se queixou.

Rever: [Quando é que o construtor trabalha](../02-objetos-classes-instancias.md#quando-é-que-o-construtor-trabalha).

<details>
<summary>Pista</summary>

Para cada valor do ecrã, vê no `print` de que atributo ele vem. Depois procura no construtor o parâmetro que dá o valor a esse atributo, e em que lugar da linha do `def` está.

</details>

## Exercício 6: Um construtor que não aceita os valores

Um colega escreveu este programa, e o Python parou logo na linha que cria o caderno:

```python
# Ficha 02, exercício 6: o programa do colega.

class Artigo:
    """Descreve um artigo do inventário: um material com código, nome e quantidade."""

    def __init__(codigo, nome, quantidade):
        """Prepara um artigo acabado de criar, guardando os três dados recebidos."""
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade


caderno = Artigo("A01", "Caderno", 6)
print(caderno.nome, caderno.quantidade)
```

A última linha da mensagem de erro foi esta:

```text
TypeError: Artigo.__init__() takes 3 positional arguments but 4 were given
```

Em português: o construtor da classe `Artigo` aceita 3 argumentos, mas recebeu 4. No Python 3.9 e nas versões anteriores, a mensagem começa por `__init__()`, sem `Artigo.` à frente.

Copia o programa para o script `colega.py`.

1. A mensagem diz que o construtor recebeu 4 valores, e o colega só escreveu três. De onde vem o quarto, e porque é que este construtor não tem lugar para ele? Responde num comentário no fim do script.
2. Corrige o programa mudando uma única linha, para mostrar `Caderno 6`.

Rever: [Quando é que o construtor trabalha](../02-objetos-classes-instancias.md#quando-é-que-o-construtor-trabalha).

<details>
<summary>Pista</summary>

Conta os lugares que a linha do `def __init__` do colega tem. Depois conta os valores que o Python entrega ao construtor, sem esqueceres o que ele entrega sozinho, e que não está escrito na chamada.

</details>

## Desafios

### Desafio 1: Um nome que muda de objeto

Este programa usa a mesma classe do exercício 3, com dois artigos e um nome a mais, `escolhido`.

```python
# Ficha 02, desafio 1: um nome que muda de objeto.

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
        Nos programas deste tema só fazemos pedidos que sabemos serem válidos.
        """
        self.quantidade = self.quantidade - unidades
        return self.quantidade


caneta = Artigo("A03", "Caneta", 8)
borracha = Artigo("A04", "Borracha", 3)
escolhido = borracha
caneta.retirar(2)
escolhido.retirar(1)
escolhido = caneta
escolhido.retirar(3)
print(caneta.quantidade, borracha.quantidade)
```

Copia o programa para o script `escolhido.py`. Descobre de cabeça a linha que o programa mostra. Depois, num comentário no fim do script, explica por palavras o que mudou na linha `escolhido = caneta` e o que não mudou.

Rever: [Cada instância é um objeto diferente](../02-objetos-classes-instancias.md#cada-instância-é-um-objeto-diferente).

<details>
<summary>Pista</summary>

Segue o programa linha a linha. Depois de cada linha, vê a quantidade da caneta, a da borracha e a caixa para onde aponta a etiqueta `escolhido`. Um pedido feito através desse nome chega a essa caixa.

</details>

### Desafio 2: Um método novo, adicionar

Copia para o script `adicionar.py` o segundo programa do guia, em [O método retirar em Python](../02-objetos-classes-instancias.md#o-método-retirar-em-python). Acrescenta à classe `Artigo` um método `adicionar`, que junta unidades à quantidade de um artigo. Como o `retirar`, o método ainda não precisa de verificar se o pedido é possível.

Decide o que o `adicionar` devolve: a quantidade que fica, como o `retirar`, ou nada. Justifica a escolha numa frase, num comentário por cima do método, e diz na docstring o que o método devolve.

No fim do programa, adiciona 4 unidades à pasta, retira-lhe 1 a seguir e mostra as quantidades dos dois artigos. Têm de aparecer 4 para o caderno e 5 para a pasta.

Rever: [O método retirar em Python](../02-objetos-classes-instancias.md#o-método-retirar-em-python).

<details>
<summary>Pista</summary>

Pensa em quem vai usar o método. Precisa do valor logo a seguir à chamada, ou pode consultar o atributo quando quiser?

</details>

### Desafio 3: O método retirar do colega

Um colega escreveu o método `retirar` de outra maneira e testou-o com este programa:

```python
# Ficha 02, desafio 3: o método retirar do colega.

class Artigo:
    """Descreve um artigo do inventário: um material com código, nome e quantidade."""

    def __init__(self, codigo, nome, quantidade):
        """Prepara um artigo acabado de criar, guardando os três dados recebidos."""
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade

    def retirar(self, unidades):
        """Retira unidades a este artigo e devolve a quantidade que fica."""
        caderno.quantidade = caderno.quantidade - unidades
        return caderno.quantidade


caderno = Artigo("A01", "Caderno", 6)
pasta = Artigo("A02", "Pasta", 2)

caderno.retirar(2)
print("Teste 1:", caderno.quantidade, pasta.quantidade)

pasta.retirar(1)
print("Teste 2:", caderno.quantidade, pasta.quantidade)
```

Copia o programa para o script `desafio.py`.

1. Sem executar, que duas linhas mostra o programa? Em qual dos dois testes é que o método faz o que devia?
2. Explica num comentário no fim do script, com a palavra `self`, o que está errado no método. Depois corrige-o.
3. Sem a correção, o colega usou a mesma classe noutro programa, em que os artigos se chamam `regua` e `esquadro` e não há nenhum nome `caderno`. Prevê o que acontece na primeira chamada a `retirar`. Para confirmares, copia outra vez o programa do colega, sem a correção, para o script `desafio_regua.py`, e troca as linhas que vêm depois da classe por estas:

   ```python partial
   regua = Artigo("A06", "Régua", 10)
   esquadro = Artigo("A14", "Esquadro", 4)

   regua.retirar(2)
   print("Teste 1:", regua.quantidade, esquadro.quantidade)

   esquadro.retirar(1)
   print("Teste 2:", regua.quantidade, esquadro.quantidade)
   ```

Rever: [O método retirar em Python](../02-objetos-classes-instancias.md#o-método-retirar-em-python) e [Quando é que o construtor trabalha](../02-objetos-classes-instancias.md#quando-é-que-o-construtor-trabalha).

<details>
<summary>Pista</summary>

Em cada teste, vê que objeto é o `self` e que objeto o método altera.

</details>

## Critérios de conclusão

- Fizeste os exercícios 1 a 6, cada um no seu script, com as respostas escritas em comentários, e o desenho do exercício 3 numa folha.
- Nas respostas por palavras, usaste as palavras que cada alínea pede.
- O programa do exercício 5 mostra exatamente `Agrafador 2` e `A08 Furador`.
- O programa do exercício 6 mostra `Caderno 6`, com uma só linha mudada.

![Rodapé](../../imagens/rodape.png)

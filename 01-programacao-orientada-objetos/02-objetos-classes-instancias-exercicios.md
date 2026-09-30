![Cabeçalho](../imagens/cabecalho.png)

# Ficha de exercícios: objetos, classes e instâncias

*M10 · Caderno 2 · Ficha de exercícios*

Esta ficha acompanha o [caderno 2](02-objetos-classes-instancias.md). É para praticares sozinho, depois de estudares o caderno e de fazeres o [laboratório](02-objetos-classes-instancias-laboratorio.md). Conta com cerca de uma hora para os seis exercícios, e mais dez minutos se fizeres o desafio opcional do fim.

Os exercícios da secção 9 do caderno, "Agora experimenta", continuam a ser teus e o professor diz quando os fazer. Esta ficha não os repete: traz exercícios mais curtos, cada um a treinar uma coisa só, do mais direto para o que pede uma pequena decisão tua.

Responde no caderno diário ou numa folha, com o número de cada exercício. Nos exercícios com código, escreve a previsão antes de executar: é a previsão, e não a execução, que mostra o que percebeste. Os programas completos podem ser copiados para um ficheiro `.py` e executados no editor de Python que usas nas aulas; os excertos não correm sozinhos, e o enunciado diz sempre de que outro código dependem. Entrega as respostas pelo meio indicado pelo professor.

## Exercício 1: classe, instância ou valor de atributo (5 min)

Cada uma das três linhas seguintes vem de um programa diferente. Em cada programa há uma classe já escrita, que não aparece aqui, com um construtor que guarda em atributos os valores que recebe, como o construtor da classe `Artigo`. São excertos e não correm sozinhos.

```python partial
regua = Artigo("A05", "Régua", 10)
livro = Livro("L12", "Atlas escolar", 3)
cacifo_b = Cacifo(14, "Piso 1")
```

1. Classifica cada um destes nove itens como classe, instância ou valor de atributo: `Livro`, `"Régua"`, `cacifo_b`, `14`, `Artigo`, `livro`, `"Atlas escolar"`, `regua` e `Cacifo`. Um nome de variável como `regua` conta como instância, porque aponta para uma instância (secção 8 do caderno).
2. Escolhe uma das três linhas e descreve o que ela faz numa frase que use as palavras classe, instância e valor de atributo.

## Exercício 2: atributo ou parâmetro (10 min)

A escola regista os cacifos dos alunos. Este programa é completo:

```python
class Cacifo:
    """Descreve um cacifo da escola: o número e o piso onde está."""

    def __init__(self, numero, piso):
        """Prepara um cacifo acabado de criar, guardando os dois dados recebidos."""
        self.numero = numero
        self.piso = piso


cacifo = Cacifo(14, "Piso 1")
print(cacifo.numero, cacifo.piso)
```

1. Na linha `self.piso = piso`, o que é `self.piso` e o que é `piso`? Qual dos dois continua a existir depois de o construtor terminar? A resposta está na secção 6 do caderno.
2. Um colega achou os nomes compridos e reescreveu o construtor com nomes curtos. É um excerto: para o experimentares, substitui o construtor do programa acima por este.

```python partial
    def __init__(self, n, p):
        """Prepara um cacifo acabado de criar, guardando os dois dados recebidos."""
        self.numero = n
        self.piso = p
```

Com o construtor do colega, e com a mesma linha `cacifo = Cacifo(14, "Piso 1")`, qual destas duas linhas funciona: `print(cacifo.numero)` ou `print(cacifo.n)`? Escreve a previsão com uma frase de justificação. Depois experimenta, substituindo a última linha do programa por estas duas linhas, uma a seguir à outra.

3. Os dois construtores fazem o mesmo trabalho. Qual dos dois preferias encontrar num programa escrito por outra pessoa, e porquê?

## Exercício 3: quantos objetos, quantos nomes (10 min)

Este programa completo usa a classe `Artigo` do programa da secção 7 do caderno. Os nomes das variáveis são letras de propósito, para que o nome não te diga nada sobre o objeto.

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


a = Artigo("A06", "Compasso", 10)
b = Artigo("A07", "Esquadro", 4)
c = a
d = c
d.retirar(3)
b.retirar(1)

print(a.quantidade, b.quantidade, c.quantidade, d.quantidade)
print(a is d, b is c)
```

1. Sem executar: quantos objetos do tipo `Artigo` existem no fim do programa, e quantos nomes apontam para eles? Desenha uma caixa por objeto e uma etiqueta por nome, colada na caixa para onde o nome aponta, como na comparação das etiquetas da secção 8 do caderno.
2. A linha `d = c` não tem `Artigo(...)` e não usa o nome `a`. Para que objeto fica a apontar o nome `d`? Explica numa frase.
3. Escreve as duas linhas que esperas ver no ecrã. Depois executa e compara.

## Exercício 4: o valor devolvido e o estado (10 min)

Este programa usa a classe `Artigo` do programa da secção 7 do caderno, a mesma do exercício 3. É um excerto: para o executares, copia o programa da secção 7 e substitui as linhas que vêm depois da classe (a partir de `caderno = ...`) por estas.

```python partial
marcador = Artigo("A09", "Marcador", 12)
restam = marcador.retirar(5)
marcador.retirar(2)
print(restam, marcador.quantidade)
print(marcador.retirar(1))
print(marcador.quantidade)
```

1. Escreve as três linhas que esperas ver. Depois executa e compara.
2. Na primeira linha do ecrã aparecem dois números diferentes. Explica porquê numa ou duas frases, usando as palavras "devolve" e "atributo" (secção 7 do caderno).
3. A linha `print(marcador.retirar(1))` faz duas coisas. Diz quais, pela ordem em que acontecem.

## Exercício 5: da saída para o código (10 min)

Copia o programa da secção 6 do caderno e substitui as linhas que vêm depois da classe (a partir de `caderno = ...`) por estas duas, que são um excerto:

```python partial
print(primeiro.nome, primeiro.quantidade)
print(segundo.codigo, segundo.nome)
```

Faltam, antes delas, as duas linhas que criam os artigos `primeiro` e `segundo`. O programa completo tem de mostrar exatamente isto:

```text
Agrafador 2
A08 Furador
```

1. Escreve as duas linhas que faltam, executa e confirma a saída. A saída não mostra todos os valores de que o construtor precisa: os que faltam escolhes tu. Explica numa frase porque é que tens de os escrever na mesma, se não aparecem no ecrã.
2. Um colega escreveu a primeira linha assim: `primeiro = Artigo("Agrafador", "A07", 2)`. Prevê o que mostra a primeira linha do ecrã com a linha dele, e explica porque é que o Python não se queixou.

## Exercício 6: um construtor que não aceita os valores (10 min)

Um colega escreveu este programa completo, e o Python parou logo na linha que cria o caderno:

```python
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

A última linha da mensagem de erro foi esta. Em versões mais antigas do Python, a mensagem começa por `__init__()`, sem `Artigo.` à frente:

```text
TypeError: Artigo.__init__() takes 3 positional arguments but 4 were given
```

Em português: o construtor da classe `Artigo` aceita 3 argumentos posicionais, mas recebeu 4. "Posicionais" quer dizer que os valores são entregues aos parâmetros pela ordem em que estão escritos: o primeiro valor vai para o primeiro parâmetro, o segundo para o segundo, e assim por diante.

1. O colega escreveu três valores entre parênteses, e a mensagem diz que o construtor recebeu 4. De onde vem o quarto? E porque é que este construtor só aceita 3? Relê a secção 6 do caderno, na parte "Criar as instâncias", antes de responder.
2. Corrige o programa mudando uma única linha. Executa e confirma que aparece `Caderno 6`.

## Desafio opcional: um método que só funciona com um artigo (10 min)

Um colega escreveu o método `retirar` de outra maneira, e testou-o com este programa completo:

```python
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

1. Prevê as duas linhas. Depois executa e compara.
2. O teste 1 dá o resultado certo e o teste 2 não. Explica porquê, usando a palavra `self`, e corrige o método.
3. Sem a correção, o colega usou a mesma classe noutro programa, em que os artigos se chamam `regua` e `esquadro` e não há nenhum nome `caderno`. Prevê o que acontece na primeira chamada a `retirar`. Depois experimenta: mantém a classe do colega, sem a corrigir, e substitui as linhas que vêm depois dela por estas, que são um excerto.

```python partial
regua = Artigo("A05", "Régua", 10)
esquadro = Artigo("A07", "Esquadro", 4)

regua.retirar(2)
print("Teste 1:", regua.quantidade, esquadro.quantidade)

esquadro.retirar(1)
print("Teste 2:", regua.quantidade, esquadro.quantidade)
```

## Antes de entregares

Revê as tuas respostas e confirma que em cada previsão escreveste o raciocínio, e não só o resultado. Indica também um ponto desta ficha que ainda não consegues explicar sem voltar ao caderno: é por aí que deves começar a próxima revisão.

![Rodapé](../imagens/rodape.png)

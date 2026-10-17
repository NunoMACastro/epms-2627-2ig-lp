![Cabeçalho](../imagens/cabecalho.png)

# Ficha de exercícios: Objetos, classes e instâncias

Ficha do tema Objetos, classes e instâncias, do módulo M10, Introdução à Programação Orientada por Objetos. Praticas, em exercícios curtos, a diferença entre classe, instância e valor de atributo, o construtor, o `self`, o valor devolvido e os nomes que apontam para o mesmo objeto. Fazes sozinho, ao teu ritmo: o que não acabares na aula, acabas em casa ou na aula seguinte.

## O que precisas de saber

O [guia do tema](02-objetos-classes-instancias.md) e o [laboratório](02-objetos-classes-instancias-laboratorio.md). Cada exercício diz em que secção do guia está a ideia que usa.

## Como trabalhar

Faz os exercícios 1 a 6 pela ordem. São a parte obrigatória, e cada um treina uma coisa só, do mais direto para o que pede uma pequena decisão tua. O desafio opcional é para quem acabar. Os exercícios de "Para ires mais longe" são mais longos e servem para aprofundar: fazes os que quiseres, ou os que o professor indicar.

Responde no caderno diário ou numa folha, com o número de cada exercício. Nos exercícios com código, escreve a previsão antes de executar: é a previsão, e não a execução, que mostra o que percebeste. Se a execução der outra coisa, procura a explicação em vez de mudar a previsão.

Um programa completo pode ser copiado para um ficheiro `.py` e executado no editor de Python que usas nas aulas. Os excertos não correm sozinhos, e o enunciado diz sempre de que outro código dependem. Entrega as respostas pelo meio indicado pelo professor.

## Exercício 1: Classe, instância ou valor de atributo

Cada uma das três linhas seguintes vem de um programa diferente. Em cada programa há uma classe já escrita, que não aparece aqui. Tem um construtor que guarda em atributos os valores que recebe, como o construtor da classe `Artigo`. São excertos e não correm sozinhos.

```python partial
regua = Artigo("A06", "Régua", 10)
livro = Livro("L12", "Atlas escolar", 3)
cacifo_b = Cacifo(14, "Piso 1")
```

1. Classifica cada um destes nove itens como classe, nome de uma instância ou valor de atributo: `Livro`, `"Régua"`, `cacifo_b`, `14`, `Artigo`, `livro`, `"Atlas escolar"`, `regua` e `Cacifo`. Um nome de variável como `regua` não é a instância: é o nome que aponta para ela ("Cada instância é um objeto diferente", no guia).
2. Escolhe uma das três linhas e descreve o que ela faz numa frase que use as palavras classe, instância e valor de atributo.

## Exercício 2: Atributo ou parâmetro

A escola regista os cacifos dos alunos. Este programa é completo:

```python
# Ficha 02, exercício 2: os cacifos da escola.

class Cacifo:
    """Descreve um cacifo da escola: o número e o piso onde está."""

    def __init__(self, numero, piso):
        """Prepara um cacifo acabado de criar, guardando os dois dados recebidos."""
        self.numero = numero
        self.piso = piso


cacifo = Cacifo(14, "Piso 1")
print(cacifo.numero, cacifo.piso)
```

1. Na linha `self.piso = piso`, o que é `self.piso` e o que é `piso`? Qual dos dois continua a existir depois de o construtor terminar? ("O parâmetro `self`", no guia.)
2. Um colega achou os nomes compridos e reescreveu o construtor com nomes curtos. É um excerto: para o experimentares, substitui o construtor do programa acima por este.

   ```python partial
       def __init__(self, n, p):
           """Prepara um cacifo acabado de criar, guardando os dois dados recebidos."""
           self.numero = n
           self.piso = p
   ```

   Com o construtor do colega, e com a mesma linha `cacifo = Cacifo(14, "Piso 1")`, qual destas duas linhas funciona: `print(cacifo.numero)` ou `print(cacifo.n)`? Escreve a previsão com uma frase de justificação. Depois experimenta: substitui a última linha do programa por estas duas linhas, uma a seguir à outra.

3. Os dois construtores fazem o mesmo trabalho. Qual dos dois preferias encontrar num programa escrito por outra pessoa, e porquê?

## Exercício 3: Quantos objetos, quantos nomes

Este programa completo usa a classe `Artigo` do segundo programa do guia, em "O método retirar em Python". Os nomes das variáveis são letras de propósito, para que o nome não te diga nada sobre o objeto.

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

1. Sem executar: quantos objetos do tipo `Artigo` existem no fim do programa, e quantos nomes apontam para eles? Desenha uma caixa por objeto e uma etiqueta por nome, colada na caixa para onde o nome aponta. É a comparação das etiquetas de "Cada instância é um objeto diferente", no guia.
2. A linha `d = c` não tem `Artigo(...)` e não usa o nome `a`. Para que objeto fica a apontar o nome `d`? Explica numa frase.
3. Escreve as duas linhas que esperas ver no ecrã. Depois executa e compara.

## Exercício 4: O valor devolvido e o estado

Este exercício usa a classe `Artigo` do segundo programa do guia, a mesma do exercício 3. É um excerto: para o executares, copia esse programa e substitui as linhas que vêm depois da classe (a partir de `caderno = ...`) por estas.

```python partial
marcador = Artigo("A07", "Marcador", 12)
restam = marcador.retirar(5)
marcador.retirar(2)
print(restam, marcador.quantidade)
print(marcador.retirar(1))
print(marcador.quantidade)
```

1. Escreve as três linhas que esperas ver. Depois executa e compara.
2. Na primeira linha do ecrã aparecem dois números diferentes. Explica porquê numa ou duas frases, usando as palavras "devolve" e "atributo" ("O método retirar em Python", no guia).
3. A linha `print(marcador.retirar(1))` faz duas coisas. Diz quais, pela ordem em que acontecem.

## Exercício 5: Da saída para o código

Copia o primeiro programa do guia, em "A classe Artigo em Python". Substitui as linhas que vêm depois da classe (a partir de `caderno = ...`) por estas duas, que são um excerto:

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
2. Um colega escreveu a primeira linha assim: `primeiro = Artigo("Agrafador", "A09", 2)`. Prevê o que mostra a primeira linha do ecrã com a linha dele, e explica porque é que o Python não se queixou.

## Exercício 6: Um construtor que não aceita os valores

Um colega escreveu este programa completo, e o Python parou logo na linha que cria o caderno:

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

A última linha da mensagem de erro foi esta. Nas versões do Python anteriores à 3.10, a mensagem começa por `__init__()`, sem `Artigo.` à frente:

```text
TypeError: Artigo.__init__() takes 3 positional arguments but 4 were given
```

Em português: o construtor da classe `Artigo` aceita 3 argumentos posicionais, mas recebeu 4. "Posicionais" quer dizer que os valores são entregues aos parâmetros pela ordem em que estão escritos. O primeiro valor vai para o primeiro parâmetro, o segundo para o segundo, e assim por diante.

1. O colega escreveu três valores entre parênteses, e a mensagem diz que o construtor recebeu 4. Porque é que este construtor só aceita 3? A ideia está em "Criar as instâncias", no guia.
2. Corrige o programa mudando uma única linha. Executa e confirma que aparece `Caderno 6`.

## Apoio

- Exercício 1: para cada item, pergunta-te: é a descrição comum? É o nome que fica a apontar para um objeto criado? É um valor que fica guardado dentro dele?
- Exercício 2: relê, no guia, o parágrafo sobre a linha `self.codigo = codigo`.
- Exercício 3: desenha primeiro as caixas, uma por cada linha que tem `Artigo(...)`. Depois cola as etiquetas, linha a linha, pela ordem do programa.
- Exercício 4: faz um traço com duas colunas, o atributo `quantidade` do marcador e a variável `restam`. Muda cada coluna só na linha que a muda.
- Exercício 5: os valores entram no construtor pela ordem dos parâmetros do `def __init__`, seja qual for a ordem em que aparecem no ecrã.
- Exercício 6: conta os lugares na linha do `def __init__` e os valores que o Python lhes entrega, sem esqueceres o que ele entrega sozinho.
- Desafio: em cada teste, pergunta-te que objeto é o `self` e que objeto o método altera.
- Mais longe 1: na coluna de `escolhido`, escreve para que caixa aponta a etiqueta depois de cada linha. Um pedido feito através de `escolhido` vai para essa caixa.
- Mais longe 2: pensa em quem vai usar o método. Precisa do valor logo, ou consulta o atributo quando quiser?
- Mais longe 3: para cada versão, segue a chamada linha a linha e escreve o valor de `self.quantidade` antes e depois.
- Mais longe 4: escolhe primeiro o artigo que vai acabar em zero. As retiradas dele têm de somar exatamente a quantidade com que começou.

## Desafio opcional

Um método que só funciona com um artigo. Um colega escreveu o método `retirar` de outra maneira, e testou-o com este programa completo:

```python
# Ficha 02, desafio: o método retirar do colega.

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
   regua = Artigo("A06", "Régua", 10)
   esquadro = Artigo("A14", "Esquadro", 4)

   regua.retirar(2)
   print("Teste 1:", regua.quantidade, esquadro.quantidade)

   esquadro.retirar(1)
   print("Teste 2:", regua.quantidade, esquadro.quantidade)
   ```

## Para ires mais longe

### Mais longe 1: Um nome que muda de objeto

Este excerto não corre sozinho: precisa da classe `Artigo` com o método `retirar`, tal como está no segundo programa do guia. Para o executares, copia esse programa e substitui as linhas que vêm depois da classe (a partir de `caderno = ...`) por estas:

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

Constrói um traço com uma linha por instrução e três colunas. As colunas são a quantidade da caneta, a quantidade da borracha e o objeto para onde aponta o nome `escolhido` depois dessa instrução. Escreve a linha que esperas ver no ecrã e só depois executa. No fim, explica por palavras o que mudou na linha `escolhido = caneta` e o que não mudou.

### Mais longe 2: Um método novo, adicionar

Acrescenta à classe `Artigo` do segundo programa do guia um método `adicionar`, que acrescenta unidades à quantidade de um artigo. Não precisas de verificar se o pedido é válido: isso fica para o guia 03.

Antes de escreveres o método, tens de tomar uma decisão que o guia não tomou por ti: o que é que `adicionar` devolve? Pode devolver a quantidade que fica, como o `retirar`, ou pode não devolver nada. Escolhe uma das opções e justifica-a numa frase, a pensar em quem vai usar o método. Escreve a docstring do método de acordo com a tua escolha.

Depois escreve, no fim do programa, as linhas necessárias para adicionar 4 unidades à pasta e em seguida retirar-lhe 1, e para mostrar as quantidades dos dois artigos no fim. Prevê o que vai aparecer no ecrã e confirma executando.

### Mais longe 3: Dois colegas, dois erros

Dois colegas escreveram versões diferentes do método `retirar`. Os excertos seguintes são só o método, e não correm sozinhos. Para os experimentares, substitui o `retirar` do segundo programa do guia por cada um deles, à vez.

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

### Mais longe 4: A tua própria representação

Escolhe dois materiais da sala inventados por ti, com código, nome e quantidade inicial. Escreve um programa completo, com a classe `Artigo` do segundo programa do guia, que crie as duas instâncias. O programa faz depois uma sequência de três chamadas a `retirar`, todas possíveis, de forma que um dos artigos acabe com a quantidade exatamente em zero. Terás de escolher os números com cuidado antes de escrever as chamadas.

Antes de executares, escreve o traço da sequência, com a quantidade dos dois artigos depois de cada chamada. Depois executa, mostrando as quantidades no fim, e compara com o traço.

Por baixo do programa, escreve um parágrafo curto que responda a duas coisas. Primeiro, onde está a classe, onde estão as instâncias e que valores mudaram. Depois, o que responderias a um colega que propusesse escrever uma classe diferente para cada um dos teus dois materiais.

## Critérios de conclusão

- Fizeste os exercícios 1 a 6, com as previsões escritas antes de executar.
- Em cada exercício com código, comparaste a previsão com o que apareceu e explicaste as diferenças.
- Nas respostas por palavras, usaste as palavras que os enunciados pedem, como classe, instância, valor de atributo, "devolve" e "atributo".
- O programa do exercício 6 está corrigido numa só linha e mostra `Caderno 6`.

## Autoavaliação

1. Em que exercício a tua previsão falhou, e o que percebeste com a diferença?
2. O que achaste mais difícil: distinguir a classe da instância, o parâmetro do atributo, ou o valor devolvido do estado do objeto?
3. Que ponto desta ficha ainda não consegues explicar sem voltar ao guia? É por aí que começas a próxima revisão.

![Rodapé](../imagens/rodape.png)

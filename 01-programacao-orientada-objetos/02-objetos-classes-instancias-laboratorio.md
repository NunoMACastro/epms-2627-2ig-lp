![Cabeçalho](../imagens/cabecalho.png)

# Laboratório: criar e usar os primeiros objetos

*M10 · Caderno 2 · Laboratório*

Este laboratório acompanha o [caderno 2](02-objetos-classes-instancias.md). Diz-te o que fazer, passo a passo, com o editor de Python aberto ao lado. As explicações do porquê estão no caderno: cada parte diz em que secção deves ter o caderno aberto. Conta com cerca de uma hora e dez minutos, repartida pela aula, à medida que o professor for explicando as secções 6, 7 e 8.

No fim deves ter um ficheiro `artigos.py` com a classe `Artigo` do caderno a funcionar, escrita por ti. Pelo caminho vais ver com os teus próprios olhos quando é que o construtor trabalha, o que acontece a um objeto quando falta o `self.` numa linha do construtor e o que quer dizer dar dois nomes ao mesmo objeto. Na última parte vais escrever sozinho uma classe nova, para outra coisa da escola.

## Antes de começar

Precisas do computador com o editor de Python que usas nas aulas, e de papel e caneta para as previsões e para os traços.

Este laboratório dá por sabido o caderno 1, as secções 1 a 5 do caderno 2 (objeto, atributo, método, classe e instância) e as funções que aprendeste no 10.º ano, com `def` e `return`. As secções 6, 7 e 8 do caderno 2 trabalham-se ao longo do laboratório.

A forma de trabalhar é sempre a mesma. Antes de executares, escreves no papel o que esperas ver. Depois executas e comparas. Quando o resultado é diferente do que previste, explica a diferença antes de continuares: é essa explicação que mais te ensina. Escrever a previsão antes de executar obriga-te a pensar no que o programa faz.

Executa sempre o ficheiro inteiro. Cada execução começa do zero: o Python lê a classe, cria os artigos outra vez com os valores escritos no programa e repete todas as instruções, pela ordem em que estão.

Em várias partes vais mudar o programa de propósito, para veres o que acontece. Faz a alteração pedida, observa, e desfaz a alteração antes de passares à parte seguinte. Se te perderes, cada parte diz qual é o programa do caderno de onde partir: basta escrevê-lo ou copiá-lo outra vez.

## Parte 1: preparar a pasta e o ficheiro (3 min)

1. Na pasta onde guardas os trabalhos de LP, cria uma pasta nova chamada `caderno-2`.
2. Dentro dela, cria um ficheiro novo chamado `artigos.py`. O nome tem de acabar em `.py` e não deve ter espaços nem acentos. Vais usar este ficheiro da parte 2 à parte 7, mudando o conteúdo de parte para parte.

## Parte 2: escrever a classe e criar dois artigos (7 min)

Tem aberta a secção 6 do caderno.

1. Escreve no ficheiro o programa completo da secção 6. Desta vez não copies nem coles: escreve-o tu, letra a letra. Ao escrever reparas em pormenores que uma cópia esconde. Repara nos dois pontos no fim das linhas `class Artigo:` e `def __init__(self, codigo, nome, quantidade):`, nos dois sublinhados antes e nos dois depois de `init`, na indentação de quatro espaços dentro da classe e de oito dentro do construtor, e nas duas linhas em branco antes de `caderno = ...`. As docstrings podem ficar como no caderno ou com palavras tuas.
2. Antes de executares, escreve no papel as duas linhas que esperas ver.
3. Executa. Deves ver as duas linhas que o caderno mostra:

```text
A01 Caderno 6
A02 Pasta 2
```

Se em vez disso aparecer uma mensagem de erro, lê a última linha e procura-a na tabela "Problemas frequentes neste laboratório", no fim deste documento. Os erros de escrita são normais quando se escreve um programa pela primeira vez, e aprender a encontrá-los a partir da mensagem faz parte do trabalho.

## Parte 3: ver quando o construtor trabalha (5 min)

Tem aberta a secção 6 do caderno, na parte "Criar as instâncias".

O caderno diz que nunca escrevemos `__init__` para chamar o construtor: é o Python que o executa, sozinho, sempre que se escreve `Artigo(...)`. Vais tornar isso visível com uma linha provisória.

1. Dentro do construtor, logo a seguir à docstring e antes de `self.codigo = codigo`, acrescenta a linha seguinte. É um excerto: vai para dentro do construtor, com a mesma indentação das linhas que começam por `self.`.

```python partial
        print("A preparar o artigo", codigo)
```

2. Antes de executares, responde no papel: quantas vezes vai aparecer a frase "A preparar o artigo"? Vai aparecer antes ou depois da linha `A01 Caderno 6`?
3. Executa. Deves ver quatro linhas:

```text
A preparar o artigo A01
A preparar o artigo A02
A01 Caderno 6
A02 Pasta 2
```

4. Agora muda só a ordem das linhas do fim do programa: põe a linha `print(caderno.codigo, caderno.nome, caderno.quantidade)` logo a seguir a `caderno = Artigo("A01", "Caderno", 6)`, antes de `pasta = Artigo("A02", "Pasta", 2)`. Escreve no papel a ordem em que esperas ver as quatro linhas, e executa.
5. Responde no papel: nunca escreveste `__init__` nas linhas do fim do programa. Que linhas fizeram o construtor trabalhar, e quantas vezes trabalhou?
6. Apaga a linha provisória do construtor e volta a pôr as linhas do fim pela ordem do caderno. Executa para confirmares que voltas a ver só as duas linhas da parte 2. O construtor serve para preparar o objeto, e não para escrever no ecrã: a linha só lá esteve para veres quando é que ele trabalha.

## Parte 4: mostrar um objeto inteiro (5 min)

Tem aberto o fim da secção 6 do caderno, na parte "Consultar atributos".

1. Acrescenta no fim do ficheiro a linha `print(caderno)`. Antes de executares, relê o último parágrafo da secção 6 e escreve no papel o que achas que vai aparecer.
2. Executa. Além das duas linhas de sempre, aparece uma terceira linha parecida com esta:

```text
<__main__.Artigo object at 0x105535fd0>
```

Esta linha diz três coisas. Diz que se trata de um objeto (em inglês, `object`) da classe `Artigo`. Diz que essa classe foi definida no programa que mandaste executar, que é o que quer dizer `__main__`. E diz onde é que o objeto está guardado na memória do computador, que é o número depois de `at`. Esse número começa por `0x` porque está escrito em base 16, a forma habitual de escrever posições de memória; não precisas de o saber ler.

3. Executa outra vez e compara o número com o da primeira execução. Em geral muda, pelo menos em parte, porque cada execução começa do zero e o objeto pode ficar guardado noutro sítio.
4. Acrescenta no fim a linha `print(pasta)` e executa. Responde no papel: os números do caderno e da pasta são iguais ou diferentes? O que te diz isso sobre o número de objetos que o programa criou? Vais precisar desta resposta na parte 7.
5. Responde também: para mostrar o nome do material, porque é que o programa do caderno escreve `print(caderno.nome)`, e não `print(caderno)`?
6. Apaga as linhas `print(caderno)` e `print(pasta)`.

## Parte 5: o que acontece sem `self.` (8 min)

Tem aberta a secção 6 do caderno, na parte "O parâmetro `self`".

O ficheiro deve ter agora o programa da secção 6, tal como o escreveste na parte 2.

1. No construtor, na linha `self.nome = nome`, apaga `self.`, de modo que a linha fique `nome = nome`. Não mexas em mais nada.
2. Antes de executares, relê o parágrafo do caderno que começa por "A linha lê-se assim" e responde no papel: o Python vai queixar-se da linha `nome = nome`? O que vai acontecer quando o programa pedir `caderno.nome`?
3. Executa. O programa para sem mostrar nenhuma das duas linhas, e a última linha da mensagem de erro é esta:

```text
AttributeError: 'Artigo' object has no attribute 'nome'
```

Em português: o objeto do tipo `Artigo` não tem nenhum atributo chamado `nome`. Um `AttributeError` é o erro que aparece quando se pede a um objeto um atributo que ele não tem.

4. Responde no papel: em que linha do ficheiro aparece o erro? Em que linha está a causa? Porque é que o Python não se queixou da linha `nome = nome`, e o que é que essa linha fez, afinal?
5. Para confirmares que só falta o nome, muda provisoriamente os dois `print` do fim para mostrarem só o código e a quantidade: `print(caderno.codigo, caderno.quantidade)` e `print(pasta.codigo, pasta.quantidade)`. Executa. Deves ver `A01 6` e `A02 2`: os dois objetos têm os outros dois atributos, e só lhes falta aquele em que tiraste o `self.`.
6. Volta a pôr `self.nome = nome` no construtor e os dois `print` como estavam. Executa para confirmares que aparecem outra vez as duas linhas da parte 2.

## Parte 6: acrescentar o método `retirar` (10 min)

Tem aberta a secção 7 do caderno.

1. Acrescenta à tua classe o método `retirar`, escrito por ti a partir da secção 7. Escreve-o dentro da classe, a seguir ao construtor, com uma linha em branco entre os dois. A linha `def retirar(self, unidades):` fica com a mesma indentação de `def __init__`, e as linhas de dentro do método ficam com mais quatro espaços.
2. Substitui as linhas que vêm depois da classe, a partir de `caderno = ...`, pelas do programa da secção 7. O ficheiro fica igual ao programa completo dessa secção.
3. Escreve no papel as três linhas que esperas ver e executa. Confirma que aparecem `Antes: 6 2`, `Depois: 4 2` e `Devolvido: 4`.
4. Agora uma experiência sobre o `self`. O caderno diz, na secção 7, que a chamada `caderno.retirar(2)` é tratada pelo Python como `Artigo.retirar(caderno, 2)`. Vais confirmá-lo. Na linha `restante = caderno.retirar(2)`, troca `caderno.retirar(2)` por `Artigo.retirar(caderno, 2)`. Prevê as três linhas e executa. Se o caderno tem razão, a saída não muda.
5. Troca agora `Artigo.retirar(caderno, 2)` por `Artigo.retirar(pasta, 2)`. Antes de executares, responde no papel: qual dos dois artigos vai ficar com menos unidades? Qual dos dois objetos vai ser o `self` dentro do método? Executa. Deves ver:

```text
Antes: 6 2
Depois: 6 0
Devolvido: 0
```

6. Responde numa frase: na forma curta, `caderno.retirar(2)`, onde está escrito o objeto que vai ocupar o `self`?
7. Volta a pôr `restante = caderno.retirar(2)` e executa para confirmares a saída do passo 3. A forma longa serviu só para veres o que o Python faz por dentro. Nas duas formas, o método é o mesmo e trabalha sobre um objeto; só muda a maneira de o chamar. Nos programas escreve-se sempre a forma curta, que é a que toda a gente espera ler.

## Parte 7: dois nomes para o mesmo objeto (7 min)

Tem aberta a secção 8 do caderno.

1. Substitui as linhas que vêm depois da classe pelas do programa da secção 8. A classe fica igual, com o construtor e o `retirar`.
2. Escreve no papel as quatro linhas que esperas ver e executa. Confirma que coincidem com as do caderno: `Caderno: 5`, `Pasta: 2`, `True` e `False`.
3. Agora troca a linha `mesmo_caderno = caderno` pela linha seguinte, e acrescenta no fim do ficheiro a linha `print("Mesmo caderno:", mesmo_caderno.quantidade)`.

```python partial
mesmo_caderno = Artigo("A01", "Caderno", 6)
```

4. Antes de executares, responde no papel: quantos objetos do tipo `Artigo` existem agora? A qual deles vai ser retirada a unidade? O que vai mostrar `caderno is mesmo_caderno`? Executa. Deves ver:

```text
Caderno: 6
Pasta: 2
False
False
Mesmo caderno: 5
```

5. Responde no papel: os objetos a que chamámos `caderno` e `mesmo_caderno` começaram com exatamente os mesmos valores. Porque é que `caderno is mesmo_caderno` dá agora `False`? Relaciona a tua resposta com o que viste na parte 4, quando o caderno e a pasta apareceram com números de memória diferentes.
6. Repara também que o programa passou a ter dois artigos com o código A01. O Python aceitou-o sem se queixar, mas a primeira regra do inventário, na secção 5 do caderno 1, diz que cada código identifica um único artigo. O Python não conhece as regras do nosso inventário: faz o que o programa lhe pede, e quem escreve o programa é que tem de as respeitar.
7. Volta a pôr `mesmo_caderno = caderno`, apaga a última linha que acrescentaste e executa para confirmares a saída do caderno.

## Parte 8: sozinho (25 min)

### 8.1: escrever a classe de cor (10 min)

1. Fecha o caderno e o ficheiro `artigos.py`. Na mesma pasta `caderno-2`, cria um ficheiro novo chamado `memoria.py`.
2. Sem olhar para nada, escreve a classe `Artigo`, com o construtor e o método `retirar`. Por baixo da classe, escreve as linhas necessárias para criar um artigo à tua escolha, retirar-lhe unidades e mostrar a quantidade que fica. As docstrings podem ser curtas e com palavras tuas.
3. Executa. Se aparecer um erro, tenta corrigi-lo sozinho, a partir da última linha da mensagem e da tabela de problemas frequentes.
4. Só depois abre a secção 7 do caderno e compara, linha a linha. Escreve no papel todas as diferenças que encontrares, mesmo as pequenas, como um sublinhado a menos, dois pontos esquecidos ou um `self.` que ficou por escrever. Marca as que faziam o programa falhar e as que não faziam diferença.

### 8.2: uma classe para outra coisa da escola (15 min)

A classe `Artigo` descreve um tipo de coisa, e a mesma forma de escrever uma classe serve para descrever outras. Na escola, cada sala tem um projetor, e a lâmpada de um projetor tem de ser trocada ao fim de um certo número de horas de uso. Para saber quando, a escola quer registar, para cada projetor, um código, a sala onde está e as horas de uso que já acumulou.

1. Na mesma pasta, cria um ficheiro novo chamado `projetor.py`.
2. Escreve uma classe `Projetor` com um construtor que receba o código, a sala e as horas de uso, e os guarde em três atributos chamados `codigo`, `sala` e `horas_uso`. A sala guarda-se como texto, por exemplo `"Sala 12"`.
3. Acrescenta à classe um método `usar`, com um parâmetro `horas`, que acrescenta as horas recebidas às horas de uso do projetor e devolve o total de horas que fica. Tal como o `retirar` do caderno, ainda não precisa de verificar se o pedido é válido. Escreve as docstrings da classe, do construtor e do método.
4. Depois da classe, cria dois projetores: o P01, na Sala 12, com 150 horas de uso; e o P02, na Sala 7, acabado de comprar, com 0 horas. Faz estas três chamadas, por esta ordem: usar o P01 durante 3 horas, usar o P02 durante 2 horas e usar o P01 durante 1 hora. Guarda numa variável o valor devolvido pela última chamada. No fim, mostra numa só linha as horas de uso dos dois projetores e o valor que guardaste.
5. Antes de executares, faz o traço no papel: uma linha por chamada, com as horas de uso dos dois projetores depois dessa chamada, como na tabela do exemplo guiado da secção 5 do caderno. Escreve também a linha que esperas ver no ecrã. Depois executa e compara.
6. Responde numa frase: porque é que aqui faz sentido escrever uma classe nova, `Projetor`, em vez de usar a classe `Artigo`? A secção 4 do caderno diz quando se justifica uma classe nova.

## Problemas frequentes neste laboratório

| O que aparece | O que costuma ser | Como resolver |
| --- | --- | --- |
| `SyntaxError: expected ':'`, ou `SyntaxError: invalid syntax` em versões mais antigas do Python | Faltam os dois pontos no fim de uma linha `class` ou `def` | Acrescenta `:` no fim da linha que a mensagem mostra |
| `IndentationError` | Uma linha com a indentação errada, por exemplo as linhas de dentro do construtor com a mesma indentação do `def` | Dentro da classe, quatro espaços; dentro de um método, oito. Compara com o caderno, linha a linha |
| `TypeError: Artigo() takes no arguments` | O nome do construtor está mal escrito, por exemplo `_init_`, com um só sublinhado de cada lado, ou `__int__`. O Python não o reconhece como construtor | O nome escreve-se `__init__`: dois sublinhados, a palavra `init` e mais dois sublinhados |
| `NameError: name 'artigo' is not defined`; as versões recentes do Python acrescentam `Did you mean: 'Artigo'?` | A classe foi escrita com maiúscula e a chamada com minúscula, ou ao contrário | Escreve o nome da classe sempre da mesma maneira: `Artigo`, com maiúscula |
| `AttributeError: 'Artigo' object has no attribute 'quantidade'`; as versões recentes podem acrescentar uma sugestão, como `Did you mean: 'quantiade'?` | O construtor guardou o atributo com outro nome, por um erro de escrita como `self.quantiade`, ou sem o `self.` à frente | Confirma que o nome depois de `self.` é exatamente o mesmo que usas no resto do programa |
| `AttributeError: 'Artigo' object has no attribute 'retirar'` | O método ficou fora da classe, com o `def` encostado à margem | Indenta todas as linhas do método mais quatro espaços, para ficarem dentro da classe |

## O que fica guardado

Guarda os ficheiros `artigos.py`, `memoria.py` e `projetor.py`, e a folha com as previsões, os traços e as respostas das partes 2 a 8. Entrega-os pelo meio indicado pelo professor.

![Rodapé](../imagens/rodape.png)

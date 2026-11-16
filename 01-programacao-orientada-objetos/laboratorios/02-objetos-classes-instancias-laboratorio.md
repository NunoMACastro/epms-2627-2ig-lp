![Cabeçalho](../../imagens/cabecalho.png)

# Laboratório: Objetos, classes e instâncias

## O que vais construir

Escreves tu a classe `Artigo`, crias com ela os dois artigos da sala, o caderno e a pasta, e pedes-lhes que retirem unidades. Pelo caminho, vês quando é que o construtor trabalha, o que acontece a um objeto quando falta o `self.` e o que quer dizer dar dois nomes ao mesmo objeto.

No fim, o programa `artigos.py` mostra:

```text
Caderno: 5
Pasta: 2
True
False
```

1. [Fase 1: Uma classe e dois objetos](#fase-1-uma-classe-e-dois-objetos)
2. [Fase 2: Quando é que o construtor trabalha](#fase-2-quando-é-que-o-construtor-trabalha)
3. [Fase 3: O que mostra um objeto inteiro](#fase-3-o-que-mostra-um-objeto-inteiro)
4. [Fase 4: O `self.` decide o que fica no objeto](#fase-4-o-self-decide-o-que-fica-no-objeto)
5. [Fase 5: O método retirar em Python](#fase-5-o-método-retirar-em-python)
6. [Fase 6: Cada instância é um objeto diferente](#fase-6-cada-instância-é-um-objeto-diferente)

## O que precisas

- O Python 3.10 ou mais recente. Para ver a versão, escreve `python3 --version` no terminal (no Windows, `py --version`). Aparece algo como `Python 3.12.4`, e o número a seguir a `3.` tem de ser 10 ou mais. Numa versão anterior, o laboratório corre na mesma, e só algumas mensagens de erro mudam.
- O editor das aulas, o mesmo do laboratório do tema 01.

Começas numa pasta nova: este laboratório não usa nenhum ficheiro do tema 01.

## Preparar o projeto

1. Cria a pasta deste laboratório, para não executares por engano o ficheiro de outro trabalho. Na pasta onde guardas os trabalhos de LP, cria uma pasta nova chamada `tema-02`.

2. Cria o ficheiro do programa. No editor, cria dentro da pasta `tema-02` um ficheiro novo chamado `artigos.py`, sem espaços nem acentos no nome. É o mesmo ficheiro da fase 1 à fase 6, e o conteúdo vai mudando de fase para fase.

## Fase 1: Uma classe e dois objetos

Escreves a classe `Artigo`, a descrição comum dos artigos, e crias com ela o A01, Caderno, com 6 unidades, e o A02, Pasta, com 2. Cada artigo passa a ser um objeto, com os seus próprios valores. Rever: [Uma classe e dois objetos](../02-objetos-classes-instancias.md#uma-classe-e-dois-objetos) e [Classe: a descrição comum](../02-objetos-classes-instancias.md#classe-a-descrição-comum).

1. Começa pela classe. Escreve no `artigos.py` esta primeira versão. Não copies nem coles: escreve-a tu, letra a letra, porque ao escrever reparas em pormenores que uma cópia esconde.

   ```python
   # artigos.py: a classe Artigo e os artigos da sala, do laboratório do tema 02.

   class Artigo:
       """Descreve um artigo do inventário: um material com código, nome e quantidade."""

       def __init__(self, codigo, nome, quantidade):
           """Prepara um artigo acabado de criar, guardando os três dados recebidos."""
           self.codigo = codigo
           self.nome = nome
           self.quantidade = quantidade
   ```

   Enquanto escreves, repara em três pormenores:

   - os dois pontos no fim das linhas `class Artigo:` e `def __init__(self, codigo, nome, quantidade):`;
   - os dois sublinhados antes e os dois depois de `init`;
   - a indentação: quatro espaços dentro da classe, e oito dentro do `__init__`.

   O `__init__` (do inglês "initialize", dar os valores iniciais) é o construtor. O Python executa-o sozinho sempre que se cria um artigo, e ele guarda no artigo novo os valores que recebe nos parâmetros `codigo`, `nome` e `quantidade`. O comentário do topo e as docstrings, o texto entre três aspas, podem ficar como aqui ou com palavras tuas.

   Guarda e executa, com o botão ou a tecla de executar do editor. O que deves ver: nada, e nenhuma mensagem de erro. Isto quer dizer que o Python leu a descrição da classe, mas ainda não criou nenhum artigo. Se aparecer outra coisa, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

2. Cria os dois artigos e mostra os dados deles. No fim do ficheiro, deixa duas linhas em branco a seguir à classe e acrescenta:

   ```python partial
   caderno = Artigo("A01", "Caderno", 6)
   pasta = Artigo("A02", "Pasta", 2)

   print(caderno.codigo, caderno.nome, caderno.quantidade)
   print(pasta.codigo, pasta.nome, pasta.quantidade)
   ```

   Cada linha `Artigo(...)` cria um objeto e entrega ao construtor os três valores entre parênteses. Os `print` consultam os atributos com o ponto: `caderno.nome` é o atributo `nome` do objeto `caderno`, um dos dados guardados nele.

   Guarda e executa. O que deves ver:

   ```text
   A01 Caderno 6
   A02 Pasta 2
   ```

   Isto quer dizer que há dois objetos, cada um com os seus três atributos. Se aparecer outra coisa, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

### Paragem 1

O programa mostra os dados dos dois artigos. Confere o teu `artigos.py` com este, completo:

```python
# artigos.py: a classe Artigo e os artigos da sala, do laboratório do tema 02.

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

Em cima está a classe, que o Python lê sem criar nada. Por baixo, as duas linhas `Artigo(...)` criam os objetos, e os dois `print` mostram os atributos de cada um.

Pensa antes de continuares: escreveste três valores dentro de cada `Artigo(...)`, mas o construtor tem quatro parâmetros. Quem preenche o parâmetro que falta? A resposta: o Python. O primeiro parâmetro, `self` (em inglês, "o próprio"), recebe o objeto novo, e é o próprio Python que o põe lá. Por isso, na chamada `Artigo(...)`, o `self` não se escreve.

## Fase 2: Quando é que o construtor trabalha

Pões no construtor uma linha provisória, que escreve uma frase de cada vez que ele trabalha. Assim vês que quem chama o construtor é o Python, no momento em que uma linha `Artigo(...)` corre. Rever: [Quando é que o construtor trabalha](../02-objetos-classes-instancias.md#quando-é-que-o-construtor-trabalha).

1. Acrescenta a linha provisória. Em `artigos.py`, dentro do construtor, a seguir à docstring e antes de `self.codigo = codigo`, acrescenta esta linha, com os mesmos oito espaços das linhas que começam por `self.`:

   ```python partial
           print("A preparar o artigo", codigo)
   ```

   A linha mostra uma frase e o código do artigo que está a ser criado. Como está dentro do construtor, só corre quando o construtor corre.

2. Antes de executares, prevê: quantas vezes aparece a frase "A preparar o artigo", e aparece antes ou depois de `A01 Caderno 6`? Depois guarda e executa. O que deves ver:

   ```text
   A preparar o artigo A01
   A preparar o artigo A02
   A01 Caderno 6
   A02 Pasta 2
   ```

   A resposta: a frase aparece duas vezes, uma por cada linha `Artigo(...)`. Aparece antes dos dados, porque as duas linhas que criam os artigos estão antes dos `print`. O construtor está escrito uma vez, na classe, e trabalhou duas.

3. Muda a ordem das linhas do fim, para o `print` do caderno ficar logo a seguir à linha que o cria. As linhas a seguir à classe ficam assim:

   ```python partial
   caderno = Artigo("A01", "Caderno", 6)
   print(caderno.codigo, caderno.nome, caderno.quantidade)
   pasta = Artigo("A02", "Pasta", 2)

   print(pasta.codigo, pasta.nome, pasta.quantidade)
   ```

   Guarda e executa. O que deves ver:

   ```text
   A preparar o artigo A01
   A01 Caderno 6
   A preparar o artigo A02
   A02 Pasta 2
   ```

   Isto quer dizer que o construtor trabalha quando a linha `Artigo(...)` corre, e não no início do programa nem quando o Python lê a classe.

4. Desfaz as duas mudanças. Apaga a linha provisória do construtor e põe as linhas do fim pela ordem da paragem 1. Guarda e executa: voltas a ver só `A01 Caderno 6` e `A02 Pasta 2`. A linha provisória serviu para veres o momento em que o construtor trabalha. O trabalho dele é preparar o objeto, e não escrever no ecrã.

### Paragem 2

O ficheiro voltou a ser o da paragem 1, e o programa mostra outra vez os dados dos dois artigos.

Pensa antes de continuares: se acrescentasses ao programa a linha `regua = Artigo("A06", "Régua", 10)`, quantas vezes trabalharia o construtor? A resposta: três vezes, uma por cada `Artigo(...)`. O construtor trabalha tantas vezes quantos os objetos que o programa cria.

## Fase 3: O que mostra um objeto inteiro

Até aqui pediste cada atributo pelo nome, com o ponto. Agora pedes ao `print` o objeto inteiro, sem dizer que atributo queres. Rever: [O que mostra um objeto inteiro](../02-objetos-classes-instancias.md#o-que-mostra-um-objeto-inteiro).

1. No fim do ficheiro, acrescenta esta linha:

   ```python partial
   print(caderno)
   ```

   Antes de executares, prevê o que vai aparecer depois das duas linhas de sempre.

2. Guarda e executa. Depois das duas linhas de sempre, aparece uma terceira parecida com esta, com outro número no fim:

   ```text
   <__main__.Artigo object at 0x105535fd0>
   ```

   A resposta: o Python não mostra os atributos. Mostra que é um objeto (em inglês, `object`) da classe `Artigo`, e o `__main__` quer dizer que a classe foi escrita no programa que executaste. O número depois de `at` diz em que sítio da memória do computador o objeto ficou guardado. Começa por `0x` e mistura algarismos e letras, e não precisas de o saber ler.

3. Executa outra vez e compara o número com o da primeira execução. Em geral muda, pelo menos em parte: cada execução começa do zero, e o objeto pode ficar guardado noutro sítio.

4. Acrescenta no fim a linha `print(pasta)`, guarda e executa. O que deves ver: duas linhas que começam por `<__main__.Artigo object at`, com números diferentes. Isto quer dizer que o programa tem dois objetos, guardados em dois sítios da memória.

5. Apaga as linhas `print(caderno)` e `print(pasta)`, guarda e executa. Voltas a ver só os dados dos dois artigos.

### Paragem 3

O ficheiro está igual ao da paragem 1, e o programa volta a mostrar `A01 Caderno 6` e `A02 Pasta 2`. O `print` de um objeto inteiro mostra a classe e o sítio da memória, e não os atributos.

Pensa antes de continuares: para mostrar o nome do caderno, porque é que se escreve `print(caderno.nome)`, e não `print(caderno)`? A resposta: o `print` não sabe que dado do caderno te interessa. Por isso, cada atributo pede-se pelo nome, depois do ponto.

## Fase 4: O `self.` decide o que fica no objeto

Tiras o `self.` de uma linha do construtor, de propósito, e vês o que acontece ao objeto. Na linha `self.nome = nome`, o `nome` da direita é o parâmetro, que desaparece quando o construtor acaba, e o `self.nome` é o atributo, que fica no objeto. Rever: [O `self.` decide o que fica no objeto](../02-objetos-classes-instancias.md#o-self-decide-o-que-fica-no-objeto).

1. No construtor, na linha `self.nome = nome`, apaga `self.`. A linha fica `nome = nome`. Não mexas em mais nada.

2. Antes de executares, prevê: o Python vai queixar-se da linha `nome = nome`? E o que acontece quando o programa pedir `caderno.nome`?

3. Guarda e executa. O programa para sem mostrar os dados dos artigos, com uma mensagem de erro parecida com esta:

   ```text
   Traceback (most recent call last):
     File ".../tema-02/artigos.py", line 16, in <module>
       print(caderno.codigo, caderno.nome, caderno.quantidade)
                             ^^^^^^^^^^^^
   AttributeError: 'Artigo' object has no attribute 'nome'
   ```

   A resposta: o Python não se queixou da linha `nome = nome`, e só parou quando o programa pediu `caderno.nome`. A primeira linha, com `Traceback`, anuncia o rasto do erro, o caminho que o programa fez até parar. A linha com `File` diz onde parou, na linha 16, e no lugar dos três pontos aparece a pasta do teu computador. A linha dos `^` aponta a parte da instrução onde o erro aconteceu, e só aparece a partir do Python 3.11. A última linha diz o tipo de erro, `AttributeError` (erro de atributo): o objeto do tipo `Artigo` não tem nenhum atributo `nome`.

4. Encontra a causa. A mensagem aponta a linha 16, a do primeiro `print`, se escreveste o programa como na paragem 1. A causa está na linha 9, `nome = nome`. É uma atribuição válida, e por isso o Python não a recusou: guarda o valor numa variável do construtor, que deixa de existir quando ele acaba. O objeto nasceu com `codigo` e `quantidade`, mas sem `nome`.

5. Confirma que só falta o nome. Muda, por agora, os dois `print` do fim para mostrarem só o código e a quantidade:

   ```python partial
   print(caderno.codigo, caderno.quantidade)
   print(pasta.codigo, pasta.quantidade)
   ```

   Guarda e executa. O que deves ver:

   ```text
   A01 6
   A02 2
   ```

   Isto quer dizer que os dois objetos foram criados, e só lhes falta o atributo em que tiraste o `self.`.

6. Repõe `self.nome = nome` no construtor e os dois `print` como estavam. Guarda e executa: aparecem outra vez `A01 Caderno 6` e `A02 Pasta 2`.

### Paragem 4

O ficheiro está outra vez como na paragem 1, e no ecrã aparecem de novo os dados dos dois artigos, sem nenhuma mensagem de erro.

Pensa antes de continuares: o Python mostrou o erro na linha 16, mas o engano estava na linha 9. O que te diz isto sobre a maneira de procurar a causa de um erro? A resposta: a linha que a mensagem aponta é onde o erro se viu, e nem sempre onde nasceu. Parte dela e sobe no programa até à instrução que devia ter guardado o atributo.

## Fase 5: O método retirar em Python

Acrescentas à classe o método `retirar`, uma operação que cada artigo sabe fazer, e pedes ao caderno que retire duas unidades. Depois experimentas outra forma de escrever a mesma chamada, para veres quem é o `self`. Rever: [O método retirar em Python](../02-objetos-classes-instancias.md#o-método-retirar-em-python) e [Método: uma operação que pertence ao objeto](../02-objetos-classes-instancias.md#método-uma-operação-que-pertence-ao-objeto).

1. Acrescenta o método à classe, a seguir ao construtor, com uma linha em branco entre os dois. A linha `def retirar(self, unidades):` leva os mesmos quatro espaços de `def __init__`, e as linhas de dentro levam oito:

   ```python partial
       def retirar(self, unidades):
           """Retira unidades a este artigo e devolve a quantidade que fica.

           Esta primeira versão ainda não verifica se o pedido é possível.
           Neste laboratório só fazemos pedidos que sabemos serem válidos.
           """
           self.quantidade = self.quantidade - unidades
           return self.quantidade
   ```

   O parâmetro `unidades` recebe as unidades que se pedem, e o `self` é o artigo que recebeu o pedido. A linha `self.quantidade = self.quantidade - unidades` calcula primeiro o lado direito, a quantidade deste artigo menos as unidades pedidas, e guarda o resultado no mesmo atributo. O `return` entrega a quantidade que ficou a quem chamou o método, sem a mostrar: mostrar é o trabalho do `print`.

2. Troca as linhas que vêm depois da classe, a partir de `caderno = ...`, por estas:

   ```python partial
   caderno = Artigo("A01", "Caderno", 6)
   pasta = Artigo("A02", "Pasta", 2)

   print("Antes:", caderno.quantidade, pasta.quantidade)
   restante = caderno.retirar(2)
   print("Depois:", caderno.quantidade, pasta.quantidade)
   print("Devolvido:", restante)
   ```

   A linha `restante = caderno.retirar(2)` pede ao caderno que retire duas unidades e guarda em `restante` o valor que o método devolve. O `2` é o argumento, o valor que ocupa o parâmetro `unidades` nesta chamada.

3. Guarda e executa. O que deves ver:

   ```text
   Antes: 6 2
   Depois: 4 2
   Devolvido: 4
   ```

   Isto quer dizer que o pedido chegou só ao caderno, que passou de 6 para 4, e que o método devolveu o 4 que ficou. Se aparecer outra coisa, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

4. Experimenta a forma longa da mesma chamada. Na linha `restante = caderno.retirar(2)`, troca `caderno.retirar(2)` por `Artigo.retirar(caderno, 2)`. Esta forma lê-se "executa o `retirar` da classe `Artigo`, com o `self` igual a `caderno` e as `unidades` iguais a 2". Guarda e executa. O que deves ver: as mesmas três linhas do passo 3, porque as duas formas pedem exatamente a mesma coisa.

5. Troca agora `Artigo.retirar(caderno, 2)` por `Artigo.retirar(pasta, 2)`. Antes de executares, prevê: a qual dos dois artigos saem as duas unidades? Depois guarda e executa. O que deves ver:

   ```text
   Antes: 6 2
   Depois: 6 0
   Devolvido: 0
   ```

   A resposta: à pasta, que passa de 2 para 0, porque na forma longa o `self` é o primeiro valor entre os parênteses. Ficar com 0 unidades é um estado válido, e a chamada não tem nada de errado. Na forma curta, `caderno.retirar(2)`, o objeto que ocupa o `self` é o que está antes do ponto.

6. Volta a pôr `restante = caderno.retirar(2)`, guarda e executa: aparecem outra vez as três linhas do passo 3. Nos programas escreve-se sempre a forma curta. A longa serviu só para veres em que lugar entra o objeto.

### Paragem 5

O programa mostra `Antes: 6 2`, `Depois: 4 2` e `Devolvido: 4`. O teu `artigos.py` deve estar agora assim:

```python
# artigos.py: a classe Artigo e os artigos da sala, do laboratório do tema 02.

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
        Neste laboratório só fazemos pedidos que sabemos serem válidos.
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

O método `retirar` ficou dentro da classe, a seguir ao construtor e com a mesma indentação. Por baixo da classe estão os dois artigos, o pedido ao caderno e os três `print`.

Pensa antes de continuares: se apagasses `restante =` e deixasses só `caderno.retirar(2)`, com que quantidade ficava o caderno? A resposta: com 4 na mesma, porque a quantidade muda dentro do método. Perdia-se só o valor devolvido. A linha `print("Devolvido:", restante)` deixava de funcionar, e o programa parava aí, já depois de mostrar `Depois: 4 2`, com `NameError: name 'restante' is not defined` ("o nome `restante` não está definido").

## Fase 6: Cada instância é um objeto diferente

Dás ao caderno um segundo nome e depois comparas o caderno com um artigo novo, criado com os mesmos valores. Para comparar, usas o `is` (em inglês, "é"), que pergunta se dois nomes apontam para o mesmo objeto e dá `True` (verdadeiro) ou `False` (falso). Rever: [Cada instância é um objeto diferente](../02-objetos-classes-instancias.md#cada-instância-é-um-objeto-diferente).

1. Troca as linhas que vêm depois da classe por estas. A classe fica igual, com o construtor e o `retirar`:

   ```python partial
   caderno = Artigo("A01", "Caderno", 6)
   pasta = Artigo("A02", "Pasta", 2)
   mesmo_caderno = caderno

   mesmo_caderno.retirar(1)

   print("Caderno:", caderno.quantidade)
   print("Pasta:", pasta.quantidade)
   print(caderno is mesmo_caderno)
   print(caderno is pasta)
   ```

   Os dois últimos `print` perguntam, com `is`, se dois nomes apontam para o mesmo objeto.

2. Antes de executares, prevê: o pedido é feito através de `mesmo_caderno`, mas qual dos artigos perde a unidade? Depois guarda e executa. O que deves ver:

   ```text
   Caderno: 5
   Pasta: 2
   True
   False
   ```

   A resposta: perde-a o caderno, porque os dois nomes apontam para o mesmo objeto. A linha `mesmo_caderno = caderno` não tem `Artigo(...)`, e por isso não nasce nenhum artigo novo. O objeto do caderno continua a ser um só, agora com dois nomes, como uma caixa com duas etiquetas coladas. Assim, `caderno is mesmo_caderno` dá `True`, e `caderno is pasta` dá `False`.

3. Troca a linha `mesmo_caderno = caderno` por esta, que cria um artigo novo com os valores com que o caderno começou:

   ```python partial
   mesmo_caderno = Artigo("A01", "Caderno", 6)
   ```

   E acrescenta no fim do ficheiro esta linha:

   ```python partial
   print("Mesmo caderno:", mesmo_caderno.quantidade)
   ```

4. Guarda e executa. O que deves ver:

   ```text
   Caderno: 6
   Pasta: 2
   False
   False
   Mesmo caderno: 5
   ```

   Isto quer dizer que há agora três objetos, um por cada `Artigo(...)`, e que a unidade saiu do novo, o que tem o nome `mesmo_caderno`. O caderno ficou com 6. `caderno is mesmo_caderno` dá agora `False`, porque são dois objetos, criados por duas chamadas a `Artigo(...)`, mesmo tendo começado com os mesmos valores. O `is` não compara os valores: pergunta se é o mesmo objeto. Na fase 3, o caderno e a pasta tinham números de memória diferentes pela mesma razão. O Python aceitou dois artigos com o código A01, contra a primeira regra do inventário, porque não conhece as regras: quem as cumpre é quem escreve o programa. Rever: [Uma operação tem de respeitar regras](../01-entidades-estado-acoes.md#uma-operação-tem-de-respeitar-regras), no guia 01.

5. Volta a pôr `mesmo_caderno = caderno` e apaga a última linha que acrescentaste. Guarda e executa: aparecem outra vez as quatro linhas do passo 2.

### Paragem 6

O programa mostra `Caderno: 5`, `Pasta: 2`, `True` e `False`. O `artigos.py` completo, como deve ficar no fim do laboratório:

```python
# artigos.py: a classe Artigo e os artigos da sala, do laboratório do tema 02.

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
        Neste laboratório só fazemos pedidos que sabemos serem válidos.
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

A classe é a da paragem 5. Por baixo estão os dois artigos, o segundo nome do caderno, o pedido feito através dele e os quatro `print`.

Pensa antes de terminares: se, a seguir a `mesmo_caderno.retirar(1)`, escrevesses `caderno.retirar(1)`, com que quantidade ficava o caderno? A resposta: com 4. Os dois pedidos chegam ao mesmo objeto, um através de cada nome, e cada um tira uma unidade.

## Se alguma coisa falhar

1. Guardaste o ficheiro antes de executar? Se o programa mostra o mesmo de antes, apesar de teres mudado o código, guarda e executa outra vez.
2. Estás a executar o ficheiro certo? Tem de ser o `artigos.py` da pasta `tema-02`.
3. Executaste o ficheiro todo, e não só umas linhas? Cada execução volta a criar os artigos com os valores escritos e faz tudo pela ordem do ficheiro.
4. Desfizeste a experiência anterior? As fases 2, 3 e 4 acabam com o ficheiro da paragem 1. Se te perderes, copia o último ficheiro completo a que chegaste, o da paragem 1, o da paragem 5 ou o da paragem 6, e refaz os passos que faltam.
5. Apareceu uma mensagem de erro? Lê primeiro a última linha, com o tipo de erro e a razão, e procura-a nos problemas a seguir. Quando a mensagem começa por `Traceback`, o erro aconteceu com o programa já a correr. Num erro de escrita, como um `SyntaxError` ou um `IndentationError`, o programa nem chega a correr, e a mensagem abre logo com o ficheiro e a linha. Na primeira classe, enganos destes são normais.

### Aparece `SyntaxError: expected ':'` ou `SyntaxError: invalid syntax`

Quer dizer "erro de escrita: esperava `:`". Falta o sinal de dois pontos no fim de uma linha `class` ou `def`. Escreve-o no fim da linha que a mensagem mostra. No Python 3.9, a mesma falta dá só `invalid syntax`. Se os dois pontos estiverem todos no sítio, vê [o último problema desta secção](#aparece-outro-syntaxerror-indentationerror-ou-taberror).

### Aparece `IndentationError: expected an indented block`

Em português, "erro de indentação: esperava-se um bloco indentado". As linhas de dentro de um `class` ou de um `def`, com a docstring, ficaram encostadas à mesma margem que ele. A partir do Python 3.10, a mensagem acaba em `on line` e no número da linha desse `class` ou `def`. Dentro da classe, o `def` leva quatro espaços, e as linhas de dentro de um método levam oito, a docstring incluída.

### Aparece `IndentationError: unexpected indent`

Quer dizer "indentação inesperada": uma linha tem mais espaços do que a de cima. Acontece, por exemplo, quando a linha provisória da fase 2 fica com quatro espaços em vez de oito: o Python queixa-se da linha `self.codigo = codigo`, a seguir a ela. Compara os espaços de cada linha com os do último ficheiro completo.

### Aparece `NameError: name 'codigo' is not defined`

As linhas que começam por `self.` ficaram com quatro espaços, a margem do `def`, e só a docstring ficou dentro do construtor. Essas linhas passaram a pertencer à classe, fora do construtor, onde o parâmetro `codigo` não existe. Dá-lhes oito espaços, como à docstring.

### Aparece `NameError: name 'artigo' is not defined`

A classe tem o nome com maiúscula e a chamada está com minúscula, ou ao contrário, e para o Python são dois nomes. As versões recentes do Python acrescentam `Did you mean: 'Artigo'?` ("querias dizer `Artigo`?"). Escreve sempre `Artigo`, com maiúscula.

### Aparece `TypeError: Artigo() takes no arguments`

Quer dizer "erro de tipo: `Artigo()` não aceita argumentos". O nome do construtor está mal escrito, como `_init_`, com um só sublinhado de cada lado, ou `__innit__`. Sem um `__init__` com esse nome exato, a classe não tem construtor que receba os três valores. Escreve o nome assim: dois sublinhados, a palavra `init` e outros dois sublinhados.

### Aparece `TypeError: Artigo.__init__() takes 3 positional arguments but 4 were given`

Compara a tua linha `def __init__` com a da [paragem 1](#paragem-1).

### Aparece `TypeError: Artigo.retirar() takes 1 positional argument but 2 were given`

Quer dizer "o `retirar` aceita 1 argumento, mas recebeu 2". No Python 3.9, a mensagem começa por `retirar()`, sem `Artigo.`. Compara a tua linha `def retirar` com a do ficheiro da [paragem 5](#paragem-5).

### Aparece `AttributeError: 'Artigo' object has no attribute 'quantidade'`

O construtor guardou a quantidade com outro nome, por um engano como `self.quantiade`, ou sem o `self.` à frente. As versões recentes do Python podem sugerir o nome que existe, como `Did you mean: 'quantiade'?`. O nome depois de `self.` tem de ser exatamente o que usas no resto do programa.

### Aparece `AttributeError: 'Artigo' object has no attribute 'retirar'`

A linha `def retirar` ficou encostada à margem, e o método saiu da classe. O Python aceita-o como uma função solta, mas os objetos `Artigo` não o têm. Dá ao `def` quatro espaços, como ao do construtor, e oito às linhas de dentro.

### Aparece `Depois: 6 2`, sem nenhuma mensagem de erro

Na linha da conta do `retirar` falta o `self.` à esquerda do `=`. A conta fica guardada numa variável do método, que desaparece quando ele acaba, como o `nome = nome` da fase 4, e a quantidade do caderno não muda. A linha tem de começar por `self.quantidade =`. Se o `self.` faltar à direita, em `quantidade - unidades`, o programa para com `NameError: name 'quantidade' is not defined`, e o Python 3.14 acrescenta `Did you mean: 'self.quantidade'?`.

### Aparece outro `SyntaxError`, `IndentationError` ou `TabError`

Compara, letra a letra e espaço a espaço, a linha que a mensagem mostra e a de cima com as do bloco que escreveste. No Python 3.9, a linha apontada pode vir depois do engano. Os enganos mais comuns, com as mensagens do Python 3.14 e do 3.9:

- falta uma das três aspas no fim de uma docstring: `SyntaxError: unterminated triple-quoted string literal`; no 3.9, `SyntaxError: EOF while scanning triple-quoted string literal`, a apontar a última linha do ficheiro;
- falta fechar um parêntese: `SyntaxError: '(' was never closed`; no 3.9, só `SyntaxError: invalid syntax`, a apontar a linha de baixo, ou `SyntaxError: unexpected EOF while parsing`, se for a última linha;
- um `def` tem outro número de espaços que não quatro: `IndentationError: unindent does not match any outer indentation level`, nas duas versões;
- uma linha tem uma tabulação no lugar dos espaços: `TabError: inconsistent use of tabs and spaces in indentation`, nas duas versões. Apaga a tabulação e escreve os espaços.

## Desafios

1. Escrever a classe de cor. Fecha o guia e o ficheiro `artigos.py`. Na pasta `tema-02`, cria um ficheiro novo chamado `memoria.py`. Sem olhar para nada, escreve a classe `Artigo`, com o construtor e o método `retirar`. Por baixo, escreve as linhas para criar um artigo à tua escolha, retirar-lhe unidades e mostrar a quantidade que fica. Executa e, se aparecer um erro, corrige-o a partir da última linha da mensagem. Só depois abre o `artigos.py` e compara, linha a linha. Num comentário no fim do `memoria.py`, escreve todas as diferenças, mesmo as pequenas, e separa as que faziam o programa falhar das que não faziam diferença. Pista: um sublinhado a menos, dois pontos esquecidos e um `self.` que ficou por escrever são diferenças pequenas que mudam muito.

2. Uma classe para outra coisa da escola. Cada sala da escola tem um projetor, e a lâmpada de um projetor tem de ser trocada ao fim de um certo número de horas de uso. Para saber quando, a escola quer registar, para cada projetor, um código, a sala onde está e as horas de uso que já acumulou. Num ficheiro `projetor.py`, escreve:

   - uma classe `Projetor`, com um construtor que guarde o código, a sala e as horas de uso em três atributos: `codigo`, `sala` e `horas_uso`. A sala guarda-se como texto, por exemplo `"Sala 12"`;
   - um método `usar`, com um parâmetro `horas`, que acrescente as horas recebidas às horas de uso e devolva o total que fica. Ainda não precisa de verificar se o pedido é válido;
   - as docstrings da classe, do construtor e do método.

   Depois da classe, cria dois projetores: o P01, na Sala 12, com 150 horas de uso, e o P02, na Sala 7, acabado de comprar, com 0 horas. Usa o P01 durante 3 horas, depois o P02 durante 2 horas e depois o P01 durante 1 hora. Guarda numa variável o valor devolvido pela última chamada. No fim, mostra numa só linha as horas de uso dos dois projetores e o valor que guardaste. Antes de executares, segue de cabeça o traço das três chamadas e prevê a linha que vai aparecer. Num comentário no início do `projetor.py`, responde: porque é que aqui faz sentido uma classe nova, e não a classe `Artigo`? Pista: compara os dados e as operações de um projetor com os de um artigo.

## Antes de terminares

- [ ] O `artigos.py` da pasta `tema-02` corre e mostra `Caderno: 5`, `Pasta: 2`, `True` e `False`.
- [ ] Desfizeste todas as experiências: o ficheiro está igual ao da paragem 6.
- [ ] Guardaste o `artigos.py` e, se fizeste os desafios, o `memoria.py` e o `projetor.py`, e entregaste-os pelo meio que o professor indicar.
- [ ] Consegues explicar, por palavras tuas, quando é que o construtor trabalha, quem é o `self` em `caderno.retirar(2)` e porque é que `mesmo_caderno = caderno` não cria um artigo novo.
- [ ] Consegues explicar a diferença entre a classe `Artigo` e os objetos `caderno` e `pasta`.

![Rodapé](../../imagens/rodape.png)

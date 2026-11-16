![Cabeçalho](../../imagens/cabecalho.png)

# Laboratório: Composição e modelação

## O que vais construir

Partes da classe `Artigo` do tema 03 e escreves a classe `Inventario`, que cria os artigos, os guarda e lhes passa os pedidos, sem deixar repetir um código. No fim, provocas uma recusa que atravessa vários métodos e lês, no ecrã, o caminho que ela fez.

Acabado, o programa `inventario.py` mostra:

```text
Registo de A01 recusado: Já existe um artigo com o código A01.
Registo de A03 recusado: A quantidade não pode ser negativa.
Consulta de A03 recusada: Não existe nenhum artigo com o código A03.
A01 depois de retirar 2: 4
Retirar 9 de A01 recusado: A quantidade não pode ser negativa.
Retirar de A07 recusado: Não existe nenhum artigo com o código A07.
A01 no fim: 4
A02 no fim: 2
```

1. [Fase 1: Uma lista para guardar os artigos](#fase-1-uma-lista-para-guardar-os-artigos)
2. [Fase 2: O inventário cria os artigos e encontra-os pelo código](#fase-2-o-inventário-cria-os-artigos-e-encontra-os-pelo-código)
3. [Fase 3: O inventário passa os pedidos aos artigos](#fase-3-o-inventário-passa-os-pedidos-aos-artigos)
4. [Fase 4: O caminho de uma recusa](#fase-4-o-caminho-de-uma-recusa)

## O que precisas

- O Python 3.10 ou mais recente. Para saberes qual tens, escreve `python3 --version` no terminal (no Windows, `py --version`), e aparece, por exemplo, `Python 3.12.4`. Numa versão anterior, o laboratório funciona na mesma: só mudam algumas mensagens de erro, e o laboratório diz quais.
- O editor das aulas, que já usaste nos três laboratórios anteriores.

Começas numa pasta vazia: a classe `Artigo`, de onde partes, vem escrita em [Preparar o projeto](#preparar-o-projeto).

## Preparar o projeto

1. Cria uma pasta nova, `tema-04`, na pasta onde guardas os trabalhos de LP. Com uma pasta por tema, não executas sem querer o ficheiro de outro laboratório.

2. Dentro de `tema-04`, cria no editor o ficheiro `inventario.py`, com o nome assim, sem espaços nem acentos. É o único ficheiro das quatro fases, e vai crescendo de fase para fase.

3. Copia para o `inventario.py` esta versão da classe `Artigo`. Tem as instruções do `artigo.py` do fim do tema 03, com as docstrings mais curtas, para os números das linhas nas mensagens de erro serem os do laboratório:

   ```python
   # inventario.py: as classes Artigo e Inventario, do laboratório do tema 04.

   class Artigo:
       """Artigo do inventário: código, nome e uma quantidade sempre válida.

       É a classe final do guia 03, com as docstrings encurtadas.
       """

       def __init__(self, codigo, nome, quantidade):
           """Cria o artigo. A quantidade inicial passa pelo setter."""
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
           """Acrescenta unidades (inteiro, 1 ou mais); senão, lança ValueError."""
           if not isinstance(unidades, int):
               raise ValueError("As unidades a adicionar têm de ser um número inteiro.")
           if unidades <= 0:
               raise ValueError("As unidades a adicionar têm de ser 1 ou mais.")
           self.quantidade = self.quantidade + unidades

       def retirar(self, unidades):
           """Retira unidades (inteiro, 1 ou mais, até ao que existe); senão, lança ValueError."""
           if not isinstance(unidades, int):
               raise ValueError("As unidades a retirar têm de ser um número inteiro.")
           if unidades <= 0:
               raise ValueError("As unidades a retirar têm de ser 1 ou mais.")
           # A falta de unidades é recusada pelo setter: o resultado seria negativo.
           self.quantidade = self.quantidade - unidades
   ```

   O setter é o segundo `def quantidade`. Todas as escritas na quantidade passam por ele, também as do construtor, do `adicionar` e do `retirar`, e é ele que recusa um valor negativo. Rever: [A propriedade `quantidade`](../03-encapsulamento-contratos.md#a-propriedade-quantidade).

   Guarda e executa. O que deves ver: nada. O ficheiro só tem a classe, e nenhuma linha cria um artigo. Se aparecer outra coisa, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

## Fase 1: Uma lista para guardar os artigos

Escreves a classe `Inventario` só com o construtor, que dá a cada inventário uma lista vazia, `_artigos`, onde vão ficar os artigos. O sublinhado diz que a lista é interna, e quem quer juntar um artigo, de fora, pede-o ao inventário. Rever: [Uma lista para guardar os artigos](../04-composicao-modelacao.md#uma-lista-para-guardar-os-artigos).

1. Depois da classe `Artigo`, deixa duas linhas em branco e escreve a classe `Inventario`, só com o construtor. Escreve-a à mão, sem copiar, para reparares no sublinhado de `_artigos` e nos dois pontos no fim das linhas `class` e `def`:

   ```python partial
   class Inventario:
       """Inventário que cria, guarda e controla os seus artigos."""

       def __init__(self):
           """Cria um inventário vazio, ainda sem artigos."""
           self._artigos = []
   ```

2. Deixa duas linhas em branco depois da classe `Inventario` e escreve, encostadas à margem, estas duas linhas, que criam um inventário e mostram a lista dele:

   ```python partial
   inventario = Inventario()
   print(inventario._artigos)
   ```

   Os parênteses de `Inventario()` ficam vazios, porque o construtor só recebe o `self`. Guarda e executa. O que deves ver:

   ```text
   []
   ```

   É a lista vazia que o construtor criou: o inventário existe e ainda não tem artigos. Aqui espreitas a lista interna só para testar o construtor, e no programa final nenhuma linha de fora lhe mexe. Se aparecer outra coisa, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

3. Apaga a linha do `print` e deixa ficar `inventario = Inventario()`.

### Paragem 1

O ficheiro tem as duas classes e, no fim, a linha que cria o inventário. Executa-o: não aparece nada.

Pensa antes de continuares: se criasses dois inventários, `a = Inventario()` e `b = Inventario()`, e juntasses um artigo à lista de `a`, a lista de `b` mudava? A resposta: não. Cada `Inventario()` corre o construtor outra vez, e cada vez nasce uma lista nova, só desse inventário.

## Fase 2: O inventário cria os artigos e encontra-os pelo código

Acrescentas o `_procurar`, que encontra um artigo pelo código, e o `registar`, que cria um artigo novo sem repetir um código. No `registar` está a composição em Python, porque é o inventário que chama `Artigo(...)`, dentro de um método seu. Rever: [O inventário cria os artigos e encontra-os pelo código](../04-composicao-modelacao.md#o-inventário-cria-os-artigos-e-encontra-os-pelo-código) e [O nosso inventário: composição](../04-composicao-modelacao.md#o-nosso-inventário-composição).

1. Dentro da classe `Inventario`, a seguir ao construtor, deixa uma linha em branco e escreve o método `_procurar`, com o `def` à mesma distância da margem que o do construtor:

   ```python partial
       def _procurar(self, codigo):
           """Método interno: devolve o artigo com este código.

           Falha: lança ValueError se não houver nenhum artigo com este código.
           """
           for artigo in self._artigos:
               if artigo.codigo == codigo:
                   return artigo
           raise ValueError("Não existe nenhum artigo com o código " + codigo + ".")
   ```

   O `raise` fica alinhado com o `for`, e não com o `if`. Assim, só se chega a ele depois de o ciclo ver todos os artigos sem dar com o código.

2. A seguir ao `_procurar`, deixa outra linha em branco e escreve o método `registar`:

   ```python partial
       def registar(self, codigo, nome, quantidade):
           """Cria um artigo novo e guarda-o no inventário.

           Recebe: o código, o nome e a quantidade inicial do artigo.
           Devolve: nada (None).
           Falha: lança ValueError se já existir um artigo com este código, ou
           se a quantidade inicial for inválida (quem a recusa é o setter do
           artigo). Em qualquer falha, o inventário fica como estava.
           """
           for artigo in self._artigos:
               if artigo.codigo == codigo:
                   raise ValueError("Já existe um artigo com o código " + codigo + ".")
           novo = Artigo(codigo, nome, quantidade)
           self._artigos.append(novo)
   ```

   A ordem conta: o método verifica o código, depois cria o artigo e só no fim o junta à lista, com o `append` (do inglês, acrescentar). Assim, quando recusa, a lista fica como estava.

3. No fim do ficheiro, a seguir a `inventario = Inventario()`, acrescenta estas linhas, que registam dois artigos e espreitam o resultado:

   ```python partial
   inventario.registar("A01", "Caderno", 6)
   inventario.registar("A02", "Pasta", 2)
   print(len(inventario._artigos))
   print(inventario._procurar("A02").nome)
   ```

   Antes de executares, prevê as duas linhas que vão aparecer. Depois guarda e executa. O que deves ver:

   ```text
   2
   Pasta
   ```

   A resposta: `len` (do inglês *length*, comprimento) conta os elementos da lista, e há lá os dois artigos que o inventário criou. A segunda linha lê-se da esquerda para a direita: `_procurar("A02")` devolve o artigo A02, e `.nome` dá o nome dele. A lista e o `_procurar` são internos, e só os usas aqui de fora para testar. Se aparecer outra coisa, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

4. Provoca agora a recusa de um código repetido. No fim do ficheiro, fora de qualquer `try`, acrescenta:

   ```python partial
   inventario.registar("A01", "Cola", 3)
   ```

   Guarda e executa. Depois das duas linhas de antes, o programa para com esta mensagem:

   ```text
   Traceback (most recent call last):
     File ".../tema-04/inventario.py", line 85, in <module>
       inventario.registar("A01", "Cola", 3)
       ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
     File ".../tema-04/inventario.py", line 75, in registar
       raise ValueError("Já existe um artigo com o código " + codigo + ".")
   ValueError: Já existe um artigo com o código A01.
   ```

   No lugar dos três pontos está a pasta do teu computador, e antes do Python 3.11 não aparece a linha de `~` e `^`. Cada linha `File` diz o número de uma linha do ficheiro e o sítio onde o Python estava, com o código dessa linha por baixo. Se escreveste o ficheiro como os passos dizem, são as linhas 85 e 75, e uma linha em branco a mais ou a menos muda esses números. A de cima acaba em `in <module>`, que é o programa principal, as linhas que vêm depois das classes. A de baixo acaba em `in registar` e mostra o `raise` do `registar`. Quem recusou foi, portanto, o inventário, o único que conhece todos os códigos. Se aparecer outra coisa, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

5. Apaga as três linhas de teste desta fase: os dois `print` e o registo da cola. Ficam a criação do inventário e os dois primeiros registos.

### Paragem 2

O programa regista o caderno e a pasta e não mostra nada.

Pensa antes de continuares: se acrescentasses `inventario.registar("A03", "Caneta", -5)`, quem recusava, e a caneta ficava na lista? A resposta: recusava o setter do artigo, com "A quantidade não pode ser negativa.". O `registar` chega à linha `Artigo(...)`, o construtor do artigo escreve a quantidade, e o setter recusa o -5 antes de o `append` correr. A lista continua com dois artigos.

## Fase 3: O inventário passa os pedidos aos artigos

Acrescentas o `quantidade_de` e o `retirar`, que encontram o artigo com o `_procurar` e lhe passam o pedido, sem verificarem as unidades. A esta forma de colaborar chama-se encaminhamento, e as regras das unidades ficam só no artigo. Rever: [O inventário passa os pedidos aos artigos](../04-composicao-modelacao.md#o-inventário-passa-os-pedidos-aos-artigos) e [Exemplo guiado: oito pedidos ao inventário](../04-composicao-modelacao.md#exemplo-guiado-oito-pedidos-ao-inventário).

1. Dentro da classe `Inventario`, a seguir ao `registar`, escreve os dois métodos, com uma linha em branco antes de cada `def`:

   ```python partial
       def quantidade_de(self, codigo):
           """Devolve a quantidade do artigo com este código, sem a alterar.

           Falha: lança ValueError se não houver nenhum artigo com este código.
           """
           artigo = self._procurar(codigo)
           return artigo.quantidade

       def retirar(self, codigo, unidades):
           """Encaminha um pedido de retirada para o artigo com este código.

           Recebe: o código do artigo e as unidades a retirar.
           Devolve: nada (None).
           Falha: lança ValueError se não houver nenhum artigo com este código,
           ou se o próprio artigo recusar o pedido, pelas regras do seu método
           retirar. Em qualquer falha, nenhuma quantidade muda.
           """
           artigo = self._procurar(codigo)
           artigo.retirar(unidades)
   ```

   Os dois começam por `self._procurar(codigo)`: dentro de um método, o inventário chama outro método seu através do `self`. Sem o `self.`, o Python não encontra o `_procurar`. Na última linha, o `retirar` é o do artigo, e não o do inventário, porque antes do ponto está um artigo.

2. Antes de escreveres o programa principal, faz de cabeça o traço dos oito pedidos que ele vai fazer ao inventário, com os métodos que tens. Cada linha parte do estado que a anterior deixou. As quatro primeiras estão feitas; prevê as que têm um ponto de interrogação:

   | Pedido | Quem responde | Resposta | Artigos no inventário depois |
   | --- | --- | --- | --- |
   | `registar("A01", "Caderno", 6)` | Inventário: código livre; setter do artigo: 6 é válido | Aceite | A01 com 6 |
   | `registar("A02", "Pasta", 2)` | Inventário e setter do artigo | Aceite | A01 com 6, A02 com 2 |
   | `registar("A01", "Cola", 3)` | Inventário: A01 já existe | `ValueError`, antes de criar o artigo | A01 com 6, A02 com 2 |
   | `registar("A03", "Caneta", -5)` | Inventário: código livre; setter do artigo: -5 é negativo | `ValueError`, ao criar o artigo, antes do `append` | A01 com 6, A02 com 2 |
   | `quantidade_de("A03")` | ? | ? | ? |
   | `retirar("A01", 2)` | ? | ? | ? |
   | `retirar("A01", 9)` | ? | ? | ? |
   | `retirar("A07", 1)` | ? | ? | ? |

   A resposta, nas quatro linhas que faltavam:

   | Pedido | Quem responde | Resposta | Artigos no inventário depois |
   | --- | --- | --- | --- |
   | `quantidade_de("A03")` | `_procurar` do inventário: A03 não existe | `ValueError` | A01 com 6, A02 com 2 |
   | `retirar("A01", 2)` | Inventário encontra A01; o artigo aceita | Aceite | A01 com 4, A02 com 2 |
   | `retirar("A01", 9)` | Inventário encontra A01; setter do artigo: 4 - 9 = -5 | `ValueError` | A01 com 4, A02 com 2 |
   | `retirar("A07", 1)` | `_procurar` do inventário: A07 não existe | `ValueError` | A01 com 4, A02 com 2 |

   A consulta de A03 falha porque a caneta recusada nunca chegou à lista.

3. Escreve agora o programa principal. Substitui todas as linhas que estão depois das duas classes, a partir de `inventario = Inventario()`, por estas:

   ```python partial
   inventario = Inventario()
   inventario.registar("A01", "Caderno", 6)
   inventario.registar("A02", "Pasta", 2)

   try:
       inventario.registar("A01", "Cola", 3)
   except ValueError as erro:
       print("Registo de A01 recusado:", erro)

   try:
       inventario.registar("A03", "Caneta", -5)
   except ValueError as erro:
       print("Registo de A03 recusado:", erro)

   try:
       print(inventario.quantidade_de("A03"))
   except ValueError as erro:
       print("Consulta de A03 recusada:", erro)

   inventario.retirar("A01", 2)
   print("A01 depois de retirar 2:", inventario.quantidade_de("A01"))

   try:
       inventario.retirar("A01", 9)
   except ValueError as erro:
       print("Retirar 9 de A01 recusado:", erro)

   try:
       inventario.retirar("A07", 1)
   except ValueError as erro:
       print("Retirar de A07 recusado:", erro)

   print("A01 no fim:", inventario.quantidade_de("A01"))
   print("A02 no fim:", inventario.quantidade_de("A02"))
   ```

   Cada pedido que o traço deu como recusado fica no seu `try`, e três consultas mostram as quantidades.

4. Guarda e executa. O que deves ver:

   ```text
   Registo de A01 recusado: Já existe um artigo com o código A01.
   Registo de A03 recusado: A quantidade não pode ser negativa.
   Consulta de A03 recusada: Não existe nenhum artigo com o código A03.
   A01 depois de retirar 2: 4
   Retirar 9 de A01 recusado: A quantidade não pode ser negativa.
   Retirar de A07 recusado: Não existe nenhum artigo com o código A07.
   A01 no fim: 4
   A02 no fim: 2
   ```

   São as respostas do traço, pela mesma ordem, e só as recusas e as consultas escrevem uma linha. Quem recusa vê-se pela mensagem: o inventário escreve "Já existe..." e "Não existe...", e o setter do artigo escreve "A quantidade não pode ser negativa.". As duas últimas linhas batem certo com a última coluna do traço. Se aparecer outra coisa, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar). Se o programa chegar ao fim com uma linha diferente, vê [O programa não para, mas uma linha sai diferente](#o-programa-não-para-mas-uma-linha-sai-diferente).

### Paragem 3

O programa mostra as oito linhas do passo 4, e elas batem certo com o traço do passo 2. O ficheiro `inventario.py` completo, para conferires o teu:

```python
# inventario.py: as classes Artigo e Inventario, do laboratório do tema 04.

class Artigo:
    """Artigo do inventário: código, nome e uma quantidade sempre válida.

    É a classe final do guia 03, com as docstrings encurtadas.
    """

    def __init__(self, codigo, nome, quantidade):
        """Cria o artigo. A quantidade inicial passa pelo setter."""
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
        """Acrescenta unidades (inteiro, 1 ou mais); senão, lança ValueError."""
        if not isinstance(unidades, int):
            raise ValueError("As unidades a adicionar têm de ser um número inteiro.")
        if unidades <= 0:
            raise ValueError("As unidades a adicionar têm de ser 1 ou mais.")
        self.quantidade = self.quantidade + unidades

    def retirar(self, unidades):
        """Retira unidades (inteiro, 1 ou mais, até ao que existe); senão, lança ValueError."""
        if not isinstance(unidades, int):
            raise ValueError("As unidades a retirar têm de ser um número inteiro.")
        if unidades <= 0:
            raise ValueError("As unidades a retirar têm de ser 1 ou mais.")
        # A falta de unidades é recusada pelo setter: o resultado seria negativo.
        self.quantidade = self.quantidade - unidades


class Inventario:
    """Inventário que cria, guarda e controla os seus artigos."""

    def __init__(self):
        """Cria um inventário vazio, ainda sem artigos."""
        self._artigos = []

    def _procurar(self, codigo):
        """Método interno: devolve o artigo com este código.

        Falha: lança ValueError se não houver nenhum artigo com este código.
        """
        for artigo in self._artigos:
            if artigo.codigo == codigo:
                return artigo
        raise ValueError("Não existe nenhum artigo com o código " + codigo + ".")

    def registar(self, codigo, nome, quantidade):
        """Cria um artigo novo e guarda-o no inventário.

        Recebe: o código, o nome e a quantidade inicial do artigo.
        Devolve: nada (None).
        Falha: lança ValueError se já existir um artigo com este código, ou
        se a quantidade inicial for inválida (quem a recusa é o setter do
        artigo). Em qualquer falha, o inventário fica como estava.
        """
        for artigo in self._artigos:
            if artigo.codigo == codigo:
                raise ValueError("Já existe um artigo com o código " + codigo + ".")
        novo = Artigo(codigo, nome, quantidade)
        self._artigos.append(novo)

    def quantidade_de(self, codigo):
        """Devolve a quantidade do artigo com este código, sem a alterar.

        Falha: lança ValueError se não houver nenhum artigo com este código.
        """
        artigo = self._procurar(codigo)
        return artigo.quantidade

    def retirar(self, codigo, unidades):
        """Encaminha um pedido de retirada para o artigo com este código.

        Recebe: o código do artigo e as unidades a retirar.
        Devolve: nada (None).
        Falha: lança ValueError se não houver nenhum artigo com este código,
        ou se o próprio artigo recusar o pedido, pelas regras do seu método
        retirar. Em qualquer falha, nenhuma quantidade muda.
        """
        artigo = self._procurar(codigo)
        artigo.retirar(unidades)


inventario = Inventario()
inventario.registar("A01", "Caderno", 6)
inventario.registar("A02", "Pasta", 2)

try:
    inventario.registar("A01", "Cola", 3)
except ValueError as erro:
    print("Registo de A01 recusado:", erro)

try:
    inventario.registar("A03", "Caneta", -5)
except ValueError as erro:
    print("Registo de A03 recusado:", erro)

try:
    print(inventario.quantidade_de("A03"))
except ValueError as erro:
    print("Consulta de A03 recusada:", erro)

inventario.retirar("A01", 2)
print("A01 depois de retirar 2:", inventario.quantidade_de("A01"))

try:
    inventario.retirar("A01", 9)
except ValueError as erro:
    print("Retirar 9 de A01 recusado:", erro)

try:
    inventario.retirar("A07", 1)
except ValueError as erro:
    print("Retirar de A07 recusado:", erro)

print("A01 no fim:", inventario.quantidade_de("A01"))
print("A02 no fim:", inventario.quantidade_de("A02"))
```

Em cima estão as duas classes: o `Artigo` protege a quantidade de cada artigo, e o `Inventario` guarda os artigos na sua lista e encontra-os pelo código. Em baixo está o programa principal, que fala sempre com o inventário, pelos códigos, e nunca escreve `Artigo(...)`.

Pensa antes de continuares: na classe `Inventario`, onde está a verificação de que as unidades a retirar são 1 ou mais? A resposta: em sítio nenhum. Essa regra é do artigo e está no `retirar` da classe `Artigo`, e o inventário só encontra o artigo e lhe passa o pedido. Se a regra mudar, muda-se num só método.

## Fase 4: O caminho de uma recusa

Fazes outra vez o pedido de retirar 9 unidades ao A01, agora fora de um `try`, para a recusa subir até parar o programa. A mensagem de erro, o traceback, mostra então a cadeia de chamadas: os métodos parados, cada um à espera do que chamou, até ao que lançou a recusa. Rever: [O caminho de uma recusa](../04-composicao-modelacao.md#o-caminho-de-uma-recusa).

1. Logo a seguir à última linha do ficheiro, fora de qualquer `try`, acrescenta:

   ```python partial
   inventario.retirar("A01", 9)
   ```

   Antes de executares, prevê: por que métodos passa este pedido até ao erro, do primeiro ao último?

2. Guarda e executa. As oito linhas aparecem como antes, e depois o programa para com esta mensagem:

   ```text
   Traceback (most recent call last):
     File ".../tema-04/inventario.py", line 134, in <module>
       inventario.retirar("A01", 9)
       ~~~~~~~~~~~~~~~~~~^^^^^^^^^^
     File ".../tema-04/inventario.py", line 97, in retirar
       artigo.retirar(unidades)
       ~~~~~~~~~~~~~~^^^^^^^^^^
     File ".../tema-04/inventario.py", line 44, in retirar
       self.quantidade = self.quantidade - unidades
       ^^^^^^^^^^^^^^^
     File ".../tema-04/inventario.py", line 26, in quantidade
       raise ValueError("A quantidade não pode ser negativa.")
   ValueError: A quantidade não pode ser negativa.
   ```

   Com o ficheiro da paragem 3 e esta linha a mais, os números das linhas são estes. A resposta: do programa principal, o pedido desce ao `retirar` do inventário, que chama o `_procurar` e depois o `retirar` do artigo, e este chama o setter. A mensagem só tem quatro entradas, uma por cada linha `File`, e nenhuma é a do `_procurar`. Quando o setter recusou, o `_procurar` já tinha acabado, com o `return`. No traceback só entram o setter, onde a recusa nasceu, e os métodos que estavam parados à espera dele. Se aparecer outra coisa, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

3. Lê as quatro entradas, de cima para baixo. Em cada uma, a linha `File` acaba no nome do sítio onde o Python estava, e por baixo vem o código dessa linha:

   | Entrada | Acaba em | Código por baixo | Quem é |
   | --- | --- | --- | --- |
   | Primeira | `in <module>` | `inventario.retirar("A01", 9)` | O programa principal, onde a cadeia começa |
   | Segunda | `in retirar` | `artigo.retirar(unidades)` | O `retirar` do inventário, que passa o pedido ao artigo |
   | Terceira | `in retirar` | `self.quantidade = self.quantidade - unidades` | O `retirar` do artigo, que escreve na propriedade |
   | Quarta | `in quantidade` | `raise ValueError("A quantidade não pode ser negativa.")` | O setter, o segundo `def quantidade` da classe `Artigo` |

   Os dois `retirar` têm o mesmo nome. O código de baixo diz qual é qual: o do inventário passa o pedido ao artigo, e o do artigo escreve na propriedade. Para procurares a causa de um erro, lês ao contrário, de baixo para cima: a última entrada é onde a exceção nasceu.

4. Apaga a linha que acrescentaste nesta fase. Guarda e executa: aparecem só as oito linhas da paragem 3, sem nenhuma mensagem de erro.

### Paragem 4

O ficheiro voltou a ser o da paragem 3, e já leste no traceback o caminho que a recusa fez.

Pensa antes de continuares: porque é que o `retirar` do inventário não tem um `try` para apanhar a recusa do artigo? A resposta: porque não saberia o que fazer com ela. Não sabe se a recusa se mostra num terminal, numa página ou num ficheiro. O artigo decide se o pedido é válido, e quem fez o pedido decide o que fazer com a recusa: aqui, o programa principal mostra-a. Um `try` no inventário que não fizesse nada escondia a recusa, e o programa principal ficava convencido de que as unidades tinham saído.

## Se alguma coisa falhar

1. Guardaste o ficheiro antes de executar? Se a saída não mudou depois de uma alteração, é quase sempre isso: guarda e executa de novo.
2. O ficheiro que estás a executar é o `inventario.py` da pasta `tema-04`?
3. Executaste o ficheiro todo? Cada execução começa do zero, com um inventário novo, e faz os pedidos pela ordem do ficheiro.
4. Apagaste as linhas de teste da fase anterior? As fases 1, 2 e 4 acabam a apagá-las. Se te perderes nas fases 1 ou 2, recomeça o ficheiro com a classe `Artigo` de [Preparar o projeto](#preparar-o-projeto) e refaz as fases desde a 1. Nas fases 3 e 4, copia o ficheiro da [paragem 3](#paragem-3).
5. Apareceu uma mensagem de erro? Começa pela última linha, que diz o tipo de erro, e procura esse tipo nos títulos de baixo.

### Aparece `IndentationError`, `TabError` ou `SyntaxError`

É um erro de escrita, e o Python recusa o ficheiro antes de correr qualquer linha. A mensagem não começa por `Traceback`: abre com o ficheiro e com o número da linha onde o Python parou de ler. As mensagens mais comuns neste laboratório:

- `IndentationError: expected an indented block after 'if' statement on line`, seguido do número da linha do `if` (no Python 3.9, só `expected an indented block`): um `if`, um `for` ou um `def` ficou sem nenhuma linha indentada por baixo. No `_procurar`, acontece quando o `return artigo` fica alinhado com o `if`, em vez de quatro espaços mais à direita.
- `IndentationError: unexpected indent`: uma linha começa com mais espaços do que devia, como a segunda linha de teste com espaços à frente.
- `IndentationError: unindent does not match any outer indentation level`: uma linha voltou para trás até uma margem que nenhuma linha de cima usa. Acontece com um `def` com dois espaços, ou com um método encostado à margem. Nesse caso, a mensagem aponta o `def` do método seguinte, e o engano está no `def` de cima.
- `TabError: inconsistent use of tabs and spaces in indentation`: há uma tabulação onde deviam estar espaços. Troca-a por espaços.
- `SyntaxError: expected ':'` (no Python 3.9, só `invalid syntax`): uma linha `class`, `def`, `for`, `if`, `try` ou `except` ficou sem os dois pontos no fim.

Na classe `Inventario`, os `def` levam quatro espaços e as linhas de dentro de um método levam oito. Dentro do `for`, o `if` leva doze, e o `return` e o `raise` que estão dentro do `if` levam dezasseis. No programa principal, as linhas de dentro de cada `try` e de cada `except` levam quatro. Põe lado a lado a linha que a mensagem indica, e a de cima, e as mesmas linhas no laboratório.

### Aparece `NameError: name 'Inventario' is not defined`, ou não aparece nada

As linhas que vêm depois das classes ficaram com espaços à frente, como as do construtor. Pode acontecer quando carregas em Enter no fim do construtor e o editor mantém o recuo. Com quatro espaços, as linhas ficam dentro da classe `Inventario`, que o Python ainda não acabou de ler, e a linha `File` de baixo acaba em `in Inventario`. A mensagem mostra também a linha `class Inventario:`, e no Python 3.14 uma linha como `...<8 lines>...`. Com oito espaços, ficam dentro do construtor e nunca correm, e não aparece nada, nem o `[]` da fase 1. Encosta à margem todas as linhas que vêm depois das classes.

### Aparece `TypeError: Inventario.__init__() takes 0 positional arguments but 1 was given`

Quer dizer que o construtor não aceita nenhum valor, mas recebeu um. No Python 3.9, a mensagem diz só `__init__()`, sem `Inventario.`. Falta o `self` entre os parênteses do `def __init__`: o Python entrega sempre ao construtor o inventário novo, e o `def` não tem onde o receber. Compara a linha com a do passo 1 da fase 1, `def __init__(self):`.

### Aparece `NameError: name 'Artigo' is not defined`

`NameError` é um erro de nome: o Python não conhece o nome `Artigo`. A classe falta no ficheiro, ou ficou com outro nome, como `artigo`, e nesse caso as versões recentes acrescentam `Did you mean: 'artigo'?`. Copia a classe de [Preparar o projeto](#preparar-o-projeto), com o `A` maiúsculo.

### Aparece `NameError: name '_procurar' is not defined`

Num dos métodos da fase 3, a linha ficou `artigo = _procurar(codigo)`, sem o `self.` à frente, e o Python procura uma função solta com esse nome. As versões recentes acrescentam `Did you mean: 'self._procurar'?` ("querias dizer `self._procurar`?"). Escreve `artigo = self._procurar(codigo)`.

### Aparece `AttributeError: 'Inventario' object has no attribute '_artigos'`

`AttributeError` é um erro de atributo: o inventário não tem nenhum atributo `_artigos`. O nome da lista está escrito de duas maneiras, como `_artigo` no construtor e `_artigos` noutro sítio. As versões recentes sugerem o nome que existe, como `Did you mean: '_artigo'?`, e o mesmo engano ao contrário dá a mensagem com `'_artigo'`. Escolhe um dos dois nomes, de preferência `_artigos`, e corrige as linhas que têm o outro. Se a mensagem não traz sugestão e não há nenhum `_artigo` no ficheiro, olha para o construtor. A linha do `def` tem de ser `def __init__(self):`, com dois sublinhados de cada lado do `init`, e a de dentro `self._artigos = []`, com o `self.`.

### Aparece `AttributeError: 'Inventario' object has no attribute 'registar'`, ou com `'retirar'`

O `def` desse método está encostado à margem. Para o Python, é uma função solta, fora da classe, e o inventário não tem esse método. No `retirar`, as versões recentes sugerem `Did you mean: 'registar'?`, que aqui não ajuda: o método existe, mas fora da classe. Afasta o `def` quatro espaços da margem e as linhas de dentro oito, como nos outros métodos.

### Aparece `TypeError: can only concatenate str (not "int") to str`

Em português: só se junta texto a texto, e não um número inteiro (`str` é o texto e `int` o inteiro). Num pedido, o código ficou escrito como número, como `quantidade_de(7)`. Nenhum artigo tem esse código, e o `raise` de `_procurar` não consegue juntar o 7 ao texto da mensagem. Como é um `TypeError`, o `except ValueError` deixa-o passar. Põe o código entre aspas, como `"A07"`.

### Aparece `ValueError: Não existe nenhum artigo com o código A02.`, com a pasta registada

Na fase 2, o programa para no `print` do `_procurar("A02")`, logo a seguir à linha `2`. Na fase 3, mostra as linhas até `A01 no fim: 4` e para na última. O `raise` de `_procurar` ficou dentro do ciclo, alinhado com o `if`. Assim, se o primeiro artigo não for o procurado, o método recusa logo na primeira volta, sem ver os outros. Alinha o `raise` com o `for`, depois do ciclo, como no ficheiro da [paragem 3](#paragem-3).

### O programa não para, mas uma linha sai diferente

Compara a saída, linha a linha, com a do passo em que estás, e fica-te pela primeira linha diferente: uma diferença no início costuma arrastar as seguintes. Vê que pedido a escreveu e que método responde a esse pedido. Depois compara esse método, linha a linha, com o do ficheiro da [paragem 3](#paragem-3), e confirma também o texto do `print`.

## Desafios

Para os desafios, cria na pasta `tema-04` um ficheiro novo, `desafios.py`, com uma cópia de todo o `inventario.py` da paragem 3. Faz os quatro desafios nesse ficheiro, um a seguir ao outro, com as respostas num comentário no fim dele. Assim, o `inventario.py` fica como na paragem 3.

1. Adicionar unidades a um artigo. Escreve, dentro da classe `Inventario`, o método `adicionar(codigo, unidades)`, com este contrato. Recebe o código de um artigo e as unidades a adicionar. Não devolve nada. Falha, com `ValueError`, se não houver nenhum artigo com esse código, ou se o próprio artigo recusar o pedido pelas regras do seu método `adicionar`. Em qualquer falha, nenhuma quantidade muda. Escreve-lhe uma docstring.

   Responde, no comentário do fim do `desafios.py`: que regras sobre as unidades vai verificar o método do inventário, e quais vai deixar ao artigo?

   Os testes escolhes tu. Escreve três pedidos de adição, cada um no seu `try`, depois das linhas que já estão no fim do ficheiro. Um tem de ser aceite, outro recusado pelo inventário, e o terceiro recusado pelo artigo. Para cada pedido, prevê se vai ser aceite ou recusado, quem recusa, com que mensagem e como ficam as quantidades, e confirma ao executar. No fim, mostra com `quantidade_de` a quantidade de cada artigo existente que usaste nos testes.

   Pista: para escolheres os testes, pensa em que regras verifica cada objeto e por que ordem o pedido passa por eles.

2. O total de unidades do inventário. Escreve o método `total_unidades()`, que devolve a soma das quantidades de todos os artigos do inventário. Não recebe nada além do `self`, não muda nenhuma quantidade e não falha.

   Responde, no comentário do fim do ficheiro, a duas perguntas. Porque é que este método pertence ao `Inventario`, e não ao `Artigo`? E o que deve devolver um inventário que ainda não tem nenhum artigo?

   Para somar, usa um acumulador: uma variável preparada antes de um ciclo `for` sobre a lista interna, que em cada volta junta a quantidade de um artigo. Testa com dois casos. Mostra o total do inventário do teu programa, e depois cria um inventário novo, vazio, e mostra o total dele. O total certo do primeiro calcula-se de cabeça, a partir das quantidades que os artigos têm nesse momento.

   Pista: pensa bem no valor com que o acumulador deve começar, e em que sítio do método ficam a linha que o prepara e o `return`. Rever: [O acumulador do método `titulos`](../04-composicao-modelacao.md#o-acumulador-do-método-titulos).

3. Os artigos esgotados. Escreve o método `esgotados()`, que devolve uma lista com os códigos dos artigos que têm quantidade 0. Se nenhum artigo estiver esgotado, devolve uma lista vazia. Testa-o duas vezes: uma com o inventário tal como está, e outra depois de retirares todas as unidades de um dos artigos. Antes de cada teste, prevê a lista que vai aparecer.

4. A descrição com as operações novas. Em [O inventário descrito por palavras](../04-composicao-modelacao.md#o-inventário-descrito-por-palavras), o guia descreve a classe `Inventario` em três frases, e a relação entre as duas classes noutras quatro. No comentário do fim do `desafios.py`, escreve de novo a descrição da classe, agora com os métodos que acrescentaste nos desafios. Responde também numa frase: a descrição da relação entre as duas classes mudou com as operações novas? Porquê?

## Antes de terminares

- [ ] O `inventario.py` da pasta `tema-04` executa e mostra as oito linhas da paragem 3.
- [ ] Apagaste as linhas de teste das fases 1, 2 e 4: o `inventario.py` está igual ao da paragem 3.
- [ ] Guardaste o `inventario.py` e, se fizeste os desafios, o `desafios.py`, com as respostas no fim, e entregaste-os como o professor indicar.
- [ ] Sabes dizer quem recusa cada um dos pedidos da fase 3, e porquê.
- [ ] Sabes dizer porque é que o `_procurar` não aparece no traceback da fase 4.
- [ ] Consegues explicar, por palavras tuas, porque é que é o inventário, e não o artigo, que garante que não há dois artigos com o mesmo código.

![Rodapé](../../imagens/rodape.png)

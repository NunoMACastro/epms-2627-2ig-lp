![Cabeçalho](../../imagens/cabecalho.png)

# Laboratório: Encapsulamento e contratos

## O que vais construir

Começas pela classe `Artigo` do tema 02, que aceita -3 cadernos sem se queixar, e acabas com uma classe que recusa cada pedido impossível sem mexer na quantidade. Pelo caminho, provocas de propósito os erros que mais vais encontrar e lês a mensagem de cada um.

No fim, o programa `artigo.py` mostra:

```text
Depois de retirar 2: 4
Retirar 9 recusado: A quantidade não pode ser negativa.
Retirar 0 recusado: As unidades a retirar têm de ser 1 ou mais.
Retirar -3 recusado: As unidades a retirar têm de ser 1 ou mais.
Caderno no fim: 4
Pasta no fim: 2
Caderno depois de retirar 4: 0
```

1. [Fase 1: Nada impede uma quantidade impossível](#fase-1-nada-impede-uma-quantidade-impossível)
2. [Fase 2: Um set que verifica, mas não obriga](#fase-2-um-set-que-verifica-mas-não-obriga)
3. [Fase 3: Recusar a sério, com `raise`](#fase-3-recusar-a-sério-com-raise)
4. [Fase 4: Tratar a recusa com `try` e `except`](#fase-4-tratar-a-recusa-com-try-e-except)
5. [Fase 5: A propriedade `quantidade`](#fase-5-a-propriedade-quantidade)
6. [Fase 6: O construtor também passa pelo setter](#fase-6-o-construtor-também-passa-pelo-setter)
7. [Fase 7: Operações com contrato](#fase-7-operações-com-contrato)

## O que precisas

- O Python 3.10 ou mais recente. No terminal, `python3 --version` mostra a versão (no Windows, `py --version`), por exemplo `Python 3.12.4`. Nas versões mais antigas, o laboratório corre na mesma, mas algumas mensagens de erro mudam, e o laboratório diz onde.
- O editor das aulas, o dos laboratórios dos temas 01 e 02.

Começas numa pasta vazia: a classe do tema 02, de onde partes, vem escrita na fase 1.

## Preparar o projeto

1. Na pasta onde guardas os trabalhos de LP, cria uma pasta nova, `tema-03`. Assim não executas por engano o ficheiro de outro tema.

2. Dentro de `tema-03`, cria no editor o ficheiro `artigo.py`, sem espaços nem acentos no nome. Serve para as sete fases, e o conteúdo vai mudando de uma fase para a outra.

## Fase 1: Nada impede uma quantidade impossível

Escreves a classe do tema 02 e fazes-lhe três alterações que não deviam ser possíveis. Vês o que acontece a um artigo num estado inválido, com valores que não cumprem as regras do inventário. Rever: [Nada impede uma quantidade impossível](../03-encapsulamento-contratos.md#nada-impede-uma-quantidade-impossível) e [As regras que devem continuar verdadeiras](../03-encapsulamento-contratos.md#as-regras-que-devem-continuar-verdadeiras).

1. Começa pela classe do tema 02, com o construtor e um `retirar` que ainda não verifica o pedido. Escreve no `artigo.py` este bloco, em vez de copiares o `artigos.py` do tema 02, que tem a docstring do `retirar` mais comprida e deixava as linhas com outros números:

   ```python
   # artigo.py: a classe do tema 02 e três alterações impossíveis, do laboratório do tema 03.

   class Artigo:
       """Descreve um artigo do inventário: um material com código, nome e quantidade."""

       def __init__(self, codigo, nome, quantidade):
           """Prepara um artigo acabado de criar, guardando os três dados recebidos."""
           self.codigo = codigo
           self.nome = nome
           self.quantidade = quantidade

       def retirar(self, unidades):
           """Retira unidades a este artigo e devolve a quantidade que fica (sem verificar)."""
           self.quantidade = self.quantidade - unidades
           return self.quantidade
   ```

   Guarda e executa. O que deves ver: nada, nem uma mensagem de erro, porque o programa ainda não cria nenhum artigo. Se aparecer outra coisa, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

2. Por baixo da classe, depois de duas linhas em branco, escreve o caderno e as três alterações impossíveis:

   ```python partial
   caderno = Artigo("A01", "Caderno", 6)

   caderno.retirar(9)
   print("Depois de retirar 9:", caderno.quantidade)

   caderno.quantidade = 2.5
   print("Depois de escrever 2.5:", caderno.quantidade)

   caderno.quantidade = "muitos"
   print("Depois de escrever muitos:", caderno.quantidade)
   ```

   A primeira alteração passa pelo `retirar`, e as outras duas escrevem diretamente no atributo, sem método nenhum.

   Antes de executares, prevê: o Python vai aceitar as três? Depois guarda e executa. O que deves ver:

   ```text
   Depois de retirar 9: -3
   Depois de escrever 2.5: 2.5
   Depois de escrever muitos: muitos
   ```

   A resposta: aceitou as três, sem uma única queixa. Nem -3, nem 2.5, nem "muitos" são uma quantidade de material. O caderno ficou num estado inválido por dois caminhos: um método que não verifica e a escrita direta no atributo.

3. Vê agora o que este estado inválido provoca. Na linha a seguir ao último `print`, acrescenta mais um pedido:

   ```python partial
   caderno.retirar(1)
   ```

   Guarda e executa. As três linhas aparecem, e depois o programa para com uma mensagem destas:

   ```text
   Traceback (most recent call last):
     File ".../tema-03/artigo.py", line 28, in <module>
       caderno.retirar(1)
       ~~~~~~~~~~~~~~~^^^
     File ".../tema-03/artigo.py", line 14, in retirar
       self.quantidade = self.quantidade - unidades
                         ~~~~~~~~~~~~~~~~^~~~~~~~~~
   TypeError: unsupported operand type(s) for -: 'str' and 'int'
   ```

   No lugar dos três pontos está a pasta do teu computador. As linhas com `~` e `^` apontam onde a conta falhou, e só aparecem a partir do Python 3.11. A última linha diz que houve um `TypeError`, um erro de tipo: o Python não sabe fazer a conta `-` entre um texto (`str`) e um número inteiro (`int`).

4. Encontra a causa. A mensagem tem duas linhas `File`, cada uma com o número de uma linha e, por baixo, o código dela. Com o ficheiro dos passos 1 a 3, a de baixo aponta a linha 14, dentro do `retirar`, onde a conta falhou. A de cima aponta a linha 28, `caderno.retirar(1)`, no programa principal, isto é, nas linhas depois da classe, a que o Python chama `<module>`. A causa está mais acima, na linha 26, `caderno.quantidade = "muitos"`, que guardou o texto. O erro vê-se onde o valor é usado, longe do sítio onde o valor errado entrou.

### Paragem 1

O programa mostra as três linhas e para com o `TypeError` da linha 28.

Pensa antes de continuares: o -3 e o `TypeError` são dois erros diferentes. Qual deles avisou alguém? A resposta: só o `TypeError`, que parou o programa e mostrou uma mensagem: é um erro de execução. O -3 é um erro de lógica: o programa segue em frente com um valor errado, e ninguém é avisado.

## Fase 2: Um set que verifica, mas não obriga

Passas a ler a quantidade com um método get (do inglês, obter) e a mudá-la com um método set (definir), que verifica o valor antes de o guardar. Vês o que o set resolve e os dois problemas que deixa por resolver. Rever: [Um set que verifica, mas não obriga](../03-encapsulamento-contratos.md#um-set-que-verifica-mas-não-obriga).

1. Começa uma versão nova do ficheiro. Apaga tudo o que está no `artigo.py` e escreve o comentário do topo e a classe com o get e o set:

   ```python
   # artigo.py: os métodos get e set, com um set que recusa com print.

   class Artigo:
       """Artigo do inventário, com métodos get e set para a quantidade."""

       def __init__(self, codigo, nome, quantidade):
           """Guarda os dados iniciais do artigo."""
           self.codigo = codigo
           self.nome = nome
           self.quantidade = quantidade

       def get_quantidade(self):
           """Devolve a quantidade atual, sem a alterar."""
           return self.quantidade

       def set_quantidade(self, valor):
           """Muda a quantidade, mas só se o valor for um inteiro não negativo."""
           if isinstance(valor, int) and valor >= 0:
               self.quantidade = valor
           else:
               print("Valor recusado:", valor)
   ```

   A condição do set só deixa passar um inteiro maior ou igual a zero. A função `isinstance` (do inglês, "é instância de") pergunta se o valor é um `int` e responde `True` ou `False`.

2. Deixa duas linhas em branco a seguir à classe e acrescenta duas tentativas de guardar -3, uma com o set e outra diretamente no atributo:

   ```python partial
   caderno = Artigo("A01", "Caderno", 6)

   caderno.set_quantidade(-3)
   print("Depois do set com -3:", caderno.get_quantidade())

   caderno.quantidade = -3
   print("Depois da escrita direta:", caderno.get_quantidade())
   ```

   Antes de executares, prevê: depois das duas tentativas, com que quantidade fica o caderno? Depois guarda e executa. O que deves ver:

   ```text
   Valor recusado: -3
   Depois do set com -3: 6
   Depois da escrita direta: -3
   ```

   A resposta: com -3. O pedido ao set foi recusado e deixou o 6, mas a escrita direta guardou o -3 sem verificação nenhuma. Este é o primeiro problema: nada obriga quem usa a classe a passar pelo set.

3. Acrescenta no fim estas duas linhas, que guardam o que o set devolve a quem lhe faz o pedido:

   ```python partial
   resposta = caderno.set_quantidade(-1)
   print("O set respondeu:", resposta)
   ```

   Guarda e executa. Depois das três linhas de antes, aparecem estas:

   ```text
   Valor recusado: -1
   O set respondeu: None
   ```

   `None` (em inglês, nenhum) quer dizer "nada" em Python. Um método sem `return`, como o set, devolve sempre `None`.

4. Pensa: com o que o set devolve, o código que o chamou consegue saber que o pedido foi recusado? A resposta: não. O set devolve `None` quer aceite quer recuse, e a frase "Valor recusado" é para quem olha para o ecrã, e não para o programa. É o segundo problema: a recusa não chega a quem fez o pedido.

### Paragem 2

O programa mostra as cinco linhas, de `Valor recusado: -3` a `O set respondeu: None`.

Pensa antes de continuares: o primeiro problema desaparecia se toda a gente se lembrasse de usar o set. Porque é que não chega confiar nisso? A resposta: num programa grande, a quantidade muda em muitos sítios, e basta um deles esquecer-se do set para o artigo ficar com -3. Quem tem de proteger a quantidade é o próprio artigo, e não quem o usa.

## Fase 3: Recusar a sério, com `raise`

Respondes aos dois problemas do set: a quantidade passa para `_quantidade`, com um sublinhado que avisa que é interna da classe, e o set recusa com `raise`. O `raise` lança uma exceção, um sinal de erro que para o método e volta ao código que fez o pedido. Rever: [O sublinhado: um atributo privado por convenção](../03-encapsulamento-contratos.md#o-sublinhado-um-atributo-privado-por-convenção) e [Recusar a sério, com `raise`](../03-encapsulamento-contratos.md#recusar-a-sério-com-raise).

1. Começa outra vez o ficheiro. Apaga tudo o que está no `artigo.py` e escreve esta versão do comentário do topo e da classe, com `_quantidade` no construtor, no get e no set:

   ```python
   # artigo.py: o atributo _quantidade e um set que recusa com raise.

   class Artigo:
       """Artigo do inventário; a quantidade fica num atributo interno, _quantidade."""

       def __init__(self, codigo, nome, quantidade):
           """Guarda os dados iniciais do artigo."""
           self.codigo = codigo
           self.nome = nome
           self._quantidade = quantidade

       def get_quantidade(self):
           """Devolve a quantidade atual, sem a alterar."""
           return self._quantidade

       def set_quantidade(self, valor):
           """Muda a quantidade; se o valor for inválido, lança ValueError e não muda nada."""
           if not isinstance(valor, int):
               raise ValueError("A quantidade tem de ser um número inteiro.")
           if valor < 0:
               raise ValueError("A quantidade não pode ser negativa.")
           self._quantidade = valor
   ```

   O `not` inverte a resposta do `isinstance`, e por isso a primeira condição lê-se "se o valor não for inteiro".

2. A seguir à classe, com duas linhas em branco pelo meio, escreve um pedido que o set aceita e outro que recusa:

   ```python partial
   caderno = Artigo("A01", "Caderno", 6)
   caderno.set_quantidade(4)
   print("Quantidade:", caderno.get_quantidade())
   caderno.set_quantidade(-3)
   print("Esta linha já não é executada.")
   ```

   Guarda e executa. O que deves ver:

   ```text
   Quantidade: 4
   Traceback (most recent call last):
     File ".../tema-03/artigo.py", line 28, in <module>
       caderno.set_quantidade(-3)
       ~~~~~~~~~~~~~~~~~~~~~~^^^^
     File ".../tema-03/artigo.py", line 21, in set_quantidade
       raise ValueError("A quantidade não pode ser negativa.")
   ValueError: A quantidade não pode ser negativa.
   ```

   O pedido de 4 foi aceite, e o de -3 foi recusado a sério: o programa parou. Se aparecer outra coisa, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

3. Lê a mensagem de baixo para cima. A última linha dá o tipo, `ValueError`, que quer dizer erro de valor, e a mensagem do teu `raise`. A linha `File` logo acima diz onde a exceção nasceu: na linha 21, a do `raise`, dentro de `set_quantidade`, se escreveste o ficheiro como nos passos 1 e 2. A de cima diz quem fez o pedido: a linha 28, no programa principal. O último `print` não chegou a correr, porque ninguém tratou a exceção.

4. Experimenta agora a ordem das verificações. No `set_quantidade`, troca a ordem dos dois `if`, cada um com o seu `raise`, para a verificação `valor < 0` vir primeiro. Os dois `if` ficam assim:

   ```python partial
           if valor < 0:
               raise ValueError("A quantidade não pode ser negativa.")
           if not isinstance(valor, int):
               raise ValueError("A quantidade tem de ser um número inteiro.")
   ```

   Depois troca as linhas depois da classe por estas duas:

   ```python partial
   caderno = Artigo("A01", "Caderno", 6)
   caderno.set_quantidade("muitos")
   ```

   Antes de executares, prevê: com `"muitos"`, qual das duas mensagens do set aparece? Depois guarda e executa. A última linha da mensagem é esta:

   ```text
   TypeError: '<' not supported between instances of 'str' and 'int'
   ```

   A resposta: nenhuma. O Python tentou fazer `"muitos" < 0` antes de saber se o valor era um número, e o `<` não compara um texto (`str`) com um inteiro (`int`). A mensagem do set, "A quantidade tem de ser um número inteiro.", dizia a quem usa a classe o que está errado no pedido. Por isso o tipo verifica-se primeiro.

5. Repõe os dois `if` pela ordem do passo 1 e as linhas do fim como no passo 2. Guarda e executa: volta a aparecer a mensagem do passo 2.

### Paragem 3

O ficheiro está outra vez como no fim do passo 2, e o programa mostra `Quantidade: 4` e para com `ValueError: A quantidade não pode ser negativa.`.

Pensa antes de continuares: se escrevesses, logo a seguir à linha que cria o caderno, estas duas linhas, o Python aceitava a primeira?

```python partial
caderno._quantidade = -3
print("Depois da escrita em _quantidade:", caderno.get_quantidade())
```

A resposta: aceitava, e a segunda linha mostrava `Depois da escrita em _quantidade: -3`. O sublinhado é só um acordo entre programadores, que o Python não faz cumprir. Mas uma linha destas, fora da classe, salta à vista: quem a lê sabe que alguém passou ao lado da classe de propósito. Se as experimentares, apaga-as no fim.

## Fase 4: Tratar a recusa com `try` e `except`

Pões o pedido dentro de um `try` (em inglês, tenta), com um `except` (exceto) que apanha o `ValueError`, para o programa continuar depois da recusa. Quando uma linha do `try` lança a exceção, o Python salta as linhas que faltam no `try` e corre o `except`. Rever: [Tratar a recusa com `try` e `except`](../03-encapsulamento-contratos.md#tratar-a-recusa-com-try-e-except).

1. Em `artigo.py`, a classe fica igual. Troca só as linhas que vêm a seguir a ela por estas:

   ```python partial
   caderno = Artigo("A01", "Caderno", 6)

   try:
       caderno.set_quantidade(-3)
       print("Esta linha só é executada se o set aceitar o valor.")
   except ValueError as erro:
       print("Pedido recusado:", erro)

   print("Quantidade:", caderno.get_quantidade())
   ```

   O `as` quer dizer "como". Na linha do `except`, dá o nome `erro` à exceção apanhada, para o `print` de baixo mostrar a mensagem que o set lhe pôs.

2. Guarda e executa. O que deves ver:

   ```text
   Pedido recusado: A quantidade não pode ser negativa.
   Quantidade: 6
   ```

   Se aparecer outra coisa, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar). O set recusou o -3, o `except` apanhou a recusa e o programa chegou ao fim. A frase "Esta linha só é executada..." não apareceu, porque o Python saiu do `try` na linha do pedido. E a quantidade continua 6: para saberes se uma recusa funcionou, confirma o estado, e não só a mensagem.

3. Na linha `except ValueError as erro:`, troca `ValueError` por `TypeError`. Antes de executares, prevê: o programa continua depois da recusa? Depois guarda e executa.

   A resposta: não. O programa para com uma mensagem que acaba em `ValueError: A quantidade não pode ser negativa.`, como se não houvesse `try`. Um `except` só apanha o tipo de exceção que diz, e um `except TypeError` deixa passar um `ValueError`.

4. Volta a pôr `ValueError` no `except`. Guarda e executa: o programa volta a continuar depois da recusa.

5. Vê agora o caminho sem recusa. No pedido do `try`, troca o -3 por 4. Guarda e executa. O que deves ver:

   ```text
   Esta linha só é executada se o set aceitar o valor.
   Quantidade: 4
   ```

   Sem exceção, o Python corre o `try` até ao fim e salta o `except`. Volta a pôr o -3, guarda e executa: aparecem outra vez as duas linhas do passo 2.

### Paragem 4

O programa mostra `Pedido recusado: A quantidade não pode ser negativa.` e `Quantidade: 6`. Compara o teu `artigo.py` com este ficheiro completo:

```python
# artigo.py: o atributo _quantidade e um set que recusa com raise.

class Artigo:
    """Artigo do inventário; a quantidade fica num atributo interno, _quantidade."""

    def __init__(self, codigo, nome, quantidade):
        """Guarda os dados iniciais do artigo."""
        self.codigo = codigo
        self.nome = nome
        self._quantidade = quantidade

    def get_quantidade(self):
        """Devolve a quantidade atual, sem a alterar."""
        return self._quantidade

    def set_quantidade(self, valor):
        """Muda a quantidade; se o valor for inválido, lança ValueError e não muda nada."""
        if not isinstance(valor, int):
            raise ValueError("A quantidade tem de ser um número inteiro.")
        if valor < 0:
            raise ValueError("A quantidade não pode ser negativa.")
        self._quantidade = valor


caderno = Artigo("A01", "Caderno", 6)

try:
    caderno.set_quantidade(-3)
    print("Esta linha só é executada se o set aceitar o valor.")
except ValueError as erro:
    print("Pedido recusado:", erro)

print("Quantidade:", caderno.get_quantidade())
```

Em cima está a classe da fase 3, com o set que recusa com `raise`. Por baixo, o pedido de -3 está dentro do `try`, e a última linha, fora dos dois blocos, mostra a quantidade que ficou.

Pensa antes de continuares: o set lança a exceção e não escreve nada no ecrã. Quem decide mostrar "Pedido recusado"? A resposta: o código que usa a classe, no `except`. A classe decide se o valor serve, e quem a usa decide o que fazer com a recusa. Hoje a classe corre num terminal, mas pode vir a ser usada numa página web, onde um `print` nem se via.

## Fase 5: A propriedade `quantidade`

Trocas o get e o set por uma propriedade, que se lê e escreve como um atributo, `caderno.quantidade`, mas passa sempre por um método. A leitura corre o getter, a escrita corre o setter, e o valor fica guardado em `_quantidade`. Rever: [A propriedade `quantidade`](../03-encapsulamento-contratos.md#a-propriedade-quantidade).

1. Apaga outra vez o conteúdo do `artigo.py` e escreve o comentário do topo e a classe com a propriedade. O get e o set dão lugar a dois métodos com o mesmo nome, `quantidade`:

   ```python
   # artigo.py: a propriedade quantidade, com getter e setter.

   class Artigo:
       """Artigo do inventário: código, nome e uma quantidade sempre válida.

       A quantidade é uma propriedade. Lê-se e escreve-se como um atributo
       normal (artigo.quantidade), mas cada escrita passa pelo setter, que
       recusa valores inválidos com ValueError.
       """

       def __init__(self, codigo, nome, quantidade):
           """Cria o artigo. A quantidade inicial passa pelo setter, como qualquer outra."""
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
   ```

   O `@property` e o `@quantidade.setter` são decoradores: dizem ao Python que o primeiro é o getter e o segundo é o setter da mesma propriedade.

2. Por baixo da classe, depois de duas linhas em branco, acrescenta estas linhas, que leem e escrevem a quantidade como num atributo normal:

   ```python partial
   caderno = Artigo("A01", "Caderno", 6)
   print("Início:", caderno.quantidade)

   caderno.quantidade = 10
   print("Depois de acertar para 10:", caderno.quantidade)

   try:
       caderno.quantidade = 2.5
   except ValueError as erro:
       print("Recusado:", erro)
   print("Depois da tentativa com 2.5:", caderno.quantidade)

   try:
       caneta = Artigo("A03", "Caneta", -5)
   except ValueError as erro:
       print("Artigo não criado:", erro)
   ```

   Antes de executares, prevê: das duas tentativas que estão dentro de um `try`, quais são recusadas? Depois guarda e executa. O que deves ver:

   ```text
   Início: 6
   Depois de acertar para 10: 10
   Recusado: A quantidade tem de ser um número inteiro.
   Depois da tentativa com 2.5: 10
   Artigo não criado: A quantidade não pode ser negativa.
   ```

   A resposta: as duas. A escrita `caderno.quantidade = 2.5`, a mesma escrita direta que na fase 2 passava ao lado do set, passa agora pelo setter, que a recusou, e a quantidade ficou 10. A caneta com -5 também foi recusada e nem chegou a ser criada, apesar de o programa não escrever na quantidade dela. Se aparecer outra coisa, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

3. Provoca um erro de propósito, para veres porque é que o valor fica num nome diferente do da propriedade. Na última linha do setter, troca `self._quantidade = valor` por `self.quantidade = valor`, sem o sublinhado. Guarda e executa. O programa para logo ao criar o caderno, com uma mensagem comprida. A linha `File` da linha 29, com `self.quantidade = valor` por baixo, aparece três vezes, e a mensagem acaba assim:

   ```text
     [Previous line repeated 995 more times]
   RecursionError: maximum recursion depth exceeded
   ```

   Em português: a linha anterior repetiu-se mais 995 vezes, e passou-se o número máximo de chamadas umas dentro das outras. `RecursionError` quer dizer erro de recursão, e recursão quer dizer uma função chamar-se a si própria. Isto acontece porque escrever em `self.quantidade` é correr o setter: cada execução chega à última linha e corre outra vez o setter, até o Python desistir. Noutras versões, o número é outro, antes da última linha pode aparecer mais uma linha `File`, e a última linha pode ter mais umas palavras, como `while calling a Python object`.

4. Volta a pôr o sublinhado, `self._quantidade = valor`. Guarda e executa: aparecem de novo as cinco linhas do passo 2.

### Paragem 5

O programa mostra as cinco linhas, de `Início: 6` a `Artigo não criado: A quantidade não pode ser negativa.`. O ficheiro tem a classe do passo 1 e, por baixo, as linhas do passo 2.

Pensa antes de continuares: na linha `print("Início:", caderno.quantidade)`, que método corre? E na linha `caderno.quantidade = 10`? A resposta: na primeira, o getter, porque o programa lê a propriedade. Na segunda, o setter, porque o programa escreve nela, e o 10 chega ao setter no parâmetro `valor`.

## Fase 6: O construtor também passa pelo setter

Na fase 5, a caneta com -5 não chegou a ser criada, porque o construtor escreve em `self.quantidade`, sem sublinhado, e por isso passa pelo setter. Agora vês o que acontece quando o construtor salta o setter. Rever: [O construtor também passa pelo setter](../03-encapsulamento-contratos.md#o-construtor-também-passa-pelo-setter).

1. No construtor, troca `self.quantidade = quantidade` por `self._quantidade = quantidade`, com sublinhado. Guarda e executa. O que deves ver:

   ```text
   Início: 6
   Depois de acertar para 10: 10
   Recusado: A quantidade tem de ser um número inteiro.
   Depois da tentativa com 2.5: 10
   ```

   A linha "Artigo não criado: ..." desapareceu. Com o sublinhado, o construtor escreve diretamente no atributo interno, e a caneta nasceu com -5 sem que nada a verificasse. A regra da quantidade tem de valer sempre, e "sempre" começa no momento em que o artigo nasce.

2. Para veres a caneta, acrescenta no fim do ficheiro, fora de qualquer `try`, esta linha:

   ```python partial
   print("A caneta nasceu com:", caneta.quantidade)
   ```

   Guarda e executa. A última linha passa a ser `A caneta nasceu com: -5`, e a terceira, `Recusado: ...`, continua lá, porque as escritas feitas depois de o artigo existir passam pelo setter. Por isso, um teste que só experimente escritas depois da criação não apanha este erro: é preciso experimentar também criar um artigo com um valor inválido.

3. Repõe o construtor como estava, com `self.quantidade = quantidade`, mas deixa ficar a linha do passo 2. Antes de executares, prevê: o que mostra agora essa linha?

4. Guarda e executa. As cinco linhas da fase 5 aparecem, e depois o programa para com uma mensagem que acaba assim:

   ```text
   NameError: name 'caneta' is not defined
   ```

   A resposta: nada, porque o programa para nessa linha. `NameError` quer dizer erro de nome: o nome `caneta` não está definido. O setter lançou `ValueError` dentro do construtor, e a exceção interrompeu também a atribuição ao nome `caneta`, que nunca chegou a acontecer. Assim, o resto do programa não pode usar um artigo inválido.

5. Apaga a linha do passo 2. Guarda e executa: vês só as cinco linhas da fase 5.

### Paragem 6

O ficheiro voltou a ser o da paragem 5, e o programa mostra as mesmas cinco linhas.

Pensa antes de continuares: em nenhuma linha do construtor aparece `_quantidade`. Quem cria então esse atributo em cada artigo? A resposta: o setter, quando o construtor escreve a quantidade inicial e o valor é válido. Se o primeiro valor for inválido, o setter recusa-o antes de guardar, e o atributo `_quantidade` nem chega a existir.

## Fase 7: Operações com contrato

Acrescentas à classe os métodos `adicionar` e `retirar`, cada um com o contrato na docstring: o que recebe, o que devolve, quando falha e o que acontece à quantidade. Cada método verifica primeiro o pedido e só depois escreve na propriedade, para a escrita passar pelo setter. Rever: [Operações com contrato](../03-encapsulamento-contratos.md#operações-com-contrato) e [Exemplo guiado: construir o método retirar](../03-encapsulamento-contratos.md#exemplo-guiado-construir-o-método-retirar).

1. Em `artigo.py`, acrescenta à classe o método `adicionar`, a seguir ao setter, com uma linha em branco antes. A linha do `def` leva os quatro espaços dos outros `def`:

   ```python partial
       def adicionar(self, unidades):
           """Acrescenta unidades ao artigo.

           Recebe: unidades, um número inteiro positivo (1 ou mais).
           Devolve: nada (None).
           Falha: lança ValueError se unidades não for um número inteiro ou
           não for positivo. Nesse caso, a quantidade fica como estava.
           """
           if not isinstance(unidades, int):
               raise ValueError("As unidades a adicionar têm de ser um número inteiro.")
           if unidades <= 0:
               raise ValueError("As unidades a adicionar têm de ser 1 ou mais.")
           self.quantidade = self.quantidade + unidades
   ```

   Lê primeiro a docstring, que é o contrato. O código de baixo cumpre-o: as duas verificações recusam o pedido antes de qualquer mudança, e a última linha escreve na propriedade.

2. Troca as linhas depois da classe por estas, com um pedido aceite, um recusado e um terceiro em que guardas o que o `adicionar` devolve:

   ```python partial
   caderno = Artigo("A01", "Caderno", 6)

   caderno.adicionar(3)
   print("Depois de adicionar 3:", caderno.quantidade)

   try:
       caderno.adicionar(0)
   except ValueError as erro:
       print("Recusado:", erro)
   print("Depois da tentativa com 0:", caderno.quantidade)

   resposta = caderno.adicionar(1)
   print("O que adicionar devolveu:", resposta)
   print("Quantidade final:", caderno.quantidade)
   ```

   Guarda e executa. O que deves ver:

   ```text
   Depois de adicionar 3: 9
   Recusado: As unidades a adicionar têm de ser 1 ou mais.
   Depois da tentativa com 0: 9
   O que adicionar devolveu: None
   Quantidade final: 10
   ```

   Isto quer dizer que o pedido de 0 foi recusado pelo próprio método, sem mexer na quantidade, e que o `adicionar` não devolve nada, como o contrato promete. Se aparecer outra coisa, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

3. Acrescenta à classe o método `retirar`, a seguir ao `adicionar`, também com uma linha em branco antes:

   ```python partial
       def retirar(self, unidades):
           """Retira unidades ao artigo.

           Recebe: unidades, um número inteiro positivo (1 ou mais).
           Devolve: nada (None).
           Falha: lança ValueError se unidades não for um número inteiro, se
           não for positivo, ou se não houver unidades suficientes. Esta última
           regra é verificada pelo setter da quantidade, que recusa qualquer
           valor negativo. Em todos os casos de falha, a quantidade fica como
           estava.
           """
           if not isinstance(unidades, int):
               raise ValueError("As unidades a retirar têm de ser um número inteiro.")
           if unidades <= 0:
               raise ValueError("As unidades a retirar têm de ser 1 ou mais.")
           # A falta de unidades é recusada pelo setter: o resultado seria negativo.
           self.quantidade = self.quantidade - unidades
   ```

   As duas verificações são as do `adicionar`, com outras mensagens, e o método não verifica se há unidades suficientes. Assim, a regra da quantidade continua escrita num só sítio, o setter.

4. Troca as linhas depois da classe por estas, com dois artigos e quatro pedidos ao caderno:

   ```python partial
   caderno = Artigo("A01", "Caderno", 6)
   pasta = Artigo("A02", "Pasta", 2)

   caderno.retirar(2)
   print("Depois de retirar 2:", caderno.quantidade)

   try:
       caderno.retirar(9)
   except ValueError as erro:
       print("Retirar 9 recusado:", erro)

   try:
       caderno.retirar(0)
   except ValueError as erro:
       print("Retirar 0 recusado:", erro)

   try:
       caderno.retirar(-3)
   except ValueError as erro:
       print("Retirar -3 recusado:", erro)

   print("Caderno no fim:", caderno.quantidade)
   print("Pasta no fim:", pasta.quantidade)
   ```

5. Antes de executares, prevê de cabeça as duas últimas colunas deste traço. O caderno começa com 6 unidades, e cada linha parte do que a anterior deixou:

   | Pedido | Verificações do método | O setter recebe | Resposta | Quantidade depois |
   | --- | --- | --- | --- | ---: |
   | `retirar(2)` | inteiro e positivo: passa | 6 - 2 = 4, que é válido | | |
   | `retirar(9)` | inteiro e positivo: passa | 4 - 9 = -5, que é negativo | | |
   | `retirar(0)` | não é positivo: `ValueError` | Não chega a ser chamado | | |
   | `retirar(-3)` | não é positivo: `ValueError` | Não chega a ser chamado | | |

6. Guarda e executa. O que deves ver:

   ```text
   Depois de retirar 2: 4
   Retirar 9 recusado: A quantidade não pode ser negativa.
   Retirar 0 recusado: As unidades a retirar têm de ser 1 ou mais.
   Retirar -3 recusado: As unidades a retirar têm de ser 1 ou mais.
   Caderno no fim: 4
   Pasta no fim: 2
   ```

   A resposta, nas duas colunas: o pedido de 2 é aceite e deixa 4. O de 9 é recusado com `ValueError` pelo setter, porque a conta daria -5, e os de 0 e de -3 pelo próprio método. A exceção do pedido de 9 nasce no setter, atravessa o `retirar`, que não a trata, e é apanhada pelo `except` à volta do pedido. A quantidade fica em 4 depois de cada recusa, e a pasta, que não recebeu nenhum pedido, fica com 2.

7. Muda o comentário do topo para esta linha, porque a classe já não tem só a propriedade:

   ```python partial
   # artigo.py: a classe Artigo final do tema 03, com a propriedade e os métodos com contrato.
   ```

8. Acrescenta no fim do ficheiro, fora de qualquer `try`, um pedido para retirar as 4 unidades que restam:

   ```python partial
   caderno.retirar(4)
   print("Caderno depois de retirar 4:", caderno.quantidade)
   ```

   Guarda e executa. A última linha é `Caderno depois de retirar 4: 0`. Retirar tudo o que existe é aceite, porque zero é um estado válido: o material esgotou. O pedido de 0 é que é recusado, porque não pede nada. O zero do estado e o zero do pedido são perguntas diferentes.

### Paragem 7

O programa mostra as seis linhas do passo 6 e, no fim, `Caderno depois de retirar 4: 0`. O ficheiro final, para conferires o teu:

```python
# artigo.py: a classe Artigo final do tema 03, com a propriedade e os métodos com contrato.

class Artigo:
    """Artigo do inventário: código, nome e uma quantidade sempre válida.

    A quantidade é uma propriedade. Lê-se e escreve-se como um atributo
    normal (artigo.quantidade), mas cada escrita passa pelo setter, que
    recusa valores inválidos com ValueError.
    """

    def __init__(self, codigo, nome, quantidade):
        """Cria o artigo. A quantidade inicial passa pelo setter, como qualquer outra."""
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
        """Acrescenta unidades ao artigo.

        Recebe: unidades, um número inteiro positivo (1 ou mais).
        Devolve: nada (None).
        Falha: lança ValueError se unidades não for um número inteiro ou
        não for positivo. Nesse caso, a quantidade fica como estava.
        """
        if not isinstance(unidades, int):
            raise ValueError("As unidades a adicionar têm de ser um número inteiro.")
        if unidades <= 0:
            raise ValueError("As unidades a adicionar têm de ser 1 ou mais.")
        self.quantidade = self.quantidade + unidades

    def retirar(self, unidades):
        """Retira unidades ao artigo.

        Recebe: unidades, um número inteiro positivo (1 ou mais).
        Devolve: nada (None).
        Falha: lança ValueError se unidades não for um número inteiro, se
        não for positivo, ou se não houver unidades suficientes. Esta última
        regra é verificada pelo setter da quantidade, que recusa qualquer
        valor negativo. Em todos os casos de falha, a quantidade fica como
        estava.
        """
        if not isinstance(unidades, int):
            raise ValueError("As unidades a retirar têm de ser um número inteiro.")
        if unidades <= 0:
            raise ValueError("As unidades a retirar têm de ser 1 ou mais.")
        # A falta de unidades é recusada pelo setter: o resultado seria negativo.
        self.quantidade = self.quantidade - unidades


caderno = Artigo("A01", "Caderno", 6)
pasta = Artigo("A02", "Pasta", 2)

caderno.retirar(2)
print("Depois de retirar 2:", caderno.quantidade)

try:
    caderno.retirar(9)
except ValueError as erro:
    print("Retirar 9 recusado:", erro)

try:
    caderno.retirar(0)
except ValueError as erro:
    print("Retirar 0 recusado:", erro)

try:
    caderno.retirar(-3)
except ValueError as erro:
    print("Retirar -3 recusado:", erro)

print("Caderno no fim:", caderno.quantidade)
print("Pasta no fim:", pasta.quantidade)

caderno.retirar(4)
print("Caderno depois de retirar 4:", caderno.quantidade)
```

Em cima está a classe final: o construtor, a propriedade, com o getter e o setter, e os métodos `adicionar` e `retirar`, cada um com o seu contrato. Por baixo estão os dois artigos, os pedidos do traço, com cada recusa no seu `try`, e o pedido que esgota o caderno.

Pensa antes de terminares: o setter já recusa quantidades negativas. Se apagasses as duas verificações do `adicionar`, o que fazia `caderno.adicionar(-3)` a um caderno com 6 unidades? A resposta: tirava-lhe três. O setter recebia 6 + (-3) = 3, uma quantidade válida, e aceitava-a sem ninguém dar pelo engano. O setter protege o estado, mas só o método sabe o que um pedido de adicionar quer dizer.

## Se alguma coisa falhar

1. Guardaste antes de executar? Se a saída não mudou com as tuas alterações, guarda e executa outra vez.
2. Estás a executar o `artigo.py` da pasta `tema-03`, e não outro ficheiro?
3. Executaste o ficheiro todo? Cada execução volta ao princípio e usa só os valores escritos no ficheiro.
4. Desfizeste a experiência anterior? Cada erro provocado acaba com um passo que o desfaz. Se te perderes, volta ao último passo que escreve o ficheiro de novo, o passo 1 das fases 1, 2, 3 ou 5, e refaz daí os passos. As paragens 4 e 7 mostram o ficheiro completo.
5. Apareceu uma mensagem de erro? Lê primeiro a última linha, com o tipo de erro e o que aconteceu, e procura-a nos títulos seguintes.

### Aparece `IndentationError`, `TabError` ou `SyntaxError`

É um erro de escrita: o Python não consegue ler o ficheiro, e o programa nem começa. Por isso, a mensagem não tem a linha `Traceback` e abre logo com o ficheiro e o número da linha. As mensagens mais comuns neste laboratório são estas:

- `IndentationError: unexpected indent` ("indentação inesperada"): a linha tem espaços a mais.
- `IndentationError: expected an indented block` ("esperava-se um bloco indentado"): um `def`, um `if`, um `try` ou um `except` ficou sem nenhuma linha indentada por baixo. Nas versões recentes, a mensagem acaba com o número dessa linha.
- `IndentationError: unindent does not match any outer indentation level` ("o recuo não corresponde a nenhum nível de indentação"): a linha recuou para uma margem que nenhuma linha de cima tem. Acontece, por exemplo, com um `def` com dois espaços.
- `TabError: inconsistent use of tabs and spaces in indentation`: uma linha tem uma tabulação no lugar dos espaços. Apaga-a e escreve os espaços.
- `SyntaxError: expected ':'` ("esperava `:`"; no Python 3.9, só `invalid syntax`): falta o sinal de dois pontos no fim de uma linha `def`, `if`, `try` ou `except`.

Dentro da classe, os `def` e os decoradores levam quatro espaços. As linhas de dentro de um método levam oito, e as de dentro de um `if`, doze. Fora da classe, as de dentro de um `try` ou de um `except` levam quatro. Compara a linha que a mensagem mostra, e a de cima, com as do bloco que escreveste.

### Aparece `AttributeError: 'Artigo' object has no attribute 'adicionar'` ou `'retirar'`

Em português: o objeto do tipo `Artigo` não tem nenhum atributo com esse nome, porque o Python chama atributo também a um método. O `def` ficou encostado à margem, fora da classe, e o Python aceitou-o como uma função solta. Dá ao `def` quatro espaços e às linhas de dentro oito, como no setter.

### Aparece `NameError: name 'ValueErrror' is not defined`

Ou o mesmo com outro nome parecido, como `valueError`. O Python não conhece esse nome, e as versões recentes acrescentam `Did you mean: 'ValueError'?` ("querias dizer `ValueError`?"). Escreve `ValueError`, com as duas maiúsculas. Enquanto só experimentares valores válidos, o programa parece certo, porque o engano só se vê quando um `raise` corre.

### Aparece `AttributeError: 'Artigo' object has no attribute '_quantidade'`

O valor nunca chegou a ser guardado em `_quantidade`, porque há um engano num nome, como `self._quantiade` ou `self.quantiade`. Nas fases 3 e 4, o construtor e o set guardam em `self._quantidade`. A partir da fase 5, o construtor escreve em `self.quantidade`, e o setter guarda em `self._quantidade`. As versões recentes do Python sugerem um nome parecido. Na propriedade, a correção não é no getter: com `return self.quantidade`, o getter chama-se a si próprio, e o programa para com um `RecursionError`.

### Aparece `RecursionError: maximum recursion depth exceeded`, sem o teres provocado

É o erro do passo 3 da fase 5. Há um `self.quantidade` onde devia estar `self._quantidade`, na última linha do setter ou no `return` do getter. Dentro dos dois métodos da propriedade, o valor lê-se e guarda-se sempre no nome com sublinhado.

### Aparece `AttributeError: 'function' object has no attribute 'setter'`

Em português: um objeto do tipo função não tem nenhum atributo `setter`. O programa para ainda a ler a classe, na linha `@quantidade.setter`, porque falta a linha `@property` antes do primeiro `def quantidade`. Escreve-a mesmo por cima desse `def`.

### Aparece um valor inválido sem nenhuma recusa, como `Depois da tentativa com 2.5: 2.5` ou `Caderno no fim: -5`

Na fase 5, o 2.5 é aceite, e a linha da caneta com -5 desaparece. Na fase 7, o caderno fica com -5, e a linha `Retirar 9 recusado` não aparece. Falta a linha `@quantidade.setter` antes do segundo `def quantidade`: sem ela, esse método deixa de ser o setter, e a escrita guarda o valor num atributo normal, sem verificação. Escreve-a mesmo por cima do segundo `def quantidade`.

### Aparece `AttributeError: property 'quantidade' of 'Artigo' object has no setter`

Em português: a propriedade `quantidade` não tem setter. Nas versões mais antigas, a mensagem é outra, como `AttributeError: can't set attribute` ("não é possível definir o atributo"). O segundo método tem outro nome, como `def guardar_quantidade(self, valor):`. Os dois métodos da propriedade chamam-se `quantidade`, porque é o nome que os liga à mesma propriedade.

### Aparece `TypeError: 'int' object is not callable`

Em português: um objeto do tipo `int` não se pode chamar. Escreveste `caderno.quantidade()`, com parênteses, como num método. Uma propriedade lê-se sem parênteses: `caderno.quantidade`.

### O programa não para no erro que esperavas

Há um `try` à volta da linha, com um `except` desse tipo de exceção, e é ele que deixa o programa continuar. Procura o `try` acima da linha.

## Desafios

Na pasta `tema-03`, cria no editor um ficheiro novo, `desafios.py`, e copia para ele todo o `artigo.py` da paragem 7. Faz os dois desafios nesse ficheiro, um a seguir ao outro, para o `artigo.py` ficar como na paragem 7.

1. Um limite máximo. Diz-se que, quando uma regra muda, só é preciso mudar a classe, e o resto do programa continua a fazer os mesmos pedidos. Vais comprová-lo. A regra nova: a quantidade de um artigo não pode passar de 100 unidades. Pode ser 100, mas não 101.

   Antes de mexer no código, decide três coisas. Em que método da classe vais escrever a regra, e porquê? Em que posição, em relação às verificações que já lá estão? Que mensagem vais usar? Escreve as três decisões num comentário por cima da regra, e depois a regra. No fim, confirma que não precisaste de mudar o construtor, o `adicionar` nem o `retirar`.

   Depois substitui as linhas que vêm depois da classe por testes teus, cada um no seu `try` quando puder ser recusado, que mostrem estes quatro casos:

   - criar um artigo com 150 unidades;
   - a um caderno com 6 unidades, adicionar 95;
   - ao mesmo caderno, adicionar 94;
   - acertar a quantidade do caderno para 101.

   Para cada caso, prevê se vai ser aceite ou recusado, quem recusa e a quantidade que fica. No fim do ficheiro, responde num comentário, numa frase: porque é que o `adicionar` passou a respeitar o limite, se não lhe tocaste? Pista: segue, no `adicionar`, o caminho do valor novo até ao sítio onde é guardado.

2. Perguntar se está esgotado. Acrescenta à classe um método `esgotado()`, que responde `True` se a quantidade for zero e `False` se não for. Escreve primeiro o contrato na docstring, com as quatro partes: o que recebe, o que devolve, quando falha e o que acontece ao estado. Depois testa-o com um artigo, antes e depois de lhe retirares todas as unidades. Pista: pensa se este método precisa de verificar algum valor, ou se só consulta.

## Antes de terminares

- [ ] O `artigo.py` da pasta `tema-03` corre e mostra as seis linhas do passo 6 da fase 7 e, no fim, `Caderno depois de retirar 4: 0`.
- [ ] Desfizeste todas as alterações feitas de propósito: o `artigo.py` está igual ao da paragem 7.
- [ ] Guardaste o `artigo.py` e, se fizeste os desafios, o `desafios.py`, e entregaste-os pelo meio que o professor indicar.
- [ ] Sabes ler uma mensagem de erro de baixo para cima e dizer onde o erro aparece e onde está a causa.
- [ ] Sabes dizer porque é que o setter guarda em `_quantidade` e o construtor escreve em `quantidade`.
- [ ] Consegues explicar, por palavras tuas, porque é que o artigo verifica cada pedido antes de mexer na quantidade, e o que fica igual quando recusa.

![Rodapé](../../imagens/rodape.png)

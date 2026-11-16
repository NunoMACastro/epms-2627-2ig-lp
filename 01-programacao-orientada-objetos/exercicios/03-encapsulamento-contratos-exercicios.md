![Cabeçalho](../../imagens/cabecalho.png)

# Ficha de exercícios: Encapsulamento e contratos

Praticas a diferença entre estado válido e pedido válido, a ordem de verificar e alterar, a leitura de uma mensagem de erro e o `try` e o `except`. Escreves também uma propriedade nova. Os exercícios 1 a 6 são obrigatórios. Cada exercício faz-se num script novo, com o nome que o enunciado indica, na pasta `tema-03` do laboratório. As respostas por palavras ficam num comentário no fim do script. Entregas os scripts pelo meio que o professor indicar. Para rever: o [guia do tema](../03-encapsulamento-contratos.md) e o [laboratório](../laboratorios/03-encapsulamento-contratos-laboratorio.md).

## O cenário

Os exercícios 4 a 6 e os desafios usam a classe `Artigo` final do guia, a do [programa completo do exemplo guiado](../03-encapsulamento-contratos.md#passo-6-executar-e-comparar-com-o-traço), sem as linhas que vêm depois da classe. É esta, com a propriedade `quantidade` e os métodos `adicionar` e `retirar`. Quando um exercício a usa, copia-a para o script e escreve por baixo dela as linhas que ele dá.

```python
# A classe final do guia 03, com o método retirar do exemplo guiado.

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
```

## Exercício 1: Estado válido e pedido válido

No inventário, a quantidade guardada num artigo é um número inteiro, 0 ou mais. Um pedido de retirada tem de ser um número inteiro positivo, que não passe do que existe. Cria o script `estado_e_pedido.py` e responde só com comentários.

1. Para cada valor, diz se é uma quantidade válida para um artigo, isto é, um estado válido, e que regra o decide: `0`, `7`, `-1`, `3.5` e `"4"`.
2. Um artigo tem 5 unidades. Para cada pedido de retirada, diz se é válido e que regra o decide: retirar `5`, retirar `0` e retirar `6`.

Rever: [As regras que devem continuar verdadeiras](../03-encapsulamento-contratos.md#as-regras-que-devem-continuar-verdadeiras).

<details>
<summary>Pista</summary>

O `0` aparece nas duas alíneas. Em cada uma, pergunta-te se é uma quantidade guardada ou um pedido.

</details>

## Exercício 2: Verificar primeiro, alterar depois

Três colegas escreveram três versões do método `set_quantidade`, para a classe com get e set do guia, a que guarda a quantidade em `_quantidade`. São excertos, sem o resto da classe, e as três só verificam se o valor é negativo.

Versão A:

```python partial
    def set_quantidade(self, valor):
        if valor < 0:
            raise ValueError("A quantidade não pode ser negativa.")
        self._quantidade = valor
```

Versão B:

```python partial
    def set_quantidade(self, valor):
        self._quantidade = valor
        if valor < 0:
            raise ValueError("A quantidade não pode ser negativa.")
```

Versão C:

```python partial
    def set_quantidade(self, valor):
        if valor < 0:
            print("A quantidade não pode ser negativa.")
        self._quantidade = valor
```

Nas três, o programa principal é este, com um caderno de 6 unidades:

```python partial
caderno = Artigo("A01", "Caderno", 6)
try:
    caderno.set_quantidade(-3)
except ValueError as erro:
    print("Recusado:", erro)
print("Quantidade:", caderno.get_quantidade())
```

Cria o script `tres_versoes.py` e responde só com comentários, sem executar.

1. Para cada versão, quem mostra a mensagem de recusa: o `except` ou o próprio método? E que quantidade fica guardada?
2. Qual das três cumpre a regra "verificar primeiro, alterar depois"? Explica numa frase o que falta a cada uma das outras duas, a pensar na quantidade guardada e em quem fez o pedido.

Rever: [Um set que verifica, mas não obriga](../03-encapsulamento-contratos.md#um-set-que-verifica-mas-não-obriga), [Recusar a sério, com `raise`](../03-encapsulamento-contratos.md#recusar-a-sério-com-raise) e [Tratar a recusa com `try` e `except`](../03-encapsulamento-contratos.md#tratar-a-recusa-com-try-e-except).

<details>
<summary>Pista</summary>

Para cada versão, segue a chamada `set_quantidade(-3)` linha a linha. Depois de cada linha, vê o valor de `_quantidade` e se o método já parou.

</details>

## Exercício 3: Ler uma mensagem de erro

Um colega copiou a classe do cenário para um ficheiro `artigo.py` e escreveu por baixo este programa principal:

```python partial
caneta = Artigo("A03", "Caneta", 4)
caneta.adicionar(2)
caneta.retirar(9)
print("Quantidade:", caneta.quantidade)
```

Ao executar, o Python mostrou isto. O caminho do ficheiro foi encurtado, e as linhas com `~` e `^` só aparecem a partir do Python 3.11:

```text
Traceback (most recent call last):
  File ".../artigo.py", line 66, in <module>
    caneta.retirar(9)
    ~~~~~~~~~~~~~~^^^
  File ".../artigo.py", line 61, in retirar
    self.quantidade = self.quantidade - unidades
    ^^^^^^^^^^^^^^^
  File ".../artigo.py", line 28, in quantidade
    raise ValueError("A quantidade não pode ser negativa.")
ValueError: A quantidade não pode ser negativa.
```

Cria o script `mensagem_de_erro.py` e responde só com comentários.

1. Qual é o tipo do erro, e qual é a mensagem?
2. Que linha do programa principal fez o pedido que falhou? Indica o número e o código.
3. Em que método nasceu a exceção? Explica porque é que a mensagem lhe chama `quantidade`.
4. A última linha do programa, a do `print`, foi executada? Que valor recebeu o setter, e que quantidade ficou guardada na caneta?

Rever: [Nada impede uma quantidade impossível](../03-encapsulamento-contratos.md#nada-impede-uma-quantidade-impossível), [Recusar a sério, com `raise`](../03-encapsulamento-contratos.md#recusar-a-sério-com-raise) e [A propriedade `quantidade`](../03-encapsulamento-contratos.md#a-propriedade-quantidade).

<details>
<summary>Pista</summary>

Lê a mensagem de baixo para cima. A última linha diz o que aconteceu. Cada linha que começa por `File` diz o número de uma linha e onde ela está, num método ou em `<module>`, o programa principal. Por baixo dela vem o código dessa linha. A linha `File` mais abaixo é a do sítio onde a exceção nasceu.

</details>

## Exercício 4: Tratar recusas e continuar

Queremos um programa principal, escrito depois da classe do cenário no script `caneta.py`, que:

- crie uma caneta com o código A03, o nome Caneta e 4 unidades;
- tente retirar 5 unidades;
- tente adicionar 2.5 unidades;
- tente retirar 4 unidades;
- mostre a quantidade final.

Cada pedido recusado mostra uma linha que começa por `Recusado:`, seguida da mensagem da exceção, e o programa continua para o pedido seguinte. Cada pedido aceite mostra uma linha que começa por `Aceite:`, seguida da quantidade que ficou. Um pedido recusado nunca mostra a linha do `Aceite:`.

1. Escreve o programa, com um `try` e um `except` para cada pedido.
2. Num comentário no fim do script, diz para cada pedido se é aceite ou recusado e, quando é recusado, quem o recusa: o método ou o setter.

Rever: [Tratar a recusa com `try` e `except`](../03-encapsulamento-contratos.md#tratar-a-recusa-com-try-e-except) e [Operações com contrato](../03-encapsulamento-contratos.md#operações-com-contrato).

<details>
<summary>Pista</summary>

Antes de escreveres, segue os três pedidos com a quantidade que cada um encontra. Para a linha do `Aceite:`, pergunta-te que linhas de um `try` correm depois de um pedido que lança uma exceção. Para saber quem recusa, compara a mensagem de cada recusa com as dos `raise` da classe.

</details>

## Exercício 5: Uma propriedade nova

O responsável do armário quer saber quando é preciso encomendar material. Queremos que cada artigo tenha um **stock mínimo**: quando a quantidade fica abaixo desse número, é altura de encomendar. O stock mínimo é um número inteiro, não pode ser negativo, e um artigo acabado de criar tem stock mínimo 0.

Deves poder consultar e acertar o stock mínimo como a quantidade, com `caderno.stock_minimo`. O programa recusa, com `ValueError`, um valor que não seja inteiro ou que seja negativo, e o stock mínimo fica como estava.

Trabalha no script `stock_minimo.py`, com a classe do cenário.

1. Decide se o stock mínimo pode ser maior do que a quantidade atual do artigo. Justifica numa frase, num comentário no fim do script, a pensar para que serve o stock mínimo.
2. Acrescenta à classe a propriedade `stock_minimo`, com getter e setter:
   - o valor fica guardado em `_stock_minimo`;
   - o setter verifica o valor pela mesma ordem da propriedade `quantidade`;
   - a docstring do setter tem o contrato, com as quatro partes e a tua decisão da alínea 1;
   - o stock mínimo 0 de um artigo novo também passa pelo setter.

   Para testar, o programa parte de um caderno com 6 unidades e mostra o stock mínimo inicial. Depois tenta acertá-lo para 10, para -1 e para `"dez"`, cada tentativa no seu `try`. No fim, mostra o stock mínimo e a quantidade.

Rever: [A propriedade `quantidade`](../03-encapsulamento-contratos.md#a-propriedade-quantidade), [O construtor também passa pelo setter](../03-encapsulamento-contratos.md#o-construtor-também-passa-pelo-setter) e [Operações com contrato](../03-encapsulamento-contratos.md#operações-com-contrato).

<details>
<summary>Pista</summary>

Parte da propriedade `quantidade` da classe e muda os nomes e as mensagens para os do stock mínimo. Depois acrescenta ao construtor a linha que dá o 0. Para o contrato, segue a forma das docstrings do `adicionar` e do `retirar`.

</details>

## Exercício 6: O erro de um colega no setter

Um colega escreveu assim o setter da quantidade:

```python partial
    @quantidade.setter
    def quantidade(self, valor):
        """Setter: guarda o valor se for válido; senão, lança ValueError (versão com erro)."""
        if not isinstance(valor, int):
            raise ValueError("A quantidade tem de ser um número inteiro.")
        if valor <= 0:
            raise ValueError("A quantidade não pode ser negativa.")
        self._quantidade = valor
```

Para testar, criou um caderno com 6 unidades e escreveu, cada uma no seu `try`, as linhas `caderno.quantidade = -3` e `caderno.quantidade = 2.5`. As duas foram recusadas, e ele ficou convencido de que o setter está certo.

Copia a classe do cenário para o script `setter_do_colega.py` e troca o setter dela por este, desde a linha do `@quantidade.setter`.

1. Escreve um teste que mostre que o colega está enganado. Parte de um caderno com 6 unidades, como o colega. Dentro de um `try`, faz um pedido que as regras do inventário aceitam e que este setter recusa. No fim, uma linha mostra a quantidade do caderno. Escolhe tu o pedido.
2. Num comentário no fim do script, explica o erro por palavras, com as palavras "estado" e "pedido".
3. Corrige o setter, mudando uma só linha.

Rever: [As regras que devem continuar verdadeiras](../03-encapsulamento-contratos.md#as-regras-que-devem-continuar-verdadeiras) e [A propriedade `quantidade`](../03-encapsulamento-contratos.md#a-propriedade-quantidade).

<details>
<summary>Pista</summary>

Lê a condição do colega como uma frase em português: que valores recusa? Compara-os com a regra da quantidade guardada, a do exercício 1.

</details>

## Desafios

### Desafio 1: Uma recusa que fica pelo caminho

Um colega escreveu esta versão do `retirar`, com um `try` dentro do próprio método. O `except ValueError:`, sem o `as`, apanha a exceção sem lhe dar um nome.

```python partial
    def retirar(self, unidades):
        """Retira unidades ao artigo (versão com erro)."""
        if not isinstance(unidades, int):
            raise ValueError("As unidades a retirar têm de ser um número inteiro.")
        if unidades <= 0:
            raise ValueError("As unidades a retirar têm de ser 1 ou mais.")
        try:
            self.quantidade = self.quantidade - unidades
        except ValueError:
            print("Não há unidades suficientes.")
```

Para a testar, escreveu este programa principal, como o do exercício 4:

```python partial
caderno = Artigo("A01", "Caderno", 6)

try:
    caderno.retirar(9)
    print("Aceite:", caderno.quantidade)
except ValueError as erro:
    print("Recusado:", erro)

print("Quantidade:", caderno.quantidade)
```

Viu a mensagem "Não há unidades suficientes." e ficou convencido de que o método funciona. Monta o programa dele no script `recusa_perdida.py`: a classe do cenário, com este `retirar` no lugar do dela, e o programa principal por baixo.

1. Descobre de cabeça as linhas que o programa mostra, e executa para confirmares.
2. Num comentário no fim do script, explica porque é que apareceu a linha do `Aceite:`, se faltavam unidades. Explica também porque é que esta versão não cumpre o contrato do `retirar`, a pensar em quem fez o pedido.
3. Corrige o método, para o programa do colega mostrar a recusa.

Rever: [Tratar a recusa com `try` e `except`](../03-encapsulamento-contratos.md#tratar-a-recusa-com-try-e-except) e [Passo 1: escrever o contrato](../03-encapsulamento-contratos.md#passo-1-escrever-o-contrato).

<details>
<summary>Pista</summary>

Segue o pedido de 9 linha a linha, primeiro dentro do método e depois no programa do colega. Em cada `try`, vê se houve uma exceção e quem a apanhou.

</details>

### Desafio 2: Uma quantidade verdadeira

No script `verdadeiro.py`, copia a classe do cenário, sem alterações, e escreve por baixo estas linhas:

```python partial
caderno = Artigo("A01", "Caderno", 6)
caderno.quantidade = True
print(caderno.quantidade)
caderno.adicionar(True)
print(caderno.quantidade)
```

1. Descobre de cabeça o que mostram os dois `print`, e executa para confirmares. Num comentário no fim do script, explica o que viste, a partir do que dão `isinstance(True, int)` e `True + 1`.
2. Muda o setter para recusar `True` e `False` como quantidade, e confirma que continua a aceitar 0 e 1. Com essa mudança, o que acontece a `caderno.adicionar(True)`? Explica porquê, no mesmo comentário, e diz em que outros sítios da classe a mesma verificação faria falta.

Rever: [Um set que verifica, mas não obriga](../03-encapsulamento-contratos.md#um-set-que-verifica-mas-não-obriga) e [Operações com contrato](../03-encapsulamento-contratos.md#operações-com-contrato).

<details>
<summary>Pista</summary>

Experimenta no script `print(isinstance(True, int))` e `print(True + 1)` antes de explicares. Com o setter novo, a linha `caderno.quantidade = True` para o programa: para veres o que acontece ao `adicionar(True)`, tira-a, ou põe-na num `try`.

</details>

### Desafio 3: O nome também tem regras

No inventário, o nome de um artigo não pode ser vazio. Com a classe do cenário, `Artigo("A08", "", 3)` é aceite sem problemas. No script `nome.py`, com a classe do cenário, o nome passa a ser uma propriedade, como a quantidade.

1. Um nome só com espaços, como `"   "`, conta como vazio? Decide, e justifica a escolha numa frase, num comentário no fim do script.
2. Acrescenta à classe uma propriedade `nome`, com getter e setter, que guarda o valor em `_nome`, recusa um nome vazio com `ValueError` e cumpre a tua decisão. O construtor passa pelo setter, e a docstring do setter tem o contrato. Testa com um nome válido, um nome vazio e um nome só com espaços. Em cada teste, o programa mostra o nome guardado ou a mensagem da recusa.

Rever: [A propriedade `quantidade`](../03-encapsulamento-contratos.md#a-propriedade-quantidade), [O construtor também passa pelo setter](../03-encapsulamento-contratos.md#o-construtor-também-passa-pelo-setter) e [Operações com contrato](../03-encapsulamento-contratos.md#operações-com-contrato).

<details>
<summary>Pista</summary>

Começa pelo contrato: a tua decisão entra na parte que diz quando o setter falha. Se decidires que um nome só com espaços é vazio, serve-te o método `strip` dos textos. Devolve o texto sem os espaços do início e do fim: `"   Caneta ".strip()` dá `"Caneta"`. Em inglês, *strip* quer dizer tirar.

</details>

## Critérios de conclusão

- Fizeste os exercícios 1 a 6, cada um no seu script, e as respostas por palavras estão num comentário no fim de cada script.
- Em cada recusa que experimentaste, viste também a quantidade que ficou, e não só a mensagem.
- No exercício 4, cada pedido mostra uma linha `Aceite:` ou `Recusado:`, e o programa chega à quantidade final.
- No exercício 5, o -1 e o `"dez"` são recusados com a mensagem do teu setter, e o stock mínimo fica como estava. No exercício 6, o setter está corrigido com uma só linha mudada.

![Rodapé](../../imagens/rodape.png)

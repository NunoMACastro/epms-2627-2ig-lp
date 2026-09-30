![Cabeçalho](../imagens/cabecalho.png)

# Laboratório: construir o inventário em Python

*M10 · Caderno 4 · Laboratório*

Este laboratório acompanha o [caderno 4](04-composicao-modelacao.md). Diz-te o que fazer, passo a passo, com o editor de Python aberto ao lado. As explicações do porquê estão no caderno: quando um passo usa uma ideia, o texto diz em que secção ela está explicada. Conta com cerca de uma hora.

No fim deves ter um ficheiro `inventario.py` com as classes `Artigo` e `Inventario` a funcionar, deves ter lido o caminho de uma exceção que atravessa vários métodos e deves ter acrescentado ao inventário duas operações escritas por ti.

## Antes de começar

Precisas do computador com o editor de Python que usas nas aulas, e de papel e caneta para as previsões e para o diagrama da última parte.

Antes do laboratório deves ter lido, no caderno 4, as secções 8 a 11: o diagrama do inventário, as listas e o ciclo `for`, o exemplo guiado e o caminho de uma recusa. O laboratório não repete essas explicações: aplica-as.

A forma de trabalhar é sempre a mesma. Antes de executares o programa, escreves no papel o que esperas ver. Depois executas e comparas. Quando o resultado é diferente do que previste, a explicação dessa diferença é o que mais te ensina, por isso não a saltes. Escrever primeiro obriga-te a pensar; executar primeiro só te mostra o que o Python fez.

Uma regra para todo o laboratório: executa sempre o ficheiro inteiro. Cada execução começa do zero, cria um inventário novo e repete todos os pedidos, pela ordem em que estão escritos.

## Parte 1: preparar o ficheiro (5 min)

1. Na pasta onde guardas os trabalhos de LP, cria uma pasta nova chamada `caderno-4`.
2. Dentro dessa pasta, cria um ficheiro novo chamado `inventario.py`. O nome tem de acabar em `.py` e não deve ter espaços nem acentos.
3. Abre o caderno 4 na secção 1. Copia do primeiro programa apenas a classe `Artigo`: desde a linha `class Artigo:` até à última linha do método `retirar`, a que diz `self.quantidade = self.quantidade - unidades`. Não copies as linhas que vêm depois da classe, as que começam em `caderno = Artigo(...)`.
4. Cola a classe no ficheiro e guarda.
5. Executa o ficheiro.

O que deves ver: nada. O ficheiro só define uma classe, e definir uma classe não mostra nada no ecrã, tal como escrever uma receita não faz nenhum bolo. Se aparecer uma mensagem de erro, lê a última linha. Um `IndentationError` quer dizer que alguma linha ficou com a indentação errada na cópia: compara-a com o caderno. Um `SyntaxError` quer dizer, quase sempre, que ficou uma linha cortada a meio.

## Parte 2: o construtor e a lista interna (5 min)

Tem aberto ao lado o passo 2 da secção 10 do caderno.

1. Depois da classe `Artigo`, deixa duas linhas em branco e escreve a classe `Inventario` com o construtor, tal como está no passo 2. Escreve-a à mão, em vez de a copiares: escrever obriga-te a reparar em cada pormenor, como o sublinhado de `_artigos` e os dois pontos no fim de cada `def`.
2. No fim do ficheiro, encostadas à margem, acrescenta estas duas linhas:

```python partial
inventario = Inventario()
print(inventario._artigos)
```

3. Escreve no papel o que esperas ver. Depois executa.

Deves ver `[]`, a lista vazia que o construtor criou. Estamos a espreitar a lista interna só para confirmar que o construtor funciona enquanto construímos a classe. É a única vez neste laboratório em que o código de fora usa `_artigos`, e vais apagar esta linha já a seguir. No programa final, o código de fora não mexe na lista, pela razão explicada no passo 2 do caderno.

4. Apaga a linha do `print`. Mantém a linha `inventario = Inventario()`.

## Parte 3: registar e procurar (10 min)

Tem aberto ao lado os passos 3 e 4 da secção 10.

1. Dentro da classe `Inventario`, a seguir ao construtor e com a mesma indentação dele, escreve o método `_procurar` e depois o método `registar`, tal como estão nos passos 3 e 4.
2. No fim do ficheiro, a seguir a `inventario = Inventario()`, acrescenta:

```python partial
inventario.registar("A01", "Caderno", 6)
inventario.registar("A02", "Pasta", 2)
print(len(inventario._artigos))
print(inventario._procurar("A02").nome)
```

3. Prevê as duas linhas que vão aparecer. Depois executa.

Deves ver `2` e `Pasta`. A segunda linha lê-se da esquerda para a direita: `_procurar("A02")` devolve o artigo com esse código, e `.nome` consulta o nome desse artigo. Mais uma vez, estamos a usar de fora duas coisas internas, a lista e o método `_procurar`, só para testar a construção. Vais apagar estas duas linhas na parte seguinte.

4. Agora vais ver o inventário recusar um código repetido. Acrescenta no fim do ficheiro, fora de qualquer `try`:

```python partial
inventario.registar("A01", "Cola", 3)
```

5. Executa. Depois das duas linhas de antes, o programa para com uma mensagem de erro. Lê a última linha, que deve ser esta:

```text
ValueError: Já existe um artigo com o código A01.
```

Lê também, logo acima, a linha que diz em que método o erro foi lançado. Deve terminar em `in registar`, e a linha de código mostrada por baixo dela deve ser a do `raise` do método `registar`. Foi o inventário que recusou, porque é ele que conhece todos os códigos (secção 2 do caderno).

6. Apaga as três linhas de teste desta parte: o `print(len(...))`, o `print(inventario._procurar(...).nome)` e o registo da cola. Mantém a criação do inventário e os dois primeiros registos.

## Parte 4: consultar e retirar (10 min)

Tem aberto ao lado o passo 5 da secção 10.

1. Dentro da classe `Inventario`, a seguir ao método `registar`, escreve os métodos `quantidade_de` e `retirar`, tal como estão no passo 5.
2. Substitui todas as linhas que estão depois das duas classes pelas linhas do programa completo do passo 7, as que começam em `inventario = Inventario()` e acabam em `print("A02 no fim:", ...)`.
3. Abre o traço do passo 6 e, para cada linha que o programa vai mostrar, escreve no papel a mensagem que esperas. Depois executa.
4. Compara com a saída mostrada no passo 7 do caderno, linha a linha.

Se alguma linha for diferente, procura a primeira que é diferente e não olhes para as outras por agora. Uma diferença cedo no programa costuma provocar as seguintes. Depois pergunta-te que método produziu essa linha e relê esse método, comparando-o com o caderno. Os enganos mais comuns são um `return` que ficou dentro do `if` com a indentação errada, uma linha de um método que ficou fora da classe e um nome escrito de duas maneiras diferentes, como `_artigos` numa linha e `_artigo` noutra.

Nesta altura, o teu ficheiro tem o programa completo do caderno. Guarda-o.

## Parte 5: ler o caminho de uma exceção (10 min)

Na secção 11 do caderno viste que uma exceção lançada no setter sobe pela cadeia de chamadas até ser apanhada. Agora vais vê-la subir até ao fim, sem que ninguém a apanhe.

1. No fim do ficheiro, depois de todas as outras linhas e fora de qualquer `try`, acrescenta:

```python partial
inventario.retirar("A01", 9)
```

2. Antes de executares, escreve no papel a lista dos métodos por onde achas que o pedido passa até ao erro, do primeiro ao último.
3. Executa. As linhas do programa aparecem todas, como antes, e no fim aparece um traceback.

O traceback que vais ver tem quatro entradas. Cada entrada tem uma linha que começa por `File`, com o caminho do teu ficheiro, o número da linha e o nome do sítio onde o Python estava, e por baixo o código dessa linha. Os caminhos e os números das linhas dependem do teu ficheiro, e algumas versões do Python acrescentam por baixo do código uma linha com sinais `^` ou `~` a apontar para a parte da linha que falhou. O que interessa são os nomes no fim de cada linha `File` e o código que aparece por baixo:

| Entrada | Termina em | Código mostrado por baixo |
| --- | --- | --- |
| Primeira | `in <module>` | `inventario.retirar("A01", 9)` |
| Segunda | `in retirar` | `artigo.retirar(unidades)` |
| Terceira | `in retirar` | `self.quantidade = self.quantidade - unidades` |
| Quarta | `in quantidade` | `raise ValueError("A quantidade não pode ser negativa.")` |

A última linha de todas é `ValueError: A quantidade não pode ser negativa.`.

4. Responde no papel, a olhar para o teu traceback:
   - `<module>` é o nome que o Python dá ao programa principal, o código que está encostado à margem. Porque é que esta é a primeira entrada?
   - Há duas entradas que terminam em `in retirar`. Qual delas é o `retirar` do inventário e qual é o do artigo? Decide pelo código mostrado por baixo de cada uma, e não pela ordem.
   - A quarta entrada termina em `in quantidade`. Que método da classe `Artigo` é este? Porque é que o nome não é `retirar`?
   - Compara a tua lista do passo 2 com as quatro entradas. Acertaste na ordem?

O traceback é a cadeia de chamadas da secção 11, escrita pelo Python: de cima para baixo, do programa principal até ao sítio onde a exceção nasceu. É por isso que se lê de baixo para cima quando se procura a causa: a última entrada é onde o erro começou.

5. Apaga a linha que acrescentaste nesta parte e executa outra vez, para confirmares que o programa volta a terminar sem erro.

## Parte 6: acrescentar duas operações, sozinho (20 min)

Nesta parte não há código dado. Escreves tu os métodos, a partir do contrato e do que aprendeste no caderno. Escreve cada método dentro da classe `Inventario`, com uma docstring, e testa-o no fim do ficheiro, depois das linhas que já lá estão.

### 6.1: adicionar unidades a um artigo

Escreve o método `adicionar(codigo, unidades)` do inventário, com este contrato. Recebe o código de um artigo e as unidades a adicionar. Não devolve nada. Falha, com `ValueError`, se não houver nenhum artigo com esse código, ou se o próprio artigo recusar o pedido pelas regras do seu método `adicionar`. Em qualquer falha, nenhuma quantidade muda.

Antes de escreveres o método, responde no papel: que regras sobre as unidades vai verificar o método do inventário, e quais vai deixar ao artigo? Revê a ideia de encaminhamento no passo 5 da secção 10.

Depois testa o método com estes três pedidos, cada um no seu `try`, depois das linhas que já estão no fim do ficheiro. Para cada um, escreve antes de executar se vai ser aceite ou recusado, quem recusa e com que mensagem, e a quantidade de A02 depois:

- adicionar 3 unidades ao artigo A02;
- adicionar 0 unidades ao artigo A02;
- adicionar 1 unidade ao artigo A09.

No fim, mostra a quantidade de A02 com `quantidade_de`.

### 6.2: o total de unidades do inventário

Escreve o método `total_unidades()`, que devolve a soma das quantidades de todos os artigos do inventário. Não recebe nada além do `self`, não muda nenhuma quantidade e não falha.

Antes de escreveres, decide e escreve no papel duas coisas. Porque é que este método pertence ao `Inventario` e não ao `Artigo`? Usa a tabela de responsabilidades da secção 2. E o que deve devolver um inventário que ainda não tem nenhum artigo?

Para somar, vais precisar de uma variável que acumula a soma: começa com um valor antes do ciclo e, em cada volta de um ciclo `for` sobre a lista interna, recebe mais a quantidade de um artigo. Pensa bem no valor com que deve começar, que é também a resposta à pergunta anterior.

Testa com duas linhas: mostra o total do inventário do teu programa, e depois cria um inventário novo, vazio, e mostra o total dele. Antes de executares, calcula à mão o total do primeiro, a partir das quantidades que os artigos têm nesse momento.

### 6.3 (opcional): os artigos esgotados

Se acabares as duas anteriores, escreve o método `esgotados()`, que devolve uma lista com os códigos dos artigos que têm quantidade 0. Se nenhum artigo estiver esgotado, devolve uma lista vazia.

Testa-o duas vezes: uma com o inventário tal como está, e outra depois de retirares todas as unidades de um dos artigos. Antes de cada teste, escreve a lista que esperas ver.

## Parte 7: atualizar o diagrama (5 min)

No papel, desenha de novo o diagrama de classes da secção 8 do caderno, agora com os métodos que acrescentaste na caixa `Inventario`. Depois responde numa frase: a linha entre as duas caixas, o losango e as multiplicidades mudaram com as operações novas? Porquê?

## Problemas frequentes neste laboratório

| O que aparece | O que costuma ser | Como resolver |
| --- | --- | --- |
| `NameError: name 'Artigo' is not defined` | A classe `Artigo` não está no ficheiro, ou ficou com outro nome | Confirma que copiaste a classe da parte 1 e que o nome começa por maiúscula |
| `AttributeError: 'Inventario' object has no attribute '_artigos'` | O nome da lista está escrito de maneiras diferentes no construtor e noutro método | Procura todas as linhas com `_artigo` e usa o mesmo nome em todas. As versões recentes do Python acrescentam à mensagem uma sugestão, como `Did you mean: '_artigo'?` |
| `AttributeError: 'Inventario' object has no attribute 'registar'` | O método ficou fora da classe, encostado à margem | Indenta todas as linhas do método quatro espaços, para ficarem dentro da classe |
| `TypeError: can only concatenate str (not "int") to str` | Foi passado um número como código, por exemplo `quantidade_de(7)`, e a mensagem de erro não conseguiu juntar o texto ao número | Os códigos são sempre textos, entre aspas: `quantidade_de("A07")` |
| O programa mostra menos linhas do que o caderno | Um `return` ou um `raise` com a indentação errada terminou um método antes do tempo | Compara a indentação de cada linha do método com o caderno |

## O que fica guardado

Guarda o ficheiro `inventario.py`, com as duas classes, os métodos da parte 6 e os testes, e a folha com as previsões, as respostas da parte 5 e o diagrama da parte 7. Entrega-os pelo meio indicado pelo professor.

![Rodapé](../imagens/rodape.png)

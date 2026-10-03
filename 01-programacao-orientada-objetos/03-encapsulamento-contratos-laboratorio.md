![Cabeçalho](../imagens/cabecalho.png)

# Laboratório: proteger a quantidade de um artigo

*M10 · Caderno 3 · Laboratório*

Este laboratório acompanha o [caderno 3](03-encapsulamento-contratos.md). Diz-te o que fazer, passo a passo, com o editor de Python aberto ao lado. As explicações do porquê estão no caderno: cada parte diz em que secção deves ter o caderno aberto. Conta com cerca de uma hora e meia, repartida pela aula, à medida que o professor for explicando cada secção.

No fim deves ter um ficheiro `artigo.py` com a classe final do caderno a funcionar, deves ter provocado de propósito, e lido, os erros de que o caderno fala, e deves ter mudado uma regra da classe num único sítio e visto essa mudança chegar a todas as operações.

## Antes de começar

Precisas do computador com o editor de Python que usas nas aulas, e de papel e caneta para as previsões.

Este laboratório dá por sabido o caderno 2 inteiro (classe, construtor, `self`, atributos e métodos) e os métodos get e set que já fizeste nas aulas. O resto (o atributo com sublinhado, `raise`, `try` e `except`, as propriedades e os contratos) é matéria nova do caderno 3, que vais vendo parte a parte. Se o professor disser, paras no fim da parte 6 e fazes as partes 7 e 8 noutra aula.

A forma de trabalhar é sempre a mesma. Antes de executares, escreves no papel o que esperas ver. Depois executas e comparas. Quando o resultado é diferente do que previste, explica a diferença antes de continuares: é essa explicação que mais te ensina. Executa sempre o ficheiro inteiro.

Em várias partes vais estragar o programa de propósito, para veres um erro acontecer. Faz a alteração pedida, observa, e desfaz a alteração antes de passares à parte seguinte. Se te perderes, cada parte diz qual é o programa completo do caderno de onde partir: basta copiá-lo outra vez.

## Parte 1: preparar o ficheiro (3 min)

1. Na pasta onde guardas os trabalhos de LP, cria uma pasta nova chamada `caderno-3`.
2. Dentro dela, cria um ficheiro chamado `artigo.py`. Vais usar sempre este ficheiro, substituindo o conteúdo de parte para parte.

## Parte 2: três estados impossíveis (10 min)

Tem aberta a secção 1 do caderno.

1. Copia para o ficheiro o programa completo da secção 1 e executa-o. Confirma que aparecem as três linhas que o caderno mostra, com -3, 2.5 e muitos.
2. Agora vais ver o "problema escondido" de que a secção fala. Acrescenta no fim do ficheiro a linha `caderno.retirar(1)`. Antes de executar, responde no papel: o que achas que vai acontecer, e porquê?
3. Executa. As três linhas aparecem, e depois o programa para com uma mensagem de erro de várias linhas, a que se chama **traceback** (a primeira linha começa por `Traceback`). A secção 7 do caderno ensina a lê-la. A última linha é esta:

```text
TypeError: unsupported operand type(s) for -: 'str' and 'int'
```

Em português: o Python não sabe fazer a operação `-` entre um texto (`str`) e um número inteiro (`int`).

4. Responde no papel: em que linha do programa principal aparece o erro? Em que linha está a causa? Quantas linhas acima da linha do erro está a causa? Relê o parágrafo da secção 1 do caderno que começa por "Há ainda um problema escondido" e diz, por palavras tuas, porque é que um estado inválido costuma rebentar longe do sítio onde foi criado.

## Parte 3: um set que verifica, mas não obriga (10 min)

Tem aberta a secção 5 do caderno.

1. Substitui o conteúdo do ficheiro pelo programa completo da secção 5. Prevê as três linhas e executa. Confirma que o -3 do set foi recusado e o da escrita direta não foi.
2. Acrescenta no fim estas duas linhas:

```python partial
resposta = caderno.set_quantidade(-1)
print("O set respondeu:", resposta)
```

3. Prevê o que aparece e executa. O set mostra "Valor recusado: -1" e depois aparece `O set respondeu: None`. `None` é um valor especial do Python que quer dizer "nada": é o que devolve um método que não tem `return`. O caderno volta a ele na secção 11. Responde no papel: com o que o set devolve, consegue o código que o chamou saber que o pedido foi recusado? É o segundo problema da secção 5.

## Parte 4: recusar a sério, com `raise` (10 min)

Tem abertas as secções 6 e 7 do caderno.

1. Substitui o conteúdo do ficheiro pelo programa completo da secção 7. Antes de executar, escreve no papel as linhas que esperas ver, incluindo a última linha do erro.
2. Executa. Aparece `Quantidade: 4` e depois um traceback que termina em `ValueError: A quantidade não pode ser negativa.`.
3. Lê o traceback de baixo para cima, como a secção 7 ensina, e responde no papel: qual é o tipo do erro e a mensagem? Em que método foi lançado? Que linha do programa principal fez o pedido? A linha `print("Esta linha já não é executada.")` apareceu? Porquê?
4. Agora, a ordem das verificações. No método `set_quantidade`, troca a ordem dos dois `if`, com o que está dentro de cada um, de modo que a verificação `valor < 0` venha primeiro. Substitui as linhas do programa principal por estas duas:

```python partial
caderno = Artigo("A01", "Caderno", 6)
caderno.set_quantidade("muitos")
```

5. Executa. A última linha do erro passa a ser:

```text
TypeError: '<' not supported between instances of 'str' and 'int'
```

Compara com a mensagem que o método teria dado com a ordem certa, "A quantidade tem de ser um número inteiro.". Qual das duas ajuda mais quem está a usar a classe? É o terceiro pormenor da secção 7.

6. Volta a pôr os dois `if` pela ordem do caderno.

## Parte 5: tratar a recusa com `try` e `except` (10 min)

Tem aberta a secção 8 do caderno.

1. Substitui o conteúdo do ficheiro pelo programa completo da secção 8. Prevê as duas linhas e executa.
2. Uma experiência sobre o tipo da exceção. Na linha `except ValueError as erro:`, troca `ValueError` por `TypeError`. Antes de executar, escreve no papel o que achas que vai acontecer.
3. Executa. O programa para com um traceback que termina em `ValueError: A quantidade não pode ser negativa.`, como se não houvesse `try`. Responde: porque é que o `except` não apanhou a exceção? O que diz a linha `except` sobre as exceções que apanha?
4. Volta a pôr `ValueError` no `except` e executa, para confirmares que o programa volta a continuar depois da recusa.

## Parte 6: a propriedade e os seus dois perigos (15 min)

Tem abertas as secções 9 e 10 do caderno.

1. Substitui o conteúdo do ficheiro pelo programa completo da secção 9. Prevê as cinco linhas e executa.
2. Primeiro perigo, o nome igual. Na última linha do setter, troca `self._quantidade = valor` por `self.quantidade = valor`, sem sublinhado. Antes de executar, relê, na secção 9, o parágrafo que começa por "O valor, esse, fica guardado em `_quantidade`" e escreve no papel o que achas que vai acontecer.
3. Executa. O programa para logo na criação do primeiro artigo. O traceback repete a mesma entrada, a da linha `self.quantidade = valor`, e termina assim (em algumas versões do Python, a última linha acrescenta mais umas palavras no fim):

```text
RecursionError: maximum recursion depth exceeded
```

Procura no traceback uma linha que diga quantas vezes a linha anterior se repetiu. Responde no papel: porque é que o setter se chama a si próprio? Porque é que o Python acaba por parar?

4. Volta a pôr o sublinhado e executa, para confirmares que tudo funciona.
5. Segundo perigo, o construtor que salta o setter. No construtor, troca `self.quantidade = quantidade` por `self._quantidade = quantidade`. Prevê o que vai acontecer à última linha que o programa mostrava, a da caneta com -5. Executa.

Agora o programa mostra só quatro linhas: a linha "Artigo não criado: ..." desapareceu, porque a caneta com -5 unidades foi criada sem que ninguém verificasse nada. É o caso da secção 10.

6. Volta a pôr o construtor como estava e executa.

## Parte 7: adicionar e retirar com contrato (10 min)

Tem abertas as secções 11 e 12 do caderno.

1. Substitui o conteúdo do ficheiro pelo programa completo do passo 6 da secção 12, com a classe final do caderno.
2. Copia para o papel só as três primeiras colunas da tabela do traço do passo 5, sem olhares para as outras duas, e preenche tu essas duas colunas. Depois executa e compara as seis linhas do programa com o teu traço.
3. Acrescenta no fim do ficheiro uma linha que chame `caderno.retirar(4)`, fora de qualquer `try`, e outra que mostre a quantidade do caderno. Prevê as duas coisas: se há erro e que quantidade fica. Executa.

Deves ver `0`: retirar todas as unidades que existem é aceite, e zero é um estado válido (secção 2, "Zero no estado e zero no pedido").

## Parte 8: mudar uma regra num só sítio, sozinho (20 min)

Na secção 3 do caderno lês que, se um dia o inventário passar a ter um limite máximo por artigo, "só é preciso mudar a classe". Vais comprová-lo.

### 8.1: um limite máximo

A regra nova é: a quantidade de um artigo não pode passar de 100 unidades. Pode ser 100, mas não 101.

1. Antes de mexer no código, decide e escreve no papel: em que método da classe vais escrever esta regra, e porquê? Em que posição, em relação às verificações que já lá estão? Que mensagem vais usar?
2. Escreve a regra. Não mudes mais nenhum método: nem o construtor, nem `adicionar`, nem `retirar`.
3. Substitui as linhas do programa principal por testes teus, cada um no seu `try` quando puder ser recusado, que mostrem estes quatro casos:
   - criar um artigo com 150 unidades;
   - a um caderno com 6 unidades, adicionar 95;
   - ao mesmo caderno, adicionar 94;
   - acertar a quantidade do caderno para 101.
4. Para cada caso, escreve antes de executar se vai ser aceite ou recusado, quem recusa (o construtor, `adicionar` ou o setter) e a quantidade do caderno depois. Executa e compara.
5. Responde numa frase: porque é que `adicionar` passou a respeitar o limite, se não lhe tocaste?

### 8.2 (opcional): perguntar se está esgotado

Se acabares a anterior, acrescenta à classe um método `esgotado()` que responde `True` se a quantidade for zero e `False` se não for. Escreve primeiro o contrato na docstring, com as quatro partes da secção 11: o que recebe, o que devolve, quando falha e o que acontece ao estado. Depois testa-o antes e depois de retirares todas as unidades de um artigo.

## Problemas frequentes neste laboratório

| O que aparece | O que costuma ser | Como resolver |
| --- | --- | --- |
| `IndentationError` | Uma linha colada com a indentação errada, ou um `if` sem nada indentado por baixo | Compara a indentação com o caderno, linha a linha |
| `NameError: name 'ValueErrror' is not defined`, ou o mesmo com outro nome parecido | O nome da exceção está mal escrito, por exemplo `ValueErrror` ou `valueError` | O nome escreve-se exatamente `ValueError`, com as duas maiúsculas |
| `AttributeError: 'Artigo' object has no attribute '_quantidade'` | O setter nunca guardou o valor: o construtor escreve num nome com um engano, como `self.quantiade`, ou o setter guarda noutro nome | O construtor escreve em `self.quantidade` e o setter guarda em `self._quantidade`, exatamente com estes nomes |
| `AttributeError: 'function' object has no attribute 'setter'` | Falta a linha `@property` antes do getter | Escreve `@property` na linha imediatamente antes do primeiro `def quantidade` |
| Valores inválidos aceites sem nenhuma recusa, como -3 | Falta a linha `@quantidade.setter`, e o setter deixou de ser um setter | Escreve `@quantidade.setter` na linha imediatamente antes do segundo `def quantidade` |
| O programa não para no erro que esperavas | Há um `try` a apanhar a exceção | Procura um `try` à volta da linha; é isso que faz o programa continuar |

## O que fica guardado

Guarda o ficheiro `artigo.py` com a parte 8 feita, e a folha com as previsões e as respostas das partes 2 a 8. Entrega-os pelo meio indicado pelo professor.

![Rodapé](../imagens/rodape.png)

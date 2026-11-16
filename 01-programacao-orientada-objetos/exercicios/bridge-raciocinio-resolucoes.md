![Cabeçalho](../../imagens/cabecalho.png)

# Ficha de recuperação: resolução

Aqui estão as respostas da [ficha de recuperação](bridge-raciocinio.md), exercício a exercício. Lê cada uma só depois de teres tentado o exercício sozinho.

A tua resposta pode ser diferente desta e estar certa. Em várias alíneas há mais do que uma resposta certa: quando é assim, a resolução diz e mostra uma delas. Nos traços dos algoritmos da ficha, os valores têm de ser iguais aos daqui.

## Exercício 1: Valores e condições

1. A tabela completa:

   | Pedido | A condição | Stock final |
   | ---: | --- | ---: |
   | 3 | Verdadeira | 5 |
   | 8 | Verdadeira | 0 |
   | 0 | Falsa | 8 |
   | -2 | Falsa | 8 |

   Com o pedido 8, as duas comparações são verdadeiras: `8 > 0`, e `8 <= 8`, porque `<=` aceita o igual. O stock fica 8 - 8 = 0. Com o pedido 0, `0 > 0` é falso. Basta uma comparação falsa para o `e` dar falso, e o stock fica 8. Com o pedido -2 acontece o mesmo, porque `-2 > 0` também é falso.

2. Com `pedido > 0` sozinho, um pedido maior do que o stock passa. Com o pedido 9, a condição dá verdadeira, e o stock fica 8 - 9 = -1. Um stock de -1 unidades é impossível. Falta a outra metade da regra: `pedido <= stock`.

3. A condição nova é `pedido >= 0 e pedido <= stock`. Com os pedidos de confirmação, e com o 0:

   | Pedido | Regra antiga | Regra nova |
   | ---: | --- | --- |
   | -1 | Recusado, stock 8 | Recusado, stock 8 |
   | 8 | Aceite, stock 0 | Aceite, stock 0 |
   | 9 | Recusado, stock 8 | Recusado, stock 8 |
   | 0 | Recusado, stock 8 | Aceite, stock 8 |

   O 0 é o único pedido que as duas regras decidem de maneira diferente: a nova aceita-o, e a antiga recusa-o. Mas o stock final é 8 nas duas, porque 8 - 0 = 8. Para se ver a diferença, o algoritmo tem de mostrar a decisão. Uma forma é escrever uma mensagem em cada caminho:

   ```text
   stock = 8
   pedido = 0
   Se pedido >= 0 e pedido <= stock
       stock = stock - pedido
       Escreve: "Aceite"
   Senão
       Escreve: "Recusado"
   Escreve: stock
   ```

   Com o pedido 0, este algoritmo mostra "Aceite" e depois 8. Com a condição antiga, mostraria "Recusado" e 8. Também podias guardar a decisão numa variável e escrevê-la no fim.

4. `stock` é um número inteiro. `"Pedido aceite"` é texto, porque está entre aspas. `pedido > 0` dá um valor lógico: verdadeiro ou falso. Em Python, são os tipos `int`, `str` e `bool`, e o valor lógico é `True` ou `False`.

5. Com `stock = pedido`, o stock fica igual ao pedido, e não ao que sobra. O pedido 4 esconde o erro: a versão certa dá 8 - 4 = 4, e a do colega também dá 4. O pedido 3 mostra-o: a versão certa dá 5, e a do colega dá 3. A correção é `stock = stock - pedido`, porque o stock novo depende do stock que havia. Há outros pedidos que servem. Os aceites, menos o 4, mostram o erro. Os recusados, como o 0 ou o 9, escondem-no.

Um pedido recusado esconde o erro porque a condição é falsa e a linha errada nem chega a ser executada. Um teste só mostra um erro quando passa pela linha errada e dá um resultado diferente do certo. E o stock final nem sempre mostra o que o `Se` decidiu: no pedido 0, aceitar e recusar deixam o mesmo stock.

## Exercício 2: Listas e ciclos

1. A tabela:

   | Passagem | Quantidade consultada | Total |
   | ---: | ---: | ---: |
   | 1 | 2 | 2 |
   | 2 | 5 | 7 |
   | 3 | 0 | 7 |

   O algoritmo mostra 7.

2. Uma resposta possível, com a lista `[2, 0, 5, 0]`:

   ```text
   quantidades = [2, 0, 5, 0]
   total = 0
   semStock = 0
   Para cada quantidade em quantidades
       total = total + quantidade
       Se quantidade == 0
           semStock = semStock + 1
   Escreve: total
   Escreve: semStock
   ```

   O contador recebe o primeiro valor, 0, antes do ciclo, na linha a seguir a `total = 0`. Dentro do ciclo, só soma 1 quando a quantidade é zero. Serve qualquer lista com dois zeros, em qualquer posição. O traço com esta lista:

   | Passagem | `quantidade` | `total` | `semStock` |
   | ---: | ---: | ---: | ---: |
   | 1 | 2 | 2 | 0 |
   | 2 | 0 | 2 | 1 |
   | 3 | 5 | 7 | 1 |
   | 4 | 0 | 7 | 2 |

   O algoritmo mostra 7 e 2.

3. Com `semStock = 0` no início de cada passagem, o contador volta a 0 antes de cada quantidade. Perde-se o que ele contou nas passagens anteriores. No fim, só diz se a última quantidade é zero: dá 1 ou 0. A versão do colega fica assim:

   ```text
   quantidades = [2, 0, 5, 0]
   total = 0
   Para cada quantidade em quantidades
       semStock = 0
       total = total + quantidade
       Se quantidade == 0
           semStock = semStock + 1
   Escreve: total
   Escreve: semStock
   ```

   Com a lista `[2, 0, 5, 0]`, o traço das duas versões prova o problema:

   | Passagem | `quantidade` | `semStock`, versão certa | `semStock`, versão do colega |
   | ---: | ---: | ---: | ---: |
   | 1 | 2 | 0 | 0 |
   | 2 | 0 | 1 | 1 |
   | 3 | 5 | 1 | 0 |
   | 4 | 0 | 2 | 1 |

   No fim, a versão certa mostra 2, e a do colega mostra 1. Outras listas também provam o problema: `[0, 0, 5]` dá 2 na versão certa e 0 na do colega.

A lista do exercício, `[2, 5, 0]`, não prova nada. Tem um só zero, no fim, e as duas versões dão 1. Uma lista sem zeros também não serve, porque as duas dão 0. Uma lista só prova um erro quando as duas versões dão resultados diferentes.

## Exercício 3: Funções, parâmetros e retorno

1. Os parâmetros são `numeroCaixas` e `unidadesPorCaixa`, os nomes que aparecem na definição da função. Os argumentos são 3 e 4, os valores que vão na chamada. O valor devolvido é 12, que fica guardado em `total`.
2. `total2 = unidadesEmCaixas(7, 3)`. O parâmetro `numeroCaixas` recebe 7, e `unidadesPorCaixa` recebe 3, porque os argumentos vão para os parâmetros pela mesma ordem. A função devolve 21.
3. Sim. O total calcula-se na linha da chamada e fica guardado em `total`. O `Escreve:` só mostra esse valor no ecrã. Sem ele, o programa faz a mesma conta, mas não mostra nada.
4. A versão do colega devolve `numeroCaixas * 4`. O teste `unidadesEmCaixas(7, 3)` deteta o erro: a versão certa devolve 21, e a do colega devolve 28. A correção é usar o parâmetro: `devolver numeroCaixas * unidadesPorCaixa`. Serve qualquer teste em que o segundo argumento não seja 4 e o primeiro não seja 0:

   | Teste | Versão certa | Versão do colega | Mostra o erro? |
   | --- | ---: | ---: | --- |
   | `(7, 3)` | 21 | 28 | Sim |
   | `(5, 2)` | 10 | 20 | Sim |
   | `(1, 3)` | 3 | 4 | Sim |
   | `(3, 4)` | 12 | 12 | Não |
   | `(2, 4)` | 8 | 8 | Não |
   | `(0, 2)` | 0 | 0 | Não |

A multiplicação esconde a ordem dos argumentos. `unidadesEmCaixas(3, 7)` também dá 21, mas quer dizer três caixas de sete unidades. Por isso a alínea 2 pede o valor de cada parâmetro. E devolver não é mostrar: a função entrega o valor à linha que a chamou, e só o `Escreve:` o põe no ecrã.

## Exercício 4: Ficheiros e organização

1. A árvore:

   ```text
   stock/
     instrucoes.txt
     programa.py
     dados/
       quantidades.txt
   ```

2. `dados/quantidades.txt`. No Windows, também se pode escrever com a barra invertida: `dados\quantidades.txt`.
3. Ler o ficheiro passa os valores que ele tem para a memória. Alterar muda os valores na memória, e o ficheiro fica como estava. Gravar escreve os valores novos no ficheiro. Se faltar o último passo, o ficheiro continua com os valores antigos, e a alteração perde-se quando o programa acaba.
4. A mensagem diz que o programa procurou `dados/quantidade.txt` e não o encontrou. Uma hipótese: o nome está errado. O programa procura `quantidade.txt`, e na árvore da alínea 1 o ficheiro chama-se `quantidades.txt`, com um s antes de `.txt`. Para a confirmar, listava a pasta `dados` e comparava o nome, letra a letra, com o da mensagem. Corrigia o nome no programa, ou o do ficheiro.

   Há outra causa possível, que dá a mesma mensagem: o programa ser executado a partir de outra pasta que não `stock`. O caminho `dados/quantidade.txt` parte da pasta de onde o programa corre. Para confirmar esta, via de que pasta o editor ou o terminal executa o programa. Corrigia executando-o a partir de `stock`. Nos dois casos, o algoritmo não muda.

Antes de mudares alguma coisa, lê a mensagem até ao fim. O caminho entre aspas simples, comparado com a árvore, já mostra o s que falta. E se corrigires só o nome, mas executares o programa a partir de outra pasta, a mensagem continua, agora com `quantidades.txt`.

## Exercício 5: Os pedidos de uma equipa

1. Uma resposta possível, em pseudocódigo:

   ```text
   pedidos = [2, 0, 3, 1]
   validos = 0
   soma = 0
   Para cada pedido em pedidos
       Se pedido é inteiro e pedido > 0
           validos = validos + 1
           soma = soma + pedido
   Escreve: validos
   Escreve: soma
   ```

   Os dois valores que se guardam, `validos` e `soma`, começam em 0 antes do ciclo. A condição tem as duas metades da regra: o pedido é inteiro, e é maior do que zero. Os mesmos passos escritos por palavras também estão certos. Em Python, pela tabela do [cenário](bridge-raciocinio.md#o-cenário) e com o `type(pedido) == int` da pista:

   ```python
   pedidos = [2, 0, 3, 1]
   validos = 0
   soma = 0
   for pedido in pedidos:
       if type(pedido) == int and pedido > 0:
           validos = validos + 1
           soma = soma + pedido
   print(validos)
   print(soma)
   ```

   Mostra 3 e 6.

2. O traço:

   | Pedido | Válido? | `validos` | `soma` |
   | ---: | --- | ---: | ---: |
   | 2 | Sim | 1 | 2 |
   | 0 | Não | 1 | 2 |
   | 3 | Sim | 2 | 5 |
   | 1 | Sim | 3 | 6 |

   No fim, o algoritmo mostra 3 e 6.

3. Por exemplo, `[4, -2, 1]`. O -2 não é válido. Somar só os válidos dá 4 + 1 = 5, e somar todos dá 4 - 2 + 1 = 3. Serve qualquer conjunto com um pedido inválido que não seja zero, como um negativo ou um com casas decimais. Os pedidos da equipa não servem, porque o único inválido é o 0, e somar 0 não muda a soma. Com eles, dá 6 das duas maneiras.

4. Os dois resultados: o número de pedidos válidos, 3, e a soma, 6. Amanhã, basta ler o ficheiro para os veres. Se gravares também os pedidos, podes refazer as contas para as confirmar.

Somar só os válidos quer dizer pôr a linha da soma dentro do `Se`, ao lado da que conta. Se a soma ficar fora do `Se`, o algoritmo soma todos os pedidos. Com os pedidos da equipa, nem se nota, e é por isso que a alínea 3 pede outros.

## Desafio 1: Uma função para a validade de um pedido

Uma resposta possível:

```text
Função pedidoValido(pedido)
    Se pedido é inteiro e pedido > 0
        devolver verdadeiro
    Senão
        devolver falso
```

A função tem um parâmetro, `pedido`. Recebe um só pedido, e não a lista toda. Devolve verdadeiro se o pedido for válido, e falso se não for. No ciclo do exercício 5, a condição passa a ser `Se pedidoValido(pedido)`. Também está certo devolver logo o valor da condição, numa linha só: `devolver pedido é inteiro e pedido > 0`.

Em Python, com o ciclo do exercício 5:

```python
def pedidoValido(pedido):
    """Diz se um pedido é válido, isto é, se é um número inteiro positivo.

    pedido: o número de unidades pedidas.
    Devolve True se o pedido for válido, e False se não for.
    """
    if type(pedido) == int and pedido > 0:
        return True
    else:
        return False


pedidos = [2, 0, 3, 1]
validos = 0
soma = 0
for pedido in pedidos:
    if pedidoValido(pedido):
        validos = validos + 1
        soma = soma + pedido
print(validos)
print(soma)
```

Mostra os mesmos 3 e 6 do exercício 5. Com os pedidos 2, 0, 3, 1, -2 e `1.5`, a função devolve `True`, `False`, `True`, `True`, `False` e `False`.

A função entrega o resultado com `devolver`, e não o mostra com `Escreve:`. Quem precisa do resultado é o `Se` do ciclo, e não o ecrã.

## Desafio 2: A condição do colega

Por exemplo, `[3, 1.5, 0, 2]`. O `1.5` é maior do que zero, por isso a condição do colega aceita-o, mas não é inteiro. O algoritmo do colega mostra 3 pedidos válidos e a soma `6.5`. Devia mostrar 2 pedidos válidos e a soma 5, só com o 3 e o 2. Serve qualquer conjunto com um pedido positivo com casas decimais, como `[0.5, 2]`: o colega mostra 2 e `2.5`, e devia mostrar 1 e 2.

Um pedido negativo não serve aqui. A condição do colega também o recusa, porque não é maior do que zero: com `[4, -2, 1]`, as duas versões mostram 2 e 5. A condição do colega só erra num pedido positivo que não é inteiro.

![Rodapé](../../imagens/rodape.png)

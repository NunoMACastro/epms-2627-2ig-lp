![Cabeçalho](../imagens/cabecalho.png)

# Ficha de exercícios: encapsulamento e contratos

*M10 · Caderno 3 · Ficha de exercícios*

Esta ficha acompanha o [caderno 3](03-encapsulamento-contratos.md). É para praticares sozinho, depois de estudares o caderno e de fazeres o [laboratório](03-encapsulamento-contratos-laboratorio.md). Conta com cerca de uma hora e cinco minutos para os seis exercícios, e mais dez minutos se fizeres o desafio opcional do fim.

Os exercícios da secção 13 do caderno, "Agora experimenta", continuam a ser teus e o professor diz quando os fazer. Esta ficha não os repete: traz exercícios mais curtos, cada um a treinar uma coisa só, do mais direto para o que pede uma pequena decisão tua.

Responde no caderno diário ou numa folha, com o número de cada exercício. Escreve sempre a previsão antes de executar. Entrega as respostas pelo meio indicado pelo professor.

## Exercício 1: estado válido e pedido válido (5 min)

Neste inventário, a quantidade de um artigo é um inteiro não negativo, e um pedido de retirada tem de ser um inteiro positivo que não passe do que existe.

1. Para cada valor, diz se seria uma quantidade válida para um artigo, isto é, um estado válido: `0`, `7`, `-1`, `3.5`, `"4"`.
2. Um artigo tem 5 unidades. Para cada pedido de retirada, diz se é válido: retirar `5`, retirar `0`, retirar `6`.
3. O zero aparece como válido numa das perguntas e como inválido na outra. Explica porquê, numa ou duas frases (secção 2 do caderno, "Zero no estado e zero no pedido").

## Exercício 2: verificar primeiro, alterar depois (10 min)

Três colegas escreveram três versões de um método `set_quantidade`. São excertos, sem o resto da classe. Nas três, o atributo interno chama-se `_quantidade` e o artigo começa com 6 unidades.

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

Para cada versão, o programa chama `set_quantidade(-3)` dentro de um `try` com `except ValueError`. Copia e completa a tabela, sem executar:

| Versão | A mensagem de recusa aparece? | Quem a mostra: o `except` ou o próprio método | Quantidade depois | O código que chamou fica a saber da recusa? |
| --- | --- | --- | ---: | --- |
| A | A completar | A completar | A completar | A completar |
| B | A completar | A completar | A completar | A completar |
| C | A completar | A completar | A completar | A completar |

Depois, diz qual das três é a única correta e resume numa frase a regra que as outras duas não cumprem.

## Exercício 3: ler um traceback (10 min)

Um colega executou a classe final do caderno 3 (a do passo 6 da secção 12) com este programa principal no fim do ficheiro:

```python partial
caneta = Artigo("A03", "Caneta", 4)
caneta.adicionar(2)
caneta.retirar(9)
print("Quantidade:", caneta.quantidade)
```

O Python mostrou isto. O caminho do ficheiro foi encurtado, e as linhas com `~` e `^` só aparecem em algumas versões do Python:

```text
Traceback (most recent call last):
  File ".../artigo.py", line 64, in <module>
    caneta.retirar(9)
    ~~~~~~~~~~~~~~^^^
  File ".../artigo.py", line 59, in retirar
    self.quantidade = self.quantidade - unidades
    ^^^^^^^^^^^^^^^
  File ".../artigo.py", line 26, in quantidade
    raise ValueError("A quantidade não pode ser negativa.")
ValueError: A quantidade não pode ser negativa.
```

1. Qual é o tipo do erro e a mensagem?
2. Que linha do programa principal fez o pedido que falhou? Indica o número e o código.
3. Em que método nasceu a exceção? Atenção: não é no `retirar`. Diz qual é e explica porque é que o traceback lhe chama `quantidade`.
4. A última linha do programa, a do `print`, foi executada? Que quantidade tinha a caneta no momento do erro, e que quantidade ficou guardada?

## Exercício 4: tratar recusas e continuar (10 min)

Usa a classe final do caderno 3, a do passo 6 da secção 12. Queremos um programa principal que:

- crie uma caneta com o código A03, o nome Caneta e 4 unidades;
- tente retirar 5 unidades;
- tente adicionar 2.5 unidades;
- tente retirar 4 unidades;
- mostre a quantidade final.

Cada pedido recusado deve mostrar uma linha a começar por `Recusado:`, seguida da mensagem da exceção, e o programa deve continuar para o pedido seguinte. Cada pedido aceite deve mostrar uma linha a começar por `Aceite:`, seguida da quantidade que ficou.

1. Antes de escrever o código, prevê: quais dos três pedidos são recusados, com que mensagem, e qual é a quantidade final?
2. Decide onde fica, em cada pedido, a linha do `Aceite:`, de modo que só apareça quando o pedido é aceite. Justifica a escolha com a secção 8 do caderno.
3. Escreve o programa principal, com um `try` e um `except` para cada pedido. Executa e compara com a tua previsão.

## Exercício 5: uma propriedade nova (20 min)

O responsável do armário quer saber quando é preciso encomendar material. Para isso, cada artigo passa a ter um **stock mínimo**: quando a quantidade fica abaixo desse número, é altura de encomendar.

As regras do stock mínimo são estas: é um número inteiro; não pode ser negativo; um artigo acabado de criar tem stock mínimo 0.

1. As regras já obrigam o setter a aceitar o 0: explica porquê, numa frase. Há uma decisão que as regras não tomam por ti: o stock mínimo pode ser maior do que a quantidade atual do artigo? Responde com uma frase de justificação, pensando para que serve o stock mínimo.
2. Na classe final do caderno 3, acrescenta uma propriedade `stock_minimo`, com getter e setter, que guarde o valor em `_stock_minimo` e recuse os valores inválidos com `ValueError`, pela mesma ordem de verificações da propriedade `quantidade`.
3. Acrescenta ao construtor a linha que dá ao artigo novo o stock mínimo 0. Escreve-a de maneira que o valor passe pelo setter (secção 10 do caderno).
4. Testa: cria um caderno com 6 unidades, mostra o stock mínimo inicial, acerta-o para 10, tenta acertá-lo para -1 e depois para 2.5, cada tentativa no seu `try`, e mostra no fim o stock mínimo e a quantidade.

## Exercício 6: encontrar o erro de um colega (10 min)

Um colega escreveu o construtor da classe final assim. É um excerto: para o experimentares, substitui o construtor da classe final do caderno 3 por este.

```python partial
    def __init__(self, codigo, nome, quantidade):
        """Cria o artigo (versão com erro)."""
        self.codigo = codigo
        self.nome = nome
        self._quantidade = quantidade
```

Para testar, criou um caderno com 6 unidades e escreveu `caderno.quantidade = -3` dentro de um `try`. Apareceu a recusa, e ele ficou convencido de que a sua classe nunca deixa existir uma quantidade inválida.

1. Escreve duas linhas de código que mostrem que o colega está enganado: uma que crie um artigo com uma quantidade inicial inválida e outra que mostre a quantidade que ficou guardada. Escolhe tu o valor inválido, mas não uses um número negativo, que é o caso que a secção 10 do caderno já mostra. Executa e mostra o resultado.
2. Explica o erro por palavras, usando a palavra setter.
3. Corrige o construtor, mudando uma única linha.

## Desafio opcional: uma quantidade verdadeira

Com a classe final do caderno 3, sem alterações:

1. Prevê o que acontece com estas linhas e depois executa-as:

```python partial
caderno = Artigo("A01", "Caderno", 6)
caderno.quantidade = True
print(caderno.quantidade)
caderno.adicionar(True)
print(caderno.quantidade)
```

2. O resultado surpreende quase toda a gente. Pesquisa ou experimenta o que dá `isinstance(True, int)` e `True + 1`, e explica o que viste.
3. Propõe uma alteração ao setter que recuse `True` e `False` como quantidade. Depois verifica: com essa alteração, `caderno.adicionar(True)` passa a ser recusado? Se não passar, explica porquê e diz em que outros sítios da classe a mesma verificação faria falta.

## Antes de entregares

Revê as tuas respostas e confirma que em cada previsão escreveste o raciocínio, e não só o resultado. Indica também um ponto desta ficha que ainda não consegues explicar sem voltar ao caderno: é por aí que deves começar a próxima revisão.

![Rodapé](../imagens/rodape.png)

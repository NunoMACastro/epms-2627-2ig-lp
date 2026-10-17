![Cabeçalho](../imagens/cabecalho.png)

# Ficha de exercícios: Encapsulamento e contratos

Ficha do tema Encapsulamento e contratos, do módulo M10, Introdução à Programação Orientada por Objetos. Praticas, em exercícios curtos, a diferença entre um estado válido e um pedido válido e a regra "verificar primeiro, alterar depois". Praticas também a leitura de uma mensagem de erro, o `try` e o `except`, uma propriedade nova e a procura de um erro num setter. Fazes sozinho, ao teu ritmo: o que não acabares na aula, acabas em casa ou na aula seguinte.

## O que precisas de saber

O [guia do tema](03-encapsulamento-contratos.md) e o [laboratório](03-encapsulamento-contratos-laboratorio.md). Cada exercício diz em que secção do guia está a ideia que usa.

## Como trabalhar

Faz os exercícios 1 a 6 pela ordem. São a parte obrigatória, e cada um treina uma coisa só, do mais direto para o que pede uma pequena decisão tua. O desafio opcional é para quem acabar. Os exercícios de "Para ires mais longe" são mais longos e servem para aprofundar: fazes os que quiseres, ou os que o professor indicar.

Responde no caderno diário ou numa folha, com o número de cada exercício. Nos exercícios com código, escreve a previsão antes de executar: é a previsão, e não a execução, que mostra o que percebeste. Se a execução der outra coisa, procura a explicação em vez de mudar a previsão. Entrega as respostas pelo meio indicado pelo professor.

## O cenário

Quase todos os exercícios usam a classe `Artigo` final do guia: a do programa do passo 6 do exemplo guiado, em "Exemplo guiado: construir o método retirar". É a mesma classe do ficheiro da paragem 7 do laboratório. Tem a propriedade `quantidade`, com getter e setter, e os métodos `adicionar` e `retirar`, com contrato.

Os blocos de código dos exercícios são excertos e não correm sozinhos. Para executar um excerto, copia esse programa completo e substitui as linhas que vêm depois da classe (a partir de `caderno = ...`) pelas linhas do excerto. Quando um excerto substitui um método, o enunciado diz qual.

## Exercício 1: Estado válido e pedido válido

Neste inventário, a quantidade de um artigo é um inteiro não negativo, e um pedido de retirada tem de ser um inteiro positivo que não passe do que existe.

1. Para cada valor, diz se seria uma quantidade válida para um artigo, isto é, um estado válido: `0`, `7`, `-1`, `3.5`, `"4"`.
2. Um artigo tem 5 unidades. Para cada pedido de retirada, diz se é válido: retirar `5`, retirar `0`, retirar `6`.
3. O zero aparece como válido numa das perguntas e como inválido na outra. Explica porquê, numa ou duas frases ("Zero no estado e zero no pedido", no guia).

## Exercício 2: Verificar primeiro, alterar depois

Três colegas escreveram três versões de um método `set_quantidade`. São excertos, sem o resto da classe. Nas três, o atributo interno chama-se `_quantidade`, e o artigo começa com 6 unidades.

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

Depois, diz qual das três cumpre a regra "verificar primeiro, alterar depois" ("Recusar a sério: `ValueError` e `raise`", no guia). Explica numa frase o que falta a cada uma das outras duas.

## Exercício 3: Ler uma mensagem de erro

Um colega executou a classe final com este programa principal no fim do ficheiro. Para ler a mensagem, usa o que o guia diz em "Recusar a sério: `ValueError` e `raise`".

```python partial
caneta = Artigo("A03", "Caneta", 4)
caneta.adicionar(2)
caneta.retirar(9)
print("Quantidade:", caneta.quantidade)
```

O Python mostrou isto. O caminho do ficheiro foi encurtado, e as linhas com `~` e `^` só aparecem a partir do Python 3.11:

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

1. Qual é o tipo do erro, e qual é a mensagem?
2. Que linha do programa principal fez o pedido que falhou? Indica o número e o código.
3. Em que método nasceu a exceção? Explica porque é que a mensagem lhe chama `quantidade`.
4. A última linha do programa, a do `print`, foi executada? Que quantidade tinha a caneta no momento do erro, e que quantidade ficou guardada?

## Exercício 4: Tratar recusas e continuar

Queremos um programa principal, depois da classe final, que:

- crie uma caneta com o código A03, o nome Caneta e 4 unidades;
- tente retirar 5 unidades;
- tente adicionar 2.5 unidades;
- tente retirar 4 unidades;
- mostre a quantidade final.

Cada pedido recusado deve mostrar uma linha a começar por `Recusado:`, seguida da mensagem da exceção, e o programa deve continuar para o pedido seguinte. Cada pedido aceite deve mostrar uma linha a começar por `Aceite:`, seguida da quantidade que ficou.

1. Antes de escrever o código, prevê: quais dos três pedidos são recusados, com que mensagem, e qual é a quantidade final?
2. Decide onde fica, em cada pedido, a linha do `Aceite:`, de modo que só apareça quando o pedido é aceite. Justifica a escolha com o que o guia diz em "Tratar a recusa: `try` e `except`".
3. Escreve o programa principal, com um `try` e um `except` para cada pedido. Executa e compara com a tua previsão.

## Exercício 5: Uma propriedade nova

O responsável do armário quer saber quando é preciso encomendar material. Para isso, cada artigo passa a ter um **stock mínimo**: quando a quantidade fica abaixo desse número, é altura de encomendar.

As regras do stock mínimo são estas: é um número inteiro; não pode ser negativo; um artigo acabado de criar tem stock mínimo 0.

1. As regras já obrigam o setter a aceitar o 0: explica porquê, numa frase. Há uma decisão que as regras não tomam por ti: o stock mínimo pode ser maior do que a quantidade atual do artigo? Responde com uma frase de justificação, a pensar para que serve o stock mínimo.
2. Na classe final, acrescenta uma propriedade `stock_minimo`, com getter e setter. A propriedade guarda o valor em `_stock_minimo` e recusa os valores inválidos com `ValueError`, pela mesma ordem de verificações da propriedade `quantidade`. Escreve na docstring do setter o contrato, com as quatro partes: o que recebe, o que devolve, quando falha e o que acontece ao estado em cada caso.
3. Acrescenta ao construtor a linha que dá ao artigo novo o stock mínimo 0. Escreve-a de maneira que o valor passe pelo setter ("O construtor também passa pelo setter", no guia).
4. Testa a propriedade. Cria um caderno com 6 unidades e mostra o stock mínimo inicial. Acerta-o para 10, e depois tenta acertá-lo para -1 e para 2.5, cada tentativa no seu `try`. No fim, mostra o stock mínimo e a quantidade.

## Exercício 6: O erro de um colega no setter

Um colega escreveu o setter da classe final assim. É um excerto: para o experimentares, substitui o setter da classe final por este, com a linha do `@quantidade.setter`.

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

1. Escreve um teste que mostre que o colega está enganado. O teste faz, dentro de um `try`, um pedido que as regras do inventário aceitam e que este setter recusa. No fim, uma linha mostra a quantidade. Escolhe tu o pedido. Executa e mostra o resultado.
2. Explica o erro por palavras, usando as palavras "estado" e "pedido" ("As regras que devem continuar verdadeiras", no guia).
3. Corrige o setter, mudando uma única linha.

## Apoio

- Exercício 1: para cada valor, escreve ao lado a regra que usaste para decidir. Na pergunta 3, compara as regras que escreveste.
- Exercício 2: para cada versão, segue a chamada linha a linha e anota, depois de cada linha, o valor de `_quantidade` e se o método já parou.
- Exercício 3: lê a mensagem de baixo para cima, como no guia. A entrada de baixo é a do sítio onde a exceção nasceu.
- Exercício 4: faz primeiro o traço dos três pedidos, com a quantidade depois de cada um. Só depois escreves o código.
- Exercício 5: parte da propriedade `quantidade` da classe final e muda só o que diz respeito ao stock mínimo: os nomes e as mensagens. Para o contrato, segue a forma das docstrings do `adicionar` e do `retirar`.
- Exercício 6: relê a regra da quantidade em "As regras que devem continuar verdadeiras", no guia, e lê a condição do colega como uma frase.
- Desafio: experimenta no Python as duas expressões da alínea 2 antes de as explicares.
- Mais longe 1: faz um caso de cada vez, a partir do artigo acabado de criar, e escreve para cada um a regra que decide.
- Mais longe 2: segue o pedido de 9 linha a linha, dentro do método e no programa do colega, e anota que linhas são executadas.
- Mais longe 3: escreve o contrato antes do código. As decisões da alínea 2 entram no contrato, na parte que diz quando a propriedade falha.

## Desafio opcional

Uma quantidade verdadeira. Com a classe final, sem alterações:

1. Prevê o que acontece com estas linhas, e depois executa-as:

   ```python partial
   caderno = Artigo("A01", "Caderno", 6)
   caderno.quantidade = True
   print(caderno.quantidade)
   caderno.adicionar(True)
   print(caderno.quantidade)
   ```

2. Experimenta o que dá `isinstance(True, int)` e `True + 1`, e explica o que viste.
3. Propõe uma alteração ao setter que recuse `True` e `False` como quantidade. Depois verifica: com essa alteração, `caderno.adicionar(True)` passa a ser recusado? Para verificares, tira a linha `caderno.quantidade = True`, ou põe-na num `try`. Se não passar, explica porquê e diz em que outros sítios da classe a mesma verificação faria falta.

## Para ires mais longe

### Mais longe 1: Decidir antes de executar

Cada linha da tabela é um caso separado, que começa com um artigo acabado de criar: `artigo = Artigo("A07", "Marcador", 5)`. A última linha não usa esse artigo: cria um artigo novo.

| Instrução | Aceite ou recusada | Quem recusa: o método, o setter ou ninguém | Quantidade depois | Mensagem, se houver |
| --- | --- | --- | ---: | --- |
| `artigo.retirar(5)` | A completar | A completar | A completar | A completar |
| `artigo.adicionar(1.5)` | A completar | A completar | A completar | A completar |
| `artigo.quantidade = 7.0` | A completar | A completar | A completar | A completar |
| `artigo.quantidade = 0` | A completar | A completar | A completar | A completar |
| `artigo.retirar(2.0)` | A completar | A completar | A completar | A completar |
| `Artigo("A09", "Agrafador", 0)` | A completar | A completar | A completar | A completar |

Preenche a tabela primeiro, e só depois escreve um programa que confirme cada caso, com um `try` e um `except` para cada instrução. Por fim, responde: 7.0 e 2.0 têm o valor de números inteiros, mas o Python recusa-os. Achas que a regra devia aceitá-los? Justifica a tua posição, a pensar no que o inventário guarda.

### Mais longe 2: Uma recusa que fica pelo caminho

Um colega escreveu esta versão do `retirar`. É um excerto: para a experimentares, substitui o `retirar` da classe final por este. O `except ValueError:`, sem o `as`, apanha a exceção sem lhe dar um nome.

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

Para a testar, o colega escreveu este programa principal, como no exercício 4:

```python partial
caderno = Artigo("A01", "Caderno", 6)

try:
    caderno.retirar(9)
    print("Aceite:", caderno.quantidade)
except ValueError as erro:
    print("Recusado:", erro)

print("Quantidade:", caderno.quantidade)
```

Viu a mensagem "Não há unidades suficientes." e ficou convencido de que o método funciona.

1. Prevê as linhas que aparecem no ecrã. Depois executa e compara.
2. Que quantidade ficou guardada no caderno? É válida?
3. Das duas linhas do `try` do colega, a do `Aceite:` e a do `Recusado:`, qual apareceu? Porquê, se faltavam unidades?
4. Explica, por palavras, porque é que esta versão não cumpre o contrato do `retirar` do guia, a pensar em quem fez o pedido.
5. Corrige o método, e confirma que o programa do colega passa a mostrar a recusa.

### Mais longe 3: O nome também tem regras

No inventário, o nome de um artigo não pode ser vazio. Com a classe final, `Artigo("A08", "", 3)` é aceite sem problemas.

1. Escreve o contrato de uma propriedade `nome`, com as quatro partes de "Adicionar: uma operação com contrato", no guia. São estas: o que recebe, o que devolve quem a consulta, quando falha e o que acontece ao estado em cada caso.
2. Antes de escreveres o contrato, tens de tomar duas decisões que o guia não tomou por ti. Um nome só com espaços, como `"   "`, conta como vazio? E se alguém passar um número como nome, por exemplo `123`? Decide e justifica cada escolha numa frase.
3. Escreve a propriedade `nome`, com getter e setter, a guardar o valor em `_nome`, e faz o construtor passar pelo setter. Se decidires que um nome só com espaços é vazio, vai-te ser útil o método `strip` dos textos. Devolve o texto sem os espaços do início e do fim: `"   Caneta ".strip()` dá `"Caneta"`. Em inglês, *strip* quer dizer tirar.
4. Testa a tua classe com um nome válido, com um nome vazio e com o caso da tua decisão na alínea 2. Em cada caso, mostra a mensagem ou o nome guardado.
5. Achas que o código do artigo também devia ser uma propriedade protegida? Com que regra? Pensa no que um artigo sozinho sabe, e no que só um inventário, que conhece todos os artigos, poderia saber.

## Critérios de conclusão

- Fizeste os exercícios 1 a 6, com as previsões escritas antes de executar.
- Em cada exercício com código, comparaste a previsão com o que apareceu e explicaste as diferenças.
- Em cada recusa que experimentaste, confirmaste também a quantidade que ficou, e não só a mensagem.
- A propriedade `stock_minimo` do exercício 5 passa nos quatro testes da alínea 4, e o setter do exercício 6 está corrigido numa só linha.

## Autoavaliação

1. Em que exercício a tua previsão falhou, e o que percebeste com a diferença?
2. O que achaste mais difícil: separar o estado do pedido, ler a mensagem de erro, ou decidir onde fica cada linha no `try`?
3. Que ponto desta ficha ainda não consegues explicar sem voltar ao guia? É por aí que começas a próxima revisão.

![Rodapé](../imagens/rodape.png)

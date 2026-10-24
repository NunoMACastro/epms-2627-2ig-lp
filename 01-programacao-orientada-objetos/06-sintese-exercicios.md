![Cabeçalho](../imagens/cabecalho.png)

# Ficha de exercícios: Síntese

Ficha do tema Síntese, do módulo M10, Introdução à Programação Orientada por Objetos. Praticas, com o inventário do guia, três tarefas: quem responde a cada pedido, um método novo com contrato e o erro de um colega. Fazes sozinho, ao teu ritmo: o que não acabares na aula, acabas em casa ou na aula seguinte.

## O que precisas de saber

O [guia do tema](06-sintese.md) e o [laboratório](06-sintese-laboratorio.md). Cada exercício usa sobretudo estas partes do guia:

- Exercício 1: o traço do passo 5 do exemplo guiado, e "Encapsulamento no programa".
- Exercício 2: "Como o inventário encontra um artigo", em "O inventário no programa: composição e procura pelo código", e o contrato do passo 3 do exemplo guiado.
- Exercício 3: "Classes e objetos no programa", o passo 4 do exemplo guiado e os três tipos de erro, em "O programa de partida".
- Desafio: "Composição: o inventário cria os seus artigos", em "O inventário no programa: composição e procura pelo código".
- Mais longe 1: "Encapsulamento no programa" e "Como o inventário encontra um artigo".

## Como trabalhar

Faz os exercícios 1 a 3 pela ordem. São a parte obrigatória. Cada um treina uma coisa só e pede uma pequena decisão que o exemplo guiado não tomou por ti. O desafio opcional é para quem acabar. O exercício de "Para ires mais longe" tem casos que enganam, para quem quer treinar mais.

Responde no caderno diário ou numa folha, com o número de cada exercício. Escreve sempre a tua previsão antes de executar. Se a execução der outra coisa, procura a explicação em vez de mudar a previsão. Entrega as respostas pelo meio indicado pelo professor.

## O cenário

Todos os exercícios usam o programa completo do passo 6 do exemplo guiado, o do inventário com o método `acertar` já escrito. Tem a classe `Artigo`, com a propriedade `quantidade` e os métodos `adicionar` e `retirar`, e a classe `Inventario`, com os métodos `registar`, `quantidade_de`, `retirar` e `acertar`.

Os blocos de código dos exercícios são excertos e não correm sozinhos. Para executar um excerto, copia o programa do passo 6. Depois substitui as linhas que vêm depois das classes, a partir de `inventario = Inventario()`, pelas linhas do excerto. Quando um exercício acrescenta ou troca um método, o enunciado diz qual.

## Exercício 1: Prever quem responde a cada pedido

Excerto para colocar depois das classes do programa do passo 6:

```python partial
inventario = Inventario()
inventario.registar("A01", "Caderno", 6)
inventario.registar("A02", "Pasta", 2)

try:
    inventario.acertar("A01", 0)
    print("Pedido 1: aceite")
except ValueError as erro:
    print("Pedido 1:", erro)

try:
    inventario.retirar("A01", 1)
    print("Pedido 2: aceite")
except ValueError as erro:
    print("Pedido 2:", erro)

try:
    inventario.acertar("A03", 4)
    print("Pedido 3: aceite")
except ValueError as erro:
    print("Pedido 3:", erro)

try:
    inventario.retirar("A02", 0)
    print("Pedido 4: aceite")
except ValueError as erro:
    print("Pedido 4:", erro)

print("A01:", inventario.quantidade_de("A01"))
print("A02:", inventario.quantidade_de("A02"))
```

1. Sem executar, copia e completa a tabela. Cada linha começa no estado deixado pela anterior. Na coluna "Quem responde", escolhe entre o método `_procurar` do inventário, o método `retirar` do artigo, o setter do artigo ou ninguém, se o pedido for aceite.

   | Pedido | Quem responde | Mensagem mostrada | A01 depois | A02 depois |
   | --- | --- | --- | ---: | ---: |
   | `acertar("A01", 0)` | A completar | A completar | A completar | A completar |
   | `retirar("A01", 1)` | A completar | A completar | A completar | A completar |
   | `acertar("A03", 4)` | A completar | A completar | A completar | A completar |
   | `retirar("A02", 0)` | A completar | A completar | A completar | A completar |

2. Os pedidos 1 e 4 têm, os dois, um zero. Explica, em duas frases, porque é que têm respostas diferentes.
3. Executa e compara as seis linhas do ecrã com a tua tabela. Se alguma for diferente, escreve o que tinhas pensado e onde estava o engano.

## Exercício 2: Perguntar ao inventário se um código existe

Antes de registar um artigo novo, a pessoa que trata do inventário quer poder perguntar se um código já está a ser usado, sem provocar nenhuma recusa. Acrescenta à classe `Inventario` do programa do passo 6 um método `existe(codigo)`, com este contrato:

- recebe um código;
- devolve `True` se o inventário tiver um artigo com esse código, e `False` se não tiver;
- nunca falha e não muda nada.

1. Escreve o método dentro da classe `Inventario`, com uma docstring que diga o contrato.
2. Testa-o com estas linhas, que substituem as que vêm depois das classes. Antes de executares, escreve as quatro linhas que esperas ver.

   ```python partial
   inventario = Inventario()
   inventario.registar("A01", "Caderno", 6)
   inventario.registar("A02", "Pasta", 2)

   print(inventario.existe("A01"))
   print(inventario.existe("A02"))
   print(inventario.existe("A07"))

   vazio = Inventario()
   print(vazio.existe("A01"))
   ```

3. Explica, em duas frases, como é que o teu método chega a cada uma das duas respostas, `True` e `False`.

## Exercício 3: Encontrar o erro de um colega

Um colega escreveu esta versão do método `acertar`. É um excerto. Para a experimentares, substitui o `acertar` da classe `Inventario` do programa do passo 6 por este:

```python partial
    def acertar(self, codigo, nova_quantidade):
        """Acerta a quantidade do artigo com este código (versão do colega)."""
        artigo = self._procurar(codigo)
        self.quantidade = nova_quantidade
```

Depois substitui as linhas que vêm depois das classes por estas:

```python partial
inventario = Inventario()
inventario.registar("A01", "Caderno", 6)
inventario.registar("A02", "Pasta", 2)

inventario.acertar("A02", 5)
print("A02 depois de acertar para 5:", inventario.quantidade_de("A02"))

try:
    inventario.acertar("A01", -1)
    print("Acerto de A01 para -1: aceite")
except ValueError as erro:
    print("Acerto de A01 para -1: recusado:", erro)
print("A01 no fim:", inventario.quantidade_de("A01"))
```

1. Antes de executares, escreve as três linhas que o programa devia mostrar se o método estivesse certo, como no passo 6.
2. Executa com a versão do colega e assinala as linhas que são diferentes da tua resposta à alínea 1. Diz também que tipo de erro é: de escrita, de execução ou de lógica.
3. Explica o erro, por palavras, em duas ou três frases. A tua explicação tem de dizer para que objeto aponta o `self` dentro deste método, e o que acontece, por isso, ao valor 5 e ao valor -1.
4. Corrige o método, mudando uma única linha. Depois volta a correr o programa inteiro, confirma que as três linhas passam a ser as da alínea 1 e diz o que mudou em cada uma.

## Apoio

- Exercício 1: faz o traço como no passo 5 do exemplo guiado, um pedido de cada vez, a partir do estado deixado pelo anterior. Para cada pedido, relê o método que ele chama e diz que pergunta faz cada `if`.
- Exercício 2: escreve primeiro o método por palavras: o que faz quando encontra o código, e o que faz quando não o encontra. Depois confirma as quatro linhas do teste, uma a uma, com essas palavras.
- Exercício 3: segue o pedido `acertar("A02", 5)` linha a linha, como no passo 7 do exemplo guiado. Depois de cada linha, escreve que objeto mudou, se algum mudou.
- Desafio: responde às duas perguntas que decidem olhando para o código, e não para os nomes das classes. Procura as linhas onde o artigo é criado e as linhas que o guardam.
- Mais longe 1: para cada pedido, segue primeiro `_procurar` com o código tal como está escrito, e só depois o setter com o valor.

## Desafio opcional

Artigos criados fora do inventário. Um colega propõe acrescentar à classe `Inventario` do programa do passo 6 este método, para poder juntar ao inventário artigos que já existem:

```python partial
    def acrescentar(self, artigo):
        """Junta ao inventário um artigo criado fora dele (proposta do colega)."""
        self._artigos.append(artigo)
```

E experimenta-o com estas linhas, que substituem as que vêm depois das classes:

```python partial
caderno = Artigo("A01", "Caderno", 6)

sala_12 = Inventario()
sala_14 = Inventario()
sala_12.acrescentar(caderno)
sala_14.acrescentar(caderno)

sala_12.retirar("A01", 2)
print("Sala 12, A01:", sala_12.quantidade_de("A01"))
print("Sala 14, A01:", sala_14.quantidade_de("A01"))
```

1. Antes de executares, escreve as duas linhas que esperas ver. Depois executa e compara.
2. Com o método `acrescentar`, a relação entre `Inventario` e `Artigo` passa a ser uma composição ou uma agregação? Responde com as duas perguntas que decidem, de "Dois graus de "tem": composição e agregação", no guia 04.
3. Explica porque é que a sala 14 mostra a quantidade que mostra, se ninguém lhe pediu nenhuma retirada.
4. Pensa no inventário de uma sala, em que as 6 unidades de A01 são as que estão naquela sala. Qual das duas versões te parece mais adequada: a do `registar` ou a do `acrescentar`? Justifica em duas frases.

## Para ires mais longe

Esta parte é opcional, para quem acabou os três exercícios e quer treinar com casos que enganam.

### Mais longe 1: Pedidos que enganam

Cada linha da tabela é um caso separado, num inventário acabado de criar com A01 a 6 e A02 a 2, como no exercício 1. Para cada pedido, escreve quem responde, a mensagem que aparece, e se o programa continua ou para. Depois confirma, escrevendo cada pedido dentro de um `try` com `except ValueError as erro`.

| Pedido | Quem responde | Mensagem | O programa continua ou para? |
| --- | --- | --- | --- |
| `acertar("A01", "7")` | A completar | A completar | A completar |
| `acertar("a01", 7)` | A completar | A completar | A completar |
| `acertar("A01", 7.0)` | A completar | A completar | A completar |
| `acertar(1, 7)` | A completar | A completar | A completar |

Um dos pedidos não acaba como os outros. Se o programa parar, lê a última linha da mensagem de erro e explica porque é que o `except ValueError` não a apanhou.

## Critérios de conclusão

- Fizeste os exercícios 1 a 3.
- No exercício 1, a tabela foi feita antes de executar, e cada linha parte do estado deixado pela anterior.
- No exercício 2, o método tem a docstring com o contrato, e as quatro linhas do teste batem com a tua previsão, incluindo a do inventário vazio.
- No exercício 3, a explicação diz para que objeto aponta o `self`, e voltaste a correr o programa inteiro depois da correção.

## Autoavaliação

1. Em que pedido do exercício 1 hesitaste mais, e o que te fez decidir?
2. No exercício 2, o que foi mais difícil: escrever o método ou escolher o que ele faz quando não encontra o código?
3. Que ponto desta ficha ainda não consegues explicar sem voltar ao guia? É por aí que começas a próxima revisão.

![Rodapé](../imagens/rodape.png)

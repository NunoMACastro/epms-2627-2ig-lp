![Cabeçalho](../../imagens/cabecalho.png)

# Ficha de exercícios: Herança e polimorfismo

Praticas a leitura de uma hierarquia de classes, a regra de procura num ciclo, a escolha entre herança e composição e a verificação do contrato de uma variante. Escreves também o contrato de uma classe abstrata, por palavras, e duas classes concretas que o cumprem. Os exercícios 1 a 6 são a parte obrigatória. Cada um faz-se num script novo, na pasta `tema-05` do laboratório, com o nome que o enunciado lhe dá. O que respondes por palavras vai para um comentário no fim desse script. Os seis scripts entregam-se como o professor indicar, com os dos desafios, se os fizeste. Para rever: o [guia do tema](../05-heranca-polimorfismo.md) e o [laboratório](../laboratorios/05-heranca-polimorfismo-laboratorio.md).

## Exercício 1: Ler uma hierarquia

Esta árvore de especialização é do programa de uma loja de instrumentos musicais:

```text
Instrumento
├── Tambor
└── InstrumentoDeCorda
    ├── Guitarra
    └── Violino
```

Cria o script `instrumentos.py` e responde só com comentários.

1. Indica a classe base de `Tambor`, a de `Guitarra` e a de `InstrumentoDeCorda`.
2. Há uma classe que é, ao mesmo tempo, derivada de uma e base de outras. Qual?
3. Escreve duas frases verdadeiras com "é um". Uma delas tem de saltar um nível da árvore, de baixo até ao topo.
4. A frase "um tambor é um instrumento de corda" é verdadeira? O que diz a árvore sobre a relação entre `Tambor` e `InstrumentoDeCorda`?

Rever: [Especialização: do geral para o particular](../05-heranca-polimorfismo.md#especialização-do-geral-para-o-particular).

<details>
<summary>Pista</summary>

Lê a árvore de baixo para cima, uma ligação de cada vez, e forma a frase "é um" de cada ligação. A classe base de uma classe é a que ficaria entre parênteses na linha `class` dela.

</details>

## Exercício 2: Prever o que o ciclo mostra

Este programa completo junta numa lista as etiquetas das prateleiras do armário e pede a cada uma o seu conteúdo:

```python
# Ficha 05, exercício 2: as etiquetas das prateleiras do armário.

class Etiqueta:
    """Etiqueta para colar numa prateleira do armário."""

    def __init__(self, texto):
        """Guarda o texto da etiqueta."""
        self.texto = texto

    def conteudo(self):
        """Devolve o texto que vai impresso na etiqueta."""
        return self.texto

    def largura(self):
        """Devolve o número de carateres da etiqueta impressa."""
        return len(self.conteudo())


class EtiquetaMaiuscula(Etiqueta):
    """Etiqueta com o texto todo em maiúsculas."""

    def conteudo(self):
        """Devolve o texto em maiúsculas."""
        return self.texto.upper()


class EtiquetaComMoldura(Etiqueta):
    """Etiqueta com o texto entre parênteses retos."""

    def conteudo(self):
        """Devolve o texto entre parênteses retos."""
        return "[" + self.texto + "]"


etiquetas = [
    Etiqueta("Cadernos"),
    EtiquetaMaiuscula("Pastas"),
    EtiquetaComMoldura("Canetas"),
]

for etiqueta in etiquetas:
    print(etiqueta.conteudo())
```

Copia-o para o script `etiquetas.py`, mas não o executes logo. Descobre primeiro, de cabeça, as três linhas que o ciclo vai mostrar, e só depois executa, para confirmares. Num comentário no fim do script, diz, para cada volta, de que classe é o objeto e em que classe o Python encontra o `conteudo`.

Rever: [Uma variante que redefine um método](../05-heranca-polimorfismo.md#uma-variante-que-redefine-um-método) e [O mesmo pedido a todas as variantes](../05-heranca-polimorfismo.md#o-mesmo-pedido-a-todas-as-variantes).

<details>
<summary>Pista</summary>

Em cada volta, faz as duas perguntas da regra de procura. De que classe é o objeto? Essa classe escreve o `conteudo`?

</details>

## Exercício 3: Herança ou composição

Cria o script `heranca_ou_composicao.py` e responde só com comentários. Para cada par, escreve a frase verdadeira, "A é um B" ou "A tem B", e diz se a relação se escreve com herança ou com composição. Aqui, como no guia, a composição é qualquer relação "tem". Se a frase verdadeira não pedir nenhuma das duas, diz porquê.

1. `Comboio` e `Carruagem`.
2. `ChefeFinal` e `Inimigo`, num jogo de computador.
3. `Hotel` e `Quarto`.
4. `RelogioInteligente` e `Relogio`.
5. `EspadaDeOuro` e `Espada`, num jogo em que todas as espadas fazem o mesmo e só mudam no nome e no dano.

Rever: [Duas maneiras de reaproveitar](../05-heranca-polimorfismo.md#duas-maneiras-de-reaproveitar), [Heranças sem sentido](../05-heranca-polimorfismo.md#heranças-sem-sentido) e [Duas perguntas sobre duas classes: "tem" e "é um"](../04-composicao-modelacao.md#duas-perguntas-sobre-duas-classes-tem-e-é-um).

<details>
<summary>Pista</summary>

Experimenta as duas frases em cada par. Uma frase "é um" só fica se passar no teste do guia 04.

</details>

## Exercício 4: Quem cumpre o contrato

O contrato do `conteudo` diz que o método não recebe nada além do `self`, devolve o texto a imprimir e não altera a etiqueta. Três colegas escreveram três variantes da `Etiqueta` do exercício 2:

```python partial
class EtiquetaComAsteriscos(Etiqueta):
    """Etiqueta com um asterisco de cada lado."""

    def conteudo(self):
        """Devolve o texto entre asteriscos."""
        return "*" + self.texto + "*"


class EtiquetaGritante(Etiqueta):
    """Etiqueta em maiúsculas, versão de outro colega."""

    def conteudo(self):
        """Devolve o texto em maiúsculas."""
        return self.texto.upper


class EtiquetaComTracos(Etiqueta):
    """Etiqueta com um traço de cada lado do texto."""

    def conteudo(self):
        """Junta um traço de cada lado do texto e devolve o resultado."""
        texto = "-" + self.texto + "-"
        return texto
```

Copia o programa do exercício 2 para o script `contrato_das_etiquetas.py` e acrescenta-lhe as três variantes, depois das outras classes.

1. Sem executar, diz num comentário no fim do script se cada variante cumpre o contrato. Quando uma não cumpre, diz que parte do contrato falha.
2. Troca a lista e o ciclo do programa principal por estas linhas:

   ```python partial
   etiquetas = [
       EtiquetaComAsteriscos("Borrachas"),
       EtiquetaGritante("Agrafadores"),
       EtiquetaComTracos("Réguas"),
   ]

   for etiqueta in etiquetas:
       print(etiqueta.conteudo())

   for etiqueta in etiquetas:
       print("Guardado:", etiqueta.texto)
   ```

   Uma das variantes não dá o que devia. Encontra-a e corrige-a, mudando só o que for preciso. No fim, as três primeiras linhas mostram o que as docstrings prometem, e as outras três, depois de `Guardado:`, os textos com que as etiquetas foram criadas.

   No mesmo comentário, conta como deste com o erro e como o corrigiste:

   - a etiqueta que falhou, o que devia aparecer, o que apareceu e que tipo de erro é: de escrita, de execução ou de lógica;
   - o que quer dizer a linha que não esperavas, e porque é que ela aparece;
   - o que mudaste, e como ficou;
   - o que mostraram as seis linhas depois da correção.

Rever: [O contrato comum](../05-heranca-polimorfismo.md#o-contrato-comum), [Nada impede uma quantidade impossível](../03-encapsulamento-contratos.md#nada-impede-uma-quantidade-impossível) e [O que mostra um objeto inteiro](../02-objetos-classes-instancias.md#o-que-mostra-um-objeto-inteiro).

<details>
<summary>Pista</summary>

Verifica as três partes do contrato em cada variante, uma de cada vez. Na alínea 2, lê palavra a palavra a linha que não esperavas, porque diz o que a variante devolveu. Em inglês, *built-in method* quer dizer "método embutido", um método que já vem com o Python.

</details>

## Exercício 5: O contrato de uma classe abstrata

Um programa de geometria tem uma classe `Forma`, para figuras planas como retângulos e quadrados. A qualquer forma se pode pedir a sua área. Cria o script `contrato_da_forma.py` e responde só com comentários.

1. Explica, numa frase, porque é que a `Forma` deve ser uma classe abstrata. Noutra frase, explica porque é que o `area` deve ser um método abstrato.
2. Escreve o contrato abstrato da `Forma`, por palavras ou organizado pela indentação. Tem de dizer o que todas as formas sabem fazer e o que cada forma concreta tem de completar. O contrato do `area` tem de estar por inteiro: o que recebe, o que devolve e o que não faz.

Rever: [O contrato de uma classe abstrata](../05-heranca-polimorfismo.md#o-contrato-de-uma-classe-abstrata).

<details>
<summary>Pista</summary>

Parte do contrato da `Notificacao`, no guia, e vê, linha a linha, o que muda quando se fala de formas.

</details>

## Exercício 6: Escrever duas formas concretas

Esta é a classe base `Forma`, já escrita. É um programa completo, que ainda não faz nada visível:

```python
# Ficha 05, exercício 6: as formas geométricas.

class Forma:
    """Uma figura geométrica plana.

    No modelo, é uma classe abstrata. Cada forma concreta deriva desta
    classe e escreve area().
    """
```

A `Forma` não tem construtor nem o método `area`. Por isso, o contrato do `area` fica na docstring da classe, onde quem escreve uma forma nova o vai procurar.

Queremos um programa para calcular a área de figuras planas. Cada retângulo guarda a largura e a altura, e cria-se com elas, como em `Retangulo(4, 3)`. A área de um retângulo é a largura vezes a altura. Cada quadrado cria-se só com o lado, como em `Quadrado(5)`. As classes `Retangulo` e `Quadrado` derivam da `Forma`, e o `area` de cada uma cumpre o contrato do exercício 5.

Deves poder pôr numa lista `Retangulo(4, 3)`, `Quadrado(5)` e `Retangulo(2, 7)`, e mostrar a área de cada forma com um ciclo `for`, uma por linha:

```text
12
25
14
```

Copia a classe `Forma` para o script `formas.py`.

1. Completa a docstring da `Forma` com o contrato do `area` que escreveste no exercício 5. Escreve-o depois da última frase, antes das três aspas que fecham.
2. Escreve o programa, por baixo da `Forma`. Decide tu que atributo guarda o quadrado e como calcula a área.
3. No fim do programa, acrescenta as linhas `geral = Forma()` e `print(geral.area())`, e executa. Deixa as duas linhas no script. Num comentário no fim do script, escreve a última linha da mensagem de erro e o que ela quer dizer, por palavras tuas.

Rever: [O contrato na docstring da classe base](../05-heranca-polimorfismo.md#o-contrato-na-docstring-da-classe-base), [Uma variante nova, sem mudar o ciclo](../05-heranca-polimorfismo.md#uma-variante-nova-sem-mudar-o-ciclo), [Uma variante com um dado novo e o `super()`](../05-heranca-polimorfismo.md#uma-variante-com-um-dado-novo-e-o-super) e [Uma variante que redefine um método](../05-heranca-polimorfismo.md#uma-variante-que-redefine-um-método).

<details>
<summary>Pista</summary>

Antes de escreveres cada construtor, decide que valores a forma recebe quando é criada, e se a `Forma` tem um construtor a quem os passar. Não dês a um atributo o nome de um método: um atributo `self.area` tapava o método `area`.

</details>

## Desafios

### Desafio 1: Um quadrado derivado do retângulo

Um colega diz que, no exercício 6, o `Quadrado` devia herdar do `Retangulo`, e não da `Forma`, porque "em Matemática, um quadrado é um retângulo". Cria o script `quadrado.py` e responde só com comentários.

1. Na versão do colega, `Quadrado(5)` é um retângulo com largura 5 e altura 5. Enquanto o `Retangulo` só souber calcular a área, pode usar-se um quadrado em qualquer sítio onde se espera um retângulo, sem surpresas? É o que pede o princípio da substituição.
2. Agora imagina que o `Retangulo` passa a ter um método `mudar_largura(nova)`, que muda só a largura e deixa a altura como estava. Um quadrado que herdasse este método continuaria a cumprir o que o retângulo promete, e a ser um quadrado? Explica o problema em duas ou três frases.

Rever: [O contrato comum](../05-heranca-polimorfismo.md#o-contrato-comum) e [Duas maneiras de reaproveitar](../05-heranca-polimorfismo.md#duas-maneiras-de-reaproveitar).

<details>
<summary>Pista</summary>

Em cada alínea, imagina um programa que recebe um retângulo e confia no que um retângulo promete.

</details>

### Desafio 2: Um método herdado que chama um método redefinido

A classe `Etiqueta` do exercício 2 tem um método `largura`, que nenhuma classe derivada redefine. Devolve o número de carateres do conteúdo da etiqueta, contados pelo `len`, que conta também os espaços e os sinais.

No script `largura.py`, copia o programa do exercício 2 e muda a última linha para `print(etiqueta.conteudo(), etiqueta.largura())`. Descobre de cabeça as três linhas que o programa mostra agora, e executa para confirmares. Num comentário no fim do script, explica o número da terceira linha com a regra de procura.

Rever: [Uma variante que redefine um método](../05-heranca-polimorfismo.md#uma-variante-que-redefine-um-método).

<details>
<summary>Pista</summary>

Segue a chamada `etiqueta.largura()` da terceira volta. Em que classe o Python encontra o `largura`? Lá dentro, para que objeto aponta o `self`? E, por isso, que `conteudo` é chamado na linha `len(self.conteudo())`?

</details>

## Critérios de conclusão

- Cada um dos seis exercícios tem o seu script, e as respostas por palavras estão no comentário do fim.
- Nas respostas por palavras, escreveste a razão de cada uma, e não só o resultado.
- No exercício 4, depois da correção, as seis linhas mostram o que o enunciado diz, e só mudaste a variante que falhava.
- No exercício 5, o contrato diz o que o `area` recebe, o que devolve e o que não faz.
- No exercício 6, a docstring da `Forma` tem esse contrato, o programa mostra as três áreas, e explicaste a mensagem de erro da forma geral.

![Rodapé](../../imagens/rodape.png)

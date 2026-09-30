![Cabeçalho](../imagens/cabecalho.png)

# Ficha de exercícios: herança, polimorfismo e abstração

*M10 · Caderno 5 · Ficha de exercícios*

Esta ficha acompanha o [caderno 5](05-heranca-polimorfismo.md). É para praticares sozinho, depois de estudares o caderno e de fazeres o [laboratório](05-heranca-polimorfismo-laboratorio.md). Conta com cerca de hora e um quarto para os sete exercícios, e mais um quarto de hora se fizeres o desafio opcional do fim.

As notificações do caderno ficam de fora de propósito. Os exercícios usam outros exemplos, com as mesmas regras, para perceberes se as regras foram compreendidas ou só decoradas. Cada exercício treina uma coisa só, e a ordem vai do mais direto para o que pede uma pequena decisão tua.

Responde no caderno diário ou numa folha, com o número de cada exercício. Nos exercícios que pedem uma previsão, escreve a previsão antes de executar o programa: é a previsão, e não a execução, que mostra o que percebeste. Entrega as respostas pelo meio indicado pelo professor.

## Exercício 1: ler uma hierarquia (5 min)

Esta árvore de especialização vem de um programa da secretaria de uma escola:

```text
Pessoa
├── Aluno
└── Funcionario
    ├── Professor
    └── Assistente
```

1. Indica a classe base de `Aluno`, a de `Professor` e a de `Funcionario`. Há uma classe que é, ao mesmo tempo, derivada de uma e base de outras: qual?
2. Escreve duas frases verdadeiras com "é um", uma delas a saltar um nível da árvore (de baixo até ao topo).
3. A frase "um aluno é um funcionário" é verdadeira? O que diz a árvore sobre a relação entre `Aluno` e `Funcionario`?

## Exercício 2: prever o que o ciclo mostra (10 min)

Lê este programa completo, sem o executar:

```python
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

1. Copia e preenche esta tabela, com a regra da secção 4 do caderno:

| Volta | Classe do objeto | Onde o Python encontra `conteudo` | Linha mostrada |
| --- | --- | --- | --- |
| 1 | A completar | A completar | A completar |
| 2 | A completar | A completar | A completar |
| 3 | A completar | A completar | A completar |

2. Executa e compara com a tua tabela.

## Exercício 3: um método herdado que chama um método redefinido (10 min)

Continua com o programa do exercício 2. A classe `Etiqueta` tem um método `largura`, que nenhuma classe derivada redefine. Devolve o número de carateres do conteúdo da etiqueta: `len` aplicado a um texto devolve o número de carateres, contando espaços e sinais. Por exemplo, `len("Pastas")` dá 6.

Muda a última linha do programa para `print(etiqueta.conteudo(), etiqueta.largura())`.

1. Para a terceira etiqueta, a com moldura, responde por esta ordem: em que classe é que o Python encontra `largura`? Dentro de `largura`, o `self` aponta para que objeto? E, por isso, que `conteudo` é chamado na linha `len(self.conteudo())`?
2. Escreve as três linhas que o programa vai mostrar agora.
3. Executa e compara. Se a terceira linha te surpreendeu, explica porquê, usando a última parte da secção 4 do caderno.

## Exercício 4: herança ou composição (10 min)

Para cada par, escreve a frase verdadeira ("A é um B" ou "A tem B") e diz se a relação se escreveria com herança ou com composição.

1. `Turma` e `Aluno`.
2. `Portatil` e `Computador`.
3. `Carro` e `Motor`.
4. `EtiquetaMaiuscula` e `Etiqueta`.
5. `Inventario` e `CaixaDeAvisos`.

Depois, responde: um colega quer criar, no programa do inventário, `class Caderno(Artigo):` e `class Pasta(Artigo):`, "porque um caderno é um artigo e uma pasta também". A frase "é um" é verdadeira. Mesmo assim, estas classes fazem falta? Justifica com a secção 10 do caderno.

## Exercício 5: quem cumpre o contrato (10 min)

O contrato de `conteudo` é: "não recebe nada além do `self`, devolve o texto a imprimir e não altera a etiqueta". Três colegas escreveram três variantes da classe `Etiqueta` do exercício 2. São excertos: para os experimentares, acrescenta-os ao programa do exercício 2, depois das outras classes.

```python partial
class EtiquetaComAsteriscos(Etiqueta):
    """Etiqueta com um asterisco de cada lado."""

    def conteudo(self):
        """Devolve o texto entre asteriscos."""
        return "*" + self.texto + "*"


class EtiquetaGritante(Etiqueta):
    """Etiqueta em maiúsculas, versão de outro colega."""

    def conteudo(self):
        """Põe o texto em maiúsculas e devolve-o."""
        self.texto = self.texto.upper()
        return self.texto


class EtiquetaDireta(Etiqueta):
    """Etiqueta que vai diretamente para o ecrã."""

    def conteudo(self):
        """Mostra o texto no ecrã."""
        print(self.texto)
```

1. Para cada variante, diz se cumpre o contrato. Se não cumprir, diz que parte do contrato falha.
2. Troca as linhas do programa principal do exercício 2 por estas, e prevê o que vai aparecer antes de executar:

```python partial
etiquetas = [
    EtiquetaComAsteriscos("Borrachas"),
    EtiquetaGritante("Agrafadores"),
    EtiquetaDireta("Réguas"),
]

for etiqueta in etiquetas:
    print(etiqueta.conteudo())

print(etiquetas[1].texto)
```

3. Executa e compara. Qual das duas variantes que não cumprem o contrato te parece mais perigosa num programa grande? Justifica numa ou duas frases.

## Exercício 6: o contrato de uma classe abstrata (10 min)

Um programa de geometria tem uma classe `Forma`, para figuras planas como retângulos e quadrados. Todas as formas têm uma área, mas a área de um retângulo calcula-se de uma maneira e a de um quadrado de outra, e não há uma maneira geral de calcular "a área de uma forma".

1. Explica, numa frase, porque é que `Forma` deve ser uma classe abstrata, e noutra frase porque é que `area` deve ser um método abstrato.
2. Escreve o contrato abstrato de `Forma` no papel, por palavras ou organizado por indentação, como no fim da secção 8 do caderno. Tem de dizer o que todas as formas sabem fazer e o que cada forma concreta tem de completar, com o contrato de `area` por inteiro: o que recebe, o que devolve e o que não faz.

## Exercício 7: escrever duas formas concretas (15 min)

Esta é a classe abstrata `Forma`, já escrita. Programa completo, que ainda não faz nada visível:

```python
from abc import ABC, abstractmethod


class Forma(ABC):
    """Uma figura geométrica plana.

    Classe abstrata: todas as formas têm uma área, mas não há uma maneira
    geral de a calcular. Cada forma concreta escreve a sua.
    """

    @abstractmethod
    def area(self):
        """Contrato: não recebe nada além do self, devolve a área da forma
        (um número maior ou igual a zero) e não altera a forma."""
```

1. Acrescenta ao programa a classe `Retangulo`, derivada de `Forma`, que se cria com a largura e a altura, por exemplo `Retangulo(4, 3)`, e cuja área é a largura vezes a altura.
2. Acrescenta a classe `Quadrado`, também derivada de `Forma`, que se cria só com o lado, por exemplo `Quadrado(5)`. Decide tu que atributo guarda e como calcula a área.
3. No fim do programa, cria uma lista com `Retangulo(4, 3)`, `Quadrado(5)` e `Retangulo(2, 7)` e mostra a área de cada forma com um ciclo `for`. Escreve as três áreas que esperas antes de executar.
4. Experimenta criar `Forma()`. Escreve a última linha do erro e diz por palavras o que significa.

## Desafio opcional: um quadrado é um retângulo?

Um colega diz que, no exercício 7, `Quadrado` devia herdar de `Retangulo`, e não de `Forma`, porque "em Matemática, um quadrado é um retângulo".

1. Com as classes do exercício 7, que só têm o método `area`, o teste de substituição da secção 7 do caderno passa? Isto é, pode usar-se um quadrado em qualquer sítio onde se espera um retângulo, sem surpresas?
2. Agora imagina que a classe `Retangulo` passa a ter um método `mudar_largura(nova)`, que muda só a largura e deixa a altura como estava. Um quadrado que herdasse este método continuaria a cumprir o que o retângulo promete, e a ser um quadrado? Explica o problema em duas ou três frases.

## Antes de entregares

Revê as tuas respostas e confirma que em cada previsão escreveste o raciocínio, e não só o resultado. Indica também um ponto desta ficha que ainda não consegues explicar sem voltar ao caderno: é por aí que deves começar a próxima revisão.

![Rodapé](../imagens/rodape.png)

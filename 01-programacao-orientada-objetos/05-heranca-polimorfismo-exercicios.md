![Cabeçalho](../imagens/cabecalho.png)

# Ficha de exercícios: Herança e polimorfismo

Ficha do tema Herança e polimorfismo, do módulo M10, Introdução à Programação Orientada por Objetos. Praticas a leitura de hierarquias, a previsão de chamadas, a escolha entre herança e composição e a verificação de contratos. Praticas também o contrato de uma classe abstrata e a escrita das suas classes concretas. Fazes sozinho, ao teu ritmo: o que não acabares na aula, acabas em casa ou na aula seguinte.

## O que precisas de saber

O [guia do tema](05-heranca-polimorfismo.md) e o [laboratório](05-heranca-polimorfismo-laboratorio.md). Cada exercício usa sobretudo estas secções do guia:

- Exercício 1: "Especialização: do geral para o particular" e "Herança em Python".
- Exercício 2: "Redefinir um método: onde o Python procura" e "Polimorfismo: a mesma chamada, comportamentos diferentes".
- Exercício 3: "Herança ou composição".
- Exercício 4: "O contrato comum". Os três tipos de erro (de escrita, de execução e de lógica) estão no guia 03, em "Nada impede uma quantidade impossível".
- Exercício 5: "Abstração, classes abstratas e o módulo `abc`", sobretudo "Escrever o contrato abstrato no papel".
- Exercício 6: "Abstração, classes abstratas e o módulo `abc`" e "Acrescentar dados numa classe derivada: `super()`".

## Como trabalhar

Faz os exercícios 1 a 6 pela ordem. São a parte obrigatória. Cada exercício treina uma coisa só, e a ordem vai do mais direto para o que pede uma pequena decisão tua. O desafio opcional e o exercício de "Para ires mais longe" são para quem acabar ou quiser treinar mais, ou para quando o professor os indicar.

As notificações do guia ficam de fora de propósito. Os exercícios usam outros exemplos, com as mesmas regras, para perceberes se as regras foram compreendidas ou só decoradas.

Responde no caderno diário ou numa folha, com o número de cada exercício. Nos exercícios que pedem uma previsão, escreve-a antes de executar o programa: é a previsão, e não a execução, que mostra o que percebeste. Um programa completo pode ser copiado para um ficheiro `.py` e executado no editor de Python que usas nas aulas. Os excertos não correm sozinhos, e o enunciado diz sempre de que outro código dependem. Entrega as respostas pelo meio indicado pelo professor.

## Exercício 1: Ler uma hierarquia

Esta árvore de especialização vem do programa de uma loja de instrumentos musicais:

```text
Instrumento
├── Tambor
└── InstrumentoDeCorda
    ├── Guitarra
    └── Violino
```

1. Indica a classe base de `Tambor`, a de `Guitarra` e a de `InstrumentoDeCorda`.
2. Há uma classe que é, ao mesmo tempo, derivada de uma e base de outras. Qual?
3. Escreve duas frases verdadeiras com "é um". Uma delas tem de saltar um nível da árvore, de baixo até ao topo.
4. A frase "um tambor é um instrumento de corda" é verdadeira? O que diz a árvore sobre a relação entre `Tambor` e `InstrumentoDeCorda`?

## Exercício 2: Prever o que o ciclo mostra

Lê este programa completo, sem o executar:

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

O método `largura` só vai ser usado no exercício de "Para ires mais longe", no fim da ficha. Por agora, não precisas dele.

1. Copia e completa esta tabela, com a regra de procura do guia:

   | Volta | Classe do objeto | Onde o Python encontra `conteudo` | Linha mostrada |
   | --- | --- | --- | --- |
   | 1 | A completar | A completar | A completar |
   | 2 | A completar | A completar | A completar |
   | 3 | A completar | A completar | A completar |

2. Executa e compara com a tua tabela.

## Exercício 3: Herança ou composição

Para cada par, escreve a frase verdadeira: "A é um B" ou "A tem B". Depois diz se a relação se escreveria com herança ou com composição, no sentido largo de "Herança ou composição", no guia: a relação "tem".

1. `Comboio` e `Carruagem`.
2. `ChefeFinal` e `Inimigo`, num jogo de computador.
3. `Hotel` e `Quarto`.
4. `RelogioInteligente` e `Relogio`.

Depois, responde a um colega. Ele quer acrescentar ao programa do exercício 2 as classes `EtiquetaCadernos(Etiqueta)` e `EtiquetaPastas(Etiqueta)`, cada uma só com uma docstring. Com elas, criaria as etiquetas das duas prateleiras com `EtiquetaCadernos("Cadernos")` e `EtiquetaPastas("Pastas")`. A frase "uma etiqueta de cadernos é uma etiqueta" é verdadeira. Mesmo assim, estas classes fazem falta? Compara-as com a `EtiquetaMaiuscula`, que também deriva de `Etiqueta`, e justifica com "Herança ou composição", no guia.

## Exercício 4: Quem cumpre o contrato

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
        """Devolve o texto em maiúsculas."""
        return self.texto.upper


class EtiquetaComTracos(Etiqueta):
    """Etiqueta com um traço de cada lado do texto."""

    def conteudo(self):
        """Junta um traço de cada lado do texto e devolve o resultado."""
        texto = "-" + self.texto + "-"
        return texto
```

1. Sem executar, diz, para cada variante, se cumpre o contrato. Se achares que não cumpre, diz que parte do contrato falha.
2. Troca as linhas do programa principal do exercício 2, a partir de `etiquetas = [`, por estas. Prevê as quatro linhas que vão aparecer, e só depois executa e compara.

   ```python partial
   etiquetas = [
       EtiquetaComAsteriscos("Borrachas"),
       EtiquetaGritante("Agrafadores"),
       EtiquetaComTracos("Réguas"),
   ]

   for etiqueta in etiquetas:
       print(etiqueta.conteudo())

   print(etiquetas[2].texto)
   ```

3. Uma das variantes não deu o que devia. Escreve o caso que falhou, o que devia aparecer e o que apareceu. O que devia aparecer tira-se do contrato e da docstring, e não do código. Diz também que tipo de erro é: de escrita, de execução ou de lógica.
4. Escreve, numa frase, uma hipótese para a causa: o que é que a linha do `return` dessa variante devolve, em vez do texto?
5. Corrige a variante, mudando só o que for preciso. Depois volta a correr o programa e confirma que as quatro linhas dão o que devem, também as das variantes que já estavam certas.

## Exercício 5: O contrato de uma classe abstrata

Um programa de geometria tem uma classe `Forma`, para figuras planas como retângulos e quadrados. Todas as formas têm uma área.

1. Explica, numa frase, porque é que `Forma` deve ser uma classe abstrata. Noutra frase, explica porque é que `area` deve ser um método abstrato.
2. Escreve no papel o contrato abstrato de `Forma`, por palavras ou organizado por indentação, como no fim de "Abstração, classes abstratas e o módulo `abc`", no guia. Tem de dizer o que todas as formas sabem fazer e o que cada forma concreta tem de completar. O contrato de `area` tem de estar por inteiro: o que recebe, o que devolve e o que não faz.

## Exercício 6: Escrever duas formas concretas

Esta é a classe abstrata `Forma`, já escrita. É um programa completo, que ainda não faz nada visível:

```python
# Ficha 05, exercício 6: as formas geométricas.

from abc import ABC, abstractmethod


class Forma(ABC):
    """Uma figura geométrica plana. Classe abstrata."""

    @abstractmethod
    def area(self):
        """Método abstrato: o contrato é o que escreveste no exercício 5."""
```

Repara que a `Forma` não tem construtor.

1. Acrescenta ao programa a classe `Retangulo`, derivada de `Forma`. Cria-se com a largura e a altura, por exemplo `Retangulo(4, 3)`, e a sua área é a largura vezes a altura.
2. Acrescenta a classe `Quadrado`, também derivada de `Forma`, que se cria só com o lado, por exemplo `Quadrado(5)`. Decide tu que atributo guarda e como calcula a área.
3. No fim do programa, cria uma lista com `Retangulo(4, 3)`, `Quadrado(5)` e `Retangulo(2, 7)`, e mostra a área de cada forma com um ciclo `for`. Escreve as três áreas que esperas antes de executar.
4. Experimenta criar `Forma()`. Escreve a última linha do erro e diz, por palavras tuas, o que significa.

## Apoio

- Exercício 1: lê a árvore de baixo para cima, ligação a ligação, com a frase "é um", como no guia. Escreve no papel cada frase que leres.
- Exercício 2: para cada volta, faz as duas perguntas da regra de procura. De que classe é o objeto? Essa classe escreve `conteudo`?
- Exercício 3: diz cada frase em voz alta, com "é um" e com "tem", e fica com a que for verdadeira. Na pergunta ao colega, compara as classes derivadas linha a linha: o que tem cada uma escrito por baixo da docstring?
- Exercício 4: verifica as três partes do contrato em cada variante, uma parte de cada vez. Na alínea 3, a linha que não esperavas é uma pista: lê-a palavra a palavra. *Built-in method* quer dizer "método embutido", um método que já vem com o Python.
- Exercício 5: começa pelo contrato da `Notificacao`, no guia, e pergunta, linha a linha, o que muda quando se fala de formas.
- Exercício 6: antes de escreveres cada construtor, decide que valores a forma recebe quando é criada. Não dês a um atributo o nome de um método: `self.area` tapava o método `area`.
- Desafio: em cada alínea, imagina um programa que recebe um retângulo e confia no que um retângulo promete.
- Mais longe 1: responde às três perguntas da alínea 1 pela ordem em que estão escritas, e escreve cada resposta antes de passares à seguinte.

## Desafio opcional

Um quadrado é um retângulo? Um colega diz que, no exercício 6, `Quadrado` devia herdar de `Retangulo`, e não de `Forma`, porque "em Matemática, um quadrado é um retângulo".

1. Com as classes do exercício 6, que só têm o método `area`, o teste de substituição de "O contrato comum", no guia, passa? Isto é, pode usar-se um quadrado em qualquer sítio onde se espera um retângulo, sem surpresas?
2. Agora imagina que a classe `Retangulo` passa a ter um método `mudar_largura(nova)`, que muda só a largura e deixa a altura como estava. Um quadrado que herdasse este método continuaria a cumprir o que o retângulo promete, e a ser um quadrado? Explica o problema em duas ou três frases.

## Para ires mais longe

Esta parte é opcional, para quem acabou os seis exercícios e quer treinar mais. Responde com o título do exercício, "Mais longe 1".

### Mais longe 1: Um método herdado que chama um método redefinido

Volta ao programa do exercício 2, com a lista e o ciclo originais. A classe `Etiqueta` tem um método `largura`, que nenhuma classe derivada redefine. Devolve o número de carateres do conteúdo da etiqueta. O `len` aplicado a um texto devolve o número de carateres, contando os espaços e os sinais: `len("Pastas")` dá 6.

Muda a última linha do programa para `print(etiqueta.conteudo(), etiqueta.largura())`.

1. Para a terceira etiqueta, a com moldura, responde por esta ordem. Em que classe é que o Python encontra `largura`? Dentro de `largura`, o `self` aponta para que objeto? E, por isso, que `conteudo` é chamado na linha `len(self.conteudo())`?
2. Escreve as três linhas que o programa vai mostrar agora.
3. Executa e compara. Se a terceira linha te surpreendeu, explica porquê, com a última parte de "Redefinir um método: onde o Python procura", no guia.

## Critérios de conclusão

- Fizeste os exercícios 1 a 6, com as previsões escritas antes de executar.
- Em cada previsão escreveste o raciocínio, e não só o resultado.
- Na tabela do exercício 2, cada volta diz onde o Python encontra o `conteudo`.
- No exercício 4, escreveste o caso que falhou, o que devia aparecer, o que apareceu e o tipo de erro. Depois da correção, voltaste a correr o programa inteiro.
- No exercício 5, o contrato diz o que `area` recebe, o que devolve e o que não faz.
- No exercício 6, o programa mostra as três áreas que previste, e explicaste a mensagem de `Forma()`.

## Autoavaliação

1. Em que previsão te enganaste, e o que percebeste com a diferença?
2. O que achaste mais difícil: ler a hierarquia, seguir a regra de procura, verificar um contrato ou escrever as formas concretas?
3. Que ponto desta ficha ainda não consegues explicar sem voltar ao guia? É por aí que começas a próxima revisão.

![Rodapé](../imagens/rodape.png)

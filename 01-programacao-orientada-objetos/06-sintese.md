![Cabeçalho](../imagens/cabecalho.png)

# Síntese

Módulo M10, Introdução à Programação Orientada por Objetos. Neste guia juntas as ideias do módulo num pequeno inventário em Python: classes e objetos, encapsulamento e composição, todas no mesmo programa. Lês o guia ao teu ritmo, de preferência em mais do que uma vez, e o que não acabares na aula acabas em casa ou na aula seguinte. Para praticar, há o [laboratório](06-sintese-laboratorio.md) e a [ficha de exercícios](06-sintese-exercicios.md) deste tema.

Nos guias 02, 03 e 04 construíste, uma peça de cada vez, um pequeno inventário de materiais. No guia [02 Objetos, classes e instâncias](02-objetos-classes-instancias.md) viste que uma classe descreve todos os artigos e que cada artigo concreto é um objeto com o seu próprio estado. No guia [03 Encapsulamento e contratos](03-encapsulamento-contratos.md), o artigo aprendeu a proteger a sua quantidade. Recusa um valor impossível com `ValueError` ("erro de valor") e, quando recusa, deixa os dados exatamente como estavam. No guia [04 Composição e modelação](04-composicao-modelacao.md), um objeto novo, o inventário, passou a criar e a guardar os artigos. Também os encontra pelo código e lhes passa os pedidos.

Este guia junta essas três ideias à volta de um único programa, que já vem quase todo escrito. Primeiro vais ler o programa e reconhecer nele cada ideia, com a indicação do guia onde foi explicada. Depois acompanhas um exemplo guiado, que completa uma operação que o programa ainda não sabe fazer. A ficha de exercícios tem tarefas curtas sobre o mesmo programa, cada uma com uma pequena decisão que o exemplo guiado não tomou por ti.

O objetivo é conseguires olhar para um programa com objetos e responder a três perguntas, sem decorar sintaxe. Que objetos existem, e o que guarda cada um? Quem decide se um pedido é aceite? O que acontece aos dados quando um pedido é aceite, e quando é recusado? São as perguntas que vais trabalhar no laboratório deste tema, que fazes na aula, passo a passo, com o professor a acompanhar.

Os programas completos correm sozinhos, como nos guias anteriores: copia-os para um ficheiro `.py` e executa o ficheiro inteiro, no editor de Python que usas nas aulas. Funcionam com o Python 3, a partir da versão 3.10. Cada execução começa do zero, com os valores escritos no programa. Os excertos estão sempre assinalados, e o texto diz de que outro código dependem.

## Neste guia

1. O que vais aprender
2. O que já sabes e vais usar
3. Ler o programa e reconhecer as ideias:
   - Três ideias num só pedido
   - O programa de partida
   - Classes e objetos no programa
   - Encapsulamento no programa
   - O inventário no programa: composição e procura pelo código
4. Exemplo guiado: completar o método `acertar`
5. Erros frequentes
6. Palavras novas deste guia
7. Verificar o que aprendeste
8. O que vem a seguir

## O que vais aprender

No fim deste guia, consegues:

- ler um programa com várias classes por zonas, a começar pelo programa principal, e dizer que objetos existem e o que guarda cada um;
- seguir um pedido feito ao inventário até à linha que decide se ele é aceite, e dizer que objeto respondeu;
- reconhecer um erro de lógica, um programa que corre sem mensagens e não faz o que devia, comparando o que ele mostra com a tua previsão;
- completar um método do inventário que encontra o artigo e lhe passa o pedido, começando pelo contrato e deixando a verificação a quem tem a regra;
- confirmar que um pedido recusado deixa o estado como estava, e que um pedido aceite mudou o que devia;
- descrever por palavras as classes do programa e a relação entre elas, e dizer o estado de cada artigo, identificado pelo código.

## O que já sabes e vais usar

Este guia quase não traz matéria nova. As novidades são duas, e pequenas. A primeira é a instrução `pass`, em "O programa de partida". A segunda é uma propriedade só com getter, que se consulta e não se altera pela propriedade; está no laboratório deste tema, que a explica. Tudo o resto vem dos guias anteriores e do 10.º ano:

- O artigo como uma linha do registo, com código, nome e quantidade: guia [01 Entidades, estado e ações](01-entidades-estado-acoes.md), em "A informação que interessa guardar".
- As regras do inventário: guia [01](01-entidades-estado-acoes.md), em "Uma operação tem de respeitar regras".
- O traço, a tabela que segue os valores passo a passo: guia [01](01-entidades-estado-acoes.md), em "Exemplo guiado: seguir os valores passo a passo".
- Classe, objeto ou instância, atributo e estado: guia [02 Objetos, classes e instâncias](02-objetos-classes-instancias.md), de "Um objeto reúne dados e operações" a "Classe e instância".
- O construtor `__init__`, o `self` e a chamada de um método com o ponto: guia [02](02-objetos-classes-instancias.md), em "A classe Artigo em Python" e "O método retirar em Python".
- Uma variável é uma etiqueta colada num objeto, e dois nomes podem apontar para o mesmo objeto: guia [02](02-objetos-classes-instancias.md), em "Cada instância é um objeto diferente".
- A invariante, e o zero no estado e o zero no pedido: guia [03 Encapsulamento e contratos](03-encapsulamento-contratos.md), em "As regras que devem continuar verdadeiras".
- O encapsulamento: guia [03](03-encapsulamento-contratos.md), em "Quem deve proteger a quantidade".
- A interface pública, com a operação de acertar a quantidade: guia [03](03-encapsulamento-contratos.md), em "Interface pública: aquilo que o objeto deixa usar".
- O `isinstance(valor, int)`, que pergunta se o valor é um inteiro, e o `not`, que inverte a resposta. Estão no guia [03](03-encapsulamento-contratos.md), em "Primeiro passo: métodos get e set" e "Recusar a sério: `ValueError` e `raise`".
- O sublinhado no início de um nome, como em `_quantidade`, que avisa que o nome é interno da classe: guia [03](03-encapsulamento-contratos.md), em "O sublinhado: um atributo privado por convenção".
- A exceção `ValueError`, lançada com `raise`, e a regra "verificar primeiro, alterar depois": guia [03](03-encapsulamento-contratos.md), em "Recusar a sério: `ValueError` e `raise`".
- O `try` e o `except ValueError as erro`, e a divisão de tarefas entre quem lança a exceção e quem a apanha: guia [03](03-encapsulamento-contratos.md), em "Tratar a recusa: `try` e `except`".
- Os três tipos de erro, de escrita, de execução e de lógica: guia [03](03-encapsulamento-contratos.md), em "Nada impede uma quantidade impossível".
- A propriedade `quantidade`. O getter (do inglês *get*, obter) lê o valor, e o setter (de *set*, pôr) verifica-o e guarda-o. Estão no guia [03](03-encapsulamento-contratos.md), em "Propriedades: `@property`".
- O construtor que passa pelo setter: guia [03](03-encapsulamento-contratos.md), em "O construtor também passa pelo setter".
- O contrato de uma operação e o valor `None` (do inglês, "nenhum"): guia [03](03-encapsulamento-contratos.md), em "Adicionar: uma operação com contrato".
- Os métodos `adicionar` e `retirar` do artigo, com as regras do pedido e a regra do estado. Estão no guia [03](03-encapsulamento-contratos.md), em "Adicionar: uma operação com contrato" e "Exemplo guiado: construir o método retirar".
- As responsabilidades, "quem sabe o quê": guia [04 Composição e modelação](04-composicao-modelacao.md), em "Quem sabe o quê: responsabilidades".
- O modelo, a descrição por palavras das classes de um programa e das relações entre elas. Cada classe descreve-se pelo que cada objeto guarda, pelos valores com que se cria e pelo que se lhe pode pedir. A relação descreve-se pela frase "tem", com o grau e as razões. Está no guia [04](04-composicao-modelacao.md), em "O inventário descrito por palavras".
- A composição e a agregação, com as quatro perguntas: guia [04](04-composicao-modelacao.md), em "Dois graus de "tem": composição e agregação" e "O nosso inventário: composição".
- A agregação em Python, com a playlist, a lista de músicas que alguém escolhe numa aplicação de música: guia [04](04-composicao-modelacao.md), em "Agregação em Python: a playlist e as músicas".
- A tabela que liga a descrição do modelo ao código: guia [04](04-composicao-modelacao.md), em "Da descrição ao código, e do código à descrição".
- A classe `Inventario`, com a lista interna `_artigos` e os métodos `_procurar`, `registar`, `quantidade_de` e `retirar`. Está no guia [04](04-composicao-modelacao.md), em "Exemplo guiado: construir a classe `Inventario`", com o encaminhamento e o caminho de uma recusa.
- As listas e o ciclo `for`: do 10.º ano, recordados no guia [04](04-composicao-modelacao.md), em "Recordar as listas e o ciclo `for`".
- A docstring, o texto entre três aspas que explica uma função, uma classe ou um método: guia [01](01-entidades-estado-acoes.md), em "Duas maneiras de organizar um programa".
- As condições com `if`, as funções com `def` e `return`, o texto entre aspas e o `print` com vários valores: do 10.º ano.

O guia [05 Herança e polimorfismo](05-heranca-polimorfismo.md) não é preciso para este guia nem para o laboratório, e nenhum dos dois te pede herança. Se quiseres rever como se distinguem a herança e a composição, lê "Herança ou composição", no guia 05.

## Três ideias num só pedido

Imagina o inventário de uma sala com dois artigos: A01, Caderno, 6 unidades, e A02, Pasta, 2 unidades. Alguém pede ao inventário: "do artigo A01, retira 2 unidades". Vamos seguir este pedido devagar, porque nele aparecem as três ideias dos guias anteriores.

O pedido é feito ao inventário, e não ao artigo, porque quem o faz conhece o código A01, e não o objeto que o representa. O inventário é o único objeto que guarda todos os artigos. Por isso é o único que consegue procurar, entre eles, o que tem o código A01. Encontra-o e passa-lhe o pedido, sem verificar nada sobre as unidades. Esta é a ideia do guia 04: o inventário reúne os artigos, encontra-os pelo código e encaminha os pedidos.

O artigo A01 recebe o pedido "retira 2". Verifica se o pedido faz sentido: 2 é um número inteiro e é positivo. Depois tenta guardar a nova quantidade, 6 - 2 = 4. Essa escrita passa pelo setter, que confirma que 4 é um inteiro não negativo e o guarda. Esta é a ideia do guia 03: é o próprio artigo que decide se o pedido é possível e que protege a sua quantidade.

No fim, A01 tem 4 unidades e A02 continua com 2, porque o pedido nunca lhe foi feito. São dois objetos diferentes, feitos a partir da mesma classe, cada um com o seu estado. Esta é a ideia do guia 02.

Agora o pedido seguinte: "do artigo A01, retira 9 unidades". O inventário encontra A01 e passa-lhe o pedido. O artigo verifica que 9 é inteiro e positivo, e tenta guardar 4 - 9 = -5. O setter recusa -5 com `ValueError`, antes de chegar à linha que guarda o valor. A quantidade continua 4. A exceção sobe até quem fez o pedido, que fica a saber que ele foi recusado e porquê.

E um terceiro pedido: "do artigo A07, retira 1 unidade". Desta vez, o inventário não encontra nenhum artigo com o código A07 e recusa o pedido ele próprio, também com `ValueError`. Nenhum artigo chega a ser contactado, e nenhuma quantidade muda.

Repara que, nos três pedidos, cada objeto fez só a parte para a qual tem informação. O inventário sabe que artigos existem, mas não sabe as regras das unidades. O artigo sabe a sua quantidade e as regras dos pedidos, mas não sabe que outros artigos existem. É esta divisão que vamos encontrar no programa de partida.

A tabela seguinte serve de mapa para o resto do guia. A coluna da direita diz onde cada ideia foi explicada pela primeira vez, para lá voltares se precisares.

| Ideia | Onde a vemos no exemplo | Secção deste guia | Explicada no |
| --- | --- | --- | --- |
| Classe | A descrição comum de todos os artigos, `Artigo` | Classes e objetos no programa | Guia 02, "Classe: a descrição comum" |
| Objeto ou instância | Os dois artigos concretos, A01 e A02, e o inventário | Classes e objetos no programa | Guia 02, "Classe e instância" |
| Atributo e estado | Código, nome e quantidade de cada artigo, num dado momento | Classes e objetos no programa | Guia 02, "Um objeto reúne dados e operações" |
| Construtor e `self` | O que prepara cada artigo quando nasce | Classes e objetos no programa | Guia 02, "A classe Artigo em Python" |
| Propriedade, getter e setter | A forma de ler e escrever a quantidade; cada escrita passa pela verificação | Encapsulamento no programa | Guia 03, "Propriedades: `@property`" e "O construtor também passa pelo setter" |
| Encapsulamento | O artigo controla as alterações à sua quantidade | Encapsulamento no programa | Guia 03, "Quem deve proteger a quantidade" |
| Exceção `ValueError`, `try` e `except` | A recusa que quem fez o pedido não pode ignorar | Encapsulamento no programa | Guia 03, "Recusar a sério: `ValueError` e `raise`" e "Tratar a recusa: `try` e `except`" |
| Composição | O inventário cria os seus artigos e guarda-os | O inventário no programa: composição e procura pelo código | Guia 04, "Dois graus de "tem": composição e agregação" e "O nosso inventário: composição" |
| Procura pelo código | O inventário encontra o artigo A01 entre todos | O inventário no programa: composição e procura pelo código | Guia 04, exemplo guiado, passo 3 |
| Encaminhamento | O inventário passa o pedido ao artigo, que decide | O inventário no programa: composição e procura pelo código | Guia 04, exemplo guiado, passo 5 |

## O programa de partida

Este é o programa à volta do qual trabalha todo o guia. É o programa final do exemplo guiado do guia 04, com as docstrings de `registar` e de `retirar` do inventário mais curtas. Tem uma diferença: a classe `Inventario` tem um método a mais, `acertar`, que acerta a quantidade de um artigo depois de uma contagem. As instruções das outras partes das classes são as mesmas do guia 04, e por isso o comportamento também é.

Antes de correres este programa, escreve no papel as duas linhas que ele devia mostrar, se fizesse o que o programa principal pede. O programa principal são as linhas encostadas à margem, no fim do ficheiro.

```python
# O programa de partida do guia 06: o inventário, com o método acertar por escrever.

class Artigo:
    """Artigo do inventário: código, nome e uma quantidade sempre válida.

    É a classe final do guia 03, com as docstrings encurtadas.
    """

    def __init__(self, codigo, nome, quantidade):
        """Cria o artigo. A quantidade inicial passa pelo setter."""
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
        """Acrescenta unidades (inteiro, 1 ou mais); senão, lança ValueError."""
        if not isinstance(unidades, int):
            raise ValueError("As unidades a adicionar têm de ser um número inteiro.")
        if unidades <= 0:
            raise ValueError("As unidades a adicionar têm de ser 1 ou mais.")
        self.quantidade = self.quantidade + unidades

    def retirar(self, unidades):
        """Retira unidades (inteiro, 1 ou mais, até ao que existe); senão, lança ValueError."""
        if not isinstance(unidades, int):
            raise ValueError("As unidades a retirar têm de ser um número inteiro.")
        if unidades <= 0:
            raise ValueError("As unidades a retirar têm de ser 1 ou mais.")
        # A falta de unidades é recusada pelo setter: o resultado seria negativo.
        self.quantidade = self.quantidade - unidades


class Inventario:
    """Inventário que cria, guarda e controla os seus artigos.

    O inventário é o dono dos artigos: cria-os em registar e guarda-os numa
    lista interna, _artigos, que o código de fora não usa. Garante a regra
    que nenhum artigo consegue garantir sozinho: não há dois artigos com o
    mesmo código. Os pedidos sobre um artigo são encaminhados para esse
    artigo, que continua a proteger a sua própria quantidade.
    """

    def __init__(self):
        """Cria um inventário vazio, ainda sem artigos."""
        self._artigos = []

    def _procurar(self, codigo):
        """Método interno: devolve o artigo com este código.

        Falha: lança ValueError se não houver nenhum artigo com este código.
        """
        for artigo in self._artigos:
            if artigo.codigo == codigo:
                return artigo
        raise ValueError("Não existe nenhum artigo com o código " + codigo + ".")

    def registar(self, codigo, nome, quantidade):
        """Cria um artigo novo e guarda-o no inventário.

        Falha: lança ValueError se já existir um artigo com este código, ou
        se a quantidade inicial for inválida. Em qualquer falha, o
        inventário fica como estava.
        """
        for artigo in self._artigos:
            if artigo.codigo == codigo:
                raise ValueError("Já existe um artigo com o código " + codigo + ".")
        novo = Artigo(codigo, nome, quantidade)
        self._artigos.append(novo)

    def quantidade_de(self, codigo):
        """Devolve a quantidade do artigo com este código, sem a alterar.

        Falha: lança ValueError se não houver nenhum artigo com este código.
        """
        artigo = self._procurar(codigo)
        return artigo.quantidade

    def retirar(self, codigo, unidades):
        """Encaminha um pedido de retirada para o artigo com este código.

        Falha: lança ValueError se não houver nenhum artigo com este código,
        ou se o próprio artigo recusar o pedido. Em qualquer falha, nenhuma
        quantidade muda.
        """
        artigo = self._procurar(codigo)
        artigo.retirar(unidades)

    def acertar(self, codigo, nova_quantidade):
        """Acerta a quantidade do artigo com este código, depois de uma contagem.

        Ainda por escrever: o exemplo guiado deste guia completa este método.
        """
        pass


inventario = Inventario()
inventario.registar("A01", "Caderno", 6)
inventario.registar("A02", "Pasta", 2)

inventario.acertar("A02", 5)
print("A01:", inventario.quantidade_de("A01"))
print("A02:", inventario.quantidade_de("A02"))
```

O programa mostra:

```text
A01: 6
A02: 2
```

Se escreveste `A02: 5` na segunda linha, a tua previsão está certa sobre o que o programa devia fazer. É o programa que está errado, e a subsecção "Um programa que corre sem erros e não faz o que devia" explica porquê.

Leitura guiada: um programa com mais de cem linhas não se lê de cima para baixo, linha a linha, na primeira vez. Lê-se por zonas, e começa-se pelo fim, como mostra a subsecção seguinte.

### Como ler um programa destes sem te perderes

1. Começa pelo **programa principal**, as linhas encostadas à margem no fim do ficheiro, a partir de `inventario = Inventario()`. São elas que dizem o que o programa faz: cria um inventário, regista dois artigos, pede para acertar a quantidade de A02 para 5 e mostra as duas quantidades.
2. Depois procura, nas classes, os métodos que o programa principal chama: `registar`, `acertar` e `quantidade_de`, todos da classe `Inventario`. Repara que o programa principal nunca fala diretamente com um artigo. Fala sempre com o inventário, usando os códigos.
3. Só depois desce à classe `Artigo`, para ver o que acontece quando o inventário passa um pedido a um artigo.

Não precisas de perceber todas as linhas antes de começares a trabalhar. Precisas de saber em que zona está cada coisa e de ir lá quando for preciso.

### Um programa que corre sem erros e não faz o que devia

O programa terminou sem nenhuma mensagem de erro. Mas pedimos para acertar a quantidade de A02 para 5, e a última linha mostra `A02: 2`. O pedido não teve efeito nenhum.

A razão está no método `acertar`. Por baixo da docstring tem apenas a instrução `pass` (em inglês, "passa"), que não faz nada. Está ali só para marcar, à vista, o sítio onde o código do método vai entrar. Quando o programa principal chama `inventario.acertar("A02", 5)`, o Python executa o método, encontra o `pass`, não faz nada e regressa. Nenhuma linha do método mexe em nenhum artigo.

O `pass` faz mais falta noutro caso. Um `def` precisa de pelo menos uma instrução por baixo, e a docstring já conta como uma. Por isso, aqui, o método funcionava igual sem o `pass`. Num `def` ainda sem docstring nem código, o `pass` é a forma de dizer "ainda não faz nada" sem o Python recusar o ficheiro.

O guia 03, em "Nada impede uma quantidade impossível", distinguiu três tipos de erro. Um **erro de escrita** impede o Python de perceber o programa: falta um parêntese, faltam os dois pontos no fim de um `def`, ou uma linha está mal indentada. O programa nem chega a começar, e o Python mostra uma mensagem com `SyntaxError` ("erro de sintaxe") ou `IndentationError` ("erro de indentação"). Um **erro de execução** para o programa a meio, com uma mensagem que começa por `Traceback` ("rasto"). Um **erro de lógica** é diferente: o programa corre do princípio ao fim, sem nenhuma mensagem, mas faz uma coisa diferente da que o problema pede.

O nosso programa tem um erro de lógica, e é o tipo de erro mais traiçoeiro, porque o Python não avisa de nada. A única forma de o apanhar é saber antes o que o programa devia mostrar e comparar com o que mostrou. Se não tivesses pensado que A02 devia ficar com 5, a linha `A02: 2` parecia perfeitamente normal. É por isso que, em todos os guias, escreves a previsão antes de executar: a previsão é o que te permite reparar que alguma coisa está errada.

## Classes e objetos no programa

Esta secção recorda o guia 02, apontando para as linhas do programa de partida.

A linha `class Artigo:` começa a **classe** `Artigo`, a descrição comum de todos os artigos. Diz que cada artigo tem um código, um nome e uma quantidade, e que a cada artigo se pode pedir que adicione ou retire unidades. A classe não é nenhum artigo em particular. É como uma receita, que diz que ingredientes são precisos e que passos seguir, mas não é nenhum dos bolos feitos com ela.

Os artigos concretos são **objetos**, também chamados **instâncias** da classe `Artigo`. Cada um tem os seus **atributos**, com os seus valores, e o conjunto desses valores num dado momento é o **estado** do objeto. No programa de partida há dois artigos. Um tem o código A01, o nome Caderno e a quantidade 6. O outro tem o código A02, o nome Pasta e a quantidade 2. Há também um terceiro objeto, de outra classe: o inventário, criado pela linha `inventario = Inventario()`. No total, o programa tem duas classes e três objetos dessas classes.

O erro típico é pensar que a quantidade 6 quer dizer seis objetos. Não quer. Há um só objeto para o artigo A01, que guarda o número 6. O objeto é a ficha do material no registo, e não cada caderno que está no armário.

Os artigos nascem dentro do método `registar`, na linha `novo = Artigo(codigo, nome, quantidade)`. Quando essa linha é executada, o Python cria um objeto novo, do tipo `Artigo`, e chama o **construtor** `__init__`. O parâmetro `self` aponta para esse objeto novo, e os outros três parâmetros recebem os valores. O construtor guarda cada valor num atributo do objeto. `self.codigo = codigo` lê-se "guarda no atributo `codigo` deste objeto o valor que chegou no parâmetro `codigo`". O construtor é executado uma vez por cada artigo criado, e cada execução prepara um objeto diferente.

Dentro de qualquer método, `self` é o objeto sobre o qual o método está a trabalhar. Repara na chamada `artigo.retirar(unidades)`, que está no método `retirar` do inventário. O objeto que está antes do ponto, `artigo`, é o que ocupa o `self` do método `retirar` da classe `Artigo`. É por isso que a mesma linha de código, `self.quantidade = self.quantidade - unidades`, mexe no caderno quando o pedido é para o caderno, e na pasta quando o pedido é para a pasta.

Os dois artigos são objetos diferentes, apesar de terem sido feitos a partir da mesma classe. Retirar unidades a um não tira nenhuma ao outro. Mas cuidado com os nomes. No guia 02, em "Cada instância é um objeto diferente", viste que uma variável é uma etiqueta colada num objeto, e não uma cópia dele. É isso que acontece quando `_procurar` devolve um artigo e o método do inventário o guarda no nome local `artigo`. Esse nome passa a apontar para o próprio objeto que está na lista. Qualquer alteração feita através dele fica no artigo guardado no inventário.

## Encapsulamento no programa

Esta secção recorda o guia 03.

A regra da quantidade é uma **invariante**: tem de ser verdadeira durante toda a vida de um artigo, antes e depois de cada operação. A quantidade de um artigo é sempre um número inteiro maior ou igual a zero. O **encapsulamento** é a forma de organizar o programa para que seja o próprio artigo a garantir esta regra. O artigo guarda a quantidade e oferece operações para a consultar e para a alterar, e todas essas operações verificam antes de alterar.

No programa, a quantidade é uma **propriedade**. Por fora lê-se e escreve-se como um atributo normal, `artigo.quantidade`. Por dentro, cada leitura passa pelo getter e cada escrita passa pelo setter. O valor vive no atributo interno `_quantidade`, com sublinhado, que avisa por convenção que o código de fora não lhe deve mexer. O setter faz duas verificações, primeiro o tipo e depois o valor, e só na última linha guarda o valor. Se uma verificação falhar, `raise ValueError(...)` para o setter nessa linha, e a linha que guarda o valor nunca chega a ser executada. É assim que se escreve em Python a regra "verificar primeiro, alterar depois".

Repara que o construtor escreve `self.quantidade = quantidade`, sem sublinhado. A quantidade inicial passa pelo setter, como qualquer outra, e por isso um artigo com quantidade inválida nem chega a existir.

O método `retirar` do artigo divide o trabalho com o setter. O método verifica as regras do pedido: as unidades têm de ser um número inteiro e têm de ser 1 ou mais. O setter verifica a regra do estado: a quantidade que resultaria do pedido não pode ser negativa. Não haver unidades suficientes é o mesmo que a nova quantidade ser negativa. Por isso é o setter que recusa esse caso, com a mensagem "A quantidade não pode ser negativa.". Cada regra está escrita num só sítio.

Quando um pedido é recusado, quem o fez fica a saber através da exceção. Se o pedido estiver dentro de um `try` com `except ValueError as erro`, o Python abandona o `try` na linha que falhou e salta para o `except`. O nome `erro` passa a referir a exceção, cuja mensagem se pode mostrar com `print`. Se nenhum `try` apanhar a exceção pelo caminho, o programa para, e o Python mostra a mensagem, com as linhas do `Traceback` por cima. A classe decide se o pedido é válido; quem usa a classe decide o que fazer com a recusa.

Para verificar uma operação recusada, ver a mensagem não chega. É preciso confirmar também que o estado não mudou. E, para verificar uma operação aceite, também não basta ver que não houve mensagem. O programa de partida acabou de te mostrar um método que não lançou exceção nenhuma e não fez nada.

## O inventário no programa: composição e procura pelo código

Esta secção recorda o guia 04.

O inventário existe porque há regras e perguntas sobre o conjunto dos artigos que nenhum artigo consegue responder sozinho. Que artigos existem? Um código já está a ser usado? Qual é o artigo com um certo código? Uma tarefa fica com quem tem a informação necessária para a fazer, e só o inventário conhece todos os artigos.

### Como o inventário encontra um artigo

O método interno `_procurar` percorre a lista `_artigos` com um ciclo `for` e compara o código de cada artigo com o código procurado. Assim que o encontra, o `return` devolve esse artigo e termina o método, mesmo a meio do ciclo. Se o ciclo acabar todas as voltas sem encontrar nenhum, chega-se à linha do `raise`, que está depois do ciclo. O método lança então `ValueError` com a mensagem "Não existe nenhum artigo com o código ...". O nome começa por sublinhado porque é uma ferramenta interna, para os métodos do próprio inventário usarem.

Os métodos `quantidade_de` e `retirar` do inventário começam os dois com `artigo = self._procurar(codigo)`. O `self.` não pode faltar: é através dele que um método chega aos outros métodos do mesmo objeto. Sem ele, o Python procura uma função solta chamada `_procurar`, e não a encontra. Se o código não existir, `_procurar` lança a exceção, e o método que o chamou é interrompido nessa mesma linha.

### Encaminhar o pedido sem repetir as regras

O método `retirar` do inventário tem só duas linhas: encontra o artigo e passa-lhe o pedido, com `artigo.retirar(unidades)`. A esta forma de colaborar chama-se **encaminhamento**. O inventário não verifica se as unidades são um inteiro, nem se são positivas, nem se chegam. Essas regras são do artigo e já estão escritas no artigo. Se o artigo recusar, a exceção nasce no artigo, atravessa o método do inventário, que não a apanha, e chega a quem fez o pedido. O inventário não apanha a exceção porque não sabe o que fazer com uma recusa: quem sabe é o programa principal.

### Composição: o inventário cria os seus artigos

A relação entre `Inventario` e `Artigo` é uma relação "tem": um inventário tem artigos. O guia 04, em "Dois graus de "tem": composição e agregação", distingue dois graus desta relação com quatro perguntas. As duas primeiras decidem: a parte faz sentido sem o todo? E quem cria a parte?

Neste programa, quem cria os artigos é o inventário, dentro do seu método `registar`. É lá, e só lá, que aparece `Artigo(...)`. O programa principal não cria nenhum artigo nem guarda nenhum artigo num nome seu: só tem o nome `inventario` e fala com ele através dos códigos. E o artigo, que é uma linha do registo deste inventário, não faz sentido sem ele. Por isso a relação é uma **composição**.

Seria uma **agregação** se o inventário recebesse artigos já criados fora dele. É o que faz a playlist do guia 04, em "Agregação em Python: a playlist e as músicas", que recebe músicas que já existem. Nesse caso, o programa principal teria linhas como `caderno = Artigo("A01", "Caderno", 6)`, e o inventário teria um método que recebe esse objeto e o junta à lista. A tabela de "Da descrição ao código, e do código à descrição", no guia 04, diz o mesmo de forma curta. A relação é uma composição quando o todo cria as partes dentro de um método seu e não as entrega a quem está de fora. É uma agregação quando o todo tem um método que recebe objetos já criados e os junta à lista.

O erro típico é chamar composição a qualquer objeto que guarda uma lista de outros objetos. A lista, sozinha, não decide nada: a playlist também guarda uma lista. O que decide é quem chama o construtor da parte e se a parte tem vida fora do todo. Antes de escreveres composição ou agregação, procura no código a linha onde a parte é criada.

## Exemplo guiado: completar o método `acertar`

Vamos agora completar o método `acertar`, acompanhando o raciocínio do princípio ao fim. Repara que o exemplo usa as três ideias ao mesmo tempo, e que é isso que o torna um bom exemplo de síntese.

### Passo 1: perceber o que o método tem de fazer

De vez em quando, alguém conta à mão o material que está no armário. Imagina que, ao contar as pastas, encontra 5, mas o programa diz que há 2: alguém arrumou três pastas e esqueceu-se de as registar. Acertar a quantidade é escrever no artigo o valor contado, para o programa voltar a dizer a verdade.

Podias perguntar porque não se usa o método `adicionar`, com 3 unidades. Há duas razões. A primeira é que quem conta sabe o total, 5, e não a diferença. Teria de fazer a conta à mão, e uma conta à mão é mais uma oportunidade de engano. A segunda é que a contagem pode dar menos do que o registado, se alguém levou material sem o registar. Então seria preciso retirar, e não adicionar. Acertar serve para os dois casos: escreve-se o valor contado, seja ele maior ou menor do que o anterior.

O guia 03, em "Interface pública: aquilo que o objeto deixa usar", já tinha esta operação na interface pública do artigo: "acertar a quantidade". Faz-se escrevendo na propriedade, como em `artigo.quantidade = 5`. O que falta é poder fazê-lo através do inventário, a partir do código, porque o programa principal não guarda nenhum artigo num nome seu.

### Passo 2: decidir quem faz o quê

Antes de escrever, aplicamos a regra do guia 04, em "Quem sabe o quê: responsabilidades": cada tarefa fica com quem tem a informação necessária para a fazer.

| Tarefa | Que informação é precisa | Quem a tem | Fica a cargo de |
| --- | --- | --- | --- |
| Encontrar o artigo com este código | Os códigos de todos os artigos | O inventário | O método `_procurar` do inventário |
| Decidir se o valor contado é uma quantidade válida | A regra da quantidade | O artigo | O setter da quantidade |
| Guardar o novo valor | O atributo interno `_quantidade` | O artigo | O setter da quantidade |

A tabela diz-nos uma coisa importante sobre o que o método `acertar` não deve fazer. Não deve verificar se o valor é inteiro, nem se é negativo. Essa regra já vive no setter. Escrevê-la outra vez no inventário seria ter a mesma regra em dois sítios, com o risco de um dia mudar num e esquecer no outro. O inventário encontra o artigo e escreve na propriedade, e a verificação acontece sozinha, porque escrever na propriedade é chamar o setter.

### Passo 3: escrever o contrato

Como nos guias 03 e 04, começamos pelo que o método promete, antes de pensar em como o escrever.

O método recebe o código de um artigo e a quantidade contada. Não devolve nada. Falha, com `ValueError`, em dois casos. O primeiro é não haver nenhum artigo com esse código, e quem recusa é `_procurar`. O segundo é a quantidade contada ser inválida, e quem recusa é o setter do artigo. Em qualquer dos dois casos, nenhuma quantidade muda. Quando não falha, a quantidade do artigo passa a ser exatamente o valor contado.

### Passo 4: escrever o método

O método completo, com o contrato na docstring, fica assim. É um excerto: substitui, na classe `Inventario` do programa de partida, o método `acertar` que tinha o `pass`.

```python partial
    def acertar(self, codigo, nova_quantidade):
        """Acerta a quantidade do artigo com este código, depois de uma contagem.

        Recebe: o código do artigo e a quantidade contada.
        Devolve: nada (None).
        Falha: lança ValueError se não houver nenhum artigo com este código,
        ou se a quantidade contada for inválida (quem a recusa é o setter
        do artigo). Em qualquer falha, nenhuma quantidade muda.
        """
        artigo = self._procurar(codigo)
        artigo.quantidade = nova_quantidade
```

Lê as duas linhas pela ordem em que o Python as executa.

A primeira, `artigo = self._procurar(codigo)`, é igual à primeira linha de `quantidade_de` e de `retirar`. Se o código não existir, `_procurar` lança `ValueError`, e o método `acertar` é interrompido aqui, sem chegar à segunda linha. Se existir, o nome local `artigo` passa a apontar para o próprio artigo guardado na lista.

A segunda, `artigo.quantidade = nova_quantidade`, é uma escrita na propriedade `quantidade` desse artigo. Para o Python, escrever na propriedade é chamar o setter, com o valor da direita no parâmetro `valor`. O setter faz as suas duas verificações e só depois guarda o valor em `_quantidade`. Se o valor for inválido, o setter lança `ValueError` antes de o guardar, e a quantidade fica como estava.

Repara no que esta linha não faz: não escreve em `artigo._quantidade`. O inventário é código de fora da classe `Artigo`, e o código de fora usa a interface pública do artigo, que é a propriedade, e não o atributo interno. Se escrevesse em `_quantidade`, passava ao lado do setter, e um acerto para -1 seria aceite em silêncio.

### Passo 5: prever antes de executar

Antes de executarmos, fazemos o traço de quatro pedidos seguidos a um inventário com A01 a 6 e A02 a 2. Cada linha começa no estado deixado pela anterior. A coluna "Quem responde" diz que peça do programa aceitou ou recusou o pedido.

Antes de leres a tabela, faz tu o traço no papel, com as mesmas colunas, para os pedidos `acertar("A02", 5)`, `acertar("A01", -1)`, `acertar("A09", 3)` e `retirar("A02", 4)`. Depois compara.

| Pedido | Quem responde | Resposta | A01 depois | A02 depois |
| --- | --- | --- | ---: | ---: |
| `acertar("A02", 5)` | `_procurar` encontra A02; o setter recebe 5, que é válido | Aceite | 6 | 5 |
| `acertar("A01", -1)` | `_procurar` encontra A01; o setter recebe -1, que é negativo | `ValueError` lançado pelo setter | 6 | 5 |
| `acertar("A09", 3)` | `_procurar` não encontra A09 | `ValueError` lançado pelo inventário | 6 | 5 |
| `retirar("A02", 4)` | `_procurar` encontra A02; o artigo aceita, 5 - 4 = 1 | Aceite | 6 | 1 |

A última linha mostra porque é que o acerto importa. A retirada de 4 pastas só é possível porque o programa passou a saber que havia 5. Antes do acerto, com 2 pastas registadas, esse pedido seria recusado.

### Passo 6: executar e comparar com o traço

Programa completo, com o método `acertar` já escrito. O programa principal faz os quatro pedidos do traço, pela mesma ordem:

```python
# O inventário com o método acertar: o programa do exemplo guiado do guia 06.

class Artigo:
    """Artigo do inventário: código, nome e uma quantidade sempre válida.

    É a classe final do guia 03, com as docstrings encurtadas.
    """

    def __init__(self, codigo, nome, quantidade):
        """Cria o artigo. A quantidade inicial passa pelo setter."""
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
        """Acrescenta unidades (inteiro, 1 ou mais); senão, lança ValueError."""
        if not isinstance(unidades, int):
            raise ValueError("As unidades a adicionar têm de ser um número inteiro.")
        if unidades <= 0:
            raise ValueError("As unidades a adicionar têm de ser 1 ou mais.")
        self.quantidade = self.quantidade + unidades

    def retirar(self, unidades):
        """Retira unidades (inteiro, 1 ou mais, até ao que existe); senão, lança ValueError."""
        if not isinstance(unidades, int):
            raise ValueError("As unidades a retirar têm de ser um número inteiro.")
        if unidades <= 0:
            raise ValueError("As unidades a retirar têm de ser 1 ou mais.")
        # A falta de unidades é recusada pelo setter: o resultado seria negativo.
        self.quantidade = self.quantidade - unidades


class Inventario:
    """Inventário que cria, guarda e controla os seus artigos.

    O inventário é o dono dos artigos: cria-os em registar e guarda-os numa
    lista interna, _artigos, que o código de fora não usa. Garante a regra
    que nenhum artigo consegue garantir sozinho: não há dois artigos com o
    mesmo código. Os pedidos sobre um artigo são encaminhados para esse
    artigo, que continua a proteger a sua própria quantidade.
    """

    def __init__(self):
        """Cria um inventário vazio, ainda sem artigos."""
        self._artigos = []

    def _procurar(self, codigo):
        """Método interno: devolve o artigo com este código.

        Falha: lança ValueError se não houver nenhum artigo com este código.
        """
        for artigo in self._artigos:
            if artigo.codigo == codigo:
                return artigo
        raise ValueError("Não existe nenhum artigo com o código " + codigo + ".")

    def registar(self, codigo, nome, quantidade):
        """Cria um artigo novo e guarda-o no inventário.

        Falha: lança ValueError se já existir um artigo com este código, ou
        se a quantidade inicial for inválida. Em qualquer falha, o
        inventário fica como estava.
        """
        for artigo in self._artigos:
            if artigo.codigo == codigo:
                raise ValueError("Já existe um artigo com o código " + codigo + ".")
        novo = Artigo(codigo, nome, quantidade)
        self._artigos.append(novo)

    def quantidade_de(self, codigo):
        """Devolve a quantidade do artigo com este código, sem a alterar.

        Falha: lança ValueError se não houver nenhum artigo com este código.
        """
        artigo = self._procurar(codigo)
        return artigo.quantidade

    def retirar(self, codigo, unidades):
        """Encaminha um pedido de retirada para o artigo com este código.

        Falha: lança ValueError se não houver nenhum artigo com este código,
        ou se o próprio artigo recusar o pedido. Em qualquer falha, nenhuma
        quantidade muda.
        """
        artigo = self._procurar(codigo)
        artigo.retirar(unidades)

    def acertar(self, codigo, nova_quantidade):
        """Acerta a quantidade do artigo com este código, depois de uma contagem.

        Recebe: o código do artigo e a quantidade contada.
        Devolve: nada (None).
        Falha: lança ValueError se não houver nenhum artigo com este código,
        ou se a quantidade contada for inválida (quem a recusa é o setter
        do artigo). Em qualquer falha, nenhuma quantidade muda.
        """
        artigo = self._procurar(codigo)
        artigo.quantidade = nova_quantidade


inventario = Inventario()
inventario.registar("A01", "Caderno", 6)
inventario.registar("A02", "Pasta", 2)

inventario.acertar("A02", 5)
print("A02 depois de acertar para 5:", inventario.quantidade_de("A02"))

try:
    inventario.acertar("A01", -1)
except ValueError as erro:
    print("Acerto de A01 recusado:", erro)

try:
    inventario.acertar("A09", 3)
except ValueError as erro:
    print("Acerto de A09 recusado:", erro)

inventario.retirar("A02", 4)
print("A02 depois de retirar 4:", inventario.quantidade_de("A02"))

print("A01 no fim:", inventario.quantidade_de("A01"))
print("A02 no fim:", inventario.quantidade_de("A02"))
```

O programa mostra:

```text
A02 depois de acertar para 5: 5
Acerto de A01 recusado: A quantidade não pode ser negativa.
Acerto de A09 recusado: Não existe nenhum artigo com o código A09.
A02 depois de retirar 4: 1
A01 no fim: 6
A02 no fim: 1
```

Leitura guiada: as classes são as do programa de partida, com o `acertar` do passo 4 no lugar do que tinha o `pass`. O que muda é o programa principal, que faz os quatro pedidos do traço. Os pedidos que podem ser recusados estão dentro de um `try`, e depois de cada pedido aceite há um `print` com a quantidade.

Compara linha a linha com o traço do passo 5. O acerto de A02 foi aceite, e a quantidade passou a 5. As duas recusas aparecem pela ordem do traço, e cada mensagem diz quem recusou. "A quantidade não pode ser negativa." vem do setter do artigo, e "Não existe nenhum artigo com o código A09." vem do inventário. A retirada de 4 pastas foi aceite e deixou 1. As duas últimas linhas confirmam o estado final: A01, que só recebeu um pedido recusado, continua com 6.

Repara também no acerto aceite: não mostra nada. Um método que cumpre o pedido termina sem erro e em silêncio. É por isso que o programa mostra a quantidade a seguir, para termos a prova de que o acerto aconteceu. Foi exatamente essa prova que faltou ao programa de partida, quando o `acertar` ainda só tinha o `pass`.

### Passo 7: seguir o caminho de uma recusa

Segue agora o pedido `inventario.acertar("A01", -1)` até ao fim, como o guia 04 fez com uma retirada, no passo 8 do seu exemplo guiado.

1. O programa principal, dentro do `try`, chama o método `acertar` do inventário, com `"A01"` e `-1`.
2. O método `acertar` chama `_procurar("A01")`, que encontra o artigo A01, devolve-o com o `return` e termina.
3. O método `acertar` executa `artigo.quantidade = nova_quantidade`, o que chama o setter do artigo A01 com -1.
4. O setter verifica que -1 é inteiro, mas é negativo, e executa `raise ValueError("A quantidade não pode ser negativa.")`.

A exceção nasce no setter e sobe pela cadeia de chamadas que ainda estão à espera:

| Onde está a exceção | O que esse sítio estava a fazer | O que lhe acontece |
| --- | --- | --- |
| Setter da quantidade | A verificar -1 | Lança a exceção; não guarda o valor |
| Método `acertar` do inventário | À espera do setter, na segunda linha | É abandonado sem terminar |
| Programa principal | Dentro de um `try` | Apanha a exceção no `except` e mostra a mensagem |

O método `_procurar` não está na tabela, porque já tinha terminado quando a exceção nasceu. Repara também que esta cadeia é mais curta do que a da retirada, no guia 04. Entre o inventário e o setter não há nenhum método do artigo: a escrita na propriedade chama o setter diretamente, a partir da linha do inventário.

### Passo 8: o modelo descrito por palavras

No guia 04, em "O inventário descrito por palavras", o modelo do inventário ficou escrito antes do código. O modelo tem de dizer o mesmo que o programa. Por isso, quando o programa ganha um método, relê-se o modelo e acerta-se o que mudou. Vamos ver o que muda com o `acertar`.

A descrição de cada classe tem três partes: o que cada objeto guarda, com que valores se cria e o que se lhe pode pedir. A descrição da classe `Artigo` não muda:

- Cada artigo guarda um código, um nome e uma quantidade, que é sempre um número inteiro não negativo.
- Um artigo cria-se com o código, o nome e a quantidade inicial.
- A um artigo pode pedir-se que adicione unidades, com `adicionar(unidades)`, e que retire unidades, com `retirar(unidades)`.

O método novo é do inventário. No artigo, o acerto faz-se escrevendo na quantidade, e a quantidade já está na primeira parte da descrição, com a sua regra.

Na descrição da classe `Inventario`, muda só a terceira parte, a do que se pode pedir, que ganha o pedido novo:

- Cada inventário guarda os seus artigos, e nunca dois com o mesmo código.
- Um inventário cria-se vazio, sem nenhum valor.
- A um inventário pode pedir-se que registe um artigo novo, com `registar(codigo, nome, quantidade)`; que diga a quantidade de um artigo, com `quantidade_de(codigo)`; e que retire unidades de um artigo, com `retirar(codigo, unidades)`. Pode pedir-se-lhe também que acerte a quantidade de um artigo depois de uma contagem, com `acertar(codigo, nova_quantidade)`.

Repara no que fica de fora. A lista `_artigos` não aparece, pela razão que o guia 04 dá. A descrição diz que o inventário guarda os seus artigos, e a lista é só a forma como o programa os guarda. O método `_procurar` também não aparece. É interno: só os métodos do próprio inventário o usam, e não faz parte do que se pode pedir ao inventário de fora. E o pedido novo não repete a regra da quantidade. Essa regra está na descrição do artigo, como no código está no setter. É a decisão do passo 2, agora no modelo: cada regra num só sítio.

A descrição da relação entre as duas classes também não muda:

- Um inventário tem artigos, e é uma composição.
- Um artigo só faz sentido dentro do seu inventário, porque é uma linha do registo.
- É o inventário que cria cada artigo, quando se lhe pede que o registe.
- Cada artigo pertence a um só inventário e desaparece se o inventário desaparecer.

O método `acertar` muda a quantidade de um artigo que já existe. Não muda quem cria os artigos, quem os guarda nem a quantos inventários pertence cada um. A relação entre duas classes muda quando muda a forma como os objetos se ligam, e não quando se acrescenta um pedido. É a mesma composição de "O inventário no programa: composição e procura pelo código".

A descrição de uma classe não tem valores, porque vale para todos os objetos dela. Para dizer como ficaram os artigos no fim do programa do passo 6, descreve-se o estado de cada um:

- O artigo A01 chama-se Caderno e tem 6 unidades.
- O artigo A02 chama-se Pasta e tem 1 unidade.

Repara que cada artigo é identificado pelo código. No guia 02, o caderno estava guardado no nome `caderno`, e podíamos falar do objeto `caderno`. Neste programa, o programa principal não guarda nenhum artigo num nome seu. Chega a eles pelo inventário e pelo código, e é também pelo código que os identificamos quando os descrevemos. O nome `artigo`, dentro dos métodos do inventário, não serve para isso: é um nome local, que aponta, em cada chamada, para o artigo que `_procurar` encontrou.

## Erros frequentes

O erro típico de cada ideia está na secção dela:

- a quantidade 6 tomada por seis objetos, em "Classes e objetos no programa";
- qualquer lista tomada por composição, em "O inventário no programa: composição e procura pelo código";
- a escrita em `artigo._quantidade`, que passa ao lado do setter, no passo 4 do exemplo guiado.

Ficam aqui os erros que aparecem quando se troca um método de um programa já escrito, como o `acertar` do exemplo guiado. Em cada um, lê a última linha da mensagem de erro, se houver uma: é a que diz o que aconteceu.

### O acerto continua sem efeito depois de escreveres o método

O que se vê: escreveste o método `acertar` do passo 4, executaste o programa de partida, e continua a aparecer `A02: 2`. Não aparece nenhuma mensagem de erro.

Porque acontece: o método novo ficou na classe ao lado do antigo, que tinha o `pass`, e o antigo ficou mais abaixo. Quando uma classe tem dois `def` com o mesmo nome, o Python guarda só o último. O método novo foi substituído pelo antigo, que não faz nada. É um erro de lógica: o programa corre e dá o resultado errado.

Como se corrige: apaga o método antigo, desde o `def acertar` até ao `pass`, para ficar um só `acertar` na classe. Procura no ficheiro todas as linhas que começam por `def acertar`: tem de haver só uma.

### `AttributeError: 'Inventario' object has no attribute 'acertar'`

O que se vê: o programa para na linha `inventario.acertar("A02", 5)`. Em português, a mensagem diz que o objeto do tipo `Inventario` não tem o atributo `acertar`. Um `AttributeError` ("erro de atributo") aparece quando se pede a um objeto um atributo ou um método que ele não tem.

Porque acontece: o método ficou fora da classe, com o `def` encostado à margem. O Python aceita-o como uma função solta, e o inventário fica sem o método.

Como se corrige: indenta todas as linhas do método quatro espaços, para ficarem dentro da classe. O `def` fica com quatro espaços, como os outros métodos, e as linhas de dentro com oito.

### `NameError: name '_procurar' is not defined`

O que se vê: o programa para dentro do método `acertar`, na linha que procura o artigo. Em português: o nome `_procurar` não está definido. Um `NameError` ("erro de nome") aparece quando se usa um nome que o Python não conhece. As versões recentes do Python acrescentam `Did you mean: 'self._procurar'?`, isto é, "querias dizer `self._procurar`?".

Porque acontece: a linha ficou escrita `artigo = _procurar(codigo)`, sem o `self.` à frente. O Python procura uma função solta com esse nome, e não a encontra.

Como se corrige: escreve `artigo = self._procurar(codigo)`, como em `quantidade_de` e em `retirar`. Dentro da classe, os métodos do próprio objeto alcançam-se através do `self`.

### Um `def` sem nada por baixo

O que se vê: o programa nem começa. A última linha da mensagem é `IndentationError: expected an indented block after function definition on line`, seguido de um número. Em português: esperava-se um bloco indentado a seguir à definição da função da linha indicada. Nas versões anteriores ao Python 3.10, a última linha diz só `IndentationError: expected an indented block`.

Porque acontece: apagaste a docstring e o `pass` do método `acertar` antes de escreveres as linhas novas, e o `def` ficou sem nenhuma instrução por baixo. É um erro de escrita, e o Python recusa o ficheiro antes de executar a primeira linha.

Como se corrige: escreve as linhas do método por baixo do `def`, com oito espaços. Se ainda não as tiveres, deixa o `pass` no lugar delas até as escreveres.

## Palavras novas deste guia

- `pass`: a instrução que não faz nada (do inglês, "passa"). Marca o sítio onde vai entrar código, ou dá a um bloco a instrução que ele precisa de ter.
- Programa principal: as linhas encostadas à margem, no fim do ficheiro, fora das classes. São elas que dizem o que o programa faz, e é por elas que se começa a ler.
- Ler um programa por zonas: começar pelo programa principal, depois ler os métodos que ele chama, e só depois as classes que esses métodos usam.

## Verificar o que aprendeste

Tenta responder sem olhar para o texto. Se uma pergunta te deixar com dúvidas, volta à secção indicada.

1. Quantas classes e quantos objetos dessas classes existem no programa de partida, e o que guarda cada objeto? ("Classes e objetos no programa")
2. Que tipo de erro tem o programa de partida: de escrita, de execução ou de lógica? Como se dá por ele? ("O programa de partida")
3. Que regras verifica o método `retirar` do artigo, e que regra fica para o setter? ("Encapsulamento no programa")
4. Porque é que, para verificar um pedido aceite, não basta ver que não apareceu nenhuma mensagem? ("O programa de partida" e "Encapsulamento no programa")
5. Porque é que a relação entre o inventário deste programa e os artigos é uma composição? O que teria de mudar no código para ser uma agregação? ("O inventário no programa: composição e procura pelo código")
6. Porque é que se acerta a quantidade, e não se usa o `adicionar`, depois de uma contagem à mão? (Exemplo guiado, passo 1)
7. Porque é que o método `acertar` escreve em `artigo.quantidade`, e não em `artigo._quantidade`? (Exemplo guiado, passo 4)
8. Segue o pedido `inventario.acertar("A01", -1)` até à linha que o recusa. Que métodos ficam a meio, e qual já tinha terminado? (Exemplo guiado, passo 7)
9. Descreve por palavras o estado da pasta no fim do programa do passo 6. Porque é que a identificas pelo código, e não por um nome do programa? (Exemplo guiado, passo 8)

## O que vem a seguir

Para praticar este tema, tens a [ficha de exercícios](06-sintese-exercicios.md) e o [laboratório](06-sintese-laboratorio.md). A ficha usa o programa do exemplo guiado: prevês quem responde a cada pedido, escreves um método novo do inventário e encontras o erro de um colega. O laboratório fecha o módulo e faz-se na aula, com o professor a acompanhar. Vais completar uma operação num programa parecido com o deste guia, explicar o modelo e mostrar o que acontece aos dados. No fim, explicas o teu trabalho ao professor numa conversa curta, sem nota.

Este é o último tema do M10. No fim do módulo escolhes o tema do teu [projeto](../projeto/README.md) e fazes o modelo da tua aplicação, descrito por palavras, como o do passo 8 do exemplo guiado. As ideias deste guia são avaliadas no projeto, no fim do M12. No módulo seguinte, o M11, vais reencontrá-las em JavaScript: os objetos, os contratos e o "quem sabe o quê" continuam a ser as mesmas perguntas.

![Rodapé](../imagens/rodape.png)

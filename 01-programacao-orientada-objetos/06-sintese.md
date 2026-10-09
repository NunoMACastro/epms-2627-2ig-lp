![Cabeçalho](../imagens/cabecalho.png)

# Juntar as ideias: um pequeno inventário em Python

*M10 · Caderno 6*

Nos cadernos 2, 3 e 4 construíste, uma peça de cada vez, um pequeno inventário de materiais. No caderno 2 viste que uma classe descreve todos os artigos e que cada artigo concreto é um objeto com o seu próprio estado. No caderno 3, o artigo aprendeu a proteger a sua quantidade: recusa um valor impossível com `ValueError` e, quando recusa, deixa os dados exatamente como estavam. No caderno 4, um objeto novo, o inventário, passou a criar e a guardar os artigos, a encontrá-los pelo código e a passar-lhes os pedidos.

Este caderno junta essas três ideias à volta de um único programa, que já vem quase todo escrito. Primeiro vais ler o programa e reconhecer nele cada ideia, com a indicação do caderno onde foi explicada. Depois acompanhas um exemplo guiado, que completa uma operação que o programa ainda não sabe fazer. Por fim, resolves três tarefas curtas, cada uma com uma pequena decisão que o exemplo guiado não tomou por ti. No fim do caderno há uma parte opcional, para quem quiser treinar com casos mais traiçoeiros.

O objetivo não é decorar sintaxe. É conseguires olhar para um programa com objetos e responder a três perguntas: que objetos existem e o que guarda cada um; quem decide se um pedido é aceite; e o que acontece aos dados quando um pedido é aceite e quando é recusado. São as perguntas que te vão ser feitas no trabalho de síntese do módulo, que o professor publica quando lá chegarmos.

## Antes de começares

Este caderno não traz matéria nova, a não ser uma pequena forma de desenhar objetos em UML leve, explicada no passo 8 do exemplo guiado. Usa o que foi explicado nos cadernos anteriores, e cada secção diz onde está a explicação completa:

- do caderno 2: classe, objeto ou instância, atributo, estado, construtor `__init__`, o parâmetro `self` e a chamada de um método com o ponto;
- do caderno 3: a propriedade `quantidade`, com getter e setter, o atributo interno `_quantidade`, o `raise ValueError`, o `try` e o `except`, e o contrato de uma operação;
- do caderno 4: a classe `Inventario`, com a lista interna `_artigos`, o método interno `_procurar`, os métodos `registar`, `quantidade_de` e `retirar`, o encaminhamento de um pedido, a diferença entre composição e agregação e a UML leve.

O caderno 5, sobre herança e polimorfismo, não é preciso para este caderno nem para o trabalho de síntese, e nenhum dos dois te pede herança. Se quiseres rever como a herança e a composição se distinguem, a secção 10 do caderno 5 compara-as, mas é leitura opcional.

Os programas completos correm sozinhos, como nos cadernos anteriores: copia-os para um ficheiro novo com a extensão `.py`, guarda-o e executa o ficheiro inteiro no editor de Python que usas nas aulas. Cada execução começa do zero, com os valores iniciais escritos no programa. Os excertos estão sempre assinalados, e o texto diz de que outro código dependem.

Conta com cerca de cinquenta minutos para as três tarefas da secção 7, depois de teres estudado as secções 1 a 6. A parte opcional leva mais cerca de vinte e cinco minutos.

## 1. Três ideias num só pedido

Imagina o inventário de uma sala com dois artigos: A01, Caderno, 6 unidades, e A02, Pasta, 2 unidades. Alguém pede ao inventário: "do artigo A01, retira 2 unidades". Vamos seguir este pedido devagar, porque nele aparecem as três ideias dos cadernos anteriores.

O pedido é feito ao inventário, e não ao artigo, porque quem o faz conhece o código A01, e não o objeto que o representa. O inventário é o único objeto que guarda todos os artigos, e por isso é o único que consegue procurar, entre eles, o que tem o código A01. Encontra-o e passa-lhe o pedido, sem verificar nada sobre as unidades. Esta é a ideia do caderno 4: o inventário reúne os artigos, encontra-os pelo código e encaminha os pedidos.

O artigo A01 recebe o pedido "retira 2". Verifica se o pedido faz sentido: 2 é um número inteiro e é positivo. Depois tenta guardar a nova quantidade, 6 - 2 = 4, e essa escrita passa pelo setter, que confirma que 4 é um inteiro não negativo e o guarda. Esta é a ideia do caderno 3: é o próprio artigo que decide se o pedido é possível e que protege a sua quantidade.

No fim, A01 tem 4 unidades e A02 continua com 2, porque o pedido nunca lhe foi feito. São dois objetos diferentes, feitos a partir da mesma classe, cada um com o seu estado. Esta é a ideia do caderno 2.

Agora o pedido seguinte: "do artigo A01, retira 9 unidades". O inventário encontra A01 e passa-lhe o pedido. O artigo verifica que 9 é inteiro e positivo, e tenta guardar 4 - 9 = -5. O setter recusa -5 com `ValueError`, antes de chegar à linha que guarda o valor. A quantidade continua 4. A exceção sobe até quem fez o pedido, que fica a saber que ele foi recusado e porquê.

E um terceiro pedido: "do artigo A07, retira 1 unidade". Desta vez, o inventário não encontra nenhum artigo com o código A07 e recusa o pedido ele próprio, também com `ValueError`. Nenhum artigo chega a ser contactado e nenhuma quantidade muda.

Repara que, nos três pedidos, cada objeto fez só a parte para a qual tem informação. O inventário sabe que artigos existem; não sabe as regras das unidades. O artigo sabe a sua quantidade e as regras dos pedidos; não sabe que outros artigos existem. Esta divisão é o que vamos encontrar no programa da secção 2.

A tabela seguinte serve de mapa para o resto do caderno. A coluna da direita diz onde cada ideia foi explicada pela primeira vez, para lá voltares se precisares.

| Ideia | Onde a vemos no exemplo | Secção deste caderno | Explicada no |
| --- | --- | --- | --- |
| Classe | A descrição comum de todos os artigos, `Artigo` | 3 | Caderno 2, secção 4 |
| Objeto ou instância | Os dois artigos concretos, A01 e A02, e o inventário | 3 | Caderno 2, secção 5 |
| Atributo e estado | Código, nome e quantidade de cada artigo, num dado momento | 3 | Caderno 2, secção 2 |
| Construtor e `self` | O que prepara cada artigo quando nasce | 3 | Caderno 2, secção 6 |
| Propriedade, getter e setter | A forma de ler e escrever a quantidade, que passa sempre pela verificação | 4 | Caderno 3, secções 9 e 10 |
| Encapsulamento | O artigo controla as alterações à sua quantidade | 4 | Caderno 3, secção 3 |
| Exceção `ValueError`, `try` e `except` | A recusa que quem fez o pedido não pode ignorar | 4 | Caderno 3, secções 7 e 8 |
| Composição | O inventário cria os seus artigos e guarda-os | 5 | Caderno 4, secções 7 e 8 |
| Procura pelo código | O inventário encontra o artigo A01 entre todos | 5 | Caderno 4, secção 10 |
| Encaminhamento | O inventário passa o pedido ao artigo, que decide | 5 | Caderno 4, secção 10 |

## 2. O programa de partida

Este é o programa à volta do qual trabalha todo o caderno. É o programa final do caderno 4, com as docstrings de `registar` e de `retirar` do inventário mais curtas, e com uma diferença: a classe `Inventario` tem um método a mais, `acertar`, que ainda não está escrito. As instruções das classes são as mesmas do caderno 4, e por isso o comportamento também é. Programa completo:

```python
class Artigo:
    """Artigo do inventário: código, nome e uma quantidade sempre válida.

    É a classe final do caderno 3, com as docstrings encurtadas.
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

        Ainda por escrever: o exemplo guiado da secção 6 completa este método.
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

### Como ler um programa destes sem te perderes

Um programa com mais de cem linhas não se lê de cima para baixo, linha a linha, na primeira vez. Lê-se por zonas, e começa-se pelo fim.

1. Começa pelo **programa principal**, as linhas encostadas à margem no fim do ficheiro, a partir de `inventario = Inventario()`. São elas que dizem o que o programa faz: cria um inventário, regista dois artigos, pede para acertar a quantidade de A02 para 5 e mostra as duas quantidades.
2. Depois procura, nas classes, os métodos que o programa principal chama: `registar`, `acertar` e `quantidade_de`, todos da classe `Inventario`. Repara que o programa principal nunca fala diretamente com um artigo; fala sempre com o inventário, usando os códigos.
3. Só depois desce à classe `Artigo`, para ver o que acontece quando o inventário passa um pedido a um artigo.

Não precisas de perceber todas as linhas antes de começares a trabalhar. Precisas de saber em que zona está cada coisa e de ir lá quando for preciso.

### Um programa que corre sem erros e não faz o que devia

O programa terminou sem nenhuma mensagem de erro. Mas pedimos para acertar a quantidade de A02 para 5, e a última linha mostra `A02: 2`. O pedido não teve efeito nenhum.

A razão está no método `acertar`. Por baixo da docstring tem apenas a instrução `pass`, que não faz nada. Está ali só para marcar, à vista, o sítio onde o código do método vai entrar. Quando o programa principal chama `inventario.acertar("A02", 5)`, o Python executa o método, encontra o `pass`, não faz nada e regressa. Nenhuma linha do método mexe em nenhum artigo.

Convém distinguir dois tipos de erro. Um **erro de sintaxe** impede o Python de perceber o programa: falta um parêntese, os dois pontos no fim de um `def`, ou uma linha está mal indentada. O programa nem chega a começar, e o Python mostra uma mensagem com `SyntaxError` ou `IndentationError`. Um **erro de comportamento** é diferente: o programa corre do princípio ao fim, sem nenhuma mensagem, mas faz uma coisa diferente da que o problema pede. O nosso programa tem um erro de comportamento, e é o tipo de erro mais difícil de apanhar, porque o Python não avisa de nada.

A única forma de apanhar um erro de comportamento é saber antes o que o programa devia mostrar e comparar com o que mostrou. Se não tivesses pensado que A02 devia ficar com 5, a linha `A02: 2` parecia perfeitamente normal. É por isso que, em todos os cadernos, escreves a previsão antes de executar: a previsão é o que te permite reparar que alguma coisa está errada.

## 3. Classes e objetos no programa

Esta secção recorda o caderno 2, apontando para as linhas do programa de partida.

A linha `class Artigo:` começa a **classe** `Artigo`, a descrição comum de todos os artigos: diz que cada artigo tem um código, um nome e uma quantidade, e que a cada artigo se pode pedir que adicione ou retire unidades. A classe não é nenhum artigo em particular. É como uma receita, que diz que ingredientes são precisos e que passos seguir, mas não é nenhum dos bolos feitos com ela.

Os artigos concretos são **objetos**, também chamados **instâncias** da classe `Artigo`. Cada um tem os seus **atributos**, com os seus valores, e o conjunto desses valores num dado momento é o **estado** do objeto. No programa de partida há dois artigos: um com o código A01, o nome Caderno e a quantidade 6, e outro com o código A02, o nome Pasta e a quantidade 2. Há também um terceiro objeto, de outra classe: o inventário, criado pela linha `inventario = Inventario()`. No total, o programa tem duas classes e três objetos.

O erro típico é pensar que a quantidade 6 quer dizer seis objetos. Não quer. Há um só objeto para o artigo A01, que guarda o número 6. O objeto é a ficha do material no registo, e não cada caderno que está no armário.

Os artigos nascem dentro do método `registar`, na linha `novo = Artigo(codigo, nome, quantidade)`. Quando essa linha é executada, o Python cria um objeto novo, do tipo `Artigo`, e chama o **construtor** `__init__` com o parâmetro `self` a apontar para esse objeto novo e os outros três parâmetros com os valores recebidos. O construtor guarda cada valor num atributo do objeto: `self.codigo = codigo` lê-se "guarda no atributo `codigo` deste objeto o valor que chegou no parâmetro `codigo`". O construtor é executado uma vez por cada artigo criado, e cada execução prepara um objeto diferente.

Dentro de qualquer método, `self` é o objeto sobre o qual o método está a trabalhar. Na chamada `artigo.retirar(unidades)`, que está no método `retirar` do inventário, o objeto que está antes do ponto, `artigo`, é o que ocupa o `self` do método `retirar` da classe `Artigo`. É por isso que a mesma linha de código, `self.quantidade = self.quantidade - unidades`, mexe no caderno quando o pedido é para o caderno e na pasta quando o pedido é para a pasta.

Os dois artigos são objetos diferentes, apesar de terem sido feitos a partir da mesma classe. Retirar unidades a um não tira nenhuma ao outro. Mas cuidado com os nomes: no caderno 2, secção 8, viste que uma variável é uma etiqueta colada num objeto, e não uma cópia dele. É isso que acontece quando `_procurar` devolve um artigo e o método do inventário o guarda no nome local `artigo`: esse nome passa a apontar para o próprio objeto que está na lista, e qualquer alteração feita através dele fica no artigo guardado no inventário.

## 4. Encapsulamento no programa

Esta secção recorda o caderno 3.

A regra da quantidade é uma **invariante**: tem de ser verdadeira durante toda a vida de um artigo, antes e depois de cada operação. A quantidade de um artigo é sempre um número inteiro maior ou igual a zero. O **encapsulamento** é a forma de organizar o programa para que seja o próprio artigo a garantir esta regra: o artigo guarda a quantidade e oferece operações para a consultar e para a alterar, e todas essas operações verificam antes de alterar.

No programa, a quantidade é uma **propriedade**. Por fora lê-se e escreve-se como um atributo normal, `artigo.quantidade`, mas por dentro cada leitura passa pelo getter e cada escrita passa pelo setter. O valor vive no atributo interno `_quantidade`, com sublinhado, que avisa por convenção que o código de fora não lhe deve mexer. O setter faz duas verificações, primeiro o tipo e depois o valor, e só na última linha guarda o valor. Se uma verificação falhar, `raise ValueError(...)` para o setter nessa linha, e a linha que guarda o valor nunca chega a ser executada. É assim que se escreve em Python a regra "verificar primeiro, alterar depois".

Repara que o construtor escreve `self.quantidade = quantidade`, sem sublinhado. A quantidade inicial passa pelo setter, como qualquer outra, e por isso um artigo com quantidade inválida nem chega a existir.

O método `retirar` do artigo divide o trabalho com o setter. O método verifica as regras do pedido: as unidades têm de ser um número inteiro e têm de ser 1 ou mais. O setter verifica a regra do estado: a quantidade que resultaria do pedido não pode ser negativa. Não haver unidades suficientes é o mesmo que a nova quantidade ser negativa, e por isso é o setter que recusa esse caso, com a mensagem "A quantidade não pode ser negativa.". Cada regra está escrita num só sítio.

Quando um pedido é recusado, quem o fez fica a saber através da exceção. Se o pedido estiver dentro de um `try` com `except ValueError as erro`, o Python abandona o `try` na linha que falhou, salta para o `except`, e o nome `erro` passa a referir a exceção, cuja mensagem se pode mostrar com `print`. Se não houver nenhum `try`, o programa para e o Python mostra a mensagem, com as linhas do `Traceback` por cima. A classe decide se o pedido é válido; quem usa a classe decide o que fazer com a recusa.

Para verificar uma operação recusada, nunca basta ver a mensagem. É preciso confirmar também que o estado não mudou. E, para verificar uma operação aceite, também não basta ver que não houve mensagem: o programa de partida acabou de te mostrar um método que não lançou exceção nenhuma e não fez nada.

## 5. O inventário no programa: composição e procura pelo código

Esta secção recorda o caderno 4.

O inventário existe porque há regras e perguntas sobre o conjunto dos artigos que nenhum artigo consegue responder sozinho: que artigos existem, se um código já está a ser usado, qual é o artigo com um certo código. Uma tarefa fica com quem tem a informação necessária para a fazer, e só o inventário conhece todos os artigos.

### Como o inventário encontra um artigo

O método interno `_procurar` percorre a lista `_artigos` com um ciclo `for` e compara o código de cada artigo com o código procurado. Assim que o encontra, o `return` devolve esse artigo e termina o método, mesmo a meio do ciclo. Se o ciclo acabar todas as voltas sem encontrar nenhum, chega-se à linha do `raise`, que está depois do ciclo, e o método lança `ValueError` com a mensagem "Não existe nenhum artigo com o código ...". O nome começa por sublinhado porque é uma ferramenta interna, para os métodos do próprio inventário usarem.

Os métodos `quantidade_de` e `retirar` do inventário começam os dois com `artigo = self._procurar(codigo)`. O `self.` é obrigatório: é através dele que um método chega aos outros métodos do mesmo objeto. Se o código não existir, `_procurar` lança a exceção e o método que o chamou é interrompido nessa mesma linha.

### Encaminhar o pedido sem repetir as regras

O método `retirar` do inventário tem só duas linhas: encontra o artigo e passa-lhe o pedido, com `artigo.retirar(unidades)`. A esta forma de colaborar chama-se **encaminhamento**. O inventário não verifica se as unidades são um inteiro, nem se são positivas, nem se chegam, porque essas regras são do artigo e já estão escritas no artigo. Se o artigo recusar, a exceção nasce no artigo, atravessa o método do inventário, que não a apanha, e chega a quem fez o pedido. O inventário não apanha a exceção porque não sabe o que fazer com uma recusa: quem sabe é o programa principal.

### Composição: o inventário cria os seus artigos

A relação entre `Inventario` e `Artigo` é uma relação "tem": um inventário tem artigos. O caderno 4, na secção 7, distingue dois graus desta relação com quatro perguntas, das quais as duas primeiras decidem: a parte faz sentido sem o todo? E quem cria a parte?

Neste programa, quem cria os artigos é o inventário, dentro do seu método `registar`. É lá, e só lá, que aparece `Artigo(...)`. O programa principal não cria nenhum artigo nem guarda nenhum artigo num nome seu: só tem o nome `inventario` e fala com ele através dos códigos. E o artigo, que é uma linha do registo deste inventário, não faz sentido sem ele. Por isso a relação é uma **composição**, e o diagrama de classes desenha-a com um losango cheio do lado do inventário.

Seria uma **agregação** se o inventário recebesse artigos já criados fora dele, como a playlist da secção 12 do caderno 4 recebe músicas que já existem. Nesse caso, o programa principal teria linhas como `caderno = Artigo("A01", "Caderno", 6)` e o inventário teria um método que recebe esse objeto e o junta à lista, e o diagrama mostraria um losango vazio. A tabela da secção 13 do caderno 4 diz o mesmo de forma curta: há losango cheio quando o todo cria as partes dentro de um método seu e não as entrega a quem está de fora; há losango vazio quando o todo tem um método que recebe objetos já criados e os junta à lista.

O erro típico é chamar composição a qualquer objeto que guarda uma lista de outros objetos. A lista, sozinha, não decide nada: a playlist também guarda uma lista. O que decide é quem chama o construtor da parte e se a parte tem vida fora do todo. Antes de escolheres o losango, procura no código a linha onde a parte é criada.

## 6. Exemplo guiado: completar o método `acertar`

Vamos agora completar o método `acertar`, acompanhando o raciocínio do princípio ao fim. Repara que o exemplo usa as três ideias ao mesmo tempo, e que é isso que o torna um bom exemplo de síntese.

### Passo 1: perceber o que o método tem de fazer

De vez em quando, alguém conta à mão o material que está no armário. Imagina que, ao contar as pastas, encontra 5, mas o programa diz que há 2: alguém arrumou três pastas e esqueceu-se de as registar. Acertar a quantidade é escrever no artigo o valor contado, para o programa voltar a dizer a verdade.

Podias perguntar porque não se usa o método `adicionar`, com 3 unidades. Há duas razões. A primeira é que quem conta sabe o total, 5, e não a diferença; teria de fazer a conta à mão, e uma conta à mão é mais uma oportunidade de engano. A segunda é que a contagem pode dar menos do que o registado, se alguém levou material sem registar, e então seria preciso retirar, e não adicionar. Acertar serve para os dois casos: escreve-se o valor contado, seja ele maior ou menor do que o anterior.

O caderno 3, secção 4, já tinha esta operação na interface pública do artigo: "acertar a quantidade", que se faz escrevendo na propriedade, como em `artigo.quantidade = 5`. O que falta é poder fazê-lo através do inventário, a partir do código, porque o programa principal não guarda nenhum artigo num nome seu.

### Passo 2: decidir quem faz o quê

Antes de escrever, aplicamos a regra do caderno 4: cada tarefa fica com quem tem a informação necessária para a fazer.

| Tarefa | Que informação é precisa | Quem a tem | Fica a cargo de |
| --- | --- | --- | --- |
| Encontrar o artigo com este código | Os códigos de todos os artigos | O inventário | O método `_procurar` do inventário |
| Decidir se o valor contado é uma quantidade válida | A regra da quantidade | O artigo | O setter da quantidade |
| Guardar o novo valor | O atributo interno `_quantidade` | O artigo | O setter da quantidade |

A tabela diz-nos uma coisa importante sobre o que o método `acertar` não deve fazer: não deve verificar se o valor é inteiro, nem se é negativo. Essa regra já vive no setter, e escrevê-la outra vez no inventário seria ter a mesma regra em dois sítios, com o risco de um dia mudar num e esquecer no outro. O inventário encontra o artigo e escreve na propriedade; a verificação acontece sozinha, porque escrever na propriedade é chamar o setter.

### Passo 3: escrever o contrato

Como nos cadernos 3 e 4, começamos pelo que o método promete, antes de pensar em como o escrever.

O método recebe o código de um artigo e a quantidade contada. Não devolve nada. Falha, com `ValueError`, em dois casos: se não houver nenhum artigo com esse código, e quem recusa é `_procurar`; ou se a quantidade contada for inválida, e quem recusa é o setter do artigo. Em qualquer dos dois casos, nenhuma quantidade muda. Quando não falha, a quantidade do artigo passa a ser exatamente o valor contado.

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

A primeira, `artigo = self._procurar(codigo)`, é igual à primeira linha de `quantidade_de` e de `retirar`. Se o código não existir, `_procurar` lança `ValueError` e o método `acertar` é interrompido aqui, sem chegar à segunda linha. Se existir, o nome local `artigo` passa a apontar para o próprio artigo guardado na lista.

A segunda, `artigo.quantidade = nova_quantidade`, é uma escrita na propriedade `quantidade` desse artigo. Para o Python, escrever na propriedade é chamar o setter, com o valor da direita no parâmetro `valor`. O setter faz as suas duas verificações e só depois guarda o valor em `_quantidade`. Se o valor for inválido, o setter lança `ValueError` antes de o guardar, e a quantidade fica como estava.

Repara no que esta linha não faz: não escreve em `artigo._quantidade`. O inventário é código de fora da classe `Artigo`, e o código de fora usa a interface pública do artigo, que é a propriedade, e não o atributo interno. Se escrevesse em `_quantidade`, passava ao lado do setter, e um acerto para -1 seria aceite em silêncio.

### Passo 5: prever antes de executar

Antes de executarmos, fazemos o traço de quatro pedidos seguidos a um inventário com A01 a 6 e A02 a 2. Cada linha começa no estado deixado pela anterior. A coluna "Quem responde" diz que peça do programa aceitou ou recusou o pedido.

| Pedido | Quem responde | Resposta | A01 depois | A02 depois |
| --- | --- | --- | ---: | ---: |
| `acertar("A02", 5)` | `_procurar` encontra A02; o setter recebe 5, que é válido | Aceite | 6 | 5 |
| `acertar("A01", -1)` | `_procurar` encontra A01; o setter recebe -1, que é negativo | `ValueError` lançado pelo setter | 6 | 5 |
| `acertar("A09", 3)` | `_procurar` não encontra A09 | `ValueError` lançado pelo inventário | 6 | 5 |
| `retirar("A02", 4)` | `_procurar` encontra A02; o artigo aceita, 5 - 4 = 1 | Aceite | 6 | 1 |

A última linha mostra porque é que o acerto importa: a retirada de 4 pastas só é possível porque o programa passou a saber que havia 5. Antes do acerto, com 2 pastas registadas, esse pedido seria recusado.

### Passo 6: executar e comparar com o traço

Programa completo, com o método `acertar` já escrito:

```python
class Artigo:
    """Artigo do inventário: código, nome e uma quantidade sempre válida.

    É a classe final do caderno 3, com as docstrings encurtadas.
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

Compara linha a linha com o traço do passo 5. O acerto de A02 foi aceite e a quantidade passou a 5. As duas recusas aparecem pela ordem do traço, e cada mensagem diz quem recusou: "A quantidade não pode ser negativa." vem do setter do artigo, e "Não existe nenhum artigo com o código A09." vem do inventário. A retirada de 4 pastas foi aceite e deixou 1. As duas últimas linhas confirmam o estado final: A01, que só recebeu um pedido recusado, continua com 6.

Repara também nos acertos aceites: não mostram nada. Um método que cumpre o pedido termina sem erro e em silêncio, e é por isso que o programa mostra a quantidade a seguir, para termos a prova de que o acerto aconteceu. Foi exatamente essa prova que faltou ao programa de partida, quando o `acertar` ainda só tinha o `pass`.

### Passo 7: seguir o caminho de uma recusa

Vale a pena seguir o pedido `inventario.acertar("A01", -1)` até ao fim, como no caderno 4, secção 11, se fez com uma retirada.

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

O método `_procurar` não está na tabela, porque já tinha terminado quando a exceção nasceu. Repara também que esta cadeia é mais curta do que a da retirada no caderno 4: entre o inventário e o setter não há nenhum método do artigo. A escrita na propriedade chama o setter diretamente, a partir da linha do inventário.

### Passo 8: o modelo em UML leve

Com o método novo, a caixa da classe `Inventario` ganha uma linha na zona dos métodos:

```text
+------------------------------------------+
| Inventario                               |
+------------------------------------------+
|                                          |
+------------------------------------------+
| registar(codigo, nome, quantidade)       |
| quantidade_de(codigo)                    |
| retirar(codigo, unidades)                |
| acertar(codigo, nova_quantidade)         |
+------------------------------------------+
```

A zona dos atributos continua vazia, pela razão da secção 8 do caderno 4: a lista `_artigos` é representada pela linha que liga as duas caixas, e não se escreve dentro da caixa. O método `_procurar` também não aparece, porque é interno e não faz parte da interface pública. A caixa da classe `Artigo` é a da secção 5 do caderno 4.

A ligação entre as duas classes é a composição da secção 5 deste caderno, desenhada como no diagrama da secção 8 do caderno 4: uma linha com um losango cheio encostado a `Inventario`, o `1` junto de `Inventario` e o `0..*` junto de `Artigo`.

![Diagrama de classes do caderno 4: Inventario, com os métodos registar(codigo, nome, quantidade), quantidade_de(codigo) e retirar(codigo, unidades), ligado a Artigo por uma linha com um losango cheio do lado de Inventario, com 1 do lado do inventário e 0..* do lado do artigo](../imagens/uml-inventario-artigo.svg)

Lê as multiplicidades nos dois sentidos, como no caderno 4, secção 6: um inventário tem de zero a muitos artigos, e cada artigo pertence a exatamente um inventário.

O diagrama de classes não tem valores. Para mostrar o estado dos artigos no fim do programa do passo 6, usamos caixas de objeto. Como os artigos não têm nome no programa principal, o título de cada caixa diz só a classe, precedida de dois pontos, e o código fica nos atributos:

```text
+------------------------+      +------------------------+
| : Artigo               |      | : Artigo               |
+------------------------+      +------------------------+
| codigo = "A01"         |      | codigo = "A02"         |
| nome = "Caderno"       |      | nome = "Pasta"         |
| quantidade = 6         |      | quantidade = 1         |
+------------------------+      +------------------------+
```

Um título começado por dois pontos, sem nada antes, quer dizer "um objeto da classe `Artigo`, sem nome no programa". É a forma de a UML desenhar um objeto anónimo, e é o caso dos nossos artigos: o programa principal chega a eles pelo inventário e pelo código, e não por um nome seu.

## 7. Agora experimenta

As três tarefas seguintes usam o programa completo do passo 6, com o método `acertar` já escrito. Cada uma pede uma decisão pequena que o exemplo guiado não tomou por ti. Quando uma tarefa tiver um excerto, copia o programa do passo 6 e substitui as linhas que vêm depois das classes, a partir de `inventario = Inventario()`, pelas linhas do excerto. Escreve sempre a tua previsão antes de executar e, se a execução der outra coisa, procura a explicação em vez de mudar a previsão. Entrega as respostas pelo meio indicado pelo professor.

### Tarefa 1: prever quem responde a cada pedido (15 min)

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

### Tarefa 2: perguntar ao inventário se um código existe (20 min)

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

### Tarefa 3: encontrar o erro de um colega (15 min)

Um colega escreveu esta versão do método `acertar`. É um excerto: para a experimentares, substitui o `acertar` da classe `Inventario` do programa do passo 6 por este.

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
2. Executa com a versão do colega e assinala as linhas que são diferentes da tua resposta à alínea 1.
3. Explica o erro, por palavras, em duas ou três frases. A tua explicação tem de dizer para que objeto aponta o `self` dentro deste método e o que acontece, por isso, ao valor 5 e ao valor -1.
4. Corrige o método, mudando uma única linha, e executa outra vez para confirmares que as três linhas passam a ser as da alínea 1.

### Para ires mais longe

Esta parte é opcional e fica fora dos cinquenta minutos das tarefas. Tem casos que enganam e uma pergunta de modelação, para quem acabou as três tarefas e quer treinar mais. Cada uma diz quanto tempo leva, e podes fazer só uma.

#### Mais longe 1: pedidos que enganam (10 min)

Cada linha da tabela é um caso separado, num inventário acabado de criar com A01 a 6 e A02 a 2, como no excerto da tarefa 1. Para cada pedido, escreve quem responde, a mensagem que aparece, e se o programa continua ou para. Depois confirma, escrevendo cada pedido dentro de um `try` com `except ValueError as erro`.

| Pedido | Quem responde | Mensagem | O programa continua ou para? |
| --- | --- | --- | --- |
| `acertar("A01", "7")` | A completar | A completar | A completar |
| `acertar("a01", 7)` | A completar | A completar | A completar |
| `acertar("A01", 7.0)` | A completar | A completar | A completar |
| `acertar(1, 7)` | A completar | A completar | A completar |

O último pedido tem uma surpresa. Se o programa parar, lê a última linha da mensagem de erro e explica porque é que o `except ValueError` não a apanhou.

#### Mais longe 2: uma variante com artigos criados fora (15 min)

Um colega propõe acrescentar à classe `Inventario` do programa do passo 6 este método, para poder juntar ao inventário artigos que já existem:

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
2. Com o método `acrescentar`, a relação entre `Inventario` e `Artigo` passa a ser uma composição ou uma agregação? Responde com as duas perguntas que decidem, da secção 7 do caderno 4, e diz que losango desenharias.
3. Explica porque é que a sala 14 mostra a quantidade que mostra, se ninguém lhe pediu nenhuma retirada.
4. Para o inventário de uma sala, em que as 6 unidades de A01 são as que estão naquela sala, qual das duas versões te parece mais adequada: a do `registar` ou a do `acrescentar`? Justifica em duas frases.

## Antes do trabalho de síntese

Tenta responder a estas perguntas sem olhar para o texto. Se alguma te deixar com dúvidas, volta à secção indicada.

- Consegues dizer quantas classes e quantos objetos existem no programa de partida, e o que guarda cada objeto? (secção 3)
- Consegues explicar a diferença entre um erro de sintaxe e um erro de comportamento, e como se apanha um erro de comportamento? (secção 2)
- Consegues dizer que regras verifica o método `retirar` do artigo e que regra fica para o setter? (secção 4)
- Consegues explicar porque é que verificar uma operação aceite exige olhar para o estado, e não só para a ausência de mensagem? (secções 2 e 4)
- Consegues explicar, a partir do código, porque é que a relação entre o inventário deste programa e os artigos é uma composição, e o que teria de mudar para ser uma agregação? (secção 5)
- Consegues seguir um pedido feito ao inventário até à linha que decide se ele é aceite? (secção 6, passo 7)
- Consegues explicar porque é que o método `acertar` escreve em `artigo.quantidade` e não em `artigo._quantidade`? (secção 6, passo 4)

No fim do módulo vais fazer o trabalho de síntese: completar uma operação num programa parecido com o deste caderno, explicar o modelo e mostrar o que acontece aos dados, e depois explicar o teu trabalho ao professor. O enunciado é publicado na [pasta das avaliações](../avaliacoes/README.md) quando a turma lá chegar.

![Rodapé](../imagens/rodape.png)

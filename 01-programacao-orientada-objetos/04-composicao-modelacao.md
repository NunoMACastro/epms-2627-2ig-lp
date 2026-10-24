![Cabeçalho](../imagens/cabecalho.png)

# Composição e modelação

Módulo M10, Introdução à Programação Orientada por Objetos. Neste guia reúnes os artigos num inventário e estudas as relações entre objetos, sobretudo a composição. Aprendes a decidir como se relacionam duas classes, a descrevê-las por palavras e a escrever em Python a classe `Inventario`. Lês o guia ao teu ritmo, de preferência em mais do que uma vez, e o que não acabares na aula acabas em casa ou na aula seguinte. Para praticar, há o [laboratório](04-composicao-modelacao-laboratorio.md) e a [ficha de exercícios](04-composicao-modelacao-exercicios.md) deste tema.

No guia anterior, [Encapsulamento e contratos](03-encapsulamento-contratos.md), cada artigo aprendeu a proteger a sua quantidade. Recusa um pedido impossível com `ValueError` e, quando recusa, deixa os dados exatamente como estavam. Um inventário, porém, não é um artigo sozinho: é um conjunto de artigos. E há perguntas sobre esse conjunto que nenhum artigo consegue responder por si. Que artigos existem? Há dois artigos com o mesmo código? Quantas unidades tem o artigo com o código A02? Para responder a estas perguntas precisamos de um objeto novo, o inventário, que reúne os artigos e fala com eles.

Este guia trata das relações entre objetos. Vamos ver que se podem fazer duas perguntas muito diferentes sobre duas classes: "uma tem a outra?" e "uma é um caso da outra?". Vamos distinguir dois graus da relação "tem", a composição e a agregação. Vamos aprender a descrever por palavras as classes e as ligações entre elas, antes de escrever código. E vamos escrever, passo a passo, a classe `Inventario` em Python.

Os programas completos correm sozinhos, como nos guias anteriores: copia-os para um ficheiro `.py` e executa o ficheiro inteiro, no editor de Python que usas nas aulas. Funcionam com o Python 3, a partir da versão 3.10. Cada execução começa do zero, com os valores escritos no programa. Os excertos estão sempre assinalados, e o texto diz de que outro código dependem.

Para os programas não ficarem demasiado compridos, a classe `Artigo` aparece neles com as docstrings mais curtas do que no guia 03. As instruções são exatamente as mesmas, e por isso o comportamento também é: as mesmas verificações, pela mesma ordem, com as mesmas mensagens.

## Neste guia

1. O que vais aprender
2. O que já sabes e vais usar
3. No papel, antes do código:
   - Artigos soltos: o que nenhum artigo consegue garantir
   - Quem sabe o quê: responsabilidades
   - Duas perguntas sobre duas classes: "tem" e "é um"
   - Duas árvores que se parecem e dizem coisas diferentes
   - Dois graus de "tem": composição e agregação
   - O nosso inventário: composição
   - O inventário descrito por palavras
4. Do papel ao Python:
   - Recordar as listas e o ciclo `for`
   - Agregação em Python: a playlist e as músicas
   - Da descrição ao código, e do código à descrição
5. Exemplo guiado: construir a classe `Inventario`
6. Erros frequentes
7. Palavras novas deste guia
8. Verificar o que aprendeste
9. O que vem a seguir

## O que vais aprender

No fim deste guia, consegues:

- explicar porque é que é preciso um objeto que reúna os artigos, e decidir que classe fica com cada tarefa;
- distinguir a relação "tem" da relação "é um", analisando o seu significado e aplicando o teste do "tudo o que B tem e faz";
- decidir entre composição e agregação com quatro perguntas, e justificar a decisão;
- descrever por palavras as classes de um programa e a relação entre elas, com o que cada objeto guarda e o que se lhe pode pedir;
- escrever em Python uma classe que cria outros objetos, os guarda numa lista e lhes passa os pedidos, como o `Inventario`;
- seguir o caminho de uma recusa que atravessa vários métodos até ser apanhada.

## O que já sabes e vais usar

- O artigo do inventário: uma referência de material, isto é, uma linha do registo, com código, nome e quantidade. Representar um problema é escolher o que interessa. Guia [01 Entidades, estado e ações](01-entidades-estado-acoes.md), em "A informação que interessa guardar".
- As três regras do inventário, a começar por "cada código identifica um único artigo": guia [01](01-entidades-estado-acoes.md), em "Uma operação tem de respeitar regras".
- O problema das variáveis soltas: guia [01](01-entidades-estado-acoes.md), em "Duas maneiras de organizar um programa".
- O traço, a tabela que regista o que acontece em cada passo de uma sequência de instruções: guia [01](01-entidades-estado-acoes.md), em "Exemplo guiado: seguir os valores passo a passo".
- Classe, instância, o construtor `__init__`, o `self` e a chamada de um método com o ponto. Estão no guia [02 Objetos, classes e instâncias](02-objetos-classes-instancias.md), de "Classe: a descrição comum" a "O método retirar em Python".
- A classe como descrição comum, que diz por palavras o que todos os objetos de um tipo têm e o que se lhes pode pedir. Guia [02](02-objetos-classes-instancias.md), em "Classe: a descrição comum".
- O estado de um objeto, o conjunto dos valores dos seus atributos num dado momento: guia [02](02-objetos-classes-instancias.md), em "Um objeto reúne dados e operações".
- Uma classe nova só se justifica quando os objetos têm dados ou operações diferentes: não há uma classe `Caderno` e outra `Pasta`. Guia [02](02-objetos-classes-instancias.md), em "Classe: a descrição comum".
- Dois nomes podem apontar para o mesmo objeto, como duas etiquetas na mesma caixa, e o `is` confirma-o: guia [02](02-objetos-classes-instancias.md), em "Cada instância é um objeto diferente".
- A classe `Artigo` do fim do guia 03, com a propriedade `quantidade`. O getter (do inglês *get*, obter) lê o valor. O setter (de *set*, pôr) verifica-o e guarda-o no atributo interno `_quantidade`. Guia [03 Encapsulamento e contratos](03-encapsulamento-contratos.md), em "Propriedades: `@property`" e "O construtor também passa pelo setter".
- A exceção `ValueError` ("erro de valor"), lançada com `raise`, e a regra "verificar primeiro, alterar depois": guia [03](03-encapsulamento-contratos.md), em "Recusar a sério: `ValueError` e `raise`". Na mesma secção está a mensagem de erro que começa por `Traceback`, que se lê de baixo para cima.
- O `isinstance(valor, int)`, que pergunta se o valor é um inteiro (*is instance*, "é instância de"), e o `not`, que inverte a resposta. Estão no guia [03](03-encapsulamento-contratos.md), em "Primeiro passo: métodos get e set" e "Recusar a sério: `ValueError` e `raise`".
- Os três tipos de erro. O de escrita, o Python encontra-o antes de o programa começar. O de execução para o programa a meio. No de lógica, o programa corre e dá um resultado errado. Guia [03](03-encapsulamento-contratos.md), em "Nada impede uma quantidade impossível".
- O `try` e o `except`, e a divisão de tarefas. Quem lança a exceção decide se o pedido é válido, e quem a apanha decide o que fazer com a recusa. Guia [03](03-encapsulamento-contratos.md), em "Tratar a recusa: `try` e `except`".
- A interface pública, aquilo que um objeto deixa usar a quem está de fora: guia [03](03-encapsulamento-contratos.md), em "Interface pública: aquilo que o objeto deixa usar".
- O sublinhado no início de um nome, como em `_quantidade`, que avisa que esse nome é interno da classe: guia [03](03-encapsulamento-contratos.md), em "O sublinhado: um atributo privado por convenção".
- O contrato de uma operação, o valor `None` (do inglês, "nenhum") e os métodos `adicionar` e `retirar` do artigo. Estão no guia [03](03-encapsulamento-contratos.md), em "Adicionar: uma operação com contrato" e "Exemplo guiado: construir o método retirar".
- A diferença entre as regras do pedido e as regras do estado: o setter protege o estado, mas não sabe o que o pedido quer dizer. Guia [03](03-encapsulamento-contratos.md), no passo 3 de "Exemplo guiado: construir o método retirar".
- O zero no estado e o zero no pedido: guia [03](03-encapsulamento-contratos.md), em "As regras que devem continuar verdadeiras".
- As listas e o ciclo `for`: do 10.º ano. Como vamos usá-los de uma maneira nova, para guardar objetos, a secção "Recordar as listas e o ciclo `for`" explica-os do princípio.
- As condições com `if` e `elif`, as funções com `def` e `return`, o texto entre aspas e o `print` com vários valores: do 10.º ano.
- A docstring, o texto entre três aspas que explica uma função, uma classe ou um método: guia [01](01-entidades-estado-acoes.md), em "Duas maneiras de organizar um programa".

## Artigos soltos: o que nenhum artigo consegue garantir

Começamos com três artigos criados a partir da classe final do guia 03, cada um no seu nome. É um programa completo.

Antes de correres este programa, tenta prever: o Python aceita os três artigos, ou recusa algum deles? Olha para os códigos e para as quantidades das três linhas que criam os artigos.

```python
# Três artigos soltos, cada um no seu nome: o primeiro programa do guia 04.

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


caderno = Artigo("A01", "Caderno", 6)
pasta = Artigo("A02", "Pasta", 2)
cola = Artigo("A01", "Cola", 3)

print(caderno.codigo, caderno.nome, caderno.quantidade)
print(pasta.codigo, pasta.nome, pasta.quantidade)
print(cola.codigo, cola.nome, cola.quantidade)
```

O programa mostra:

```text
A01 Caderno 6
A02 Pasta 2
A01 Cola 3
```

Leitura guiada: a classe é a do fim do guia 03, e não precisas de a ler de novo linha a linha. Lê as três linhas que criam os artigos, cada uma com o seu nome, e depois os três `print`, que mostram os três atributos de cada artigo.

O Python aceitou os três artigos. As três quantidades são válidas, e o setter verificou cada uma delas. Mas o caderno e a cola ficaram com o mesmo código, A01. No guia 01 escrevemos três regras para o inventário, e a primeira era esta: cada código identifica um único artigo. Esta regra acabou de ser quebrada, e nenhuma parte do programa deu por isso.

Podias pensar que bastava acrescentar uma verificação ao construtor do `Artigo`. Pensa, no entanto, no que o construtor sabe no momento em que a cola está a ser criada. Sabe o que recebeu nos parâmetros: `"A01"`, `"Cola"` e `3`. Sabe que `self` é o objeto novo, a cola. E não sabe mais nada. O caderno, criado duas linhas acima, é outro objeto, guardado num nome do programa principal. Nada dentro da classe `Artigo` lhe dá acesso a esse nome. Um artigo conhece os seus próprios dados, e só esses. Para saber se um código já está a ser usado é preciso conhecer todos os artigos, e nenhum artigo os conhece.

Há outras perguntas que ficam sem dono. Imagina que alguém escreve o código A02 e quer saber quantas unidades tem esse artigo. Tu sabes, ao ler o programa, que o artigo A02 está guardado no nome `pasta`. O programa não sabe: para ele, `pasta` é só um nome, e o código A02 está escondido dentro do objeto. Para encontrar o artigo a partir do código, o programa teria de comparar o código pedido com o código de cada artigo, um a um. Seria uma cadeia de condições como esta, que é um excerto: depende dos três artigos criados no programa acima.

```python partial
codigo_pedido = "A02"
if codigo_pedido == caderno.codigo:
    print(caderno.quantidade)
elif codigo_pedido == pasta.codigo:
    print(pasta.quantidade)
elif codigo_pedido == cola.codigo:
    print(cola.quantidade)
```

Cada artigo novo obrigaria a acrescentar um nome novo ao programa e uma condição nova a esta cadeia, escritos à mão. É o problema das variáveis soltas do guia 01, agora um degrau acima. No guia 01 eram o código, o nome e a quantidade que andavam soltos em variáveis separadas, e a classe `Artigo` juntou-os num objeto. Agora são os próprios artigos que andam soltos, em nomes separados. A ligação entre eles só existe na cabeça de quem escreveu o programa.

A solução segue o mesmo caminho: juntar numa unidade aquilo que tem de estar junto. Vamos criar um objeto cuja tarefa é guardar os artigos todos e responder às perguntas sobre o conjunto. Esse objeto é o inventário.

## Quem sabe o quê: responsabilidades

Antes de escrevermos a classe do inventário, temos de decidir o que fica a cargo dela e o que continua a cargo de cada artigo. Chamamos **responsabilidades** de uma classe ao que os seus objetos sabem e ao que fazem. Decidir as responsabilidades é decidir, para cada tarefa do programa, qual é a classe que fica encarregada dela.

Há uma regra simples que resolve a maior parte das decisões: uma tarefa fica com quem tem a informação necessária para a fazer. Aplicada ao nosso problema, dá esta tabela:

| Pergunta ou tarefa | Que informação é precisa | Quem a tem | Fica a cargo de |
| --- | --- | --- | --- |
| Quantas unidades tem este artigo? | A quantidade desse artigo | O próprio artigo | `Artigo` |
| Posso retirar 2 unidades deste artigo? | A quantidade e as regras dos pedidos | O próprio artigo | `Artigo` |
| Que artigos existem? | A lista de todos os artigos | Quem guarda todos | `Inventario` |
| Já existe um artigo com o código A01? | Os códigos de todos os artigos | Quem guarda todos | `Inventario` |
| Qual é o artigo com o código A02? | Os códigos de todos os artigos | Quem guarda todos | `Inventario` |

Repara que nenhuma linha passa do artigo para o inventário, nem ao contrário, sem uma razão. O inventário não fica a verificar se há unidades suficientes, porque essa regra já vive no artigo. O guia 03 mostrou o que custa escrever a mesma regra em dois sítios: basta mudá-la num sítio e esquecê-la no outro para o programa ficar incoerente. E o artigo não fica a verificar se o seu código é único. Para isso teria de conhecer todos os outros artigos, e então cada artigo passaria a carregar o inventário inteiro dentro de si.

Separar responsabilidades não quer dizer que cada objeto trabalhe isolado. O inventário e os artigos vão colaborar. Quando alguém pedir ao inventário para retirar 2 unidades do artigo A01, o inventário encontra o artigo A01, porque conhece todos, e passa-lhe o pedido. O artigo decide se o pedido é possível, porque conhece a sua quantidade e as regras. Cada um faz a parte que sabe fazer. No exemplo guiado, no fim da matéria, vamos dar nome a esta passagem do pedido e escrevê-la em Python.

## Duas perguntas sobre duas classes: "tem" e "é um"

Quando duas classes estão relacionadas, a primeira coisa a decidir é o tipo de relação. Há duas relações que aparecem constantemente e que convém não confundir.

A primeira é a relação **"tem"**. Um inventário tem artigos. Uma encomenda tem linhas. Uma turma tem alunos. É a relação entre um todo e as suas partes, ou entre um objeto e outros objetos que ele guarda e usa. Também se diz "contém" ou "é formado por".

A segunda é a relação **"é um"**. Um carro é um veículo. Uma bicicleta também é um veículo. É a relação entre um tipo particular e um tipo mais geral. Tudo o que é verdade para qualquer veículo, por exemplo transportar pessoas de um sítio para outro, também é verdade para um carro. O carro é um caso particular de veículo, com mais pormenores.

Para decidir, analisa a relação entre as duas classes e verifica qual das frases a descreve corretamente.

- "Um inventário tem artigos." Verdadeira.
- "Um inventário é um artigo." Falsa.
- "Um carro é um veículo." Verdadeira.
- "Um carro tem um motor." Verdadeira, e repara que o motor não é um carro nem o carro é um motor.

Às vezes a frase "é um" parece quase verdadeira, e é preciso um teste mais cuidadoso. O teste é este: se A é um B, então tudo o que um B tem e tudo o que um B faz tem de fazer sentido para um A. Vamos aplicá-lo à frase "um inventário é um artigo". Um artigo tem um código, um nome e uma quantidade. Qual seria a quantidade de um inventário? O inventário tem artigos com 6, 2 e 10 unidades, de materiais diferentes. Não há um número que seja "a quantidade do inventário". Um artigo aceita o pedido "retirar 2 unidades". Retirar 2 unidades de um inventário, sem dizer de que artigo, não quer dizer nada. O teste falha, e por isso o inventário não é um artigo.

O erro típico é pensar que o inventário é "um artigo maior, com muitos artigos lá dentro". Essa ideia mistura as duas relações: ter coisas lá dentro não faz de ninguém uma dessas coisas. Uma mochila tem cadernos, mas não é um caderno. Uma biblioteca tem livros, mas não se lê uma biblioteca de uma ponta à outra como se lê um livro.

Esta distinção é a base da herança, a forma de escrever a relação "é um" em código, assunto do guia 05, [Herança e polimorfismo](05-heranca-polimorfismo.md). Quem usa herança numa relação que é afinal "tem" acaba com classes que oferecem operações sem sentido. Seria um inventário com uma quantidade própria e um método para retirar unidades sem dizer de que artigo. Antes de ligares duas classes, diz a frase. Se "é um" soar falso, não é herança.

## Duas árvores que se parecem e dizem coisas diferentes

Há dois tipos de desenho em forma de árvore que aparecem muito quando se pensa num programa antes de o escrever. Parecem-se no aspeto, mas dizem coisas muito diferentes.

A primeira é uma **hierarquia de especialização**, também chamada árvore de classificação. Cada ramo liga um tipo geral a um tipo mais particular:

```text
Veículo
├── Veículo com motor
│   ├── Carro
│   └── Mota
└── Bicicleta
```

Esta árvore lê-se de baixo para cima com a frase "é um": um carro é um veículo com motor, e um veículo com motor é um veículo. Cada nível acrescenta pormenor ao de cima. Tudo o que o tipo de cima descreve continua a ser verdade para os de baixo. Por isso, um carro concreto é, ao mesmo tempo, um carro, um veículo com motor e um veículo. O que a árvore não diz é que o carro está "dentro" do veículo. Não há nenhum veículo que contenha carros.

A segunda é uma **árvore de partes**. Cada ramo liga um todo a uma parte sua:

```text
Inventário da sala
├── Artigo A01: Caderno, 6 unidades
├── Artigo A02: Pasta, 2 unidades
└── Artigo A03: Caneta, 10 unidades
```

Esta árvore lê-se de cima para baixo com a frase "tem": o inventário da sala tem estes três artigos. Aqui, o de baixo não é um caso particular do de cima. O artigo A01 não é "um tipo de inventário"; é uma das linhas que o inventário guarda. Repara também que os nomes desta árvore são objetos concretos, com valores, enquanto os nomes da primeira são tipos.

Para distinguir as duas árvores, lê cada ligação com as duas frases e fica com a que for verdadeira. "Uma mota é um veículo com motor" é verdadeira, e por isso a primeira árvore é de especialização. "O inventário tem o artigo A02" é verdadeira, e "o artigo A02 é um inventário" é falsa, e por isso a segunda árvore é de partes. Os dois desenhos parecem-se tanto que não basta olhar para eles. Quando descreves as classes de um programa, escreve sempre a frase que liga cada par de classes: "é um" ou "tem".

Um aviso para não confundires as coisas. Uma árvore de classificação não quer dizer que cada nome se torne uma classe. No guia 02 vimos que não criamos uma classe `Caderno` e outra classe `Pasta`, porque cadernos e pastas guardam os mesmos dados e aceitam as mesmas operações. Um tipo só merece uma classe própria quando os seus objetos têm dados ou comportamentos diferentes. Essa situação é o assunto do guia 05.

## Dois graus de "tem": composição e agregação

A relação "tem" não é sempre igual. Às vezes, a parte está tão presa ao todo que não faz sentido sem ele. Outras vezes, o todo limita-se a reunir partes que existem por conta própria. Os dois casos têm nomes diferentes.

### Composição

Há **composição** quando a parte só faz sentido dentro do seu todo: pertence a um único todo, nasce com ele ou é criada por ele, e desaparece quando ele desaparece.

Pensa numa encomenda feita numa loja na internet. A encomenda tem linhas: "2 camisolas, tamanho M" é uma linha, "1 boné" é outra. Uma linha sozinha não quer dizer nada: 2 camisolas de que encomenda, para quem, entregues onde? A linha só tem significado dentro da encomenda. É a própria encomenda que cria as suas linhas, à medida que se acrescentam produtos. Uma linha nunca passa de uma encomenda para outra. E se a encomenda for anulada e apagada, as suas linhas vão com ela, porque não havia mais nada a que pertencessem.

### Agregação

Há **agregação** quando o todo reúne partes que existem por si próprias. As partes foram criadas fora do todo, antes dele ou independentemente dele. Podem pertencer a vários todos ao mesmo tempo, e continuam a existir quando o todo desaparece.

Pensa numa playlist, uma lista de músicas escolhidas por alguém numa aplicação de música. A playlist tem músicas, mas as músicas já existiam na plataforma antes de alguém as pôr numa playlist. A mesma música pode estar na tua playlist "Para estudar" e na tua playlist "Para correr". É a mesma música nas duas, e não uma cópia. Se apagares a playlist "Para correr", as músicas continuam na plataforma, e a que também estava em "Para estudar" continua lá.

### As perguntas que decidem

Para decidir entre as duas, faz estas perguntas pela ordem em que estão escritas. As duas primeiras decidem; as outras duas confirmam a decisão. A pergunta 1 é a que pesa mais, porque uma composição é, antes de tudo, uma parte que só faz sentido dentro do todo. A pergunta 2 é uma ajuda, porque no código se vê bem quem chama o construtor da parte. Se as duas primeiras perguntas derem respostas diferentes, decide a primeira.

| Pergunta | Composição | Agregação |
| --- | --- | --- |
| 1. A parte faz sentido sem o todo? | Não | Sim |
| 2. Quem cria a parte? | O próprio todo, ou nasce com ele | Alguém fora do todo, e o todo recebe-a já criada |
| 3. A parte pode estar em dois todos ao mesmo tempo? | Não | Pode |
| 4. Se o todo desaparecer, o que acontece à parte? | Desaparece com ele | Continua a existir |

Aplicadas aos dois exemplos:

| Pergunta | Encomenda e linhas | Playlist e músicas |
| --- | --- | --- |
| 1. A parte faz sentido sem o todo? | Não: "2 camisolas" de que encomenda? | Sim: a música existe sem a playlist |
| 2. Quem cria a parte? | A encomenda, ao acrescentar um produto | A plataforma; a playlist só a recebe |
| 3. A parte pode estar em dois todos? | Não | Sim: está nas duas playlists |
| 4. Se o todo desaparecer? | As linhas desaparecem | As músicas ficam |
| Decisão | Composição | Agregação |

### Dois enganos a evitar

Há dois erros típicos. O primeiro é pensar que agregação quer dizer que a parte é menos importante. Não quer: as músicas são o mais importante de uma playlist. A diferença está na força da ligação, e não na importância. O segundo é pensar que qualquer lista de objetos é uma composição. Uma lista diz que o todo guarda várias partes, mas não diz se as partes têm vida própria. Isso decide-se com as perguntas da tabela.

Se, num problema, não conseguires decidir, escreve só a frase "tem" e, ao lado, a pergunta a que não consegues responder. Uma dúvida escrita vale mais do que uma escolha feita ao acaso, porque diz a quem lê o que falta saber sobre o problema.

### A decisão depende do problema

A mesma dupla de classes pode ligar-se de maneiras diferentes em problemas diferentes. Pensa numa aplicação da secretaria da escola. Um aluno existe antes de ter turma, pode mudar de turma a meio do ano e continua a existir quando a turma termina: turma e alunos é uma agregação. Numa aplicação que só servisse para preparar a pauta de uma turma, talvez os alunos só existissem dentro dessa pauta. É a mesma ideia do guia 01: representar um problema é escolher o que interessa. As perguntas da tabela respondem-se sempre a pensar no problema concreto.

### A mesma palavra com dois sentidos

Vais encontrar a palavra composição com dois sentidos, e convém saber qual é qual. Em programação, em geral, **composição de objetos** quer dizer construir um objeto a partir de outros objetos, que ele guarda e usa para fazer o seu trabalho. Nesse sentido largo, composição é o nome da relação "tem", e é a alternativa à herança, assunto do guia 05. Nesta secção, composição tem um sentido estreito: a forma mais forte da relação "tem", o contrário da agregação. O nome deste tema, Composição e modelação, usa a palavra no sentido largo, e a tabela das quatro perguntas usa-a no sentido estreito. Quando uma conversa ficar confusa, pergunta, ou diz, em que sentido se está a usar.

## O nosso inventário: composição

Vamos agora aplicar as perguntas ao inventário e aos artigos, no problema que temos vindo a construir desde o guia 01.

A primeira pergunta é se um artigo faz sentido sem o inventário. No guia 01 definimos artigo como uma referência de material no inventário, isto é, uma linha do registo. "Caderno, 6 unidades" responde a que pergunta, se não soubermos de que inventário é? Seis cadernos em que sala, em que armário? Sozinho, o artigo é como a linha da encomenda: não diz nada. A resposta é não.

A segunda pergunta é quem cria o artigo. Aqui somos nós que decidimos, porque somos nós que escrevemos o programa, e vamos decidir que é o inventário. O inventário vai ter um método `registar(codigo, nome, quantidade)` que recebe os dados de um artigo novo. Verifica que o código ainda não está a ser usado, e só então cria o artigo, lá dentro. A razão desta escolha está em "Artigos soltos: o que nenhum artigo consegue garantir". A única regra que falta garantir, o código único, só pode ser verificada por quem conhece todos os artigos. Se é o inventário que verifica, faz todo o sentido que seja ele a decidir se o artigo chega a nascer. É outra vez a regra do guia 03, "verificar primeiro, alterar depois", agora aplicada ao nascimento de um artigo.

As duas perguntas de confirmação vão no mesmo sentido. Um artigo não pode estar em dois inventários ao mesmo tempo. As 6 unidades de A01 são as desta sala, e o inventário de outra sala tem os seus próprios artigos e as suas próprias quantidades. E se o inventário deixar de existir, os seus artigos, que eram as linhas do seu registo, vão com ele.

Podes objetar que os cadernos continuam no armário mesmo que alguém apague o inventário, e que por isso a resposta à primeira pergunta devia ser sim. A objeção é razoável. Responde-se separando duas coisas que a palavra "artigo" pode misturar:

| O material físico | O artigo do nosso programa |
| --- | --- |
| Os seis cadernos que estão na prateleira | A linha do registo sobre esse material: o código A01, o nome Caderno e 6 unidades |
| Existe com programa ou sem ele | Existe dentro do inventário |
| Se o inventário for apagado, fica no armário | Se o inventário for apagado, desaparece com ele |

O programa guarda informação sobre os cadernos, e as quatro perguntas falam dessa informação, a da coluna da direita. Se o inventário for apagado, os cadernos ficam no armário, mas as linhas do registo desaparecem com ele.

É a mesma diferença que há entre a camisola e a linha "2 camisolas" de uma encomenda. A camisola existe na loja antes e depois de qualquer encomenda; a linha só existe dentro da encomenda.

A relação entre `Inventario` e `Artigo` é, portanto, uma composição.

Podíamos ter feito outra escolha. Se, no nosso programa, os artigos fossem criados fora do inventário e entregues depois, já feitos, a pergunta 2 passava a apontar para a agregação. Imagina, além disso, que o artigo passava a fazer sentido sem o inventário, por exemplo num catálogo de materiais partilhado por várias salas. Aí, a relação seria uma agregação. Não há uma resposta certa em abstrato: a decisão tem de bater certo com o código.

## O inventário descrito por palavras

Já decidimos que classes vai ter o programa, o que fica a cargo de cada uma e como se relacionam. Antes de escrever código, convém pôr estas decisões por escrito. Uma descrição escrita deixa discuti-las com um colega, ou com o professor, sem ler um programa linha a linha. Também mostra os enganos mais cedo, porque mudar uma frase custa menos do que mudar um programa.

### A descrição de uma classe

No guia 02, em "Classe: a descrição comum", a classe `Artigo` foi descrita por palavras. A descrição dizia o que cada artigo tem, com que valores se cria e o que se lhe pode pedir. Esta é a descrição da classe `Artigo` do fim do guia 03, com as mesmas três partes:

- Cada artigo guarda um código, um nome e uma quantidade, que é sempre um número inteiro não negativo.
- Um artigo cria-se com o código, o nome e a quantidade inicial.
- A um artigo pode pedir-se que adicione unidades, com `adicionar(unidades)`, e que retire unidades, com `retirar(unidades)`.

Cada parte responde a uma pergunta. A primeira diz o que cada objeto guarda: são os atributos. A segunda diz com que valores se cria um objeto: são os parâmetros do construtor. A terceira diz o que se pode pedir a cada objeto, e com que valores: são os métodos, com os seus parâmetros entre parênteses.

Repara em três pormenores.

O primeiro é a quantidade. Em Python, o valor está guardado no atributo interno `_quantidade`, e quem usa a classe lê-o e escreve-o pela propriedade `quantidade`. A descrição fala só da quantidade, sem o sublinhado. Mostra aquilo que quem usa a classe vê e pode pedir: a interface pública do guia 03. Onde e como o Python guarda o valor é uma decisão do código.

O segundo é o `self`. A descrição escreve `adicionar(unidades)`, e não `adicionar(self, unidades)`. Todos os métodos recebem o `self`, e é sempre o próprio objeto, por isso escrevê-lo não acrescenta informação.

O terceiro é que a descrição de uma classe não tem valores. Seria um erro escrever "cada artigo tem 6 unidades". O 6 é a quantidade de um artigo concreto, e não de todos os artigos: é a distinção entre classe e instância do guia 02. Para falar de um objeto concreto, descreve-se o seu estado, que é outra coisa: o artigo A01 chama-se Caderno e tem 6 unidades.

### A descrição do inventário

A classe `Inventario` descreve-se com as mesmas três partes:

- Cada inventário guarda os seus artigos, e nunca dois com o mesmo código.
- Um inventário cria-se vazio, sem nenhum valor.
- A um inventário pode pedir-se que registe um artigo novo, com `registar(codigo, nome, quantidade)`; que diga a quantidade de um artigo, com `quantidade_de(codigo)`; e que retire unidades de um artigo, com `retirar(codigo, unidades)`.

A primeira parte diz que o inventário guarda os seus artigos, e não diz como os guarda. No programa, vão ficar numa lista. Essa é uma decisão do código, como o `_quantidade` do artigo, e por isso a lista não entra na descrição. Entra a regra que dá razão de ser ao inventário: não há dois artigos com o mesmo código.

### A descrição da relação

Falta a ligação entre as duas classes. Descreve-se com a frase da relação e, numa relação "tem", com o grau e as razões que o justificam:

- Um inventário tem artigos, e é uma composição.
- Um artigo só faz sentido dentro do seu inventário, porque é uma linha do registo.
- É o inventário que cria cada artigo, quando se lhe pede que o registe.
- Cada artigo pertence a um só inventário e desaparece se o inventário desaparecer.

As três últimas frases são as respostas às perguntas de "Dois graus de "tem": composição e agregação", pela mesma ordem; a última responde às duas perguntas que confirmam. Quem lê a descrição fica a saber que relação é e porquê, sem abrir o programa. Se um colega discordar, sabe também que pergunta discutir.

### O modelo

Juntas, as três descrições formam o **modelo** do inventário. Chamamos modelo à descrição das classes de um programa, do que cada uma guarda e faz, e das relações entre elas. **Modelar** é escrever o modelo, antes do código. É a segunda palavra do nome deste tema, Composição e modelação.

É este modelo que o exemplo guiado vai traduzir para Python. Antes, recordas as listas e vês em Python como é uma agregação, com a playlist. No fim do exemplo guiado comparas, em Python, a composição do inventário com a agregação da playlist.

## Recordar as listas e o ciclo `for`

O inventário vai guardar os artigos numa lista e percorrê-los com um ciclo `for`. São duas ferramentas que provavelmente já usaste no 10.º ano, com números e textos, mas vamos explicá-las do princípio. Aqui vão guardar objetos, e isso levanta uma pergunta que o guia 02 já preparou. O programa seguinte é completo, com a mesma classe `Artigo` do primeiro programa.

Antes de correres este programa, tenta prever as seis linhas que ele mostra. Pensa sobretudo na quinta: a retirada é feita através da lista, e a linha mostra a quantidade através do nome `caderno`.

```python
# Uma lista de artigos e o ciclo for: o segundo programa do guia 04.

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


caderno = Artigo("A01", "Caderno", 6)
pasta = Artigo("A02", "Pasta", 2)

artigos = []
print("Artigos na lista:", len(artigos))

artigos.append(caderno)
artigos.append(pasta)
print("Artigos na lista:", len(artigos))

for artigo in artigos:
    print(artigo.codigo, artigo.nome, artigo.quantidade)

artigos[0].retirar(2)
print("Quantidade de caderno:", caderno.quantidade)
print(artigos[0] is caderno)
```

O programa mostra:

```text
Artigos na lista: 0
Artigos na lista: 2
A01 Caderno 6
A02 Pasta 2
Quantidade de caderno: 4
True
```

Leitura guiada: a classe é a mesma, e o que interessa vem depois dela. Vamos ler essa parte uma ferramenta de cada vez, pela ordem do programa.

`artigos = []` cria uma **lista** vazia e dá-lhe o nome `artigos`. Uma lista é um valor que guarda vários valores por ordem. Os parênteses retos sem nada lá dentro representam uma lista sem nenhum elemento. `len(artigos)` devolve o número de elementos da lista, que neste momento é 0. O nome `len` vem do inglês *length*, "comprimento".

`artigos.append(caderno)` acrescenta um elemento no fim da lista; *append* quer dizer "acrescentar". `append` é um método das listas. O Python já o traz feito, tal como os métodos que escreves nas tuas classes, e chama-se com o ponto, sobre a lista que o recebe. Depois dos dois `append`, a lista tem 2 elementos, o caderno na primeira posição e a pasta na segunda.

`for artigo in artigos:` é o ciclo `for`, que se lê "para cada artigo na lista artigos". Repete o bloco indentado por baixo dele uma vez por cada elemento da lista, pela ordem da lista. Em cada volta, o nome `artigo` passa a apontar para o elemento seguinte: na primeira volta aponta para o caderno, na segunda para a pasta. Depois do último elemento, o ciclo termina, e o programa continua na linha seguinte ao bloco. O nome `artigo`, no singular, foi escolhido para se ler bem. Podias escolher um nome como `a` ou `coisa`, e o Python não se queixava; quem lê o código, sim. O nome da própria lista é que não serve: em "Erros frequentes" vês o que acontece.

`artigos[0]` é o primeiro elemento da lista. O número entre parênteses retos chama-se **índice** e indica a posição. Em Python, as posições começam em 0: `artigos[0]` é o caderno e `artigos[1]` é a pasta.

Chegamos à pergunta importante. A linha `artigos[0].retirar(2)` retira 2 unidades ao primeiro elemento da lista. A linha seguinte mostra a quantidade através do nome `caderno`, e aparece 4. A retirada feita através da lista chegou ao objeto para onde o nome `caderno` aponta. E a última linha, com o `is` do guia 02, confirma que `artigos[0]` e `caderno` são o mesmo objeto.

É a ideia das etiquetas do guia 02, em "Cada instância é um objeto diferente". Uma lista não guarda cópias dos objetos: guarda os próprios objetos, tal como uma variável é só um nome que aponta para um objeto. Depois de `artigos.append(caderno)`, o mesmo artigo passou a ser alcançável por dois caminhos, o nome `caderno` e a posição 0 da lista. Qualquer alteração feita por um dos caminhos vê-se pelo outro, porque só existe um artigo. O mesmo acontece com o nome `artigo` dentro do `for`: em cada volta aponta para um dos objetos da lista, e não para uma cópia dele.

## Agregação em Python: a playlist e as músicas

Antes de escrevermos o inventário, vemos em Python o caso mais simples de um objeto que guarda outros numa lista. É a playlist que agrega músicas, de "Dois graus de "tem": composição e agregação". É um programa completo.

Antes de correres, tenta prever as quatro linhas. Pensa sobretudo nas duas últimas: o título da música `chuva` muda uma única vez, através do nome `chuva`, depois de ela estar nas duas playlists.

```python
# Uma playlist que agrega músicas: o terceiro programa do guia 04.

class Musica:
    """Uma música, identificada pelo título."""

    def __init__(self, titulo):
        """Guarda o título da música."""
        self.titulo = titulo


class Playlist:
    """Uma lista de músicas escolhidas por alguém.

    A playlist agrega músicas que já existem: não as cria, recebe-as.
    A mesma música pode estar em várias playlists ao mesmo tempo.
    """

    def __init__(self, nome):
        """Cria uma playlist vazia, com um nome."""
        self.nome = nome
        self._musicas = []

    def acrescentar(self, musica):
        """Junta à playlist uma música que já existe, criada fora dela."""
        self._musicas.append(musica)

    def titulos(self):
        """Devolve uma lista com os títulos das músicas, pela ordem da playlist."""
        resultado = []
        for musica in self._musicas:
            resultado.append(musica.titulo)
        return resultado


chuva = Musica("Chuva de Outono")
ritmo = Musica("Ritmo Forte")

estudar = Playlist("Para estudar")
correr = Playlist("Para correr")

estudar.acrescentar(chuva)
correr.acrescentar(ritmo)
correr.acrescentar(chuva)

print(estudar.nome, estudar.titulos())
print(correr.nome, correr.titulos())

chuva.titulo = "Chuva de Outono (acústica)"

print(estudar.nome, estudar.titulos())
print(correr.nome, correr.titulos())
```

O programa mostra:

```text
Para estudar ['Chuva de Outono']
Para correr ['Ritmo Forte', 'Chuva de Outono']
Para estudar ['Chuva de Outono (acústica)']
Para correr ['Ritmo Forte', 'Chuva de Outono (acústica)']
```

Quando o `print` recebe uma lista, mostra-a entre parênteses retos, com os elementos separados por vírgulas. Os textos aparecem entre plicas, `'...'`, em vez das aspas com que os escreveste. Se um texto tiver uma plica lá dentro, como `"Pão d'Avó"`, o Python mostra-o entre aspas, para a plica não se confundir com o fim do texto.

Leitura guiada: começa pelas duas classes, de cima para baixo. A `Musica` só guarda um título. A `Playlist` guarda um nome e uma lista interna, `_musicas`, com o sublinhado do guia 03, que começa vazia. Tem um método para juntar uma música, `acrescentar`, e outro para devolver os títulos, `titulos`. Depois lê o programa principal: duas músicas, duas playlists, três `acrescentar`, dois pares de `print`, e entre eles uma mudança de título.

As duas músicas são criadas no programa principal, com `Musica(...)`, antes de qualquer playlist existir. O método `acrescentar` não cria nada: recebe no parâmetro `musica` um objeto que já existe e junta-o à lista. Em lado nenhum da classe `Playlist` aparece `Musica(...)`. É o sinal, no código, da resposta "alguém fora do todo" à pergunta 2.

A música `chuva` foi acrescentada às duas playlists. Não foi copiada: as duas listas guardam o mesmo objeto, tal como a lista de "Recordar as listas e o ciclo `for`" guardava o próprio caderno. A prova está nas duas últimas linhas. Mudámos o título uma única vez, através do nome `chuva`, e a mudança aparece nas duas playlists, porque só existe uma música. É a resposta "pode" à pergunta 3. E as músicas continuam acessíveis pelos nomes `chuva` e `ritmo`, fora de qualquer playlist. Se o programa deixasse de usar a playlist `correr`, as músicas continuavam a existir, e a `chuva` continuava em `estudar`. É a resposta da pergunta 4.

### O acumulador do método `titulos`

A lista que aparece em cada linha é construída pelo método `titulos`. Lê o corpo dele com cuidado: usa uma forma de trabalhar com ciclos que vais voltar a encontrar muitas vezes. Antes do ciclo, a linha `resultado = []` cria uma lista vazia, que vai receber os títulos. Em cada volta do `for`, o nome `musica` aponta para uma das músicas da playlist. A linha `resultado.append(musica.titulo)` acrescenta o título dessa música no fim da lista. Só depois de o ciclo acabar, já com um título por cada música, é que `return resultado` devolve a lista completa. Na primeira chamada para a playlist "Para correr", a lista começa vazia. Fica com `'Ritmo Forte'` depois da primeira volta, e com `'Ritmo Forte'` e `'Chuva de Outono'` depois da segunda.

A uma variável como `resultado`, que é preparada antes do ciclo e vai juntando, volta a volta, uma parte do resultado, chama-se **acumulador**. Há três pormenores que decidem se um acumulador funciona.

O primeiro é o valor com que começa, escrito antes do ciclo. Tem de ser o resultado certo para o caso em que o ciclo não dá nenhuma volta. Os títulos de uma playlist sem músicas formam uma lista vazia, e por isso `resultado` começa vazio.

O segundo é que a linha que prepara o acumulador fica fora do ciclo. Se ficasse dentro, a lista voltava a ficar vazia no início de cada volta, e no fim só teria o último título. Numa playlist sem músicas, o programa até parava com um erro, porque o nome `resultado` nunca chegava a receber um valor.

O terceiro é que o `return` fica depois do ciclo, encostado à indentação do `for`. Se ficasse dentro, o método terminava logo na primeira volta, com uma lista que só teria o primeiro título. Numa playlist sem músicas, o método devolvia `None`, porque nunca chegava a nenhum `return`. Aqui, o resultado só está pronto quando todas as músicas tiverem passado pelo ciclo.

## Da descrição ao código, e do código à descrição

Cada parte da descrição de um modelo tem um correspondente no Python. A playlist já mostrou a maior parte deles. O exemplo guiado, a seguir, mostra o que falta: a composição, com o inventário.

| Na descrição por palavras | No código Python |
| --- | --- |
| A classe `Inventario` | `class Inventario:` |
| O que cada objeto guarda, como o nome | `self.nome = ...` no construtor, ou uma propriedade |
| Com que valores se cria um objeto | Os parâmetros do construtor, depois do `self` |
| O que se pode pedir, como `retirar(codigo, unidades)` | `def retirar(self, codigo, unidades):` |
| "Um inventário tem artigos" | Uma lista interna, criada vazia no construtor |
| A relação é uma composição | O todo cria as partes dentro de um método seu e não as entrega a quem está de fora |
| A relação é uma agregação | O todo tem um método que recebe objetos já criados e junta-os à lista |

A tabela lê-se nos dois sentidos. Quando tens o modelo e vais escrever o programa, lês da esquerda para a direita. É o que vamos fazer no exemplo guiado, com o modelo do inventário. Quando tens um programa e queres perceber o seu modelo, lês da direita para a esquerda. Procuras as classes, os atributos e os métodos, e depois procuras onde é que cada objeto é criado e quem o guarda. Foi o que fizeste com a playlist. A lista `_musicas`, criada vazia no construtor, diz que uma playlist tem músicas. O método `acrescentar`, que recebe músicas já criadas, diz que a relação é uma agregação.

Quando chegar a altura de modelares a tua aplicação, a ordem de trabalho deste guia ajuda-te. Primeiro, as frases "tem" e "é um" entre as coisas do problema. Depois, as responsabilidades: quem tem a informação de que cada tarefa precisa. Depois, a descrição de cada classe e a da relação entre elas, com as perguntas de "Dois graus de "tem": composição e agregação". Só no fim, o código.

## Exemplo guiado: construir a classe `Inventario`

Vamos agora escrever a classe do inventário, da esquerda para a direita da tabela anterior. Partimos do modelo de "O inventário descrito por palavras" e das responsabilidades de "Quem sabe o quê: responsabilidades". Acompanha o raciocínio de cada passo, porque é o raciocínio, e não só o código final, que interessa.

### Passo 1: escrever o contrato de cada operação

Como no guia 03, começamos pelo que cada operação promete, antes de pensar em como a escrever. O inventário tem uma regra própria, que é a razão de ele existir: não pode haver dois artigos com o mesmo código. E tem três operações públicas:

| Operação | Recebe | Devolve | Falha, com `ValueError`, quando |
| --- | --- | --- | --- |
| `registar(codigo, nome, quantidade)` | Os dados de um artigo novo | Nada | Já existe um artigo com esse código, ou a quantidade inicial é inválida |
| `quantidade_de(codigo)` | Um código | A quantidade do artigo com esse código | Não existe nenhum artigo com esse código |
| `retirar(codigo, unidades)` | Um código e as unidades a retirar | Nada | Não existe nenhum artigo com esse código, ou o artigo recusa o pedido |

Em todas as falhas, o estado fica como estava: nenhum artigo é criado e nenhuma quantidade muda. É a mesma promessa que o artigo já faz no guia 03, agora feita pelo inventário.

### Passo 2: o construtor e a lista interna

Excerto, que é o início da classe e não corre sozinho:

```python partial
class Inventario:
    """Inventário que cria, guarda e controla os seus artigos."""

    def __init__(self):
        """Cria um inventário vazio, ainda sem artigos."""
        self._artigos = []
```

O construtor só tem o parâmetro `self`, e por isso um inventário cria-se com `Inventario()`, sem argumentos. A sua única tarefa é dar a cada inventário novo uma lista vazia, onde vão ficar os artigos. Cada inventário recebe a sua própria lista. O construtor é executado uma vez por cada inventário criado, e cada execução cria uma lista nova.

O nome da lista começa por sublinhado, `_artigos`, pela mesma razão que `_quantidade` no guia 03: é um assunto interno da classe. Pensa no que aconteceria se o código de fora fizesse `inventario._artigos.append(...)` diretamente. Estaria a pôr um artigo na lista sem passar pela verificação do código único, que vamos escrever no método `registar`. O sublinhado avisa que a lista não se usa de fora; quem quer registar um artigo pede ao inventário.

### Passo 3: procurar um artigo pelo código

Quase todas as operações do inventário começam da mesma maneira: encontrar o artigo que tem um certo código. Em vez de escrevermos essa procura em cada método, escrevemo-la uma vez, num método próprio. Excerto, que pertence à classe e não corre sozinho:

```python partial
    def _procurar(self, codigo):
        """Método interno: devolve o artigo com este código.

        Falha: lança ValueError se não houver nenhum artigo com este código.
        """
        for artigo in self._artigos:
            if artigo.codigo == codigo:
                return artigo
        raise ValueError("Não existe nenhum artigo com o código " + codigo + ".")
```

O nome deste método também começa por sublinhado. É a mesma convenção dos atributos, aplicada a um método: `_procurar` é uma ferramenta interna do inventário, para os seus próprios métodos usarem. Não faz parte da interface pública. Esta escolha tem uma razão ligada à composição. Numa composição, as partes pertencem ao todo, e o código de fora não recebe os artigos para lhes mexer diretamente. Quem quer alguma coisa de um artigo pede-a ao inventário. Por isso, o método que devolve um artigo fica reservado aos métodos da própria classe, e `_procurar` não entra na descrição do inventário, em "O inventário descrito por palavras".

O ciclo percorre a lista interna, um artigo de cada vez, e compara o código de cada um com o código procurado.

Repara primeiro no `return` dentro do ciclo. Um `return` termina o método imediatamente, mesmo que esteja a meio de um ciclo. Assim que o método encontra o artigo certo, devolve-o, e as voltas que faltavam já não são feitas. Não é preciso continuar a procurar depois de encontrar. No método `titulos` da playlist era ao contrário: o `return` ficava depois do ciclo, porque o resultado só estava pronto no fim. Aqui, a procura acaba assim que encontra o artigo, e o `return` está dentro do ciclo de propósito.

Repara depois no `raise` depois do ciclo, encostado à indentação do `for`. Só se chega a essa linha se o ciclo acabar todas as voltas sem nenhum `return`, ou seja, se nenhum artigo tiver o código procurado. Nesse caso, a procura falhou, e o método lança `ValueError`, como qualquer método do guia 03 que recebe um pedido impossível.

A mensagem é construída com o operador `+`, que, entre textos, junta um texto a seguir ao outro. Se o código procurado for `"A07"`, a mensagem fica "Não existe nenhum artigo com o código A07.". Repara nos espaços e no ponto final, que fazem parte dos textos entre aspas.

Vejamos o traço de duas procuras numa lista com dois artigos, A01 e A02, por esta ordem.

| Procura | Volta | `artigo` aponta para | `artigo.codigo == codigo`? | O que acontece |
| --- | --- | --- | --- | --- |
| `_procurar("A02")` | 1 | o artigo A01 | `"A01" == "A02"`: `False` | segue para a volta seguinte |
| `_procurar("A02")` | 2 | o artigo A02 | `"A02" == "A02"`: `True` | `return`: devolve o artigo A02 e termina |
| `_procurar("A07")` | 1 | o artigo A01 | `False` | segue |
| `_procurar("A07")` | 2 | o artigo A02 | `False` | segue; a lista acabou |
| `_procurar("A07")` | depois do ciclo | nenhum | não se aplica | `raise ValueError` |

### Passo 4: registar um artigo, com a regra do todo

Excerto, que pertence à classe e não corre sozinho:

```python partial
    def registar(self, codigo, nome, quantidade):
        """Cria um artigo novo e guarda-o no inventário.

        Recebe: o código, o nome e a quantidade inicial do artigo.
        Devolve: nada (None).
        Falha: lança ValueError se já existir um artigo com este código, ou
        se a quantidade inicial for inválida (quem a recusa é o setter do
        artigo). Em qualquer falha, o inventário fica como estava.
        """
        for artigo in self._artigos:
            if artigo.codigo == codigo:
                raise ValueError("Já existe um artigo com o código " + codigo + ".")
        novo = Artigo(codigo, nome, quantidade)
        self._artigos.append(novo)
```

O método faz três coisas, por esta ordem.

Primeiro verifica a regra do todo: percorre os artigos e, se algum já tiver o código pedido, lança `ValueError`. Este ciclo tem a mesma forma do ciclo de `_procurar`, mas a decisão é a contrária. Em `_procurar`, encontrar o código é o caso bom, e não o encontrar é a falha. Em `registar`, encontrar o código é a falha, e não o encontrar é o caso bom. É por isso que `registar` não usa `_procurar`. Se o usasse, o caso bom, código ainda livre, viria sob a forma de um `ValueError` que teria de ser apanhado com `try` e `except`. O método ficaria muito mais difícil de ler.

Depois cria o artigo, com `Artigo(codigo, nome, quantidade)`. É aqui que a composição aparece no código: é o inventário, dentro de um método seu, que chama o construtor da parte. Repara também no que o inventário não faz: não verifica a quantidade. Quem verifica a quantidade é o setter do artigo, chamado pelo construtor do artigo, exatamente como no guia 03. Se a quantidade for inválida, o setter lança `ValueError`, o construtor é interrompido, e o método `registar` também, na mesma linha.

Por fim, e só por fim, acrescenta o artigo novo à lista. Esta ordem é o que garante a promessa do contrato. Se o código estiver repetido, o método para no primeiro `raise`, antes de criar o artigo. Se a quantidade for inválida, para na linha que cria o artigo, antes do `append`. Nos dois casos, a linha que altera o inventário nunca chega a ser executada, e a lista fica como estava.

### Passo 5: consultar e retirar, encaminhando o pedido ao artigo

Excerto, que pertence à classe e não corre sozinho:

```python partial
    def quantidade_de(self, codigo):
        """Devolve a quantidade do artigo com este código, sem a alterar.

        Falha: lança ValueError se não houver nenhum artigo com este código.
        """
        artigo = self._procurar(codigo)
        return artigo.quantidade

    def retirar(self, codigo, unidades):
        """Encaminha um pedido de retirada para o artigo com este código.

        Recebe: o código do artigo e as unidades a retirar.
        Devolve: nada (None).
        Falha: lança ValueError se não houver nenhum artigo com este código,
        ou se o próprio artigo recusar o pedido, pelas regras do seu método
        retirar. Em qualquer falha, nenhuma quantidade muda.
        """
        artigo = self._procurar(codigo)
        artigo.retirar(unidades)
```

Repara primeiro na forma da chamada, `self._procurar(codigo)`. É a primeira vez que um método pede trabalho a outro método do mesmo objeto. Já sabes, do guia 02, que dentro de um método `self` é o objeto sobre o qual o método está a trabalhar, que aqui é o próprio inventário. De fora, escreve-se `inventario.registar(...)` para pedir alguma coisa ao objeto `inventario`. Da mesma maneira, de dentro escreve-se `self._procurar(...)` para o inventário pedir alguma coisa a si próprio. É a mesma ideia de `self.quantidade` no guia 03, em que o artigo lia a sua própria propriedade; aqui, o inventário chama um método seu.

O `self.` é obrigatório. Sem ele, a linha ficaria `artigo = _procurar(codigo)`, e o Python iria procurar uma função solta com esse nome, escrita fora de qualquer classe. Como essa função não existe, o programa parava com `NameError: name '_procurar' is not defined`. Um `NameError` ("erro de nome") aparece quando se usa um nome que o Python não conhece, e a mensagem diz "o nome `_procurar` não está definido". As versões recentes do Python acrescentam `Did you mean: 'self._procurar'?`, isto é, "querias dizer `self._procurar`?". Dentro da classe, a forma de chegar aos métodos do próprio objeto é através do `self`.

Os dois métodos começam por encontrar o artigo com `_procurar`. Se o código não existir, `_procurar` lança `ValueError`, e o método que o chamou é interrompido nessa mesma linha, sem chegar à segunda. Se o código existir, o nome local `artigo` passa a apontar para o artigo certo. É o próprio objeto guardado na lista, e não uma cópia, como viste em "Recordar as listas e o ciclo `for`".

Depois, cada método faz um pedido a esse artigo. `quantidade_de` lê a propriedade `quantidade` e devolve o valor. `retirar` chama o método `retirar` do artigo, com as mesmas unidades que recebeu.

Chamamos **encaminhamento** a esta forma de colaborar: um objeto recebe um pedido, encontra o objeto que sabe cumpri-lo e passa-lho. O inventário não verifica se as unidades são um inteiro, nem se são positivas, nem se chegam. Não há nenhum `unidades <= 0` na classe `Inventario`. Essas regras são do artigo, e o artigo já as verifica no seu método `retirar` e no seu setter. O inventário ocupa-se do que só ele sabe fazer: encontrar o artigo a partir do código.

Os dois métodos têm o mesmo nome, `retirar`, mas são métodos diferentes, de classes diferentes, com parâmetros diferentes. `inventario.retirar("A01", 2)` recebe um código e um número. `artigo.retirar(2)` recebe só um número, porque o artigo já sabe quem é. Quando lês uma chamada, olha sempre para o objeto antes do ponto: é ele que diz de que classe é o método.

### Passo 6: prever antes de executar

Antes de executarmos, fazemos o traço de uma sequência de pedidos a um inventário acabado de criar. Cada linha começa no estado deixado pela anterior. A coluna "Quem responde" diz que objeto aceitou ou recusou o pedido.

| Pedido | Quem responde | Resposta | Artigos no inventário depois |
| --- | --- | --- | --- |
| `registar("A01", "Caderno", 6)` | Inventário: código livre; setter do artigo: 6 é válido | Aceite | A01 com 6 |
| `registar("A02", "Pasta", 2)` | Inventário e setter do artigo | Aceite | A01 com 6, A02 com 2 |
| `registar("A01", "Cola", 3)` | Inventário: A01 já existe | `ValueError`, antes de criar o artigo | A01 com 6, A02 com 2 |
| `registar("A03", "Caneta", -5)` | Inventário: código livre; setter do artigo: -5 é negativo | `ValueError`, ao criar o artigo, antes do `append` | A01 com 6, A02 com 2 |
| `quantidade_de("A03")` | `_procurar` do inventário: A03 não existe | `ValueError` | sem alteração |
| `retirar("A01", 2)` | Inventário encontra A01; o artigo aceita | Aceite | A01 com 4, A02 com 2 |
| `retirar("A01", 9)` | Inventário encontra A01; setter do artigo: 4 - 9 = -5 | `ValueError` | A01 com 4, A02 com 2 |
| `retirar("A07", 1)` | `_procurar` do inventário: A07 não existe | `ValueError` | A01 com 4, A02 com 2 |

Repara na quinta linha. A consulta de A03 falha, e isso prova que o registo recusado da caneta não deixou nada para trás: o artigo nunca chegou à lista.

### Passo 7: o programa completo e a comparação com o traço

Este é o programa completo, com a classe final `Inventario`. Os pedidos do fim são os do traço do passo 6, pela mesma ordem. Antes de o correres, escreve, para cada linha que o programa vai mostrar, a mensagem que esperas, a partir do traço.

```python
# O inventário que cria e guarda os seus artigos: o programa do exemplo guiado do guia 04.

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

        Recebe: o código, o nome e a quantidade inicial do artigo.
        Devolve: nada (None).
        Falha: lança ValueError se já existir um artigo com este código, ou
        se a quantidade inicial for inválida (quem a recusa é o setter do
        artigo). Em qualquer falha, o inventário fica como estava.
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

        Recebe: o código do artigo e as unidades a retirar.
        Devolve: nada (None).
        Falha: lança ValueError se não houver nenhum artigo com este código,
        ou se o próprio artigo recusar o pedido, pelas regras do seu método
        retirar. Em qualquer falha, nenhuma quantidade muda.
        """
        artigo = self._procurar(codigo)
        artigo.retirar(unidades)


inventario = Inventario()
inventario.registar("A01", "Caderno", 6)
inventario.registar("A02", "Pasta", 2)

try:
    inventario.registar("A01", "Cola", 3)
except ValueError as erro:
    print("Registo de A01 recusado:", erro)

try:
    inventario.registar("A03", "Caneta", -5)
except ValueError as erro:
    print("Registo de A03 recusado:", erro)

try:
    print(inventario.quantidade_de("A03"))
except ValueError as erro:
    print("Consulta de A03 recusada:", erro)

inventario.retirar("A01", 2)
print("A01 depois de retirar 2:", inventario.quantidade_de("A01"))

try:
    inventario.retirar("A01", 9)
except ValueError as erro:
    print("Retirar 9 de A01 recusado:", erro)

try:
    inventario.retirar("A07", 1)
except ValueError as erro:
    print("Retirar de A07 recusado:", erro)

print("A01 no fim:", inventario.quantidade_de("A01"))
print("A02 no fim:", inventario.quantidade_de("A02"))
```

O programa mostra:

```text
Registo de A01 recusado: Já existe um artigo com o código A01.
Registo de A03 recusado: A quantidade não pode ser negativa.
Consulta de A03 recusada: Não existe nenhum artigo com o código A03.
A01 depois de retirar 2: 4
Retirar 9 de A01 recusado: A quantidade não pode ser negativa.
Retirar de A07 recusado: Não existe nenhum artigo com o código A07.
A01 no fim: 4
A02 no fim: 2
```

Compara linha a linha com o traço do passo 6. Os dois primeiros registos foram aceites e não mostram nada, porque um método que cumpre o pedido termina sem erro e em silêncio. As recusas aparecem pela ordem do traço, e cada mensagem diz quem recusou. "Já existe um artigo..." e "Não existe nenhum artigo..." vêm do inventário, e "A quantidade não pode ser negativa." vem do setter do artigo. As duas últimas linhas confirmam que, depois de cinco pedidos recusados, as quantidades são as do traço.

Olha também para o programa principal, depois das classes. Em lado nenhum aparece `Artigo(...)`: os artigos nascem dentro do inventário. Em lado nenhum aparece um nome como `caderno` ou `pasta`: o programa principal não guarda nenhum artigo. Fala sempre com o inventário, usando os códigos. É exatamente o que a composição do modelo promete.

### Passo 8: o caminho de um pedido e o caminho de uma recusa

Segue agora, com mais cuidado, o pedido `inventario.retirar("A01", 9)`. É a primeira vez que uma exceção atravessa vários métodos antes de ser apanhada.

Quando o programa principal chama `inventario.retirar("A01", 9)`, começa uma **cadeia de chamadas**, em que cada método chama o seguinte e fica à espera dele:

1. O programa principal, dentro do `try`, chama `retirar` do inventário.
2. O `retirar` do inventário chama `_procurar("A01")`, que devolve o artigo A01. Depois chama o `retirar` desse artigo, com 9.
3. O `retirar` do artigo verifica o pedido: 9 é inteiro e é positivo. Depois executa `self.quantidade = self.quantidade - unidades`, o que chama o setter com 4 - 9 = -5.
4. O setter vê que -5 é negativo e executa `raise ValueError("A quantidade não pode ser negativa.")`.

A exceção nasce no fundo da cadeia, no setter, e começa a subir. Sai do setter sem que a linha que guarda o valor tenha sido executada. Chega ao `retirar` do artigo, que estava parado na linha da subtração, à espera do setter. Como esse método não tem `try`, é abandonado ali mesmo. Chega ao `retirar` do inventário, que estava parado na linha `artigo.retirar(unidades)`; também não tem `try`, e também é abandonado. Chega por fim ao programa principal, que está dentro de um `try` com `except ValueError`. É aí que é apanhada e que a mensagem é mostrada.

| Onde está a exceção | O que esse sítio estava a fazer | O que lhe acontece |
| --- | --- | --- |
| Setter da quantidade | A verificar -5 | Lança a exceção; não guarda o valor |
| `retirar` do artigo | À espera do setter | É abandonado sem terminar |
| `retirar` do inventário | À espera do artigo | É abandonado sem terminar |
| Programa principal | Dentro de um `try` | Apanha a exceção no `except` e continua |

Repara que `_procurar` não aparece nesta tabela, apesar de o ponto 2 da cadeia o chamar. Quando a exceção nasce, `_procurar` já terminou: encontrou o artigo A01, devolveu-o com o `return` e saiu. Nesse momento, os únicos métodos que ainda não terminaram são os que estão parados à espera de outro. São esses que formam a cadeia por onde a exceção sobe. Um método que já terminou não está à espera de nada, e por isso a exceção não passa por ele.

Uma exceção sobe pela cadeia de chamadas até encontrar um `try` com o `except` certo. Todos os métodos que estiverem pelo caminho sem um `try` que a apanhe são interrompidos no ponto onde estavam. Se não houver nenhum, a exceção chega ao fim da cadeia, e o programa para. Aparecem as linhas do `Traceback` que viste no guia 03. *Traceback* quer dizer "rasto": é o caminho que a exceção percorreu. Mostra, para cada nível da cadeia, do programa principal até ao setter, o ficheiro, o número da linha e o código dessa linha. Lê-se de baixo para cima, como aprendeste. No laboratório deste tema vais provocar um traceback destes de propósito e ler os seus níveis.

Porque é que o inventário não tem um `try` para apanhar a recusa do artigo? Pela divisão de tarefas do guia 03, em "Tratar a recusa: `try` e `except`". Quem lança a exceção decide se o pedido é válido, e quem a apanha decide o que fazer com a recusa. O inventário não sabe o que fazer com uma recusa. Não sabe se o programa está a escrever num terminal, a mostrar uma página na internet ou a registar o pedido num ficheiro. Por isso deixa a exceção passar, e é o programa principal, que sabe onde está, que decide mostrar a mensagem. Se o inventário apanhasse a exceção e não fizesse nada, a recusa desaparecia pelo caminho. Quem fez o pedido ficaria convencido de que ele tinha sido cumprido.

### Passo 9: comparar a composição com a agregação

Temos agora duas classes que guardam listas de objetos: o `Inventario` deste exemplo guiado e a `Playlist` de "Agregação em Python: a playlist e as músicas". Compara-as:

| Pergunta | `Inventario` e `Artigo` (composição) | `Playlist` e `Musica` (agregação) |
| --- | --- | --- |
| Quem chama o construtor da parte? | O inventário, dentro de `registar` | O programa principal, fora da playlist |
| O que recebe o método que junta a parte? | Os dados: código, nome e quantidade | Um objeto já criado |
| A parte pode estar em dois todos? | Não: cada `registar` cria um artigo novo, que só este inventário guarda | Sim: a mesma música está nas duas playlists |
| O programa principal guarda a parte num nome seu? | Não: só o inventário guarda os artigos | Sim: `chuva` e `ritmo` apontam para as músicas |
| O todo entrega as partes a quem as pede? | Não: `_procurar` é interno; pede-se ao inventário | Não é preciso: quem tem a música já a tem |

O Python não tem uma palavra própria para composição nem para agregação. As duas classes usam uma lista e um `append`, e à primeira vista parecem iguais. A diferença está nas decisões que tomámos ao escrever o código: quem cria a parte, o que o método recebe e se o todo deixa as partes sair. A descrição do modelo escreve essas decisões antes do código, com a palavra composição ou agregação e as razões que a justificam. Qualquer pessoa as lê sem abrir o programa.

## Erros frequentes

O erro típico de cada ideia está na secção dela:

- o inventário tomado por "um artigo maior", em "Duas perguntas sobre duas classes: "tem" e "é um"";
- a agregação tomada por menos importante e qualquer lista tomada por composição, em "Dois graus de "tem": composição e agregação";
- os valores na descrição de uma classe, em "O inventário descrito por palavras";
- o acumulador preparado dentro do ciclo e o `return` dentro do ciclo, em "O acumulador do método `titulos`", na secção da playlist;
- o `self.` esquecido antes de `_procurar`, no passo 5 do exemplo guiado.

Ficam aqui os erros que aparecem quando se escreve, pela primeira vez, uma classe que guarda outros objetos numa lista. Em cada um, lê a última linha da mensagem de erro: é a que diz o que aconteceu.

### A procura não encontra um artigo que existe

O que se vê: no programa do exemplo guiado, as linhas aparecem como no passo 7 até `A01 no fim: 4`. Depois, em vez de `A02 no fim: 2`, o programa para, e a última linha da mensagem é `ValueError: Não existe nenhum artigo com o código A02.`. Mas a pasta A02 foi registada no início do programa.

Porque acontece: o `raise` de `_procurar` ficou com a indentação do `if`, dentro do ciclo. Na primeira volta, se o primeiro artigo não for o procurado, o método lança logo a exceção, sem olhar para os outros. Só o primeiro artigo da lista chega a ser encontrado. As recusas de A03 e de A07 parecem certas, porque esses códigos também não existem. A primeira procura de um artigo que existe e não é o primeiro é a de A02, na última linha.

Como se corrige: o `raise` fica depois do ciclo, encostado à indentação do `for`, como no passo 3. Para confirmar, faz o traço de `_procurar("A02")` com a tabela do passo 3 e diz, em cada volta, que linha é executada a seguir.

### O `return` com a indentação do `if`

O que se vê: o programa nem começa. Não aparece nenhuma das linhas da saída, só uma mensagem que acaba em `IndentationError: expected an indented block after 'if' statement on line`, seguido de um número. Um `IndentationError` é um "erro de indentação", e a mensagem diz "esperava-se um bloco indentado a seguir à instrução `if` da linha" indicada. Nas versões anteriores ao Python 3.10, a última linha diz só `IndentationError: expected an indented block`.

Porque acontece: o `return artigo` de `_procurar` ficou com a mesma indentação do `if`. Como o `return` era a única linha do `if`, o `if` fica sem nenhuma instrução por baixo. É um erro de escrita, e o Python recusa o ficheiro antes de executar a primeira linha.

Como se corrige: o `return` fica quatro espaços mais à direita do que o `if`, como no passo 3. O número no fim da mensagem é a linha desse `if`.

### O inventário não tem a lista

O que se vê: o programa para no primeiro `registar`, com `AttributeError: 'Inventario' object has no attribute '_artigos'`. Em português: o objeto do tipo `Inventario` não tem o atributo `_artigos`. Um `AttributeError` ("erro de atributo") aparece quando se pede a um objeto um atributo que ele não tem. As versões recentes do Python acrescentam uma sugestão, como `Did you mean: '_artigo'?`, "querias dizer `_artigo`?".

Porque acontece: o nome da lista está escrito de maneiras diferentes no construtor e noutro método, por exemplo `self._artigo = []` no construtor e `self._artigos` no `registar`. Para o Python são dois nomes diferentes, e o segundo nunca recebeu um valor.

Como se corrige: procura todas as linhas com `_artigo` e usa o mesmo nome em todas.

### Um código escrito como número

O que se vê: o programa para com `TypeError: can only concatenate str (not "int") to str`, mesmo que a chamada esteja dentro de um `try` com `except ValueError`. Um `TypeError` ("erro de tipo") aparece quando uma operação recebe valores de um tipo que não aceita. A mensagem diz "só se pode juntar texto a texto, e não um inteiro": `str` é o nome que o Python dá ao texto, e `int` ao número inteiro.

Porque acontece: foi passado um número como código, como em `inventario.quantidade_de(7)`. Nenhum artigo tem o código 7, e `_procurar` chega ao `raise`. Mas a mensagem do `raise` junta textos com `+`, e o 7 não é um texto. O Python para nessa conta, com um `TypeError`, antes de lançar o `ValueError`. Como o `except` só apanha `ValueError`, o `TypeError` passa por ele.

Como se corrige: neste inventário, os códigos são textos, escritos entre aspas, como `inventario.quantidade_de("A07")`.

### O nome do ciclo igual ao nome da lista

O que se vê: no segundo programa deste guia, se o ciclo for escrito `for artigos in artigos:`, com `artigos` também no `print` de dentro, o ciclo ainda mostra os dois artigos. Mas a linha seguinte, `artigos[0].retirar(2)`, para o programa com `TypeError: 'Artigo' object is not subscriptable`. Em português: um objeto `Artigo` não aceita índices.

Porque acontece: em cada volta, o nome do ciclo passa a apontar para um elemento da lista. Se o nome do ciclo for o da própria lista, depois do ciclo `artigos` aponta para o último artigo, e não para a lista. O programa perdeu o nome que chegava à lista.

Como se corrige: dá ao ciclo um nome diferente do da lista, de preferência o singular dela: `for artigo in artigos:`.

## Palavras novas deste guia

- Responsabilidades de uma classe: o que os seus objetos sabem e o que fazem.
- Relação "tem": a relação entre um todo e as suas partes, ou entre um objeto e outros objetos que ele guarda e usa.
- Relação "é um": a relação entre um tipo particular e um tipo mais geral, como entre o carro e o veículo.
- Hierarquia de especialização, ou árvore de classificação: uma árvore em que cada ramo liga um tipo geral a um tipo mais particular; lê-se de baixo para cima, com "é um".
- Árvore de partes: uma árvore em que cada ramo liga um todo a uma parte sua; lê-se de cima para baixo, com "tem".
- Composição: a relação "tem" em que a parte só faz sentido dentro do todo, é criada por ele e desaparece com ele.
- Agregação: a relação "tem" em que o todo reúne partes que existem por si próprias.
- Composição de objetos: no sentido largo da programação, construir um objeto a partir de outros objetos que ele guarda e usa.
- Modelo: a descrição das classes de um programa, do que cada uma guarda e faz, e das relações entre elas.
- Modelar: escrever o modelo de um programa, antes do código.
- Lista: um valor que guarda vários valores por ordem, escrito entre parênteses retos.
- Índice: o número entre parênteses retos que indica uma posição da lista, a contar de 0.
- Acumulador: uma variável preparada antes de um ciclo, que vai juntando, volta a volta, uma parte do resultado.
- Método interno: um método com um sublinhado no início do nome, como `_procurar`, que só os métodos da própria classe usam.
- Encaminhamento: um objeto recebe um pedido, encontra o objeto que sabe cumpri-lo e passa-lho.
- Cadeia de chamadas: os métodos que estão parados, cada um à espera do seguinte, desde o programa principal até ao sítio onde o Python está a trabalhar.

## Verificar o que aprendeste

Tenta responder sem olhar para o texto. Se uma pergunta te deixar com dúvidas, volta à secção indicada.

1. Porque é que nenhum artigo consegue garantir que o seu código é único? ("Artigos soltos: o que nenhum artigo consegue garantir")
2. Aplica o teste "se A é um B, tudo o que B tem e faz tem de fazer sentido para A" à frase "um inventário é um artigo". Onde é que o teste falha? ("Duas perguntas sobre duas classes: "tem" e "é um"")
3. Como se lê cada uma das duas árvores, de que lado para que lado e com que frase? ("Duas árvores que se parecem e dizem coisas diferentes")
4. Descreve por palavras uma classe à tua escolha: o que cada objeto guarda, com que valores se cria e o que se lhe pode pedir. Porque é que a descrição não leva valores? ("O inventário descrito por palavras")
5. Porque é que a descrição do inventário diz que ele guarda os seus artigos, e não fala da lista onde o programa os guarda? ("O inventário descrito por palavras")
6. Com que perguntas decides entre composição e agregação, e qual decide quando as duas primeiras dão respostas diferentes? ("Dois graus de "tem": composição e agregação")
7. Porque é que o método `registar` só faz o `append` no fim? (Exemplo guiado, passo 4)
8. Descreve o caminho de uma exceção lançada pelo setter até ao `except` do programa principal. Porque é que `_procurar` não faz parte desse caminho? (Exemplo guiado, passo 8)
9. No código da playlist e no do inventário, aponta a linha que decide se a relação é composição ou agregação. ("Agregação em Python: a playlist e as músicas" e exemplo guiado, passo 9)

## O que vem a seguir

Para praticar este tema, faz o [laboratório](04-composicao-modelacao-laboratorio.md) e depois a [ficha de exercícios](04-composicao-modelacao-exercicios.md). No laboratório constróis o inventário no computador, um passo de cada vez, e lês o caminho de uma recusa. Na ficha praticas sozinho a descrição de classes por palavras, a escolha entre composição e agregação e a leitura de código com objetos que colaboram.

O tema seguinte é [Herança e polimorfismo](05-heranca-polimorfismo.md), sobre a relação "é um", que em Python se escreve com a herança. A pergunta deixa de ser "o que é que este objeto tem?" e passa a ser "de que tipo mais geral é este objeto um caso?".

![Rodapé](../imagens/rodape.png)

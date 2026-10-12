![Cabeçalho](../imagens/cabecalho.png)

# Laboratório: completar a retirada de material

*M10 · Caderno 6 · Laboratório*

Este laboratório acompanha o [caderno 6](06-sintese.md) e fecha o M10. Diz-te o que fazer, passo a passo, com o editor de Python aberto ao lado. As explicações do porquê estão nos cadernos 2, 3, 4 e 6: quando um passo usa uma ideia, o texto diz em que caderno e em que secção ela está explicada. Faz-se na aula, com o professor a acompanhar, e conta com cerca de duas horas.

Vais trabalhar com um pequeno programa em Python que acompanha os materiais de uma sala. O programa já conhece dois artigos, já sabe registá-los, consultar a quantidade de cada um e consultar as suas saídas, mas ainda não sabe retirar unidades. Primeiro explicas como os dados estão organizados; depois completas a operação que falta, verificas os resultados com casos escolhidos e explicas a correção que fizeste. No fim, mostras o teu trabalho ao professor numa conversa curta.

No fim deves ter um ficheiro `inventario.py` com a retirada completa nas duas classes, um ficheiro `ensaios.py` com os casos que experimentaste, e uma folha com o modelo do programa, as tabelas de previsão e as frases que explicam a correção.

## Antes de começar

Precisas do computador com o editor de Python que usas nas aulas, e de papel e caneta para o diagrama, as previsões e as respostas.

Este laboratório não traz matéria nova. Junta num só problema o que aprendeste nos cadernos 2, 3, 4 e 6, e dá essa matéria por sabida:

- do caderno 2: classe, objeto ou instância, atributo, estado, o construtor `__init__`, o parâmetro `self` e a chamada de um método com o ponto;
- do caderno 3: a propriedade com getter e setter, o atributo interno com sublinhado, a recusa com `raise ValueError`, o `try` e o `except`, a regra "verificar primeiro, alterar depois" e o exemplo guiado do método `retirar`, na secção 12;
- do caderno 4, até à secção 12: a classe `Inventario`, com a lista interna `_artigos`, o método interno `_procurar` e o método `registar`, que cria os artigos; o encaminhamento de um pedido; o caminho de uma recusa; a diferença entre composição e agregação, com a playlist da secção 12; e a UML leve;
- do caderno 6: o programa de partida, a leitura de um programa por zonas, a diferença entre um erro de sintaxe e um erro de comportamento, o exemplo guiado do método `acertar` e as caixas de objeto.

Se ainda não estudaste o caderno 6, lê pelo menos as secções 2 a 6 antes da aula. O caderno 5, sobre herança e polimorfismo, não é preciso: o laboratório não pede herança.

A forma de trabalhar é a dos outros laboratórios. Antes de executares, escreves no papel o que esperas ver. Depois executas e comparas. Quando o resultado é diferente do que previste, procura a explicação antes de continuares: é essa explicação que mais te ensina. Se a previsão estiver errada, não a apagues para ficar igual ao ecrã: escreve ao lado o que estava errado e porquê.

Executa sempre o ficheiro inteiro. Cada execução começa do zero: cria um inventário novo, regista os dois artigos com os valores iniciais e repete todos os pedidos, pela ordem em que estão escritos.

## Como trabalhas com o professor

O professor acompanha o laboratório do princípio ao fim. Podes trabalhar sozinho ou em par, como ele indicar. Em par, os dois têm de conseguir explicar tudo o que está escrito, porque o professor pode fazer a pergunta a qualquer um.

Algumas partes acabam com a frase "Mostra ao professor antes de avançar". Quer dizer o que diz: chamas o professor, mostras o que fizeste, e só passas à parte seguinte depois de ele o confirmar. Há uma razão para isto. Cada parte usa a anterior: um modelo mal percebido leva a escrever uma regra no objeto errado, e uma previsão errada faz-te procurar um erro onde ele não está. Se o professor encontrar alguma coisa a corrigir, não te dá a resposta: faz-te uma pergunta, ou aponta para uma linha do teu código ou da tua tabela, e tu corriges e voltas a mostrar. Enquanto esperas, relê a secção do caderno de que vais precisar na parte seguinte.

Este laboratório não tem nota. É prática guiada: serve para juntares as ideias do módulo com ajuda, antes de as usares sozinho no projeto. Pedir ajuda faz parte do trabalho, e o professor está lá para isso.

## O problema: os artigos e as suas saídas

| Código | Nome | Quantidade inicial | Saídas iniciais |
| --- | --- | ---: | ---: |
| A10 | Régua | 6 | 0 |
| A11 | Cola | 3 | 0 |

Cada linha representa um artigo. Os códigos são diferentes, os nomes estão preenchidos e as quantidades são válidas. Estes dados já vêm escritos no programa: não precisas de criar outros artigos nem de os pedir a quem usa o programa.

Há uma informação nova em relação aos cadernos. A equipa que usa o programa quer saber quantas unidades de cada artigo já saíram da sala desde que o programa começou, para perceber que materiais se gastam mais. Por isso, cada artigo guarda, além da quantidade, as suas **saídas**: o total de unidades que já saíram por retiradas aceites. Um artigo acabado de criar tem zero saídas. As saídas obedecem a três regras:

- uma retirada aceite aumenta as saídas no número de unidades retiradas, ao mesmo tempo que diminui a quantidade;
- uma retirada recusada não muda nada: nem a quantidade, nem as saídas;
- adicionar unidades é uma entrada de material, e não uma saída, por isso não muda as saídas.

Por exemplo, se a um artigo com 6 unidades e 0 saídas forem retiradas 2 unidades e depois 1, fica com 3 unidades e 3 saídas. Se a seguir for recusado um pedido de 9, continua com 3 unidades e 3 saídas.

Repara que, enquanto ninguém adicionar unidades, a quantidade e as saídas de um artigo somam sempre o mesmo: a quantidade com que ele começou. No exemplo, 6 e 0, depois 4 e 2, depois 3 e 3: a soma é sempre 6. É uma regra que tem de continuar verdadeira depois de cada pedido, aceite ou recusado, tal como a regra da quantidade que o caderno 6, na secção 4, chama invariante. Vais poder usá-la para verificar os teus resultados: se a soma mudar sem nenhuma adição, há uma saída contada a mais ou a menos.

## O programa inicial

Este é o programa com que vais trabalhar. É parecido com o programa de partida do caderno 6: tem a classe `Artigo` e a classe `Inventario`, agora com as saídas, e um programa principal que regista os dois artigos e faz dois pedidos de retirada. Faltam as duas partes da retirada, assinaladas com "Por completar". Programa completo:

```python
"""Programa inicial do laboratório do caderno 6: completar a retirada de material.

O programa executa do princípio ao fim sem mensagens de erro, mas ainda não
faz o que o problema pede: as duas partes da operação de retirada, a do
inventário e a do artigo, estão por completar. Procura as linhas que dizem
"Por completar". Todo o resto já está preparado e não precisa de mudar.
"""


class Artigo:
    """Artigo do inventário: código, nome, uma quantidade sempre válida e as saídas.

    A quantidade é uma propriedade com getter e setter, como no caderno 3.
    As saídas contam quantas unidades já saíram por retiradas aceites;
    são uma propriedade só com getter, por isso o código de fora pode
    consultá-las, mas não as pode alterar.
    """

    def __init__(self, codigo, nome, quantidade):
        """Cria o artigo, ainda sem saídas. A quantidade inicial passa pelo setter."""
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self._saidas = 0

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

    @property
    def saidas(self):
        """Getter: devolve quantas unidades já saíram por retiradas aceites.

        Não há setter: só os métodos do próprio artigo mudam o atributo
        interno _saidas.
        """
        return self._saidas

    def adicionar(self, unidades):
        """Acrescenta unidades (inteiro, 1 ou mais); senão, lança ValueError.

        Uma entrada de material não é uma saída: as saídas não mudam.
        """
        if not isinstance(unidades, int):
            raise ValueError("As unidades a adicionar têm de ser um número inteiro.")
        if unidades <= 0:
            raise ValueError("As unidades a adicionar têm de ser 1 ou mais.")
        self.quantidade = self.quantidade + unidades

    def retirar(self, unidades):
        """Retira unidades ao artigo e conta-as nas saídas.

        Recebe: unidades, um número inteiro positivo (1 ou mais).
        Devolve: nada (None).
        Falha: lança ValueError se unidades não for um número inteiro, se
        não for positivo, ou se não houver unidades suficientes. Em qualquer
        falha, a quantidade e as saídas ficam como estavam.
        Quando não falha, a quantidade diminui e as saídas aumentam o número
        de unidades retiradas.
        """
        # Por completar: o artigo decide se o pedido é possível e altera os seus dados.
        pass


class Inventario:
    """Inventário que cria, guarda e controla os seus artigos.

    Cria os artigos em registar e guarda-os numa lista interna, _artigos,
    que o código de fora não usa. Não deixa haver dois artigos com o mesmo
    código. Os pedidos sobre um artigo são encaminhados para o artigo com
    esse código, que continua a proteger os seus próprios dados.
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

    def saidas_de(self, codigo):
        """Devolve as saídas do artigo com este código, sem as alterar.

        Falha: lança ValueError se não houver nenhum artigo com este código.
        """
        artigo = self._procurar(codigo)
        return artigo.saidas

    def retirar(self, codigo, unidades):
        """Encaminha um pedido de retirada para o artigo com este código.

        Recebe: o código do artigo e as unidades a retirar.
        Devolve: nada (None).
        Falha: lança ValueError se não houver nenhum artigo com este código,
        ou se o próprio artigo recusar o pedido. Em qualquer falha, nenhum
        artigo muda.
        """
        # Por completar: o inventário encontra o artigo pelo código e passa-lhe o pedido.
        pass


# Os dois artigos do laboratório. Os dados são fictícios e já estão verificados.
inventario = Inventario()
inventario.registar("A10", "Régua", 6)
inventario.registar("A11", "Cola", 3)

print("Início")
print("A10: quantidade", inventario.quantidade_de("A10"), "e saídas", inventario.saidas_de("A10"))
print("A11: quantidade", inventario.quantidade_de("A11"), "e saídas", inventario.saidas_de("A11"))

try:
    inventario.retirar("A10", 4)
    print("Retirar 4 de A10: aceite")
except ValueError as erro:
    print("Retirar 4 de A10: recusado:", erro)

try:
    inventario.retirar("A10", 5)
    print("Retirar 5 de A10: aceite")
except ValueError as erro:
    print("Retirar 5 de A10: recusado:", erro)

print("Fim")
print("A10: quantidade", inventario.quantidade_de("A10"), "e saídas", inventario.saidas_de("A10"))
print("A11: quantidade", inventario.quantidade_de("A11"), "e saídas", inventario.saidas_de("A11"))
```

Em relação ao programa de partida do caderno 6, há três diferenças. O artigo tem as saídas, guardadas no atributo interno `_saidas` e consultadas pela propriedade `saidas`. O inventário tem o método `saidas_de(codigo)`, que encontra o artigo pelo código e devolve as suas saídas, tal como `quantidade_de(codigo)` devolve a quantidade. E não há método `acertar`: o método que falta escrever é o `retirar`, nas duas classes.

## Parte 1: preparar o ficheiro e observar o programa inicial (15 min)

1. Na pasta onde guardas os trabalhos de LP, cria uma pasta nova chamada `caderno-6`. Dentro dela, cria um ficheiro chamado `inventario.py`. O nome tem de acabar em `.py` e não deve ter espaços nem acentos.
2. Copia para o ficheiro o programa inicial completo, desde a primeira linha da docstring até à última linha, a que mostra a quantidade e as saídas de A11 no fim. Guarda.
3. Antes de executares, lê o programa por zonas, como no caderno 6, secção 2: primeiro o programa principal, no fim do ficheiro; depois os métodos do inventário que ele chama; só depois a classe `Artigo`. Procura as duas linhas que dizem "Por completar": estão no método `retirar` do inventário e no método `retirar` do artigo. Repara também na propriedade `saidas`: tem getter, mas não tem setter, por isso o código de fora pode consultar as saídas, mas não as pode alterar.
4. Executa o ficheiro inteiro. Depois responde por escrito:
   - O pedido para retirar 4 unidades de A10 devia ser aceite, tendo em conta os dados iniciais? Porquê?
   - O que diz o programa sobre esse pedido?
   - Que quantidade e que saídas ficaram guardadas em A10 no fim?
   - O programa tem um erro de sintaxe ou um erro de comportamento? Explica a diferença numa frase.

Guarda estas respostas: vais precisar delas na parte 6, para as comparares com o programa corrigido. Se o programa parar com uma mensagem de erro, a cópia ficou com algum engano: consulta a tabela de problemas frequentes, no fim deste laboratório.

## Parte 2: explicar o modelo antes de alterar o código (20 min)

Numa folha, desenha em UML leve, como no caderno 4, secções 5 e 6, e no caderno 6, secção 6, passo 8:

- a caixa da classe `Artigo` e a caixa da classe `Inventario`, com os atributos e os métodos da interface pública de cada uma;
- a linha entre as duas caixas, com o losango, se o houver, e as multiplicidades;
- as caixas de objeto dos dois artigos no início do programa, com os valores de cada atributo.

Por baixo do desenho, responde:

1. Neste programa, a relação entre `Inventario` e `Artigo` é uma composição ou uma agregação? Justifica com as perguntas da secção 7 do caderno 4, indicando a linha do programa onde os artigos são criados.
2. Que objeto encontra o artigo a partir do código? Que objeto decide se há unidades suficientes? Que objeto guarda as saídas?
3. Porque é que faz sentido que a propriedade `saidas` não tenha setter? Pensa no que podia acontecer às saídas se qualquer parte do programa as pudesse escrever.

Mostra ao professor antes de avançar: o diagrama de classes, as caixas de objeto e as três respostas.

## Parte 3: completar a retirada (40 min)

A operação de retirada tem duas partes, uma em cada classe, e vais completar as duas.

O método `retirar(codigo, unidades)` do inventário recebe o código de um artigo e as unidades a retirar. Encontra o artigo com esse código e passa-lhe o pedido. Não verifica as unidades: essas regras são do artigo.

O método `retirar(unidades)` do artigo recebe as unidades a retirar, decide se o pedido é possível e, se for, altera os dados do artigo. Deve cumprir este contrato:

| Situação | O que acontece | Quantidade | Saídas |
| --- | --- | --- | --- |
| As unidades são um número inteiro, 1 ou mais, e não ultrapassam a quantidade | O pedido é aceite e o método termina sem mensagem | Diminui as unidades pedidas | Aumentam as unidades pedidas |
| As unidades não são um número inteiro | `ValueError` com a mensagem "As unidades a retirar têm de ser um número inteiro." | Fica igual | Ficam iguais |
| As unidades são inteiras, mas menores do que 1 | `ValueError` com a mensagem "As unidades a retirar têm de ser 1 ou mais." | Fica igual | Ficam iguais |
| As unidades ultrapassam a quantidade | `ValueError` | Fica igual | Ficam iguais |

No último caso, podes deixar a recusa ao setter da quantidade, como no caderno 3, e então a mensagem é a do setter, "A quantidade não pode ser negativa."; ou podes verificar no próprio método se há unidades suficientes, e então usa a mensagem "Não há unidades suficientes.". As duas formas cumprem o contrato. Escolhe uma: na conversa com o professor, no fim, vais explicar porque a escolheste.

Se o código não existir, quem recusa é o inventário, com o `ValueError` do método `_procurar`, "Não existe nenhum artigo com o código ...", e nenhum artigo muda.

Zero é uma quantidade válida: retirar todas as unidades de um artigo deixa-o com quantidade 0, e o pedido é aceite. Pedir para retirar zero unidades é recusado.

Dentro do artigo, as saídas mudam-se no atributo interno `_saidas`, porque a propriedade `saidas` não tem setter.

Trabalha por esta ordem:

1. Escreve primeiro, no papel e por palavras, os passos de cada um dos dois métodos, pela ordem em que devem acontecer. Ao lado de cada passo do método do artigo, escreve o que já mudou no artigo se o pedido for recusado logo nesse passo.

   Mostra ao professor antes de avançar: os passos dos dois métodos, por palavras.

2. Completa só o interior dos dois métodos `retirar`, no teu ficheiro `inventario.py`, no lugar das linhas "Por completar" e do `pass` que se lhes segue. Não mudes o resto do programa: o registo dos artigos, as consultas, a adição e o programa principal já estão preparados.
3. Executa o ficheiro inteiro. Se aparecer uma mensagem de erro do Python, lê primeiro a última linha, que diz o tipo de erro, e depois as de cima, que dizem onde aconteceu. A tabela de problemas frequentes, no fim deste laboratório, ajuda com as mensagens mais comuns.

Para recordar como um método recusa um pedido com `raise` antes de alterar o estado, consulta o caderno 3, secção 12. Para recordar como o inventário encontra um artigo e lhe passa um pedido, consulta o caderno 4, secção 10, passo 5, e o caderno 6, secção 5. Usa números pequenos. Não precisas de pedir dados a quem usa o programa, de criar páginas, de guardar ficheiros nem de acrescentar outras funcionalidades.

## Parte 4: verificar a sequência do programa (10 min)

O programa principal pede para retirar 4 unidades de A10 e, a seguir, 5. Antes de executares o teu programa completado, copia esta tabela para a folha e preenche as colunas de previsão. Cada linha começa no estado deixado pela anterior.

| Momento | Resposta prevista | A10: quantidade e saídas previstas | A11: quantidade e saídas previstas | O que observaste no ecrã |
| --- | --- | --- | --- | --- |
| Início | Não há pedido | 6 e 0 | 3 e 0 | A preencher |
| Depois de pedir 4 a A10 | A preencher | A preencher | A preencher | A preencher |
| Depois de pedir 5 a A10 | A preencher | A preencher | A preencher | A preencher |

Depois executa o ficheiro inteiro e preenche a última coluna. Confirma também a regra da soma: a quantidade e as saídas de A10 continuam a somar 6? Se a previsão e a observação forem diferentes, não alteres a previsão só para ficar igual ao ecrã. Procura primeiro qual das duas está errada e escreve porquê. Se for o programa, corrige-o e volta a executar o ficheiro inteiro.

Mostra ao professor antes de avançar: a tabela, com as previsões e as observações e, se alguma previsão foi diferente do ecrã, a explicação da diferença.

## Parte 5: verificar outros casos (25 min)

Agora vais experimentar outras situações. Cada linha da tabela é um ensaio separado, que começa com um programa acabado de iniciar, em que A10 tem 6 unidades e 0 saídas e A11 tem 3 unidades e 0 saídas.

Para não mexeres no teu ficheiro de trabalho, guarda uma cópia dele, na mesma pasta, com o nome `ensaios.py`. Nessa cópia, mantém as duas classes e as três linhas que criam o inventário e registam os artigos. Substitui todas as linhas a partir de `print("Início")` por este bloco:

```python partial
print("Antes")
print("A10: quantidade", inventario.quantidade_de("A10"), "e saídas", inventario.saidas_de("A10"))
print("A11: quantidade", inventario.quantidade_de("A11"), "e saídas", inventario.saidas_de("A11"))

try:
    inventario.retirar("A11", 3)
    print("Pedido aceite")
except ValueError as erro:
    print("Pedido recusado:", erro)

print("Depois")
print("A10: quantidade", inventario.quantidade_de("A10"), "e saídas", inventario.saidas_de("A10"))
print("A11: quantidade", inventario.quantidade_de("A11"), "e saídas", inventario.saidas_de("A11"))
```

Este bloco depende das classes e do inventário criados acima; não é para executar sozinho. A linha `inventario.retirar("A11", 3)` é o pedido. Em cada ensaio, muda o código e as unidades dessa linha para os da tabela e executa outra vez o ficheiro inteiro, para voltares a começar com os valores iniciais. Preenche as previsões antes de cada execução.

| Pedido | Aceite ou recusado, e quem recusa | Mensagem prevista | A10 depois: quantidade e saídas | A11 depois: quantidade e saídas | Resultado observado |
| --- | --- | --- | --- | --- | --- |
| `retirar("A11", 3)` | A preencher | A preencher | A preencher | A preencher | A preencher |
| `retirar("A11", 0)` | A preencher | A preencher | A preencher | A preencher | A preencher |
| `retirar("A11", 1.5)` | A preencher | A preencher | A preencher | A preencher | A preencher |
| `retirar("A12", 1)` | A preencher | A preencher | A preencher | A preencher | A preencher |

Em cada ensaio, lê as quatro linhas de estado, as de A10 e as de A11, antes e depois do pedido. Um pedido feito a A11 não deve mudar A10, e só confirmas isso se olhares para as duas.

Faz ainda um último ensaio, desta vez com dois pedidos seguidos, sem reiniciar entre eles: retirar 3 unidades de A11 e, logo a seguir, retirar 1. Para isso, copia o bloco do `try` e do `except` e cola a cópia logo a seguir ao primeiro, antes da linha `print("Depois")`, com o pedido de 1 unidade. Prevê e regista as duas respostas e o estado final dos dois artigos. Depois explica, em duas frases, o que a segunda resposta diz sobre retirar unidades de um artigo vazio, e porque é que as saídas de A11 têm o valor que têm.

Se tiveres tempo, ensaia também `retirar("A11", -1)` e `retirar("A11", "2")`, um de cada vez, com previsão.

Mostra ao professor antes de avançar: a tabela dos quatro ensaios e o ensaio dos dois pedidos seguidos, com as duas frases.

## Parte 6: explicar a correção (10 min)

Volta às respostas que escreveste na parte 1, antes de completares os métodos. Escolhe um pedido que o programa inicial tratava mal e que o teu programa agora trata de acordo com o contrato. Escreve quatro frases, cada uma com valores ou instruções concretas:

1. "Esperava ...": o que o pedido devia fazer à quantidade e às saídas.
2. "Observei ...": o que o programa inicial mostrou.
3. "A instrução que explica a diferença é ...": a linha do programa inicial responsável e porquê.
4. "Depois da alteração, confirmei ...": o que o teu programa mostra agora, com os valores.

## Parte 7: conversa curta com o professor (5 min)

No fim, o professor conversa contigo durante uns cinco minutos, com o teu programa aberto. A conversa não dá nota: serve para tu e o professor perceberem o que já está firme e o que precisa de mais prática antes do projeto. Se trabalhaste em par, a conversa é individual na mesma, e cada pessoa explica o seu próprio raciocínio.

Não precisas de recitar definições: usa o teu programa e os valores. O professor escolhe uma ou duas destas tarefas:

- mostrar, no teu código, onde o pedido é encaminhado e onde é decidido;
- explicar porque é que uma recusa não pode alterar nem a quantidade nem as saídas, apontando a linha do teu código que garante isso;
- explicar que forma escolheste para recusar a falta de unidades, a do setter ou a da verificação no método, e porquê;
- mostrar como confirmaste que A10 não mudou nos ensaios feitos com A11;
- prever o resultado de um pedido com outros valores, escolhido pelo professor, antes de o executares;
- encontrar e corrigir um erro que o professor introduza numa cópia do teu programa.

Podes dizer em que passos recebeste ajuda: essa informação serve para orientar o trabalho seguinte.

## Problemas frequentes neste laboratório

| O que aparece | O que costuma ser | Como resolver |
| --- | --- | --- |
| `IndentationError: unindent does not match any outer indentation level` | Uma linha de um método ficou com uma indentação diferente das outras linhas do mesmo método | Dentro de um método, todas as linhas ficam alinhadas com a docstring: oito espaços a partir da margem |
| `NameError: name '_procurar' is not defined` | Dentro de um método do inventário, a chamada ficou escrita `_procurar(codigo)`, sem o `self.` à frente | Escreve `self._procurar(codigo)`, como em `quantidade_de` (caderno 4, secção 10, passo 5). As versões recentes do Python acrescentam à mensagem a sugestão `Did you mean: 'self._procurar'?` |
| `AttributeError: property 'saidas' of 'Artigo' object has no setter`, ou `AttributeError: can't set attribute` nas versões do Python anteriores à 3.11 | O método do artigo escreve nas saídas através da propriedade, com `self.saidas = ...`, e a propriedade não tem setter | Dentro do artigo, as saídas mudam-se no atributo interno `_saidas`, como diz a parte 3 |
| `TypeError: '<=' not supported between instances of 'str' and 'int'`, ou o mesmo com outro sinal de comparação, no ensaio com `"2"` | O método compara as unidades com um número antes de verificar se são um número inteiro, e o Python não sabe comparar um texto com um número | Verifica primeiro o tipo e só depois o valor, pela ordem do setter e do exemplo guiado do caderno 3 (secções 7 e 12) |
| O programa diz "aceite", mas a quantidade e as saídas não mudaram | Um dos métodos `retirar` ainda não faz nada: ficou só com o `pass`, ou o inventário encontra o artigo mas não lhe passa o pedido | Segue o pedido desde o programa principal até ao método do artigo, e confirma que cada passo chama o seguinte |
| Num ensaio, o programa para com um traceback que acaba em `ValueError`, em vez de mostrar "Pedido recusado" | O pedido ficou fora do `try` | Põe o pedido dentro do `try`, como no bloco da parte 5, com o `except ValueError as erro` por baixo |

## O que fica guardado

Guarda a pasta `caderno-6`, com os ficheiros `inventario.py` e `ensaios.py`, e a folha com o diagrama, as respostas, as tabelas e as quatro frases da parte 6. Entrega-os pelo meio indicado pelo professor e guarda uma cópia para ti: vais voltar a precisar destas ideias.

## A seguir: o projeto

As ideias que juntaste neste laboratório são as ideias centrais do M10: distinguir a classe dos objetos e do estado de cada um, proteger os dados de um objeto quando ele recusa um pedido, e dar cada tarefa ao objeto que tem a informação para a fazer, como o inventário que encontra o artigo e o artigo que decide. Vão ser avaliadas no [projeto](../projeto/README.md): a tua aplicação, com um tema que escolhes de uma lista preparada pelo professor, avaliada no fim do M12, com demonstração, explicação e uma pequena alteração feita na hora. O projeto é a avaliação prática do M10, do M11 e do M12, cada uma com os critérios do seu módulo, e os critérios do M10 são estas três ideias, agora na tua aplicação.

O projeto começa já no fim do M10, com a escolha do tema e o modelo da tua aplicação em UML leve, como o que desenhaste na parte 2. A conversa da parte 7 é um primeiro ensaio da explicação que o projeto te vai pedir: o que é cada objeto, onde está a regra e o que acontece aos dados quando um pedido é recusado.

![Rodapé](../imagens/rodape.png)

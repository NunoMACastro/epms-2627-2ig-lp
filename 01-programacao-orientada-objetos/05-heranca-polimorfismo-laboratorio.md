![Cabeçalho](../imagens/cabecalho.png)

# Laboratório: Herança e polimorfismo

Laboratório do tema Herança e polimorfismo, do módulo M10, Introdução à Programação Orientada por Objetos. Vais construir notificações em Python, com herança, polimorfismo e uma classe abstrata: uma classe base, várias variantes que herdam dela e um ciclo que as apresenta todas. Cada passo diz o que fazer, porquê e o que deves ver, e avanças ao teu ritmo. O que não acabares na aula, acabas em casa ou na aula seguinte. Tudo o que precisas está aqui; o [guia do tema](05-heranca-polimorfismo.md) tem a teoria completa, para quem quiser saber mais.

## O que vais construir

No fim, tens um ficheiro `notificacoes.py` com uma classe abstrata, `Notificacao`, quatro variantes que herdam dela e um ciclo que pede a todas que se apresentem. Uma notificação é uma mensagem preparada para ser apresentada a alguém, como "Contagem concluída" ou "A02 esgotou". As variantes apresentam-se de maneiras diferentes: só com o texto, com um aviso antes, com o nome de quem a enviou, ou em maiúsculas. Pelo caminho, provocas de propósito três erros típicos da herança e lês as mensagens que o Python mostra.

As classes do fim da fase 5 estão desenhadas neste diagrama de classes:

![Diagrama: Notificacao, com o nome em itálico e {abstract}, o atributo texto e o método apresentar() em itálico; por baixo, NotificacaoBreve, NotificacaoDetalhada e NotificacaoAssinada, esta com o atributo origem, todas com o método apresentar(); as três ligam-se a Notificacao por linhas que se juntam num triângulo vazio](../imagens/uml-notificacao-abstrata.svg)

Lê-o assim. Cada caixa é uma classe. Em cima está o nome da classe, no meio os atributos e em baixo os métodos, com os parâmetros entre parênteses. O `self` e o construtor `__init__` não se escrevem, porque todas as classes os têm. As linhas que saem das três caixas de baixo acabam num triângulo vazio, encostado à caixa `Notificacao`. Esse triângulo quer dizer "é um". Para ler a ligação, começa numa caixa de baixo, segue a linha até ao triângulo e diz a frase: `NotificacaoAssinada` é uma `Notificacao`. As caixas de baixo mostram só o que acrescentam à de cima ou o que mudam nela. O `{abstract}` e o itálico dizem que `Notificacao` é uma classe abstrata, uma ideia que aprendes na fase 5. Na fase 6 juntas uma quarta variante, a urgente, que entra no diagrama da mesma maneira.

| Fase | O que muda | O que funciona no fim |
| --- | --- | --- |
| 1 | Escreves a classe base `Notificacao` e a classe derivada `NotificacaoBreve` | Uma notificação breve com texto, sem a classe derivada escrever construtor nem métodos |
| 2 | Acrescentas a `NotificacaoDetalhada`, que redefine o método `apresentar` | Duas variantes que se apresentam de maneiras diferentes |
| 3 | Acrescentas a `NotificacaoAssinada`, com um dado novo e `super()` | Uma variante que guarda a origem e aproveita o construtor da base |
| 4 | Pões as três variantes numa lista e apresenta-las com um ciclo `for` | O mesmo pedido, três respostas diferentes |
| 5 | Tornas a classe base abstrata, com o módulo `abc` | O Python recusa criar uma notificação geral e uma variante que não escreveu o `apresentar` |
| 6 | Acrescentas a `NotificacaoUrgente`, sem mexer no ciclo | Quatro variantes no mesmo ciclo, e o texto guardado intacto |

Em todas as fases trabalhas da mesma maneira. Antes de executares o programa, escreves no papel o que esperas ver. Depois executas e comparas. Quando o resultado é diferente do que previste, explica a diferença antes de continuares: é essa explicação que mais te ensina.

Executa sempre o ficheiro inteiro. Cada execução começa do zero, com os valores escritos no programa. Nas fases 2, 3, 5 e 6 vais estragar o programa de propósito, para veres um erro acontecer. Faz sempre a alteração pedida, observa e desfaz a alteração antes de continuares.

## Palavras que vais usar

- Relação "é um": a relação entre um tipo particular e um tipo mais geral, como "uma bicicleta é um veículo" ou "uma notificação breve é uma notificação". Confirma-se dizendo a frase em voz alta. Quando a frase parece quase verdadeira, há um teste: se A é um B, tudo o que um B tem e faz tem de fazer sentido para A. Não se confunde com a relação "tem": uma mochila tem cadernos, mas não é um caderno. Para saber mais, vê "Especialização: do geral para o particular" no [guia](05-heranca-polimorfismo.md).
- Herança: a forma de escrever a relação "é um" em Python. Em `class NotificacaoBreve(Notificacao):`, a classe entre parênteses é a classe base, a geral, e a que se está a escrever é a classe derivada, a particular. Lê-se "a classe `NotificacaoBreve`, que é uma `Notificacao`".
- Herdar: a classe derivada recebe da base os seus métodos, incluindo o construtor, sem os escrever outra vez.
- Redefinir um método: escrever, numa classe derivada, um método com o mesmo nome de um método da base. Em inglês diz-se *override*.
- Regra de procura: quando se chama um método sobre um objeto, o Python procura-o primeiro na classe do objeto, depois na classe base, depois na base da base.
- `super()`: dá acesso aos métodos da classe base, para o mesmo objeto. O nome vem de superclasse, o outro nome da classe base. `super().__init__(texto)`, dentro de um construtor, pede ao construtor da base que faça a sua parte.
- Polimorfismo: o mesmo pedido, feito da mesma maneira, funciona com objetos de classes diferentes, e cada um responde à sua maneira.
- Contrato: o que um método promete, a quem o chama. Aqui: o método `apresentar` não recebe nada além do `self`, devolve um texto e não altera a notificação.
- Classe abstrata e método abstrato: uma classe abstrata descreve o que é comum a várias classes, mas não se criam objetos dela. Um método abstrato tem o nome e o contrato, mas não tem instruções: cada classe derivada tem de o escrever.
- Módulo `abc`: um ficheiro de código que vem com o Python, com as ferramentas `ABC` e `abstractmethod` (do inglês *abstract method*, "método abstrato") para escrever classes abstratas. A sigla vem do inglês *Abstract Base Classes*, "classes base abstratas".
- Decorador: uma linha que começa por `@`, antes de um `def`, e muda a maneira como o método é usado. Já conheces o `@property`, do tema 03.
- Lista e ciclo `for`: uma lista guarda vários valores por ordem, entre parênteses retos, e pode guardar objetos. O `for` repete o bloco indentado por baixo dele uma vez por cada elemento da lista. Vêm do 10.º ano.
- `isinstance(valor, Classe)`: pergunta se um valor é de uma certa classe, e dá `True` ou `False`. *Is instance* quer dizer "é instância de". Vem do tema 03.
- Exceção: um sinal de que alguma coisa correu mal, que interrompe o programa, a não ser que um `try` com o `except` certo a apanhe. Vem do tema 03.
- Mensagem de erro: o texto que o Python mostra quando para por causa de um erro. Quando o erro acontece com o programa a correr, a primeira linha é `Traceback (most recent call last)`, que quer dizer "o rasto, com a chamada mais recente no fim". Num erro de escrita, como um `IndentationError` ("erro de indentação"), o Python nem começa a correr o programa. Nos dois casos, a última linha diz o tipo de erro e o que aconteceu.
- Tipos de erro, do tema 03: um erro de escrita é recusado pelo Python antes de o programa começar. Um erro de execução para o programa a meio. Um erro de lógica deixa o programa correr, mas com um resultado errado.

## O que precisas

- O editor de Python que usas nas aulas, para escrever e executar os programas. Confirma que funciona: num ficheiro de ensaio, escreve `print("Olá")` e executa. Deve aparecer `Olá`, o que quer dizer que o editor está a executar programas de Python.
- O Python 3, a partir da versão 3.10. Nas versões mais antigas, algumas mensagens de erro são um pouco diferentes, e o laboratório diz onde.
- Papel e caneta, para as previsões, as tabelas, as respostas e o diagrama.

O laboratório começa de uma pasta vazia. Não precisas de nenhum ficheiro dos laboratórios anteriores.

## Se alguma coisa falhar

1. Guardaste o ficheiro antes de executar? O editor executa o que está guardado no disco. Guarda e executa outra vez.
2. Estás a executar o ficheiro certo? Confirma que o separador aberto é o `notificacoes.py` da pasta `tema-05`.
3. Apareceu uma mensagem de erro? Lê a última linha: diz o tipo de erro e o que aconteceu. Procura essa linha em [Problemas frequentes](#problemas-frequentes).
4. Desfizeste a experiência da fase anterior? Cada experiência diz como a desfazer. Se te perderes, copia o ficheiro completo da paragem mais recente que mostra o ficheiro inteiro, a [paragem 3](#paragem-3) ou a [paragem 5](#paragem-5), e continua a partir daí.

## Preparar o projeto

1. Na pasta onde guardas os trabalhos de LP, cria uma pasta nova chamada `tema-05`. É aí que fica o ficheiro deste laboratório.
2. Dentro dela, cria um ficheiro novo chamado `notificacoes.py`. O nome tem de acabar em `.py`, para o editor o reconhecer como um programa de Python, e não deve ter espaços nem acentos.

## Fase 1: Uma classe derivada que herda tudo

Imagina duas classes de notificações quase iguais. As duas guardam um texto no construtor, e as duas têm um método `apresentar` que devolve um texto. Escrever as duas por inteiro repetia o construtor, e uma regra nova sobre o texto teria de ser escrita nos dois sítios.

A herança resolve isto. Escreve-se uma vez o que é comum, numa classe geral, a classe base. Depois escreve-se cada variante como uma classe derivada, que recebe da base tudo o que ela tem. Só se justifica quando a frase "é um" é verdadeira, e é: "uma notificação breve é uma notificação". Para saber mais, lê "Herança em Python" no [guia](05-heranca-polimorfismo.md).

1. Escreve no ficheiro, à mão, este conteúdo. É o ficheiro completo, por agora. Escrever, em vez de copiar, obriga-te a reparar em cada pormenor, como os parênteses na linha `class NotificacaoBreve(Notificacao):`.

   ```python
   # notificacoes.py: notificações com herança, do laboratório do tema 05.

   class Notificacao:
       """Uma mensagem preparada para ser apresentada a alguém."""

       def __init__(self, texto):
           """Guarda o texto da notificação."""
           self.texto = texto

       def apresentar(self):
           """Devolve o texto da notificação, pronto a mostrar."""
           return self.texto


   class NotificacaoBreve(Notificacao):
       """Notificação que apresenta só o texto: faz tudo como a classe base."""
   ```

   Leitura guiada: a primeira linha é um comentário que diz o que é o ficheiro. A classe `Notificacao` é a classe base: tem um construtor, que guarda o texto, e um método `apresentar`, que o devolve. A classe `NotificacaoBreve` é a classe derivada. Tem o nome da base entre parênteses e só tem a docstring: não escreve construtor nem métodos. O corpo de uma classe não pode ficar vazio, e a docstring conta como conteúdo.

2. Guarda e executa. O que deves ver: nada. O ficheiro só define classes, e definir uma classe não mostra nada no ecrã. Se aparecer uma mensagem de erro, vê os [problemas frequentes](#problemas-frequentes).

3. No fim do ficheiro, encostadas à margem e depois de duas linhas em branco, acrescenta estas linhas de teste:

   ```python partial
   breve = NotificacaoBreve("Contagem concluída")
   print(breve.texto)
   print(breve.apresentar())
   print(isinstance(breve, NotificacaoBreve))
   print(isinstance(breve, Notificacao))
   ```

4. Antes de executares, responde no papel. A classe `NotificacaoBreve` não escreve construtor: que construtor vai ser executado na primeira linha, e onde está escrito? E que `apresentar` vai ser executado na terceira linha? Escreve também as quatro linhas que esperas ver. Depois executa. O que deves ver:

   ```text
   Contagem concluída
   Contagem concluída
   True
   True
   ```

   A resposta: nas duas linhas é executado o que está escrito na classe `Notificacao`. Quando se chama um método sobre um objeto, o Python procura-o primeiro na classe do objeto. Se não o encontrar lá, procura na classe base. Chama-se a isto a regra de procura, e vale também para o construtor. A tabela mostra-a aplicada às duas chamadas:

   | Chamada | Classe do objeto | Essa classe escreve o método? | Onde o Python encontra o método | Resultado |
   | --- | --- | --- | --- | --- |
   | `NotificacaoBreve("Contagem concluída")`, o construtor | `NotificacaoBreve` | Não | Na classe base, `Notificacao` | O objeto fica com o texto |
   | `breve.apresentar()` | `NotificacaoBreve` | Não | Na classe base, `Notificacao` | `Contagem concluída` |

   O primeiro `True` diz que a notificação é uma `NotificacaoBreve`. O segundo diz que é também uma `Notificacao`: o Python sabe que um objeto de uma classe derivada é, ao mesmo tempo, um objeto da classe base. É a relação "é um", escrita em código.

### Paragem 1

O ficheiro tem as duas classes, e o programa mostra as quatro linhas acima.

Pensa antes de continuares: se criasses outra notificação breve, com o texto "Material em falta", o texto da primeira mudava? A resposta: não. Herdar não é partilhar valores. A herança liga as duas classes: diz que a descrição de `NotificacaoBreve` inclui a de `Notificacao`. Os valores continuam a pertencer a cada objeto, e cada notificação breve guarda o seu próprio texto.

## Fase 2: Uma variante que redefine um método

A notificação detalhada apresenta-se de outra maneira: com "Aviso interno: " antes do texto. Também é uma notificação, e por isso herda da base. Mas não lhe serve o `apresentar` que a base tem. Escreve o seu, com o mesmo nome. Quando uma classe derivada escreve um método com o mesmo nome de um método da base, diz-se que o **redefine**. Pela regra de procura, o Python encontra primeiro o da classe do objeto, e é esse que usa. Para saber mais, lê "Redefinir um método: onde o Python procura" no [guia](05-heranca-polimorfismo.md).

1. Entre a classe `NotificacaoBreve` e as linhas de teste, escreve a classe `NotificacaoDetalhada`. Deixa duas linhas em branco antes e depois dela.

   ```python partial
   class NotificacaoDetalhada(Notificacao):
       """Notificação que apresenta o texto com um aviso antes."""

       def apresentar(self):
           """Devolve o texto com "Aviso interno: " antes."""
           return "Aviso interno: " + self.texto
   ```

   Leitura guiada: a classe herda de `Notificacao`, e por isso herda o construtor. Escreve só o método `apresentar`, que junta "Aviso interno: " ao texto com o `+` e devolve o resultado.

2. Substitui todas as linhas de teste, a partir de `breve = ...`, por estas:

   ```python partial
   breve = NotificacaoBreve("Contagem concluída")
   detalhada = NotificacaoDetalhada("Material em falta")
   print(breve.apresentar())
   print(detalhada.apresentar())
   ```

3. Antes de executares, copia para o papel esta tabela e completa a segunda linha, com a regra de procura. A primeira já está feita.

   | Chamada | Classe do objeto | Essa classe escreve `apresentar`? | Onde o Python encontra `apresentar` | Resultado |
   | --- | --- | --- | --- | --- |
   | `breve.apresentar()` | `NotificacaoBreve` | Não | Na classe base, `Notificacao` | `Contagem concluída` |
   | `detalhada.apresentar()` | A completar | A completar | A completar | A completar |

   Depois executa. O que deves ver:

   ```text
   Contagem concluída
   Aviso interno: Material em falta
   ```

   A segunda linha da tabela: a classe do objeto é `NotificacaoDetalhada`, que escreve o seu `apresentar`; o Python encontra-o na própria classe, e o resultado é `Aviso interno: Material em falta`. Repara que o `apresentar` da `Notificacao` continua lá: a notificação breve usou-o na primeira linha. Redefinir não apaga o método da base. Só o tapa para os objetos da classe derivada.

4. Agora, uma experiência. Na classe `NotificacaoDetalhada`, apaga o método `apresentar` inteiro: a linha do `def`, a docstring e a linha do `return`. Deixa só a docstring da classe. Antes de executares, escreve o que achas que a segunda linha vai mostrar. Depois executa. O que deves ver:

   ```text
   Contagem concluída
   Material em falta
   ```

   A segunda linha passou a mostrar o texto sem o aviso, e não apareceu nenhum erro. Responde no papel: de que classe veio o `apresentar` usado agora, e porquê? Porque é que o Python não se queixou?

   A resposta: o `apresentar` veio da classe base, `Notificacao`. A detalhada deixou de ter o seu, e o Python, pela regra de procura, foi buscá-lo à base. Não se queixou porque, para ele, não falta nada: a classe herda um `apresentar` que funciona. Mas a notificação detalhada passou a apresentar-se como breve, e ninguém foi avisado. Guarda esta resposta: na fase 5 vais ver como se obriga cada variante a escrever o seu `apresentar`.

5. Volta a escrever o método `apresentar` da classe `NotificacaoDetalhada`, como no passo 1, e executa. O aviso deve voltar à segunda linha.

### Paragem 2

O programa mostra `Contagem concluída` e `Aviso interno: Material em falta`.

Pensa antes de continuares: quando `breve.apresentar()` executa o método escrito na classe `Notificacao`, quem é o `self`? A resposta: é a notificação breve, o objeto que está antes do ponto, como em todas as chamadas que já fizeste. O método foi escrito na base, mas trabalha sobre o objeto que recebeu o pedido. É por isso que `self.texto` é o texto desta notificação.

## Fase 3: Uma variante com um dado novo: `super()`

Uma especialização também pode acrescentar dados. A notificação assinada diz, no fim, quem a enviou: "Encomenda recebida (enviada por: Secretaria)". Além do texto, guarda a origem, e por isso o seu construtor recebe dois valores. Uma classe derivada escreve o seu próprio construtor quando tem de fazer, na criação, alguma coisa que o da base não faz. É o caso: guardar a origem. A breve e a detalhada não tinham nada a acrescentar, e por isso herdaram o construtor da base.

O construtor novo tapa o da base. Mas o da base sabe guardar o texto, e queremos aproveitá-lo, para a regra sobre o texto continuar num só sítio. Por isso, a primeira linha do construtor novo é `super().__init__(texto)`. Lê-se "executa o construtor da classe base, com este texto, sobre este objeto". Para criar uma notificação, continuas a escrever o nome da classe, `NotificacaoAssinada(...)`, e não `__init__`. O `super().__init__` serve para um construtor pedir ajuda ao da base. Para saber mais, lê "Acrescentar dados numa classe derivada: `super()`" no [guia](05-heranca-polimorfismo.md).

1. A seguir à classe `NotificacaoDetalhada`, com duas linhas em branco antes e depois, escreve a classe `NotificacaoAssinada`:

   ```python partial
   class NotificacaoAssinada(Notificacao):
       """Notificação que diz, no fim, quem a enviou."""

       def __init__(self, texto, origem):
           """Guarda o texto, através do construtor da classe base, e a origem."""
           super().__init__(texto)
           self.origem = origem

       def apresentar(self):
           """Devolve o texto seguido da origem, entre parênteses."""
           return self.texto + " (enviada por: " + self.origem + ")"
   ```

   Leitura guiada: começa pelo construtor. Recebe dois valores, além do `self`. A primeira linha passa o texto ao construtor da base, que o guarda em `self.texto`. A segunda guarda a origem, que é só desta classe. O `apresentar` junta três textos com o `+`: o texto, "(enviada por: " com a origem, e o parêntese que fecha.

2. Substitui todas as linhas de teste, a partir de `breve = ...`, por estas:

   ```python partial
   assinada = NotificacaoAssinada("Encomenda recebida", "Secretaria")
   print(assinada.origem)
   print(assinada.apresentar())
   ```

3. Prevê as duas linhas e executa. O que deves ver:

   ```text
   Secretaria
   Encomenda recebida (enviada por: Secretaria)
   ```

4. Agora, a experiência do esquecimento. No construtor de `NotificacaoAssinada`, apaga a linha `super().__init__(texto)`. Antes de executares, responde no papel: em que linha do programa achas que vai aparecer o erro, na que cria a notificação ou na que a apresenta? Depois executa.

   O programa mostra `Secretaria` e depois para. A última linha da mensagem de erro deve ser esta:

   ```text
   AttributeError: 'NotificacaoAssinada' object has no attribute 'texto'
   ```

   Em português: o objeto do tipo `NotificacaoAssinada` não tem o atributo `texto`. Um `AttributeError` ("erro de atributo") aparece quando se pede a um objeto um atributo que ele não tem.

5. Lê a mensagem de baixo para cima. Por cima da última linha há duas entradas, cada uma com uma linha que começa por `File`, com o caminho do teu ficheiro e o número da linha. A de baixo acaba em `in apresentar`, e por baixo dela está a linha `return self.texto + " (enviada por: " + self.origem + ")"`. A de cima acaba em `in <module>`, que quer dizer "no programa principal", com a linha `print(assinada.apresentar())`. A partir do Python 3.11, aparecem também linhas com `~` e `^`, que sublinham a parte da linha onde o erro aconteceu. Responde no papel:

   1. Em que método estava o Python quando o erro aconteceu?
   2. A criação da notificação correu bem, e o erro só apareceu na chamada seguinte. Porquê?
   3. A mensagem aponta para o método `apresentar`, mas o engano está no construtor. Porque é que o erro aparece longe da causa?
   4. Que tipo de erro é: de escrita, de execução ou de lógica?

   As respostas:

   1. No método `apresentar`: a entrada de baixo acaba em `in apresentar`, na linha que usa `self.texto`.
   2. O construtor da assinada foi executado sem problemas: guardou a origem e terminou. Nenhuma linha usou o texto durante a criação. O construtor da base, que o guardaria, nunca foi chamado, porque o da derivada o tapa e já não o chamava.
   3. O erro aparece onde o texto é usado pela primeira vez, mas a causa está onde o texto devia ter sido guardado. Quando um objeto não tem um atributo que devia ter, procura primeiro no construtor.
   4. De execução: o programa começou, mostrou `Secretaria` e parou a meio.

6. Volta a escrever a linha `super().__init__(texto)`, como primeira linha do construtor, e executa. As duas linhas do passo 3 devem voltar.

### Paragem 3

O programa mostra `Secretaria` e `Encomenda recebida (enviada por: Secretaria)`. O ficheiro `notificacoes.py` completo, como deve estar agora:

```python
# notificacoes.py: notificações com herança, do laboratório do tema 05.

class Notificacao:
    """Uma mensagem preparada para ser apresentada a alguém."""

    def __init__(self, texto):
        """Guarda o texto da notificação."""
        self.texto = texto

    def apresentar(self):
        """Devolve o texto da notificação, pronto a mostrar."""
        return self.texto


class NotificacaoBreve(Notificacao):
    """Notificação que apresenta só o texto: faz tudo como a classe base."""


class NotificacaoDetalhada(Notificacao):
    """Notificação que apresenta o texto com um aviso antes."""

    def apresentar(self):
        """Devolve o texto com "Aviso interno: " antes."""
        return "Aviso interno: " + self.texto


class NotificacaoAssinada(Notificacao):
    """Notificação que diz, no fim, quem a enviou."""

    def __init__(self, texto, origem):
        """Guarda o texto, através do construtor da classe base, e a origem."""
        super().__init__(texto)
        self.origem = origem

    def apresentar(self):
        """Devolve o texto seguido da origem, entre parênteses."""
        return self.texto + " (enviada por: " + self.origem + ")"


assinada = NotificacaoAssinada("Encomenda recebida", "Secretaria")
print(assinada.origem)
print(assinada.apresentar())
```

Pensa antes de continuares: porque é que a `NotificacaoBreve` e a `NotificacaoDetalhada` não têm a linha do `super()`? A resposta: porque não escrevem construtor. Herdam o da base, e é ele que é executado quando se cria uma delas. O `super().__init__` só faz falta dentro de um construtor que tapa o da base.

## Fase 4: O mesmo pedido a todas: polimorfismo

Agora vais guardar uma notificação de cada variante numa lista e pedir a cada uma, num ciclo `for`, que se apresente. Uma lista pode guardar objetos, tal como guarda números ou textos. Em cada volta do ciclo, o nome do ciclo aponta para um dos objetos da lista. O ciclo vai ter uma única linha de trabalho, igual nas três voltas. Mesmo assim, cada volta vai dar um resultado diferente, porque o Python encontra o `apresentar` da classe de cada objeto. Chama-se **polimorfismo** a isto: o mesmo pedido, feito da mesma maneira, funciona com objetos de classes diferentes, e cada objeto responde à sua maneira. A palavra vem do grego e quer dizer "muitas formas". Para saber mais, lê "Polimorfismo: a mesma chamada, comportamentos diferentes" no [guia](05-heranca-polimorfismo.md).

1. Substitui todas as linhas de teste, a partir de `assinada = ...`, por estas:

   ```python partial
   avisos = [
       NotificacaoBreve("Contagem concluída"),
       NotificacaoDetalhada("Material em falta"),
       NotificacaoAssinada("Encomenda recebida", "Secretaria"),
   ]

   for aviso in avisos:
       print(aviso.apresentar())
   ```

   Leitura guiada: a lista é escrita com os três objetos criados dentro dos parênteses retos, um por linha, separados por vírgulas. É o mesmo que criar uma lista vazia e fazer três `append`, só que mais curto. A vírgula depois do último objeto é opcional; escreve-se para que, ao acrescentar um elemento numa linha nova, não seja preciso mexer na de cima. O ciclo dá três voltas, e em cada uma o nome `aviso` aponta para uma das notificações.

2. Antes de executares, copia para o papel esta tabela e completa-a, uma volta de cada vez.

   | Volta | Classe do objeto | Onde o Python encontra `apresentar` | Linha mostrada |
   | --- | --- | --- | --- |
   | 1 | A completar | A completar | A completar |
   | 2 | A completar | A completar | A completar |
   | 3 | A completar | A completar | A completar |

3. Executa e compara com a tua tabela. O que deves ver:

   ```text
   Contagem concluída
   Aviso interno: Material em falta
   Encomenda recebida (enviada por: Secretaria)
   ```

   A tabela completa:

   | Volta | Classe do objeto | Onde o Python encontra `apresentar` | Linha mostrada |
   | --- | --- | --- | --- |
   | 1 | `NotificacaoBreve` | Na classe base, `Notificacao` | `Contagem concluída` |
   | 2 | `NotificacaoDetalhada` | Na própria classe | `Aviso interno: Material em falta` |
   | 3 | `NotificacaoAssinada` | Na própria classe | `Encomenda recebida (enviada por: Secretaria)` |

### Paragem 4

O programa mostra as três linhas acima, uma por variante.

Pensa antes de continuares: se escrevesses uma quarta variante, que linhas do ciclo `for` terias de mudar? A resposta: nenhuma. Juntavas um objeto da variante nova à lista, e o ciclo pedia-lhe que se apresentasse como pede às outras. Nenhuma linha do teu programa pergunta de que variante é cada notificação. Quem escolhe o `apresentar` certo é o Python, a partir da classe de cada objeto.

## Fase 5: Uma classe base abstrata

A classe `Notificacao` tem dois problemas. O primeiro é que se pode criar uma notificação "geral", com `Notificacao("Olá")`, que se apresenta como a breve. Mas uma notificação geral não tem uma maneira definida de se apresentar. O segundo viste-o na fase 2: uma variante que se esquece do `apresentar` apresenta-se como breve, e ninguém é avisado.

A solução é tornar a `Notificacao` uma **classe abstrata**: uma classe que descreve o que é comum a todas as variantes, mas de onde não se criam objetos. O método `apresentar` passa a ser um **método abstrato**. Tem o nome e o contrato, mas não tem instruções, e cada variante é obrigada a escrevê-lo. O Python não tem uma palavra própria para "abstrato". Usa o módulo `abc`, que vem com a linguagem. Uma classe abstrata herda de `ABC`, e um método abstrato leva antes do `def` o decorador `@abstractmethod`. Para saber mais, lê "Abstração, classes abstratas e o módulo `abc`" no [guia](05-heranca-polimorfismo.md).

1. Logo a seguir à primeira linha do ficheiro, o comentário, deixa uma linha em branco e escreve esta linha. Depois dela, deixa duas linhas em branco antes da classe `Notificacao`.

   ```python partial
   from abc import ABC, abstractmethod
   ```

   Leitura guiada: lê-se "do módulo `abc`, importa `ABC` e `abstractmethod`". Um módulo é um ficheiro de código Python que outros programas podem usar; este vem instalado com o Python. Não confundas com os módulos da disciplina, como o M10. Depois desta linha, os dois nomes podem ser usados no resto do ficheiro.

2. Muda a primeira linha da classe base para `class Notificacao(ABC):`. Muda também a docstring da classe para `"""Uma mensagem preparada para ser apresentada a alguém. Classe abstrata."""`. É a herança desta fase: herdar de `ABC` é o que dá à `Notificacao` a capacidade de ter métodos abstratos.

3. Substitui o método `apresentar` da classe `Notificacao`, as três linhas, por esta versão abstrata, com a mesma indentação:

   ```python partial
       @abstractmethod
       def apresentar(self):
           """Contrato: não recebe nada além do self, devolve um texto pronto
           a mostrar e não altera a notificação. Cada variante escreve como."""
   ```

   Leitura guiada: o decorador `@abstractmethod` marca o método como abstrato. O corpo tem só a docstring, que é o contrato, escrito em duas linhas. Não tem instruções, porque não há uma maneira geral de apresentar uma notificação. Tal como numa classe, a docstring chega para o corpo não ficar vazio. Repara que o construtor da `Notificacao` não mudou: uma classe abstrata pode ter métodos com instruções, que as variantes herdam.

4. Não mudes mais nada. Antes de executares, pensa na experiência da fase 2: há alguma classe derivada que ainda não escreveu o seu próprio `apresentar`? Escreve no papel o que achas que vai acontecer. Depois executa.

   O programa para logo na criação da lista, sem mostrar nenhuma linha. A última linha da mensagem depende da versão do Python. Nas versões mais recentes é esta:

   ```text
   TypeError: Can't instantiate abstract class NotificacaoBreve without an implementation for abstract method 'apresentar'
   ```

   Em português: não se pode criar um objeto da classe abstrata `NotificacaoBreve` sem a implementação do método abstrato `apresentar`. A implementação de um método são as suas instruções. *Instantiate* quer dizer "instanciar", criar uma instância. Até à versão 3.11, a linha acaba em `with abstract method apresentar`, "com o método abstrato `apresentar`". Um `TypeError` é um "erro de tipo", que já viste no tema 03.

   Responde no papel: porque é que a `NotificacaoBreve` deixou de poder ser criada, se não lhe mexeste? Que tem isto a ver com a experiência da fase 2?

   A resposta: a `NotificacaoBreve` contava com o `apresentar` da base, e esse passou a abstrato, sem instruções. A breve continua a ter um método abstrato por completar. Por isso é, ela também, uma classe abstrata, e o Python não deixa criar objetos dela, mesmo sem ninguém lhe ter mexido. É o mesmo esquecimento da fase 2: uma variante sem o seu `apresentar`. Antes passava em silêncio. Agora é detetado no momento em que se tenta criar o objeto, perto da causa.

5. Resolve o problema na classe `NotificacaoBreve`. Substitui a classe inteira por esta versão, que escreve o seu próprio `apresentar` e tem a docstring certa. A antiga dizia "faz tudo como a classe base", e isso deixou de ser verdade.

   ```python partial
   class NotificacaoBreve(Notificacao):
       """Notificação que apresenta só o texto."""

       def apresentar(self):
           """Devolve o texto tal como está guardado."""
           return self.texto
   ```

   Executa. As três linhas da fase 4 devem voltar a aparecer.

6. No fim do ficheiro, fora de qualquer `try`, acrescenta a linha `geral = Notificacao("Olá")` e executa. Depois das três linhas, o programa para. Lê a última linha da mensagem e diz, por palavras tuas, o que ela quer dizer.

   A resposta: a última linha é `TypeError: Can't instantiate abstract class Notificacao without an implementation for abstract method 'apresentar'`, ou, até à versão 3.11, `... with abstract method apresentar`. Quer dizer que não se pode criar um objeto da classe abstrata `Notificacao`, porque o método abstrato `apresentar` não tem instruções. É o primeiro problema do início desta fase, resolvido: já não há notificações "gerais".

   Depois de responderes, apaga a linha `geral = Notificacao("Olá")`.

7. No papel, completa o contrato abstrato da `Notificacao`, escrito nesta forma, organizada por indentação. As três primeiras linhas já estão feitas.

   ```text
   Classe abstrata Notificacao
       Todas têm: um texto, guardado quando a notificação é criada
       Todas sabem: apresentar()   (abstrato: cada variante escreve como)
           recebe: A completar
           devolve: A completar
           não faz: A completar
   ```

   A resposta: recebe nada, além do `self`; devolve um texto pronto a mostrar; não altera a notificação e não mostra nada no ecrã. Quem decide o que fazer com o texto é quem o pediu: mostra-o no terminal, numa página ou noutro sítio. Esta forma de escrever é como o pseudocódigo: não há uma forma única. O que conta é que se perceba o que é comum a todas as variantes, e que o contrato do método abstrato esteja por inteiro.

### Paragem 5

O programa mostra as três linhas da fase 4, agora com a classe base abstrata. O ficheiro `notificacoes.py` completo, como deve estar agora:

```python
# notificacoes.py: notificações com herança, do laboratório do tema 05.

from abc import ABC, abstractmethod


class Notificacao(ABC):
    """Uma mensagem preparada para ser apresentada a alguém. Classe abstrata."""

    def __init__(self, texto):
        """Guarda o texto da notificação."""
        self.texto = texto

    @abstractmethod
    def apresentar(self):
        """Contrato: não recebe nada além do self, devolve um texto pronto
        a mostrar e não altera a notificação. Cada variante escreve como."""


class NotificacaoBreve(Notificacao):
    """Notificação que apresenta só o texto."""

    def apresentar(self):
        """Devolve o texto tal como está guardado."""
        return self.texto


class NotificacaoDetalhada(Notificacao):
    """Notificação que apresenta o texto com um aviso antes."""

    def apresentar(self):
        """Devolve o texto com "Aviso interno: " antes."""
        return "Aviso interno: " + self.texto


class NotificacaoAssinada(Notificacao):
    """Notificação que diz, no fim, quem a enviou."""

    def __init__(self, texto, origem):
        """Guarda o texto, através do construtor da classe base, e a origem."""
        super().__init__(texto)
        self.origem = origem

    def apresentar(self):
        """Devolve o texto seguido da origem, entre parênteses."""
        return self.texto + " (enviada por: " + self.origem + ")"


avisos = [
    NotificacaoBreve("Contagem concluída"),
    NotificacaoDetalhada("Material em falta"),
    NotificacaoAssinada("Encomenda recebida", "Secretaria"),
]

for aviso in avisos:
    print(aviso.apresentar())
```

Pensa antes de continuares: abstrata quer dizer vazia? Olha para a classe `Notificacao` do teu ficheiro. A resposta: não. A classe abstrata tem um construtor com instruções, que guarda o texto e que todas as variantes herdam. Abstrata quer dizer incompleta de propósito: há uma parte, o `apresentar`, que só as classes derivadas completam.

## Fase 6: Uma variante nova, sem mudar o ciclo

O responsável do armário da sala quer que os avisos de material esgotado chamem a atenção. Pede uma notificação que se apresente com "URGENTE: " antes do texto, e com o texto todo em maiúsculas. "Uma notificação urgente é uma notificação", e por isso a classe nova herda da `Notificacao`. Não guarda dados novos, e por isso não escreve construtor. Como o `apresentar` é abstrato, é obrigada a escrevê-lo.

Para pôr um texto em maiúsculas, os textos do Python têm o método `upper` (do inglês, "de cima", como nas letras maiúsculas): `"A02 esgotou".upper()` devolve `"A02 ESGOTOU"`. O `upper` devolve um texto novo, e o texto original fica como estava. É isso que permite cumprir o contrato: o `apresentar` devolve um texto novo e não altera a notificação. Para saber mais, lê o exemplo guiado do [guia](05-heranca-polimorfismo.md).

1. A seguir à classe `NotificacaoAssinada`, com duas linhas em branco antes e depois, escreve a classe `NotificacaoUrgente`:

   ```python partial
   class NotificacaoUrgente(Notificacao):
       """Notificação que pede atenção imediata: o texto aparece em maiúsculas."""

       def apresentar(self):
           """Devolve "URGENTE: " seguido do texto em maiúsculas, sem alterar o texto guardado."""
           return "URGENTE: " + self.texto.upper()
   ```

   Leitura guiada: a classe só escreve o `apresentar`. O `self.texto.upper()` lê-se da esquerda para a direita: o texto desta notificação, e depois um texto novo, igual a ele, em maiúsculas. O `+` junta-lhe "URGENTE: " à frente.

2. Na lista `avisos`, depois da linha da notificação assinada, acrescenta uma linha com `NotificacaoUrgente("A02 esgotou"),`. No fim do ficheiro, depois do ciclo e encostada à margem, acrescenta esta linha:

   ```python partial
   print("Texto guardado na urgente:", avisos[3].texto)
   ```

   `avisos[3]` é o quarto elemento da lista, porque os índices começam em 0.

3. Antes de executares, escreve as cinco linhas que esperas ver. Depois executa. O que deves ver:

   ```text
   Contagem concluída
   Aviso interno: Material em falta
   Encomenda recebida (enviada por: Secretaria)
   URGENTE: A02 ESGOTOU
   Texto guardado na urgente: A02 esgotou
   ```

   A quarta linha vem do `apresentar` da `NotificacaoUrgente`. A última confirma o contrato: o texto guardado continua em minúsculas, porque o `upper` devolveu um texto novo e o atributo `texto` não foi tocado.

4. Responde no papel: que linhas do ciclo `for` tiveste de mudar para a variante nova funcionar? A resposta: nenhuma. Escreveste uma classe nova e juntaste um objeto à lista. O ciclo é, letra a letra, o da fase 4. É isto que o polimorfismo permite.

5. Uma experiência, para veres o contrato a ser quebrado. No `apresentar` da `NotificacaoUrgente`, substitui a linha do `return` por estas duas, com a mesma indentação:

   ```python partial
           self.texto = self.texto.upper()
           return "URGENTE: " + self.texto
   ```

   Executa. As quatro primeiras linhas ficam iguais, mas a última passa a `Texto guardado na urgente: A02 ESGOTOU`. O método mudou o atributo `texto`, que passou a apontar para o texto em maiúsculas, e o contrato diz que o `apresentar` não altera a notificação. Repara que nenhuma mensagem de erro avisou: só a última linha mostra o problema. Volta a pôr a linha do `return` como estava no passo 1, e executa outra vez para confirmar que a última linha voltou a `A02 esgotou`.

6. No papel, copia o diagrama de "O que vais construir" e acrescenta-lhe a caixa da `NotificacaoUrgente`, com a sua linha até ao triângulo. Na caixa nova, escreve só o que a classe acrescenta ou muda em relação à `Notificacao`. A resposta: a caixa tem o nome `NotificacaoUrgente`, a zona dos atributos vazia e `apresentar()` na zona dos métodos. A classe não guarda dados novos, e escreve o seu próprio `apresentar`. A linha sai da caixa nova e junta-se às outras, até ao triângulo encostado à `Notificacao`.

### Paragem 6

O programa mostra as cinco linhas do passo 3. O ficheiro `notificacoes.py` completo, como deve estar no fim:

```python
# notificacoes.py: notificações com herança, do laboratório do tema 05.

from abc import ABC, abstractmethod


class Notificacao(ABC):
    """Uma mensagem preparada para ser apresentada a alguém. Classe abstrata."""

    def __init__(self, texto):
        """Guarda o texto da notificação."""
        self.texto = texto

    @abstractmethod
    def apresentar(self):
        """Contrato: não recebe nada além do self, devolve um texto pronto
        a mostrar e não altera a notificação. Cada variante escreve como."""


class NotificacaoBreve(Notificacao):
    """Notificação que apresenta só o texto."""

    def apresentar(self):
        """Devolve o texto tal como está guardado."""
        return self.texto


class NotificacaoDetalhada(Notificacao):
    """Notificação que apresenta o texto com um aviso antes."""

    def apresentar(self):
        """Devolve o texto com "Aviso interno: " antes."""
        return "Aviso interno: " + self.texto


class NotificacaoAssinada(Notificacao):
    """Notificação que diz, no fim, quem a enviou."""

    def __init__(self, texto, origem):
        """Guarda o texto, através do construtor da classe base, e a origem."""
        super().__init__(texto)
        self.origem = origem

    def apresentar(self):
        """Devolve o texto seguido da origem, entre parênteses."""
        return self.texto + " (enviada por: " + self.origem + ")"


class NotificacaoUrgente(Notificacao):
    """Notificação que pede atenção imediata: o texto aparece em maiúsculas."""

    def apresentar(self):
        """Devolve "URGENTE: " seguido do texto em maiúsculas, sem alterar o texto guardado."""
        return "URGENTE: " + self.texto.upper()


avisos = [
    NotificacaoBreve("Contagem concluída"),
    NotificacaoDetalhada("Material em falta"),
    NotificacaoAssinada("Encomenda recebida", "Secretaria"),
    NotificacaoUrgente("A02 esgotou"),
]

for aviso in avisos:
    print(aviso.apresentar())

print("Texto guardado na urgente:", avisos[3].texto)
```

Pensa antes de terminares: porque é que a `NotificacaoUrgente` não tem construtor nem `super()`? A resposta: porque não guarda dados novos, só o texto, que a base já guarda. Herda o construtor da base, como a breve e a detalhada.

## Problemas frequentes

### `NameError: name 'Notificacao' is not defined`

Em português: o nome `Notificacao` não está definido. Um `NameError` ("erro de nome") aparece quando se usa um nome que o Python não conhece. A mensagem aponta a linha de uma classe derivada, como `class NotificacaoBreve(Notificacao):`. A classe base foi escrita depois dessa linha, ou tem outro nome. O Python lê o ficheiro de cima para baixo: a classe base tem de estar escrita antes das classes que herdam dela. As versões recentes do Python podem acrescentar uma sugestão, como `Did you mean: ...?`, "querias dizer ...?", se houver um nome parecido.

### `NameError: name 'ABC' is not defined`

Em português: o nome `ABC` não está definido. Falta a linha `from abc import ABC, abstractmethod` no início do ficheiro, ou tem um engano. Confirma a linha, com as maiúsculas de `ABC`.

### `IndentationError: expected an indented block after class definition on line`

Em português: esperava-se um bloco indentado a seguir à definição da classe da linha indicada. Nas versões anteriores ao Python 3.10, a mensagem é só `IndentationError: expected an indented block`. O programa nem chega a correr. Uma classe ficou sem nenhuma linha por baixo, nem sequer a docstring, por exemplo depois de apagares o `apresentar` na fase 2 e também a docstring da classe. Escreve a docstring da classe, indentada quatro espaços.

### `TypeError: NotificacaoAssinada.__init__() missing 1 required positional argument: 'origem'`

Em português: falta ao construtor de `NotificacaoAssinada` um argumento obrigatório, a `origem`. Nas versões anteriores ao Python 3.10, a mensagem começa por `__init__()`, sem o nome da classe. Foi criada uma notificação com menos valores do que o seu construtor pede. Vê quantos valores o construtor dessa classe recebe, sem contar o `self`, e passa-os todos, pela mesma ordem.

### `TypeError: Notificacao.__init__() missing 1 required positional argument: 'texto'`

Em português: falta ao construtor de `Notificacao` o argumento `texto`. A mensagem aponta a linha do `super()`, que ficou `super().__init__()`, com os parênteses vazios. O construtor da base também precisa do texto, e quem lho dá é a classe derivada, nessa chamada. Escreve `super().__init__(texto)`.

### `TypeError: Can't instantiate abstract class ...`

Uma classe derivada não se deixa criar, porque o Python acha que lhe falta o `apresentar`. Confirma três coisas: que a classe escreve o método; que o nome é exatamente `apresentar`, letra a letra; e que o `def` está indentado dentro da classe. Um método `apresenta`, ou encostado à margem, não conta: para o Python, o `apresentar` abstrato continua por escrever.

### `AttributeError: 'NotificacaoAssinada' object has no attribute 'texto'`

Falta a linha `super().__init__(texto)` no construtor da `NotificacaoAssinada`. Sem ela, o construtor da base nunca é executado, e o objeto fica sem o atributo `texto`. O erro aparece mais tarde, no método que usa o texto. Põe a linha do `super()` como primeira linha do construtor.

### Na fase 5 não aparece nenhum erro, e o ciclo mostra `None`

Falta o `(ABC)` na primeira linha da classe base: a linha ficou `class Notificacao:`. Sem essa herança, o `@abstractmethod` não tem efeito nenhum. O Python deixa criar a notificação breve, e o `apresentar` abstrato, sem instruções, devolve `None`, o valor que quer dizer "nada". Confirma que a linha é `class Notificacao(ABC):`.

### Aparece `None` numa das linhas do ciclo, e uma linha a mais por cima

O `apresentar` de uma variante tem um `print` em vez de um `return`. O `print` do método mostra o texto, e depois o `print` do ciclo mostra o que o método devolveu: `None`, porque um método sem `return` não devolve nada. Troca o `print` por `return`: quem pede o texto é que decide se o mostra.

## Desafios

1. Uma variante tua, sem dados novos. Inventa uma maneira nova de apresentar uma notificação, só a partir do texto. Por exemplo, pôr o texto entre parênteses retos, ou começar por "Lembrete: ". Escolhe tu, desde que seja diferente das variantes deste laboratório. Escreve a classe, com uma docstring em cada classe e em cada método. Antes de a escreveres, decide e escreve no papel: esta variante precisa de construtor próprio? Porquê?

   Depois junta um objeto da tua variante à lista `avisos`. Antes de executares, escreve a linha nova que esperas ver. Por fim, acrescenta uma linha que mostre o atributo `texto` da tua notificação depois do ciclo, e confirma que não mudou.

   Pista: pensa no que a variante tem de guardar que a base ainda não guarde.

2. Uma variante tua, com um dado novo. Inventa uma variante que precise de guardar mais um dado além do texto. Por exemplo, uma notificação com prazo, que se apresente como "Devolver os marcadores (até sexta-feira)". Escolhe tu o dado e o formato, desde que sejam diferentes da notificação assinada. Escreve a classe, com um construtor que receba o texto e o dado novo. Junta um objeto desta variante à lista, prevê a linha que vai aparecer e executa.

   Pista: lembra-te do que aconteceu na fase 3, quando faltou uma linha no construtor.

3. O diagrama do teu programa. No papel, desenha o diagrama de classes do teu programa final, sem copiar o de "O que vais construir". Desenha a classe abstrata `Notificacao`, com o nome em itálico ou com `{abstract}`, e todas as variantes que o teu ficheiro tem, também as tuas. Liga cada variante à `Notificacao` com uma linha e o triângulo. Em cada caixa de uma variante, escreve só o que ela acrescenta ou redefine.

## Antes de terminares

- [ ] O ficheiro `notificacoes.py` executa e mostra as cinco linhas da paragem 6, mais as linhas das tuas variantes, se fizeste os desafios.
- [ ] Desfizeste as experiências: o `apresentar` da detalhada voltou, a linha do `super()` voltou, o `return` da urgente está como no passo 1 da fase 6, e apagaste a linha `geral = Notificacao("Olá")`.
- [ ] Tens no papel as previsões, as tabelas das fases 2 e 4, as respostas das fases 3 e 5, o contrato da fase 5 e o diagrama da fase 6.
- [ ] Guardaste o `notificacoes.py` e a folha, e entregaste-os pelo meio indicado pelo professor.
- [ ] Sabes dizer onde é que o Python encontrou o `apresentar` de cada volta do ciclo.
- [ ] Sabes dizer porque é que a notificação breve deixou de poder ser criada na fase 5.
- [ ] Consegues explicar, por palavras tuas, o que é o polimorfismo, com o ciclo deste laboratório.

![Rodapé](../imagens/rodape.png)

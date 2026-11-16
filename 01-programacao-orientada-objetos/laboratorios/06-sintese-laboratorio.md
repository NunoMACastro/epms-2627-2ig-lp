![Cabeçalho](../../imagens/cabecalho.png)

# Laboratório: Síntese

## O que vais construir

Completas a retirada de material num inventário em Python, em que cada artigo guarda também as suas saídas: as unidades que já saíram em retiradas aceites. Antes do código, descreves o modelo do programa e o plano da operação. Depois, confirmas o resultado com ensaios, explicas a correção num comentário e, no fim, conversas com o professor.

1. [Fase 1: Um programa que corre e não faz o que devia](#fase-1-um-programa-que-corre-e-não-faz-o-que-devia)
2. [Fase 2: O modelo antes do código](#fase-2-o-modelo-antes-do-código)
3. [Fase 3: O plano da retirada](#fase-3-o-plano-da-retirada)
4. [Fase 4: Os dois métodos, e a sequência do programa](#fase-4-os-dois-métodos-e-a-sequência-do-programa)
5. [Fase 5: Outros casos, cada um num ensaio](#fase-5-outros-casos-cada-um-num-ensaio)
6. [Fase 6: Explicar a correção](#fase-6-explicar-a-correção)

## O que precisas

- O Python 3.10 ou mais recente. No terminal, `python3 --version` mostra a versão que tens (no Windows, o comando é `py --version`), numa linha como `Python 3.12.4`. Com uma versão mais antiga, tudo corre da mesma maneira, e mudam só algumas mensagens de erro, que o texto indica.
- O editor de Python com que fizeste os laboratórios dos temas anteriores.

Começas com uma pasta vazia, porque o programa inicial vem todo em [Preparar o projeto](#preparar-o-projeto).

## Preparar o projeto

1. Na pasta dos teus trabalhos de LP, cria a pasta `tema-06` e, dentro dela, o ficheiro `inventario.py`, com o nome escrito assim, sem espaços nem acentos. Os ficheiros deste laboratório ficam todos nessa pasta.

2. Copia para o `inventario.py` a primeira parte do programa inicial, a docstring do ficheiro e a classe `Artigo`:

   ```python
   """Laboratório do tema 06: o inventário de uma sala, com as saídas de cada artigo.

   No programa inicial, as duas partes da operação de retirada, a do inventário
   e a do artigo, estão por completar, nas linhas que dizem "Por completar".
   Nessa versão, o programa executa do princípio ao fim sem mensagens de erro,
   mas não faz o que o problema pede. Todo o resto já está preparado e não muda.
   """


   class Artigo:
       """Artigo do inventário: código, nome, uma quantidade sempre válida e as saídas.

       A quantidade é uma propriedade com getter e setter, como no tema 03.
       As saídas contam quantas unidades já saíram por retiradas aceites.
       São uma propriedade só com getter: o código de fora pode consultá-las,
       mas não as pode alterar pela propriedade. O atributo interno _saidas
       continua acessível, mas o sublinhado avisa que não se mexe nele de fora.
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

           Não há setter: as saídas mudam-se no atributo interno _saidas,
           dentro dos métodos do próprio artigo.
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
   ```

   Repara em duas coisas. A propriedade `saidas` tem o `@property` e o getter, e não tem setter. É uma propriedade só com getter: de fora lê-se, como em `artigo.saidas`, mas não se escreve. E o `retirar` só tem um comentário "Por completar" e o `pass`, uma instrução que não faz nada e só marca o sítio onde o código vai entrar. É um dos dois métodos que vais escrever. Rever: [A propriedade `quantidade`](../03-encapsulamento-contratos.md#a-propriedade-quantidade).

   Guarda e executa. O que deves ver: nada, porque o ficheiro só define a classe, e nenhuma linha cria um artigo. Se aparecer uma mensagem de erro, a cópia ficou com um engano: vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

3. Deixa duas linhas em branco depois do `pass` do `Artigo` e copia a segunda parte, a classe `Inventario`. A linha `class Inventario:` fica encostada à margem, como a da classe `Artigo`, e o `def` de cada método a quatro espaços:

   ```python
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
   ```

   O `retirar` do inventário também está por completar. Guarda e executa: continua a não aparecer nada.

4. Deixa outra vez duas linhas em branco e copia a última parte, o programa principal, encostado à margem:

   ```python
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

   Guarda, mas não executes ainda: a fase 1 começa com uma previsão.

5. Lê o programa por zonas, a começar pelo fim. Primeiro, o programa principal, as linhas que vêm depois das classes: cria o inventário, regista A10 e A11, mostra o início, pede duas retiradas a A10 e mostra o fim. Depois, procura na classe `Inventario` os métodos que ele chama, e só no fim desce à classe `Artigo`. Rever: [Um programa lê-se por zonas](../06-sintese.md#um-programa-lê-se-por-zonas).

## Fase 1: Um programa que corre e não faz o que devia

Executas o programa inicial e vês se ele faz o que devia. Quando não faz, tem um erro de lógica, o tipo de erro de que o Python não avisa. Rever: [Um programa que corre e não faz o que devia](../06-sintese.md#um-programa-que-corre-e-não-faz-o-que-devia) e [Nada impede uma quantidade impossível](../03-encapsulamento-contratos.md#nada-impede-uma-quantidade-impossível).

1. Antes de executares, prevê: o que diz o programa sobre os dois pedidos a A10? E com que quantidade e que saídas fica A10 no fim? Depois guarda e executa o ficheiro inteiro. O que deves ver:

   ```text
   Início
   A10: quantidade 6 e saídas 0
   A11: quantidade 3 e saídas 0
   Retirar 4 de A10: aceite
   Retirar 5 de A10: aceite
   Fim
   A10: quantidade 6 e saídas 0
   A11: quantidade 3 e saídas 0
   ```

   A resposta: corre até ao fim, sem nenhuma mensagem de erro, e diz "aceite" aos dois pedidos. No fim, A10 continua com quantidade 6 e saídas 0. Os dois métodos `retirar` só têm o `pass`, que não faz nada nem lança nenhuma exceção, e por isso nenhum pedido chega ao `except`. Se o programa parar com uma mensagem, a cópia ficou com um engano: vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

2. Responde de cabeça, a olhar para o ecrã. Pensa na tua resposta antes de leres a que vem a seguir.

   1. O pedido para retirar 4 unidades de A10 devia ser aceite?

      A resposta: sim. 4 é um número inteiro, é 1 ou mais e não passa das 6 unidades de A10.

   2. O programa escreveu "aceite" nesse pedido. Isso prova que as 4 unidades saíram?

      A resposta: não. O programa principal escreve "aceite" sempre que o `try` chega ao fim sem exceção, e um método que não faz nada também não lança nenhuma. O que mostra se o pedido foi cumprido é o estado de A10 depois dele, e continua em 6 e 0.

   3. Porque é que este erro é de lógica, e não de escrita nem de execução?

      A resposta: com um erro de escrita, o Python recusava o ficheiro antes de começar, e com um de execução o programa parava a meio. Este programa corre do princípio ao fim, sem nenhuma mensagem, e faz uma coisa diferente da que o problema pede.

### Paragem 1

O programa corre sem nenhuma mensagem de erro, diz "aceite" aos dois pedidos e não muda nada.

Pensa antes de continuares: o pedido de 5 também aparece como "aceite". Depois de aceite o de 4, devia ser aceite? A resposta: não. Depois de retirar 4, A10 ficaria com 2 unidades, e 5 é mais do que 2. Com os métodos completos, este pedido vai ser recusado.

## Fase 2: O modelo antes do código

Descreves por palavras, num comentário no fim do `inventario.py`, as duas classes, a relação entre elas e o estado dos dois artigos. É o modelo do programa, e escreve-se antes de mexer no código, para cada regra ir parar ao objeto certo. Rever: [O modelo antes do código](../06-sintese.md#o-modelo-antes-do-código) e [O inventário descrito por palavras](../04-composicao-modelacao.md#o-inventário-descrito-por-palavras).

1. Cola este comentário no fim do `inventario.py`, depois do programa principal. É o modelo do inventário do tema 04, dito por outras palavras, e ainda sem as saídas. Fica no fim do ficheiro, com `#` no início de cada linha, para o Python não o ler como código e para as linhas do programa não mudarem de número.

   ```python partial
   # O modelo do programa
   #
   # Artigo
   # - Cada artigo guarda um código, um nome e uma quantidade, que é sempre um
   #   número inteiro não negativo.
   # - Um artigo cria-se com o código, o nome e a quantidade inicial.
   # - A um artigo pode pedir-se que adicione unidades, com adicionar(unidades),
   #   e que retire unidades, com retirar(unidades).
   #
   # Inventario
   # - Cada inventário guarda os seus artigos, e nunca dois com o mesmo código.
   # - Um inventário cria-se vazio, sem nenhum valor.
   # - A um inventário pode pedir-se que registe um artigo novo, com
   #   registar(codigo, nome, quantidade); que diga a quantidade de um artigo,
   #   com quantidade_de(codigo); e que retire unidades de um artigo, com
   #   retirar(codigo, unidades).
   #
   # A relação entre as duas classes
   # - Um inventário tem artigos, e é uma composição.
   # - Um artigo só faz sentido dentro do seu inventário, porque é uma linha
   #   do registo.
   # - É o inventário que cria cada artigo, quando se lhe pede que o registe.
   # - Cada artigo pertence a um só inventário e desaparece se o inventário
   #   desaparecer.
   ```

   Completa-o com o que este programa tem a mais. Na classe `Artigo`, falta o dado que conta as saídas e com quantas começa; na classe `Inventario`, o pedido que as consulta. Confirma também se a relação muda com as saídas, e corrige-a se mudar.

2. Por baixo, escreve o estado dos dois artigos no início do programa, numa frase para cada um, com o valor de cada dado, também das saídas. No tema 04, o estado do caderno acabado de registar era: "O artigo A01 chama-se Caderno e tem 6 unidades."

3. Por baixo do estado, responde, no mesmo comentário:

   1. Neste programa, a relação entre `Inventario` e `Artigo` é uma composição ou uma agregação? Justifica com duas perguntas: a parte faz sentido sem o todo? Quem cria a parte? Indica a linha do programa onde os artigos são criados.
   2. Que objeto encontra o artigo a partir do código? Que objeto decide se há unidades suficientes? Que objeto guarda as saídas?
   3. Porque é que faz sentido que a propriedade `saidas` não tenha setter? Pensa no que podia acontecer às saídas se qualquer parte do programa as pudesse escrever.

   Guarda e executa. O que deves ver: as oito linhas da fase 1, iguais, porque um comentário não muda o que o programa faz. Se aparecer uma mensagem de erro numa linha de português, falta-lhe o `#`: vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

### Paragem 2

Mostra ao professor antes de leres a resposta: a descrição das classes e da relação, o estado dos dois artigos e as três respostas. Chama-o e mostra-lhe o ecrã. Se houver alguma coisa a corrigir, ele não te dá a resposta: aponta-te uma linha ou faz-te uma pergunta, e tu corriges e voltas a mostrar. Nas paragens 3, 4 e 5 é igual.

O comentário de referência, com o modelo e o estado:

```python partial
# O modelo do programa
#
# Artigo
# - Cada artigo guarda um código, um nome, uma quantidade, que é sempre um
#   número inteiro não negativo, e as saídas, o total de unidades que já
#   saíram por retiradas aceites.
# - Um artigo cria-se com o código, o nome e a quantidade inicial, e começa
#   sem nenhuma saída.
# - A um artigo pode pedir-se que adicione unidades, com adicionar(unidades),
#   e que retire unidades, com retirar(unidades).
#
# Inventario
# - Cada inventário guarda os seus artigos, e nunca dois com o mesmo código.
# - Um inventário cria-se vazio, sem nenhum valor.
# - A um inventário pode pedir-se que registe um artigo novo, com
#   registar(codigo, nome, quantidade); que diga a quantidade de um artigo,
#   com quantidade_de(codigo), ou as saídas de um artigo, com
#   saidas_de(codigo); e que retire unidades de um artigo, com
#   retirar(codigo, unidades).
#
# A relação entre as duas classes
# - Um inventário tem artigos, e é uma composição.
# - Um artigo só faz sentido dentro do seu inventário, porque é uma linha
#   do registo.
# - É o inventário que cria cada artigo, quando se lhe pede que o registe.
# - Cada artigo pertence a um só inventário e desaparece se o inventário
#   desaparecer.
#
# O estado no início do programa
# - O artigo A10 chama-se Régua, tem 6 unidades e 0 saídas.
# - O artigo A11 chama-se Cola, tem 3 unidades e 0 saídas.
```

A relação ficou a do tema 04, porque as saídas não mudam quem cria os artigos nem quem os guarda. Se escreveste `_quantidade` e `_saidas`, troca-os pela quantidade e pelas saídas: são os atributos internos onde os valores vivem, e a descrição mostra o que quem usa a classe vê. Se identificaste um artigo por um nome, como `regua`, corrige-o: esse nome não existe no programa, que chega a cada artigo pelo inventário e pelo código. Se escreveste valores na descrição de uma classe, tira-os, porque os valores de um artigo concreto vão só no estado dele.

As respostas:

1. Composição. A primeira pergunta é a que decide, e a resposta é não: um artigo não faz sentido sem o inventário, porque é uma linha do registo dele. A segunda vai no mesmo sentido: é o inventário que cria os artigos, na linha `novo = Artigo(codigo, nome, quantidade)`, dentro do método `registar`, e o programa principal não cria nem guarda nenhum. Ter uma lista não basta para ser composição: a playlist do guia 04 também tem uma, e é uma agregação.
2. O inventário encontra o artigo pelo código, no método interno `_procurar`. O artigo decide se há unidades suficientes, no setter da quantidade, que recusa um valor negativo. O artigo guarda as saídas, no atributo interno `_saidas`.
3. Sem setter, o código de fora não pode alterar as saídas pela propriedade: `artigo.saidas = 5` dá `AttributeError`. Assim, as saídas só mudam dentro do `retirar` do artigo, depois das verificações. Se qualquer parte do programa as pudesse escrever, o total podia deixar de corresponder às retiradas aceites, por engano ou com um valor sem sentido, como um negativo. E ninguém saberia onde se tinha estragado.

## Fase 3: O plano da retirada

Escreves por palavras o plano dos dois métodos `retirar`, o do artigo e o do inventário, antes de escreveres o código. Cada passo do plano diz o que já mudou se o pedido for recusado ali, e os passos que podem recusar vêm todos antes das alterações. Rever: [O plano da retirada](../06-sintese.md#o-plano-da-retirada) e [O inventário passa os pedidos aos artigos](../04-composicao-modelacao.md#o-inventário-passa-os-pedidos-aos-artigos).

1. O `retirar(unidades)` do artigo cumpre este contrato:

   | Pedido | O que acontece | Quantidade | Saídas |
   | --- | --- | --- | --- |
   | Um número inteiro, 1 ou mais, que não passa da quantidade | É aceite, sem mensagem | Diminui as unidades pedidas | Aumentam as unidades pedidas |
   | Não é um número inteiro | `ValueError`: "As unidades a retirar têm de ser um número inteiro." | Fica igual | Ficam iguais |
   | Um número inteiro menor do que 1 | `ValueError`: "As unidades a retirar têm de ser 1 ou mais." | Fica igual | Ficam iguais |
   | Passa da quantidade | `ValueError` do setter: "A quantidade não pode ser negativa." | Fica igual | Ficam iguais |

   Numa retirada aceite, a quantidade desce o mesmo que as saídas sobem. Por isso, enquanto ninguém adiciona unidades, as duas somam sempre a quantidade com que o artigo começou. Retirar 2 unidades de A10 e depois 1 leva-o de 6 e 0 a 4 e 2, e depois a 3 e 3, e a soma é sempre 6. É a regra da soma, que te vai servir para confirmar os resultados.

   No comentário do fim do `inventario.py`, escreve o plano do `retirar` do artigo, um passo por linha. Depois de cada passo, escreve dois pontos e o que já mudou no artigo se o pedido for recusado nesse passo. Num passo que não pode recusar, escreve "aqui não há recusa", e porquê. Os dois primeiros passos estão feitos; acrescenta os que faltam, pela ordem em que acontecem:

   | Passo do `retirar` do artigo | O que já mudou no artigo, se o pedido for recusado neste passo |
   | --- | --- |
   | Verificar se as unidades são um número inteiro | Nada |
   | Verificar se as unidades são 1 ou mais | Nada |
   | ? | ? |
   | ? | ? |

2. Escreve da mesma maneira o plano do `retirar` do inventário, desta vez sem nenhum passo feito. Um código que não existe é recusado pelo inventário, no `_procurar`, com "Não existe nenhum artigo com o código ...", e então nenhum artigo muda.

   Guarda e executa outra vez: devem continuar a aparecer as oito linhas da fase 1. Uma mensagem de erro numa linha do plano quer dizer, outra vez, que falta um `#`.

### Paragem 3

Mostra ao professor antes de leres a resposta: os planos dos dois métodos.

O plano do `retirar` do artigo:

| Passo do `retirar` do artigo | O que já mudou no artigo, se o pedido for recusado neste passo |
| --- | --- |
| Verificar se as unidades são um número inteiro | Nada |
| Verificar se as unidades são 1 ou mais | Nada |
| Escrever a nova quantidade pela propriedade; o setter recusa-a se ficar negativa | Nada: o setter recusa antes de guardar |
| Aumentar as saídas nas unidades retiradas | Aqui não há recusa: só se chega a este passo se o setter aceitou |

O plano do `retirar` do inventário:

| Passo do `retirar` do inventário | O que já mudou, se o pedido for recusado neste passo |
| --- | --- |
| Encontrar o artigo com este código | Nada: se o código não existir, `_procurar` recusa, e nenhum artigo foi contactado |
| Passar o pedido ao artigo | Nada no inventário: se o artigo recusar, a recusa é dele, e pelo plano do artigo ele não mudou |

A decisão desta fase é a ordem dos passos do artigo. As duas alterações ficam depois das verificações, e a da quantidade vem antes da das saídas, porque escrever a quantidade ainda é uma verificação: o setter pode recusá-la.

Pensa antes de continuares: se o passo das saídas viesse antes do da quantidade, o que mostraria o fim do programa para A10? A resposta: no pedido de 5, as saídas passavam de 4 a 9, e logo a seguir o setter recusava a quantidade. O `raise` do setter não desfaz o que foi feito antes dele, e A10 ficava com 2 unidades e 9 saídas. A soma dava 11, e não 6: é assim que a regra da soma apanha uma saída contada a mais.

## Fase 4: Os dois métodos, e a sequência do programa

Passas os dois planos para Python, no lugar das linhas "Por completar", e prevês o que o programa principal vai mostrar, pedido a pedido. Como cada pedido encontra o estado que o anterior deixou, a previsão faz-se como um traço. Rever: [Os dois métodos, e a sequência do programa](../06-sintese.md#os-dois-métodos-e-a-sequência-do-programa) e [O inventário passa os pedidos aos artigos](../04-composicao-modelacao.md#o-inventário-passa-os-pedidos-aos-artigos).

1. No método `retirar` da classe `Inventario`, apaga a linha do comentário "Por completar" e a linha do `pass`. No lugar delas, escreve o código de cada passo do teu plano, com oito espaços no início, alinhado com a docstring. O método `saidas_de`, logo acima, já encontra um artigo pelo código, com `self._procurar(codigo)`, e faz uma coisa com ele. Quando passares o pedido ao artigo, lembra-te de que o `retirar` dele recebe só as unidades.

2. No método `retirar` da classe `Artigo`, faz o mesmo, pela ordem do teu plano. As duas verificações escrevem-se como as do `adicionar`, logo acima, com as mensagens do contrato da fase 3. A quantidade escreve-se pela propriedade, `self.quantidade = ...`, para passar pelo setter, e as saídas no atributo interno, `self._saidas = ...`, porque a propriedade `saidas` não tem setter.

3. Antes de executares, prevê de cabeça a resposta a cada pedido e o estado dos dois artigos depois dele. Cada linha começa no estado deixado pela de cima:

   | Momento | Resposta | A10: quantidade e saídas | A11: quantidade e saídas |
   | --- | --- | --- | --- |
   | Início | Não há pedido | 6 e 0 | 3 e 0 |
   | Depois de pedir 4 a A10 | ? | ? | ? |
   | Depois de pedir 5 a A10 | ? | ? | ? |

4. Guarda e executa o ficheiro inteiro. Se aparecer uma mensagem de erro, lê primeiro a última linha, que diz o tipo de erro, e procura esse tipo em [Se alguma coisa falhar](#se-alguma-coisa-falhar). Quando o programa correr até ao fim, mostra oito linhas, como na fase 1, e a quinta diz o que aconteceu ao pedido de 5.

5. Compara o ecrã com a tua previsão, linha a linha, e confirma a regra da soma: a quantidade e as saídas de A10 continuam a somar 6? Se a previsão e o ecrã forem diferentes, descobre primeiro qual dos dois está errado, e escreve porquê no comentário do fim do ficheiro. Se for o programa, corrige-o e volta a executar o ficheiro inteiro.

### Paragem 4

Mostra ao professor antes de leres a resposta: o que o programa mostra e, se alguma previsão foi diferente do ecrã, a explicação da diferença, no comentário do fim.

O que deves ver:

```text
Início
A10: quantidade 6 e saídas 0
A11: quantidade 3 e saídas 0
Retirar 4 de A10: aceite
Retirar 5 de A10: recusado: A quantidade não pode ser negativa.
Fim
A10: quantidade 2 e saídas 4
A11: quantidade 3 e saídas 0
```

A resposta à previsão:

| Momento | Resposta | A10 | A11 |
| --- | --- | --- | --- |
| Início | Não há pedido | 6 e 0 | 3 e 0 |
| Depois de pedir 4 a A10 | Aceite | 2 e 4 | 3 e 0 |
| Depois de pedir 5 a A10 | Recusado pelo setter: "A quantidade não pode ser negativa." | 2 e 4 | 3 e 0 |

A soma de A10 é 6 nas três linhas, e a coluna de A11 mostra que o outro artigo não foi tocado.

O ficheiro `inventario.py` completo, sem o comentário do fim. O teu deve estar igual, com os dois comentários do `retirar` do artigo, que podes copiar daqui:

```python
"""Laboratório do tema 06: o inventário de uma sala, com as saídas de cada artigo.

No programa inicial, as duas partes da operação de retirada, a do inventário
e a do artigo, estão por completar, nas linhas que dizem "Por completar".
Nessa versão, o programa executa do princípio ao fim sem mensagens de erro,
mas não faz o que o problema pede. Todo o resto já está preparado e não muda.
"""


class Artigo:
    """Artigo do inventário: código, nome, uma quantidade sempre válida e as saídas.

    A quantidade é uma propriedade com getter e setter, como no tema 03.
    As saídas contam quantas unidades já saíram por retiradas aceites.
    São uma propriedade só com getter: o código de fora pode consultá-las,
    mas não as pode alterar pela propriedade. O atributo interno _saidas
    continua acessível, mas o sublinhado avisa que não se mexe nele de fora.
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

        Não há setter: as saídas mudam-se no atributo interno _saidas,
        dentro dos métodos do próprio artigo.
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
        if not isinstance(unidades, int):
            raise ValueError("As unidades a retirar têm de ser um número inteiro.")
        if unidades <= 0:
            raise ValueError("As unidades a retirar têm de ser 1 ou mais.")
        # A falta de unidades é recusada pelo setter: o resultado seria negativo.
        self.quantidade = self.quantidade - unidades
        # Só se chega aqui se o setter aceitou: a saída conta-se depois da alteração.
        self._saidas = self._saidas + unidades


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
        artigo = self._procurar(codigo)
        artigo.retirar(unidades)


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

Em cima, o `retirar` do `Artigo` verifica o pedido primeiro, e só depois altera a quantidade, pelo setter, e as saídas. Por baixo, o `retirar` do `Inventario` só encontra o artigo pelo código e passa-lhe os pedidos que o programa principal faz.

Pensa antes de continuares: o `retirar` do inventário não tem nenhum `try`. Porque é que não deve apanhar a recusa do artigo? A resposta: quem lança a exceção decide se o pedido é válido, e quem a apanha decide o que fazer com a recusa. O inventário não sabe o que fazer com ela, e o programa principal sabe: mostra a mensagem. Se o inventário a apanhasse, a recusa não chegava ao programa principal, e ele escrevia "aceite" a um pedido recusado.

## Fase 5: Outros casos, cada um num ensaio

Experimentas os casos que o programa principal não experimenta, cada um num ensaio: um código que não existe, um zero, um número decimal e a retirada de todas as unidades. Cada ensaio é uma execução à parte, que começa sempre com A10 em 6 e 0 e A11 em 3 e 0. Rever: [Outros casos, cada um num ensaio](../06-sintese.md#outros-casos-cada-um-num-ensaio).

1. Os ensaios fazem-se noutro ficheiro, para o teu `inventario.py` não mudar. Cria no editor, na pasta `tema-06`, o ficheiro `ensaios.py`, e cola nele todo o `inventario.py`. No `ensaios.py`, deixa as duas classes e as três linhas que criam o inventário e registam os artigos. Substitui por este bloco todas as linhas a partir de `print("Início")`, também as do comentário do fim:

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

   O bloco mostra os dois artigos antes e depois de um só pedido, o da linha `inventario.retirar("A11", 3)`. Sozinho não corre, porque usa as classes e o inventário de cima.

2. Faz os quatro ensaios, um de cada vez. Em cada um, troca o código e as unidades da linha do pedido e executa o ficheiro inteiro, para começares outra vez com os valores iniciais:

   - `retirar("A11", 3)`
   - `retirar("A11", 0)`
   - `retirar("A11", 1.5)`
   - `retirar("A12", 1)`

   Antes de executares cada um, prevê de cabeça se o pedido é aceite ou recusado, quem o recusa, com que mensagem, e como ficam A10 e A11. Depois lê as quatro linhas do estado, as de A10 e as de A11, antes e depois do pedido. Um pedido a A11 não pode mudar A10, e só as linhas de A10 o confirmam.

3. Faz ainda um ensaio com dois pedidos seguidos, sem recomeçar entre eles: retirar 3 unidades de A11 e, logo a seguir, retirar 1. Volta a pôr o pedido `inventario.retirar("A11", 3)`. Depois copia o bloco do `try` e do `except` e cola a cópia logo a seguir ao primeiro, antes da linha `print("Depois")`, com o pedido de 1 unidade. Executa e escreve duas frases num comentário no fim do `ensaios.py`. Uma diz o que a segunda resposta mostra sobre um artigo vazio, e a outra porque é que as saídas de A11 têm o valor que têm.

### Paragem 5

Mostra ao professor antes de leres a resposta: os quatro ensaios, que voltas a executar se ele pedir, e o ensaio dos dois pedidos seguidos, com as duas frases.

Os quatro ensaios, todos começados com A10 em 6 e 0 e A11 em 3 e 0:

| Pedido | Aceite ou recusado, e quem recusa | Mensagem | A10 depois | A11 depois |
| --- | --- | --- | --- | --- |
| `retirar("A11", 3)` | Aceite | Pedido aceite | 6 e 0 | 0 e 3 |
| `retirar("A11", 0)` | Recusado pelo método `retirar` do artigo | As unidades a retirar têm de ser 1 ou mais. | 6 e 0 | 3 e 0 |
| `retirar("A11", 1.5)` | Recusado pelo método `retirar` do artigo | As unidades a retirar têm de ser um número inteiro. | 6 e 0 | 3 e 0 |
| `retirar("A12", 1)` | Recusado pelo inventário, no `_procurar` | Não existe nenhum artigo com o código A12. | 6 e 0 | 3 e 0 |

Os dois pedidos seguidos, 3 e depois 1, mostram:

```text
Antes
A10: quantidade 6 e saídas 0
A11: quantidade 3 e saídas 0
Pedido aceite
Pedido recusado: A quantidade não pode ser negativa.
Depois
A10: quantidade 6 e saídas 0
A11: quantidade 0 e saídas 3
```

A primeira frase: um artigo com quantidade 0 é válido, mas não tem nada para retirar, e qualquer pedido de 1 ou mais é recusado. A segunda: as saídas ficam em 3 porque só contam as retiradas aceites, e o pedido de 1 foi recusado antes de as saídas mudarem.

Pensa antes de continuares: 1.5 é mais do que 1. Porque é que o pedido de 1.5 recebe a mensagem do número inteiro, e não é aceite? A resposta: porque 1.5 não é um número inteiro, e o método verifica o tipo antes do valor. A primeira verificação recusa-o, e a segunda nem chega a ser feita.

## Fase 6: Explicar a correção

Escreves, em quatro frases com valores, a explicação da correção que fizeste nos dois métodos `retirar`. Uma correção explica-se assim sempre que um programa falha: o que esperavas, o que viste, a causa e a confirmação de que ficou resolvido. Rever: [Explicar a correção](../06-sintese.md#explicar-a-correção).

1. Volta às respostas da fase 1 e à paragem 1. O pedido de 5 a A10 é um dos que o programa inicial tratava mal: disse "aceite", e devia ter recusado. No comentário do fim do `inventario.py`, escreve as quatro frases para esse pedido, cada uma com valores ou instruções concretas:

   1. "Esperava ...": o que o pedido devia fazer à quantidade e às saídas.
   2. "Observei ...": o que o programa inicial mostrou.
   3. "A instrução que explica a diferença é ...": a linha do programa inicial responsável, e porquê.
   4. "Depois da alteração, confirmei ...": o que o teu programa mostra agora, com os valores.

2. Compara a forma das tuas frases com este exemplo, feito para o outro pedido, o de 4 a A10. "Esperava que, ao retirar 4 de A10, a quantidade passasse de 6 a 2 e as saídas de 0 a 4. Observei no programa inicial a mensagem "aceite", mas A10 continuou com quantidade 6 e saídas 0. A instrução que explica a diferença é o `pass` dos dois métodos `retirar`: não muda nenhum dado e também não lança nenhuma exceção. Por isso o programa principal escreveu "aceite" sem nada ter mudado. Depois da alteração, confirmei que o mesmo pedido deixa A10 com quantidade 2 e saídas 4, e que o pedido de 5 a seguir é recusado sem mudar esses valores." Cada frase tem valores ou instruções concretas, e quem a lê pode repetir o caso para a confirmar. Uma explicação que diga só "o método não funcionava e agora funciona" ainda não explica nada.

### Paragem 6

No fim, o professor conversa contigo durante uns minutos, com o teu programa aberto. A conversa não dá nota: serve para tu e o professor perceberem o que já está firme e o que precisa de mais prática.

Não há nada para decorar, porque as respostas estão no que fizeste: usa o teu programa e os valores. O professor escolhe uma ou duas destas tarefas:

- mostrar, no teu código, onde o pedido é encaminhado e onde é decidido (fases 3 e 4);
- explicar porque é que uma recusa não pode alterar nem a quantidade nem as saídas, apontando a linha do teu código que o garante (fases 3 e 4);
- dizer que outra forma havia de recusar a falta de unidades, e qual escolherias, e porquê (fase 3, e o [passo 4 do exemplo guiado do guia 03](../03-encapsulamento-contratos.md#passo-4-alterar-através-da-propriedade));
- mostrar como confirmaste que A10 não mudou nos ensaios feitos com A11 (fase 5);
- prever o resultado de um pedido com outros valores, escolhido pelo professor, antes de o executares (fases 4 e 5);
- encontrar e corrigir um erro que o professor ponha numa cópia do teu programa (fase 6). Segues a rotina de sempre: reproduzes o erro com um caso e dizes que tipo de erro é. Escreves uma hipótese num comentário no fim da cópia e confirma-la com os valores, e depois corriges a causa e voltas a correr tudo.

## Se alguma coisa falhar

1. Guardaste o ficheiro antes de executar? O editor executa o que está guardado: se a saída não mudou depois de uma alteração, guarda e executa outra vez.
2. Estás a executar o ficheiro certo? É o `inventario.py`, o `ensaios.py`, na fase 5, ou o `desafios.py`, nos desafios, todos na pasta `tema-06`.
3. Executaste o ficheiro inteiro? Cada execução começa do zero: cria um inventário novo, regista os dois artigos com os valores iniciais e faz os pedidos pela ordem em que estão escritos.
4. Perdeste-te? Até à fase 4, copia outra vez as três partes de [Preparar o projeto](#preparar-o-projeto) e cola por baixo o teu comentário. Na fase 5 e seguintes, parte do ficheiro da [paragem 4](#paragem-4).
5. Apareceu uma mensagem de erro? Lê primeiro a última linha, que diz o tipo de erro. Por cima dela, cada linha `File` diz uma linha do ficheiro onde o Python estava, com o código dessa linha por baixo. A de baixo é onde o erro aconteceu, e a de cima, que acaba em `in <module>`, é a do programa principal, que fez o pedido. Procura o tipo de erro nos títulos de baixo.

### Aparece `IndentationError`, `TabError` ou `SyntaxError`

É um erro de escrita: o Python recusa o ficheiro antes de correr qualquer linha, e por isso a mensagem não começa por `Traceback`. Abre com o nome do ficheiro e o número da linha onde a leitura parou. Neste laboratório, as mais prováveis são estas:

- `IndentationError: unindent does not match any outer indentation level`: uma linha de um dos teus métodos ficou com uma margem diferente das outras, como seis espaços em vez de oito.
- `IndentationError: expected an indented block after class definition on line 76` (no Python 3.9, só `expected an indented block`): a linha `class Inventario:` ficou com espaços à frente. A mensagem aponta a docstring, por baixo, mas o engano está na linha da classe. Encosta-a à margem.
- `IndentationError: unexpected indent` ("indentação inesperada"): uma linha tem espaços a mais à frente, como doze em vez de oito, sem estar dentro de um `if`.
- `TabError: inconsistent use of tabs and spaces in indentation`: uma tabulação ficou no meio dos espaços da margem. Apaga-a e escreve os espaços.
- `SyntaxError: expected ':'` (no Python 3.9, só `invalid syntax`): um `if` ficou sem os dois pontos no fim.
- `SyntaxError: invalid syntax` numa linha de português depois do programa principal, ou `IndentationError: unexpected indent`, se essa linha começar por espaços: a linha do teu comentário ficou sem o `#` no início. O Python tentou lê-la como código. Põe-lhe o `#`.

Dentro de um método, as linhas ficam a oito espaços da margem, alinhadas com a docstring, e as que estão dentro de um `if` ficam a doze. O `adicionar` do artigo tem a mesma forma do teu `retirar`: compara a margem da linha que a mensagem indica com a das linhas dele.

### Aparece `NameError: name '_procurar' is not defined`

`NameError` quer dizer erro de nome: o Python não conhece o nome `_procurar`. No `retirar` do inventário, a chamada ficou escrita sem o `self.` à frente, e o Python procura uma função solta com esse nome. Nas versões mais recentes, como a 3.14, a mensagem acaba com a sugestão `Did you mean: 'self._procurar'?`, que quer dizer "querias dizer `self._procurar`?". No 3.9, não traz nenhuma. Escreve `self._procurar(codigo)`, como no `saidas_de`.

### Aparece `TypeError: Artigo.retirar() takes 2 positional arguments but 3 were given`

`TypeError` quer dizer erro de tipo, e aqui diz que a chamada não bate com o `def`: o `retirar` do artigo aceita 2 valores e recebeu 3. No Python 3.9, a mensagem não tem o `Artigo.` antes do `retirar()`. No inventário, a chamada ao artigo ficou com o código e as unidades, como `artigo.retirar(codigo, unidades)`, e o artigo só recebe as unidades. O Python conta também o `self`, e por isso diz 2 e 3. Escreve `artigo.retirar(unidades)`.

### Aparece `TypeError: Inventario.retirar() missing 1 required positional argument: 'unidades'`

Quem se queixa é o `retirar` do inventário, que precisa de dois valores, o código e as unidades, e só recebeu um. No Python 3.9, falta o `Inventario.` no início da mensagem. A linha `File` de baixo mostra a linha do teu `retirar` do inventário onde o pedido é passado. Lê-a ao lado do teu plano da fase 3: a quem é que esse passo passa o pedido? Se escreveste o `self.` porque o Python 3.14 o sugeriu, num `NameError: name 'retirar' is not defined`, a sugestão não serve aqui: volta à pergunta de cima.

### Aparece `AttributeError: property 'saidas' of 'Artigo' object has no setter`

`AttributeError` quer dizer erro de atributo. Antes do Python 3.11, a mensagem começa por `AttributeError: can't set attribute`, "não se pode escrever o atributo". O teu `retirar` do artigo escreve nas saídas pela propriedade, com `self.saidas = ...`, e a propriedade não tem setter. Dentro do artigo, as saídas mudam-se no atributo interno: `self._saidas = self._saidas + unidades`.

### Aparece `TypeError: '<=' not supported between instances of 'str' and 'int'`

A comparação `<=` não se pode fazer entre um texto e um número inteiro (`str` é o texto e `int` o inteiro). Aparece num pedido com um texto, como `"2"`, quando o teu método compara as unidades com um número antes de verificar se são um número inteiro. Se usaste outro sinal, como `<`, a mensagem mostra esse sinal. Verifica primeiro o tipo, com o `isinstance`, e só depois o valor, como no setter e no `adicionar`.

### O programa diz "aceite", mas a quantidade e as saídas não mudaram

Um dos métodos `retirar` ainda não faz nada: ficou só com o `pass`, ou o inventário encontra o artigo e não lhe passa o pedido. Segue o pedido desde o programa principal até ao método do artigo, e confirma que cada passo chama o seguinte.

### Num ensaio, o programa para com `ValueError`, em vez de mostrar "Pedido recusado"

A linha do pedido ficou fora do `try`. A mensagem mostra o caminho do pedido, uma linha `File` por método, do programa principal até ao sítio onde a recusa nasceu. Pode ser o `retirar` do artigo, o setter, que aparece como `in quantidade`, ou o `_procurar`. Põe a linha do pedido dentro do `try`, com quatro espaços à frente, como no bloco da fase 5.

## Desafios

Os desafios fazem-se numa cópia, para o `ensaios.py` ficar como na paragem 5. Cria no editor, na pasta `tema-06`, o ficheiro `desafios.py`, e cola nele todo o `ensaios.py`. Faz os três desafios nesse ficheiro, pela ordem, com as respostas num comentário no fim dele.

1. Os ensaios que faltam. Apaga o segundo bloco do `try` e do `except`, para ficar um só pedido, como nos quatro ensaios da fase 5, e ensaia `retirar("A11", -1)` e `retirar("A11", "2")`, um de cada vez. Antes de cada um, prevê se o pedido é aceite ou recusado, quem o recusa, a mensagem e o estado dos dois artigos depois. Depois de executares, escreve no comentário do fim que linha do teu método recusou cada um. Pista: segue o teu método pela ordem das linhas, com o valor do pedido.

2. Um terceiro artigo. Regista um terceiro artigo, A12, Tesoura, com 4 unidades, a seguir aos registos de A10 e A11, e acrescenta uma linha que mostre A12 no "Antes" e outra no "Depois". No lugar do pedido, faz três pedidos seguidos a A12, cada um no seu `try`: retirar 1, depois 2, depois 2. Antes de executares, prevê a resposta a cada pedido, a quantidade e as saídas de A12 depois de cada um, e a soma das duas. Confirma, no fim, que A10 e A11 não mudaram. Pista: cada pedido parte do estado deixado pelo anterior, e a soma diz-te se contaste bem as saídas.

3. A outra forma de recusar. Muda o `retirar` do artigo para ser ele, e não o setter, a recusar um pedido que passa da quantidade, com a mensagem "Não há unidades suficientes.". A recusa tem de vir antes de qualquer alteração. Executa outra vez o `desafios.py`, com os três pedidos a A12. Depois troca esses três blocos por um só pedido a A11, e repete o -1 e o `"2"` do desafio 1. Responde no comentário do fim: que respostas mudam, e quais ficam iguais? Porquê? A soma de A12 continua certa? E, em duas frases, qual das duas formas preferes, e porquê? Pista: procura os pedidos que passam da quantidade.

## Antes de terminares

- [ ] O `inventario.py` executa e mostra as oito linhas da paragem 4.
- [ ] O comentário do fim do `inventario.py` tem o modelo, o estado dos dois artigos e as três respostas da fase 2. Tem também os dois planos da fase 3 e as quatro frases da fase 6.
- [ ] O `ensaios.py` tem o bloco da fase 5, fizeste com ele os quatro ensaios e os dois pedidos seguidos, e o comentário do fim tem as duas frases.
- [ ] Entregaste a pasta `tema-06` pelo meio que o professor indicar, com o `desafios.py`, se fizeste os desafios.
- [ ] Sabes dizer, para cada pedido da fase 5, quem o recusa e porquê.
- [ ] Consegues explicar, por palavras tuas, porque é que uma recusa não muda nem a quantidade nem as saídas, e que linha do teu código o garante.

![Rodapé](../../imagens/rodape.png)

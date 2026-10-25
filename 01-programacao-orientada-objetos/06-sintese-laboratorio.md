![Cabeçalho](../imagens/cabecalho.png)

# Laboratório: Síntese

Laboratório do tema Síntese, do módulo M10, Introdução à Programação Orientada por Objetos. Vais completar a retirada de material num pequeno inventário em Python, e explicar o que fizeste. É o laboratório que fecha o módulo, e faz-se na aula, com o professor a acompanhar. Cada passo diz o que fazer, porquê e o que deves ver, e avanças ao teu ritmo. O que não acabares na aula, acabas na aula seguinte. Tudo o que precisas está aqui; o [guia do tema](06-sintese.md) tem a teoria completa, para quem quiser saber mais.

## O que vais construir

Vais trabalhar com um pequeno programa em Python que acompanha os materiais de uma sala. O programa já conhece dois artigos e já sabe registá-los. Também já sabe consultar a quantidade de cada um e as suas saídas, mas ainda não sabe retirar unidades. Primeiro explicas como os dados estão organizados. Depois completas a operação que falta, verificas os resultados com casos escolhidos e explicas a correção que fizeste. No fim, mostras o teu trabalho ao professor numa conversa curta.

No fim do laboratório tens:

- uma pasta `tema-06` com dois ficheiros: o `inventario.py`, com a retirada completa nas duas classes, e o `ensaios.py`, com os casos que experimentaste;
- uma folha com o modelo do programa, o plano dos dois métodos, as tabelas de previsão e as frases que explicam a correção.

### O problema: os artigos e as suas saídas

| Código | Nome | Quantidade inicial | Saídas iniciais |
| --- | --- | ---: | ---: |
| A10 | Régua | 6 | 0 |
| A11 | Cola | 3 | 0 |

Cada linha representa um artigo. Os códigos são diferentes, os nomes estão preenchidos e as quantidades são válidas. Estes dados já vêm escritos no programa: não precisas de criar outros artigos nem de os pedir a quem usa o programa.

Há uma informação nova em relação aos temas anteriores. A equipa que usa o programa quer saber quantas unidades de cada artigo já saíram da sala desde que o programa começou, para perceber que materiais se gastam mais. Por isso, cada artigo guarda, além da quantidade, as suas **saídas**: o total de unidades que já saíram por retiradas aceites. Um artigo acabado de criar tem zero saídas. As saídas obedecem a três regras:

- uma retirada aceite aumenta as saídas no número de unidades retiradas, ao mesmo tempo que diminui a quantidade;
- uma retirada recusada não muda nada: nem a quantidade, nem as saídas;
- adicionar unidades é uma entrada de material, e não uma saída, por isso não muda as saídas.

Por exemplo, se a um artigo com 6 unidades e 0 saídas forem retiradas 2 unidades e depois 1, fica com 3 unidades e 3 saídas. Se a seguir for recusado um pedido de 9, continua com 3 unidades e 3 saídas.

Repara que, enquanto ninguém adicionar unidades, a quantidade e as saídas de um artigo somam sempre o mesmo: a quantidade com que ele começou. No exemplo, 6 e 0, depois 4 e 2, depois 3 e 3: a soma é sempre 6. Chama-se **invariante** a uma regra que tem de continuar verdadeira depois de cada operação, como a regra da quantidade, que nunca pode ser negativa. A regra da soma não é uma invariante, porque uma adição a muda; mas neste laboratório ninguém adiciona, e por isso serve para verificar os teus resultados. Se a soma mudar sem nenhuma adição, há uma saída contada a mais ou a menos.

### As fases

| Fase | O que fazes | O que tens no fim |
| --- | --- | --- |
| 1 | Executas o programa inicial e lês o que ele mostra | Sabes dizer que tipo de erro tem o programa |
| 2 | Descreves por palavras, no papel, o modelo do programa | A descrição das duas classes e da relação entre elas, e o estado dos dois artigos, confirmados pelo professor |
| 3 | Escreves por palavras o plano dos dois métodos `retirar` | O plano, confirmado pelo professor |
| 4 | Completas os dois métodos e comparas o programa com a tua previsão | O programa principal aceita o pedido de 4 e recusa o de 5 |
| 5 | Crias o `ensaios.py` e experimentas outros casos | Os quatro ensaios e os dois pedidos seguidos, confirmados pelo professor |
| 6 | Explicas a correção, com valores | As quatro frases, e a conversa com o professor |

### Como trabalhas com o professor

O professor acompanha o laboratório do princípio ao fim. Podes trabalhar sozinho ou em par, como ele indicar. Em par, os dois têm de conseguir explicar tudo o que está escrito, porque o professor pode fazer a pergunta a qualquer um.

Algumas paragens começam pela frase "Mostra ao professor antes de leres a resposta". Quer dizer o que diz: chamas o professor e mostras o que fizeste. Só depois de ele o confirmar lês a resposta do laboratório e passas à fase seguinte. Há uma razão para isto. Cada fase usa a anterior: um modelo mal percebido leva a escrever uma regra no objeto errado, e uma previsão errada faz-te procurar um erro onde ele não está. Se o professor encontrar alguma coisa a corrigir, não te dá a resposta. Faz-te uma pergunta, ou aponta para uma linha do teu código ou da tua tabela, e tu corriges e voltas a mostrar. Enquanto esperas, lê a explicação do início da fase seguinte.

Este laboratório não tem nota. É prática guiada: serve para juntares as ideias do módulo com ajuda, antes de as usares sozinho no projeto. Pedir ajuda faz parte do trabalho, e o professor está lá para isso.

Em todas as fases trabalhas da mesma maneira. Antes de executares, escreves no papel o que esperas ver. Depois executas e comparas. Quando o resultado é diferente do que previste, procura a explicação antes de continuares: é essa explicação que mais te ensina. Se a previsão estiver errada, não a apagues para ficar igual ao ecrã. Escreve ao lado o que estava errado e porquê.

## Palavras que vais usar

- Classe e objeto: a classe é a descrição comum, como `Artigo`, que diz que dados e que operações cada artigo tem. Cada artigo concreto é um objeto, também chamado instância, da classe. Para saber mais, vê "Classes e objetos no programa" no [guia](06-sintese.md).
- Atributo e estado: um atributo é um dado guardado num objeto, como o código ou a quantidade. O estado é o conjunto dos valores dos atributos num dado momento.
- Construtor e `self`: o construtor, `__init__`, prepara cada objeto quando ele nasce. Dentro de um método, `self` é o objeto sobre o qual o método está a trabalhar: em `artigo.retirar(4)`, é o objeto `artigo`.
- Propriedade, getter e setter: a `quantidade` de um artigo lê-se e escreve-se como um atributo. Cada leitura passa por um método, o getter (do inglês *get*, obter). Cada escrita passa por outro, o setter (de *set*, pôr), que recusa os valores inválidos.
- Atributo interno: um atributo com um sublinhado no início do nome, como `_quantidade` ou `_saidas`. Avisa que só a própria classe o deve usar.
- Exceção: um sinal de que alguma coisa correu mal, que interrompe o funcionamento normal do programa. `raise` lança uma exceção, e para o método nessa linha. `ValueError` ("erro de valor") é a exceção que usamos para recusar um valor ou um pedido. `try` e `except` apanham-na, para o programa continuar.
- Contrato: o que uma operação recebe, o que devolve, quando falha e o que acontece aos dados em cada caso.
- Encaminhamento: o inventário recebe um pedido, encontra o artigo que sabe cumpri-lo e passa-lho, sem verificar nada sobre as unidades.
- Composição: a relação "tem" em que o todo cria as suas partes e as guarda, e as partes não fazem sentido sem ele.
- Agregação: a relação "tem" em que o todo recebe partes já criadas fora dele, que existem sem ele, como as músicas de uma playlist.
- Modelo: a descrição por palavras das classes de um programa e das relações entre elas. Diz o que cada objeto guarda, com que valores se cria e o que se lhe pode pedir.
- Saídas: o total de unidades de um artigo que já saíram da sala por retiradas aceites.
- Invariante: uma regra que tem de continuar verdadeira depois de cada operação, como a regra da quantidade, que nunca pode ser negativa.
- Traço: a tabela que regista, pedido a pedido, o que acontece e como fica o estado depois. Faz-se no papel, antes de executar.
- `pass`: a instrução que não faz nada (do inglês, "passa"). Marca o sítio onde vai entrar código.
- Programa principal: as linhas encostadas à margem, no fim do ficheiro, fora das classes. São elas que dizem o que o programa faz.
- Erro de escrita, de execução e de lógica: no de escrita, o Python recusa o ficheiro antes de começar. O de execução para o programa a meio. No de lógica, o programa corre até ao fim e faz uma coisa diferente da que devia.
- Mensagem de erro: o texto que o Python mostra quando para por causa de um erro. Quando o erro acontece com o programa a correr, a primeira linha é `Traceback (most recent call last)`, "o rasto, com a chamada mais recente no fim". A última linha diz o tipo de erro e o que aconteceu.

## O que precisas

- O editor de Python que usas nas aulas, para escrever e executar os programas. Confirma que funciona: num ficheiro de ensaio, escreve `print("Olá")` e executa. Deve aparecer `Olá`, o que quer dizer que o editor está a executar programas de Python.
- O Python 3, a partir da versão 3.10. Nas versões mais antigas, algumas mensagens de erro são um pouco diferentes, e o laboratório diz onde.
- Papel e caneta, para o modelo, as previsões, o plano e as respostas.

O laboratório começa de uma pasta vazia. Não precisas de nenhum ficheiro de outro laboratório: o programa inicial está todo aqui.

Um programa de Python é um ficheiro de texto com a extensão `.py`. Executar o programa é pedir ao Python que siga as instruções do ficheiro, de cima para baixo. Executa sempre o ficheiro inteiro. Cada execução começa do zero: cria um inventário novo, regista os dois artigos com os valores iniciais e repete todos os pedidos, pela ordem em que estão escritos.

## Se alguma coisa falhar

1. Guardaste o ficheiro antes de executar? O editor executa o que está guardado no disco. Guarda e executa outra vez.
2. Estás a executar o ficheiro certo? Confirma que o separador aberto é o `inventario.py`, ou o `ensaios.py` na fase 5, da pasta `tema-06`.
3. Apareceu uma mensagem de erro? Lê primeiro a última linha, que diz o tipo de erro e o que aconteceu. Depois lê as de cima, que dizem onde aconteceu. Procura essa última linha em [Problemas frequentes](#problemas-frequentes).
4. Perdeste-te? Até à fase 4, copia outra vez o programa inicial de "Preparar o projeto". Na fase 5 e seguintes, parte do ficheiro completo da [paragem 4](#paragem-4).

## Preparar o projeto

1. Na pasta onde guardas os trabalhos de LP, cria uma pasta nova chamada `tema-06`. Dentro dela, cria um ficheiro novo chamado `inventario.py`. O nome tem de acabar em `.py`, para o editor o reconhecer como um programa de Python, e não deve ter espaços nem acentos.
2. Copia para `inventario.py` o programa inicial completo, desde a primeira linha até à última, a que mostra a quantidade e as saídas de A11 no fim. É o ficheiro completo:

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

   Leitura guiada: o texto entre três aspas no início é a docstring do ficheiro, que diz para que serve o programa. Na classe `Artigo`, a quantidade é uma propriedade. O `@property` faz do primeiro `def quantidade` o getter, e o `@quantidade.setter` faz do segundo o setter, que verifica o valor antes de o guardar. As saídas são diferentes. Têm o `@property` e o getter, mas não têm setter: o código de fora consulta-as com `artigo.saidas`, mas não as pode alterar pela propriedade (`artigo.saidas = 5` dá `AttributeError`). O valor vive no atributo interno `_saidas`, que o construtor põe a zero. Esse atributo continua acessível, mas o sublinhado avisa que não se mexe nele de fora. A classe `Inventario` cria os artigos em `registar` e encontra-os pelo código em `_procurar`. Os métodos `quantidade_de` e `saidas_de` encontram um artigo e devolvem um dado dele. Os dois métodos `retirar`, um em cada classe, só têm um comentário e a instrução `pass`, que não faz nada. São eles que vais completar.

3. Guarda o ficheiro. Antes de o executares, lê-o por zonas, porque um programa com mais de cem linhas não se lê de cima para baixo na primeira vez. Começa pelo programa principal, as linhas encostadas à margem no fim do ficheiro. Cria um inventário, regista os dois artigos, mostra o início, faz dois pedidos de retirada a A10 e mostra o fim. Depois procura, na classe `Inventario`, os métodos que o programa principal chama. Só depois desce à classe `Artigo`. Procura as duas linhas que dizem "Por completar": estão no método `retirar` do inventário e no método `retirar` do artigo.

## Fase 1: Um programa que corre e não faz o que devia

Um programa pode estar errado de três maneiras. Num erro de escrita, o Python recusa o ficheiro antes de começar: falta um parêntese, faltam os dois pontos no fim de um `def`, ou uma linha está mal indentada. Num erro de execução, o programa para a meio, com uma mensagem que começa por `Traceback`. Num erro de lógica, o programa corre do princípio ao fim, sem nenhuma mensagem, e faz uma coisa diferente da que o problema pede. O erro de lógica é o mais traiçoeiro, porque o Python não avisa de nada. Só o apanhas se souberes antes o que o programa devia mostrar. Para saber mais, lê "Um programa que corre sem erros e não faz o que devia", no [guia](06-sintese.md).

1. Antes de executares, prevê e escreve no papel. O programa vai parar com uma mensagem de erro, ou vai correr até ao fim? O que diz sobre os dois pedidos? Que quantidade e que saídas mostra para A10 no fim?

2. Executa o ficheiro inteiro. O que deves ver:

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

   A resposta à previsão: o programa corre até ao fim, sem nenhuma mensagem de erro. Os dois métodos `retirar` só têm o `pass`, que não faz nada e não lança nada. Por isso nenhum pedido salta para o `except`, e o programa principal escreve "aceite" nos dois. No fim, A10 continua com quantidade 6 e saídas 0. Se o programa parar com uma mensagem de erro, a cópia ficou com algum engano: compara-a com o bloco de "Preparar o projeto" e vê os [problemas frequentes](#problemas-frequentes).

3. Responde por escrito, a olhar para o ecrã. Cada pergunta tem a resposta logo a seguir; escreve a tua antes de a leres.

   1. O pedido para retirar 4 unidades de A10 devia ser aceite, tendo em conta os dados iniciais? Porquê?

      A resposta: sim. 4 é um número inteiro, é 1 ou mais, e não ultrapassa as 6 unidades de A10.

   2. O que diz o programa sobre esse pedido?

      A resposta: diz "aceite". Mas repara de onde vem essa palavra. O programa principal escreve "aceite" sempre que o `try` chega ao fim sem exceção. Como o `pass` não lança nada, a mensagem não prova que o pedido foi cumprido.

   3. Que quantidade e que saídas ficaram guardadas em A10 no fim?

      A resposta: quantidade 6 e saídas 0. Nada mudou.

   4. Que tipo de erro tem o programa: de escrita, de execução ou de lógica? Explica a diferença numa frase.

      A resposta: de lógica. O programa corre do princípio ao fim sem nenhuma mensagem do Python, mas não faz o que o problema pede. Um erro de escrita impedia-o de começar, e um erro de execução parava-o a meio.

4. Guarda estas respostas: vais precisar delas na fase 6, para as comparares com o programa corrigido.

### Paragem 1

O programa corre sem nenhuma mensagem de erro, diz "aceite" aos dois pedidos e não muda nada.

Pensa antes de continuares: o pedido de 5 também aparece como "aceite". Depois de aceite o de 4, devia ser aceite? A resposta: não. Depois de retirar 4, A10 ficaria com 2 unidades, e 5 é mais do que 2. Com os métodos completos, este pedido vai ser recusado.

## Fase 2: O modelo antes do código

Antes de mexeres no código, vais descrever por palavras como os dados estão organizados. Um modelo mal percebido leva a escrever uma regra no objeto errado. Uma descrição escrita mostra o modelo sem teres de ler o programa linha a linha, e permite discuti-lo com o professor antes de escreveres código.

O modelo de um programa é a descrição das suas classes e das relações entre elas. A descrição de cada classe tem três partes. A primeira diz o que cada objeto guarda, e corresponde aos atributos. A segunda diz com que valores se cria um objeto, e corresponde aos parâmetros do construtor. A terceira diz o que se pode pedir a cada objeto, e corresponde aos métodos, com os parâmetros entre parênteses.

A descrição mostra a interface pública da classe, aquilo que quem a usa vê e pode pedir. Por isso não se escreve o `self`, nem o `__init__`, nem os nomes internos com sublinhado: fala-se da quantidade, e não de `_quantidade`. A lista `_artigos` do inventário também não se escreve. A descrição diz só que o inventário guarda os seus artigos, porque a lista é a forma como o programa os guarda. E a descrição de uma classe vale para todos os objetos dela, e por isso não leva valores.

A relação entre duas classes descreve-se com a frase que as liga, "tem" ou "é um". Numa relação "tem", diz-se também o grau, composição ou agregação, e as razões que o justificam. As razões respondem a quatro perguntas: a parte faz sentido sem o todo? Quem cria a parte? A parte pode estar em dois todos ao mesmo tempo? O que lhe acontece se o todo desaparecer? Numa composição, o todo cria as suas partes e guarda-as, e as partes não fazem sentido sem ele.

Este é o modelo do inventário do tema 04, que ainda não tinha as saídas. Primeiro, a descrição da classe `Artigo`:

- Cada artigo guarda um código, um nome e uma quantidade, que é sempre um número inteiro não negativo.
- Um artigo cria-se com o código, o nome e a quantidade inicial.
- A um artigo pode pedir-se que adicione unidades, com `adicionar(unidades)`, e que retire unidades, com `retirar(unidades)`.

Depois, a da classe `Inventario`:

- Cada inventário guarda os seus artigos, e nunca dois com o mesmo código.
- Um inventário cria-se vazio, sem nenhum valor.
- A um inventário pode pedir-se que registe um artigo novo, com `registar(codigo, nome, quantidade)`; que diga a quantidade de um artigo, com `quantidade_de(codigo)`; e que retire unidades de um artigo, com `retirar(codigo, unidades)`.

E por fim a da relação entre as duas:

- Um inventário tem artigos, e é uma composição.
- Um artigo só faz sentido dentro do seu inventário, porque é uma linha do registo.
- É o inventário que cria cada artigo, quando se lhe pede que o registe.
- Cada artigo pertence a um só inventário e desaparece se o inventário desaparecer.

Para falar de um artigo concreto, com os valores, descreve-se o seu estado, numa frase. Os artigos deste programa não têm nome no programa principal: o programa chega a eles pelo inventário e pelo código. Por isso, cada artigo identifica-se pelo código. Este é o estado do caderno A01 do tema 04, acabado de registar:

- O artigo A01 chama-se Caderno e tem 6 unidades.

Para saber mais, lê o passo 8 do exemplo guiado do [guia](06-sintese.md).

1. Numa folha, escreve a descrição das duas classes do teu `inventario.py`. Parte das descrições acima e acrescenta o que este programa tem a mais. Na descrição do artigo, falta o dado que conta as saídas; na do inventário, o pedido que as consulta. Escreve também a descrição da relação entre as duas classes, com a frase que as liga e, se for uma relação "tem", o grau e as razões.

2. Por baixo, escreve o estado dos dois artigos no início do programa, numa frase para cada um, com os valores de cada dado.

3. Por baixo da descrição, responde:

   1. Neste programa, a relação entre `Inventario` e `Artigo` é uma composição ou uma agregação? Justifica com duas perguntas: a parte faz sentido sem o todo? Quem cria a parte? Indica a linha do programa onde os artigos são criados.
   2. Que objeto encontra o artigo a partir do código? Que objeto decide se há unidades suficientes? Que objeto guarda as saídas?
   3. Porque é que faz sentido que a propriedade `saidas` não tenha setter? Pensa no que podia acontecer às saídas se qualquer parte do programa as pudesse escrever.

### Paragem 2

Mostra ao professor antes de leres a resposta: a descrição das duas classes e da relação, o estado dos dois artigos e as três respostas.

A descrição de referência da classe `Artigo`:

- Cada artigo guarda um código, um nome, uma quantidade, que é sempre um número inteiro não negativo, e as saídas, o total de unidades que já saíram por retiradas aceites.
- Um artigo cria-se com o código, o nome e a quantidade inicial, e começa sem nenhuma saída.
- A um artigo pode pedir-se que adicione unidades, com `adicionar(unidades)`, e que retire unidades, com `retirar(unidades)`.

A da classe `Inventario`:

- Cada inventário guarda os seus artigos, e nunca dois com o mesmo código.
- Um inventário cria-se vazio, sem nenhum valor.
- A um inventário pode pedir-se que registe um artigo novo, com `registar(codigo, nome, quantidade)`; que diga a quantidade de um artigo, com `quantidade_de(codigo)`; e que retire unidades de um artigo, com `retirar(codigo, unidades)`. Pode pedir-se-lhe também que diga as saídas de um artigo, com `saidas_de(codigo)`.

A da relação, que é a do tema 04, porque as saídas não mudam quem cria os artigos nem quem os guarda:

- Um inventário tem artigos, e é uma composição.
- Um artigo só faz sentido dentro do seu inventário, porque é uma linha do registo.
- É o inventário que cria cada artigo, quando se lhe pede que o registe.
- Cada artigo pertence a um só inventário e desaparece se o inventário desaparecer.

O estado dos dois artigos no início do programa:

- O artigo A10 chama-se Régua, tem 6 unidades e 0 saídas.
- O artigo A11 chama-se Cola, tem 3 unidades e 0 saídas.

Se escreveste `_quantidade` e `_saidas`, sabe que são os atributos internos onde os valores vivem; a descrição mostra a interface pública, com a quantidade e as saídas. Se identificaste um artigo por um nome, como `regua`, diz ao professor que esse nome não existe no programa: o que identifica cada artigo é o código. Se escreveste valores na descrição de uma classe, tira-os: os valores de um artigo concreto vão só no estado dele.

As respostas:

1. Composição. A linha que cria os artigos é `novo = Artigo(codigo, nome, quantidade)`, dentro do método `registar` do inventário. O programa principal não cria nenhum artigo nem guarda nenhum artigo num nome seu. A parte não faz sentido sem o todo: o artigo é a linha do registo deste inventário. E quem cria a parte é o todo. Repara que a lista, sozinha, não decide nada; o que decide é a linha onde o artigo nasce.
2. O inventário encontra o artigo pelo código, no método interno `_procurar`. O artigo decide se há unidades suficientes, no seu método `retirar` ou no setter da quantidade. O artigo guarda as saídas, no atributo interno `_saidas`.
3. Sem setter, o código de fora não pode alterar as saídas pela propriedade: `artigo.saidas = 5` dá `AttributeError`. O atributo interno `_saidas` continua acessível, mas o sublinhado avisa que não se mexe nele de fora. Assim, as saídas mudam dentro do método `retirar` do artigo, depois das verificações. Se qualquer parte as pudesse escrever, o total podia deixar de corresponder às retiradas aceites, por engano ou com um valor sem sentido, como um negativo. E ninguém saberia onde se tinha estragado.

## Fase 3: O plano da retirada

A operação de retirada tem duas partes, uma em cada classe, e vais completar as duas. Antes de escreveres código, escreves o plano de cada método por palavras.

O método `retirar(codigo, unidades)` do inventário recebe o código de um artigo e as unidades a retirar. Encontra o artigo com esse código e passa-lhe o pedido. Não verifica as unidades: essas regras são do artigo, e já lá estão escritas. A esta forma de colaborar chama-se encaminhamento.

O método `retirar(unidades)` do artigo recebe as unidades a retirar, decide se o pedido é possível e, se for, altera os dados do artigo. Deve cumprir este contrato:

| Situação | O que acontece | Quantidade | Saídas |
| --- | --- | --- | --- |
| As unidades são um número inteiro, 1 ou mais, e não ultrapassam a quantidade | O pedido é aceite e o método termina sem mensagem | Diminui as unidades pedidas | Aumentam as unidades pedidas |
| As unidades não são um número inteiro | `ValueError` com a mensagem "As unidades a retirar têm de ser um número inteiro." | Fica igual | Ficam iguais |
| As unidades são inteiras, mas menores do que 1 | `ValueError` com a mensagem "As unidades a retirar têm de ser 1 ou mais." | Fica igual | Ficam iguais |
| As unidades ultrapassam a quantidade | `ValueError` | Fica igual | Ficam iguais |

No último caso, há duas formas de recusar, e as duas cumprem o contrato. Podes deixar a recusa ao setter da quantidade, como no tema 03. A nova quantidade seria negativa, e o setter recusa-a com a sua mensagem, "A quantidade não pode ser negativa.". Ou podes verificar no próprio método se há unidades suficientes, e então usas a mensagem "Não há unidades suficientes.". Escolhe uma. Na conversa com o professor, no fim, vais explicar porque a escolheste.

Se o código não existir, quem recusa é o inventário, com o `ValueError` do método `_procurar`, "Não existe nenhum artigo com o código ...", e nenhum artigo muda.

Zero é uma quantidade válida: retirar todas as unidades de um artigo deixa-o com quantidade 0, e o pedido é aceite. Pedir para retirar zero unidades é recusado, porque não é uma retirada.

Dentro do artigo, as saídas mudam-se no atributo interno `_saidas`, porque a propriedade `saidas` não tem setter.

O plano é uma tabela com duas colunas. Na primeira, os passos do método, pela ordem em que acontecem. Na segunda, o que já mudou no artigo se o pedido for recusado nesse passo. Esta coluna obriga-te a olhar para o estado em cada ponto do método. Este é o plano do método `adicionar` do artigo, que já está escrito no teu ficheiro:

| Passo do `adicionar` | O que já mudou no artigo, se o pedido for recusado neste passo |
| --- | --- |
| Verificar se as unidades são um número inteiro | Nada |
| Verificar se as unidades são 1 ou mais | Nada |
| Escrever a nova quantidade pela propriedade; o setter verifica-a e guarda-a | Aqui não há recusa: somar 1 ou mais a uma quantidade válida dá outra quantidade válida |

As saídas não aparecem no plano do `adicionar`, porque uma entrada de material não é uma saída.

1. Copia para a folha o plano do método `retirar` do artigo e completa-o. Os dois primeiros passos já estão escritos. Acrescenta os passos que faltam, pela ordem em que devem acontecer, com a segunda coluna preenchida em cada um. Usa a forma que escolheste para a falta de unidades.

   | Passo do `retirar` do artigo | O que já mudou no artigo, se o pedido for recusado neste passo |
   | --- | --- |
   | Verificar se as unidades são um número inteiro | Nada |
   | Verificar se as unidades são 1 ou mais | Nada |
   | A completar | A completar |

2. Escreve, numa tabela igual, o plano do método `retirar` do inventário, desta vez sem nenhuma linha começada.

### Paragem 3

Mostra ao professor antes de leres a resposta: os planos dos dois métodos.

O plano do `retirar` do artigo, na forma em que o setter recusa a falta de unidades:

| Passo do `retirar` do artigo | O que já mudou no artigo, se o pedido for recusado neste passo |
| --- | --- |
| Verificar se as unidades são um número inteiro | Nada |
| Verificar se as unidades são 1 ou mais | Nada |
| Escrever a nova quantidade pela propriedade; o setter recusa-a se ficar negativa | Nada: o setter recusa antes de guardar |
| Aumentar as saídas nas unidades retiradas | Aqui não há recusa: só se chega a este passo se o setter aceitou |

Na forma em que verificas a falta de unidades no próprio método, há um passo a mais, "Verificar se há unidades suficientes", também com "Nada". Fica depois das duas primeiras verificações e antes de qualquer alteração. Depois vêm as duas alterações, a da quantidade e a das saídas.

O plano do `retirar` do inventário:

| Passo do `retirar` do inventário | O que já mudou, se o pedido for recusado neste passo |
| --- | --- |
| Encontrar o artigo com este código | Nada: se o código não existir, `_procurar` recusa, e nenhum artigo foi contactado |
| Passar o pedido ao artigo | Nada no inventário: se o artigo recusar, a recusa é dele, e pelo plano do artigo ele não mudou |

A decisão desta fase é a ordem dos passos do artigo. As duas alterações, a da quantidade e a das saídas, ficam depois de todas as verificações. Na forma do setter, a quantidade é escrita antes das saídas, porque a escrita da quantidade ainda é uma verificação: o setter pode recusá-la. É a regra "verificar primeiro, alterar depois", agora com dois dados para alterar.

Pensa antes de continuares: na forma do setter, se o passo das saídas viesse antes do passo da quantidade, o que mostraria o fim do programa para A10? A resposta: no pedido de 5, as saídas passavam de 4 a 9, e logo a seguir o setter recusava a quantidade. O `raise` do setter já não desfaz o que foi feito antes dele. A10 ficava com 2 unidades e 9 saídas, e a soma dava 11, e não 6. É assim que a regra da soma apanha uma saída contada a mais.

## Fase 4: Os dois métodos, e a sequência do programa

Agora passas o plano para Python. Escreves os dois métodos no lugar das linhas "Por completar" e do `pass` que se lhes segue. Não mudas mais nada no programa: o registo dos artigos, as consultas, a adição e o programa principal já estão preparados.

No inventário, para encontrar o artigo, um método chama outro método do mesmo objeto. Escreve-se `self._procurar(codigo)`, com o `self.` à frente, porque dentro de um método o `self` é o próprio inventário. Depois faz-se o pedido ao artigo encontrado. Repara que há dois métodos chamados `retirar`, um em cada classe. O do inventário recebe um código e um número. O do artigo recebe só um número, porque o artigo já sabe quem é. O objeto antes do ponto diz de que classe é o método chamado.

No artigo, as duas verificações do pedido escrevem-se como no método `adicionar`, que está logo acima, com as mensagens do contrato. Um `raise` para o método nessa linha, e as linhas seguintes já não são executadas. A quantidade escreve-se pela propriedade, `self.quantidade = ...`, para passar pelo setter. As saídas escrevem-se no atributo interno, `self._saidas = ...`.

1. No método `retirar` da classe `Inventario`, apaga a linha do comentário "Por completar" e a linha do `pass`. No lugar delas, escreve as linhas do teu plano, com oito espaços no início, alinhadas com a docstring. O método `saidas_de`, logo acima, já encontra um artigo pelo código e faz uma coisa com ele.

2. No método `retirar` da classe `Artigo`, faz o mesmo: apaga o comentário "Por completar" e o `pass`, e escreve as linhas do teu plano, pela ordem do plano.

3. Antes de executares, copia esta tabela para a folha e preenche as colunas de previsão. Cada linha começa no estado deixado pela anterior.

   | Momento | Resposta prevista | A10: quantidade e saídas previstas | A11: quantidade e saídas previstas | O que observaste no ecrã |
   | --- | --- | --- | --- | --- |
   | Início | Não há pedido | 6 e 0 | 3 e 0 | A preencher |
   | Depois de pedir 4 a A10 | A preencher | A preencher | A preencher | A preencher |
   | Depois de pedir 5 a A10 | A preencher | A preencher | A preencher | A preencher |

4. Executa o ficheiro inteiro. Se aparecer uma mensagem de erro do Python, lê primeiro a última linha, que diz o tipo de erro, e depois as de cima, que dizem onde aconteceu. Os [problemas frequentes](#problemas-frequentes) ajudam com as mensagens mais comuns.

5. Quando o programa correr até ao fim, preenche a última coluna. Confirma também a regra da soma: a quantidade e as saídas de A10 continuam a somar 6? Se a previsão e a observação forem diferentes, não alteres a previsão só para ficar igual ao ecrã. Procura primeiro qual das duas está errada, e escreve porquê. Se for o programa, corrige-o e volta a executar o ficheiro inteiro.

### Paragem 4

Mostra ao professor antes de leres a resposta: a tabela, com as previsões e as observações e, se alguma previsão foi diferente do ecrã, a explicação da diferença.

O que deves ver, se deixaste a falta de unidades ao setter:

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

Se verificaste a falta de unidades no próprio método, a quinta linha é `Retirar 5 de A10: recusado: Não há unidades suficientes.`, e todas as outras são iguais.

A tabela de referência:

| Momento | Resposta | A10 | A11 |
| --- | --- | --- | --- |
| Início | Não há pedido | 6 e 0 | 3 e 0 |
| Depois de pedir 4 a A10 | Aceite | 2 e 4 | 3 e 0 |
| Depois de pedir 5 a A10 | Recusado: "A quantidade não pode ser negativa.", ou "Não há unidades suficientes." | 2 e 4 | 3 e 0 |

A soma de A10 é 6 nas três linhas. A coluna de A11 mostra que o outro artigo não foi tocado.

O ficheiro `inventario.py` completo, como deve estar agora, na forma em que o setter recusa a falta de unidades:

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

Leitura guiada: lê primeiro o `retirar` do inventário, que tem duas linhas. A primeira encontra o artigo; se o código não existir, `_procurar` lança `ValueError`, e o método para ali. A segunda passa o pedido ao artigo, sem verificar nada e sem `try`. Depois lê o `retirar` do artigo, de cima para baixo. As duas verificações do pedido vêm primeiro, primeiro o tipo e depois o valor, para um texto nunca chegar à comparação com zero. A linha da quantidade escreve na propriedade, e por isso chama o setter. Se a quantidade ficasse negativa, o setter lançava `ValueError` antes de a guardar, e o método parava nessa linha. A linha das saídas só é executada se nenhuma linha acima tiver lançado uma exceção. É ela que fica em último lugar.

Se escolheste verificar a falta de unidades no próprio método, o teu `retirar` do artigo tem estas linhas depois da docstring. Substituem todas as linhas depois da docstring, incluindo os dois comentários:

```python partial
        if not isinstance(unidades, int):
            raise ValueError("As unidades a retirar têm de ser um número inteiro.")
        if unidades <= 0:
            raise ValueError("As unidades a retirar têm de ser 1 ou mais.")
        if unidades > self.quantidade:
            raise ValueError("Não há unidades suficientes.")
        self.quantidade = self.quantidade - unidades
        self._saidas = self._saidas + unidades
```

Nesta forma, as três verificações acontecem antes de qualquer alteração, e a ordem das duas últimas linhas deixa de importar. Mas a linha das saídas não pode subir para antes do último `if`. O pedido que ultrapassa a quantidade tem de ser recusado sem mudar nada.

Pensa antes de continuares: o `retirar` do inventário não tem nenhum `try`. Porque é que não deve apanhar a recusa do artigo? A resposta: quem lança a exceção decide se o pedido é válido, e quem a apanha decide o que fazer com a recusa. O inventário não sabe o que fazer com ela, e o programa principal sabe: mostra a mensagem. Se o inventário a apanhasse, a recusa não chegava ao programa principal, e ele escrevia "aceite" a um pedido recusado.

## Fase 5: Outros casos, cada um num ensaio

Os dois pedidos do programa principal são para o mesmo artigo. Não experimentam um código que não existe, nem um zero, nem um número decimal, nem a retirada de todas as unidades. Nesta fase experimentas esses casos, cada um num ensaio separado. Cada ensaio começa com o programa acabado de iniciar: A10 com 6 unidades e 0 saídas, e A11 com 3 unidades e 0 saídas.

1. Para não mexeres no teu ficheiro de trabalho, guarda uma cópia do `inventario.py`, na mesma pasta, com o nome `ensaios.py`. Nessa cópia, mantém as duas classes e as três linhas que criam o inventário e registam os artigos. Substitui todas as linhas a partir de `print("Início")` por este bloco:

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

   Leitura guiada: este bloco depende das classes e do inventário criados acima, e não é para executar sozinho. Mostra o estado dos dois artigos antes, faz um pedido dentro de um `try` e mostra o estado depois. A linha `inventario.retirar("A11", 3)` é o pedido.

2. Copia esta tabela para a folha. Em cada ensaio, preenche primeiro as colunas de previsão. Depois muda o código e as unidades da linha do pedido para os da tabela, e executa o ficheiro inteiro, para voltares a começar com os valores iniciais.

   | Pedido | Aceite ou recusado, e quem recusa | Mensagem prevista | A10 depois: quantidade e saídas | A11 depois: quantidade e saídas | Resultado observado |
   | --- | --- | --- | --- | --- | --- |
   | `retirar("A11", 3)` | A preencher | A preencher | A preencher | A preencher | A preencher |
   | `retirar("A11", 0)` | A preencher | A preencher | A preencher | A preencher | A preencher |
   | `retirar("A11", 1.5)` | A preencher | A preencher | A preencher | A preencher | A preencher |
   | `retirar("A12", 1)` | A preencher | A preencher | A preencher | A preencher | A preencher |

   Em cada ensaio, lê as quatro linhas de estado, as de A10 e as de A11, antes e depois do pedido. Um pedido feito a A11 não deve mudar A10, e só confirmas isso se olhares para as duas.

3. Faz ainda um último ensaio, desta vez com dois pedidos seguidos, sem reiniciar entre eles: retirar 3 unidades de A11 e, logo a seguir, retirar 1. Para isso, volta a pôr o pedido `inventario.retirar("A11", 3)`. Depois copia o bloco do `try` e do `except` e cola a cópia logo a seguir ao primeiro, antes da linha `print("Depois")`, com o pedido de 1 unidade. Prevê e regista as duas respostas e o estado final dos dois artigos. Depois executa e explica, em duas frases, o que a segunda resposta diz sobre um artigo vazio, e porque é que as saídas de A11 têm o valor que têm.

### Paragem 5

Mostra ao professor antes de leres a resposta: a tabela dos quatro ensaios e o ensaio dos dois pedidos seguidos, com as duas frases.

A tabela de referência. Em todas as linhas, o ensaio começou com A10 em 6 e 0 e A11 em 3 e 0:

| Pedido | Aceite ou recusado, e quem recusa | Mensagem | A10 depois | A11 depois |
| --- | --- | --- | --- | --- |
| `retirar("A11", 3)` | Aceite | Pedido aceite | 6 e 0 | 0 e 3 |
| `retirar("A11", 0)` | Recusado pelo método `retirar` do artigo | As unidades a retirar têm de ser 1 ou mais. | 6 e 0 | 3 e 0 |
| `retirar("A11", 1.5)` | Recusado pelo método `retirar` do artigo | As unidades a retirar têm de ser um número inteiro. | 6 e 0 | 3 e 0 |
| `retirar("A12", 1)` | Recusado pelo inventário, no `_procurar` | Não existe nenhum artigo com o código A12. | 6 e 0 | 3 e 0 |

As mensagens são iguais nas duas formas de recusar a falta de unidades, porque nenhum destes quatro pedidos ultrapassa a quantidade. O primeiro ensaio mostra:

```text
Antes
A10: quantidade 6 e saídas 0
A11: quantidade 3 e saídas 0
Pedido aceite
Depois
A10: quantidade 6 e saídas 0
A11: quantidade 0 e saídas 3
```

O ensaio dos dois pedidos seguidos, 3 e depois 1, mostra:

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

Na forma em que verificas a falta de unidades no próprio método, a segunda resposta é `Pedido recusado: Não há unidades suficientes.`, com o mesmo estado final.

As duas frases: um artigo com quantidade 0 é válido, mas não tem nada para retirar. Por isso qualquer pedido de 1 ou mais é recusado, porque a quantidade ficaria negativa. As saídas ficam em 3 porque só contam as retiradas aceites, e a segunda foi recusada antes de as saídas mudarem.

Pensa antes de continuares: 1.5 é mais do que 1. Porque é que o pedido de 1.5 recebe a mensagem do número inteiro, e não é aceite? A resposta: porque 1.5 não é um número inteiro, e o método verifica o tipo antes do valor. A primeira verificação recusa-o, e a segunda nem chega a ser feita.

## Fase 6: Explicar a correção

Encontrar e corrigir um erro acaba com uma explicação feita com valores: o que esperavas, o que viste, a causa e a confirmação de que ficou resolvido. É a mesma rotina que segues sempre que um programa falha. Nesta fase escreves essa explicação para a correção que fizeste.

1. Volta às respostas que escreveste na fase 1, antes de completares os métodos. Escolhe um pedido que o programa inicial tratava mal e que o teu programa agora trata de acordo com o contrato. Escreve quatro frases, cada uma com valores ou instruções concretas:

   1. "Esperava ...": o que o pedido devia fazer à quantidade e às saídas.
   2. "Observei ...": o que o programa inicial mostrou.
   3. "A instrução que explica a diferença é ...": a linha do programa inicial responsável, e porquê.
   4. "Depois da alteração, confirmei ...": o que o teu programa mostra agora, com os valores.

2. Compara as tuas frases com este exemplo, feito para o pedido de 4 a A10. "Esperava que, ao retirar 4 de A10, a quantidade passasse de 6 a 2 e as saídas de 0 a 4. Observei no programa inicial a mensagem "aceite", mas A10 continuou com quantidade 6 e saídas 0. A instrução que explica a diferença é o `pass` dos dois métodos `retirar`, que não faz nada e não lança nenhuma exceção. Por isso o programa principal escreveu "aceite" sem nada ter mudado. Depois da alteração, confirmei que o mesmo pedido deixa A10 com quantidade 2 e saídas 4, e que o pedido de 5 a seguir é recusado sem mudar esses valores." Repara que cada frase tem valores ou instruções concretas. Uma explicação que diga só "o método não funcionava e agora funciona" ainda não explica nada.

### Paragem 6

No fim, o professor conversa contigo, numa conversa curta, com o teu programa aberto. A conversa não dá nota: serve para tu e o professor perceberem o que já está firme e o que precisa de mais prática antes do projeto. Se trabalhaste em par, a conversa é individual na mesma, e cada pessoa explica o seu próprio raciocínio.

Não precisas de recitar definições: usa o teu programa e os valores. Não há uma resposta para decorar, porque as respostas estão no que fizeste nas fases indicadas. O professor escolhe uma ou duas destas tarefas:

- mostrar, no teu código, onde o pedido é encaminhado e onde é decidido (fases 3 e 4);
- explicar porque é que uma recusa não pode alterar nem a quantidade nem as saídas, apontando a linha do teu código que garante isso (fases 3 e 4);
- explicar que forma escolheste para recusar a falta de unidades, a do setter ou a da verificação no método, e porquê (fase 3);
- mostrar como confirmaste que A10 não mudou nos ensaios feitos com A11 (fase 5);
- prever o resultado de um pedido com outros valores, escolhido pelo professor, antes de o executares (fases 4 e 5);
- encontrar e corrigir um erro que o professor introduza numa cópia do teu programa. Segue a rotina de sempre. Reproduz o erro com um caso e diz que tipo de erro é. Escreve uma hipótese e confirma-a com os valores. Corrige a causa e volta a correr tudo (fase 6).

Podes dizer em que passos recebeste ajuda: essa informação serve para orientar o trabalho seguinte.

As ideias que juntaste neste laboratório são as ideias centrais do M10. A primeira é distinguir a classe dos objetos e do estado de cada um. A segunda é proteger os dados de um objeto quando ele recusa um pedido. A terceira é dar cada tarefa ao objeto que tem a informação para a fazer, como o inventário que encontra o artigo e o artigo que decide. Vão ser avaliadas no [projeto](../projeto/README.md): a tua aplicação, um livro de receitas. O projeto é avaliado no fim do M12, com demonstração, explicação e uma pequena alteração feita na hora. É a avaliação prática do M10, do M11 e do M12, cada uma com os critérios do seu módulo. Os critérios do M10 são estas três ideias, agora na tua aplicação.

O projeto começa já no fim do M10, com o modelo do teu livro de receitas, descrito por palavras, como o que escreveste na fase 2. Esta conversa é um primeiro ensaio da explicação que o projeto te vai pedir. O que é cada objeto? Onde está a regra? O que acontece aos dados quando um pedido é recusado?

## Problemas frequentes

### `IndentationError: unindent does not match any outer indentation level`

Em português: uma linha recuou para a esquerda, mas não ficou alinhada com nenhum dos níveis de indentação de cima. Um `IndentationError` é um "erro de indentação", e o programa nem chega a começar. Uma linha de um método ficou com uma indentação diferente das outras linhas do mesmo método, por exemplo com seis espaços em vez de oito. Dentro de um método, todas as linhas ficam alinhadas com a docstring, com oito espaços a partir da margem, e as linhas dentro de um `if` com doze.

### `NameError: name '_procurar' is not defined`

Em português: o nome `_procurar` não está definido. Um `NameError` ("erro de nome") aparece quando se usa um nome que o Python não conhece. Dentro do método do inventário, a chamada ficou escrita `_procurar(codigo)`, sem o `self.` à frente, e o Python procura uma função solta com esse nome. Escreve `self._procurar(codigo)`, como em `quantidade_de`. As versões recentes do Python acrescentam à mensagem `Did you mean: 'self._procurar'?`, isto é, "querias dizer `self._procurar`?".

### `TypeError: Artigo.retirar() takes 2 positional arguments but 3 were given`

Em português: o `retirar` recebe 2 argumentos, mas foram dados 3. Um `TypeError` ("erro de tipo") aparece aqui porque a chamada não bate com o `def`. A mensagem começa por `Artigo.retirar()`, o que diz logo que é o método do artigo. Nas versões anteriores à 3.10, começa só por `retirar()`. No inventário, a chamada ao artigo ficou com o código e as unidades, como `artigo.retirar(codigo, unidades)`. O `retirar` do artigo só recebe as unidades, porque o artigo já sabe quem é. O Python conta também o `self`, e por isso diz 2 e 3. Escreve `artigo.retirar(unidades)`.

### `AttributeError: property 'saidas' of 'Artigo' object has no setter`

Em português: a propriedade `saidas` do objeto `Artigo` não tem setter. Nas versões do Python anteriores à 3.11, a mensagem começa por `AttributeError: can't set attribute`, "não se pode escrever o atributo". Um `AttributeError` é um "erro de atributo". O método do artigo escreve nas saídas através da propriedade, com `self.saidas = ...`, e a propriedade não tem setter. Dentro do artigo, as saídas mudam-se no atributo interno: `self._saidas = self._saidas + unidades`.

### `TypeError: '<=' not supported between instances of 'str' and 'int'`

Em português: a comparação `<=` não é possível entre um texto e um número inteiro (`str` é o texto e `int` o inteiro). Aparece num pedido com um texto, como `"2"`. O método compara as unidades com um número antes de verificar se são um número inteiro. Se trocaste outro sinal, como `<`, a mensagem mostra esse sinal. Verifica primeiro o tipo, com o `isinstance`, e só depois o valor, como no setter e no `adicionar`.

### O programa diz "aceite", mas a quantidade e as saídas não mudaram

Um dos métodos `retirar` ainda não faz nada: ficou só com o `pass`, ou o inventário encontra o artigo mas não lhe passa o pedido. Segue o pedido desde o programa principal até ao método do artigo, e confirma que cada passo chama o seguinte.

### Num ensaio, o programa para com uma mensagem que acaba em `ValueError`, em vez de mostrar "Pedido recusado"

O pedido ficou fora do `try`. A mensagem mostra o caminho do pedido, do programa principal até ao método onde a recusa nasceu: o `retirar` do artigo, o setter ou o `_procurar`. Põe o pedido dentro do `try`, como no bloco da fase 5, com o `except ValueError as erro` por baixo.

## Desafios

1. Os ensaios que faltam. No `ensaios.py`, ensaia `retirar("A11", -1)` e `retirar("A11", "2")`, um de cada vez, como na fase 5. Antes de cada um, escreve se o pedido é aceite ou recusado, quem o recusa, a mensagem e o estado dos dois artigos depois. Depois de executares, diz, para cada um, que linha do teu método o recusou. Pista: segue o teu método pela ordem das linhas, com o valor do pedido.

2. Um terceiro artigo. No `ensaios.py`, regista um terceiro artigo, A12, Tesoura, com 4 unidades, a seguir aos registos de A10 e A11. Acrescenta uma linha que mostre A12 no "Antes" e no "Depois". No lugar do pedido, faz três pedidos seguidos a A12, cada um no seu `try`: retirar 1, depois 2, depois 2. Antes de executares, faz uma tabela com a resposta a cada pedido, a quantidade e as saídas de A12 depois de cada um, e a soma das duas. Confirma, no fim, que A10 e A11 não mudaram. Pista: cada pedido parte do estado deixado pelo anterior, e a soma diz-te se contaste bem as saídas.

3. A outra forma. Faz uma cópia do `ensaios.py` com o nome `outra-forma.py`. Nela, troca a forma de recusar a falta de unidades: se a deixaste ao setter, verifica-a no próprio método, e ao contrário. Corre lá os quatro ensaios e os dois pedidos seguidos da fase 5. Que mensagens mudam, e quais ficam iguais? Porquê? No fim, diz em duas frases qual das duas formas preferes, e porquê. Pista: procura os pedidos que ultrapassam a quantidade.

## Antes de terminares

- [ ] O `inventario.py` executa e mostra as oito linhas da paragem 4, com a mensagem da forma que escolheste.
- [ ] O `ensaios.py` tem o bloco da fase 5, e fizeste os quatro ensaios e os dois pedidos seguidos.
- [ ] Tens na folha a descrição das classes e da relação, o estado dos dois artigos e as respostas da fase 2. Tens também os dois planos, as tabelas das fases 4 e 5 e as quatro frases.
- [ ] Guardaste a pasta `tema-06` e a folha, e entregaste-as pelo meio indicado pelo professor. Guarda uma cópia para ti: vais voltar a precisar destas ideias no projeto.
- [ ] Sabes dizer quem recusa cada um dos pedidos da fase 5, e porquê.
- [ ] Consegues explicar, por palavras tuas, porque é que uma recusa não muda nem a quantidade nem as saídas, e que linha do teu código o garante.

![Rodapé](../imagens/rodape.png)

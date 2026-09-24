![Cabeçalho](../imagens/cabecalho.png)

# Dos materiais da sala aos dados de um programa

*M10 · Caderno 1*

Imagina que és responsável pelos materiais de uma sala de aula. No armário há cadernos, pastas e canetas. Durante a semana, algumas unidades são usadas e saem do armário; outras chegam numa encomenda e são arrumadas. Quando alguém te pergunta "ainda temos pastas?", precisas de uma forma de responder sem abrir o armário e contar tudo outra vez.

A solução mais antiga é uma folha de registo, com uma linha por material e o número de unidades que existem. A solução que vamos construir ao longo deste módulo é um programa que mantém esse registo por nós. Antes de escrever qualquer programa, porém, temos de tomar duas decisões: que informação precisamos de guardar e que operações fazem sentido sobre essa informação. Este caderno trata dessas duas decisões.

Quase todo o caderno se faz em papel. Só na secção 6 aparece código Python, para comparar duas maneiras de organizar o mesmo programa. Esse código usa apenas instruções básicas (variáveis, uma função, uma condição e `print`), e cada linha é explicada.

## Antes de começarmos

O professor pode propor-te um [diagnóstico de programação](../avaliacoes/diagnostico-inicial.md). Serve para perceber de que te recordas e onde precisas de apoio. Podes responder por palavras, desenhos, contas ou pseudocódigo; não tens de conhecer nenhuma linguagem em particular.

Depois do diagnóstico, podes trabalhar uma das atividades do [bridge de raciocínio](bridge-raciocinio.md), escolhida com o professor. "Bridge" é a palavra inglesa para ponte. Aqui, é uma atividade curta para recuperar uma ideia de que vais precisar antes de avançar, como seguir os valores de uma variável ao longo de um programa ou ler uma condição.

## 1. A informação que interessa guardar

Uma ficha de material pode ter este aspeto:

| Informação | O que guardámos |
| --- | --- |
| Código | A01 |
| Nome | Caderno |
| Quantidade | 6 |

Cada linha desta ficha responde a uma pergunta diferente, e vale a pena perceber porque é que precisamos das três.

O **código** identifica o material. À primeira vista parece repetir o nome, mas não repete. Dois materiais podem ter nomes parecidos, como "Caderno" e "Caderno quadriculado", e a mesma pessoa pode escrever o nome de maneiras diferentes em dias diferentes: "caderno", "Caderno", "Cadernos". O código é curto, é escolhido uma vez e não se repete: não há dois materiais com o código A01. Quando um valor não se repete e permite distinguir cada coisa de todas as outras, dizemos que identifica essa coisa. Na escola passa-se o mesmo contigo: além do nome, tens um número de aluno. Pode haver dois alunos com o mesmo nome, mas não há dois com o mesmo número.

O **nome** descreve o material a quem lê a ficha. O código A01 não diz nada a uma pessoa que abre o armário; a palavra "Caderno" diz. O nome serve as pessoas, e o código serve a identificação.

A **quantidade** diz quantas unidades desse material existem neste momento. É a informação que mais vai mudar, porque muda sempre que alguém usa ou arruma material.

No nosso inventário, chamamos **artigo** a cada referência de material, isto é, a cada linha do registo. A ficha A01 representa o artigo "Caderno", do qual há seis unidades. Repara no que isto significa: não temos seis fichas, uma por caderno físico. Temos uma ficha, e o número 6 está escrito dentro dela. Se amanhã chegarem mais quatro cadernos, não criamos quatro fichas novas. Mudamos o 6 para 10 na ficha que já existe.

Esta é uma escolha de representação, feita a pensar no problema. Se quiséssemos acompanhar cada computador portátil da escola individualmente, com o seu número de série e o nome de quem o requisitou, precisaríamos de uma ficha por equipamento. Para cadernos e canetas isso não faz sentido: ninguém quer saber qual dos seis cadernos foi usado, só quantos restam. Representar um problema é sempre escolher o que interessa e deixar de fora o resto.

Cada ficha tem ainda de cumprir regras para fazer sentido: o código não se repete, o nome está preenchido e a quantidade é um número inteiro que não é negativo. Vamos voltar a estas regras na secção 5, com calma.

## 2. Entidade: aquilo que escolhemos representar

Ao analisar um problema, procuramos as coisas ou as ideias sobre as quais precisamos de guardar informação. Chamamos **entidade** a cada uma dessas coisas relevantes para o problema.

No inventário da sala, um artigo é uma entidade: precisamos de saber o seu código, o seu nome e a sua quantidade. A parede da sala também existe, e o quadro também, mas não precisamos de os representar para controlar os materiais do armário. Existir no mundo real não chega para uma coisa entrar no programa. Tem de ser relevante para o que queremos resolver.

Também se podem representar ideias em que não se consegue tocar, como uma reserva de sala, uma tarefa por fazer ou uma encomenda. Uma encomenda não é um objeto físico: é um pedido que alguém fez e que outra pessoa vai entregar. Mesmo assim, tem informação própria, como a data em que foi feita e o que foi pedido. Por isso, "entidade" não quer dizer "algo em que conseguimos tocar". Quer dizer "algo sobre o qual o programa precisa de guardar informação".

Pensa noutro problema para confirmares a ideia. Num programa de gestão da biblioteca da escola, as entidades seriam provavelmente os livros, os leitores e os empréstimos. As estantes só seriam uma entidade se o programa precisasse de dizer em que estante está cada livro. A mesma coisa real pode ser entidade num problema e não ser noutro, porque o que decide é a pergunta a que o programa tem de responder.

O erro típico de quem começa é querer representar tudo o que vê. Um programa que guarda a cor das paredes da sala não fica melhor por isso: fica mais difícil de escrever e de corrigir, sem responder a nenhuma pergunta nova. Ao longo deste módulo vamos concentrar-nos em duas entidades, os artigos e o inventário que os reúne.

## 3. Estado: como está a informação neste momento

A ficha A01 diz que há 6 cadernos. Depois de alguém retirar 2, a quantidade deve passar a 4.

Chamamos **estado** ao conjunto dos valores de uma entidade num certo momento. O estado funciona como uma fotografia: mostra como as coisas estão agora, e daqui a cinco minutos a fotografia pode ser outra. Podemos comparar o estado antes e depois de uma operação:

| Informação | Antes de retirar | Depois de retirar 2 |
| --- | --- | --- |
| Código | A01 | A01 |
| Nome | Caderno | Caderno |
| Quantidade | 6 | 4 |

Olha para a tabela com atenção. O artigo continua a ser A01. Mudou a quantidade, mas não passámos a falar de outro material. O estado mudou e a identidade do artigo manteve-se. Acontece o mesmo com o marcador de um jogo de futebol: ao intervalo está 1-0 e no fim está 2-1, mas o jogo é o mesmo. O marcador mostra o estado do jogo, e o jogo não passou a ser outro por o resultado ter mudado.

Esta distinção vai ser útil muitas vezes. Quando um programa não faz o que esperavas, uma das primeiras perguntas a fazer é esta: qual era o estado antes desta instrução, e qual é o estado depois? Se consegues responder às duas, consegues perceber o que a instrução fez de facto, e não apenas o que devia ter feito.

Um erro frequente é pensar que, quando a quantidade muda, aparece um artigo novo. Não aparece. Se aparecesse um artigo novo cada vez que alguém retira material, ao fim de um mês a folha de registo teria dezenas de linhas para o mesmo caderno, e ninguém saberia qual delas estava certa.

## 4. Comportamento: o que podemos pedir que aconteça

Guardar dados não chega. Um inventário serve para ser consultado e atualizado, e isso exige operações. Para um artigo, faz sentido pedir três coisas: consultar a quantidade, para saber quantas unidades existem agora; adicionar unidades, quando chega material; e retirar unidades, quando o material é usado.

Chamamos **comportamento** ao conjunto de operações que podemos pedir a uma entidade. "Quantidade 6" é uma informação sobre o estado. "Retirar 2" é um pedido de operação. A primeira descreve como as coisas estão; a segunda pede que alguma coisa aconteça.

Consultar também é uma operação, mas não altera a quantidade. Se perguntas quantos cadernos existem e a resposta é 6, não passam a existir menos cadernos por teres feito a pergunta. É como olhar para um relógio: ver as horas não muda as horas. Dito assim parece óbvio, mas vai ser importante quando escrevermos código. Há operações que só leem o estado e operações que o mudam, e confundir as duas é a origem de muitos erros.

Nem todas as operações imagináveis fazem sentido. "Pintar o artigo de azul" não é uma operação do nosso inventário, porque não guardamos cores. As operações que escolhemos dependem da informação que escolhemos guardar, e as duas escolhas fazem-se em conjunto: se decidirmos guardar uma informação que nenhuma operação usa, provavelmente não precisávamos dela; se quisermos uma operação que precisa de uma informação que não guardamos, falta alguma coisa na ficha.

## 5. Uma operação tem de respeitar regras

Podes retirar 2 unidades quando existem 6. Mas não podes retirar 9, porque não há unidades suficientes. Um programa que aceitasse esse pedido ficaria com -3 cadernos, um número que não corresponde a nada que exista no armário. O programa deve recusar o pedido e conservar a quantidade que existia.

Para saber quando aceitar e quando recusar, precisamos de regras escritas. Neste inventário adotamos estas três:

1. Cada código identifica um único artigo.
2. O nome do artigo está preenchido.
3. A quantidade é um número inteiro não negativo.

"Inteiro" significa sem parte decimal: 4 é inteiro, 4,5 não é. Não faz sentido ter quatro cadernos e meio no armário. "Não negativo" significa zero ou maior do que zero. Juntando as duas condições, as quantidades possíveis são 0, 1, 2, 3 e assim por diante.

Ter zero unidades é possível e é um estado válido: significa que o material esgotou. A ficha continua a existir, porque o material continua a fazer parte do inventário, e voltará a ter unidades quando chegar uma encomenda.

Há ainda uma regra para os pedidos, que é diferente da regra do estado: um pedido para adicionar ou para retirar tem de ser um número inteiro positivo, isto é, 1 ou mais. Pedir para retirar zero unidades é recusado. Pode parecer estranho recusar um pedido que não faria mal nenhum, mas um pedido de zero unidades não corresponde a nenhuma ação real e quase sempre é um engano de quem o escreveu. Outros programas podem escolher outra regra. O importante é que a regra esteja escrita e que o programa a siga sempre.

As duas regras sobre o zero não se contradizem. Com 6 unidades, retirar 6 é aceite e deixa a quantidade em zero, que é um estado válido. Com 6 unidades, retirar 0 é recusado, porque o pedido não é válido. A pergunta "este estado é válido?" e a pergunta "este pedido é válido?" são perguntas diferentes, e cada uma tem a sua regra.

### Exemplo guiado: seguir os valores passo a passo

Partimos do artigo A01 com 6 unidades e fazemos três pedidos, pela ordem indicada. Em cada passo aplicamos as regras antes de mexer na ficha.

| Passo | Pedido | O que acontece | Quantidade depois |
| --- | --- | --- | ---: |
| Início | Nenhum | A ficha indica 6 unidades | 6 |
| 1 | Consultar | Respondemos que existem 6; a ficha não muda | 6 |
| 2 | Retirar 2 | 2 é um inteiro positivo e não passa de 6; fazemos 6 - 2 | 4 |
| 3 | Retirar 5 | 5 é um inteiro positivo, mas só existem 4; o pedido é recusado | 4 |

Vamos ler a tabela linha a linha, porque é assim que se lê um programa.

Na linha de início ainda não aconteceu nada: registamos só o ponto de partida. Sem esta linha não conseguiríamos verificar a seguinte, porque não saberíamos de onde partimos.

No passo 1, consultar não altera a ficha. A coluna da direita repete o 6, e essa repetição é informação: diz-nos que a operação aconteceu e que o estado ficou igual.

No passo 2 verificamos as regras antes de calcular. O pedido é um inteiro positivo, e há unidades suficientes, porque 2 não é maior do que 6. Só depois de confirmar as duas coisas fazemos a conta e escrevemos 4 na ficha.

No passo 3 o ponto de partida já não é 6, é 4, porque cada linha começa com a quantidade deixada pela linha anterior. Este é o erro mais comum ao construir uma tabela destas: voltar ao valor inicial em cada linha. Como 5 é maior do que 4, o pedido é recusado e a quantidade fica em 4. Recusar não é pôr a ficha a zero nem apagá-la. Recusar é não mexer.

Uma tabela como esta chama-se um **traço**: um registo do que acontece em cada passo de uma sequência de instruções. Serve para explicar um programa a outra pessoa e serve, sobretudo, para encontrar erros, porque obriga a olhar para o estado depois de cada instrução em vez de olhar só para o resultado final.

## 6. Duas maneiras de organizar um programa

Até aqui trabalhámos em papel. Agora vamos ver como um programa em Python poderia fazer o mesmo. Vamos vê-lo de duas maneiras, porque a diferença entre elas é a razão de ser deste módulo.

Uma maneira de pensar e de organizar um programa chama-se um **paradigma de programação**. Um paradigma não é uma linguagem: a mesma linguagem, como o Python, permite escrever programas em mais do que um paradigma. É mais parecido com um critério de arrumação. Duas pessoas podem arrumar o mesmo armário por tipo de material ou por frequência de uso; o armário e os materiais são os mesmos, e o que muda é a lógica com que cada coisa é posta no seu lugar.

### A maneira habitual nos primeiros programas: programação estruturada

Nos primeiros programas que se aprendem a escrever, os dados ficam em variáveis e as operações são funções que recebem dados e devolvem resultados. O programa é uma sequência de passos, com condições e ciclos a decidir que passos se executam. Esta forma de organizar chama-se **programação estruturada**. Também se diz programação procedimental, porque o programa se organiza em procedimentos, isto é, em funções.

Aqui está a ficha A01 e o exemplo guiado da secção 5 escritos dessa maneira. É um programa completo. Para o executares, copia-o para um ficheiro novo com a extensão `.py` (por exemplo, `inventario.py`) no editor de Python que usas nas aulas, e executa o ficheiro inteiro. Todos os programas completos destes cadernos funcionam com Python 3, a partir da versão 3.10.

```python
def retirar(quantidade, unidades):
    """Devolve a quantidade que fica depois de um pedido de retirada.

    Se o pedido for possível, devolve a quantidade menos as unidades pedidas.
    Se não for possível, devolve a quantidade que recebeu, sem mudanças.
    """
    if unidades > 0 and unidades <= quantidade:
        return quantidade - unidades
    return quantidade


# O artigo A01 fica guardado em três variáveis separadas.
codigo_caderno = "A01"
nome_caderno = "Caderno"
quantidade_caderno = 6

quantidade_caderno = retirar(quantidade_caderno, 2)
print(nome_caderno, quantidade_caderno)

quantidade_caderno = retirar(quantidade_caderno, 5)
print(nome_caderno, quantidade_caderno)
```

Ao executar, o programa mostra:

```text
Caderno 4
Caderno 4
```

Vamos ler o programa por partes.

A primeira parte define uma função. `def retirar(quantidade, unidades):` diz ao Python que, a partir dali, existe uma função chamada `retirar` que recebe dois valores: a quantidade que existe e as unidades que se querem retirar. As linhas indentadas por baixo (mais afastadas da margem) pertencem à função. Definir a função não a executa: só a prepara para ser usada mais tarde.

O texto entre três aspas, logo a seguir à linha do `def`, chama-se **docstring**. É uma explicação do que a função faz, escrita para pessoas. O Python não a executa como instrução, mas guarda-a, e os editores mostram-na quando passas o rato por cima do nome da função. Vamos escrever docstrings em todas as funções, classes e métodos destes cadernos, porque obrigam quem escreve a dizer o que o código promete.

A linha `if unidades > 0 and unidades <= quantidade:` junta as duas condições do pedido. `unidades > 0` pergunta se o pedido é positivo. `unidades <= quantidade` pergunta se o pedido é menor ou igual ao que existe, ou seja, se há unidades suficientes. A palavra `and` exige que as duas perguntas tenham resposta verdadeira. Se tiverem, a função executa `return quantidade - unidades`: calcula o que fica e devolve esse valor a quem a chamou, terminando ali. Se alguma das perguntas tiver resposta falsa, a função salta para a última linha e devolve a quantidade que recebeu, sem mudanças.

A segunda parte é o programa principal. As três primeiras linhas guardam os dados do artigo A01 em três variáveis. A seguir vem a linha mais importante:

```python partial
quantidade_caderno = retirar(quantidade_caderno, 2)
```

Esta linha repete uma linha do programa acima e não corre sozinha, porque depende da função e da variável definidas antes. Lê-se da direita para a esquerda. Primeiro o Python chama a função com os valores 6 e 2. A função verifica o pedido e devolve 4. Só depois a atribuição guarda esse 4 na variável `quantidade_caderno`. Repara que a função, por si só, não muda a variável: recebe um número e devolve outro. Quem muda a variável é a atribuição. Se escrevêssemos só `retirar(quantidade_caderno, 2)`, sem o `quantidade_caderno =` à esquerda, o 4 seria calculado e perdido, e a variável continuaria com 6.

Na segunda chamada, a função recebe 4 e 5. Como 5 é maior do que 4, a condição é falsa e a função devolve o 4 que recebeu. O programa mostra `Caderno 4` duas vezes, exatamente como o traço da secção 5: depois de retirar 2 ficaram 4, e o pedido de 5 foi recusado sem mexer na quantidade.

Este programa tem duas limitações que vamos resolver mais à frente. A primeira é que quem chama a função não fica a saber que o pedido foi recusado: recebe um número e mais nada. A segunda é que a função não verifica se o pedido é inteiro, e aceitaria retirar 1.5 unidades. As duas ficam para o caderno 3.

### O problema das variáveis soltas

Agora acrescentamos o artigo A02, "Pasta", com 2 unidades, e cometemos um engano pequeno, do género que acontece a toda a gente. O programa é completo e pode ser executado sozinho:

```python
def retirar(quantidade, unidades):
    """Devolve a quantidade que fica depois de um pedido de retirada.

    Se o pedido for possível, devolve a quantidade menos as unidades pedidas.
    Se não for possível, devolve a quantidade que recebeu, sem mudanças.
    """
    if unidades > 0 and unidades <= quantidade:
        return quantidade - unidades
    return quantidade


codigo_caderno = "A01"
nome_caderno = "Caderno"
quantidade_caderno = 6

codigo_pasta = "A02"
nome_pasta = "Pasta"
quantidade_pasta = 2

# Queríamos retirar 1 pasta, mas escrevemos a variável do caderno no pedido.
quantidade_pasta = retirar(quantidade_caderno, 1)

print(nome_caderno, quantidade_caderno)
print(nome_pasta, quantidade_pasta)
```

O programa mostra:

```text
Caderno 6
Pasta 5
```

A pasta tinha 2 unidades. Pedimos para retirar 1 e ficou com 5. O Python não se queixou, porque para o Python `quantidade_caderno` e `quantidade_pasta` são apenas dois números guardados com dois nomes diferentes. A função recebeu 6 e 1, fez a conta 6 - 1, e a atribuição guardou o resultado na variável da pasta. Cada instrução, isoladamente, fez exatamente o que estava escrito.

O problema está noutro lado. A ligação entre `codigo_pasta`, `nome_pasta` e `quantidade_pasta` só existe na nossa cabeça, através dos nomes que escolhemos para as variáveis. O programa não sabe que aquelas três variáveis descrevem o mesmo artigo, nem que `quantidade_caderno` pertence a outro. E a função `retirar` não sabe nada sobre artigos: recebe dois números e devolve um terceiro.

Com dois artigos precisamos de seis variáveis. Com cinquenta artigos precisaríamos de cento e cinquenta, e cada chamada teria de receber a variável certa, escrita à mão, sem que nada no programa ajudasse a detetar a troca.

### A outra maneira: programação orientada a objetos

Na **programação orientada a objetos** (também se diz orientada por objetos, como no nome oficial deste módulo, e abrevia-se POO) juntamos numa só unidade o código, o nome e a quantidade de um artigo, e ligamos a essa unidade as operações que lhe dizem respeito. Em vez de dizermos "chama a função retirar com a quantidade do caderno", passamos a dizer "pede ao caderno que retire 2". O artigo guarda os seus próprios dados e sabe realizar as suas próprias operações. Deixa de ser possível entregar a quantidade da pasta ao caderno por engano, porque cada artigo só mexe na sua.

Essa unidade chama-se objeto, e é o assunto do próximo caderno. O que interessa agora é perceber que as três ideias deste caderno têm um nome próprio em POO:

| Ideia deste caderno | Nome em programação orientada a objetos | Onde a vais estudar |
| --- | --- | --- |
| Entidade, como o artigo | Objeto, descrito por uma classe | Caderno 2 |
| Estado: código, nome e quantidade | Atributos do objeto | Caderno 2 |
| Comportamento: consultar, adicionar, retirar | Métodos do objeto | Cadernos 2 e 3 |
| Regras: quantidade inteira não negativa | Proteção do estado do objeto | Caderno 3 |

A programação orientada a objetos não deita fora o que já sabes. Continuamos a usar variáveis, condições, ciclos e funções, mas passam a estar arrumados dentro dos objetos, junto dos dados a que dizem respeito. A programação estruturada também não está errada: para um cálculo pequeno, uma função solta é muitas vezes a solução mais simples. A POO ajuda quando há muitas entidades, cada uma com o seu estado e as suas regras, que é precisamente o caso de um inventário.

## 7. Agora experimenta

Cada exercício pede uma decisão que o exemplo guiado não tomou por ti. Escreve o raciocínio, e não só a resposta final: é o raciocínio que o professor vai querer ouvir-te explicar. Os exercícios fazem-se no caderno diário ou numa folha, e são entregues pelo meio indicado pelo professor.

### Exercício 1: Informação ou operação

A ficha A02 tem o nome "Pasta" e a quantidade 3. Lê estas expressões: "A02", "Pasta", "quantidade 3", "consultar a quantidade", "retirar 1", "adicionar 4" e "a quantidade passou a 2".

Faz duas colunas, uma com o título "informação guardada na ficha" e outra com o título "operação que podemos pedir", e coloca cada expressão na coluna certa. Uma das expressões é mais difícil de classificar do que as outras. Identifica-a e explica, numa ou duas frases, porque a puseste na coluna que escolheste.

### Exercício 2: Os casos que o exemplo não mostrou

A ficha A02, "Pasta", tem 3 unidades. Cada linha da tabela é um caso separado, que começa sempre com 3 unidades. Copia a tabela e completa-a. Na última coluna, indica qual das regras da secção 5 usaste para decidir.

| Pedido | Aceite ou recusado | Quantidade depois | Regra usada |
| --- | --- | ---: | --- |
| Retirar 3 | A completar | A completar | A completar |
| Retirar 0 | A completar | A completar | A completar |
| Adicionar 4 | A completar | A completar | A completar |
| Retirar 1,5 | A completar | A completar | A completar |

Depois, em duas ou três frases, explica porque é que "retirar 3" e "retirar 0" têm respostas diferentes, apesar de o zero aparecer nos dois casos.

### Exercício 3: A ordem dos pedidos

A ficha A03, "Caneta", tem 4 unidades. Vais construir dois traços, cada um a começar em 4.

No primeiro traço, os pedidos são, por esta ordem: adicionar 5 e depois retirar 7. No segundo traço, os mesmos pedidos aparecem pela ordem inversa: retirar 7 e depois adicionar 5.

Usa colunas iguais às do exemplo guiado da secção 5. Compara a quantidade final dos dois traços e explica porque são diferentes, se os pedidos são os mesmos. Termina com uma frase que explique a um colega porque é que, num traço, não se pode trocar a ordem das linhas.

### Exercício 4: O passo que falta

Um programa tem uma ficha com 5 unidades. Recebe um pedido para retirar 2, verifica que o pedido é possível e mostra a mensagem "Pedido aceite". No entanto, quando consultamos a quantidade logo a seguir, a resposta continua a ser 5.

Explica o que devia ter acontecido à ficha e escreve, por palavras, o passo que falta entre verificar o pedido e mostrar a mensagem. Depois relaciona a tua resposta com o primeiro programa da secção 6: que parte da linha `quantidade_caderno = retirar(quantidade_caderno, 2)` produziria o mesmo erro se fosse esquecida? Justifica.

### Exercício 5: Variáveis soltas e nomes cuidadosos

Volta ao programa com o caderno e a pasta, na secção 6. Imagina que o inventário passa a ter três artigos, A01, A02 e A03, escritos da mesma maneira, e responde por escrito.

1. Quantas variáveis são precisas para guardar os três artigos? E para quarenta artigos? Mostra a conta.
2. Um colega diz: "O engano da secção 6 resolve-se escolhendo nomes de variáveis com mais cuidado." Concordas? Na tua resposta, explica o que é que o programa sabe e o que é que só a pessoa que o escreveu sabe.

### Exercício 6: Uma ficha tua

Escolhe um material interno fictício e cria a sua ficha, com código, nome e quantidade inicial. Não acrescentes outros campos.

Escreve uma sequência de três pedidos sobre essa ficha, a começar na quantidade inicial que escolheste, de forma que um pedido seja aceite, outro seja recusado, e um deles deixe a quantidade em zero. Vais ter de planear a ordem e os números antes de escrever o traço. Apresenta a sequência como um traço, com as colunas do exemplo guiado.

Por baixo do traço, explica a diferença entre aquilo que escolheste guardar na ficha e aquilo que escolheste fazer com esses dados.

## Antes de passares ao caderno 2

Tenta responder a estas perguntas sem olhar para o texto. Se alguma te deixar com dúvidas, volta à secção indicada.

- Consegues explicar porque é que uma ficha com quantidade 6 não corresponde a seis fichas? (secção 1)
- Consegues dar um exemplo de uma coisa real que não seria uma entidade no inventário da sala, e dizer porquê? (secção 2)
- Consegues mostrar, com uma tabela antes e depois, que mudar o estado não muda a identidade do artigo? (secção 3)
- Consegues dizer por que razão "retirar 6" com 6 unidades é aceite e "retirar 0" é recusado? (secção 5)
- Consegues explicar, com o engano da pasta, porque é que as variáveis soltas tornam um programa frágil? (secção 6)

![Rodapé](../imagens/rodape.png)

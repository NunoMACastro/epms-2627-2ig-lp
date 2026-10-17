![Cabeçalho](../imagens/cabecalho.png)

# Entidades, estado e ações

Módulo M10, Introdução à Programação Orientada por Objetos. Este guia explica como se escolhe a informação que um programa guarda sobre uma coisa, e as ações que lhe podemos pedir. É o caminho dos materiais de uma sala aos dados de um programa. Lês ao teu ritmo, e o que não acabares na aula acabas em casa ou na aula seguinte. Para praticar, há o [laboratório](01-entidades-estado-acoes-laboratorio.md) e a [ficha de exercícios](01-entidades-estado-acoes-exercicios.md) deste tema.

Imagina que és responsável pelos materiais de uma sala de aula. No armário há cadernos, pastas e canetas. Durante a semana, algumas unidades são usadas e saem do armário; outras chegam numa encomenda e são arrumadas. Quando alguém te pergunta "ainda temos pastas?", precisas de uma forma de responder sem abrir o armário e contar tudo outra vez.

A solução mais antiga é uma folha de registo, com uma linha por material e o número de unidades que existem. A solução que vamos construir ao longo deste módulo é um programa que mantém esse registo por nós. Antes de escrever qualquer programa, porém, temos de tomar duas decisões. Que informação precisamos de guardar? E que operações fazem sentido sobre essa informação? Este guia trata dessas duas decisões.

Quase todo o guia se faz em papel. Os programas em Python aparecem só na secção "Duas maneiras de organizar um programa", para comparar duas maneiras de organizar o mesmo programa. Usam apenas instruções básicas (variáveis, uma função, uma condição e `print`), e cada linha é explicada. Este tema ainda não escreve objetos em Python: isso começa no tema 02.

## Neste guia

1. O que vais aprender
2. O que já sabes e vais usar
3. A informação que interessa guardar
4. Entidade: aquilo que escolhemos representar
5. Estado: como está a informação neste momento
6. Comportamento: o que podemos pedir que aconteça
7. Uma operação tem de respeitar regras
8. Duas maneiras de organizar um programa
9. Exemplo guiado: seguir os valores passo a passo
10. Erros frequentes
11. Palavras novas deste guia
12. Verificar o que aprendeste
13. O que vem a seguir

## O que vais aprender

No fim deste guia, consegues:

- escolher a informação que um programa precisa de guardar sobre uma coisa, e dizer porque é que o resto fica de fora;
- reconhecer as entidades de um problema, a partir das perguntas a que o programa tem de responder;
- distinguir o estado de uma entidade das operações que lhe podemos pedir, e as operações que só leem das que mudam o estado;
- aplicar as regras do inventário a um pedido e seguir os valores passo a passo, numa tabela;
- explicar, com um programa em Python, porque é que guardar cada artigo em variáveis soltas torna um programa frágil;
- dizer o que a programação orientada a objetos muda em relação à programação estruturada.

## O que já sabes e vais usar

- As variáveis e a atribuição com `=`, que guarda um valor com um nome, do 10.º ano.
- As funções com `def`, os parâmetros e o `return`, do 10.º ano.
- As condições com `if`, as comparações, como `>` e `<=`, e o `and`, do 10.º ano.
- O texto entre aspas, como `"Caderno"`, e os números, do 10.º ano.
- Os comentários, as linhas que começam por `#`, que o Python não executa, do 10.º ano.
- O `print`, que mostra valores no ecrã, também vários de uma vez, separados por vírgulas, do 10.º ano.
- Copiar um programa para um ficheiro `.py`, guardá-lo e executá-lo no editor de Python das aulas, do 10.º ano.

Se alguma destas bases estiver menos firme, há duas ajudas para fazeres por tua conta, sem entrega. O [diagnóstico de programação](../avaliacoes/diagnostico-inicial.md) é uma revisão opcional do 10.º ano. Serve para perceberes de que te recordas e onde precisas de apoio. Podes responder por palavras, desenhos, contas ou pseudocódigo, e não tens de conhecer nenhuma linguagem em particular. A [ficha de recuperação](bridge-raciocinio.md) é curta e serve para recuperar uma ideia de que vais precisar. Por exemplo, seguir os valores de uma variável ao longo de um programa, ou ler uma condição.

## A informação que interessa guardar

Uma ficha de material pode ter este aspeto:

| Informação | O que guardámos |
| --- | --- |
| Código | A01 |
| Nome | Caderno |
| Quantidade | 6 |

Cada linha desta ficha responde a uma pergunta diferente. Vamos ver porque é que precisamos das três.

O **código** identifica o material. À primeira vista parece repetir o nome, mas não repete. Dois materiais podem ter nomes parecidos, como "Caderno" e "Caderno quadriculado". E a mesma pessoa pode escrever o nome de maneiras diferentes em dias diferentes: "caderno", "Caderno", "Cadernos". O código é curto, é escolhido uma vez e não se repete: não há dois materiais com o código A01. Quando um valor não se repete e permite distinguir cada coisa de todas as outras, dizemos que **identifica** essa coisa. Na escola passa-se o mesmo contigo: além do nome, tens um número de aluno. Pode haver dois alunos com o mesmo nome, mas não há dois com o mesmo número.

O **nome** descreve o material a quem lê a ficha. O código A01 não diz nada a uma pessoa que abre o armário; a palavra "Caderno" diz. O nome serve as pessoas, e o código serve a identificação.

A **quantidade** diz quantas unidades desse material existem neste momento. É a informação que mais vai mudar, porque muda sempre que alguém usa ou arruma material.

No nosso inventário, chamamos **artigo** a cada referência de material, isto é, a cada linha do registo. A ficha A01 representa o artigo "Caderno", do qual há seis unidades. Repara no que isto significa: não temos seis fichas, uma por caderno físico. Temos uma ficha, e o número 6 está escrito dentro dela. Se amanhã chegarem mais quatro cadernos, não criamos quatro fichas novas. Mudamos o 6 para 10 na ficha que já existe.

Esta é uma escolha de **representação**, feita a pensar no problema. Imagina que querias acompanhar cada computador portátil da escola, um a um, com o seu número de série e o nome de quem o requisitou. Aí precisarias de uma ficha por equipamento. Para cadernos e canetas isso não faz sentido: ninguém quer saber qual dos seis cadernos foi usado, só quantos restam. Representar um problema é sempre escolher o que interessa e deixar de fora o resto.

Cada ficha tem ainda de cumprir regras para fazer sentido: o código não se repete, o nome está preenchido e a quantidade é um número inteiro que não é negativo. Vamos voltar a estas regras com calma, na secção "Uma operação tem de respeitar regras".

## Entidade: aquilo que escolhemos representar

Ao analisar um problema, procuramos as coisas ou as ideias sobre as quais precisamos de guardar informação. Chamamos **entidade** a cada uma dessas coisas relevantes para o problema.

No inventário da sala, um artigo é uma entidade: precisamos de saber o seu código, o seu nome e a sua quantidade. A parede da sala também existe, e o quadro também, mas não precisamos de os representar para controlar os materiais do armário. Existir no mundo real não chega para uma coisa entrar no programa. Tem de ser relevante para o que queremos resolver.

Também se podem representar ideias em que não se consegue tocar, como uma reserva de sala, uma tarefa por fazer ou uma encomenda. Uma encomenda não é um objeto físico: é um pedido que alguém fez e que outra pessoa vai entregar. Mesmo assim, tem informação própria, como a data em que foi feita e o que foi pedido. Por isso, "entidade" não quer dizer "algo em que conseguimos tocar". Quer dizer "algo sobre o qual o programa precisa de guardar informação".

Pensa noutro problema para confirmares a ideia. Num programa de gestão da biblioteca da escola, as entidades seriam provavelmente os livros, os leitores e os empréstimos. As estantes só seriam uma entidade se o programa precisasse de dizer em que estante está cada livro. A mesma coisa real pode ser entidade num problema e não ser noutro, porque o que decide é a pergunta a que o programa tem de responder.

Ao longo deste módulo vamos concentrar-nos em duas entidades, os artigos e o inventário que os reúne.

## Estado: como está a informação neste momento

A ficha A01 diz que há 6 cadernos. Depois de alguém retirar 2, a quantidade deve passar a 4.

Chamamos **estado** ao conjunto dos valores de uma entidade num certo momento. O estado funciona como uma fotografia: mostra como as coisas estão agora, e daqui a cinco minutos a fotografia pode ser outra. Podemos comparar o estado antes e depois de uma operação:

| Informação | Antes de retirar | Depois de retirar 2 |
| --- | --- | --- |
| Código | A01 | A01 |
| Nome | Caderno | Caderno |
| Quantidade | 6 | 4 |

Olha para a tabela com atenção. O artigo continua a ser A01. Mudou a quantidade, mas não passámos a falar de outro material. O estado mudou e a **identidade** do artigo manteve-se: continua a ser o mesmo artigo, aquele que o código A01 identifica. Acontece o mesmo com o marcador de um jogo de futebol: ao intervalo está 1-0 e no fim está 2-1, mas o jogo é o mesmo. O marcador mostra o estado do jogo, e o jogo não passou a ser outro por o resultado ter mudado.

Esta distinção vai ser útil muitas vezes. Quando um programa não faz o que esperavas, uma das primeiras perguntas a fazer é esta: qual era o estado antes desta instrução, e qual é o estado depois? Se consegues responder às duas, consegues perceber o que a instrução fez de facto, e não apenas o que devia ter feito.

## Comportamento: o que podemos pedir que aconteça

Guardar dados não chega. Um inventário serve para ser consultado e atualizado, e isso exige operações. Para um artigo, faz sentido pedir três coisas: consultar a quantidade, para saber quantas unidades existem agora; adicionar unidades, quando chega material; e retirar unidades, quando o material é usado. A cada uma destas ações chamamos uma **operação**.

Chamamos **comportamento** ao conjunto de operações que podemos pedir a uma entidade. "Quantidade 6" é uma informação sobre o estado. "Retirar 2" é um pedido de operação. A primeira descreve como as coisas estão; a segunda pede que alguma coisa aconteça.

Consultar também é uma operação, mas não altera a quantidade. Se perguntas quantos cadernos existem e a resposta é 6, não passam a existir menos cadernos por teres feito a pergunta. É como olhar para um relógio: ver as horas não muda as horas. Dito assim parece óbvio, mas vai ser importante quando escrevermos código. Há operações que só leem o estado e operações que o mudam, e confundir as duas é a origem de muitos erros.

Nem todas as operações imagináveis fazem sentido. "Pintar o artigo de azul" não é uma operação do nosso inventário, porque não guardamos cores. As operações que escolhemos dependem da informação que escolhemos guardar, e as duas escolhas fazem-se em conjunto. Se decidirmos guardar uma informação que nenhuma operação usa, provavelmente não precisávamos dela. Se quisermos uma operação que precisa de uma informação que não guardamos, falta alguma coisa na ficha.

## Uma operação tem de respeitar regras

Podes retirar 2 unidades quando existem 6. Mas não podes retirar 9, porque não há unidades suficientes. Um programa que aceitasse esse pedido ficaria com -3 cadernos, um número que não corresponde a nada que exista no armário. O programa deve recusar o pedido e conservar a quantidade que existia.

Para saber quando aceitar e quando recusar, precisamos de regras escritas. Neste inventário adotamos estas três:

1. Cada código identifica um único artigo.
2. O nome do artigo está preenchido.
3. A quantidade é um número inteiro não negativo.

**Inteiro** significa sem parte decimal: 4 é inteiro, 4,5 não é. Não faz sentido ter quatro cadernos e meio no armário. **Não negativo** significa zero ou maior do que zero. Juntando as duas condições, as quantidades possíveis são 0, 1, 2, 3 e assim por diante.

Ter zero unidades é possível e é um estado válido: significa que o material esgotou. A ficha continua a existir, porque o material continua a fazer parte do inventário, e voltará a ter unidades quando chegar uma encomenda.

Há ainda uma regra para os pedidos, que é diferente da regra do estado. Um pedido para adicionar ou para retirar tem de ser um número inteiro **positivo**, isto é, 1 ou mais. Pedir para retirar zero unidades é recusado. Pode parecer estranho recusar um pedido que não faria mal nenhum. Mas um pedido de zero unidades não corresponde a nenhuma ação real, e quase sempre é um engano de quem o escreveu. Outros programas podem escolher outra regra. O importante é que a regra esteja escrita e que o programa a siga sempre.

As duas regras sobre o zero não se contradizem. Com 6 unidades, retirar 6 é aceite e deixa a quantidade em zero, que é um estado válido. Com 6 unidades, retirar 0 é recusado, porque o pedido não é válido. A pergunta "este estado é válido?" e a pergunta "este pedido é válido?" são perguntas diferentes, e cada uma tem a sua regra.

## Duas maneiras de organizar um programa

Até aqui trabalhámos em papel. Agora vamos ver como um programa em Python poderia guardar a ficha A01 e responder a pedidos. Vamos vê-lo de duas maneiras, porque a diferença entre elas é a razão de ser deste módulo.

Uma maneira de pensar e de organizar um programa chama-se um **paradigma de programação**. Um paradigma não é uma linguagem: a mesma linguagem, como o Python, permite escrever programas em mais do que um paradigma. É mais parecido com um critério de arrumação. Duas pessoas podem arrumar o mesmo armário por tipo de material ou por frequência de uso. O armário e os materiais são os mesmos, e o que muda é a lógica com que cada coisa é posta no seu lugar.

### A maneira habitual nos primeiros programas: programação estruturada

Nos primeiros programas que se aprendem a escrever, os dados ficam em variáveis e as operações são funções que recebem dados e devolvem resultados. O programa é uma sequência de passos, com condições e ciclos a decidir que passos se executam. Esta forma de organizar chama-se **programação estruturada**. Também se diz programação procedimental, porque o programa se organiza em procedimentos, isto é, em funções.

Aqui está a ficha A01 escrita dessa maneira, com dois pedidos: retirar 2 unidades e, a seguir, retirar 5. É um programa completo. Para o executares, copia-o para um ficheiro novo com a extensão `.py` (por exemplo, `inventario.py`) no editor de Python que usas nas aulas, e executa o ficheiro inteiro. Todos os programas completos deste guia funcionam com Python 3, a partir da versão 3.10.

Antes de correres este programa, tenta prever: o que mostram os dois `print`? Aplica as regras da secção anterior a cada pedido.

```python
# inventario.py: o artigo A01 e uma função que retira unidades de uma quantidade.


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

Leitura guiada: vamos ler o programa por partes, de cima para baixo.

A primeira linha é um comentário, que diz o que o ficheiro é. A parte seguinte define uma função. `def retirar(quantidade, unidades):` diz ao Python que, a partir dali, existe uma função chamada `retirar` que recebe dois valores: a quantidade que existe e as unidades que se querem retirar. As linhas indentadas por baixo (mais afastadas da margem) pertencem à função. Definir a função não a executa: só a prepara para ser usada mais tarde.

O texto entre três aspas, logo a seguir à linha do `def`, chama-se **docstring** (do inglês, texto de documentação). É uma explicação do que a função faz, escrita para pessoas. O Python não a executa como instrução, mas guarda-a, e alguns editores, como o VS Code, mostram-na quando passas o rato por cima do nome da função. Vamos escrever docstrings em todas as funções deste módulo, e no código novo que vais escrever nos guias seguintes, porque obrigam quem escreve a dizer o que o código promete.

A linha `if unidades > 0 and unidades <= quantidade:` junta as duas condições do pedido. `unidades > 0` pergunta se o pedido é positivo. `unidades <= quantidade` pergunta se o pedido é menor ou igual ao que existe, ou seja, se há unidades suficientes. A palavra `and` (em português, "e") exige que as duas perguntas tenham resposta verdadeira. Se tiverem, a função executa `return quantidade - unidades`. Calcula o que fica, devolve esse valor a quem a chamou e termina ali. Se alguma das perguntas tiver resposta falsa, a função salta para a última linha e devolve a quantidade que recebeu, sem mudanças.

A segunda parte é o programa principal. As três primeiras linhas guardam os dados do artigo A01 em três variáveis. A seguir vem a linha mais importante:

```python partial
quantidade_caderno = retirar(quantidade_caderno, 2)
```

Esta linha repete uma linha do programa acima e não corre sozinha, porque depende da função e da variável definidas antes. Lê-se da direita para a esquerda. Primeiro o Python chama a função com os valores 6 e 2. A função verifica o pedido e devolve 4. Só depois a atribuição guarda esse 4 na variável `quantidade_caderno`. Repara que a função, por si só, não muda a variável: recebe um número e devolve outro. Quem muda a variável é a atribuição. Se escrevêssemos só `retirar(quantidade_caderno, 2)`, sem o `quantidade_caderno =` à esquerda, o 4 seria calculado e perdido, e a variável continuaria com 6.

Na segunda chamada, a função recebe 4 e 5. Como 5 é maior do que 4, a condição é falsa e a função devolve o 4 que recebeu. O programa mostra `Caderno 4` duas vezes, exatamente como as regras mandam. Depois de retirar 2 ficaram 4, e o pedido de 5 foi recusado sem mexer na quantidade.

Este programa tem duas limitações, que vamos resolver mais à frente, no guia 03. A primeira é que quem chama a função não fica a saber que o pedido foi recusado: recebe um número e mais nada. A segunda é que a função não verifica se o pedido é inteiro, e aceitaria retirar 1.5 unidades. Repara que o Python escreve os números com parte decimal com um ponto, `1.5`, onde em português escrevemos 1,5.

### O problema das variáveis soltas

Agora acrescentamos o artigo A02, "Pasta", com 2 unidades, e cometemos um engano pequeno, do género que acontece a toda a gente. O programa é completo e pode ser executado sozinho.

Antes de correres este programa, tenta prever o que mostram os dois `print`. Segue os valores que cada linha usa de facto, e não o que o comentário diz que queríamos fazer.

```python
# inventario.py: o caderno e a pasta, cada um guardado em três variáveis soltas.


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

Leitura guiada: a pasta tinha 2 unidades. Pedimos para retirar 1 e ficou com 5. O Python não se queixou, porque para o Python `quantidade_caderno` e `quantidade_pasta` são apenas dois números guardados com dois nomes diferentes. A função recebeu 6 e 1 e fez a conta 6 - 1. A atribuição guardou o resultado na variável da pasta. Cada instrução, isoladamente, fez exatamente o que estava escrito.

O problema está noutro lado. A ligação entre `codigo_pasta`, `nome_pasta` e `quantidade_pasta` só existe na nossa cabeça, através dos nomes que escolhemos para as variáveis. O programa não sabe que aquelas três variáveis descrevem o mesmo artigo, nem que `quantidade_caderno` pertence a outro. E a função `retirar` não sabe nada sobre artigos: recebe dois números e devolve um terceiro. A cada uma destas variáveis, que guardam um pedaço de um artigo sem nada que as ligue às outras, chamamos aqui **variáveis soltas**.

Com dois artigos precisamos de seis variáveis. Com cinquenta artigos precisaríamos de cento e cinquenta. E cada chamada teria de receber a variável certa, escrita à mão, sem que nada no programa ajudasse a detetar a troca.

### A outra maneira: programação orientada a objetos

Na **programação orientada a objetos** juntamos numa só unidade o código, o nome e a quantidade de um artigo, e ligamos a essa unidade as operações que lhe dizem respeito. Também se diz programação orientada por objetos, como no nome oficial deste módulo, e abrevia-se POO. Em vez de dizermos "chama a função retirar com a quantidade do caderno", passamos a dizer "pede ao caderno que retire 2". O artigo guarda os seus próprios dados e sabe realizar as suas próprias operações. A troca deste programa deixa de acontecer, porque cada artigo só mexe na sua quantidade. Continua a ser possível pedir ao artigo errado, mas o engano fica à vista, no nome do artigo a quem se pede.

Essa unidade chama-se **objeto**, e é o assunto do próximo guia. O que interessa agora é perceber que as ideias deste guia têm um nome próprio em POO:

| Ideia deste guia | Nome em programação orientada a objetos | Onde a vais estudar |
| --- | --- | --- |
| Entidade, como o artigo | Objeto | Guia 02 |
| Estado: código, nome e quantidade | Atributos do objeto, os valores que ele guarda | Guia 02 |
| Comportamento: consultar, adicionar, retirar | Métodos do objeto, as operações que ele sabe fazer | Guias 02 e 03 |
| Regras: quantidade inteira não negativa | Proteção do estado do objeto | Guia 03 |

A programação orientada a objetos não deita fora o que já sabes. Continuamos a usar variáveis, condições, ciclos e funções, e muitos deles passam a estar arrumados junto dos dados a que dizem respeito. A programação estruturada também não está errada: para um cálculo pequeno, uma função solta é muitas vezes a solução mais simples. A POO ajuda quando há muitas entidades, cada uma com o seu estado e as suas regras, que é precisamente o caso de um inventário.

## Exemplo guiado: seguir os valores passo a passo

O problema: o artigo A01 tem 6 unidades e recebe três pedidos, por esta ordem: consultar a quantidade, retirar 2 e retirar 5. Queremos saber, depois de cada pedido, o que aconteceu e com quantas unidades ficou a ficha. Em cada passo aplicamos as regras antes de mexer na ficha.

Antes de leres a tabela, faz tu o traço no papel, com uma linha por pedido. Em cada linha, escreve o que acontece, com a regra que verificaste, e com quantas unidades fica a ficha. Depois compara com a tabela.

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

O resultado: a ficha acaba com 4 unidades, e o único pedido recusado é o último. Uma tabela como esta chama-se um **traço**: um registo do que acontece em cada passo de uma sequência de instruções. Serve para explicar um programa a outra pessoa. Serve, sobretudo, para encontrar erros, porque obriga a olhar para o estado depois de cada instrução, em vez de olhar só para o resultado final.

Para confirmar o traço, compara-o com o primeiro programa da secção "Duas maneiras de organizar um programa", que faz os pedidos dos passos 2 e 3 ao mesmo artigo. O programa mostra `Caderno 4` duas vezes: são as quantidades da coluna da direita nesses dois passos. O ponto de partida, as 6 unidades, está na linha `quantidade_caderno = 6`.

## Erros frequentes

### Querer representar tudo o que se vê

O que se vê: uma ficha com informação que nenhuma pergunta do programa usa, como a cor das paredes da sala ou a cor de um caderno. Porque acontece: quem começa quer representar tudo o que existe na situação. Mas um programa que guarda a cor das paredes da sala não fica melhor por isso. Fica mais difícil de escrever e de corrigir, sem responder a nenhuma pergunta nova. Como se corrige: para cada informação, pergunta a que pergunta do programa responde, e que operação a usa. Se a resposta for "nenhuma", tira-a da ficha.

### Criar um artigo novo quando a quantidade muda

O que se vê: depois de um pedido, uma linha nova no registo para o mesmo material, como "A01, Caderno, 4" por baixo de "A01, Caderno, 6". Porque acontece: confunde-se a mudança de estado com uma coisa nova. Se aparecesse um artigo novo cada vez que alguém retira material, ao fim de um mês a folha de registo teria dezenas de linhas para o mesmo caderno. E ninguém saberia qual delas estava certa. Como se corrige: muda o valor na ficha que já existe. O código continua a identificar o mesmo artigo, e só a quantidade muda.

### Copiar só uma parte de um programa

O que se vê: ao executar, aparece uma mensagem como `NameError: name 'retirar' is not defined`. `NameError` quer dizer erro de nome, e o resto da mensagem, em inglês, diz que o nome `retirar` não está definido. Porque acontece: a linha usa uma função ou uma variável que só existe nas linhas de cima do programa, e essas linhas não foram copiadas. Também acontece quando a função fica escrita depois das linhas que a usam. Como se corrige: copia o programa completo, com a função no início, antes de todas as chamadas. Os blocos que o guia apresenta como "não corre sozinha" servem para ler, e não para executar à parte.

## Palavras novas deste guia

- Identificar: distinguir uma coisa de todas as outras, com um valor que não se repete, como o código A01 ou o número de aluno.
- Artigo: cada referência de material do inventário, isto é, cada linha do registo, com o código, o nome e a quantidade.
- Representação: a escolha do que um programa guarda sobre um problema, e do que deixa de fora.
- Entidade: uma coisa ou uma ideia sobre a qual o programa precisa de guardar informação, como um artigo ou uma encomenda.
- Estado: o conjunto dos valores de uma entidade num certo momento, como uma fotografia.
- Identidade: o que faz de um artigo o mesmo artigo, mesmo quando o estado muda; no inventário, é o código que a mostra.
- Operação: uma ação que podemos pedir a uma entidade, como consultar, adicionar ou retirar.
- Comportamento: o conjunto das operações que podemos pedir a uma entidade.
- Inteiro: um número sem parte decimal, como 4; 4,5 não é inteiro.
- Não negativo: zero ou maior do que zero.
- Positivo: maior do que zero, isto é, 1 ou mais, num número inteiro.
- Traço: a tabela que regista o que acontece em cada passo de uma sequência de instruções, com o estado depois de cada um.
- Paradigma de programação: uma maneira de pensar e de organizar um programa; não é uma linguagem.
- Programação estruturada: a maneira de organizar em que os dados ficam em variáveis e as operações são funções; também se diz procedimental.
- Docstring (do inglês, texto de documentação): o texto entre três aspas logo a seguir ao `def`, que explica a pessoas o que a função faz.
- Variáveis soltas: variáveis que guardam pedaços do mesmo artigo sem nada no programa que as ligue umas às outras.
- Programação orientada a objetos (POO): a maneira de organizar em que os dados de cada entidade e as operações sobre eles ficam juntos, numa só unidade.
- Objeto: a unidade que junta os dados de uma entidade e as operações que lhe dizem respeito; é o assunto do guia 02.

## Verificar o que aprendeste

1. Porque é que uma ficha com a quantidade 6 não corresponde a seis fichas?
2. Dá um exemplo de uma coisa real que não seria uma entidade no inventário da sala, e diz porquê.
3. A pasta A02 tem 2 unidades, e chegam mais 3. Com uma tabela de antes e depois, mostra que mudar o estado da pasta não muda a sua identidade.
4. A ficha A02 tem o nome "Pasta" e a quantidade 3. Lê estas expressões: "A02", "Pasta", "quantidade 3", "consultar a quantidade", "retirar 1", "adicionar 4" e "a quantidade passou a 2". Faz duas colunas, "informação guardada na ficha" e "operação que podemos pedir", e põe cada expressão na coluna certa. Uma das expressões é mais difícil de classificar do que as outras. Qual é, e porque a puseste na coluna que escolheste?
5. Porque é que "retirar 6", com 6 unidades, é aceite, e "retirar 0" é recusado?
6. Um programa tem uma ficha com 5 unidades. Recebe um pedido para retirar 2, verifica que o pedido é possível e mostra a mensagem "Pedido aceite". Mas, quando consultamos a quantidade logo a seguir, a resposta continua a ser 5. O que devia ter acontecido à ficha, e que passo falta entre verificar o pedido e mostrar a mensagem? Na linha `quantidade_caderno = retirar(quantidade_caderno, 2)`, que parte produziria o mesmo erro se fosse esquecida?
7. Com o engano da pasta, explica porque é que as variáveis soltas tornam um programa frágil.
8. Um colega diz: "O engano da pasta resolve-se escolhendo nomes de variáveis com mais cuidado." Concordas? Na resposta, diz o que é que o programa sabe e o que é que só a pessoa que o escreveu sabe.

## O que vem a seguir

Para praticar este tema, faz o [laboratório](01-entidades-estado-acoes-laboratorio.md) e depois a [ficha de exercícios](01-entidades-estado-acoes-exercicios.md). O tema seguinte é [Objetos, classes e instâncias](02-objetos-classes-instancias.md): o Python passa a juntar os dados e as operações de um artigo num objeto.

![Rodapé](../imagens/rodape.png)

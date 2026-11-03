![Cabeçalho](../imagens/cabecalho.png)

# Temas para treinar em casa

Estes seis temas servem para treinares em casa o que vais fazer no [livro de receitas](README.md). São opcionais e não contam para a nota.

Escolhe um tema e escreve o programa em Python, com classes, como nos guias do M10. Cada tema tem três classes: a do registo, a da variante, que tem tudo o que o registo tem e mais um dado, e a da coleção que os junta. O enunciado de cada tema diz o nome das três.

No fim do programa, escreve algumas linhas que experimentem cada operação e cada recusa e que mostrem a lista, para veres se tudo funciona. Quando acabares, compara o teu programa com as [resoluções](temas-de-treino-resolucoes.md).

## Coleção de jogos

Queremos um programa para registar os jogos que tens e quantas horas jogaste em cada um. Para cada jogo, guardamos um código, um título e as horas jogadas. O código não se pode repetir, o título não pode ficar vazio, e as horas são um número inteiro, 0 ou mais: um jogo acabado de comprar tem 0 horas.

Por exemplo:

| Código | Título | Horas jogadas |
| --- | --- | ---: |
| J01 | Corrida Rápida | 12 |
| J03 | Torre de Blocos | 0 |

Um jogo pode ser multijogador. Um jogo multijogador tem tudo o que um jogo tem e também o número máximo de jogadores, que é um número inteiro de 2 a 100. Por exemplo, o J02, Arena dos Heróis, com 30 horas jogadas, é para até 8 jogadores.

As três classes são o jogo, o jogo multijogador e a coleção de jogos.

Quando se vê a lista, os jogos aparecem assim:

```text
J01 Corrida Rápida, 12 horas
J02 Arena dos Heróis, 30 horas, até 8 jogadores
J03 Torre de Blocos, 0 horas
```

Deves poder:

- acrescentar um jogo, simples ou multijogador;
- ver a lista dos jogos;
- somar a um jogo as horas de uma sessão de jogo;
- ver só os jogos com mais de 10 horas.

O programa recusa:

- um código que já existe;
- um título vazio;
- horas que não sejam um número inteiro, 0 ou mais, tanto nas horas de um jogo como nas de uma sessão;
- um número de jogadores que não seja um número inteiro de 2 a 100.

Quando recusa, mostra uma mensagem a dizer porquê, e nada muda.

## Cartas colecionáveis

Queremos um programa para gerir uma coleção de cartas colecionáveis. Para cada carta, guardamos um código, um nome e a raridade, de 1, a mais comum, a 5, a mais rara. O código não se pode repetir, o nome não pode ficar vazio, e a raridade é um número inteiro de 1 a 5.

Por exemplo:

| Código | Nome | Raridade |
| --- | --- | ---: |
| C001 | Lobo da Neve | 3 |
| C003 | Rato do Celeiro | 1 |

Uma carta pode ser de edição limitada. Uma carta de edição limitada tem tudo o que uma carta tem e também o número de cópias que se fizeram dela. As cópias são um número inteiro de 1 a 1000. Por exemplo, a C002, Dragão Dourado, de raridade 5, teve uma edição de 250 cópias.

As três classes são a carta, a carta de edição limitada e a coleção de cartas.

Quando se vê a lista, as cartas aparecem assim:

```text
C001 Lobo da Neve, raridade 3
C002 Dragão Dourado, raridade 5, edição de 250 cópias
C003 Rato do Celeiro, raridade 1
```

Deves poder:

- acrescentar uma carta, simples ou de edição limitada;
- ver a lista das cartas;
- corrigir a raridade de uma carta;
- ver só as cartas de raridade 4 ou mais.

O programa recusa:

- um código que já existe;
- um nome vazio;
- uma raridade que não seja um número inteiro de 1 a 5, tanto ao acrescentar como ao corrigir;
- um número de cópias que não seja um número inteiro de 1 a 1000.

Quando recusa, mostra uma mensagem a dizer porquê, e nada muda.

## Diário de treinos

Queremos um programa para registar os treinos que fazes e quanto tempo durou cada um. Para cada treino, guardamos um código, a atividade e a duração, em minutos. O código não se pode repetir, a atividade não pode ficar vazia, e a duração é um número inteiro maior do que 0.

Por exemplo:

| Código | Atividade | Duração, em minutos |
| --- | --- | ---: |
| T01 | Ginásio | 45 |
| T03 | Natação | 40 |

Um treino pode ter distância, como uma corrida ou um passeio de bicicleta. Um treino com distância tem tudo o que um treino tem e também a distância percorrida, em metros, que é um número inteiro maior do que 0. Por exemplo, o T02, Corrida, durou 30 minutos, e foram 5000 metros.

As três classes são o treino, o treino com distância e o diário de treinos.

Quando se vê a lista, os treinos aparecem assim:

```text
T01 Ginásio, 45 minutos
T02 Corrida, 30 minutos, 5000 metros
T03 Natação, 40 minutos
```

Deves poder:

- acrescentar um treino, simples ou com distância;
- ver a lista dos treinos;
- corrigir a duração de um treino;
- ver só os treinos de mais de 30 minutos.

O programa recusa:

- um código que já existe;
- uma atividade vazia;
- uma duração que não seja um número inteiro maior do que 0, tanto ao acrescentar como ao corrigir;
- uma distância que não seja um número inteiro maior do que 0.

Quando recusa, mostra uma mensagem a dizer porquê, e nada muda.

## Playlist

Queremos um programa para fazer uma playlist: uma lista de músicas, com a duração de cada uma em segundos. Uma música de 3 minutos e 20 segundos tem 200 segundos. Para cada música, guardamos um código, um título e a duração. O código não se pode repetir na playlist, o título não pode ficar vazio, e a duração é um número inteiro de segundos maior do que 0.

Por exemplo:

| Código | Título | Duração, em segundos |
| --- | --- | ---: |
| M01 | Noite de Verão | 200 |
| M03 | Chuva Miúda | 180 |

Uma música pode ser de um álbum. Uma música de um álbum tem tudo o que uma música tem e também o número da faixa no álbum, que é um número inteiro de 1 a 30. Por exemplo, a M02, Tempestade, com 245 segundos, é a faixa 3 do seu álbum.

As três classes são a música, a música de um álbum e a playlist.

Quando se vê a lista, as músicas aparecem assim:

```text
M01 Noite de Verão, 200 segundos
M02 Tempestade, 245 segundos, faixa 3
M03 Chuva Miúda, 180 segundos
```

Deves poder:

- acrescentar uma música, solta ou de um álbum;
- ver a lista das músicas;
- corrigir a duração de uma música;
- ver só as músicas com mais de 4 minutos, ou seja, mais de 240 segundos.

O programa recusa:

- um código que já existe na playlist;
- um título vazio;
- uma duração que não seja um número inteiro maior do que 0, tanto ao acrescentar como ao corrigir;
- uma faixa que não seja um número inteiro de 1 a 30.

Quando recusa, mostra uma mensagem a dizer porquê, e nada muda.

## Campeonato

Queremos um programa para gerir as equipas de um campeonato inventado por ti e os pontos de cada uma. Para cada equipa, guardamos uma sigla, um nome e os pontos. A sigla não se pode repetir, o nome não pode ficar vazio, e os pontos são um número inteiro, 0 ou mais.

Por exemplo:

| Sigla | Nome | Pontos |
| --- | --- | ---: |
| LBO | Leões do Bairro | 12 |
| TVE | Tubarões do Vale | 0 |

Uma equipa pode ter estádio. Uma equipa com estádio tem tudo o que uma equipa tem e também o número de lugares do estádio, que é um número inteiro de 500 a 90 000. Por exemplo, a ACR, Águias da Ribeira, com 9 pontos, tem um estádio de 5000 lugares.

As três classes são a equipa, a equipa com estádio e o campeonato.

Quando se vê a lista, as equipas aparecem assim:

```text
LBO Leões do Bairro, 12 pontos
ACR Águias da Ribeira, 9 pontos, estádio de 5000 lugares
TVE Tubarões do Vale, 0 pontos
```

Deves poder:

- acrescentar uma equipa, com ou sem estádio;
- ver a lista das equipas;
- somar a uma equipa os pontos que ganhou num jogo;
- ver só as equipas com 10 pontos ou mais.

O programa recusa:

- uma sigla que já existe;
- um nome vazio;
- pontos que não sejam um número inteiro, 0 ou mais, tanto nos pontos de uma equipa como nos ganhos num jogo;
- um número de lugares que não seja um número inteiro de 500 a 90 000.

Quando recusa, mostra uma mensagem a dizer porquê, e nada muda.

## Apps do telemóvel

Queremos um programa para gerir as apps instaladas num telemóvel. Para cada app, guardamos um código, um nome e o tamanho, em MB. O código não se pode repetir, o nome não pode ficar vazio, e o tamanho é um número inteiro de 1 a 4000.

Por exemplo:

| Código | Nome | Tamanho, em MB |
| --- | --- | ---: |
| A01 | Mensagens | 150 |
| A03 | Mapas | 1200 |

Uma app pode ser um jogo. Um jogo tem tudo o que uma app tem e também a idade mínima para jogar, que tem de ser uma destas: 3, 7, 12, 16 ou 18 anos. Por exemplo, o A02, Corrida na Cidade, com 300 MB, é para jogadores a partir dos 7 anos.

As três classes são a app, o jogo e o telemóvel.

Quando se vê a lista, as apps aparecem assim:

```text
A01 Mensagens, 150 MB
A02 Corrida na Cidade, 300 MB, a partir dos 7 anos
A03 Mapas, 1200 MB
```

Deves poder:

- instalar uma app, simples ou jogo;
- ver a lista das apps;
- atualizar uma app, ou seja, mudar o tamanho dela para o novo valor;
- ver só as apps que ocupam mais de 1000 MB.

O programa recusa:

- um código que já existe;
- um nome vazio;
- um tamanho que não seja um número inteiro de 1 a 4000, tanto ao instalar como ao atualizar;
- uma idade mínima que não seja 3, 7, 12, 16 ou 18.

Quando recusa, mostra uma mensagem a dizer porquê, e nada muda.

![Rodapé](../imagens/rodape.png)

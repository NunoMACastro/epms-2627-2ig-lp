![Cabeçalho](../imagens/cabecalho.png)

# Temas para treinar em casa

Estes cinco temas servem para treinares em casa o que vais fazer no [livro de receitas](README.md). São opcionais e não contam para a nota.

Cada tema tem a mesma estrutura do livro de receitas: um registo, uma variante desse registo, com um dado a mais, e a coleção que os reúne. Escolhe um tema e faz o modelo, como no livro de receitas:

1. a classe do registo: o que guarda, com que valores se cria e o que se lhe pode pedir;
2. a classe da variante, da mesma maneira, e o que tem de diferente do registo;
3. a classe da coleção, da mesma maneira;
4. as relações entre as classes: para cada par, a frase "tem" ou "é um", e, numa relação "tem", se é uma composição ou uma agregação;
5. as regras dos números, por palavras, com os limites bem claros;
6. dois registos que cumprem as regras, um deles da variante;
7. uma alteração que é aceite e outra que é recusada, cada uma com o que acontece aos dados.

## Coleção de jogos

Registas os jogos que tens e quantas horas jogaste cada um. As três classes são o jogo, o jogo multijogador e a coleção de jogos.

| Dado | Exemplo | Regra |
| --- | --- | --- |
| Código | J01 | não se pode repetir |
| Título | Corrida Rápida | não pode ficar vazio |
| Horas jogadas | 12 | número inteiro, 0 ou mais |

Um jogo multijogador tem tudo o que um jogo tem e também o número máximo de jogadores:

| Dado | Exemplo | Regra |
| --- | --- | --- |
| Jogadores, no máximo | 8 | número inteiro de 2 a 100 |

Na lista, cada jogo aparece assim:

```text
J01 Corrida Rápida, 12 horas
J02 Arena dos Heróis, 30 horas, até 8 jogadores
```

Na aplicação, podes:

- acrescentar um jogo, simples ou multijogador;
- ver a lista dos jogos;
- somar as horas de uma sessão de jogo;
- ver só os jogos com mais de 10 horas.

A aplicação recusa:

- um código que já existe;
- um título vazio;
- horas que não sejam um número inteiro, 0 ou mais;
- um número de jogadores que não seja um número inteiro de 2 a 100.

## Cartas colecionáveis

Registas as cartas de uma coleção e a raridade de cada uma, de 1, a mais comum, a 5, a mais rara. As três classes são a carta, a carta de edição limitada e a coleção de cartas.

| Dado | Exemplo | Regra |
| --- | --- | --- |
| Código | C001 | não se pode repetir |
| Nome | Lobo da Neve | não pode ficar vazio |
| Raridade | 3 | número inteiro de 1 a 5 |

Uma carta de edição limitada tem tudo o que uma carta tem e também o número de cópias que se fizeram dela:

| Dado | Exemplo | Regra |
| --- | --- | --- |
| Cópias da edição | 250 | número inteiro de 1 a 1000 |

Na lista, cada carta aparece assim:

```text
C001 Lobo da Neve, raridade 3
C002 Dragão Dourado, raridade 5, edição de 250 cópias
```

Na aplicação, podes:

- acrescentar uma carta, simples ou de edição limitada;
- ver a lista das cartas;
- corrigir a raridade de uma carta;
- ver só as cartas de raridade 4 ou mais.

A aplicação recusa:

- um código que já existe;
- um nome vazio;
- uma raridade que não seja um número inteiro de 1 a 5;
- um número de cópias que não seja um número inteiro de 1 a 1000.

## Diário de treinos

Registas os treinos que fizeste e quanto tempo durou cada um. As três classes são o treino, o treino com distância e o diário de treinos.

| Dado | Exemplo | Regra |
| --- | --- | --- |
| Código | T01 | não se pode repetir |
| Atividade | Ginásio | não pode ficar vazia |
| Duração, em minutos | 45 | número inteiro maior do que 0 |

Um treino com distância, como uma corrida ou um passeio de bicicleta, tem tudo o que um treino tem e também a distância percorrida:

| Dado | Exemplo | Regra |
| --- | --- | --- |
| Distância, em metros | 5000 | número inteiro maior do que 0 |

Na lista, cada treino aparece assim:

```text
T01 Ginásio, 45 minutos
T02 Corrida, 30 minutos, 5000 metros
```

Na aplicação, podes:

- acrescentar um treino, simples ou com distância;
- ver a lista dos treinos;
- corrigir a duração de um treino;
- ver só os treinos de mais de 30 minutos.

A aplicação recusa:

- um código que já existe;
- uma atividade vazia;
- uma duração que não seja um número inteiro maior do que 0;
- uma distância que não seja um número inteiro maior do que 0.

## Playlist

Registas as músicas de uma lista e a duração de cada uma, em segundos: uma música de 3 minutos e 20 segundos tem 200 segundos. As três classes são a música, a música de um álbum e a playlist.

| Dado | Exemplo | Regra |
| --- | --- | --- |
| Código | M01 | não se pode repetir |
| Título | Noite de Verão | não pode ficar vazio |
| Duração, em segundos | 200 | número inteiro maior do que 0 |

Uma música de um álbum tem tudo o que uma música tem e também o número da faixa no álbum:

| Dado | Exemplo | Regra |
| --- | --- | --- |
| Faixa | 3 | número inteiro de 1 a 30 |

Na lista, cada música aparece assim:

```text
M01 Noite de Verão, 200 segundos
M02 Tempestade, 245 segundos, faixa 3
```

Na aplicação, podes:

- acrescentar uma música, solta ou de um álbum;
- ver a lista das músicas;
- corrigir a duração de uma música;
- ver só as músicas com mais de 4 minutos, ou seja, mais de 240 segundos.

A aplicação recusa:

- um código que já existe;
- um título vazio;
- uma duração que não seja um número inteiro maior do que 0;
- uma faixa que não seja um número inteiro de 1 a 30.

## Campeonato

Registas as equipas de um campeonato inventado por ti e os pontos de cada uma. As três classes são a equipa, a equipa com estádio e o campeonato.

| Dado | Exemplo | Regra |
| --- | --- | --- |
| Sigla | LBO | não se pode repetir |
| Nome | Leões do Bairro | não pode ficar vazio |
| Pontos | 12 | número inteiro, 0 ou mais |

Uma equipa com estádio tem tudo o que uma equipa tem e também o número de lugares do estádio:

| Dado | Exemplo | Regra |
| --- | --- | --- |
| Lugares do estádio | 5000 | número inteiro de 500 a 90 000 |

Na lista, cada equipa aparece assim:

```text
LBO Leões do Bairro, 12 pontos
ACR Águias da Ribeira, 9 pontos, estádio de 5000 lugares
```

Na aplicação, podes:

- acrescentar uma equipa, com ou sem estádio;
- ver a lista das equipas;
- somar os pontos ganhos num jogo;
- ver só as equipas com 10 pontos ou mais.

A aplicação recusa:

- uma sigla que já existe;
- um nome vazio;
- pontos que não sejam um número inteiro, 0 ou mais;
- um número de lugares que não seja um número inteiro de 500 a 90 000.

![Rodapé](../imagens/rodape.png)

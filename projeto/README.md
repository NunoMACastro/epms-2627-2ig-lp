![Cabeçalho](../imagens/cabecalho.png)

# O teu projeto: um livro de receitas

Vais construir uma aplicação: um livro de receitas, onde guardas receitas e o tempo que cada uma leva a preparar. Para já, ainda não programas. Fazes o modelo da aplicação, como aprendeste nos guias do M10: descreves por palavras as classes, os dados e as regras.

## O livro de receitas

Cada receita tem três dados:

| Dado | Exemplo | Regra |
| --- | --- | --- |
| Código | R01 | não se pode repetir |
| Nome | Sopa de legumes | não pode ficar vazio |
| Tempo de preparação, em minutos | 40 | número inteiro maior do que 0 |

Algumas receitas vão ao forno, como um bolo ou um assado. Uma receita de forno tem tudo o que uma receita tem e também a temperatura do forno:

| Dado | Exemplo | Regra |
| --- | --- | --- |
| Temperatura do forno, em graus | 180 | número inteiro de 100 a 250 |

Na lista, cada receita aparece com os seus dados. Uma receita de forno mostra também a temperatura:

```text
R01 Sopa de legumes, 40 minutos
R02 Bolo de laranja, 45 minutos, forno a 180 graus
```

Na aplicação, podes:

- acrescentar uma receita nova, simples ou de forno;
- ver a lista das receitas;
- corrigir o tempo de uma receita;
- ver só as receitas que se fazem em 30 minutos ou menos.

A aplicação recusa:

- um código que já existe;
- um nome vazio;
- um tempo que não seja um número inteiro maior do que 0;
- uma temperatura que não seja um número inteiro de 100 a 250.

Quando recusa, nada muda.

## O que tens de fazer agora: o modelo

O modelo tem três classes: a receita, a receita de forno e o livro de receitas. Descreve-as por palavras, como no guia [Composição e modelação](../01-programacao-orientada-objetos/04-composicao-modelacao.md):

1. a classe da receita: o que guarda, com que valores se cria e o que se lhe pode pedir;
2. a classe da receita de forno, da mesma maneira, e o que tem de diferente da receita;
3. a classe do livro de receitas, da mesma maneira;
4. as relações entre as classes: para cada par, a frase "tem" ou "é um", e, numa relação "tem", se é uma composição ou uma agregação;
5. a regra do tempo e a da temperatura, por palavras, com os limites bem claros;
6. duas receitas que cumprem as regras, uma delas de forno;
7. uma correção do tempo que é aceite e outra que é recusada, cada uma com o que acontece aos dados.

Entregas o modelo ao professor pelo meio que ele indicar.

O projeto continua no M11, com a primeira versão da aplicação no computador. Quando lá chegares, esta página diz-te o que fazer.

## Para treinares em casa

Se quiseres treinar, faz o modelo de um destes temas, com a classe do registo e a da coleção. É opcional e não conta para a nota.

| Tema | Cada registo | Número e regra |
| --- | --- | --- |
| Coleção de jogos | um jogo | horas jogadas, 0 ou mais |
| Cartas colecionáveis | uma carta | raridade, de 1 a 5 |
| Diário de treinos | um treino | minutos, mais de 0 |
| Playlist | uma música | duração em segundos, mais de 0 |
| Campeonato | uma equipa | pontos, 0 ou mais |

![Rodapé](../imagens/rodape.png)

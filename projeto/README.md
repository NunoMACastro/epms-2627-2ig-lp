![Cabeçalho](../imagens/cabecalho.png)

# O teu projeto: um livro de receitas

Vais construir uma aplicação: um livro de receitas.

## O livro de receitas

Queremos uma aplicação para guardar receitas e o tempo que cada uma leva a preparar. Para cada receita, guardamos um código, um nome e o tempo de preparação, em minutos. O código não se pode repetir, o nome não pode ficar vazio, e o tempo é um número inteiro maior do que 0. Uma receita que se prepara em 0 minutos não existe, por isso o tempo mais pequeno aceite é 1.

Por exemplo, a receita R01, Sopa de legumes, leva 40 minutos a preparar.

Algumas receitas vão ao forno, como um bolo ou um assado. Uma receita de forno tem tudo o que uma receita tem e também a temperatura do forno, em graus, que é um número inteiro de 100 a 250. A temperatura tem dois limites: 100 e 250 são aceites, 99 e 251 não são. Por exemplo, a R02, Bolo de laranja, leva 45 minutos, com o forno a 180 graus.

As três classes são a receita, a receita de forno e o livro de receitas.

Cada receita tem a sua descrição, e a de forno mostra também a temperatura. A lista pede a descrição a cada receita, sem perguntar se é de forno. Quando se vê a lista, as receitas aparecem assim:

```text
R01 Sopa de legumes, 40 minutos
R02 Bolo de laranja, 45 minutos, forno a 180 graus
```

Deves poder:

- acrescentar uma receita nova, simples ou de forno;
- ver a lista das receitas;
- corrigir o tempo de uma receita;
- ver só as receitas que se fazem em 30 minutos ou menos.

A aplicação recusa:

- um código que já existe;
- um nome vazio;
- um tempo que não seja um número inteiro maior do que 0, tanto ao acrescentar como ao corrigir;
- uma temperatura que não seja um número inteiro de 100 a 250.

Quando recusa, mostra uma mensagem a dizer porquê, e nada muda.

## O modelo, que fizeste no fim do M10

Na aula de 29 de outubro, fizeste o modelo do livro de receitas. Descreveste por palavras as três classes, como em [O inventário descrito por palavras](../01-programacao-orientada-objetos/04-composicao-modelacao.md#o-inventário-descrito-por-palavras), no guia 04. O modelo tinha sete partes:

1. a classe da receita: o que guarda, com que valores se cria e o que se lhe pode pedir;
2. a classe da receita de forno, da mesma maneira, e o que tem de diferente da receita;
3. a classe do livro de receitas, da mesma maneira;
4. as duas relações, entre a receita de forno e a receita e entre o livro e as receitas. Para cada uma, a frase "tem" ou "é um" e, na relação "tem", se é uma composição ou uma agregação, com as razões;
5. a regra do tempo e a da temperatura, por palavras, com os limites bem claros;
6. duas receitas que cumprem as regras, uma delas de forno;
7. uma correção do tempo que é aceite e outra que é recusada, cada uma com o que acontece aos dados.

A receita de forno descreve-se como a notificação assinada, em [Passo 2: o programa descrito por palavras](../01-programacao-orientada-objetos/05-heranca-polimorfismo.md#passo-2-o-programa-descrito-por-palavras), no guia 05. Entre o livro e as receitas, aceitam-se a composição e a agregação, quando a razão segue as perguntas de [Dois graus de "tem": composição e agregação](../01-programacao-orientada-objetos/04-composicao-modelacao.md#dois-graus-de-tem-composição-e-agregação), no guia 04.

O projeto continua no M11. No tema 08, Primeira versão do projeto, há um marco de acompanhamento, sem nota: mostras ao professor como vai o teu trabalho.

## Para treinares em casa

Se quiseres treinar em casa, tens seis [temas](temas-de-treino.md) para fazer em Python, como nos guias de [Programação orientada a objetos](../01-programacao-orientada-objetos/README.md). Têm a mesma estrutura do livro de receitas: jogos, cartas, o diário de treinos, músicas, equipas e apps. São opcionais e não contam para a nota.

![Rodapé](../imagens/rodape.png)

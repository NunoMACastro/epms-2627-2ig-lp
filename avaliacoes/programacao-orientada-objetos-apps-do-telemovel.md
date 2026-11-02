![Cabeçalho](../imagens/cabecalho.png)

# Avaliação contínua de programação orientada a objetos: as apps do telemóvel

## As apps do telemóvel

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

## O que precisas de saber antes

- As classes, os objetos e os métodos: guias [Objetos, classes e instâncias](../01-programacao-orientada-objetos/02-objetos-classes-instancias.md) e [Encapsulamento e contratos](../01-programacao-orientada-objetos/03-encapsulamento-contratos.md).
- Uma classe que guarda outros objetos numa lista: guia [Composição e modelação](../01-programacao-orientada-objetos/04-composicao-modelacao.md).
- Uma classe que tem tudo o que outra tem e mais alguma coisa, com o `super()`: guia [Herança e polimorfismo](../01-programacao-orientada-objetos/05-heranca-polimorfismo.md).
- Os [temas de treino](../projeto/temas-de-treino.md) do projeto têm a mesma forma deste exercício.

## Como está organizada

São 90 minutos, em Python:

- o professor apresenta o exercício: 5 minutos;
- tarefa 1, o programa: 60 minutos;
- tarefa 2, uma alteração pedida na hora e algumas perguntas: 20 minutos;
- entrega: 5 minutos.

Trabalhas sozinho. Podes consultar os guias, os laboratórios, as fichas, os temas de treino e as resoluções deles, os teus apontamentos e o código que escreveste nas aulas. Não podes usar assistentes de inteligência artificial, nem as sugestões automáticas de código do editor, nem falar com os colegas.

## Tarefa 1: o programa (60 minutos)

Escreve o programa das apps do telemóvel, com as três classes.

Deves poder:

- instalar uma app, simples ou jogo;
- ver a lista das apps;
- atualizar uma app, ou seja, mudar o tamanho dela para o novo valor.

O programa recusa:

- um código que já existe;
- um nome vazio;
- um tamanho que não seja um número inteiro de 1 a 4000, tanto ao instalar como ao atualizar;
- uma idade mínima que não seja 3, 7, 12, 16 ou 18.

Quando recusa, mostra uma mensagem a dizer porquê, e nada muda.

No fim do programa, escreve algumas linhas que experimentem cada operação e cada recusa e que mostrem a lista.

Se acabares antes, acrescenta uma maneira de ver só as apps que ocupam mais de 1000 MB.

## Tarefa 2: a alteração pedida na hora (20 minutos)

Por volta do minuto 65, o professor pede a toda a turma uma pequena alteração ao programa. Fazes a alteração sozinho e voltas a experimentar o programa. Enquanto isso, o professor pode fazer-te perguntas sobre o teu código.

## Como é avaliada

Este exercício não tem nota própria: o professor observa o teu trabalho, como nas outras aulas, e o que observa entra na avaliação contínua do módulo. Observa quatro coisas:

- se usas classes e objetos, e se cada app guarda os seus dados;
- se as regras estão dentro das classes e se uma recusa deixa os dados como estavam;
- se é o telemóvel que guarda as apps e que recusa o código repetido;
- se o jogo aproveita o que a app já tem e se a lista mostra cada app sem perguntar se é um jogo.

## Entrega

No fim, entregas o teu ficheiro `.py` pelo meio que o professor indicar.

![Rodapé](../imagens/rodape.png)

![Cabeçalho](../imagens/cabecalho.png)

# Juntar as ideias: compreender e completar um pequeno inventário

*M10 · Caderno 6*

Já estudámos objectos, classes, estado, métodos e a forma como diferentes objectos colaboram. Também vimos como uma operação pode proteger os dados de um artigo. Vamos agora juntar essas ideias num pequeno programa que já vem parcialmente preparado.

O objectivo não é escrever uma aplicação inteira nem decorar sintaxe. É **perceber o modelo, completar uma operação e explicar o que acontece aos dados**. Podes consultar os cadernos anteriores durante o trabalho.

## 1. Recordar o percurso com um exemplo

Imagina duas fichas: A01, Caderno, 8 unidades; A02, Pasta, 3 unidades. Ambas seguem a descrição comum `Artigo`.

Se o inventário recebe um pedido para retirar 3 unidades do primeiro artigo, encaminha-o para A01. A01 verifica o pedido, passa de 8 para 5 unidades e responde que aceitou. A02 continua com 3.

Se o pedido seguinte for retirar 6 de A01, a operação é recusada: só existem 5. A quantidade não muda.

| Ideia estudada | Onde a vemos neste exemplo |
| --- | --- |
| Classe | A descrição comum dos artigos |
| Instâncias | As duas fichas concretas A01 e A02 |
| Estado | Código, nome e quantidade de cada artigo |
| Método | A operação que recebe o pedido de retirada |
| Encapsulamento | O artigo controla a alteração da sua quantidade |
| Composição | O inventário reúne os artigos e usa as suas operações |

Lê a tabela como uma ligação entre conceitos e acontecimentos, não como uma lista para decorar. Se uma palavra ainda não fizer sentido, volta ao acontecimento que a exemplifica.

## 2. Como ler o programa sem tentar perceber tudo de uma vez

No [programa inicial do trabalho](../avaliacoes/inventario-inicial.js), começa por encontrar estas zonas:

1. A classe `Artigo`, com os dados e operações comuns.
2. A criação dos artigos A01 e A02.
3. O objecto `inventario`, que guarda a lista dos dois artigos.
4. As chamadas finais, que fazem pedidos e mostram resultados.

Primeiro lê as chamadas finais para perceber o que o programa tenta fazer. Depois procura os métodos chamados. Não precisas de memorizar todas as linhas antes de começar.

## 3. O que faz o construtor?

No caderno anterior, o construtor recebia apenas a quantidade inicial. Neste trabalho recebe também código e nome. Este excerto mostra a criação de um artigo no programa fornecido:

```js partial
const artigoA = new Artigo("A01", "Caderno", 6);
```

Lê a chamada por ordem: estamos a criar um novo artigo com código A01, nome Caderno e quantidade 6. Esses valores chegam ao construtor pela mesma ordem dos seus parâmetros.

| Valor enviado | Parâmetro que o recebe | Dado preparado na instância |
| --- | --- | --- |
| `"A01"` | `codigo` | Código do artigo |
| `"Caderno"` | `nome` | Nome do material |
| `6` | `quantidade` | Quantidade inicial |

O construtor guarda os valores no novo objecto. Não retira unidades: prepara o estado inicial. Quando criamos o segundo artigo, preparamos outra instância com os seus próprios valores.

Os dados iniciais já vêm escolhidos e correctos. A tarefa não é construir um formulário para criar artigos; vais trabalhar sobre estes dois artigos preparados.

## 4. Uma consulta, uma alteração e uma resposta

`consultarQuantidade()` pergunta quanto existe. `adicionar(unidades)` tenta acrescentar unidades. `retirar(unidades)` deverá tentar retirá-las.

Nas operações de alteração, o valor booleano responde a uma pergunta: **o pedido foi aceite?** A consulta responde a outra: **quantas unidades existem agora?**

Por exemplo, para um artigo com 8 unidades, uma retirada de 3 pode devolver `true` e deixar a consulta devolver 5. O primeiro valor não é a quantidade; é uma resposta de aceitação.

Quando verificares o teu programa, observa sempre as duas coisas. Um método pode devolver `false` e, por erro, já ter alterado a quantidade. A resposta, sozinha, não demonstra que o estado foi preservado.

## 5. O que significa o programa estar incompleto?

O método de retirada do programa inicial responde sempre `false`. Foi deixado assim para teres uma parte concreta a completar. O ficheiro pode executar sem apresentar um erro da linguagem, mas ainda não cumpre a tarefa de retirar unidades.

Um **erro de sintaxe** impede a linguagem de interpretar correctamente o código, por exemplo quando falta uma chaveta. Um **erro de comportamento** pode existir num programa que executa: faz algo diferente do que o problema pede.

Antes de alterar a retirada, procura um pedido que deveria ser aceite e observa a resposta actual. Essa comparação dá-te um ponto de partida: sabes o que está em falta e o que tens de voltar a verificar depois da correcção.

## 6. Como registar uma verificação

Segue este exemplo resolvido, com valores diferentes dos usados no trabalho:

| O que queremos verificar | Antes | Pedido | O que esperamos |
| --- | ---: | --- | --- |
| Uma retirada possível | 8 | Retirar 3 | Aceite; ficam 5 |
| Uma retirada acima do disponível, logo a seguir | 5 | Retirar 6 | Recusado; continuam 5 |

Depois de executar, acrescentamos o que observámos. Se coincidir com a previsão, temos evidência sobre esses casos. Se não coincidir, procuramos a causa antes de mudar instruções ao acaso.

Um registo útil de correcção pode ter quatro frases: “Esperava…”, “Observei…”, “A instrução que explica a diferença é…” e “Depois da alteração, confirmei…”. Cada frase deve referir valores ou instruções concretas.

## 7. Preparação antes do trabalho

Responde brevemente, por palavras:

1. Qual é a diferença entre criar um artigo e retirar unidades desse artigo?
2. Que objecto decide se a retirada é possível: o inventário ou o artigo? Que dados precisa para decidir?
3. Como podes confirmar que uma retirada em A01 não alterou A02?
4. Se o pedido for recusado, que duas observações deves fazer no programa?

Depois segue o [enunciado completo](../avaliacoes/mini-problema.md). Lá encontras os dados do trabalho, as alterações pedidas, os casos a verificar e o que deves entregar.

## 8. Explicar o teu trabalho

A tua explicação não precisa de recitar definições. Usa o programa e os valores: mostra qual foi o artigo que recebeu o pedido, aponta a condição que decidiu e explica o que aconteceu à quantidade.

O professor poderá pedir uma pequena alteração de valores para verificar se compreendeste o raciocínio. Se trabalhaste em par, cada um deve conseguir explicar o seu próprio traço e identificar a responsabilidade de cada objecto.

Também retomaremos as notificações do caderno 5: duas variantes podem receber o mesmo pedido e apresentar texto de maneira diferente. Essa explicação é separada do inventário; não tens de acrescentar herança ao programa para terminar o trabalho.

![Rodapé](../imagens/rodape.png)

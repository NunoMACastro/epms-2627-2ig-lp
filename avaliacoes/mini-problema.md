![Cabeçalho](../imagens/cabecalho.png)

# Trabalho prático: completar a retirada de material

*M10 · Trabalho de síntese*

Uma equipa usa um programa para acompanhar os materiais de uma sala. O programa já conhece dois artigos e já sabe consultar e adicionar unidades. Falta completar a operação que retira unidades.

Vais receber um programa parcialmente preparado. Primeiro explica como os dados estão organizados; depois completa a operação em falta e verifica os resultados. Podes consultar os cadernos e os exemplos trabalhados nas aulas e pedir uma pista ao professor.

## Os artigos com que vais trabalhar

| Código | Nome | Quantidade inicial |
| --- | --- | ---: |
| A01 | Caderno | 6 |
| A02 | Pasta | 2 |

Cada linha representa um artigo. Os códigos são diferentes, os nomes estão preenchidos e as quantidades são válidas. Estes dados já vêm escritos no programa; não precisas de criar outros artigos nem de os introduzir através de um formulário.

O inventário guarda a lista `[A01, A02]`. Neste trabalho, o pedido feito ao inventário é encaminhado para o **primeiro artigo**, A01.

## 1. Preparar e observar o programa inicial

Abre [o programa inicial](inventario-inicial.js) e guarda uma cópia de trabalho com o nome `M10-B06-inventario-trabalho.js`, na pasta indicada pelo professor. Usa as [instruções de execução](../01-programacao-orientada-objetos/README.md) quando precisares de recordar como abrir e executar um exemplo.

Localiza o método `retirar`. Neste momento devolve sempre `false`, que neste programa significa “pedido recusado”. **A operação ainda não está concluída.** A tua tarefa é substituir essa resposta provisória por uma decisão que respeite as regras abaixo.

Executa o programa inicial. Observa o pedido de 2 unidades e escreve:

- Devia ser aceite, tendo em conta os dados iniciais? Porquê?
- Qual foi a resposta apresentada?
- Que quantidade ficou guardada em A01?

Guarda estas observações para poderes compará-las com o programa corrigido.

## 2. Explicar o modelo antes de alterar o código

Usando como referência os esquemas do caderno 4, desenha:

- Uma caixa `Artigo`, com os dados que guarda e as operações que disponibiliza.
- Uma caixa `Inventario`, com a lista de artigos e a operação que encaminha a retirada.
- Uma linha entre as caixas, com uma frase que explique a relação.

Acrescenta as duas fichas concretas A01 e A02, com os seus valores. Por baixo do desenho, explica qual dos objectos deve decidir se há unidades suficientes.

## 3. Completar o método de retirada

O método recebe o número de unidades que queremos retirar. Deve seguir este contrato:

| Situação | Resposta | O que acontece à quantidade |
| --- | --- | --- |
| O pedido é um número inteiro positivo e não ultrapassa o disponível | `true` (aceite) | Retiram-se as unidades pedidas |
| O pedido não cumpre alguma dessas condições | `false` (recusado) | Mantém-se a quantidade anterior |

Zero é permitido como quantidade existente. Por exemplo, retirar todas as unidades disponíveis pode deixar o artigo vazio. Mas pedir para retirar zero unidades é recusado neste trabalho.

Escreve primeiro os passos da decisão por palavras. Depois completa **apenas o interior do método `retirar`**. A criação dos artigos, a consulta, a adição e o encaminhamento já estão preparados. Consulta o caderno 3 para recordar como se lê uma condição e como se termina um método com `return`.

Usa números pequenos. Não precisas de converter texto, criar páginas, guardar ficheiros de dados ou acrescentar outras funcionalidades.

## 4. Verificar a sequência já fornecida

No final do programa existem chamadas que retiram 2 unidades de A01 e, a seguir, tentam retirar 9. Executa o ficheiro inteiro para começar com as quantidades iniciais da tabela.

Preenche esta tabela. A segunda linha de pedidos começa na quantidade deixada pela primeira:

| Momento | Resposta prevista | A01: quantidade prevista | A02: quantidade prevista | O que observaste na consola |
| --- | --- | --- | --- | --- |
| Antes dos pedidos | Não há pedido | 6 | 2 | A preencher |
| Depois de pedir 2 a A01 | A preencher | A preencher | A preencher | A preencher |
| Depois de pedir 9 a A01 | A preencher | A preencher | A preencher | A preencher |

Se previsão e observação forem diferentes, não alteres a tabela apenas para ficar igual à consola. Procura primeiro qual das duas está errada e explica porquê.

## 5. Verificar limites e pedidos incorrectos

Agora precisamos de testar outras situações. Para cada linha da tabela seguinte, começa com **um programa acabado de iniciar**, em que A01 tem 6 e A02 tem 2.

Para não executar os pedidos anteriores por engano, faz uma cópia de trabalho para estas verificações. Mantém as definições e a criação dos objectos. Substitui as mensagens e chamadas finais por este pequeno bloco, já no interior das chavetas exteriores do ficheiro:

```js partial
console.log("Antes:", artigoA.consultarQuantidade(), artigoB.consultarQuantidade());
console.log("Resposta:", inventario.retirarDoPrimeiro(6));
console.log("Depois:", artigoA.consultarQuantidade(), artigoB.consultarQuantidade());
```

Este trecho depende dos objectos definidos acima; não é para executar sozinho. O `6` na chamada é o pedido. Em cada ensaio substitui-o pelo número da linha correspondente e volta a executar o ficheiro completo.

| Pedido a A01 | Resposta que esperas | Quantidade final esperada de A01 | Quantidade final esperada de A02 | Resultado observado |
| --- | --- | --- | --- | --- |
| 6 | A preencher | A preencher | A preencher | A preencher |
| 0 | A preencher | A preencher | A preencher | A preencher |
| −1 | A preencher | A preencher | A preencher | A preencher |
| 1,5 (escrever `1.5` no código) | A preencher | A preencher | A preencher | A preencher |

Faz ainda um último ensaio: num programa acabado de iniciar, pede 6 e depois pede 1 **sem reiniciar entre os dois pedidos**. Acrescenta à chamada de 6 uma segunda chamada com 1 e uma consulta final. Explica o que a segunda resposta nos diz sobre a retirada de um artigo vazio.

## 6. Explicar uma correcção e uma decisão

Volta às observações feitas antes de completares o método. Descreve um caso que o programa inicial resolvia mal e que agora resolve de acordo com o contrato. Indica os valores antes e depois, além da resposta da operação.

Na conversa com o professor, prepara-te para:

- Mostrar onde o pedido é encaminhado e onde é decidido.
- Explicar por que uma recusa não pode alterar a quantidade.
- Mostrar como verificaste que A02 manteve o seu estado.
- Resolver uma pequena alteração de valores usando o mesmo raciocínio.

Se trabalhares em par, cada pessoa fará a sua própria explicação. Podes indicar em que passos recebeste ajuda; essa informação serve para orientar o trabalho seguinte.

## O que entregar

Entrega pelo meio indicado pelo professor:

1. O esquema com as classes/responsabilidades e as duas fichas concretas.
2. O ficheiro de trabalho com a retirada completada.
3. As tabelas de previsão e observação, incluindo o ensaio do artigo vazio.
4. A explicação curta da correcção feita ao programa inicial.

O professor vai observar se distingues descrição e objectos concretos, se o artigo mantém a quantidade válida, se consegues seguir os pedidos e se explicas o próprio trabalho. Não é necessário aumentar o número de classes ou acrescentar funcionalidades. O trabalho realiza-se no bloco de síntese, incluindo as explicações e o apoio necessário.

![Rodapé](../imagens/rodape.png)

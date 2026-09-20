# Como impedir que um artigo fique com uma quantidade impossível?

*M10 · Caderno 3*

No caderno anterior, pedimos a um artigo com 6 unidades que retirasse 2. O método fez a subtracção e ficaram 4. Escolhemos um pedido que sabíamos ser possível. Mas um programa também precisa de lidar com pedidos incorrectos.

Vamos partir de um erro simples para perceber **por que razão um objecto deve controlar as alterações aos seus dados**. É esta necessidade que nos vai levar ao encapsulamento.

## 1. O problema de alterar um valor sem verificar nada

Imagina que o artigo A01 tem 6 unidades e alguém pede para retirar 9. Se o programa fizer apenas a conta, obtém:

```text
6 − 9 = −3
```

O resultado matemático existe, mas não é uma quantidade de material válida para o nosso inventário. Não podemos ter menos três cadernos guardados na sala.

O problema não se resolve apresentando uma mensagem de erro depois de guardar −3. Nessa altura, a informação já ficou incorrecta. Precisamos de **verificar antes de alterar** e de conservar os dados quando o pedido é recusado.

## 2. Que regras devem continuar verdadeiras?

Uma quantidade do inventário é um número inteiro não negativo: 0, 1, 2, 3 e assim por diante. Não usamos −3 nem 1,5 como quantidade destes materiais.

Esta regra deve ser verdadeira antes e depois de cada operação. Uma regra que queremos manter ao longo do funcionamento do programa chama-se uma **invariante**. Não precisas de decorar a palavra sem a compreender: neste exemplo, significa “qualquer que seja a operação, o artigo não pode ficar com uma quantidade negativa ou fraccionada”.

Também precisamos de decidir quais os pedidos aceites. Neste inventário:

- Adicionar exige um número inteiro positivo de unidades.
- Retirar exige um número inteiro positivo e não pode ultrapassar a quantidade disponível.
- Consultar apenas informa da quantidade; não a altera.

### Zero no estado e zero no pedido

Com 6 unidades, retirar 6 é possível. A quantidade passa a zero: o material esgotou.

Com 6 unidades, pedir para retirar 0 é recusado segundo a regra que escolhemos. Não é uma retirada efectiva. **A validade do estado final e a validade da quantidade pedida são perguntas diferentes.** Outros programas podem escolher outra regra para o pedido zero; aqui, a regra foi definida explicitamente.

## 3. Quem deve ser responsável por proteger a quantidade?

Se várias partes de um programa puderem alterar directamente a quantidade, cada uma terá de se lembrar das mesmas verificações. Basta uma esquecer-se para o artigo ficar num estado inválido.

Podemos organizar o programa de outra maneira: o artigo guarda a quantidade e oferece operações para a consultar ou alterar. Quem precisa de retirar material faz o pedido ao artigo. O próprio artigo decide se pode cumprir esse pedido.

Esta organização é uma ideia central do **encapsulamento**: reunir estado e comportamento numa unidade com responsabilidade sobre a sua utilização. No nosso caso, não basta pôr dados e métodos perto uns dos outros; os métodos devem controlar as alterações e respeitar as regras.

A **ocultação de informação** complementa essa organização. A quantidade deixa de ser um campo em que qualquer parte do programa pode escrever directamente. O exterior usa as operações disponibilizadas, sem precisar de mexer na forma como a quantidade é guardada.

Pensa numa pessoa responsável pelo armário: podes pedir duas unidades ou perguntar quantas restam. Não precisas de reescrever o registo do armário por tua conta. A comparação ajuda a separar o pedido da responsabilidade de manter o registo correcto.

## 4. Interface pública: aquilo que o objecto deixa usar

Chamamos **interface pública** ao conjunto de operações que um objecto disponibiliza a quem o utiliza. A palavra “interface” não significa necessariamente um ecrã com botões. Aqui, estamos a falar de pedidos que podem ser feitos no código.

Para o artigo, oferecemos estas operações:

| Pedido | Informação recebida | Resposta | Altera a quantidade? |
| --- | --- | --- | --- |
| Consultar a quantidade | Nenhuma | A quantidade actual | Não |
| Adicionar unidades | Quantas unidades adicionar | Aceite ou recusado | Só quando o pedido é aceite |
| Retirar unidades | Quantas unidades retirar | Aceite ou recusado | Só quando o pedido é aceite |

O utilizador destas operações precisa de conhecer o seu significado e as regras de aceitação. Não precisa de conseguir escrever directamente no campo interno da quantidade.

## 5. Um contrato explica o que uma operação promete

Um **contrato de uma operação** é uma descrição clara do que ela recebe e do que faz. Ajuda tanto quem escreve a operação como quem a utiliza.

Vejamos um contrato completo para retirar unidades:

> A operação recebe o número de unidades pedidas. Se esse número for inteiro, positivo e não ultrapassar a quantidade disponível, retira as unidades e responde “aceite”. Caso contrário, responde “recusado” e mantém a quantidade anterior.

Há três partes a observar: **entrada** (o pedido), **resultado** (a resposta) e **efeito** (o que aconteceu ao estado). Dizer apenas que a operação devolveu “recusado” não prova que o estado tenha sido preservado; temos de verificar também a quantidade.

### Exemplo resolvido: duas chamadas sucessivas

| Passo | Quantidade antes | Pedido | Verificação | Resposta | Quantidade depois |
| --- | ---: | --- | --- | --- | ---: |
| 1 | 6 | Retirar 2 | 2 é inteiro, positivo e cabe nas 6 unidades | Aceite | 4 |
| 2 | 4 | Retirar 9 | 9 ultrapassa as 4 unidades disponíveis | Recusado | 4 |

A segunda chamada começa no estado deixado pela primeira. Não regressa automaticamente a 6. A rejeição conserva as 4 unidades que realmente existiam naquele momento.

## 6. Traduzir a decisão para JavaScript, um passo de cada vez

O [ficheiro de demonstração](exemplos/M10-B03-contrato.js) já contém uma classe. O professor irá percorrê-la contigo. Primeiro vamos compreender a operação de retirada; não tens de escrever a classe de memória.

Dentro do método, fazemos três perguntas. Os excertos seguintes pertencem ao método fornecido e não são programas para executar isoladamente.

**Primeira pergunta: o pedido é um número inteiro?**

```js partial
if (Number.isInteger(unidades) === false) {
  return false;
}
```

`Number.isInteger(unidades)` verifica se o valor recebido é um número inteiro. A comparação `=== false` pergunta se essa verificação deu falso. `if` lê-se “se”: quando a condição se verifica, executam-se as instruções entre as chavetas.

`return false` termina o método e devolve o valor falso. Neste contrato, falso significa “pedido recusado”. Como ainda não alterámos a quantidade, ela mantém o valor anterior.

**Segunda pergunta: o pedido é positivo?**

```js partial
if (unidades <= 0) {
  return false;
}
```

O símbolo `<=` significa “menor ou igual”. Se o pedido for zero ou negativo, o método termina com uma recusa.

**Terceira pergunta: existem unidades suficientes?**

```js partial
if (unidades > this.#quantidade) {
  return false;
}
```

O símbolo `>` significa “maior que”. Nesta chamada, `this` refere-se ao artigo que recebeu o pedido. `#quantidade` é o nome do seu campo privado, que guarda a quantidade. Se o pedido for superior ao que existe, não podemos aceitá-lo.

Só chegamos às instruções seguintes quando as três verificações deixaram continuar:

```js partial
this.#quantidade = this.#quantidade - unidades;
return true;
```

Agora é seguro fazer a subtracção. `true`, verdadeiro, significa “pedido aceite” neste contrato.

Repara na ordem: **verificar → alterar → responder**. Nos pedidos recusados, o método termina durante a verificação, antes de chegar à alteração.

## 7. Como reconhecer a classe e o estado privado no exemplo

A linha `class Artigo` inicia a descrição da classe. Dentro dela estão os dados e os métodos. A linha `const artigo = new Artigo();` cria uma instância e associa-lhe o nome `artigo`. `new` significa aqui que estamos a pedir um novo objecto a partir da classe.

O campo `#quantidade` começa com 6. O símbolo `#` faz parte do mecanismo de campos privados de JavaScript: o código exterior à classe não pode aceder directamente a esse campo. Para conhecer o valor, chama `consultarQuantidade()`; para o alterar, usa os métodos disponibilizados.

Por exemplo, `artigo.consultarQuantidade()` devolve um número, como 6. Já `artigo.retirar(2)` devolve um booleano, `true` ou `false`. Um booleano é um valor lógico com apenas essas duas possibilidades.

No caderno anterior, o método devolvia directamente a quantidade restante. **Neste exemplo escolhemos outra resposta:** o resultado diz se o pedido foi aceite, e uma consulta separada permite saber quanto resta. O nome de um método, por si só, não define o que devolve; é preciso conhecer o contrato.

A demonstração completa apresenta estado 6; depois `true` e 4 ao retirar 2; depois `false` e 4 ao tentar retirar 9; finalmente `true` e 7 ao adicionar 3. Acompanha a quantidade entre chamadas para perceber cada resultado.

## 8. Agora experimenta

### Exercício 1: Decidir antes de calcular

Em cada linha começamos de novo com 5 unidades. Completa as colunas vazias. Antes de escrever a quantidade final, verifica se o pedido deve ser aceite.

| Pedido | Aceite ou recusado? | Quantidade final | Regra que usaste |
| --- | --- | --- | --- |
| Retirar 5 | A completar | A completar | A completar |
| Retirar 6 | A completar | A completar | A completar |
| Retirar 0 | A completar | A completar | A completar |
| Adicionar 2 | A completar | A completar | A completar |
| Adicionar 1,5 | A completar | A completar | A completar |

### Exercício 2: Explicar uma sequência

Um artigo começa com 4 unidades. Recebe, por ordem, os pedidos: retirar 3; retirar 2; adicionar 2. Faz uma tabela com quantidade antes, resposta e quantidade depois de cada pedido. Usa a tabela resolvida da secção 5 como modelo.

### Exercício 3: Consultar não é retirar

Um colega afirma: “Se `consultarQuantidade()` devolve 6, o método acabou de acrescentar seis unidades.” Explica o erro. Na tua resposta, distingue o valor devolvido da alteração do estado.

### Exercício 4: Confirmar uma rejeição no programa

Numa cópia do ficheiro de demonstração, substitui apenas a chamada `artigo.retirar(2)` por `artigo.retirar(1.5)`. Em JavaScript escrevemos a parte decimal com ponto.

Prevê a resposta e a quantidade apresentadas nessa linha. Executa desde o início e confirma. Depois explica por que precisaste de observar **os dois valores**, e não apenas `false`.

### Exercício 5: Encontrar um erro de ordem

Um programa começa com 6 unidades. Ao receber um pedido de 9, subtrai primeiro e só depois verifica se a quantidade ficou negativa. Detecta o problema e responde “recusado”, mas não volta a alterar a quantidade.

Indica a quantidade que ficou guardada. Explica por que a mensagem de recusa não resolve o erro. Escreve, por palavras, a ordem correcta das decisões e da alteração.

### Exercício 6: Escrever um contrato

Escreve o contrato de **adicionar unidades**, seguindo as três partes da secção 5: o que recebe, quando aceita e o que acontece em cada caso. Acrescenta um exemplo aceite e um recusado, ambos com estado inicial conhecido.

## Para rever antes de avançar

O encapsulamento ajuda-nos a atribuir ao artigo a responsabilidade pelos seus dados. A ocultação evita alterações directas que contornem essa responsabilidade. A interface pública apresenta as operações disponíveis e os contratos explicam como usá-las.

A ideia central é simples de verificar: se um pedido é recusado, a quantidade não deve ficar diferente por causa desse pedido.

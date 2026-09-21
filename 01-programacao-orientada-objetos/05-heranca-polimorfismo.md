![Cabeçalho](../imagens/cabecalho.png)

# A mesma operação, maneiras diferentes de a realizar

*M10 · Caderno 5*

No inventário, vimos que uma unidade pode **ter** outras: o inventário contém artigos. Agora vamos estudar outra relação: um tipo mais específico que **é um caso** de um tipo geral.

Para isso vamos usar um exemplo separado. Imagina que um programa prepara pequenas mensagens, como “Contagem concluída”. Às vezes queremos apenas o texto; noutras situações queremos uma apresentação mais detalhada. Vamos chamar **notificação** a essa mensagem preparada para ser apresentada.

Trabalharemos em papel e em pseudocódigo. Não vamos enviar mensagens nem usar serviços de notificações. O objectivo é compreender herança, polimorfismo e abstracção sem ter de aprender já a sua implementação em JavaScript.

## 1. Encontrar o que é comum e o que é diferente

Considera estas duas apresentações da mesma informação:

| Tipo de notificação | Texto guardado | Resultado da apresentação |
| --- | --- | --- |
| Breve | Contagem concluída | Contagem concluída |
| Detalhada | Contagem concluída | Aviso interno: Contagem concluída |

As duas notificações guardam texto. As duas podem receber um pedido para o apresentar. A diferença está na maneira de produzir o resultado: a breve devolve apenas o texto; a detalhada acrescenta “Aviso interno: ” antes dele.

Podemos descrever aquilo que é comum num tipo geral, `Notificacao`, e representar as duas formas como tipos mais específicos: `NotificacaoBreve` e `NotificacaoDetalhada`.

Uma notificação breve **é uma notificação**. Uma notificação detalhada também. Esta frase faz sentido porque ambas continuam a cumprir o papel geral de uma notificação.

## 2. Especialização: do geral para o particular

Uma **especialização** descreve um caso mais específico de um tipo geral. Conserva aquilo que caracteriza o tipo geral e acrescenta ou concretiza alguma particularidade.

No exemplo, a ideia geral é “guardar um texto e permitir apresentá-lo”. A particularidade da notificação breve é apresentá-lo sem prefixo. A da detalhada é acrescentar o aviso inicial.

Podemos mostrar a relação numa árvore:

```text
Notificacao
├── NotificacaoBreve
└── NotificacaoDetalhada
```

Lê a árvore de cima para baixo: na raiz está o tipo geral; nos ramos estão especializações. Lê-a também de baixo para cima: “NotificacaoBreve é uma Notificacao”.

Não é a mesma árvore que obteríamos ao listar os artigos de um inventário. “Inventario contém Artigo” indica organização por partes. “NotificacaoBreve é uma Notificacao” indica uma relação entre tipos.

## 3. Herança: aproveitar uma descrição de base

A **herança** permite definir uma classe a partir de outra. A classe mais geral é a **classe base**. A classe mais específica é uma **classe derivada**, ou subclasse.

Ao definir uma classe derivada, podemos aproveitar características e comportamentos já definidos na classe base. Neste modelo, a classe base `Notificacao` declara que existe um atributo `texto`. As duas classes derivadas herdam essa característica: não deixam de ter texto por o apresentarem de maneira diferente.

Herdar uma característica **não significa que todos os objectos partilham o mesmo valor**. Duas notificações breves podem guardar textos diferentes, tal como dois artigos podem ter quantidades diferentes. A descrição do atributo é comum; o valor pertence ao estado de cada instância.

Também não significa copiar a mensagem de um objecto para outro. Herança é uma relação entre classes. Se eu mudar o texto de uma notificação concreta, isso não muda automaticamente o texto de todas as outras.

### Exemplo resolvido: classes e instâncias na mesma situação

Podemos ter:

- Uma instância de `NotificacaoBreve` com o texto “Material disponível”.
- Outra instância de `NotificacaoBreve` com o texto “Contagem concluída”.
- Uma instância de `NotificacaoDetalhada` com o texto “Material em falta”.

Há duas classes concretas no exemplo e três objectos criados a partir delas. As três instâncias têm texto, mas não precisam de guardar a mesma mensagem.

## 4. Polimorfismo: pedir a mesma operação sem escolher os pormenores

Vamos dar à operação o nome `apresentar()`. Os parênteses vazios indicam que a chamada não fornece um argumento: a notificação já tem o texto guardado no seu estado.

Imagina um trecho de programa que recebe uma notificação e pede apenas:

> Apresenta o teu texto.

Se receber uma notificação breve, obtém a mensagem simples. Se receber uma detalhada, obtém a mensagem com o prefixo. O pedido é o mesmo, mas cada tipo concreto realiza-o de acordo com a sua definição.

Chamamos **polimorfismo** a esta possibilidade de utilizar uma operação comum com objectos que a concretizam de maneiras diferentes, mantendo um contrato compatível.

Neste exemplo, quem faz o pedido não precisa de saber como construir cada apresentação. Essa responsabilidade pertence à notificação. Isto é útil quando temos várias concretizações de uma operação e queremos que o código que as utiliza trabalhe com o que têm em comum.

## 5. O contrato comum é o que permite substituir uma variante por outra

Não basta dar o mesmo nome a dois métodos. Para podermos usar as variantes da mesma maneira, precisamos de saber o que ambas prometem.

O nosso contrato é:

> `apresentar()` não recebe argumentos, devolve um texto que apresenta a mensagem guardada e não altera essa mensagem.

A breve e a detalhada respeitam-no. Ambas devolvem texto; nenhuma precisa de apagar ou modificar o texto original para o apresentar.

Se uma terceira variante devolvesse o número `3` ou apagasse a mensagem, quem a utiliza já não poderia confiar na mesma promessa. Ter o nome `apresentar` não chegaria para a tornar uma substituição adequada.

### Exemplo resolvido: seguir duas chamadas

| Objecto que recebe o pedido | Estado antes | Pedido | Resultado devolvido | Estado depois |
| --- | --- | --- | --- | --- |
| Notificação breve | texto: Material disponível | apresentar() | Material disponível | texto: Material disponível |
| Notificação detalhada | texto: Material disponível | apresentar() | Aviso interno: Material disponível | texto: Material disponível |

A diferença está no resultado da apresentação, não numa alteração do texto guardado. Nas duas linhas o chamador fez o mesmo pedido.

## 6. Abstracção: escolher o essencial de um modelo

Quando criámos a classe `Artigo`, escolhemos código, nome e quantidade porque eram relevantes para o nosso problema. Não tentámos representar todos os pormenores físicos de um caderno, como a textura da capa ou a posição exacta na prateleira.

**Abstrair** é seleccionar as características relevantes para compreender ou resolver um problema e deixar de fora os pormenores que não são necessários nessa situação.

Na notificação geral fazemos algo semelhante: interessam-nos o texto guardado e a possibilidade de o apresentar. O prefixo específico de cada variante fica para as concretizações. Isso permite falar do que é comum sem obrigar todas as notificações a ter a mesma apresentação.

Abstracção não significa escrever pouco ou deixar uma explicação incompleta. Significa escolher conscientemente o nível de detalhe adequado.

## 7. Classes abstractas e métodos abstractos

No nosso modelo, `Notificacao` descreve aquilo que todas as notificações devem ter, mas não escolhe uma forma concreta de apresentação. Vamos tratá-la como uma **classe abstracta**: uma base destinada a organizar aquilo que é comum, e não a produzir directamente uma notificação pronta a apresentar.

`apresentar()` é declarado nessa base como um **método abstracto**. A declaração diz que a operação tem de existir e qual é o seu contrato; ainda não fornece as instruções para construir a apresentação.

As classes concretas têm de **concretizar** essa operação: escrever como se realiza. `NotificacaoBreve` devolve o texto; `NotificacaoDetalhada` acrescenta o prefixo.

É por isso que não criamos, neste modelo, uma instância directamente de `Notificacao`. Faltaria escolher como apresentar a mensagem. Criamos uma instância de uma das variantes concretas, onde essa decisão já está definida.

## 8. Ler o modelo em pseudocódigo

O pseudocódigo seguinte serve para descrever ideias, não para executar na consola. `HERDA` indica a relação com a classe base. `JUNTAR` significa colocar um texto a seguir ao outro; o espaço depois dos dois pontos faz parte do prefixo.

```pseudocode
CLASSE ABSTRACTA Notificacao
    ATRIBUTO texto
    MÉTODO ABSTRACTO apresentar() DEVOLVE TEXTO
FIM CLASSE

CLASSE NotificacaoBreve HERDA Notificacao
    MÉTODO apresentar()
        DEVOLVER texto
    FIM MÉTODO
FIM CLASSE

CLASSE NotificacaoDetalhada HERDA Notificacao
    MÉTODO apresentar()
        DEVOLVER JUNTAR("Aviso interno: ", texto)
    FIM MÉTODO
FIM CLASSE
```

Na primeira classe, repara que o método não tem um conjunto de instruções: existe apenas a declaração do que deverá fazer. Nas outras duas, o método já tem um corpo, ou seja, as instruções que produzem o resultado.

Não estamos a apresentar uma palavra-chave `abstract` de JavaScript. Estamos a compreender um conceito de POO numa notação de apoio. A passagem para a linguagem será trabalhada mais tarde.

## 9. Agora experimenta

### Exercício 1: Ler a árvore

Usando a árvore da secção 2, identifica a classe base e as duas classes derivadas. Escreve uma frase com “é uma” para cada classe derivada. Depois indica o atributo que ambas herdam.

### Exercício 2: Acompanhar duas apresentações

Cria em papel duas fichas: uma notificação breve e uma detalhada, ambas com o texto “Material em falta”. Para cada uma, escreve o pedido `apresentar()`, o resultado que esperas e o texto que fica guardado depois. Segue a tabela resolvida da secção 5.

### Exercício 3: Distinguir classe e estado

Duas notificações breves guardam mensagens diferentes. Um colega diz que isso é impossível porque pertencem à mesma classe. Explica o erro usando a diferença entre a descrição do atributo `texto` e o seu valor numa instância.

### Exercício 4: Verificar se uma variante cumpre o contrato

Uma nova variante tem um método `apresentar()` que devolve a mensagem, mas também apaga o texto guardado durante a operação. Compara este comportamento com o contrato da secção 5. Identifica a parte que não é respeitada e descreve como a corrigir.

### Exercício 5: Propor outra apresentação

Propõe uma variante que apresente a mensagem de outra maneira, mas mantenha o contrato comum. Escreve o nome da variante, o texto inicial, um resultado concreto e uma frase a explicar se o estado muda. Não precisas de escrever código.

### Exercício 6: Regressar ao inventário

Um colega sugere “Inventario herda de Notificacao” porque um inventário poderia usar mensagens. Explica por que usar uma notificação não transforma o inventário numa notificação. Compara a relação com “Inventario contém Artigos”.

### Exercício 7: Explicar o que falta na classe abstracta

Porque é que, no modelo apresentado, escolhemos uma classe concreta para criar uma notificação? Na resposta, indica o que a base já descreve e o que cada variante ainda tem de concretizar.

## Para rever antes de avançar

A herança relaciona uma classe especializada com uma classe base. O polimorfismo permite usar um pedido comum com concretizações diferentes que respeitam o mesmo contrato. A abstracção ajuda a seleccionar aquilo que interessa ao modelo; uma classe abstracta pode expressar uma base que ainda precisa de concretizações.

No inventário, continuaremos a usar composição. Não é necessário acrescentar herança a um programa só para mostrar que conhecemos o conceito.

![Rodapé](../imagens/rodape.png)

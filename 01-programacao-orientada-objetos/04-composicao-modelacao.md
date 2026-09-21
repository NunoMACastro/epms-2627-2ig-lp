![Cabeçalho](../imagens/cabecalho.png)

# Como colaboram o inventário e os artigos?

*M10 · Caderno 4*

Até agora olhámos sobretudo para um artigo de cada vez. Mas um inventário reúne vários artigos. Precisamos de perceber o que cabe ao inventário fazer e o que continua a ser responsabilidade de cada artigo.

Vamos usar apenas os dois materiais já conhecidos: A01, Caderno, com 6 unidades; A02, Pasta, com 2. Começamos por desenhar e seguir um pedido em papel. Depois observamos a mesma colaboração num pequeno programa.

## 1. Um problema, duas responsabilidades

O artigo sabe quantas unidades tem e decide se uma retirada é possível. O inventário sabe quais são os artigos que reúne e permite encaminhar um pedido para um deles.

Estas tarefas são diferentes:

| Pergunta | Quem tem a informação necessária? |
| --- | --- |
| Quais são os artigos reunidos neste inventário? | O inventário, que guarda a lista |
| Quantas unidades tem A01? | O artigo A01, que guarda a sua quantidade |
| A01 pode retirar duas unidades? | A01, que conhece a sua quantidade e a regra |

Separar **responsabilidades** significa decidir que parte do programa fica encarregada de cada tarefa. Não significa que cada parte trabalhe isoladamente. Elas podem colaborar, fazendo pedidos umas às outras.

## 2. “Tem artigos” não significa “é um artigo”

Um inventário **tem artigos**. Um artigo é um dos elementos que podemos reunir no inventário. Por isso, não descrevemos o inventário como se fosse um artigo maior.

Esta distinção aparece noutras situações: uma mochila tem cadernos, mas não é um caderno. Ter algo dentro de si ou utilizar esse algo não faz com que ambas as coisas sejam do mesmo tipo.

Em programação, falamos de **composição de objectos** quando construímos uma unidade que utiliza outras como partes da sua organização. Neste modelo, o inventário mantém uma lista de artigos e utiliza as operações deles.

Não estamos a fazer uma conta para juntar as quantidades num único artigo. Cada artigo continua a ter identidade e estado próprios. A lista permite organizá-los sem apagar as suas diferenças.

## 3. Representar uma classe por um esquema

Um desenho ajuda a discutir o modelo antes de escrever mais código. Vamos usar uma forma simplificada de representar classes, inspirada em UML, uma linguagem de diagramas usada para descrever sistemas.

A caixa seguinte tem três partes. Lê-a de cima para baixo:

```text
+-----------------------------+
| Artigo                      |  nome da classe
+-----------------------------+
| codigo                      |
| nome                        |  dados guardados
| quantidade                  |
+-----------------------------+
| consultarQuantidade()       |
| adicionar(unidades)         |  operações disponíveis
| retirar(unidades)           |
+-----------------------------+
```

Na parte de cima escrevemos o nome da classe. No meio indicamos os dados que cada instância terá. Em baixo listamos os métodos. Os parênteses ajudam a distinguir operações de dados; `unidades` indica a informação recebida pela operação.

Este esquema descreve a classe. Por isso não escrevemos “quantidade 6” na caixa comum. Se quisermos representar a instância A01, então podemos acrescentar uma ficha separada com código A01, nome Caderno e quantidade 6.

O desenho não precisa de ter cores, ferramentas especiais ou todos os símbolos de UML. Primeiro interessa perceber o que cada parte significa.

## 4. Acrescentar o inventário ao desenho

Para a demonstração vamos permitir um pedido muito específico: retirar unidades do **primeiro artigo** da lista. Assim podemos estudar a colaboração sem ter de programar já uma pesquisa por código.

```text
+----------------------------+                  +-------------------------+
| Inventario                 |                  | Artigo                  |
+----------------------------+                  +-------------------------+
| artigos                    | ---- contém ---> | codigo, nome, quantidade|
+----------------------------+                  +-------------------------+
| retirarDoPrimeiro(unidades)|                  | consultarQuantidade()   |
+----------------------------+                  | retirar(unidades)       |
                                                +-------------------------+
```

A linha “contém” diz que o inventário reúne artigos. Não significa que está a retirar unidades nem que um artigo herda do inventário. No diagrama, `artigos` é o nome do dado que guarda a colecção; não é o nome de um artigo individual.

A representação é simplificada: não estamos a definir regras sobre destruir um artigo quando se elimina um inventário, nem a estudar todos os pormenores formais dos diagramas.

## 5. Exemplo resolvido: seguir um pedido até ao artigo

Começamos com a lista `[A01, A02]`. A01 tem 6 unidades e A02 tem 2. Pedimos ao inventário para retirar 2 unidades do primeiro artigo.

1. **O inventário recebe o pedido.** Sabe que o primeiro artigo da lista é A01.
2. **O inventário pede a A01 que retire 2.** Não altera directamente a quantidade.
3. **A01 verifica o pedido.** Há unidades suficientes e a quantidade pedida é válida.
4. **A01 altera o seu estado:** passa de 6 para 4 e responde que aceitou.
5. **O inventário devolve essa resposta** a quem iniciou o pedido.

| Artigo | Antes | Depois |
| --- | ---: | ---: |
| A01 | 6 | 4 |
| A02 | 2 | 2 |

Chamamos **encaminhamento** a passar o pedido ao objecto que o sabe executar. O inventário não precisa de repetir a regra da retirada. Se a repetisse, poderíamos acabar com duas versões diferentes da mesma regra.

Se o pedido seguinte for retirar 9, o percurso é semelhante, mas A01 recusa porque só tem 4. A resposta volta pelo inventário e a quantidade mantém-se em 4. A decisão continua no artigo.

## 6. Reconhecer esta colaboração em JavaScript

Abre [o exemplo deste caderno](../exemplos/programacao-orientada-objetos/composicao.js). A classe de artigo retoma a quantidade privada e a retirada já estudadas. Desta vez queremos criar dois objectos com quantidades iniciais diferentes.

Estas duas linhas, retiradas do programa completo, mostram a criação:

```js partial
const artigoA = new Artigo(6);
const artigoB = new Artigo(2);
```

A primeira chamada cria uma instância com 6 unidades e associa-lhe o nome `artigoA`; a segunda cria outra com 2. O **construtor** é a operação especial que prepara uma nova instância. Recebe o valor inicial e guarda-o no campo privado desse novo objecto. No ficheiro, está escrito com o nome `constructor`.

Para concentrar a demonstração na colaboração, este exemplo só guarda a quantidade. A01 e A02 são os rótulos das fichas que estamos a representar. No trabalho final voltaremos a ter também código e nome guardados em cada artigo.

O inventário usa uma **lista**, chamada array em JavaScript, para reunir as duas instâncias. Neste excerto, retirado do objecto `inventario`, os parênteses rectos delimitam a lista:

```js partial
artigos: [artigoA, artigoB]
```

Uma posição da lista é identificada por um número chamado **índice**. Em JavaScript, o primeiro índice é `0` e o segundo é `1`. Portanto, `this.artigos[0]` selecciona o primeiro artigo da lista deste inventário.

Agora podemos ler o encaminhamento. O excerto seguinte é o método fornecido dentro do objecto inventário:

```js partial
retirarDoPrimeiro(unidades) {
  return this.artigos[0].retirar(unidades);
}
```

O método recebe o número de unidades, selecciona o primeiro artigo, chama o método `retirar` desse artigo e devolve a resposta recebida. A palavra `return` não faz a retirada: entrega a resposta a quem chamou. A retirada acontece dentro do artigo.

## 7. Agora experimenta

### Exercício 1: Ler um esquema

Volta à caixa `Artigo` da secção 3. Identifica o nome da classe, dois dados que guarda e um método. Explica por que `quantidade` está na zona dos dados e `retirar(unidades)` está na zona das operações.

### Exercício 2: Seguir um pedido diferente

Começa com A01 a 6 e A02 a 2. O inventário recebe um pedido para retirar **1** do primeiro artigo. Escreve os cinco passos da colaboração, seguindo o exemplo da secção 5, mas usando os novos valores. No fim apresenta as quantidades dos dois artigos.

### Exercício 3: Escolher outro elemento da lista

Numa cópia do programa, faz estas duas alterações:

1. No encaminhamento, muda `this.artigos[0]` para `this.artigos[1]`.
2. Na primeira chamada final ao inventário, muda o pedido de `2` para `1`.

Antes de executar, identifica qual o artigo que vai receber o pedido e prevê as quantidades apresentadas nas mensagens A01 e A02. Executa desde o início. Para este exercício, analisa primeiro essas três mensagens; a tentativa final de 9 é uma verificação adicional já fornecida.

### Exercício 4: Corrigir uma relação mal escolhida

Um colega escreve no desenho: “Inventario é um Artigo”. Explica o problema usando o que cada um guarda e faz. Depois substitui a frase por uma relação adequada. Não precisas de programar nada.

### Exercício 5: Decidir onde fica uma regra

Imagina que apenas o inventário verifica se existem unidades suficientes, mas o método `retirar` do artigo faz sempre a subtracção. Outro trecho do programa chama directamente o artigo, que tem 6 unidades, e pede 9.

Que quantidade poderia ficar? Onde deveria estar a verificação para que a chamada directa também fosse segura? Relaciona a resposta com o caderno sobre encapsulamento.

### Exercício 6: Desenhar e explicar o teu modelo

Desenha duas caixas, uma para `Inventario` e outra para `Artigo`, seguindo a organização mostrada neste caderno. Acrescenta uma linha legendada entre elas. Não precisas de copiar a disposição exacta das caixas.

Por baixo, escreve um pedido de retirada e explica quem o encaminha, quem decide e quem guarda a quantidade. Usa um pedido possível e outro impossível. Entrega o desenho e essa explicação.

## Para rever antes de avançar

A composição permite organizar objectos que colaboram. O inventário reúne artigos e encaminha pedidos; cada artigo mantém a responsabilidade pela sua quantidade. Uma linha entre duas caixas deve ter um significado que consigas explicar.

No próximo caderno veremos uma relação diferente: um tipo mais específico que continua a ser um caso de um tipo geral. É aí que entra a herança.

![Rodapé](../imagens/rodape.png)

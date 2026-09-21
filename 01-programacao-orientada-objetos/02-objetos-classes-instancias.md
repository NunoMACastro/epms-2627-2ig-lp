![Cabeçalho](../imagens/cabecalho.png)

# Objectos e classes: uma descrição comum, vários artigos

*M10 · Caderno 2*

No [caderno anterior](01-entidades-estado-acoes.md), começámos a organizar a informação sobre os materiais de uma sala. Agora vamos perceber como um programa pode representar cada artigo e manter os seus dados junto das operações que lhe dizem respeito.

Podes começar por acompanhar as explicações e trabalhar em papel. Na parte de JavaScript, cada construção necessária será apresentada antes de ser usada nos exercícios.

## 1. O que estamos a representar?

Imagina uma sala onde estão guardados cadernos e pastas. Para saber o que existe, fazemos este registo:

| Código | Nome do material | Quantidade disponível |
| --- | --- | ---: |
| A01 | Caderno | 6 |
| A02 | Pasta | 2 |

**Um artigo é, aqui, uma referência de material no inventário.** A ficha A01 representa o material “Caderno”, do qual existem seis unidades. Não estamos a criar uma ficha para cada um dos seis cadernos físicos. A ficha A02 representa outro material, “Pasta”.

Esta escolha é importante: vamos representar **dois artigos**, apesar de existirem oito unidades físicas ao todo. Se a quantidade de cadernos passar de 6 para 5, continuamos a ter a mesma ficha A01, agora com um dado actualizado.

O programa não vê os objectos da sala. Só conhece a informação que lhe fornecemos. Temos, por isso, de escolher o que interessa guardar e o que deve poder fazer com essa informação.

## 2. Um objecto reúne dados sobre algo e operações relacionadas com esses dados

Em programação, um **objecto** é uma unidade que pode reunir dados e operações. No nosso exemplo, podemos usar um objecto para representar a ficha do artigo A01.

Os dados respondem a perguntas como “qual é o código?”, “qual é o nome?” e “quantas unidades existem?”. As operações respondem a pedidos como “consulta a quantidade” ou “retira duas unidades”.

Os dados do objecto são guardados em **propriedades**, também chamadas atributos quando estamos a descrever o modelo. Uma propriedade tem um **nome** e um **valor**:

| Nome da propriedade | Valor no artigo A01 | O que nos diz |
| --- | --- | --- |
| `codigo` | `"A01"` | Qual é a referência do material |
| `nome` | `"Caderno"` | Como se chama o material |
| `quantidade` | `6` | Quantas unidades existem neste momento |

Repara na diferença entre a propriedade `quantidade` e o valor `6`. A propriedade é a informação que queremos guardar; o valor é aquilo que sabemos neste momento. Depois de retirar duas unidades, a propriedade continua a chamar-se `quantidade`, mas o seu valor passa a ser `4`.

Chamamos **estado** ao conjunto dos valores guardados num objecto num determinado momento. Código A01, nome Caderno e quantidade 6 descrevem um estado. Código A01, nome Caderno e quantidade 4 descrevem um estado posterior do mesmo objecto.

## 3. O que é um método?

Um **método** é uma operação definida num objecto ou na sua classe. Tal como uma função, pode receber informações, executar instruções e devolver um resultado. A diferença que nos interessa agora é a ligação ao objecto: o método pode trabalhar sobre os dados desse objecto.

Por exemplo, o método `retirar` representa a operação de retirar unidades. Dizer apenas “retirar” não chega: precisamos de indicar **de que artigo** e **quantas unidades**. Um pedido completo seria:

> Ao artigo A01, pede para retirar duas unidades.

Se A01 tinha 6 unidades, passa a ter 4. O artigo A02 não recebeu esse pedido e continua com 2. É esta ligação entre receptor do pedido, operação e estado que vamos acompanhar.

**Definir um método** e **chamá-lo** são momentos diferentes. Definir significa escrever como a operação funciona. Chamar significa pedir que essas instruções sejam executadas agora, sobre um determinado objecto. Ter uma operação disponível não significa que ela já tenha acontecido.

Consultar a quantidade também pode ser um método. Nesse caso, a operação fornece informação, mas não precisa de modificar o estado. Nem todos os métodos alteram dados.

## 4. Para que serve uma classe?

Olha novamente para as duas linhas do inventário. Os valores são diferentes, mas a organização é igual: ambos os artigos têm código, nome e quantidade. Também faz sentido poder consultar a quantidade e retirar unidades de qualquer um deles.

Em vez de descrever esta organização de novo para cada artigo, podemos definir uma descrição comum. Essa descrição é uma **classe**.

Uma classe estabelece que dados e operações caracterizam os objectos desse tipo. A classe `Artigo` pode dizer:

- Cada artigo tem um código, um nome e uma quantidade.
- Podemos consultar a sua quantidade.
- Podemos pedir-lhe que retire unidades.

A classe não é uma linha preenchida do inventário. Descreve **como são os artigos**; não representa, por si só, o artigo A01 ou A02. É a diferença entre um modelo de ficha com campos por preencher e cada ficha concreta preenchida.

Esta comparação ajuda a compreender os dados, mas uma classe vai além de um formulário vazio: também pode definir as operações comuns aos objectos. É por isso que incluímos os métodos na descrição.

Quando dizemos que um objecto é “do tipo Artigo”, estamos a classificá-lo segundo esse modelo. Esperamos que tenha os dados e comportamentos de um artigo. “Artigo” não é o nome de um material; “Caderno” e “Pasta” são valores guardados em artigos concretos.

## 5. Classe e instância: como se relacionam?

Uma **instância de uma classe** é um objecto concreto criado de acordo com essa classe. “Objecto” é o termo mais geral; “instância de Artigo” destaca a relação desse objecto com a classe `Artigo`.

Lê este esquema de cima para baixo. A parte superior mostra a descrição comum. As duas colunas inferiores mostram objectos concretos, com valores preenchidos:

```text
                 Classe Artigo
        Dados: codigo, nome, quantidade
        Operações: consultar, retirar
                ↓                ↓
         Uma instância       Outra instância
         codigo: A01         codigo: A02
         nome: Caderno       nome: Pasta
         quantidade: 6       quantidade: 2
```

As linhas representam a relação entre a descrição e os seus exemplos concretos. Não representam pedidos de retirada nem circulação de unidades.

Temos **uma classe e duas instâncias**. Não precisamos de uma classe `Caderno` e de outra classe `Pasta` só porque os nomes dos materiais são diferentes: as duas fichas seguem a mesma organização e as mesmas operações.

### Exemplo resolvido: o que muda quando retiramos duas unidades?

1. Identificamos o destinatário do pedido: A01.
2. Consultamos a sua quantidade actual: 6.
3. Aplicamos a operação: 6 − 2 = 4.
4. Actualizamos apenas a quantidade de A01.

| Momento | Quantidade de A01 | Quantidade de A02 |
| --- | ---: | ---: |
| Antes do pedido | 6 | 2 |
| Depois de retirar 2 a A01 | 4 | 2 |

A descrição da classe continua a ser a mesma. A01 continua a ser o mesmo artigo. O que mudou foi um valor no estado dessa instância. Usar a mesma classe não significa partilhar uma única quantidade.

## 6. Primeiro contacto com um objecto em JavaScript

Vamos começar por escrever directamente um objecto. Este pequeno programa pode ser executado sozinho:

```js
const artigo = {
  codigo: "A01",
  nome: "Caderno",
  quantidade: 6
};

console.log(artigo.nome);
console.log(artigo.quantidade);
```

Lê-o por partes:

- `const artigo =` associa o nome `artigo` ao objecto que se segue.
- As chavetas `{` e `}` delimitam a descrição desse objecto.
- Em `nome: "Caderno"`, os dois pontos separam o nome da propriedade do seu valor. As aspas indicam texto.
- As vírgulas separam propriedades.
- `artigo.nome` significa “a propriedade nome do objecto artigo”. O ponto liga o objecto à informação que queremos consultar.
- `console.log` apresenta um valor na consola, a área onde podemos ler mensagens do programa.

O programa apresenta `Caderno` e depois `6`. Não retirou unidades: apenas consultou e mostrou dados.

Esta forma de escrever directamente um objecto chama-se **objecto literal**. Não contém uma declaração de classe. Em JavaScript é possível criar objectos desta maneira; começamos por aqui para observar dados e operações antes de estudar a escrita de classes.

`const` impede que o nome `artigo` seja associado a outro valor através de uma nova atribuição. Não torna automaticamente todas as propriedades imutáveis. Uma propriedade como `quantidade` pode mudar durante uma operação.

## 7. Como se lê uma chamada de método?

No [exemplo completo deste caderno](../exemplos/programacao-orientada-objetos/objetos.js), a operação `retirar` já está escrita. A parte seguinte é um excerto do objecto `artigoA`; não é um programa para executar sozinho:

```js partial
retirar(unidades) {
  this.quantidade = this.quantidade - unidades;
  return this.quantidade;
}
```

`unidades` é um **parâmetro**: um nome usado dentro do método para a informação que será recebida. O método não fica limitado a retirar sempre duas unidades. O número é escolhido no momento da chamada.

Quando o programa executa `artigoA.retirar(2)`, `artigoA` é o receptor, `retirar` é a operação e `2` é o **argumento**, ou seja, o valor fornecido para o parâmetro `unidades`.

Nessa chamada, `this` refere-se ao objecto que recebeu o pedido, A01. Assim, `this.quantidade` é a quantidade de A01. A atribuição calcula primeiro `6 - 2` e guarda o resultado `4` na quantidade desse objecto. Esta leitura de `this` corresponde às chamadas sobre objectos usadas neste caderno.

A instrução `return` **devolve** um valor a quem chamou o método. Devolver não é o mesmo que mostrar no ecrã. No programa completo, guardamos a quantidade devolvida no nome `restante` e só depois a apresentamos com `console.log`.

Acompanha a execução pela ordem das mensagens:

| Mensagem | Significado |
| --- | --- |
| `Antes: 6 2` | Quantidades de A01 e A02 antes da chamada |
| `Depois: 4 2` | Quantidades depois de retirar 2 a A01 |
| `Devolvido: 4` | Resultado entregue pela operação a quem a chamou |

Por enquanto, escolhemos retiradas que sabemos serem possíveis. Este primeiro método ainda não verifica pedidos incorrectos. No caderno seguinte vamos perceber por que essa verificação tem de fazer parte da operação.

## 8. Agora experimenta

### Exercício 1: Ler fichas concretas

Considera duas novas fichas: A03, “Caneta”, 8 unidades; A04, “Borracha”, 3 unidades. Ambas seguem o modelo `Artigo`.

1. Escreve o nome da classe e os códigos das duas instâncias.
2. Identifica uma propriedade que ambas têm e indica o valor dessa propriedade em cada uma.
3. Explica por que a quantidade 8 não significa que criámos oito instâncias para as canetas.

### Exercício 2: Acompanhar uma sequência

Começa com A03 a 8 unidades e A04 a 3. São feitos, por esta ordem, os pedidos: retirar 2 de A03; consultar A04; retirar 1 de A04.

Constrói uma tabela com uma linha para o estado inicial e outra depois de cada pedido. Em cada linha escreve as quantidades dos dois artigos. Usa a tabela resolvida da secção 5 como modelo. No fim, explica qual dos pedidos não alterou dados.

### Exercício 3: Alterar uma chamada

No ficheiro de exemplo, localiza `const restante = artigoA.retirar(2);`. Numa cópia de trabalho, muda apenas o argumento de `2` para `3`.

Antes de executar, escreve o que esperas nas três mensagens da consola. Executa o ficheiro inteiro e compara com a tua previsão. O programa começa de novo com A01 a 6 e A02 a 2 sempre que executas o ficheiro completo.

### Exercício 4: Encontrar uma instrução errada

Um colega quer retirar unidades, mas dentro do método escreveu esta atribuição:

```js partial
this.quantidade = unidades;
```

Para este exercício, considera um artigo com 7 unidades e um pedido de 2. Escreve o valor que a instrução errada guarda e o valor que deveria ficar. Depois escreve a atribuição corrigida e explica o papel da subtracção. Podes consultar o exemplo resolvido.

### Exercício 5: Fazer a tua própria representação

Escolhe dois materiais internos diferentes. Usa apenas código, nome e quantidade. Escreve uma descrição comum `Artigo` e duas fichas preenchidas, seguindo o esquema da secção 5. Acrescenta uma retirada possível a uma delas e mostra as duas fichas depois da operação.

Explica a um colega onde está a classe, onde estão as instâncias e qual foi o dado alterado. Entrega o esquema e a explicação curta pelo meio indicado pelo professor.

## Para rever antes de avançar

Um objecto representa uma unidade concreta de informação e comportamento. A classe descreve uma organização comum a objectos desse tipo. Uma instância é um desses objectos concretos. As propriedades guardam valores; os métodos realizam operações. Duas instâncias podem seguir a mesma classe e manter estados diferentes.

Se ainda confundes classe e instância, volta ao esquema: pergunta se estás a olhar para a **descrição comum** ou para uma **ficha com valores concretos**. No próximo caderno vamos estudar como impedir que uma operação deixe esses valores num estado inválido.

![Rodapé](../imagens/rodape.png)

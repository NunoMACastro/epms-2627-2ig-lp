![Cabeçalho](../imagens/cabecalho.png)

# Ficha de exercícios: relações entre objetos, composição e UML leve

*M10 · Caderno 4 · Ficha de exercícios*

Esta ficha acompanha o [caderno 4](04-composicao-modelacao.md). É para praticares sozinho, depois de estudares o caderno e de fazeres o [laboratório](04-composicao-modelacao-laboratorio.md). Conta com cerca de hora e um quarto para os sete exercícios, e mais um quarto de hora se fizeres o desafio opcional do fim.

Cada exercício treina uma coisa só, e a ordem vai do mais direto para o que pede uma pequena decisão tua. Responde no caderno diário ou numa folha, com o número de cada exercício. Quando um exercício pede uma justificação, a justificação é a parte mais importante da resposta: uma escolha certa sem razão escrita vale pouco, e uma escolha discutível bem justificada mostra que percebeste as regras. Entrega as respostas pelo meio indicado pelo professor.

## Exercício 1: ler a caixa de uma classe (5 min)

Esta é a caixa de uma classe de uma loja online:

```text
+----------------------------------------+
| Encomenda                              |
+----------------------------------------+
| numero                                 |
| data                                   |
| estado                                 |
+----------------------------------------+
| acrescentar_linha(codigo, unidades)    |
| anular()                               |
| total_unidades()                       |
+----------------------------------------+
```

1. Escreve o nome da classe, os seus atributos e os seus métodos.
2. Qual dos métodos recebe informação quando é chamado, e que informação recebe?
3. Um colega escreveu `numero = 157` na zona dos atributos desta caixa. Explica, numa ou duas frases, o que está errado, e diz onde faria sentido escrever `numero = 157` (secção 5 do caderno).

## Exercício 2: "tem" ou "é um" (10 min)

Para cada par, escreve a frase verdadeira: "A tem B", "A é um B" ou, se nenhuma das duas for verdadeira, uma frase tua que diga como se relacionam.

1. Inventário e artigo.
2. Caneta e material de escrita.
3. Portátil e computador.
4. Turma e aluno.
5. Carro e motor.
6. Artigo e inventário, por esta ordem.

Depois, responde: um colega propõe, para o programa do inventário, que "o Inventario é um Artigo, porque também tem um nome e guarda quantidades". Usa o teste da secção 3 do caderno ("se A é um B, tudo o que B tem e faz tem de fazer sentido para A") para lhe responder, em três ou quatro frases.

## Exercício 3: composição ou agregação (15 min)

Para cada par, o primeiro é o todo e o segundo é a parte. Copia a tabela e responde às duas perguntas que decidem (secção 7 do caderno). Depois escreve a decisão e se o losango é cheio ou vazio.

| Todo e parte | A parte faz sentido sem o todo? | Quem cria a parte? | Decisão e losango |
| --- | --- | --- | --- |
| Livro e capítulo | A completar | A completar | A completar |
| Equipa de futsal da escola e jogador | A completar | A completar | A completar |
| Casa e divisão (cozinha, quarto, sala) | A completar | A completar | A completar |
| Carrinho de compras de uma loja online e produto | A completar | A completar | A completar |

No último par, pensa no que acontece ao produto quando o carrinho é esvaziado ou abandonado, e se o mesmo produto pode estar no carrinho de outra pessoa ao mesmo tempo. Compara com a linha de encomenda da secção 7: uma linha "2 camisolas" pertence a uma encomenda, mas a camisola, o produto, existe na loja antes e depois da encomenda.

## Exercício 4: descobrir a relação a partir do código (10 min)

Lê este programa completo. Não precisas de o executar para responder, mas podes fazê-lo no fim para confirmar que funciona.

```python
class Aula:
    """Uma aula do horário: dia da semana, hora de início e disciplina."""

    def __init__(self, dia, hora, disciplina):
        self.dia = dia
        self.hora = hora
        self.disciplina = disciplina


class Horario:
    """O horário semanal de uma turma."""

    def __init__(self, turma):
        self.turma = turma
        self._aulas = []

    def marcar(self, dia, hora, disciplina):
        """Marca uma aula nova no horário."""
        nova = Aula(dia, hora, disciplina)
        self._aulas.append(nova)

    def numero_de_aulas(self):
        """Devolve quantas aulas estão marcadas."""
        return len(self._aulas)


class Aluno:
    """Um aluno da escola, identificado pelo número de processo."""

    def __init__(self, numero):
        self.numero = numero


class Clube:
    """Um clube da escola, como o clube de xadrez ou o de teatro."""

    def __init__(self, nome):
        self.nome = nome
        self._socios = []

    def inscrever(self, aluno):
        """Inscreve no clube um aluno que já existe."""
        self._socios.append(aluno)

    def numero_de_socios(self):
        """Devolve quantos alunos estão inscritos."""
        return len(self._socios)


horario = Horario("11.º IG")
horario.marcar("quarta", 10, "LP")
horario.marcar("quinta", 8, "Matemática")

aluno = Aluno(1520)
xadrez = Clube("Xadrez")
teatro = Clube("Teatro")
xadrez.inscrever(aluno)
teatro.inscrever(aluno)

print(horario.numero_de_aulas(), xadrez.numero_de_socios(), teatro.numero_de_socios())
```

1. Na classe `Horario`, indica a linha onde as aulas são criadas. Quem as cria?
2. Na classe `Clube`, o método `inscrever` cria algum aluno? De onde vem o aluno que ele guarda?
3. Com base nas tuas respostas, diz se cada uma das relações, `Horario` com `Aula` e `Clube` com `Aluno`, é uma composição ou uma agregação. Confirma a decisão com a pergunta "a parte faz sentido sem o todo?".
4. Desenha as duas relações em UML leve: quatro caixas só com o nome da classe, as linhas, os losangos e as multiplicidades.

## Exercício 5: seguir pedidos pelo inventário (15 min)

Este exercício usa as classes `Artigo` e `Inventario` do programa completo do passo 7 da secção 10 do caderno, sem alterações. Para executar o excerto, copia esse programa e substitui as linhas que vêm depois das classes, a partir de `inventario = Inventario()`, por estas:

```python partial
inventario = Inventario()
inventario.registar("A04", "Marcador", 5)
inventario.registar("A05", "Agrafador", 1)

try:
    inventario.retirar("A05", 2)
except ValueError as erro:
    print("Pedido 1:", erro)

try:
    inventario.retirar("A06", 1)
except ValueError as erro:
    print("Pedido 2:", erro)

try:
    inventario.retirar("A04", 0)
except ValueError as erro:
    print("Pedido 3:", erro)

inventario.retirar("A04", 5)
print("A04:", inventario.quantidade_de("A04"))
print("A05:", inventario.quantidade_de("A05"))
```

1. Sem executar, copia e completa esta tabela. Na coluna "Quem recusa", escolhe entre o método `_procurar` do inventário, o método `retirar` do artigo, o setter do artigo ou ninguém.

| Pedido | Quem recusa | Mensagem mostrada, se houver |
| --- | --- | --- |
| `retirar("A05", 2)` | A completar | A completar |
| `retirar("A06", 1)` | A completar | A completar |
| `retirar("A04", 0)` | A completar | A completar |
| `retirar("A04", 5)` | A completar | A completar |

2. Escreve as duas últimas linhas que o programa vai mostrar.
3. Executa e compara com as tuas respostas. Se alguma estiver diferente, explica o que tinhas pensado e onde estava o engano.

## Exercício 6: um erro no encaminhamento (15 min)

Um colega escreveu esta versão do método `retirar` do inventário. É um excerto: para a experimentares, substitui o `retirar` da classe `Inventario` do programa do passo 7 por este.

```python partial
    def retirar(self, codigo, unidades):
        """Retira unidades ao artigo com este código (versão com erro)."""
        artigo = self._procurar(codigo)
        artigo.quantidade = artigo.quantidade - unidades
```

O colega testou-a com um artigo de 6 unidades: retirar 2 deixou 4, e retirar 9 foi recusado com a mensagem "A quantidade não pode ser negativa." e manteve as 4. Ficou convencido de que o método funciona.

1. Descobre um pedido de retirada que mostre que esta versão tem um erro. Escreve o pedido, a quantidade antes, a quantidade depois e porque é que o resultado está errado. Confirma executando.
2. Explica por palavras o que esta versão salta. Na tua resposta, diz que regras deixaram de ser verificadas e em que método da classe `Artigo` estão escritas.
3. Corrige o método, mudando uma única linha.
4. Porque é que os dois testes do colega não apanharam o erro? Relaciona com o passo 3 da secção 12 do caderno 3, onde se explica o que o setter protege e o que não sabe.

## Exercício 7: desenhar um modelo (15 min)

Lê a descrição:

> Os professores fazem requisições de material ao armazém da escola. Cada requisição tem um número e uma data, e é formada por linhas. Cada linha diz o código de um artigo e as unidades pedidas. As linhas são criadas pela requisição, quando o professor acrescenta um pedido, e não fazem sentido fora dela. Uma requisição pode ser anulada.

1. Desenha em UML leve as classes `Requisicao` e `LinhaRequisicao`, com os atributos e os métodos que a descrição justifica. Não precisas de inventar mais nada.
2. Liga as duas caixas com a relação adequada: a linha, o losango certo, do lado certo, e as multiplicidades.
3. Há uma decisão que a descrição não toma por ti: a multiplicidade do lado das linhas. Uma requisição tem de ter sempre pelo menos uma linha, ou pode existir uma requisição sem linhas enquanto o professor a está a preparar? Escolhe `1..*` ou `0..*` e justifica a tua escolha numa frase. As duas escolhas podem estar certas, se a justificação estiver.

## Desafio opcional: artigos arrumados em armários

A escola decide registar também em que armário está cada artigo. Um armário agrupa alguns artigos do inventário. Um artigo pode mudar de armário quando se arruma a sala. Se um armário for retirado da sala, os artigos que lá estavam continuam no inventário e passam para outro armário.

1. A relação entre `Armario` e `Artigo` é uma composição ou uma agregação? Justifica com as perguntas da secção 7.
2. O mesmo artigo fica ligado ao inventário por uma composição e ao armário por outra relação. Isto é uma contradição? Explica, pensando em quem cria o artigo e em quem o guarda.

## Antes de entregares

Revê as tuas respostas e confirma que em cada decisão escreveste a razão, e não só a escolha. Indica também um ponto desta ficha que ainda não consegues explicar sem voltar ao caderno: é por aí que deves começar a próxima revisão.

![Rodapé](../imagens/rodape.png)

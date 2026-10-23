![Cabeçalho](../imagens/cabecalho.png)

# Ficha de exercícios: Composição e modelação

Ficha do tema Composição e modelação, do módulo M10, Introdução à Programação Orientada por Objetos. Praticas a leitura e o desenho de diagramas em UML leve e a escolha entre "tem" e "é um" e entre composição e agregação. Praticas também a leitura de código com objetos que colaboram. Fazes sozinho, ao teu ritmo: o que não acabares na aula, acabas em casa ou na aula seguinte.

## O que precisas de saber

O [guia do tema](04-composicao-modelacao.md) e o [laboratório](04-composicao-modelacao-laboratorio.md). Cada exercício usa sobretudo estas secções do guia:

- Exercício 1: "UML leve: a caixa de uma classe".
- Exercício 2: "Duas perguntas sobre duas classes: "tem" e "é um"".
- Exercício 3: "Dois graus de "tem": composição e agregação" e "Agregação em Python: a playlist e as músicas".
- Exercício 4: o exemplo guiado, "Exemplo guiado: construir a classe `Inventario`", sobretudo os passos 3, 5 e 6. Os três tipos de erro (de escrita, de execução e de lógica) estão no guia 03, em "Nada impede uma quantidade impossível".
- Exercício 5: "UML leve: as linhas entre as caixas" e "Dois graus de "tem": composição e agregação".

## Como trabalhar

Faz os exercícios 1 a 5 pela ordem. São a parte obrigatória. Cada exercício treina uma coisa só, e a ordem vai do mais direto para o que pede uma pequena decisão tua. O desafio opcional é para quem acabar. Os três exercícios de "Para ires mais longe" são para quem quer treinar mais com outros casos: podes fazer só um ou dois, ou os que o professor indicar.

Responde no caderno diário ou numa folha, com o número de cada exercício. Quando um exercício pede uma justificação, a justificação é a parte mais importante da resposta. Uma escolha certa sem razão escrita vale pouco. Uma escolha discutível bem justificada mostra que percebeste as regras.

Um programa completo pode ser copiado para um ficheiro `.py` e executado no editor de Python que usas nas aulas. Os excertos não correm sozinhos, e o enunciado diz sempre de que outro código dependem. Entrega as respostas pelo meio indicado pelo professor.

## Exercício 1: Ler a caixa de uma classe

Esta é a caixa de uma classe de um jogo de computador:

```text
+----------------------------------------+
| Personagem                             |
+----------------------------------------+
| nome                                   |
| vida                                   |
| nivel                                  |
+----------------------------------------+
| sofrer_dano(pontos)                    |
| descansar()                            |
| vida_em_falta()                        |
+----------------------------------------+
```

1. Escreve o nome da classe, os seus atributos e os seus métodos.
2. Qual dos métodos recebe informação quando é chamado, e que informação recebe?
3. Desenha a caixa de objeto de uma personagem chamada Aurora, com valores à tua escolha para a vida e o nível. Depois explica, numa ou duas frases, porque é que `nome = "Aurora"` não se escreve na caixa da classe `Personagem`.

## Exercício 2: "Tem" ou "é um"

Para cada par, escreve a frase verdadeira: "A tem B" ou "A é um B". Se nenhuma das duas for verdadeira, escreve uma frase tua que diga como se relacionam.

1. Telemóvel e bateria.
2. Caneta e material de escrita.
3. Portátil e computador.
4. Artigo e inventário, por esta ordem.

Depois, responde a um colega. Para um programa da secretaria da escola, ele propõe que "a Turma é um Aluno, porque também tem um nome e um número". Esta é a caixa da classe `Aluno` desse programa:

```text
+-----------------------------------+
| Aluno                             |
+-----------------------------------+
| nome                              |
| numero                            |
| data_nascimento                   |
+-----------------------------------+
| idade()                           |
| receber_nota(disciplina, nota)    |
+-----------------------------------+
```

Responde-lhe em três ou quatro frases, com o teste de "Duas perguntas sobre duas classes: "tem" e "é um"", no guia. O teste diz: "se A é um B, tudo o que B tem e faz tem de fazer sentido para A".

## Exercício 3: Descobrir a relação a partir do código

Lê este programa completo. Não precisas de o executar para responder, mas podes fazê-lo no fim para confirmar que funciona.

```python
# Ficha 04, exercício 3: o horário de uma turma e os clubes da escola.

class Aula:
    """Uma aula do horário: dia da semana, hora de início e disciplina."""

    def __init__(self, dia, hora, disciplina):
        """Guarda o dia, a hora e a disciplina da aula."""
        self.dia = dia
        self.hora = hora
        self.disciplina = disciplina


class Horario:
    """O horário semanal de uma turma."""

    def __init__(self, turma):
        """Cria o horário de uma turma, ainda sem aulas."""
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
        """Guarda o número de processo do aluno."""
        self.numero = numero


class Clube:
    """Um clube da escola, como o clube de xadrez ou o de teatro."""

    def __init__(self, nome):
        """Cria um clube com um nome, ainda sem sócios."""
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

Se quiseres desenhar estas duas relações em UML leve, com os losangos e as multiplicidades, faz depois o Mais longe 2, na parte opcional do fim da ficha.

## Exercício 4: Um erro no encaminhamento

Um colega escreveu esta versão do método `retirar` do inventário. É um excerto. Para a experimentares, copia o programa completo do exemplo guiado do guia, o do passo 7, ou o `inventario.py` da paragem 3 do laboratório, que faz o mesmo. Depois substitui o `retirar` da classe `Inventario` por este.

```python partial
    def retirar(self, codigo, unidades):
        """Retira unidades ao artigo com este código (versão com erro)."""
        for artigo in self._artigos:
            if artigo.codigo == codigo:
                artigo.retirar(unidades)
```

O colega testou-a com estas linhas, que substituem as que vêm depois das classes, a partir de `inventario = Inventario()`:

```python partial
inventario = Inventario()
inventario.registar("A01", "Caderno", 6)

inventario.retirar("A01", 2)
print("Depois de retirar 2:", inventario.quantidade_de("A01"))

try:
    inventario.retirar("A01", 9)
except ValueError as erro:
    print("Retirar 9 recusado:", erro)
print("Depois de tentar retirar 9:", inventario.quantidade_de("A01"))
```

Retirar 2 deixou 4. Retirar 9 foi recusado com a mensagem "A quantidade não pode ser negativa.", e o artigo manteve as 4. O colega ficou convencido de que o método funciona.

1. Descobre um pedido de retirada que mostre que esta versão tem um erro. Escreve o pedido, o que devia acontecer e o que acontece. Diz também que tipo de erro é: de escrita, de execução ou de lógica. Confirma executando.
2. Segue esse pedido na versão do colega, volta a volta, e explica por palavras o que lhe falta.
3. Corrige o método. Depois volta a correr os três pedidos, os dois do colega e o teu, e confirma que todos dão o que devem.
4. Porque é que os dois testes do colega não apanharam o erro? Compara-os com os pedidos do traço do passo 6 do exemplo guiado.

## Exercício 5: Desenhar um modelo

Lê a descrição:

> Os professores fazem requisições de material ao armazém da escola. Cada requisição tem um número e uma data, e é formada por linhas. Cada linha diz o código de um artigo e as unidades pedidas. As linhas são criadas pela requisição, quando o professor acrescenta um pedido, e não fazem sentido fora dela. Uma requisição pode ser anulada.

O diagrama já está começado. A caixa `Requisicao` tem o nome e os atributos, e a linha que sai dela vai ligar à caixa `LinhaRequisicao`, que ainda não está desenhada. A linha ainda não tem losango nem números.

```text
+------------------------+
| Requisicao             |
+------------------------+
| numero                 |
| data                   |
+------------------------+
|                        |---------------------------
+------------------------+
```

1. Copia o desenho para a folha. Completa a zona dos métodos da `Requisicao` e desenha, na outra ponta da linha, a caixa `LinhaRequisicao`, com os atributos e os métodos que a descrição justifica. Não precisas de inventar mais nada.
2. Na linha, desenha o losango certo, do lado certo, e escreve as multiplicidades. Se precisares, revê no guia como se desenham os losangos, em "Dois graus de "tem": composição e agregação". Em que ponta se escreve cada multiplicidade está em "UML leve: as linhas entre as caixas".
3. Há uma decisão que a descrição não toma por ti: a multiplicidade do lado das linhas. Uma requisição tem de ter sempre pelo menos uma linha? Ou pode existir uma requisição sem linhas, enquanto o professor a está a preparar? Escolhe `1..*` ou `0..*` e justifica a tua escolha numa frase. As duas escolhas podem estar certas, se a justificação estiver.

## Apoio

- Exercício 1: relê, no guia, o que diz cada zona da caixa e o que distingue uma caixa de classe de uma caixa de objeto.
- Exercício 2: analisa cada relação nos dois sentidos e verifica qual das frases é verdadeira. Na resposta ao colega, aplica o teste ao pé da letra, como o guia o aplica ao inventário.
- Exercício 3: relê a comparação entre o `Inventario` e a `Playlist`, no passo 9 do exemplo guiado.
- Exercício 4: segue a versão do colega volta a volta, com um pedido à tua escolha, e escreve que linha é executada a seguir, até o método acabar.
- Exercício 5: começa pelas duas perguntas que decidem, aplicadas à descrição, e só depois desenha. Lê cada ligação nos dois sentidos antes de escreveres os números.
- Desafio: responde às quatro perguntas de "Dois graus de "tem": composição e agregação" para o armário e o artigo, uma a uma, antes de decidires.
- Mais longe 1: em cada par, imagina a aplicação a funcionar. O que acontece à parte quando o todo é apagado?
- Mais longe 2: volta às tuas respostas do exercício 3 e escreve primeiro as duas frases de cada ligação, uma em cada sentido.
- Mais longe 3: faz como no traço do passo 6 do exemplo guiado, um pedido de cada vez, a partir do estado deixado pelo anterior.

## Desafio opcional

Artigos arrumados em armários. A escola decide registar também em que armário está cada artigo. Um armário agrupa alguns artigos do inventário. Um artigo pode mudar de armário quando se arruma a sala. Se um armário for retirado da sala, os artigos que lá estavam continuam no inventário e passam para outro armário.

1. A relação entre `Armario` e `Artigo` é uma composição ou uma agregação? Justifica com as perguntas de "Dois graus de "tem": composição e agregação", no guia.
2. O mesmo artigo fica ligado ao inventário por uma composição e ao armário por outra relação. Isto é uma contradição? Explica, pensando em quem cria o artigo e em quem o guarda.

## Para ires mais longe

Esta parte é opcional, para quem acabou os cinco exercícios e quer treinar mais com outros casos. O Mais longe 1 dá mais prática da escolha entre composição e agregação. O Mais longe 2 completa o exercício 3 com o diagrama. O Mais longe 3 segue pedidos pelo inventário, com o código sem erros. Se o exercício 4 te custou, o Mais longe 3 ajuda a rever o caminho de um pedido antes de voltares a ele. Responde com o título de cada um, por exemplo "Mais longe 2".

### Mais longe 1: Composição ou agregação

Para cada par, o primeiro é o todo e o segundo é a parte. Copia a tabela e responde às duas perguntas que decidem, de "Dois graus de "tem": composição e agregação", no guia. Depois escreve a decisão e se o losango é cheio ou vazio.

| Todo e parte | A parte faz sentido sem o todo? | Quem cria a parte? | Decisão e losango |
| --- | --- | --- | --- |
| Conversa de uma aplicação de mensagens e mensagem | A completar | A completar | A completar |
| Equipa de futsal da escola e jogador | A completar | A completar | A completar |
| Documento de texto e parágrafo | A completar | A completar | A completar |
| Carrinho de compras de uma loja na internet e produto | A completar | A completar | A completar |

No último par, pensa no que acontece ao produto quando o carrinho é esvaziado ou abandonado. Pensa também se o mesmo produto pode estar no carrinho de outra pessoa ao mesmo tempo. Compara com a linha de encomenda do guia: uma linha "2 camisolas" pertence a uma encomenda, mas a camisola, o produto, existe na loja antes e depois da encomenda.

### Mais longe 2: As relações do exercício 3 em UML leve

Volta ao programa do exercício 3 e às decisões que tomaste na alínea 3. Desenha as duas relações em UML leve: quatro caixas só com o nome da classe, as linhas, os losangos e as multiplicidades. Para saberes em que ponta se escreve cada multiplicidade, lê cada ligação nos dois sentidos, como em "UML leve: as linhas entre as caixas".

### Mais longe 3: Seguir pedidos pelo inventário

Este exercício usa as classes `Artigo` e `Inventario` do programa completo do exemplo guiado do guia, o do passo 7, sem alterações. Para executar o excerto, copia esse programa, ou o `inventario.py` da paragem 3 do laboratório, que faz o mesmo. Depois substitui as linhas que vêm depois das classes, a partir de `inventario = Inventario()`, por estas:

```python partial
inventario = Inventario()
inventario.registar("A07", "Marcador", 5)
inventario.registar("A09", "Agrafador", 1)

try:
    inventario.retirar("A09", 2)
except ValueError as erro:
    print("Pedido 1:", erro)

try:
    inventario.retirar("A06", 1)
except ValueError as erro:
    print("Pedido 2:", erro)

try:
    inventario.retirar("A07", 0)
except ValueError as erro:
    print("Pedido 3:", erro)

inventario.retirar("A07", 5)
print("A07:", inventario.quantidade_de("A07"))
print("A09:", inventario.quantidade_de("A09"))
```

1. Sem executar, copia e completa esta tabela. Na coluna "Quem recusa", escolhe entre o método `_procurar` do inventário, o método `retirar` do artigo, o setter do artigo ou ninguém.

   | Pedido | Quem recusa | Mensagem mostrada, se houver |
   | --- | --- | --- |
   | `retirar("A09", 2)` | A completar | A completar |
   | `retirar("A06", 1)` | A completar | A completar |
   | `retirar("A07", 0)` | A completar | A completar |
   | `retirar("A07", 5)` | A completar | A completar |

2. Escreve as duas últimas linhas que o programa vai mostrar.
3. Executa e compara com as tuas respostas. Se alguma estiver diferente, explica o que tinhas pensado e onde estava o engano.

## Critérios de conclusão

- Fizeste os exercícios 1 a 5.
- Em cada decisão escreveste a razão, e não só a escolha.
- No exercício 4, confirmaste no computador o pedido que mostra o erro e, depois da correção, voltaste a correr os três pedidos.
- No exercício 5, completaste as duas caixas, o losango está do lado certo, as multiplicidades estão nas pontas certas e a escolha do lado das linhas está justificada.

## Autoavaliação

1. Em que exercício hesitaste mais entre duas respostas, e o que te fez decidir?
2. O que achaste mais difícil: escolher entre "tem" e "é um", entre composição e agregação, ou pôr as multiplicidades nas pontas certas?
3. Que ponto desta ficha ainda não consegues explicar sem voltar ao guia? É por aí que começas a próxima revisão.

![Rodapé](../imagens/rodape.png)

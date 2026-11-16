![Cabeçalho](../../imagens/cabecalho.png)

# Ficha de exercícios: Composição e modelação

Praticas a descrição de uma classe por palavras e duas escolhas: entre "tem" e "é um", e entre composição e agregação. Procuras também o erro de um colega no inventário. Os exercícios 1 a 5 são obrigatórios. Cada exercício faz-se num script novo, na pasta `tema-04` do laboratório, com o nome que o enunciado dá. As respostas por palavras vão para um comentário no fim desse script. Entregas os cinco scripts como o professor indicar e, se fizeste os desafios, também os deles. Para rever: o [guia do tema](../04-composicao-modelacao.md) e o [laboratório](../laboratorios/04-composicao-modelacao-laboratorio.md).

## Exercício 1: Ler a descrição de uma classe

Esta é a descrição, por palavras, da classe `Personagem` de um jogo de computador:

- Cada personagem guarda um nome, os pontos de vida e o nível.
- Uma personagem cria-se com esses três valores.
- A uma personagem pode pedir-se que sofra dano, com `sofrer_dano(pontos)`; que descanse, com `descansar()`; e que diga quantos pontos de vida lhe faltam, com `vida_em_falta()`.

Cria o script `personagem.py` e responde só com comentários.

1. Escreve o nome da classe, os seus atributos e os seus métodos.
2. Que método recebe informação quando é chamado, e que informação recebe?
3. Descreve por palavras o estado de uma personagem chamada Aurora, com valores à tua escolha para a vida e o nível.

Rever: [O inventário descrito por palavras](../04-composicao-modelacao.md#o-inventário-descrito-por-palavras) e [Classe: a descrição comum](../02-objetos-classes-instancias.md#classe-a-descrição-comum).

<details>
<summary>Pista</summary>

Cada frase da descrição responde a uma pergunta: o que guarda cada personagem, com que valores se cria e o que se lhe pode pedir. A descrição vale para todas as personagens. O estado da alínea 3 é o de uma só, e por isso leva os valores dela.

</details>

## Exercício 2: "Tem" ou "é um"

Cria o script `tem_ou_e_um.py` e responde só com comentários. Para cada par, escreve a frase verdadeira: "A tem B" ou "A é um B". Se nenhuma das duas for verdadeira, escreve uma frase tua que diga como se relacionam.

1. Telemóvel e bateria.
2. Caneta e material de escrita.
3. Portátil e computador.
4. Artigo e inventário, por esta ordem.

Depois, responde a um colega. Para um programa da secretaria da escola, ele propõe que "a Turma é um Aluno, porque também tem um nome e um número". A classe `Aluno` desse programa descreve-se assim:

- Cada aluno guarda um nome, um número e a data de nascimento.
- Um aluno cria-se com esses três valores.
- A um aluno pode pedir-se que diga a sua idade, com `idade()`, e que receba uma nota numa disciplina, com `receber_nota(disciplina, nota)`.

Responde-lhe em três ou quatro frases, com o teste que o guia faz quando a frase "é um" parece quase certa.

Rever: [Duas perguntas sobre duas classes: "tem" e "é um"](../04-composicao-modelacao.md#duas-perguntas-sobre-duas-classes-tem-e-é-um).

<details>
<summary>Pista</summary>

Experimenta cada par nos dois sentidos, com as duas frases. Na resposta ao colega, pega em cada frase da descrição do `Aluno` e pergunta se faz sentido para uma turma.

</details>

## Exercício 3: Descobrir a relação a partir do código

Este programa junta o horário de uma turma e os clubes da escola:

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
        """Inscreve um aluno no clube."""
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

Copia-o para o script `horario_e_clubes.py`. Num comentário no fim do script, diz se cada relação é uma composição ou uma agregação. Justifica cada decisão com as duas perguntas que decidem. Para a pergunta "quem cria a parte?", copia também a linha do programa que lhe responde.

1. `Horario` com `Aula`.
2. `Clube` com `Aluno`.

Rever: [Dois graus de "tem": composição e agregação](../04-composicao-modelacao.md#dois-graus-de-tem-composição-e-agregação) e [Da descrição ao código, e do código à descrição](../04-composicao-modelacao.md#da-descrição-ao-código-e-do-código-à-descrição).

<details>
<summary>Pista</summary>

As duas classes guardam as partes numa lista, e por isso a lista não decide. Relê, no guia, como se vê no código quem cria a parte.

</details>

## Exercício 4: Um erro no encaminhamento

Este exercício e o desafio 2 usam as duas classes do [programa completo do exemplo guiado](../04-composicao-modelacao.md#passo-4-o-programa-completo-e-a-comparação-com-o-traço), `Artigo` e `Inventario`, sem as linhas que vêm depois delas:

```python
# As classes Artigo e Inventario do exemplo guiado do guia 04.

class Artigo:
    """Artigo do inventário: código, nome e uma quantidade sempre válida.

    É a classe final do guia 03, com as docstrings encurtadas.
    """

    def __init__(self, codigo, nome, quantidade):
        """Cria o artigo. A quantidade inicial passa pelo setter."""
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade

    @property
    def quantidade(self):
        """Getter: devolve a quantidade atual, sem a alterar."""
        return self._quantidade

    @quantidade.setter
    def quantidade(self, valor):
        """Setter: guarda o valor se for um inteiro não negativo; senão, lança ValueError."""
        if not isinstance(valor, int):
            raise ValueError("A quantidade tem de ser um número inteiro.")
        if valor < 0:
            raise ValueError("A quantidade não pode ser negativa.")
        self._quantidade = valor

    def adicionar(self, unidades):
        """Acrescenta unidades (inteiro, 1 ou mais); senão, lança ValueError."""
        if not isinstance(unidades, int):
            raise ValueError("As unidades a adicionar têm de ser um número inteiro.")
        if unidades <= 0:
            raise ValueError("As unidades a adicionar têm de ser 1 ou mais.")
        self.quantidade = self.quantidade + unidades

    def retirar(self, unidades):
        """Retira unidades (inteiro, 1 ou mais, até ao que existe); senão, lança ValueError."""
        if not isinstance(unidades, int):
            raise ValueError("As unidades a retirar têm de ser um número inteiro.")
        if unidades <= 0:
            raise ValueError("As unidades a retirar têm de ser 1 ou mais.")
        # A falta de unidades é recusada pelo setter: o resultado seria negativo.
        self.quantidade = self.quantidade - unidades


class Inventario:
    """Inventário que cria, guarda e controla os seus artigos.

    O inventário é o dono dos artigos: cria-os em registar e guarda-os numa
    lista interna, _artigos, que o código de fora não usa. Garante a regra
    que nenhum artigo consegue garantir sozinho: não há dois artigos com o
    mesmo código. Os pedidos sobre um artigo são encaminhados para esse
    artigo, que continua a proteger a sua própria quantidade.
    """

    def __init__(self):
        """Cria um inventário vazio, ainda sem artigos."""
        self._artigos = []

    def _procurar(self, codigo):
        """Método interno: devolve o artigo com este código.

        Falha: lança ValueError se não houver nenhum artigo com este código.
        """
        for artigo in self._artigos:
            if artigo.codigo == codigo:
                return artigo
        raise ValueError("Não existe nenhum artigo com o código " + codigo + ".")

    def registar(self, codigo, nome, quantidade):
        """Cria um artigo novo e guarda-o no inventário.

        Recebe: o código, o nome e a quantidade inicial do artigo.
        Devolve: nada (None).
        Falha: lança ValueError se já existir um artigo com este código, ou
        se a quantidade inicial for inválida (quem a recusa é o setter do
        artigo). Em qualquer falha, o inventário fica como estava.
        """
        for artigo in self._artigos:
            if artigo.codigo == codigo:
                raise ValueError("Já existe um artigo com o código " + codigo + ".")
        novo = Artigo(codigo, nome, quantidade)
        self._artigos.append(novo)

    def quantidade_de(self, codigo):
        """Devolve a quantidade do artigo com este código, sem a alterar.

        Falha: lança ValueError se não houver nenhum artigo com este código.
        """
        artigo = self._procurar(codigo)
        return artigo.quantidade

    def retirar(self, codigo, unidades):
        """Encaminha um pedido de retirada para o artigo com este código.

        Recebe: o código do artigo e as unidades a retirar.
        Devolve: nada (None).
        Falha: lança ValueError se não houver nenhum artigo com este código,
        ou se o próprio artigo recusar o pedido, pelas regras do seu método
        retirar. Em qualquer falha, nenhuma quantidade muda.
        """
        artigo = self._procurar(codigo)
        artigo.retirar(unidades)
```

Um colega escreveu esta versão do método `retirar` do inventário:

```python partial
    def retirar(self, codigo, unidades):
        """Retira unidades ao artigo com este código (versão com erro)."""
        for artigo in self._artigos:
            if artigo.codigo == codigo:
                artigo.retirar(unidades)
```

Testou-a com este programa principal:

```python partial
inventario = Inventario()
inventario.registar("A02", "Pasta", 2)
inventario.registar("A01", "Caderno", 6)

inventario.retirar("A01", 2)
print("Depois de retirar 2:", inventario.quantidade_de("A01"))

try:
    inventario.retirar("A01", 9)
except ValueError as erro:
    print("Retirar 9 recusado:", erro)
print("Depois de tentar retirar 9:", inventario.quantidade_de("A01"))
```

Retirar 2 deixou 4. Retirar 9 foi recusado com a mensagem "A quantidade não pode ser negativa.", e o caderno manteve as 4. Para o colega, o método está certo.

No script `encaminhamento.py`, copia as classes do início do exercício e troca o `retirar` do `Inventario`, o último método da classe, pelo do colega. Escreve por baixo o programa dele. Descobre um pedido de retirada que mostre o erro, e corrige o método. No fim, os três pedidos, os dois do colega e o teu, dão o que devem.

Num comentário no fim do script, escreve como encontraste e corrigiste o erro:

- o pedido que mostra o erro, o que devia acontecer, o que acontece e que tipo de erro é: de escrita, de execução ou de lógica;
- o que falta à versão do colega, e em que sítio do método o teu pedido devia ter sido recusado;
- o que mudaste no método, e como ficou;
- o que deram os três pedidos depois da correção.

Explica também, no mesmo comentário, porque é que os dois testes do colega não apanharam o erro.

Rever: [O inventário cria os artigos e encontra-os pelo código](../04-composicao-modelacao.md#o-inventário-cria-os-artigos-e-encontra-os-pelo-código), [O inventário passa os pedidos aos artigos](../04-composicao-modelacao.md#o-inventário-passa-os-pedidos-aos-artigos) e [Nada impede uma quantidade impossível](../03-encapsulamento-contratos.md#nada-impede-uma-quantidade-impossível).

<details>
<summary>Pista</summary>

Lê outra vez a docstring do `retirar` do `Inventario`, nas classes do início do exercício. Que pedidos promete ela recusar? O colega experimentou todos? Um pedido que não é recusado não mostra nada. Para veres o que aconteceu ao teu, põe um `print` logo a seguir a ele, dentro do `try`, como a linha `Aceite:` da ficha 03.

</details>

## Exercício 5: Descrever um modelo

Queremos descrever um programa para as requisições de material que os professores fazem ao armazém da escola. Cada requisição tem um número e uma data, e é formada por linhas. Cada linha diz o código de um artigo e as unidades pedidas, e não faz sentido fora da sua requisição.

Deves poder acrescentar a uma requisição o código de um artigo e as unidades: é a requisição que cria essa linha. Deves poder também anular uma requisição.

Cria o script `requisicao.py` e responde só com comentários.

1. Descreve por palavras as classes `Requisicao` e `LinhaRequisicao`, nas três partes que o guia usa para o inventário. Usa só o que o enunciado justifica, sem inventar mais nada.
2. Descreve a relação entre as duas classes: a frase "tem", se é uma composição ou uma agregação, e as respostas às duas perguntas que decidem.
3. O enunciado não diz o que acontece a uma requisição anulada. Pode desaparecer, com as suas linhas, ou ficar guardada, marcada como anulada, para se saber mais tarde o que foi pedido. Escolhe uma das duas, com a razão, e diz o que muda na tua descrição da `Requisicao`. As duas escolhas podem estar certas.

Rever: [O inventário descrito por palavras](../04-composicao-modelacao.md#o-inventário-descrito-por-palavras) e [Dois graus de "tem": composição e agregação](../04-composicao-modelacao.md#dois-graus-de-tem-composição-e-agregação).

<details>
<summary>Pista</summary>

Começa pela relação: procura no enunciado a frase que responde a cada uma das duas perguntas que decidem. Só depois descreves as classes. Na alínea 3, pensa no que a requisição tem de guardar em cada uma das duas escolhas.

</details>

## Desafios

### Desafio 1: Composição ou agregação

Em cada par, o primeiro é o todo e o segundo é a parte. Cria o script `pares.py` e responde só com comentários, com uma linha por par: a resposta às duas perguntas que decidem e a decisão.

1. Uma conversa de uma aplicação de mensagens e uma mensagem.
2. A equipa de futsal da escola e um aluno que joga nela.
3. O carrinho de compras de uma loja na internet e um produto.

Rever: [Dois graus de "tem": composição e agregação](../04-composicao-modelacao.md#dois-graus-de-tem-composição-e-agregação).

<details>
<summary>Pista</summary>

Imagina a aplicação a funcionar. Para a pergunta "quem cria a parte?", pensa no momento em que a parte aparece pela primeira vez na aplicação.

</details>

### Desafio 2: Seguir pedidos pelo inventário

No script `pedidos.py`, copia as classes do [exercício 4](#exercício-4-um-erro-no-encaminhamento), sem alterações, e escreve por baixo estas linhas:

```python partial
inventario = Inventario()
inventario.registar("A07", "Marcador", 5)

try:
    inventario.retirar("A07", 0)
except ValueError as erro:
    print("Pedido 1:", erro)

try:
    inventario.retirar("A06", 0)
except ValueError as erro:
    print("Pedido 2:", erro)

print("A07:", inventario.quantidade_de("A07"))
```

Descobre de cabeça o que o programa mostra, e executa para confirmares. Num comentário no fim do script, diz quem recusa cada pedido: o `_procurar` do inventário, o `retirar` do artigo ou o setter. O pedido 2 tem dois problemas: explica porque é que é esse método a recusá-lo, e não outro.

Rever: [O inventário passa os pedidos aos artigos](../04-composicao-modelacao.md#o-inventário-passa-os-pedidos-aos-artigos) e [O caminho de uma recusa](../04-composicao-modelacao.md#o-caminho-de-uma-recusa).

<details>
<summary>Pista</summary>

Segue cada pedido pelos métodos por onde passa, pela ordem em que correm. Em cada método, vê que verificações faz antes de passar o pedido ao seguinte.

</details>

### Desafio 3: Artigos arrumados em armários

A escola decide registar também em que armário está cada artigo. Um armário agrupa alguns artigos do inventário. Um artigo pode mudar de armário quando se arruma a sala. Se um armário for retirado da sala, os artigos que lá estavam continuam no inventário e passam para outro armário.

Cria o script `armarios.py` e responde só com comentários.

1. A relação entre `Armario` e `Artigo` é uma composição ou uma agregação? Justifica com as quatro perguntas do guia.
2. O artigo já pertence ao inventário, numa composição. Pode estar também ligado a um armário? Explica, a pensar em quem cria o artigo e em quem o guarda.

Rever: [Dois graus de "tem": composição e agregação](../04-composicao-modelacao.md#dois-graus-de-tem-composição-e-agregação) e [O nosso inventário: composição](../04-composicao-modelacao.md#o-nosso-inventário-composição).

<details>
<summary>Pista</summary>

Para a pergunta "quem cria a parte?", lembra-te de onde está, no programa do guia, a linha que cria cada artigo.

</details>

## Critérios de conclusão

- Fizeste os exercícios 1 a 5, cada um no seu script, com as respostas por palavras num comentário no fim.
- Em cada decisão, escreveste a razão, e não só a escolha.
- No exercício 4, o teu pedido é recusado depois da correção, e os dois pedidos do colega continuam a dar o mesmo.
- No exercício 5, a descrição da `Requisicao` está de acordo com o que escolheste para uma requisição anulada.

![Rodapé](../../imagens/rodape.png)

![Cabeçalho](../imagens/cabecalho.png)

# Temas para treinar em casa: resoluções

Aqui tens um programa em Python para cada um dos [temas de treino](temas-de-treino.md). Tenta primeiro fazer o teu, sozinho, e só depois compara.

O teu programa não tem de ser igual a este. Os nomes dos métodos podem ser outros, e há mais do que uma maneira certa de o organizar. O que tem de fazer é o mesmo: aceitar o que as regras deixam, recusar o resto com uma mensagem e não mudar nada quando recusa.

Os cinco programas usam classes, métodos, herança com `super()` e listas de objetos. Não usam o `raise`, nem o `try` e o `except`. Seguem sempre a mesma ideia:

- cada número com uma regra tem um método que diz se um valor serve, com `True` ou `False`, como `raridade_valida(valor)` nas cartas;
- o método `verificar()` diz o que está mal num registo novo: devolve a mensagem do primeiro problema, ou um texto vazio, `""`, se estiver tudo certo;
- a coleção só guarda um registo novo depois de o verificar e de confirmar que o código não se repete;
- cada pedido, como acrescentar, corrigir ou somar, devolve `""` quando é aceite, ou a mensagem da recusa, e o programa principal mostra-a com `mostrar_resultado`.

Na variante, `super().verificar()` e `super().descricao()` chamam os métodos da classe base, como `super().__init__` chama o construtor dela. Assim, as regras e a primeira parte da linha da lista escrevem-se num só sítio. Se escreveste a variante a repetir as verificações e a descrição, sem esse `super()`, também está certo. E se usaste o `raise`, o `try` e o `except`, como nos guias, também está certo.

Em quatro temas, a coleção cria os registos, como o inventário do guia 04 cria os artigos: é uma composição. Na playlist, as músicas são criadas fora e a playlist recebe-as já feitas: é uma agregação, como a playlist do guia 04.

## Coleção de jogos

Repara em duas coisas. As horas aceitam o 0, e a sessão que se soma também: uma sessão de 0 horas não muda nada. E a sessão verifica-se antes de se somar: sem isso, uma sessão de -2 horas baixava as horas do jogo.

### O programa

```python
# Coleção de jogos: a resolução em Python do tema de treino.
# O jogo guarda as horas jogadas, o jogo multijogador é um jogo com um dado a mais,
# e a coleção cria e guarda os jogos. Não há exceções: cada pedido devolve "" quando
# é aceite, ou a mensagem da recusa. No fim, o programa principal experimenta as
# operações aceites e as quatro recusas.


class Jogo:
    """Jogo da coleção: código, título e horas jogadas.

    As regras dos dados estão nesta classe: verificar() diz o que está mal num
    jogo novo, e somar_horas() só soma uma sessão válida. Uma variante que se
    descreva de outra maneira redefine descricao().
    """

    def __init__(self, codigo, titulo, horas):
        """Guarda os dados do jogo. Quem cria um jogo pede-lhe depois que se verifique."""
        self.codigo = codigo
        self.titulo = titulo
        self.horas = horas

    def horas_validas(self, valor):
        """Diz se o valor serve para horas: True se for um número inteiro, 0 ou mais."""
        if not isinstance(valor, int):
            return False
        return valor >= 0

    def verificar(self):
        """Verifica os dados do jogo.

        Devolve: "" se estiver tudo certo, ou a mensagem do primeiro problema.
        """
        # O strip tira os espaços das pontas: um título só com espaços também é vazio.
        if self.titulo.strip() == "":
            return "O título não pode ficar vazio."
        if not self.horas_validas(self.horas):
            return "As horas têm de ser um número inteiro, 0 ou mais."
        return ""

    def somar_horas(self, horas_da_sessao):
        """Soma as horas de uma sessão, se forem um número inteiro, 0 ou mais.

        Devolve: "" se as somou, ou a mensagem da recusa, e então as horas não mudam.
        """
        # A sessão verifica-se antes de se somar. Sem isto, uma sessão de -2 horas
        # baixava as horas do jogo.
        if not self.horas_validas(horas_da_sessao):
            return "As horas da sessão têm de ser um número inteiro, 0 ou mais."
        self.horas = self.horas + horas_da_sessao
        return ""

    def descricao(self):
        """Devolve a linha da lista, como "J01 Corrida Rápida, 12 horas"."""
        return self.codigo + " " + self.titulo + ", " + str(self.horas) + " horas"


class JogoMultijogador(Jogo):
    """Jogo multijogador: tudo o que um jogo tem e o número máximo de jogadores."""

    def __init__(self, codigo, titulo, horas, jogadores):
        """Guarda o código, o título e as horas, pelo construtor do jogo, e os jogadores."""
        super().__init__(codigo, titulo, horas)
        self.jogadores = jogadores

    def jogadores_validos(self, valor):
        """Diz se o valor serve para o número de jogadores: True se for um inteiro de 2 a 100."""
        if not isinstance(valor, int):
            return False
        return valor >= 2 and valor <= 100

    def verificar(self):
        """Verifica os dados como um jogo simples e, depois, o número de jogadores.

        Devolve: "" se estiver tudo certo, ou a mensagem do primeiro problema.
        """
        # super() dá acesso à versão da classe base de verificar(): as regras do
        # título e das horas ficam escritas num só sítio.
        mensagem = super().verificar()
        if mensagem != "":
            return mensagem
        if not self.jogadores_validos(self.jogadores):
            return "O número de jogadores tem de ser um número inteiro de 2 a 100."
        return ""

    def descricao(self):
        """Devolve a descrição de um jogo, com o máximo de jogadores no fim."""
        return super().descricao() + ", até " + str(self.jogadores) + " jogadores"


class ColecaoDeJogos:
    """Coleção que cria, guarda e controla os seus jogos.

    A coleção é a dona dos jogos: cria-os nos métodos acrescentar e guarda-os
    numa lista interna, _jogos, que o código de fora não usa. Só guarda um jogo
    que passou na verificação, e garante a regra que nenhum jogo consegue
    garantir sozinho: não há dois jogos com o mesmo código. Cada pedido
    devolve "" quando é aceite, ou a mensagem da recusa.
    """

    def __init__(self):
        """Cria uma coleção vazia, ainda sem jogos."""
        self._jogos = []

    def _codigo_existe(self, codigo):
        """Método interno: diz se já há um jogo com este código (True ou False)."""
        for jogo in self._jogos:
            if jogo.codigo == codigo:
                return True
        return False

    def _guardar(self, jogo):
        """Método interno: guarda um jogo novo, se o código estiver livre e os dados certos.

        Devolve: "" se o guardou, ou a mensagem da recusa, e então a coleção não muda.
        """
        if self._codigo_existe(jogo.codigo):
            return "Já existe um jogo com o código " + jogo.codigo + "."
        # Cada jogo usa o verificar() da sua classe: o multijogador também verifica os jogadores.
        mensagem = jogo.verificar()
        if mensagem != "":
            return mensagem
        self._jogos.append(jogo)
        return ""

    def acrescentar_jogo(self, codigo, titulo, horas):
        """Cria um jogo simples e guarda-o, se for válido. Devolve "" ou a mensagem da recusa."""
        return self._guardar(Jogo(codigo, titulo, horas))

    def acrescentar_multijogador(self, codigo, titulo, horas, jogadores):
        """Cria um jogo multijogador e guarda-o, se for válido. Devolve "" ou a mensagem da recusa."""
        return self._guardar(JogoMultijogador(codigo, titulo, horas, jogadores))

    def somar_horas(self, codigo, horas_da_sessao):
        """Encaminha para o jogo com este código as horas de uma sessão.

        Devolve: a resposta do jogo, ou a mensagem de que o código não existe.
        """
        for jogo in self._jogos:
            if jogo.codigo == codigo:
                return jogo.somar_horas(horas_da_sessao)
        return "Não existe nenhum jogo com o código " + codigo + "."

    def lista(self):
        """Devolve uma lista com a descrição de cada jogo, pela ordem em que entrou."""
        descricoes = []
        for jogo in self._jogos:
            # Cada jogo usa o descricao() da sua classe: o ciclo não pergunta o tipo.
            descricoes.append(jogo.descricao())
        return descricoes

    def com_mais_de_10_horas(self):
        """Devolve as descrições dos jogos com mais de 10 horas, sem mudar nenhum."""
        descricoes = []
        for jogo in self._jogos:
            if jogo.horas > 10:
                descricoes.append(jogo.descricao())
        return descricoes


def mostrar(titulo, descricoes):
    """Mostra um título e, por baixo, uma descrição por linha."""
    print(titulo)
    for descricao in descricoes:
        print("  " + descricao)


def mostrar_resultado(pedido, mensagem):
    """Mostra o pedido e diz se foi aceite ou, se foi recusado, porquê."""
    if mensagem == "":
        print(pedido + ": aceite.")
    else:
        print(pedido + ": recusado. " + mensagem)


colecao = ColecaoDeJogos()
mensagem = colecao.acrescentar_jogo("J01", "Corrida Rápida", 12)
mostrar_resultado("Acrescentar J01", mensagem)
mensagem = colecao.acrescentar_multijogador("J02", "Arena dos Heróis", 30, 8)
mostrar_resultado("Acrescentar J02", mensagem)
# O limite da regra: um jogo acabado de comprar tem 0 horas, e é aceite.
mensagem = colecao.acrescentar_jogo("J03", "Torre de Blocos", 0)
mostrar_resultado("Acrescentar J03", mensagem)
mostrar("Lista inicial:", colecao.lista())
mostrar("Com mais de 10 horas:", colecao.com_mais_de_10_horas())

# As quatro recusas: nenhuma muda a coleção.
mensagem = colecao.acrescentar_jogo("J01", "Pinguins no Gelo", 5)
mostrar_resultado("Acrescentar outro J01", mensagem)
mensagem = colecao.acrescentar_jogo("J04", "   ", 5)
mostrar_resultado("Acrescentar J04 sem título", mensagem)
mensagem = colecao.acrescentar_jogo("J04", "Pinguins no Gelo", -1)
mostrar_resultado("Acrescentar J04 com -1 horas", mensagem)
mensagem = colecao.acrescentar_multijogador("J04", "Pinguins no Gelo", 5, 1)
mostrar_resultado("Acrescentar J04 para 1 jogador", mensagem)

mensagem = colecao.somar_horas("J03", 11)
mostrar_resultado("Somar 11 horas a J03", mensagem)
mensagem = colecao.somar_horas("J03", -2)
mostrar_resultado("Somar -2 horas a J03", mensagem)

mostrar("Lista no fim:", colecao.lista())
mostrar("Com mais de 10 horas, no fim:", colecao.com_mais_de_10_horas())
```

### O que o programa mostra

```text
Acrescentar J01: aceite.
Acrescentar J02: aceite.
Acrescentar J03: aceite.
Lista inicial:
  J01 Corrida Rápida, 12 horas
  J02 Arena dos Heróis, 30 horas, até 8 jogadores
  J03 Torre de Blocos, 0 horas
Com mais de 10 horas:
  J01 Corrida Rápida, 12 horas
  J02 Arena dos Heróis, 30 horas, até 8 jogadores
Acrescentar outro J01: recusado. Já existe um jogo com o código J01.
Acrescentar J04 sem título: recusado. O título não pode ficar vazio.
Acrescentar J04 com -1 horas: recusado. As horas têm de ser um número inteiro, 0 ou mais.
Acrescentar J04 para 1 jogador: recusado. O número de jogadores tem de ser um número inteiro de 2 a 100.
Somar 11 horas a J03: aceite.
Somar -2 horas a J03: recusado. As horas da sessão têm de ser um número inteiro, 0 ou mais.
Lista no fim:
  J01 Corrida Rápida, 12 horas
  J02 Arena dos Heróis, 30 horas, até 8 jogadores
  J03 Torre de Blocos, 11 horas
Com mais de 10 horas, no fim:
  J01 Corrida Rápida, 12 horas
  J02 Arena dos Heróis, 30 horas, até 8 jogadores
  J03 Torre de Blocos, 11 horas
```

A sessão de 11 horas leva o J03 de 0 para 11 horas, e é por isso que ele entra nos jogos com mais de 10 horas. Nenhuma das cinco recusas mudou a lista.

## Cartas colecionáveis

A raridade tem dois limites, de 1 a 5, e `raridade_valida` verifica os dois. A correção da raridade usa o mesmo método, por isso a regra também vale quando se corrige. No filtro, "4 ou mais" escreve-se `>= 4`.

### O programa

```python
# Cartas colecionáveis: a resolução em Python do tema de treino.
# A carta guarda a raridade, de 1 a 5, a carta de edição limitada é uma carta com
# o número de cópias, e a coleção cria e guarda as cartas. Não há exceções: cada
# pedido devolve "" quando é aceite, ou a mensagem da recusa. No fim, o programa
# principal experimenta as operações aceites e as quatro recusas.


class Carta:
    """Carta da coleção: código, nome e raridade.

    As regras dos dados estão nesta classe: verificar() diz o que está mal numa
    carta nova, e corrigir_raridade() só aceita uma raridade válida. Uma
    variante que se descreva de outra maneira redefine descricao().
    """

    def __init__(self, codigo, nome, raridade):
        """Guarda os dados da carta. Quem cria uma carta pede-lhe depois que se verifique."""
        self.codigo = codigo
        self.nome = nome
        self.raridade = raridade

    def raridade_valida(self, valor):
        """Diz se o valor serve para raridade: True se for um número inteiro de 1 a 5."""
        if not isinstance(valor, int):
            return False
        return valor >= 1 and valor <= 5

    def verificar(self):
        """Verifica os dados da carta.

        Devolve: "" se estiver tudo certo, ou a mensagem do primeiro problema.
        """
        # O strip tira os espaços das pontas: um nome só com espaços também é vazio.
        if self.nome.strip() == "":
            return "O nome não pode ficar vazio."
        if not self.raridade_valida(self.raridade):
            return "A raridade tem de ser um número inteiro de 1 a 5."
        return ""

    def corrigir_raridade(self, valor):
        """Muda a raridade, se o valor for um número inteiro de 1 a 5.

        Devolve: "" se a mudou, ou a mensagem da recusa, e então a raridade não muda.
        """
        # A mesma regra de verificar(): uma correção não pode estragar a carta.
        if not self.raridade_valida(valor):
            return "A raridade tem de ser um número inteiro de 1 a 5."
        self.raridade = valor
        return ""

    def descricao(self):
        """Devolve a linha da lista, como "C001 Lobo da Neve, raridade 3"."""
        return self.codigo + " " + self.nome + ", raridade " + str(self.raridade)


class CartaEdicaoLimitada(Carta):
    """Carta de edição limitada: tudo o que uma carta tem e o número de cópias."""

    def __init__(self, codigo, nome, raridade, copias):
        """Guarda o código, o nome e a raridade, pelo construtor da carta, e as cópias."""
        super().__init__(codigo, nome, raridade)
        self.copias = copias

    def copias_validas(self, valor):
        """Diz se o valor serve para o número de cópias: True se for um inteiro de 1 a 1000."""
        if not isinstance(valor, int):
            return False
        return valor >= 1 and valor <= 1000

    def verificar(self):
        """Verifica os dados como uma carta simples e, depois, as cópias.

        Devolve: "" se estiver tudo certo, ou a mensagem do primeiro problema.
        """
        # super() dá acesso à versão da classe base de verificar(): as regras do
        # nome e da raridade ficam escritas num só sítio.
        mensagem = super().verificar()
        if mensagem != "":
            return mensagem
        if not self.copias_validas(self.copias):
            return "O número de cópias tem de ser um número inteiro de 1 a 1000."
        return ""

    def descricao(self):
        """Devolve a descrição de uma carta, com o número de cópias no fim."""
        return super().descricao() + ", edição de " + str(self.copias) + " cópias"


class ColecaoDeCartas:
    """Coleção que cria, guarda e controla as suas cartas.

    A coleção é a dona das cartas: cria-as nos métodos acrescentar e guarda-as
    numa lista interna, _cartas, que o código de fora não usa. Só guarda uma
    carta que passou na verificação, e garante que não há duas cartas com o
    mesmo código. Cada pedido devolve "" quando é aceite, ou a mensagem da recusa.
    """

    def __init__(self):
        """Cria uma coleção vazia, ainda sem cartas."""
        self._cartas = []

    def _codigo_existe(self, codigo):
        """Método interno: diz se já há uma carta com este código (True ou False)."""
        for carta in self._cartas:
            if carta.codigo == codigo:
                return True
        return False

    def _guardar(self, carta):
        """Método interno: guarda uma carta nova, se o código estiver livre e os dados certos.

        Devolve: "" se a guardou, ou a mensagem da recusa, e então a coleção não muda.
        """
        if self._codigo_existe(carta.codigo):
            return "Já existe uma carta com o código " + carta.codigo + "."
        # Cada carta usa o verificar() da sua classe: a de edição limitada também verifica as cópias.
        mensagem = carta.verificar()
        if mensagem != "":
            return mensagem
        self._cartas.append(carta)
        return ""

    def acrescentar_carta(self, codigo, nome, raridade):
        """Cria uma carta simples e guarda-a, se for válida. Devolve "" ou a mensagem da recusa."""
        return self._guardar(Carta(codigo, nome, raridade))

    def acrescentar_edicao_limitada(self, codigo, nome, raridade, copias):
        """Cria uma carta de edição limitada e guarda-a, se for válida. Devolve "" ou a mensagem."""
        return self._guardar(CartaEdicaoLimitada(codigo, nome, raridade, copias))

    def corrigir_raridade(self, codigo, raridade):
        """Encaminha para a carta com este código a correção da raridade.

        Devolve: a resposta da carta, ou a mensagem de que o código não existe.
        """
        for carta in self._cartas:
            if carta.codigo == codigo:
                return carta.corrigir_raridade(raridade)
        return "Não existe nenhuma carta com o código " + codigo + "."

    def lista(self):
        """Devolve uma lista com a descrição de cada carta, pela ordem em que entrou."""
        descricoes = []
        for carta in self._cartas:
            # Cada carta usa o descricao() da sua classe: o ciclo não pergunta o tipo.
            descricoes.append(carta.descricao())
        return descricoes

    def de_raridade_4_ou_mais(self):
        """Devolve as descrições das cartas de raridade 4 ou 5, sem mudar nenhuma."""
        descricoes = []
        for carta in self._cartas:
            # ">= 4", e não "> 4": as cartas de raridade 4 também entram.
            if carta.raridade >= 4:
                descricoes.append(carta.descricao())
        return descricoes


def mostrar(titulo, descricoes):
    """Mostra um título e, por baixo, uma descrição por linha."""
    print(titulo)
    for descricao in descricoes:
        print("  " + descricao)


def mostrar_resultado(pedido, mensagem):
    """Mostra o pedido e diz se foi aceite ou, se foi recusado, porquê."""
    if mensagem == "":
        print(pedido + ": aceite.")
    else:
        print(pedido + ": recusado. " + mensagem)


colecao = ColecaoDeCartas()
mensagem = colecao.acrescentar_carta("C001", "Lobo da Neve", 3)
mostrar_resultado("Acrescentar C001", mensagem)
mensagem = colecao.acrescentar_edicao_limitada("C002", "Dragão Dourado", 5, 250)
mostrar_resultado("Acrescentar C002", mensagem)
# O limite de baixo da raridade: 1 é aceite.
mensagem = colecao.acrescentar_carta("C003", "Rato do Celeiro", 1)
mostrar_resultado("Acrescentar C003", mensagem)
mostrar("Lista inicial:", colecao.lista())
mostrar("De raridade 4 ou mais:", colecao.de_raridade_4_ou_mais())

# As quatro recusas: nenhuma muda a coleção.
mensagem = colecao.acrescentar_carta("C001", "Coruja Branca", 2)
mostrar_resultado("Acrescentar outra C001", mensagem)
mensagem = colecao.acrescentar_carta("C004", "", 2)
mostrar_resultado("Acrescentar C004 sem nome", mensagem)
mensagem = colecao.acrescentar_carta("C004", "Coruja Branca", 6)
mostrar_resultado("Acrescentar C004 de raridade 6", mensagem)
mensagem = colecao.acrescentar_edicao_limitada("C004", "Coruja Branca", 2, 1001)
mostrar_resultado("Acrescentar C004 com 1001 cópias", mensagem)

mensagem = colecao.corrigir_raridade("C001", 4)
mostrar_resultado("Corrigir a raridade de C001 para 4", mensagem)
mensagem = colecao.corrigir_raridade("C001", 0)
mostrar_resultado("Corrigir a raridade de C001 para 0", mensagem)

mostrar("Lista no fim:", colecao.lista())
mostrar("De raridade 4 ou mais, no fim:", colecao.de_raridade_4_ou_mais())
```

### O que o programa mostra

```text
Acrescentar C001: aceite.
Acrescentar C002: aceite.
Acrescentar C003: aceite.
Lista inicial:
  C001 Lobo da Neve, raridade 3
  C002 Dragão Dourado, raridade 5, edição de 250 cópias
  C003 Rato do Celeiro, raridade 1
De raridade 4 ou mais:
  C002 Dragão Dourado, raridade 5, edição de 250 cópias
Acrescentar outra C001: recusado. Já existe uma carta com o código C001.
Acrescentar C004 sem nome: recusado. O nome não pode ficar vazio.
Acrescentar C004 de raridade 6: recusado. A raridade tem de ser um número inteiro de 1 a 5.
Acrescentar C004 com 1001 cópias: recusado. O número de cópias tem de ser um número inteiro de 1 a 1000.
Corrigir a raridade de C001 para 4: aceite.
Corrigir a raridade de C001 para 0: recusado. A raridade tem de ser um número inteiro de 1 a 5.
Lista no fim:
  C001 Lobo da Neve, raridade 4
  C002 Dragão Dourado, raridade 5, edição de 250 cópias
  C003 Rato do Celeiro, raridade 1
De raridade 4 ou mais, no fim:
  C001 Lobo da Neve, raridade 4
  C002 Dragão Dourado, raridade 5, edição de 250 cópias
```

Antes da correção, só a C002 é de raridade 4 ou mais. Depois de a C001 passar a raridade 4, entra também, porque o filtro inclui o 4.

## Diário de treinos

A duração não aceita o 0, ao contrário da quantidade do inventário dos guias, e por isso a comparação é `valor > 0`. No filtro, "mais de 30 minutos" deixa de fora um treino de 30 minutos certos.

### O programa

```python
# Diário de treinos: a resolução em Python do tema de treino.
# O treino guarda a duração, o treino com distância é um treino com os metros
# percorridos, e o diário cria e guarda os treinos. Não há exceções: cada pedido
# devolve "" quando é aceite, ou a mensagem da recusa. No fim, o programa
# principal experimenta as operações aceites e as quatro recusas.


class Treino:
    """Treino do diário: código, atividade e duração em minutos.

    As regras dos dados estão nesta classe: verificar() diz o que está mal num
    treino novo, e corrigir_duracao() só aceita uma duração válida. Uma
    variante que se descreva de outra maneira redefine descricao().
    """

    def __init__(self, codigo, atividade, duracao):
        """Guarda os dados do treino. Quem cria um treino pede-lhe depois que se verifique."""
        self.codigo = codigo
        self.atividade = atividade
        self.duracao = duracao

    def duracao_valida(self, valor):
        """Diz se o valor serve para duração: True se for um número inteiro maior do que 0."""
        if not isinstance(valor, int):
            return False
        # "> 0", e não ">= 0": ao contrário da quantidade do inventário, o 0 é recusado.
        return valor > 0

    def verificar(self):
        """Verifica os dados do treino.

        Devolve: "" se estiver tudo certo, ou a mensagem do primeiro problema.
        """
        # O strip tira os espaços das pontas: uma atividade só com espaços também é vazia.
        if self.atividade.strip() == "":
            return "A atividade não pode ficar vazia."
        if not self.duracao_valida(self.duracao):
            return "A duração tem de ser um número inteiro maior do que 0."
        return ""

    def corrigir_duracao(self, valor):
        """Muda a duração, se o valor for um número inteiro maior do que 0.

        Devolve: "" se a mudou, ou a mensagem da recusa, e então a duração não muda.
        """
        # A mesma regra de verificar(): uma correção não pode estragar o treino.
        if not self.duracao_valida(valor):
            return "A duração tem de ser um número inteiro maior do que 0."
        self.duracao = valor
        return ""

    def descricao(self):
        """Devolve a linha da lista, como "T01 Ginásio, 45 minutos"."""
        return self.codigo + " " + self.atividade + ", " + str(self.duracao) + " minutos"


class TreinoComDistancia(Treino):
    """Treino com distância: tudo o que um treino tem e a distância em metros."""

    def __init__(self, codigo, atividade, duracao, distancia):
        """Guarda o código, a atividade e a duração, pelo construtor do treino, e a distância."""
        super().__init__(codigo, atividade, duracao)
        self.distancia = distancia

    def distancia_valida(self, valor):
        """Diz se o valor serve para distância: True se for um número inteiro maior do que 0."""
        if not isinstance(valor, int):
            return False
        return valor > 0

    def verificar(self):
        """Verifica os dados como um treino simples e, depois, a distância.

        Devolve: "" se estiver tudo certo, ou a mensagem do primeiro problema.
        """
        # super() dá acesso à versão da classe base de verificar(): as regras da
        # atividade e da duração ficam escritas num só sítio.
        mensagem = super().verificar()
        if mensagem != "":
            return mensagem
        if not self.distancia_valida(self.distancia):
            return "A distância tem de ser um número inteiro de metros maior do que 0."
        return ""

    def descricao(self):
        """Devolve a descrição de um treino, com a distância no fim."""
        return super().descricao() + ", " + str(self.distancia) + " metros"


class DiarioDeTreinos:
    """Diário que cria, guarda e controla os seus treinos.

    O diário é o dono dos treinos: cria-os nos métodos acrescentar e guarda-os
    numa lista interna, _treinos, que o código de fora não usa. Só guarda um
    treino que passou na verificação, e garante que não há dois treinos com o
    mesmo código. Cada pedido devolve "" quando é aceite, ou a mensagem da recusa.
    """

    def __init__(self):
        """Cria um diário vazio, ainda sem treinos."""
        self._treinos = []

    def _codigo_existe(self, codigo):
        """Método interno: diz se já há um treino com este código (True ou False)."""
        for treino in self._treinos:
            if treino.codigo == codigo:
                return True
        return False

    def _guardar(self, treino):
        """Método interno: guarda um treino novo, se o código estiver livre e os dados certos.

        Devolve: "" se o guardou, ou a mensagem da recusa, e então o diário não muda.
        """
        if self._codigo_existe(treino.codigo):
            return "Já existe um treino com o código " + treino.codigo + "."
        # Cada treino usa o verificar() da sua classe: o com distância também verifica os metros.
        mensagem = treino.verificar()
        if mensagem != "":
            return mensagem
        self._treinos.append(treino)
        return ""

    def acrescentar_treino(self, codigo, atividade, duracao):
        """Cria um treino simples e guarda-o, se for válido. Devolve "" ou a mensagem da recusa."""
        return self._guardar(Treino(codigo, atividade, duracao))

    def acrescentar_com_distancia(self, codigo, atividade, duracao, distancia):
        """Cria um treino com distância e guarda-o, se for válido. Devolve "" ou a mensagem."""
        return self._guardar(TreinoComDistancia(codigo, atividade, duracao, distancia))

    def corrigir_duracao(self, codigo, duracao):
        """Encaminha para o treino com este código a correção da duração.

        Devolve: a resposta do treino, ou a mensagem de que o código não existe.
        """
        for treino in self._treinos:
            if treino.codigo == codigo:
                return treino.corrigir_duracao(duracao)
        return "Não existe nenhum treino com o código " + codigo + "."

    def lista(self):
        """Devolve uma lista com a descrição de cada treino, pela ordem em que entrou."""
        descricoes = []
        for treino in self._treinos:
            # Cada treino usa o descricao() da sua classe: o ciclo não pergunta o tipo.
            descricoes.append(treino.descricao())
        return descricoes

    def com_mais_de_30_minutos(self):
        """Devolve as descrições dos treinos de mais de 30 minutos, sem mudar nenhum."""
        descricoes = []
        for treino in self._treinos:
            # "> 30": um treino de 30 minutos certos não é de mais de 30 minutos.
            if treino.duracao > 30:
                descricoes.append(treino.descricao())
        return descricoes


def mostrar(titulo, descricoes):
    """Mostra um título e, por baixo, uma descrição por linha."""
    print(titulo)
    for descricao in descricoes:
        print("  " + descricao)


def mostrar_resultado(pedido, mensagem):
    """Mostra o pedido e diz se foi aceite ou, se foi recusado, porquê."""
    if mensagem == "":
        print(pedido + ": aceite.")
    else:
        print(pedido + ": recusado. " + mensagem)


diario = DiarioDeTreinos()
mensagem = diario.acrescentar_treino("T01", "Ginásio", 45)
mostrar_resultado("Acrescentar T01", mensagem)
mensagem = diario.acrescentar_com_distancia("T02", "Corrida", 30, 5000)
mostrar_resultado("Acrescentar T02", mensagem)
mostrar("Lista inicial:", diario.lista())
# T02 tem 30 minutos certos: ainda não é um treino de mais de 30 minutos.
mostrar("Com mais de 30 minutos:", diario.com_mais_de_30_minutos())

# As quatro recusas: nenhuma muda o diário.
mensagem = diario.acrescentar_treino("T01", "Natação", 40)
mostrar_resultado("Acrescentar outro T01", mensagem)
mensagem = diario.acrescentar_treino("T03", "", 40)
mostrar_resultado("Acrescentar T03 sem atividade", mensagem)
mensagem = diario.acrescentar_treino("T03", "Natação", 0)
mostrar_resultado("Acrescentar T03 com 0 minutos", mensagem)
mensagem = diario.acrescentar_com_distancia("T03", "Bicicleta", 60, 0)
mostrar_resultado("Acrescentar T03 com 0 metros", mensagem)

mensagem = diario.corrigir_duracao("T02", 35)
mostrar_resultado("Corrigir a duração de T02 para 35", mensagem)
mensagem = diario.corrigir_duracao("T02", 0)
mostrar_resultado("Corrigir a duração de T02 para 0", mensagem)

mostrar("Lista no fim:", diario.lista())
mostrar("Com mais de 30 minutos, no fim:", diario.com_mais_de_30_minutos())
```

### O que o programa mostra

```text
Acrescentar T01: aceite.
Acrescentar T02: aceite.
Lista inicial:
  T01 Ginásio, 45 minutos
  T02 Corrida, 30 minutos, 5000 metros
Com mais de 30 minutos:
  T01 Ginásio, 45 minutos
Acrescentar outro T01: recusado. Já existe um treino com o código T01.
Acrescentar T03 sem atividade: recusado. A atividade não pode ficar vazia.
Acrescentar T03 com 0 minutos: recusado. A duração tem de ser um número inteiro maior do que 0.
Acrescentar T03 com 0 metros: recusado. A distância tem de ser um número inteiro de metros maior do que 0.
Corrigir a duração de T02 para 35: aceite.
Corrigir a duração de T02 para 0: recusado. A duração tem de ser um número inteiro maior do que 0.
Lista no fim:
  T01 Ginásio, 45 minutos
  T02 Corrida, 35 minutos, 5000 metros
Com mais de 30 minutos, no fim:
  T01 Ginásio, 45 minutos
  T02 Corrida, 35 minutos, 5000 metros
```

No princípio, o T02 tem 30 minutos certos e fica de fora do filtro. Depois da correção para 35 minutos, entra.

## Playlist

Aqui, a playlist não cria as músicas: recebe-as já criadas. Uma música errada chega a ser criada, mas a playlist verifica-a antes de a guardar e recusa-a. A mesma música pode estar em duas playlists.

### O programa

```python
# Playlist: a resolução em Python do tema de treino.
# A música guarda a duração em segundos, a música de um álbum é uma música com o
# número da faixa, e a playlist reúne músicas que já existem: é uma agregação, como
# a playlist do guia 04. Não há exceções: cada pedido devolve "" quando é aceite,
# ou a mensagem da recusa. No fim, o programa principal experimenta as operações
# aceites, as quatro recusas e a mesma música em duas playlists.


class Musica:
    """Música: código, título e duração em segundos.

    As regras dos dados estão nesta classe: verificar() diz o que está mal numa
    música, e corrigir_duracao() só aceita uma duração válida. Uma variante que
    se descreva de outra maneira redefine descricao().
    """

    def __init__(self, codigo, titulo, duracao):
        """Guarda os dados da música. A playlist verifica-a antes de a guardar."""
        self.codigo = codigo
        self.titulo = titulo
        self.duracao = duracao

    def duracao_valida(self, valor):
        """Diz se o valor serve para duração: True se for um número inteiro maior do que 0."""
        if not isinstance(valor, int):
            return False
        return valor > 0

    def verificar(self):
        """Verifica os dados da música.

        Devolve: "" se estiver tudo certo, ou a mensagem do primeiro problema.
        """
        # O strip tira os espaços das pontas: um título só com espaços também é vazio.
        if self.titulo.strip() == "":
            return "O título não pode ficar vazio."
        if not self.duracao_valida(self.duracao):
            return "A duração tem de ser um número inteiro de segundos maior do que 0."
        return ""

    def corrigir_duracao(self, valor):
        """Muda a duração, se o valor for um número inteiro maior do que 0.

        Devolve: "" se a mudou, ou a mensagem da recusa, e então a duração não muda.
        """
        # A mesma regra de verificar(): uma correção não pode estragar a música.
        if not self.duracao_valida(valor):
            return "A duração tem de ser um número inteiro de segundos maior do que 0."
        self.duracao = valor
        return ""

    def descricao(self):
        """Devolve a linha da lista, como "M01 Noite de Verão, 200 segundos"."""
        return self.codigo + " " + self.titulo + ", " + str(self.duracao) + " segundos"


class MusicaDeAlbum(Musica):
    """Música de um álbum: tudo o que uma música tem e o número da faixa."""

    def __init__(self, codigo, titulo, duracao, faixa):
        """Guarda o código, o título e a duração, pelo construtor da música, e a faixa."""
        super().__init__(codigo, titulo, duracao)
        self.faixa = faixa

    def faixa_valida(self, valor):
        """Diz se o valor serve para faixa: True se for um número inteiro de 1 a 30."""
        if not isinstance(valor, int):
            return False
        return valor >= 1 and valor <= 30

    def verificar(self):
        """Verifica os dados como uma música solta e, depois, a faixa.

        Devolve: "" se estiver tudo certo, ou a mensagem do primeiro problema.
        """
        # super() dá acesso à versão da classe base de verificar(): as regras do
        # título e da duração ficam escritas num só sítio.
        mensagem = super().verificar()
        if mensagem != "":
            return mensagem
        if not self.faixa_valida(self.faixa):
            return "A faixa tem de ser um número inteiro de 1 a 30."
        return ""

    def descricao(self):
        """Devolve a descrição de uma música, com o número da faixa no fim."""
        return super().descricao() + ", faixa " + str(self.faixa)


class Playlist:
    """Playlist que agrega músicas: não as cria, recebe-as já criadas.

    Guarda as músicas numa lista interna, _musicas, que o código de fora não
    usa. Só guarda uma música que passou na verificação, e nunca duas com o
    mesmo código. A mesma música pode estar em várias playlists, e continua a
    existir se uma playlist desaparecer. Cada pedido devolve "" quando é
    aceite, ou a mensagem da recusa.
    """

    def __init__(self, nome):
        """Cria uma playlist vazia, com este nome (texto)."""
        self.nome = nome
        self._musicas = []

    def _codigo_existe(self, codigo):
        """Método interno: diz se já há uma música com este código (True ou False)."""
        for musica in self._musicas:
            if musica.codigo == codigo:
                return True
        return False

    def acrescentar(self, musica):
        """Junta à playlist uma música já criada, simples ou de um álbum, se for válida.

        Devolve: "" se a juntou, ou a mensagem da recusa, e então a playlist não muda.
        """
        if self._codigo_existe(musica.codigo):
            return "Já existe uma música com o código " + musica.codigo + "."
        # Cada música usa o verificar() da sua classe: a de um álbum também verifica a faixa.
        mensagem = musica.verificar()
        if mensagem != "":
            return mensagem
        self._musicas.append(musica)
        return ""

    def corrigir_duracao(self, codigo, duracao):
        """Encaminha para a música com este código a correção da duração.

        Devolve: a resposta da música, ou a mensagem de que o código não existe.
        """
        for musica in self._musicas:
            if musica.codigo == codigo:
                return musica.corrigir_duracao(duracao)
        return "Não existe nenhuma música com o código " + codigo + "."

    def lista(self):
        """Devolve uma lista com a descrição de cada música, pela ordem em que entrou."""
        descricoes = []
        for musica in self._musicas:
            # Cada música usa o descricao() da sua classe: o ciclo não pergunta o tipo.
            descricoes.append(musica.descricao())
        return descricoes

    def com_mais_de_4_minutos(self):
        """Devolve as descrições das músicas com mais de 240 segundos, sem mudar nenhuma."""
        descricoes = []
        for musica in self._musicas:
            # 4 minutos são 240 segundos; "> 240" deixa de fora uma música de 4 minutos certos.
            if musica.duracao > 240:
                descricoes.append(musica.descricao())
        return descricoes


def mostrar(titulo, descricoes):
    """Mostra um título e, por baixo, uma descrição por linha."""
    print(titulo)
    for descricao in descricoes:
        print("  " + descricao)


def mostrar_resultado(pedido, mensagem):
    """Mostra o pedido e diz se foi aceite ou, se foi recusado, porquê."""
    if mensagem == "":
        print(pedido + ": aceite.")
    else:
        print(pedido + ": recusado. " + mensagem)


# Numa agregação, as músicas criam-se fora da playlist, e só depois se juntam.
noite = Musica("M01", "Noite de Verão", 200)
tempestade = MusicaDeAlbum("M02", "Tempestade", 245, 3)

para_estudar = Playlist("Para estudar")
mostrar_resultado("Acrescentar M01", para_estudar.acrescentar(noite))
mostrar_resultado("Acrescentar M02", para_estudar.acrescentar(tempestade))
mostrar("Lista inicial:", para_estudar.lista())
mostrar("Com mais de 4 minutos:", para_estudar.com_mais_de_4_minutos())

# As quatro recusas. Uma música errada chega a ser criada, mas a playlist
# verifica-a e não a guarda: a playlist não muda.
mensagem = para_estudar.acrescentar(Musica("M01", "Chuva Miúda", 180))
mostrar_resultado("Acrescentar outra M01", mensagem)
mensagem = para_estudar.acrescentar(Musica("M03", "", 180))
mostrar_resultado("Acrescentar M03 sem título", mensagem)
mensagem = para_estudar.acrescentar(Musica("M03", "Chuva Miúda", 0))
mostrar_resultado("Acrescentar M03 com 0 segundos", mensagem)
mensagem = para_estudar.acrescentar(MusicaDeAlbum("M03", "Chuva Miúda", 180, 31))
mostrar_resultado("Acrescentar M03 na faixa 31", mensagem)

mensagem = para_estudar.corrigir_duracao("M01", 250)
mostrar_resultado("Corrigir a duração de M01 para 250", mensagem)
mensagem = para_estudar.corrigir_duracao("M01", 0)
mostrar_resultado("Corrigir a duração de M01 para 0", mensagem)

mostrar("Lista no fim:", para_estudar.lista())
mostrar("Com mais de 4 minutos, no fim:", para_estudar.com_mais_de_4_minutos())

# A mesma música noutra playlist: é o mesmo objeto, e não uma cópia. A correção
# feita pela playlist "Para estudar" também se vê aqui.
para_correr = Playlist("Para correr")
mostrar_resultado("Acrescentar M01 a Para correr", para_correr.acrescentar(noite))
mostrar("Para correr:", para_correr.lista())
```

### O que o programa mostra

```text
Acrescentar M01: aceite.
Acrescentar M02: aceite.
Lista inicial:
  M01 Noite de Verão, 200 segundos
  M02 Tempestade, 245 segundos, faixa 3
Com mais de 4 minutos:
  M02 Tempestade, 245 segundos, faixa 3
Acrescentar outra M01: recusado. Já existe uma música com o código M01.
Acrescentar M03 sem título: recusado. O título não pode ficar vazio.
Acrescentar M03 com 0 segundos: recusado. A duração tem de ser um número inteiro de segundos maior do que 0.
Acrescentar M03 na faixa 31: recusado. A faixa tem de ser um número inteiro de 1 a 30.
Corrigir a duração de M01 para 250: aceite.
Corrigir a duração de M01 para 0: recusado. A duração tem de ser um número inteiro de segundos maior do que 0.
Lista no fim:
  M01 Noite de Verão, 250 segundos
  M02 Tempestade, 245 segundos, faixa 3
Com mais de 4 minutos, no fim:
  M01 Noite de Verão, 250 segundos
  M02 Tempestade, 245 segundos, faixa 3
Acrescentar M01 a Para correr: aceite.
Para correr:
  M01 Noite de Verão, 250 segundos
```

As três últimas linhas mostram a agregação. A playlist "Para correr" recebeu a mesma música, e não uma cópia, por isso já tem os 250 segundos da correção feita pela playlist "Para estudar".

## Campeonato

A sigla faz o papel do código. Os pontos de um jogo aceitam o 0, de um jogo perdido, e verificam-se antes de se somarem, como as horas da sessão nos jogos. Em Python, os 90 000 lugares escrevem-se `90000`, sem espaço nem ponto: `90.000` seria o número decimal 90,0.

### O programa

```python
# Campeonato: a resolução em Python do tema de treino.
# A equipa guarda os pontos, a equipa com estádio é uma equipa com os lugares do
# estádio, e o campeonato cria e guarda as equipas. Não há exceções: cada pedido
# devolve "" quando é aceite, ou a mensagem da recusa. No fim, o programa
# principal experimenta as operações aceites e as quatro recusas.


class Equipa:
    """Equipa do campeonato: sigla, nome e pontos.

    As regras dos dados estão nesta classe: verificar() diz o que está mal numa
    equipa nova, e somar_pontos() só soma os pontos válidos de um jogo. Uma
    variante que se descreva de outra maneira redefine descricao().
    """

    def __init__(self, sigla, nome, pontos):
        """Guarda os dados da equipa. Quem cria uma equipa pede-lhe depois que se verifique."""
        self.sigla = sigla
        self.nome = nome
        self.pontos = pontos

    def pontos_validos(self, valor):
        """Diz se o valor serve para pontos: True se for um número inteiro, 0 ou mais."""
        if not isinstance(valor, int):
            return False
        return valor >= 0

    def verificar(self):
        """Verifica os dados da equipa.

        Devolve: "" se estiver tudo certo, ou a mensagem do primeiro problema.
        """
        # O strip tira os espaços das pontas: um nome só com espaços também é vazio.
        if self.nome.strip() == "":
            return "O nome não pode ficar vazio."
        if not self.pontos_validos(self.pontos):
            return "Os pontos têm de ser um número inteiro, 0 ou mais."
        return ""

    def somar_pontos(self, pontos_do_jogo):
        """Soma os pontos ganhos num jogo, se forem um número inteiro, 0 ou mais.

        Devolve: "" se os somou, ou a mensagem da recusa, e então os pontos não mudam.
        """
        # Os pontos do jogo verificam-se antes de se somarem. Sem isto, um jogo de
        # -3 pontos baixava os pontos da equipa.
        if not self.pontos_validos(pontos_do_jogo):
            return "Os pontos do jogo têm de ser um número inteiro, 0 ou mais."
        self.pontos = self.pontos + pontos_do_jogo
        return ""

    def descricao(self):
        """Devolve a linha da lista, como "LBO Leões do Bairro, 12 pontos"."""
        return self.sigla + " " + self.nome + ", " + str(self.pontos) + " pontos"


class EquipaComEstadio(Equipa):
    """Equipa com estádio: tudo o que uma equipa tem e os lugares do estádio."""

    def __init__(self, sigla, nome, pontos, lugares):
        """Guarda a sigla, o nome e os pontos, pelo construtor da equipa, e os lugares."""
        super().__init__(sigla, nome, pontos)
        self.lugares = lugares

    def lugares_validos(self, valor):
        """Diz se o valor serve para lugares: True se for um número inteiro de 500 a 90000."""
        if not isinstance(valor, int):
            return False
        return valor >= 500 and valor <= 90000

    def verificar(self):
        """Verifica os dados como uma equipa sem estádio e, depois, os lugares.

        Devolve: "" se estiver tudo certo, ou a mensagem do primeiro problema.
        """
        # super() dá acesso à versão da classe base de verificar(): as regras do
        # nome e dos pontos ficam escritas num só sítio.
        mensagem = super().verificar()
        if mensagem != "":
            return mensagem
        if not self.lugares_validos(self.lugares):
            return "Os lugares têm de ser um número inteiro de 500 a 90000."
        return ""

    def descricao(self):
        """Devolve a descrição de uma equipa, com os lugares do estádio no fim."""
        return super().descricao() + ", estádio de " + str(self.lugares) + " lugares"


class Campeonato:
    """Campeonato que cria, guarda e controla as suas equipas.

    O campeonato é o dono das equipas: cria-as nos métodos acrescentar e
    guarda-as numa lista interna, _equipas, que o código de fora não usa. Só
    guarda uma equipa que passou na verificação, e garante que não há duas
    equipas com a mesma sigla. Cada pedido devolve "" quando é aceite, ou a
    mensagem da recusa.
    """

    def __init__(self):
        """Cria um campeonato vazio, ainda sem equipas."""
        self._equipas = []

    def _sigla_existe(self, sigla):
        """Método interno: diz se já há uma equipa com esta sigla (True ou False)."""
        for equipa in self._equipas:
            if equipa.sigla == sigla:
                return True
        return False

    def _guardar(self, equipa):
        """Método interno: guarda uma equipa nova, se a sigla estiver livre e os dados certos.

        Devolve: "" se a guardou, ou a mensagem da recusa, e então o campeonato não muda.
        """
        if self._sigla_existe(equipa.sigla):
            return "Já existe uma equipa com a sigla " + equipa.sigla + "."
        # Cada equipa usa o verificar() da sua classe: a com estádio também verifica os lugares.
        mensagem = equipa.verificar()
        if mensagem != "":
            return mensagem
        self._equipas.append(equipa)
        return ""

    def acrescentar_equipa(self, sigla, nome, pontos):
        """Cria uma equipa sem estádio e guarda-a, se for válida. Devolve "" ou a mensagem da recusa."""
        return self._guardar(Equipa(sigla, nome, pontos))

    def acrescentar_com_estadio(self, sigla, nome, pontos, lugares):
        """Cria uma equipa com estádio e guarda-a, se for válida. Devolve "" ou a mensagem."""
        return self._guardar(EquipaComEstadio(sigla, nome, pontos, lugares))

    def somar_pontos(self, sigla, pontos_do_jogo):
        """Encaminha para a equipa com esta sigla os pontos ganhos num jogo.

        Devolve: a resposta da equipa, ou a mensagem de que a sigla não existe.
        """
        for equipa in self._equipas:
            if equipa.sigla == sigla:
                return equipa.somar_pontos(pontos_do_jogo)
        return "Não existe nenhuma equipa com a sigla " + sigla + "."

    def lista(self):
        """Devolve uma lista com a descrição de cada equipa, pela ordem em que entrou."""
        descricoes = []
        for equipa in self._equipas:
            # Cada equipa usa o descricao() da sua classe: o ciclo não pergunta o tipo.
            descricoes.append(equipa.descricao())
        return descricoes

    def com_10_pontos_ou_mais(self):
        """Devolve as descrições das equipas com 10 pontos ou mais, sem mudar nenhuma."""
        descricoes = []
        for equipa in self._equipas:
            # ">= 10", e não "> 10": uma equipa com 10 pontos certos também entra.
            if equipa.pontos >= 10:
                descricoes.append(equipa.descricao())
        return descricoes


def mostrar(titulo, descricoes):
    """Mostra um título e, por baixo, uma descrição por linha."""
    print(titulo)
    for descricao in descricoes:
        print("  " + descricao)


def mostrar_resultado(pedido, mensagem):
    """Mostra o pedido e diz se foi aceite ou, se foi recusado, porquê."""
    if mensagem == "":
        print(pedido + ": aceite.")
    else:
        print(pedido + ": recusado. " + mensagem)


campeonato = Campeonato()
mensagem = campeonato.acrescentar_equipa("LBO", "Leões do Bairro", 12)
mostrar_resultado("Acrescentar LBO", mensagem)
mensagem = campeonato.acrescentar_com_estadio("ACR", "Águias da Ribeira", 9, 5000)
mostrar_resultado("Acrescentar ACR", mensagem)
# O limite da regra: uma equipa que ainda não ganhou nada tem 0 pontos, e é aceite.
mensagem = campeonato.acrescentar_equipa("TVE", "Tubarões do Vale", 0)
mostrar_resultado("Acrescentar TVE", mensagem)
mostrar("Lista inicial:", campeonato.lista())
mostrar("Com 10 pontos ou mais:", campeonato.com_10_pontos_ou_mais())

# As quatro recusas: nenhuma muda o campeonato.
mensagem = campeonato.acrescentar_equipa("LBO", "Lobos da Serra", 3)
mostrar_resultado("Acrescentar outra LBO", mensagem)
mensagem = campeonato.acrescentar_equipa("LSE", "", 3)
mostrar_resultado("Acrescentar LSE sem nome", mensagem)
mensagem = campeonato.acrescentar_equipa("LSE", "Lobos da Serra", -3)
mostrar_resultado("Acrescentar LSE com -3 pontos", mensagem)
mensagem = campeonato.acrescentar_com_estadio("LSE", "Lobos da Serra", 3, 499)
mostrar_resultado("Acrescentar LSE com 499 lugares", mensagem)

# Somar 3 pontos e somar 0 pontos, como num jogo perdido: os dois são aceites.
mensagem = campeonato.somar_pontos("ACR", 3)
mostrar_resultado("Somar 3 pontos a ACR", mensagem)
mensagem = campeonato.somar_pontos("TVE", 0)
mostrar_resultado("Somar 0 pontos a TVE", mensagem)
mensagem = campeonato.somar_pontos("ACR", -3)
mostrar_resultado("Somar -3 pontos a ACR", mensagem)

mostrar("Lista no fim:", campeonato.lista())
mostrar("Com 10 pontos ou mais, no fim:", campeonato.com_10_pontos_ou_mais())
```

### O que o programa mostra

```text
Acrescentar LBO: aceite.
Acrescentar ACR: aceite.
Acrescentar TVE: aceite.
Lista inicial:
  LBO Leões do Bairro, 12 pontos
  ACR Águias da Ribeira, 9 pontos, estádio de 5000 lugares
  TVE Tubarões do Vale, 0 pontos
Com 10 pontos ou mais:
  LBO Leões do Bairro, 12 pontos
Acrescentar outra LBO: recusado. Já existe uma equipa com a sigla LBO.
Acrescentar LSE sem nome: recusado. O nome não pode ficar vazio.
Acrescentar LSE com -3 pontos: recusado. Os pontos têm de ser um número inteiro, 0 ou mais.
Acrescentar LSE com 499 lugares: recusado. Os lugares têm de ser um número inteiro de 500 a 90000.
Somar 3 pontos a ACR: aceite.
Somar 0 pontos a TVE: aceite.
Somar -3 pontos a ACR: recusado. Os pontos do jogo têm de ser um número inteiro, 0 ou mais.
Lista no fim:
  LBO Leões do Bairro, 12 pontos
  ACR Águias da Ribeira, 12 pontos, estádio de 5000 lugares
  TVE Tubarões do Vale, 0 pontos
Com 10 pontos ou mais, no fim:
  LBO Leões do Bairro, 12 pontos
  ACR Águias da Ribeira, 12 pontos, estádio de 5000 lugares
```

No princípio, só os LBO têm 10 pontos ou mais. Depois de somarem 3 pontos, os ACR passam de 9 para 12 e entram também. Os TVE somaram os 0 pontos de um jogo perdido sem erro e ficaram iguais.

![Rodapé](../imagens/rodape.png)

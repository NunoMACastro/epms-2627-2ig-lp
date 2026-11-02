![Cabeçalho](../imagens/cabecalho.png)

# Temas para treinar em casa: resoluções

Aqui tens um programa em Python para cada um dos [temas de treino](temas-de-treino.md). Tenta primeiro fazer o teu, sozinho, e só depois compara.

O teu programa não tem de ser igual a este. Os nomes dos métodos podem ser outros, e há mais do que uma maneira certa de o organizar. O que tem de fazer é o mesmo: aceitar o que as regras deixam, recusar o resto com uma mensagem e não mudar nada quando recusa.

Os cinco programas usam só o que aprendeste no M10: classes, propriedades com setter, `raise ValueError`, `try` e `except`, herança com `super()` e listas de objetos. Há um pormenor que os guias só mostraram com o construtor: na variante, `super().descricao()` chama a descrição da classe base, como `super().__init__` chama o construtor dela. Assim, a primeira parte da linha da lista escreve-se num só sítio. Se escreveste a descrição da variante por inteiro, sem o `super()`, também está certo.

Em quatro temas, a coleção cria os registos, como o inventário do guia 04 cria os artigos: é uma composição. Na playlist, as músicas são criadas fora e a playlist recebe-as já feitas: é uma agregação, como a playlist do guia 04.

## Coleção de jogos

Repara em duas coisas. As horas aceitam o 0, e a sessão que se soma também: uma sessão de 0 horas não muda nada. E a sessão verifica-se antes de se somar. Se só o setter verificasse, uma sessão de -2 horas passava sempre que o total continuasse positivo.

### O programa

```python
# Coleção de jogos: a resolução em Python do tema de treino.
# O jogo guarda as horas jogadas, o jogo multijogador é um jogo com um dado a mais,
# e a coleção cria e guarda os jogos. No fim, o programa principal experimenta as
# operações aceites e as quatro recusas.


class Jogo:
    """Jogo da coleção: código, título e horas jogadas, sempre válidas.

    Uma variante que se descreva de outra maneira redefine descricao().
    """

    def __init__(self, codigo, titulo, horas):
        """Cria o jogo.

        Recebe: o código (texto), o título (texto) e as horas jogadas (inteiro).
        Falha: lança ValueError se o título estiver vazio, ou se as horas forem
        inválidas (quem as recusa é o setter).
        """
        # O strip tira os espaços das pontas: um título só com espaços também é vazio.
        if titulo.strip() == "":
            raise ValueError("O título não pode ficar vazio.")
        self.codigo = codigo
        self.titulo = titulo
        self.horas = horas

    @property
    def horas(self):
        """Getter: devolve as horas jogadas, sem as alterar."""
        return self._horas

    @horas.setter
    def horas(self, valor):
        """Setter: guarda o valor se for um inteiro, 0 ou mais; senão, lança ValueError."""
        if not isinstance(valor, int):
            raise ValueError("As horas têm de ser um número inteiro.")
        if valor < 0:
            raise ValueError("As horas não podem ser negativas.")
        self._horas = valor

    def somar_horas(self, horas_da_sessao):
        """Soma as horas de uma sessão (inteiro, 0 ou mais); senão, lança ValueError.

        Uma sessão de 0 horas é aceite e não muda nada.
        """
        # Sem esta verificação, uma sessão de -2 horas passava no setter
        # sempre que o total continuasse positivo, e as horas desciam.
        if not isinstance(horas_da_sessao, int):
            raise ValueError("As horas da sessão têm de ser um número inteiro.")
        if horas_da_sessao < 0:
            raise ValueError("As horas da sessão não podem ser negativas.")
        self.horas = self.horas + horas_da_sessao

    def descricao(self):
        """Devolve a linha da lista, como "J01 Corrida Rápida, 12 horas"."""
        return self.codigo + " " + self.titulo + ", " + str(self.horas) + " horas"


class JogoMultijogador(Jogo):
    """Jogo multijogador: tudo o que um jogo tem e o número máximo de jogadores."""

    def __init__(self, codigo, titulo, horas, jogadores):
        """Guarda o código, o título e as horas, pelo construtor do jogo, e os jogadores.

        Recebe: os três dados do jogo e o número máximo de jogadores (inteiro).
        Falha: lança ValueError se algum dado for inválido.
        """
        super().__init__(codigo, titulo, horas)
        self.jogadores = jogadores

    @property
    def jogadores(self):
        """Getter: devolve o número máximo de jogadores, sem o alterar."""
        return self._jogadores

    @jogadores.setter
    def jogadores(self, valor):
        """Setter: guarda o valor se for um inteiro de 2 a 100; senão, lança ValueError."""
        if not isinstance(valor, int):
            raise ValueError("O número de jogadores tem de ser um número inteiro.")
        if valor < 2 or valor > 100:
            raise ValueError("O número de jogadores tem de ser de 2 a 100.")
        self._jogadores = valor

    def descricao(self):
        """Devolve a descrição de um jogo, com o máximo de jogadores no fim."""
        # super() dá acesso à versão da classe base de descricao(), para este mesmo
        # jogo. Assim, a primeira parte da linha escreve-se num só sítio.
        return super().descricao() + ", até " + str(self.jogadores) + " jogadores"


class ColecaoDeJogos:
    """Coleção que cria, guarda e controla os seus jogos.

    A coleção é a dona dos jogos: cria-os nos métodos acrescentar e guarda-os
    numa lista interna, _jogos, que o código de fora não usa. Garante a regra
    que nenhum jogo consegue garantir sozinho: não há dois jogos com o mesmo
    código. As horas de cada jogo continuam protegidas pelo próprio jogo.
    """

    def __init__(self):
        """Cria uma coleção vazia, ainda sem jogos."""
        self._jogos = []

    def _verificar_codigo_livre(self, codigo):
        """Método interno: lança ValueError se já houver um jogo com este código."""
        for jogo in self._jogos:
            if jogo.codigo == codigo:
                raise ValueError("Já existe um jogo com o código " + codigo + ".")

    def _procurar(self, codigo):
        """Método interno: devolve o jogo com este código.

        Falha: lança ValueError se não houver nenhum jogo com este código.
        """
        for jogo in self._jogos:
            if jogo.codigo == codigo:
                return jogo
        raise ValueError("Não existe nenhum jogo com o código " + codigo + ".")

    def acrescentar_jogo(self, codigo, titulo, horas):
        """Cria um jogo simples e guarda-o na coleção.

        Falha: lança ValueError se o código já existir ou se um dado for
        inválido. Em qualquer falha, a coleção fica como estava.
        """
        self._verificar_codigo_livre(codigo)
        self._jogos.append(Jogo(codigo, titulo, horas))

    def acrescentar_multijogador(self, codigo, titulo, horas, jogadores):
        """Cria um jogo multijogador e guarda-o na coleção.

        Falha: como acrescentar_jogo, e também se o número de jogadores for inválido.
        """
        self._verificar_codigo_livre(codigo)
        self._jogos.append(JogoMultijogador(codigo, titulo, horas, jogadores))

    def somar_horas(self, codigo, horas_da_sessao):
        """Encaminha para o jogo com este código as horas de uma sessão.

        Falha: lança ValueError se o código não existir ou se o jogo recusar
        a sessão. Em qualquer falha, nenhumas horas mudam.
        """
        jogo = self._procurar(codigo)
        jogo.somar_horas(horas_da_sessao)

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


colecao = ColecaoDeJogos()
colecao.acrescentar_jogo("J01", "Corrida Rápida", 12)
colecao.acrescentar_multijogador("J02", "Arena dos Heróis", 30, 8)
# O limite da regra: um jogo acabado de comprar tem 0 horas, e é aceite.
colecao.acrescentar_jogo("J03", "Torre de Blocos", 0)
mostrar("Lista inicial:", colecao.lista())
mostrar("Com mais de 10 horas:", colecao.com_mais_de_10_horas())

try:
    colecao.acrescentar_jogo("J01", "Pinguins no Gelo", 5)
except ValueError as erro:
    print("Recusado:", erro)

try:
    colecao.acrescentar_jogo("J04", "   ", 5)
except ValueError as erro:
    print("Recusado:", erro)

try:
    colecao.acrescentar_jogo("J04", "Pinguins no Gelo", -1)
except ValueError as erro:
    print("Recusado:", erro)

try:
    colecao.acrescentar_multijogador("J04", "Pinguins no Gelo", 5, 1)
except ValueError as erro:
    print("Recusado:", erro)

colecao.somar_horas("J03", 11)

try:
    colecao.somar_horas("J03", -2)
except ValueError as erro:
    print("Recusado:", erro)

mostrar("Lista no fim:", colecao.lista())
mostrar("Com mais de 10 horas, no fim:", colecao.com_mais_de_10_horas())
```

### O que o programa mostra

```text
Lista inicial:
  J01 Corrida Rápida, 12 horas
  J02 Arena dos Heróis, 30 horas, até 8 jogadores
  J03 Torre de Blocos, 0 horas
Com mais de 10 horas:
  J01 Corrida Rápida, 12 horas
  J02 Arena dos Heróis, 30 horas, até 8 jogadores
Recusado: Já existe um jogo com o código J01.
Recusado: O título não pode ficar vazio.
Recusado: As horas não podem ser negativas.
Recusado: O número de jogadores tem de ser de 2 a 100.
Recusado: As horas da sessão não podem ser negativas.
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

A raridade tem dois limites, de 1 a 5, e o setter verifica os dois. A correção da raridade passa pelo setter, por isso a regra também vale quando se corrige. No filtro, "4 ou mais" escreve-se `>= 4`.

### O programa

```python
# Cartas colecionáveis: a resolução em Python do tema de treino.
# A carta guarda a raridade, de 1 a 5, a carta de edição limitada é uma carta com
# o número de cópias, e a coleção cria e guarda as cartas. No fim, o programa
# principal experimenta as operações aceites e as quatro recusas.


class Carta:
    """Carta da coleção: código, nome e raridade, sempre válida.

    Uma variante que se descreva de outra maneira redefine descricao().
    """

    def __init__(self, codigo, nome, raridade):
        """Cria a carta.

        Recebe: o código (texto), o nome (texto) e a raridade (inteiro).
        Falha: lança ValueError se o nome estiver vazio, ou se a raridade for
        inválida (quem a recusa é o setter).
        """
        # O strip tira os espaços das pontas: um nome só com espaços também é vazio.
        if nome.strip() == "":
            raise ValueError("O nome não pode ficar vazio.")
        self.codigo = codigo
        self.nome = nome
        self.raridade = raridade

    @property
    def raridade(self):
        """Getter: devolve a raridade, sem a alterar."""
        return self._raridade

    @raridade.setter
    def raridade(self, valor):
        """Setter: guarda o valor se for um inteiro de 1 a 5; senão, lança ValueError.

        É o único caminho para mudar a raridade, ao criar e ao corrigir.
        """
        if not isinstance(valor, int):
            raise ValueError("A raridade tem de ser um número inteiro.")
        if valor < 1 or valor > 5:
            raise ValueError("A raridade tem de ser de 1 a 5.")
        self._raridade = valor

    def descricao(self):
        """Devolve a linha da lista, como "C001 Lobo da Neve, raridade 3"."""
        return self.codigo + " " + self.nome + ", raridade " + str(self.raridade)


class CartaEdicaoLimitada(Carta):
    """Carta de edição limitada: tudo o que uma carta tem e o número de cópias."""

    def __init__(self, codigo, nome, raridade, copias):
        """Guarda o código, o nome e a raridade, pelo construtor da carta, e as cópias.

        Recebe: os três dados da carta e o número de cópias da edição (inteiro).
        Falha: lança ValueError se algum dado for inválido.
        """
        super().__init__(codigo, nome, raridade)
        self.copias = copias

    @property
    def copias(self):
        """Getter: devolve o número de cópias da edição, sem o alterar."""
        return self._copias

    @copias.setter
    def copias(self, valor):
        """Setter: guarda o valor se for um inteiro de 1 a 1000; senão, lança ValueError."""
        if not isinstance(valor, int):
            raise ValueError("O número de cópias tem de ser um número inteiro.")
        if valor < 1 or valor > 1000:
            raise ValueError("O número de cópias tem de ser de 1 a 1000.")
        self._copias = valor

    def descricao(self):
        """Devolve a descrição de uma carta, com o número de cópias no fim."""
        # super() dá acesso à versão da classe base de descricao(), para esta carta.
        return super().descricao() + ", edição de " + str(self.copias) + " cópias"


class ColecaoDeCartas:
    """Coleção que cria, guarda e controla as suas cartas.

    A coleção é a dona das cartas: cria-as nos métodos acrescentar e guarda-as
    numa lista interna, _cartas, que o código de fora não usa. Garante que não
    há duas cartas com o mesmo código. A raridade de cada carta continua
    protegida pela própria carta.
    """

    def __init__(self):
        """Cria uma coleção vazia, ainda sem cartas."""
        self._cartas = []

    def _verificar_codigo_livre(self, codigo):
        """Método interno: lança ValueError se já houver uma carta com este código."""
        for carta in self._cartas:
            if carta.codigo == codigo:
                raise ValueError("Já existe uma carta com o código " + codigo + ".")

    def _procurar(self, codigo):
        """Método interno: devolve a carta com este código.

        Falha: lança ValueError se não houver nenhuma carta com este código.
        """
        for carta in self._cartas:
            if carta.codigo == codigo:
                return carta
        raise ValueError("Não existe nenhuma carta com o código " + codigo + ".")

    def acrescentar_carta(self, codigo, nome, raridade):
        """Cria uma carta simples e guarda-a na coleção.

        Falha: lança ValueError se o código já existir ou se um dado for
        inválido. Em qualquer falha, a coleção fica como estava.
        """
        self._verificar_codigo_livre(codigo)
        self._cartas.append(Carta(codigo, nome, raridade))

    def acrescentar_edicao_limitada(self, codigo, nome, raridade, copias):
        """Cria uma carta de edição limitada e guarda-a na coleção.

        Falha: como acrescentar_carta, e também se o número de cópias for inválido.
        """
        self._verificar_codigo_livre(codigo)
        self._cartas.append(CartaEdicaoLimitada(codigo, nome, raridade, copias))

    def corrigir_raridade(self, codigo, raridade):
        """Muda a raridade da carta com este código, pelo setter da carta.

        Falha: lança ValueError se o código não existir ou se a raridade for
        inválida. Em qualquer falha, a raridade não muda.
        """
        carta = self._procurar(codigo)
        carta.raridade = raridade

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


colecao = ColecaoDeCartas()
colecao.acrescentar_carta("C001", "Lobo da Neve", 3)
colecao.acrescentar_edicao_limitada("C002", "Dragão Dourado", 5, 250)
# Os dois limites da regra da raridade são aceites: 1 e 5.
colecao.acrescentar_carta("C003", "Rato do Celeiro", 1)
mostrar("Lista inicial:", colecao.lista())
mostrar("De raridade 4 ou mais:", colecao.de_raridade_4_ou_mais())

try:
    colecao.acrescentar_carta("C001", "Coruja Branca", 2)
except ValueError as erro:
    print("Recusado:", erro)

try:
    colecao.acrescentar_carta("C004", "", 2)
except ValueError as erro:
    print("Recusado:", erro)

try:
    colecao.acrescentar_carta("C004", "Coruja Branca", 6)
except ValueError as erro:
    print("Recusado:", erro)

try:
    colecao.acrescentar_edicao_limitada("C004", "Coruja Branca", 2, 1001)
except ValueError as erro:
    print("Recusado:", erro)

colecao.corrigir_raridade("C001", 4)

try:
    colecao.corrigir_raridade("C001", 0)
except ValueError as erro:
    print("Recusado:", erro)

mostrar("Lista no fim:", colecao.lista())
mostrar("De raridade 4 ou mais, no fim:", colecao.de_raridade_4_ou_mais())
```

### O que o programa mostra

```text
Lista inicial:
  C001 Lobo da Neve, raridade 3
  C002 Dragão Dourado, raridade 5, edição de 250 cópias
  C003 Rato do Celeiro, raridade 1
De raridade 4 ou mais:
  C002 Dragão Dourado, raridade 5, edição de 250 cópias
Recusado: Já existe uma carta com o código C001.
Recusado: O nome não pode ficar vazio.
Recusado: A raridade tem de ser de 1 a 5.
Recusado: O número de cópias tem de ser de 1 a 1000.
Recusado: A raridade tem de ser de 1 a 5.
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

A duração não aceita o 0, ao contrário da quantidade do inventário dos guias, e por isso a comparação é `<= 0`. No filtro, "mais de 30 minutos" deixa de fora um treino de 30 minutos certos.

### O programa

```python
# Diário de treinos: a resolução em Python do tema de treino.
# O treino guarda a duração, o treino com distância é um treino com os metros
# percorridos, e o diário cria e guarda os treinos. No fim, o programa principal
# experimenta as operações aceites e as quatro recusas.


class Treino:
    """Treino do diário: código, atividade e duração em minutos, sempre válida.

    Uma variante que se descreva de outra maneira redefine descricao().
    """

    def __init__(self, codigo, atividade, duracao):
        """Cria o treino.

        Recebe: o código (texto), a atividade (texto) e a duração em minutos (inteiro).
        Falha: lança ValueError se a atividade estiver vazia, ou se a duração
        for inválida (quem a recusa é o setter).
        """
        # O strip tira os espaços das pontas: uma atividade só com espaços também é vazia.
        if atividade.strip() == "":
            raise ValueError("A atividade não pode ficar vazia.")
        self.codigo = codigo
        self.atividade = atividade
        self.duracao = duracao

    @property
    def duracao(self):
        """Getter: devolve a duração em minutos, sem a alterar."""
        return self._duracao

    @duracao.setter
    def duracao(self, valor):
        """Setter: guarda o valor se for um inteiro maior do que 0; senão, lança ValueError."""
        if not isinstance(valor, int):
            raise ValueError("A duração tem de ser um número inteiro de minutos.")
        # "<= 0", e não "< 0": ao contrário da quantidade do inventário, o 0 é recusado.
        if valor <= 0:
            raise ValueError("A duração tem de ser maior do que 0.")
        self._duracao = valor

    def descricao(self):
        """Devolve a linha da lista, como "T01 Ginásio, 45 minutos"."""
        return self.codigo + " " + self.atividade + ", " + str(self.duracao) + " minutos"


class TreinoComDistancia(Treino):
    """Treino com distância: tudo o que um treino tem e a distância em metros."""

    def __init__(self, codigo, atividade, duracao, distancia):
        """Guarda o código, a atividade e a duração, pelo construtor do treino, e a distância.

        Recebe: os três dados do treino e a distância percorrida, em metros (inteiro).
        Falha: lança ValueError se algum dado for inválido.
        """
        super().__init__(codigo, atividade, duracao)
        self.distancia = distancia

    @property
    def distancia(self):
        """Getter: devolve a distância em metros, sem a alterar."""
        return self._distancia

    @distancia.setter
    def distancia(self, valor):
        """Setter: guarda o valor se for um inteiro maior do que 0; senão, lança ValueError."""
        if not isinstance(valor, int):
            raise ValueError("A distância tem de ser um número inteiro de metros.")
        if valor <= 0:
            raise ValueError("A distância tem de ser maior do que 0.")
        self._distancia = valor

    def descricao(self):
        """Devolve a descrição de um treino, com a distância no fim."""
        # super() dá acesso à versão da classe base de descricao(), para este treino.
        return super().descricao() + ", " + str(self.distancia) + " metros"


class DiarioDeTreinos:
    """Diário que cria, guarda e controla os seus treinos.

    O diário é o dono dos treinos: cria-os nos métodos acrescentar e guarda-os
    numa lista interna, _treinos, que o código de fora não usa. Garante que não
    há dois treinos com o mesmo código. A duração de cada treino continua
    protegida pelo próprio treino.
    """

    def __init__(self):
        """Cria um diário vazio, ainda sem treinos."""
        self._treinos = []

    def _verificar_codigo_livre(self, codigo):
        """Método interno: lança ValueError se já houver um treino com este código."""
        for treino in self._treinos:
            if treino.codigo == codigo:
                raise ValueError("Já existe um treino com o código " + codigo + ".")

    def _procurar(self, codigo):
        """Método interno: devolve o treino com este código.

        Falha: lança ValueError se não houver nenhum treino com este código.
        """
        for treino in self._treinos:
            if treino.codigo == codigo:
                return treino
        raise ValueError("Não existe nenhum treino com o código " + codigo + ".")

    def acrescentar_treino(self, codigo, atividade, duracao):
        """Cria um treino simples e guarda-o no diário.

        Falha: lança ValueError se o código já existir ou se um dado for
        inválido. Em qualquer falha, o diário fica como estava.
        """
        self._verificar_codigo_livre(codigo)
        self._treinos.append(Treino(codigo, atividade, duracao))

    def acrescentar_com_distancia(self, codigo, atividade, duracao, distancia):
        """Cria um treino com distância e guarda-o no diário.

        Falha: como acrescentar_treino, e também se a distância for inválida.
        """
        self._verificar_codigo_livre(codigo)
        self._treinos.append(TreinoComDistancia(codigo, atividade, duracao, distancia))

    def corrigir_duracao(self, codigo, duracao):
        """Muda a duração do treino com este código, pelo setter do treino.

        Falha: lança ValueError se o código não existir ou se a duração for
        inválida. Em qualquer falha, a duração não muda.
        """
        treino = self._procurar(codigo)
        treino.duracao = duracao

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


diario = DiarioDeTreinos()
diario.acrescentar_treino("T01", "Ginásio", 45)
diario.acrescentar_com_distancia("T02", "Corrida", 30, 5000)
mostrar("Lista inicial:", diario.lista())
# T02 tem 30 minutos certos: ainda não é um treino de mais de 30 minutos.
mostrar("Com mais de 30 minutos:", diario.com_mais_de_30_minutos())

try:
    diario.acrescentar_treino("T01", "Natação", 40)
except ValueError as erro:
    print("Recusado:", erro)

try:
    diario.acrescentar_treino("T04", "", 40)
except ValueError as erro:
    print("Recusado:", erro)

try:
    diario.acrescentar_treino("T04", "Natação", 0)
except ValueError as erro:
    print("Recusado:", erro)

try:
    diario.acrescentar_com_distancia("T04", "Bicicleta", 60, 0)
except ValueError as erro:
    print("Recusado:", erro)

diario.corrigir_duracao("T02", 35)

try:
    diario.corrigir_duracao("T02", 0)
except ValueError as erro:
    print("Recusado:", erro)

mostrar("Lista no fim:", diario.lista())
mostrar("Com mais de 30 minutos, no fim:", diario.com_mais_de_30_minutos())
```

### O que o programa mostra

```text
Lista inicial:
  T01 Ginásio, 45 minutos
  T02 Corrida, 30 minutos, 5000 metros
Com mais de 30 minutos:
  T01 Ginásio, 45 minutos
Recusado: Já existe um treino com o código T01.
Recusado: A atividade não pode ficar vazia.
Recusado: A duração tem de ser maior do que 0.
Recusado: A distância tem de ser maior do que 0.
Recusado: A duração tem de ser maior do que 0.
Lista no fim:
  T01 Ginásio, 45 minutos
  T02 Corrida, 35 minutos, 5000 metros
Com mais de 30 minutos, no fim:
  T01 Ginásio, 45 minutos
  T02 Corrida, 35 minutos, 5000 metros
```

No princípio, o T02 tem 30 minutos certos e fica de fora do filtro. Depois da correção para 35 minutos, entra.

## Playlist

Aqui, a playlist não cria as músicas: recebe-as já criadas. Por isso, as recusas do título, da duração e da faixa acontecem ao criar a música, antes de ela chegar à playlist. A mesma música pode estar em duas playlists.

### O programa

```python
# Playlist: a resolução em Python do tema de treino.
# A música guarda a duração em segundos, a música de um álbum é uma música com o
# número da faixa, e a playlist reúne músicas que já existem: é uma agregação, como
# a playlist do guia 04. No fim, o programa principal experimenta as operações
# aceites, as quatro recusas e a mesma música em duas playlists.


class Musica:
    """Música: código, título e duração em segundos, sempre válida.

    Uma variante que se descreva de outra maneira redefine descricao().
    """

    def __init__(self, codigo, titulo, duracao):
        """Cria a música.

        Recebe: o código (texto), o título (texto) e a duração em segundos (inteiro).
        Falha: lança ValueError se o título estiver vazio, ou se a duração for
        inválida (quem a recusa é o setter).
        """
        # O strip tira os espaços das pontas: um título só com espaços também é vazio.
        if titulo.strip() == "":
            raise ValueError("O título não pode ficar vazio.")
        self.codigo = codigo
        self.titulo = titulo
        self.duracao = duracao

    @property
    def duracao(self):
        """Getter: devolve a duração em segundos, sem a alterar."""
        return self._duracao

    @duracao.setter
    def duracao(self, valor):
        """Setter: guarda o valor se for um inteiro maior do que 0; senão, lança ValueError."""
        if not isinstance(valor, int):
            raise ValueError("A duração tem de ser um número inteiro de segundos.")
        if valor <= 0:
            raise ValueError("A duração tem de ser maior do que 0.")
        self._duracao = valor

    def descricao(self):
        """Devolve a linha da lista, como "M01 Noite de Verão, 200 segundos"."""
        return self.codigo + " " + self.titulo + ", " + str(self.duracao) + " segundos"


class MusicaDeAlbum(Musica):
    """Música de um álbum: tudo o que uma música tem e o número da faixa."""

    def __init__(self, codigo, titulo, duracao, faixa):
        """Guarda o código, o título e a duração, pelo construtor da música, e a faixa.

        Recebe: os três dados da música e o número da faixa no álbum (inteiro).
        Falha: lança ValueError se algum dado for inválido.
        """
        super().__init__(codigo, titulo, duracao)
        self.faixa = faixa

    @property
    def faixa(self):
        """Getter: devolve o número da faixa, sem o alterar."""
        return self._faixa

    @faixa.setter
    def faixa(self, valor):
        """Setter: guarda o valor se for um inteiro de 1 a 30; senão, lança ValueError."""
        if not isinstance(valor, int):
            raise ValueError("A faixa tem de ser um número inteiro.")
        if valor < 1 or valor > 30:
            raise ValueError("A faixa tem de ser de 1 a 30.")
        self._faixa = valor

    def descricao(self):
        """Devolve a descrição de uma música, com o número da faixa no fim."""
        # super() dá acesso à versão da classe base de descricao(), para esta música.
        return super().descricao() + ", faixa " + str(self.faixa)


class Playlist:
    """Playlist que agrega músicas: não as cria, recebe-as já criadas.

    Guarda as músicas numa lista interna, _musicas, que o código de fora não
    usa, e garante que não há duas músicas com o mesmo código na mesma
    playlist. A mesma música pode estar em várias playlists, e continua a
    existir se uma playlist desaparecer. A duração de cada música continua
    protegida pela própria música.
    """

    def __init__(self, nome):
        """Cria uma playlist vazia, com este nome (texto)."""
        self.nome = nome
        self._musicas = []

    def _procurar(self, codigo):
        """Método interno: devolve a música com este código.

        Falha: lança ValueError se não houver nenhuma música com este código.
        """
        for musica in self._musicas:
            if musica.codigo == codigo:
                return musica
        raise ValueError("Não existe nenhuma música com o código " + codigo + ".")

    def acrescentar(self, musica):
        """Junta à playlist uma música já criada, simples ou de um álbum.

        Recebe: um objeto Musica ou MusicaDeAlbum.
        Falha: lança ValueError se a playlist já tiver uma música com o mesmo
        código. Nesse caso, a playlist fica como estava.
        """
        for existente in self._musicas:
            if existente.codigo == musica.codigo:
                raise ValueError("Já existe uma música com o código " + musica.codigo + ".")
        self._musicas.append(musica)

    def corrigir_duracao(self, codigo, duracao):
        """Muda a duração da música com este código, pelo setter da música.

        Falha: lança ValueError se o código não existir ou se a duração for
        inválida. Em qualquer falha, a duração não muda.
        """
        musica = self._procurar(codigo)
        musica.duracao = duracao

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


# Numa agregação, as músicas criam-se fora da playlist, e só depois se juntam.
noite = Musica("M01", "Noite de Verão", 200)
tempestade = MusicaDeAlbum("M02", "Tempestade", 245, 3)

para_estudar = Playlist("Para estudar")
para_estudar.acrescentar(noite)
para_estudar.acrescentar(tempestade)
mostrar("Lista inicial:", para_estudar.lista())
mostrar("Com mais de 4 minutos:", para_estudar.com_mais_de_4_minutos())

try:
    para_estudar.acrescentar(Musica("M01", "Chuva Miúda", 180))
except ValueError as erro:
    print("Recusado:", erro)

# As três recusas seguintes acontecem ao criar a música, antes de ela chegar à
# playlist: o objeto não chega a existir, e a playlist não muda.
try:
    para_estudar.acrescentar(Musica("M04", "", 180))
except ValueError as erro:
    print("Recusado:", erro)

try:
    para_estudar.acrescentar(Musica("M04", "Chuva Miúda", 0))
except ValueError as erro:
    print("Recusado:", erro)

try:
    para_estudar.acrescentar(MusicaDeAlbum("M04", "Chuva Miúda", 180, 31))
except ValueError as erro:
    print("Recusado:", erro)

para_estudar.corrigir_duracao("M01", 250)

try:
    para_estudar.corrigir_duracao("M01", 0)
except ValueError as erro:
    print("Recusado:", erro)

mostrar("Lista no fim:", para_estudar.lista())
mostrar("Com mais de 4 minutos, no fim:", para_estudar.com_mais_de_4_minutos())

# A mesma música noutra playlist: é o mesmo objeto, e não uma cópia. A correção
# feita pela playlist "Para estudar" também se vê aqui.
para_correr = Playlist("Para correr")
para_correr.acrescentar(noite)
mostrar("Para correr:", para_correr.lista())
```

### O que o programa mostra

```text
Lista inicial:
  M01 Noite de Verão, 200 segundos
  M02 Tempestade, 245 segundos, faixa 3
Com mais de 4 minutos:
  M02 Tempestade, 245 segundos, faixa 3
Recusado: Já existe uma música com o código M01.
Recusado: O título não pode ficar vazio.
Recusado: A duração tem de ser maior do que 0.
Recusado: A faixa tem de ser de 1 a 30.
Recusado: A duração tem de ser maior do que 0.
Lista no fim:
  M01 Noite de Verão, 250 segundos
  M02 Tempestade, 245 segundos, faixa 3
Com mais de 4 minutos, no fim:
  M01 Noite de Verão, 250 segundos
  M02 Tempestade, 245 segundos, faixa 3
Para correr:
  M01 Noite de Verão, 250 segundos
```

As duas últimas linhas mostram a agregação. A playlist "Para correr" recebeu a mesma música, e não uma cópia, por isso já tem os 250 segundos da correção feita pela playlist "Para estudar".

## Campeonato

A sigla faz o papel do código. Os pontos de um jogo aceitam o 0, de um jogo perdido, e verificam-se antes de se somarem, como as horas da sessão nos jogos. Em Python, os 90 000 lugares escrevem-se `90000`, sem espaço nem ponto: `90.000` seria o número decimal 90,0.

### O programa

```python
# Campeonato: a resolução em Python do tema de treino.
# A equipa guarda os pontos, a equipa com estádio é uma equipa com os lugares do
# estádio, e o campeonato cria e guarda as equipas. No fim, o programa principal
# experimenta as operações aceites e as quatro recusas.


class Equipa:
    """Equipa do campeonato: sigla, nome e pontos, sempre válidos.

    Uma variante que se descreva de outra maneira redefine descricao().
    """

    def __init__(self, sigla, nome, pontos):
        """Cria a equipa.

        Recebe: a sigla (texto), o nome (texto) e os pontos (inteiro).
        Falha: lança ValueError se o nome estiver vazio, ou se os pontos forem
        inválidos (quem os recusa é o setter).
        """
        # O strip tira os espaços das pontas: um nome só com espaços também é vazio.
        if nome.strip() == "":
            raise ValueError("O nome não pode ficar vazio.")
        self.sigla = sigla
        self.nome = nome
        self.pontos = pontos

    @property
    def pontos(self):
        """Getter: devolve os pontos, sem os alterar."""
        return self._pontos

    @pontos.setter
    def pontos(self, valor):
        """Setter: guarda o valor se for um inteiro, 0 ou mais; senão, lança ValueError."""
        if not isinstance(valor, int):
            raise ValueError("Os pontos têm de ser um número inteiro.")
        if valor < 0:
            raise ValueError("Os pontos não podem ser negativos.")
        self._pontos = valor

    def somar_pontos(self, pontos_do_jogo):
        """Soma os pontos ganhos num jogo (inteiro, 0 ou mais); senão, lança ValueError.

        Um jogo perdido dá 0 pontos: é aceite e não muda nada.
        """
        # Sem esta verificação, um jogo de -3 pontos passava no setter sempre
        # que o total continuasse positivo, e a equipa perdia pontos.
        if not isinstance(pontos_do_jogo, int):
            raise ValueError("Os pontos do jogo têm de ser um número inteiro.")
        if pontos_do_jogo < 0:
            raise ValueError("Os pontos do jogo não podem ser negativos.")
        self.pontos = self.pontos + pontos_do_jogo

    def descricao(self):
        """Devolve a linha da lista, como "LBO Leões do Bairro, 12 pontos"."""
        return self.sigla + " " + self.nome + ", " + str(self.pontos) + " pontos"


class EquipaComEstadio(Equipa):
    """Equipa com estádio: tudo o que uma equipa tem e os lugares do estádio."""

    def __init__(self, sigla, nome, pontos, lugares):
        """Guarda a sigla, o nome e os pontos, pelo construtor da equipa, e os lugares.

        Recebe: os três dados da equipa e o número de lugares do estádio (inteiro).
        Falha: lança ValueError se algum dado for inválido.
        """
        super().__init__(sigla, nome, pontos)
        self.lugares = lugares

    @property
    def lugares(self):
        """Getter: devolve o número de lugares do estádio, sem o alterar."""
        return self._lugares

    @lugares.setter
    def lugares(self, valor):
        """Setter: guarda o valor se for um inteiro de 500 a 90000; senão, lança ValueError."""
        if not isinstance(valor, int):
            raise ValueError("Os lugares têm de ser um número inteiro.")
        if valor < 500 or valor > 90000:
            raise ValueError("Os lugares têm de ser de 500 a 90000.")
        self._lugares = valor

    def descricao(self):
        """Devolve a descrição de uma equipa, com os lugares do estádio no fim."""
        # super() dá acesso à versão da classe base de descricao(), para esta equipa.
        return super().descricao() + ", estádio de " + str(self.lugares) + " lugares"


class Campeonato:
    """Campeonato que cria, guarda e controla as suas equipas.

    O campeonato é o dono das equipas: cria-as nos métodos acrescentar e
    guarda-as numa lista interna, _equipas, que o código de fora não usa.
    Garante que não há duas equipas com a mesma sigla. Os pontos de cada
    equipa continuam protegidos pela própria equipa.
    """

    def __init__(self):
        """Cria um campeonato vazio, ainda sem equipas."""
        self._equipas = []

    def _verificar_sigla_livre(self, sigla):
        """Método interno: lança ValueError se já houver uma equipa com esta sigla."""
        for equipa in self._equipas:
            if equipa.sigla == sigla:
                raise ValueError("Já existe uma equipa com a sigla " + sigla + ".")

    def _procurar(self, sigla):
        """Método interno: devolve a equipa com esta sigla.

        Falha: lança ValueError se não houver nenhuma equipa com esta sigla.
        """
        for equipa in self._equipas:
            if equipa.sigla == sigla:
                return equipa
        raise ValueError("Não existe nenhuma equipa com a sigla " + sigla + ".")

    def acrescentar_equipa(self, sigla, nome, pontos):
        """Cria uma equipa sem estádio e guarda-a no campeonato.

        Falha: lança ValueError se a sigla já existir ou se um dado for
        inválido. Em qualquer falha, o campeonato fica como estava.
        """
        self._verificar_sigla_livre(sigla)
        self._equipas.append(Equipa(sigla, nome, pontos))

    def acrescentar_com_estadio(self, sigla, nome, pontos, lugares):
        """Cria uma equipa com estádio e guarda-a no campeonato.

        Falha: como acrescentar_equipa, e também se os lugares forem inválidos.
        """
        self._verificar_sigla_livre(sigla)
        self._equipas.append(EquipaComEstadio(sigla, nome, pontos, lugares))

    def somar_pontos(self, sigla, pontos_do_jogo):
        """Encaminha para a equipa com esta sigla os pontos ganhos num jogo.

        Falha: lança ValueError se a sigla não existir ou se a equipa recusar
        os pontos. Em qualquer falha, nenhuns pontos mudam.
        """
        equipa = self._procurar(sigla)
        equipa.somar_pontos(pontos_do_jogo)

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


campeonato = Campeonato()
campeonato.acrescentar_equipa("LBO", "Leões do Bairro", 12)
campeonato.acrescentar_com_estadio("ACR", "Águias da Ribeira", 9, 5000)
# O limite da regra: uma equipa que ainda não ganhou nada tem 0 pontos, e é aceite.
campeonato.acrescentar_equipa("TVE", "Tubarões do Vale", 0)
mostrar("Lista inicial:", campeonato.lista())
mostrar("Com 10 pontos ou mais:", campeonato.com_10_pontos_ou_mais())

try:
    campeonato.acrescentar_equipa("LBO", "Lobos da Serra", 3)
except ValueError as erro:
    print("Recusado:", erro)

try:
    campeonato.acrescentar_equipa("LSE", "", 3)
except ValueError as erro:
    print("Recusado:", erro)

try:
    campeonato.acrescentar_equipa("LSE", "Lobos da Serra", -3)
except ValueError as erro:
    print("Recusado:", erro)

try:
    campeonato.acrescentar_com_estadio("LSE", "Lobos da Serra", 3, 499)
except ValueError as erro:
    print("Recusado:", erro)

# Somar 3 pontos e somar 0 pontos, como num jogo perdido: os dois são aceites.
campeonato.somar_pontos("ACR", 3)
campeonato.somar_pontos("TVE", 0)

try:
    campeonato.somar_pontos("ACR", -3)
except ValueError as erro:
    print("Recusado:", erro)

mostrar("Lista no fim:", campeonato.lista())
mostrar("Com 10 pontos ou mais, no fim:", campeonato.com_10_pontos_ou_mais())
```

### O que o programa mostra

```text
Lista inicial:
  LBO Leões do Bairro, 12 pontos
  ACR Águias da Ribeira, 9 pontos, estádio de 5000 lugares
  TVE Tubarões do Vale, 0 pontos
Com 10 pontos ou mais:
  LBO Leões do Bairro, 12 pontos
Recusado: Já existe uma equipa com a sigla LBO.
Recusado: O nome não pode ficar vazio.
Recusado: Os pontos não podem ser negativos.
Recusado: Os lugares têm de ser de 500 a 90000.
Recusado: Os pontos do jogo não podem ser negativos.
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

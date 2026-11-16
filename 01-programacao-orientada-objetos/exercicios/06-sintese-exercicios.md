![Cabeçalho](../../imagens/cabecalho.png)

# Ficha de exercícios: Síntese

Treinas, no inventário do guia, três coisas: dizer quem responde a cada pedido, escrever um método novo com o seu contrato e encontrar o erro de um colega. A parte obrigatória são os exercícios 1 a 3. Cada um faz-se num script novo, na pasta `tema-06` do laboratório, com o nome que o enunciado lhe dá. O que respondes por palavras fica num comentário no fim desse script. Os três scripts entregam-se pelo meio que o professor indicar, e os dos desafios também, se os fizeste. Para rever: o [guia do tema](../06-sintese.md) e o [laboratório](../laboratorios/06-sintese-laboratorio.md).

## O cenário

Os exercícios e os desafios usam as duas classes do [programa completo do exemplo guiado](../06-sintese.md#passo-6-executar-e-comparar-com-o-traço), `Artigo` e `Inventario`. São estas, com o método `acertar` já escrito. Em cada exercício, copia-as para o script e escreve por baixo as linhas que o enunciado dá.

```python
# As classes Artigo e Inventario do exemplo guiado do guia 06.

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

        Falha: lança ValueError se já existir um artigo com este código, ou
        se a quantidade inicial for inválida. Em qualquer falha, o
        inventário fica como estava.
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

        Falha: lança ValueError se não houver nenhum artigo com este código,
        ou se o próprio artigo recusar o pedido. Em qualquer falha, nenhuma
        quantidade muda.
        """
        artigo = self._procurar(codigo)
        artigo.retirar(unidades)

    def acertar(self, codigo, nova_quantidade):
        """Acerta a quantidade do artigo com este código, depois de uma contagem.

        Recebe: o código do artigo e a quantidade contada.
        Devolve: nada (None).
        Falha: lança ValueError se não houver nenhum artigo com este código,
        ou se a quantidade contada for inválida (quem a recusa é o setter
        do artigo). Em qualquer falha, nenhuma quantidade muda.
        """
        artigo = self._procurar(codigo)
        artigo.quantidade = nova_quantidade
```

## Exercício 1: Prever quem responde a cada pedido

No script `quem_responde.py`, copia as classes do cenário e escreve por baixo estas linhas:

```python partial
inventario = Inventario()
inventario.registar("A01", "Caderno", 6)
inventario.registar("A02", "Pasta", 2)

try:
    inventario.acertar("A01", 0)
    print("Pedido 1: aceite")
except ValueError as erro:
    print("Pedido 1:", erro)

try:
    inventario.retirar("A01", 1)
    print("Pedido 2: aceite")
except ValueError as erro:
    print("Pedido 2:", erro)

try:
    inventario.acertar("A03", 4)
    print("Pedido 3: aceite")
except ValueError as erro:
    print("Pedido 3:", erro)

try:
    inventario.retirar("A02", 0)
    print("Pedido 4: aceite")
except ValueError as erro:
    print("Pedido 4:", erro)

print("A01:", inventario.quantidade_de("A01"))
print("A02:", inventario.quantidade_de("A02"))
```

Descobre de cabeça, sem executar, as seis linhas que o programa mostra. Cada pedido encontra os artigos como o pedido anterior os deixou. Depois executa, para confirmares. Num comentário no fim do script, diz que parte do programa aceita ou recusa cada pedido: o `_procurar` do inventário, o `retirar` do artigo ou o setter do artigo. Se alguma linha do ecrã não for a que esperavas, explica no mesmo comentário onde estava o engano.

Rever: [Passo 5: prever antes de executar](../06-sintese.md#passo-5-prever-antes-de-executar) e [O plano da retirada](../06-sintese.md#o-plano-da-retirada).

<details>
<summary>Pista</summary>

Segue um pedido de cada vez, como no traço do exemplo guiado. Em cada um, lê as linhas do método que ele chama pela ordem em que correm, e vê em qual delas o pedido é aceite ou recusado.

</details>

## Exercício 2: Perguntar ao inventário se um código está livre

Antes de registar um artigo novo, quem trata do inventário quer saber se o código que escolheu está livre, sem provocar nenhuma recusa. No script `codigo_livre.py`, copia as classes do cenário e acrescenta ao `Inventario`, depois do `acertar`, um método `codigo_livre(codigo)` com este contrato:

- recebe um código;
- devolve `True` se nenhum artigo do inventário tiver esse código, e `False` se algum o tiver;
- nunca falha e não muda nada.

O método leva uma docstring que diz o contrato. Por baixo das classes, testa-o com estas linhas:

```python partial
inventario = Inventario()
inventario.registar("A01", "Caderno", 6)
inventario.registar("A02", "Pasta", 2)

print("A01 livre:", inventario.codigo_livre("A01"))
print("A02 livre:", inventario.codigo_livre("A02"))
print("A07 livre:", inventario.codigo_livre("A07"))
print("A07 livre outra vez:", inventario.codigo_livre("A07"))

vazio = Inventario()
print("A01 livre num inventário vazio:", vazio.codigo_livre("A01"))
```

O teste tem de mostrar:

```text
A01 livre: False
A02 livre: False
A07 livre: True
A07 livre outra vez: True
A01 livre num inventário vazio: True
```

Num comentário no fim do script, explica em duas frases porque é que o inventário vazio responde `True`.

Rever: [O inventário cria os artigos e encontra-os pelo código](../04-composicao-modelacao.md#o-inventário-cria-os-artigos-e-encontra-os-pelo-código) e [Passo 2: escrever o contrato](../06-sintese.md#passo-2-escrever-o-contrato).

<details>
<summary>Pista</summary>

Antes do código, descreve o método por palavras, num comentário: o que responde quando encontra o código num artigo, e o que responde quando não o encontra. Depois confirma essas palavras com as linhas do teste, uma de cada vez.

</details>

## Exercício 3: Encontrar o erro de um colega

Um colega escreveu esta versão do método `acertar`:

```python partial
    def acertar(self, codigo, nova_quantidade):
        """Acerta a quantidade do artigo com este código (versão do colega)."""
        artigo = self._procurar(codigo)
        self.quantidade = nova_quantidade
```

No script `acertar_do_colega.py`, copia as classes do cenário e troca o `acertar` do `Inventario`, o último método da classe, pelo do colega. Escreve por baixo este programa principal:

```python partial
inventario = Inventario()
inventario.registar("A01", "Caderno", 6)
inventario.registar("A02", "Pasta", 2)

inventario.acertar("A02", 5)
print("A02 depois de acertar para 5:", inventario.quantidade_de("A02"))

try:
    inventario.acertar("A01", -1)
    print("Acerto de A01 para -1: aceite")
except ValueError as erro:
    print("Acerto de A01 para -1: recusado:", erro)
print("A01 no fim:", inventario.quantidade_de("A01"))
```

Com o `acertar` certo, o programa mostra:

```text
A02 depois de acertar para 5: 5
Acerto de A01 para -1: recusado: A quantidade não pode ser negativa.
A01 no fim: 6
```

Encontra o erro e corrige o método, mudando uma só linha, até o programa mostrar estas três linhas.

Num comentário no fim do script, conta como encontraste e corrigiste o erro:

- as linhas que o programa mostrou com a versão do colega, quais são diferentes e que tipo de erro é: de escrita, de execução ou de lógica;
- a causa, em duas ou três frases: o que aconteceu ao 5 e ao -1, e porquê;
- a linha que mudaste, e como ficou;
- o que mudou em cada uma das três linhas quando voltaste a correr o programa inteiro.

Rever: [Passo 7: seguir o caminho de uma recusa](../06-sintese.md#passo-7-seguir-o-caminho-de-uma-recusa), [O inventário passa os pedidos aos artigos](../04-composicao-modelacao.md#o-inventário-passa-os-pedidos-aos-artigos) e [O `self.` decide o que fica no objeto](../02-objetos-classes-instancias.md#o-self-decide-o-que-fica-no-objeto).

<details>
<summary>Pista</summary>

Segue o pedido `acertar("A02", 5)` pelo método do colega, linha a linha. Depois de cada linha, vê que objeto mudou, se algum mudou.

</details>

## Desafios

### Desafio 1: Artigos criados fora do inventário

Um colega quer juntar a um inventário artigos que já existem, e propõe este método para o `Inventario`:

```python partial
    def acrescentar(self, artigo):
        """Junta ao inventário um artigo criado fora dele (proposta do colega)."""
        self._artigos.append(artigo)
```

No script `duas_salas.py`, copia as classes do cenário, acrescenta o método ao `Inventario`, depois do `acertar`, e escreve por baixo estas linhas:

```python partial
caderno = Artigo("A01", "Caderno", 6)

sala_12 = Inventario()
sala_14 = Inventario()
sala_12.acrescentar(caderno)
sala_14.acrescentar(caderno)

sala_12.retirar("A01", 2)
print("Sala 12, A01:", sala_12.quantidade_de("A01"))
print("Sala 14, A01:", sala_14.quantidade_de("A01"))
```

Responde num comentário no fim do script.

1. Descobre de cabeça as duas linhas que o programa mostra, e executa para confirmares. Explica a linha da sala 14, se ninguém lhe pediu nenhuma retirada.
2. No inventário de uma sala, as 6 unidades de A01 são as que estão nessa sala. Qual das duas formas serve melhor, a do `registar` ou a do `acrescentar`? Justifica em duas frases.

Rever: [Uma lista guarda os objetos, e não cópias](../04-composicao-modelacao.md#uma-lista-guarda-os-objetos-e-não-cópias) e [Dois graus de "tem": composição e agregação](../04-composicao-modelacao.md#dois-graus-de-tem-composição-e-agregação).

<details>
<summary>Pista</summary>

Procura a linha onde o caderno é criado e as linhas que o põem em cada sala. Na alínea 2, pensa no que deve acontecer à sala 14 quando alguém tira material da sala 12.

</details>

### Desafio 2: Pedidos que enganam

No script `pedidos_que_enganam.py`, copia as classes do cenário e regista A01 e A02, com 6 e 2 unidades, como no exercício 1. Por baixo, escreve estes dois pedidos, cada um no seu `try`, como os do exercício 1, e mostra no fim a quantidade de A01:

- `acertar("a01", 7)`;
- `acertar("A01", 7.0)`.

Antes de executares, descobre de cabeça se cada pedido é aceite ou recusado, quem responde e a mensagem que aparece. Num comentário no fim do script, explica cada resposta numa frase.

Rever: [O inventário cria os artigos e encontra-os pelo código](../04-composicao-modelacao.md#o-inventário-cria-os-artigos-e-encontra-os-pelo-código) e [Um set que verifica, mas não obriga](../03-encapsulamento-contratos.md#um-set-que-verifica-mas-não-obriga).

<details>
<summary>Pista</summary>

Em cada pedido, segue primeiro o `_procurar` e só depois o setter. Em cada comparação e em cada `if`, põe os valores do pedido nos dois lados, como na tabela da procura do guia 04.

</details>

## Critérios de conclusão

- Os exercícios 1 a 3 estão feitos, cada um no seu script, com o que respondeste por palavras no comentário do fim.
- No exercício 1, descobriste as seis linhas antes de executar, e o comentário diz quem aceita ou recusa cada pedido.
- No exercício 2, o método tem a docstring com o contrato, e o teste mostra as cinco linhas do enunciado.
- No exercício 3, mudaste uma só linha, e o programa mostra as três linhas do enunciado.

![Rodapé](../../imagens/rodape.png)

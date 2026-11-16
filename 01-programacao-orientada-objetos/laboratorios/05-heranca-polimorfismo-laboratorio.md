![Cabeçalho](../../imagens/cabecalho.png)

# Laboratório: Herança e polimorfismo

## O que vais construir

Escreves a classe `Notificacao` e quatro variantes que herdam dela, e pedes a todas, num só ciclo, que se apresentem. Pelo caminho, provocas erros de propósito e passas para a classe base o contrato que todas as variantes cumprem.

Acabado, o programa `notificacoes.py` mostra:

```text
Contagem concluída
Aviso interno: Material em falta
Encomenda recebida (enviada por: Secretaria)
URGENTE: A02 ESGOTOU
Texto guardado na urgente: A02 esgotou
```

1. [Fase 1: Uma classe derivada que herda tudo](#fase-1-uma-classe-derivada-que-herda-tudo)
2. [Fase 2: Uma variante que redefine um método](#fase-2-uma-variante-que-redefine-um-método)
3. [Fase 3: Uma variante com um dado novo e o `super()`](#fase-3-uma-variante-com-um-dado-novo-e-o-super)
4. [Fase 4: O mesmo pedido a todas as variantes](#fase-4-o-mesmo-pedido-a-todas-as-variantes)
5. [Fase 5: O contrato de uma classe abstrata](#fase-5-o-contrato-de-uma-classe-abstrata)
6. [Fase 6: Uma variante nova, sem mudar o ciclo](#fase-6-uma-variante-nova-sem-mudar-o-ciclo)

## O que precisas

- O Python 3.10 ou mais recente. Confirma a versão com `python3 --version` no terminal, ou `py --version` no Windows: aparece uma linha como `Python 3.12.4`. Com uma versão anterior, os programas correm na mesma, e mudam só algumas mensagens de erro, que o texto assinala.
- O editor de Python das aulas, o mesmo dos laboratórios anteriores.

Partes de uma pasta vazia, sem nenhum ficheiro de outro laboratório.

## Preparar o projeto

1. Cria a pasta `tema-05` dentro da pasta onde tens os trabalhos de LP. Os ficheiros deste tema ficam todos lá, à parte dos de outros laboratórios.

2. Abre o editor e cria, dentro de `tema-05`, o ficheiro `notificacoes.py`, escrito tal e qual, sem espaços nem acentos. É nele que trabalhas nas seis fases.

## Fase 1: Uma classe derivada que herda tudo

Escreves a classe base `Notificacao`, que guarda o texto e se apresenta, e a classe derivada `NotificacaoBreve`, que herda tudo dela sem escrever nenhum método. É a herança, escrita com o nome da base entre parênteses, a seguir ao nome da classe nova. Rever: [Uma classe derivada que herda tudo](../05-heranca-polimorfismo.md#uma-classe-derivada-que-herda-tudo) e [Especialização: do geral para o particular](../05-heranca-polimorfismo.md#especialização-do-geral-para-o-particular).

1. Escreve à mão no `notificacoes.py` esta primeira versão. Escrever, em vez de copiar, faz-te reparar nos parênteses de `class NotificacaoBreve(Notificacao):` e nos dois pontos no fim das linhas `class` e `def`.

   ```python
   # notificacoes.py: notificações com herança, do laboratório do tema 05.

   class Notificacao:
       """Uma mensagem preparada para ser apresentada a alguém."""

       def __init__(self, texto):
           """Guarda o texto da notificação."""
           self.texto = texto

       def apresentar(self):
           """Devolve o texto da notificação, pronto a mostrar."""
           return self.texto


   class NotificacaoBreve(Notificacao):
       """Notificação que apresenta só o texto: faz tudo como a classe base."""
   ```

   A `NotificacaoBreve` só tem a docstring, e chega: sem ela, a classe ficava sem corpo, e o Python recusava o ficheiro.

2. Guarda e executa. O que deves ver: nada. O ficheiro só define as duas classes, e definir uma classe não mostra nada no ecrã. Se aparecer outra coisa, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

3. Deixa duas linhas em branco depois da docstring da `NotificacaoBreve` e escreve, encostadas à margem, estas linhas de teste:

   ```python partial
   breve = NotificacaoBreve("Contagem concluída")
   print(breve.texto)
   print(breve.apresentar())
   print(isinstance(breve, NotificacaoBreve))
   print(isinstance(breve, Notificacao))
   ```

   Antes de executares, prevê: a `NotificacaoBreve` não escreve construtor nem `apresentar`. Quem guarda o texto da breve, e que `apresentar` responde na linha `print(breve.apresentar())`? Depois guarda e executa. O que deves ver:

   ```text
   Contagem concluída
   Contagem concluída
   True
   True
   ```

   A resposta: o construtor e o `apresentar` vêm os dois da `Notificacao`. O Python procura-os primeiro na classe do objeto, não os encontra e usa os da classe base. Os dois `True` dizem que a breve é uma `NotificacaoBreve` e, ao mesmo tempo, uma `Notificacao`. Se aparecer outra coisa, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

### Paragem 1

O ficheiro tem as duas classes e as linhas de teste, e o programa mostra as quatro linhas do passo 3.

Pensa antes de continuares: se criasses outra notificação breve, com o texto "Material em falta", o texto da primeira mudava? A resposta: não. A herança liga a classe `NotificacaoBreve` à classe `Notificacao`, e não os objetos uns aos outros, e cada breve fica com o seu texto.

## Fase 2: Uma variante que redefine um método

Acrescentas a `NotificacaoDetalhada`, que herda o construtor da base e escreve o seu próprio `apresentar`, com "Aviso interno: " antes do texto. Diz-se que redefine o método, e o Python escolhe a versão a usar pela regra de procura: primeiro na classe do objeto, depois na base. Rever: [Uma variante que redefine um método](../05-heranca-polimorfismo.md#uma-variante-que-redefine-um-método).

1. Entre a classe `NotificacaoBreve` e as linhas de teste, escreve a classe `NotificacaoDetalhada`, com duas linhas em branco antes e depois dela:

   ```python partial
   class NotificacaoDetalhada(Notificacao):
       """Notificação que apresenta o texto com um aviso antes."""

       def apresentar(self):
           """Devolve o texto com "Aviso interno: " antes."""
           return "Aviso interno: " + self.texto
   ```

2. Substitui as linhas de teste, desde `breve = ...` até ao fim do ficheiro, por estas:

   ```python partial
   breve = NotificacaoBreve("Contagem concluída")
   detalhada = NotificacaoDetalhada("Material em falta")
   print(breve.apresentar())
   print(detalhada.apresentar())
   ```

   Guarda e executa. O que deves ver:

   ```text
   Contagem concluída
   Aviso interno: Material em falta
   ```

   A segunda linha vem do `apresentar` da detalhada, que o Python encontra logo na classe do objeto. O da base continua no ficheiro, e é ele que responde à breve, na primeira linha.

3. Provoca agora um esquecimento. Na `NotificacaoDetalhada`, apaga o método `apresentar` inteiro, com a linha do `def`, a docstring dele e o `return`, e deixa só a docstring da classe. Antes de executares, prevê: o que mostra agora a segunda linha, e aparece algum erro? Depois guarda e executa. O que deves ver:

   ```text
   Contagem concluída
   Material em falta
   ```

   A resposta: a detalhada passou a apresentar-se como a breve, e não apareceu nenhum erro. Sem um `apresentar` na classe do objeto, a regra de procura vai buscar o da base, e para o Python não falta nada. Se aparecer um `IndentationError`, apagaste também a docstring da classe: vê [Aparece `IndentationError`, `TabError` ou `SyntaxError`](#aparece-indentationerror-taberror-ou-syntaxerror).

4. Volta a escrever o `apresentar` da detalhada, como no passo 1, e executa. O aviso volta à segunda linha.

### Paragem 2

O programa mostra `Contagem concluída` e `Aviso interno: Material em falta`, como no passo 2.

Pensa antes de continuares: quando `breve.apresentar()` corre o método escrito na `Notificacao`, quem é o `self`? A resposta: a breve. O `self` é sempre o objeto antes do ponto, também quando o método vem da classe base, e por isso `self.texto` dá o texto da breve.

## Fase 3: Uma variante com um dado novo e o `super()`

Acrescentas a `NotificacaoAssinada`, que guarda também a origem e por isso escreve o seu construtor, que recebe dois valores. A primeira linha dele, `super().__init__(texto)`, pede ao construtor da classe base que guarde o texto. Rever: [Uma variante com um dado novo e o `super()`](../05-heranca-polimorfismo.md#uma-variante-com-um-dado-novo-e-o-super).

1. A seguir à classe `NotificacaoDetalhada`, com duas linhas em branco antes e depois, escreve a classe `NotificacaoAssinada`:

   ```python partial
   class NotificacaoAssinada(Notificacao):
       """Notificação que diz, no fim, quem a enviou."""

       def __init__(self, texto, origem):
           """Guarda o texto, através do construtor da classe base, e a origem."""
           super().__init__(texto)
           self.origem = origem

       def apresentar(self):
           """Devolve o texto seguido da origem, entre parênteses."""
           return self.texto + " (enviada por: " + self.origem + ")"
   ```

2. Substitui as linhas de teste, desde `breve = ...`, por estas:

   ```python partial
   assinada = NotificacaoAssinada("Encomenda recebida", "Secretaria")
   print(assinada.origem)
   print(assinada.apresentar())
   ```

   Guarda e executa. O que deves ver:

   ```text
   Secretaria
   Encomenda recebida (enviada por: Secretaria)
   ```

   A origem foi guardada pelo construtor da assinada, e o texto pelo construtor da base, que o `super()` chamou.

3. Provoca um erro de propósito: no construtor da assinada, apaga a linha `super().__init__(texto)`. Antes de executares, prevê: o programa para na linha que cria a assinada, ou mais à frente? Depois guarda e executa. O programa mostra `Secretaria` e para com esta mensagem:

   ```text
   Traceback (most recent call last):
     File ".../tema-05/notificacoes.py", line 41, in <module>
       print(assinada.apresentar())
             ~~~~~~~~~~~~~~~~~~~^^
     File ".../tema-05/notificacoes.py", line 36, in apresentar
       return self.texto + " (enviada por: " + self.origem + ")"
              ^^^^^^^^^^
   AttributeError: 'NotificacaoAssinada' object has no attribute 'texto'
   ```

   Os três pontos ficam no lugar da pasta do teu computador, e as linhas de `~` e `^` só aparecem a partir do Python 3.11. A última linha, um `AttributeError` (erro de atributo), diz que o objeto `NotificacaoAssinada` não tem o atributo `texto`. Com o ficheiro escrito como os passos mandam, os números de linha da mensagem são 41 e 36. Com uma linha em branco a mais ou a menos, os teus números são outros.

   A resposta: mais à frente. O construtor da assinada guardou a origem e acabou sem erro. O da base, que guardava o texto, nunca correu: o da assinada tapa-o, e só a linha que apagaste o chamava. Cada linha `File` diz onde o Python estava, com o código por baixo: a de cima acaba em `in <module>`, o programa principal, que são as linhas fora das classes. A de baixo acaba em `in apresentar`, onde o texto foi usado pela primeira vez. O erro vê-se longe da causa, que está no construtor, e é um erro de execução, porque o programa começou e parou a meio.

4. Volta a pôr a linha `super().__init__(texto)` como primeira linha do construtor, e executa. As duas linhas do passo 2 voltam.

### Paragem 3

O programa mostra as duas linhas do passo 2. O `notificacoes.py` inteiro, como o teu deve estar:

```python
# notificacoes.py: notificações com herança, do laboratório do tema 05.

class Notificacao:
    """Uma mensagem preparada para ser apresentada a alguém."""

    def __init__(self, texto):
        """Guarda o texto da notificação."""
        self.texto = texto

    def apresentar(self):
        """Devolve o texto da notificação, pronto a mostrar."""
        return self.texto


class NotificacaoBreve(Notificacao):
    """Notificação que apresenta só o texto: faz tudo como a classe base."""


class NotificacaoDetalhada(Notificacao):
    """Notificação que apresenta o texto com um aviso antes."""

    def apresentar(self):
        """Devolve o texto com "Aviso interno: " antes."""
        return "Aviso interno: " + self.texto


class NotificacaoAssinada(Notificacao):
    """Notificação que diz, no fim, quem a enviou."""

    def __init__(self, texto, origem):
        """Guarda o texto, através do construtor da classe base, e a origem."""
        super().__init__(texto)
        self.origem = origem

    def apresentar(self):
        """Devolve o texto seguido da origem, entre parênteses."""
        return self.texto + " (enviada por: " + self.origem + ")"


assinada = NotificacaoAssinada("Encomenda recebida", "Secretaria")
print(assinada.origem)
print(assinada.apresentar())
```

Em cima está a classe base, que guarda o texto e se apresenta da maneira breve, e por baixo as três variantes, cada uma só com o que muda. No fim ficam as linhas de teste, que criam uma assinada e mostram a origem e a apresentação dela.

Pensa antes de continuares: porque é que a `NotificacaoBreve` e a `NotificacaoDetalhada` não têm a linha do `super()`? A resposta: porque não escrevem construtor. Quando se cria uma delas, corre o construtor que herdam da base, e o `super().__init__` só faz falta num construtor que tapa o da base.

## Fase 4: O mesmo pedido a todas as variantes

Juntas numa lista uma notificação de cada variante e pedes a todas, num ciclo `for`, que se apresentem, sempre com a mesma linha. Chama-se polimorfismo a este mesmo pedido, a que cada objeto responde à maneira da sua classe. Rever: [O mesmo pedido a todas as variantes](../05-heranca-polimorfismo.md#o-mesmo-pedido-a-todas-as-variantes).

1. Substitui as linhas de teste, desde `assinada = ...`, por estas:

   ```python partial
   avisos = [
       NotificacaoBreve("Contagem concluída"),
       NotificacaoDetalhada("Material em falta"),
       NotificacaoAssinada("Encomenda recebida", "Secretaria"),
   ]

   for aviso in avisos:
       print(aviso.apresentar())
   ```

   Os três objetos criam-se dentro dos parênteses retos, um por linha e separados por vírgulas, e a lista fica com os três, como se lhe fizesses três `append`.

2. Antes de executares, prevê as três linhas, uma volta de cada vez: de que classe é o objeto, e onde encontra o Python o `apresentar` dele? Depois guarda e executa. O que deves ver:

   ```text
   Contagem concluída
   Aviso interno: Material em falta
   Encomenda recebida (enviada por: Secretaria)
   ```

   A resposta, volta a volta:

   | Volta | Classe do objeto | Onde o Python encontra `apresentar` | Linha mostrada |
   | --- | --- | --- | --- |
   | 1 | `NotificacaoBreve` | Na classe base, `Notificacao` | `Contagem concluída` |
   | 2 | `NotificacaoDetalhada` | Na própria classe | `Aviso interno: Material em falta` |
   | 3 | `NotificacaoAssinada` | Na própria classe | `Encomenda recebida (enviada por: Secretaria)` |

### Paragem 4

O programa mostra as três linhas do passo 2, uma por variante.

Pensa antes de continuares: se escrevesses uma quarta variante, que linhas do ciclo terias de mudar? A resposta: nenhuma. Juntavas um objeto dela à lista, e o ciclo pedia-lhe que se apresentasse, como às outras, porque nenhuma linha do programa pergunta de que variante é cada notificação.

## Fase 5: O contrato de uma classe abstrata

Escreves o contrato da `Notificacao` como o de uma classe abstrata, primeiro por palavras e depois nas docstrings da classe base, sem mudar nenhuma instrução. No modelo, a `Notificacao` é uma classe abstrata, de onde não se criam objetos, e o `apresentar` é um método abstrato, sem instruções gerais. Rever: [O contrato de uma classe abstrata](../05-heranca-polimorfismo.md#o-contrato-de-uma-classe-abstrata), [O contrato na docstring da classe base](../05-heranca-polimorfismo.md#o-contrato-na-docstring-da-classe-base) e [O contrato comum](../05-heranca-polimorfismo.md#o-contrato-comum).

1. Começa por criar uma notificação da própria classe base. No fim do ficheiro, a seguir ao ciclo e encostadas à margem, acrescenta estas duas linhas:

   ```python partial
   geral = Notificacao("Olá")
   print(geral.apresentar())
   ```

   Antes de executares, prevê: o Python deixa criar esta notificação geral, e como é que ela se apresenta? Depois guarda e executa. O que deves ver:

   ```text
   Contagem concluída
   Aviso interno: Material em falta
   Encomenda recebida (enviada por: Secretaria)
   Olá
   ```

   A resposta: deixa, e ela apresenta-se da maneira breve, com o `apresentar` da `Notificacao`. Para o Python, a base é uma classe como as outras. No modelo, uma notificação geral não tem maneira própria de se apresentar, e os objetos criam-se das variantes. No ficheiro, a base apresenta-se da maneira breve, e por isso a breve não escreve o seu `apresentar`: só o redefinem as variantes que se apresentam de outra maneira.

   Apaga as duas linhas que acrescentaste.

2. Completa de cabeça o contrato abstrato da `Notificacao`, escrito nesta forma, organizada pela indentação. As três primeiras linhas já estão feitas.

   ```text
   Classe abstrata Notificacao
       Todas têm: um texto, guardado quando a notificação é criada
       Todas sabem: apresentar()   (abstrato: cada variante escreve como)
           recebe: A completar
           devolve: A completar
           não faz: A completar
   ```

   A resposta: em "recebe", nada, além do `self`; em "devolve", um texto pronto a mostrar; em "não faz", alterar a notificação e mostrar o texto no ecrã. Quem pediu o texto é que decide onde o mostra. Esta forma não é a única: serve qualquer uma que diga o que todas as notificações têm e o contrato do `apresentar` por inteiro.

3. Passa agora o contrato para o código. Substitui a classe `Notificacao` inteira por esta versão, em que só mudam as duas docstrings:

   ```python partial
   class Notificacao:
       """Uma mensagem preparada para ser apresentada a alguém.

       No modelo, é uma classe abstrata: os objetos criam-se das variantes.
       Todas as notificações guardam um texto e sabem apresentar-se. Uma
       variante que se apresente de outra maneira redefine apresentar().
       """

       def __init__(self, texto):
           """Guarda o texto da notificação."""
           self.texto = texto

       def apresentar(self):
           """Devolve o texto da notificação, pronto a mostrar.

           Contrato: não recebe nada além do self, devolve um texto pronto a
           mostrar e não altera a notificação. Não mostra nada no ecrã.
           """
           return self.texto
   ```

   Uma docstring comprida tem uma frase na primeira linha, uma linha em branco, o resto da explicação e, sozinhas na última linha, as três aspas que a fecham. O "No modelo" da docstring da classe é a descrição do passo 2.

4. Guarda e executa. O que deves ver: as três linhas da fase 4, iguais. As docstrings explicam o programa a quem o lê, e não mudam o que ele faz.

5. Responde de cabeça: se repetisses agora a experiência da fase 2, em que apagaste o `apresentar` da detalhada, o contrato na docstring fazia aparecer um erro? A resposta: não. A detalhada voltava a apresentar-se como a base, sem nenhum aviso, porque o Python não confere se as variantes cumprem o que a docstring diz. O esquecimento só se apanha quando se compara a saída com o que o contrato e a previsão diziam.

### Paragem 5

O programa mostra as três linhas da fase 4, e a classe base tem o contrato nas docstrings. O ficheiro completo, como deve estar agora:

```python
# notificacoes.py: notificações com herança, do laboratório do tema 05.

class Notificacao:
    """Uma mensagem preparada para ser apresentada a alguém.

    No modelo, é uma classe abstrata: os objetos criam-se das variantes.
    Todas as notificações guardam um texto e sabem apresentar-se. Uma
    variante que se apresente de outra maneira redefine apresentar().
    """

    def __init__(self, texto):
        """Guarda o texto da notificação."""
        self.texto = texto

    def apresentar(self):
        """Devolve o texto da notificação, pronto a mostrar.

        Contrato: não recebe nada além do self, devolve um texto pronto a
        mostrar e não altera a notificação. Não mostra nada no ecrã.
        """
        return self.texto


class NotificacaoBreve(Notificacao):
    """Notificação que apresenta só o texto: faz tudo como a classe base."""


class NotificacaoDetalhada(Notificacao):
    """Notificação que apresenta o texto com um aviso antes."""

    def apresentar(self):
        """Devolve o texto com "Aviso interno: " antes."""
        return "Aviso interno: " + self.texto


class NotificacaoAssinada(Notificacao):
    """Notificação que diz, no fim, quem a enviou."""

    def __init__(self, texto, origem):
        """Guarda o texto, através do construtor da classe base, e a origem."""
        super().__init__(texto)
        self.origem = origem

    def apresentar(self):
        """Devolve o texto seguido da origem, entre parênteses."""
        return self.texto + " (enviada por: " + self.origem + ")"


avisos = [
    NotificacaoBreve("Contagem concluída"),
    NotificacaoDetalhada("Material em falta"),
    NotificacaoAssinada("Encomenda recebida", "Secretaria"),
]

for aviso in avisos:
    print(aviso.apresentar())
```

Desde a paragem 3, só mudaram as docstrings da `Notificacao`, e as instruções das classes são as mesmas. Por baixo das classes, as linhas de teste deram lugar à lista e ao ciclo da fase 4.

Pensa antes de continuares: abstrata quer dizer vazia? A resposta: não. O texto guardado na criação, a primeira linha do contrato, vale para todas as notificações. O ficheiro escreve-o uma só vez, no construtor da base, que as variantes herdam ou, como a assinada, chamam com o `super()`. O que cada variante pode mudar é só a maneira de se apresentar.

## Fase 6: Uma variante nova, sem mudar o ciclo

Acrescentas a `NotificacaoUrgente`, que se apresenta com "URGENTE: " e o texto em maiúsculas, e juntas uma à lista sem mexer no ciclo da fase 4. Não guarda dados novos, por isso não escreve construtor, e redefine o `apresentar`, como o contrato da base prevê. Rever: [Uma variante nova, sem mudar o ciclo](../05-heranca-polimorfismo.md#uma-variante-nova-sem-mudar-o-ciclo).

1. A seguir à classe `NotificacaoAssinada`, com duas linhas em branco antes e depois, escreve a classe `NotificacaoUrgente`:

   ```python partial
   class NotificacaoUrgente(Notificacao):
       """Notificação que pede atenção imediata: o texto aparece em maiúsculas."""

       def apresentar(self):
           """Devolve "URGENTE: " seguido do texto em maiúsculas, sem alterar o texto guardado."""
           return "URGENTE: " + self.texto.upper()
   ```

   O `upper`, que em inglês quer dizer "de cima", como as letras maiúsculas, devolve um texto novo, todo em maiúsculas, e deixa o texto guardado como estava. Por isso, este `apresentar` não altera a notificação, como o contrato promete.

2. Na lista `avisos`, a seguir à linha da assinada, que acaba numa vírgula, acrescenta, com os mesmos quatro espaços, a linha `NotificacaoUrgente("A02 esgotou"),`. Depois, no fim do ficheiro, deixa uma linha em branco a seguir ao ciclo e acrescenta, encostada à margem, esta linha:

   ```python partial
   print("Texto guardado na urgente:", avisos[3].texto)
   ```

   O `[3]` escolhe o quarto elemento da lista, a urgente, porque as posições se contam a partir do 0. Antes de executares, prevê as cinco linhas. Depois guarda e executa. O que deves ver:

   ```text
   Contagem concluída
   Aviso interno: Material em falta
   Encomenda recebida (enviada por: Secretaria)
   URGENTE: A02 ESGOTOU
   Texto guardado na urgente: A02 esgotou
   ```

   A quarta linha vem do `apresentar` da urgente, e a última mostra o texto guardado tal como foi criado, porque o `upper` não mexeu no atributo. O ciclo `for` é, letra a letra, o da fase 4.

3. Provoca agora uma quebra do contrato. No `apresentar` da urgente, troca a linha do `return` por estas duas, com a mesma indentação:

   ```python partial
           self.texto = self.texto.upper()
           return "URGENTE: " + self.texto
   ```

   Guarda e executa. Só muda a última linha, que passa a `Texto guardado na urgente: A02 ESGOTOU`. O método mudou o atributo `texto`, que o contrato manda deixar como está, e nenhuma mensagem de erro o disse.

4. Volta a pôr o `return` do passo 1 e executa. A última linha volta a mostrar `A02 esgotou`.

### Paragem 6

O programa mostra as cinco linhas do passo 2. O ficheiro `notificacoes.py` completo, como deve ficar no fim:

```python
# notificacoes.py: notificações com herança, do laboratório do tema 05.

class Notificacao:
    """Uma mensagem preparada para ser apresentada a alguém.

    No modelo, é uma classe abstrata: os objetos criam-se das variantes.
    Todas as notificações guardam um texto e sabem apresentar-se. Uma
    variante que se apresente de outra maneira redefine apresentar().
    """

    def __init__(self, texto):
        """Guarda o texto da notificação."""
        self.texto = texto

    def apresentar(self):
        """Devolve o texto da notificação, pronto a mostrar.

        Contrato: não recebe nada além do self, devolve um texto pronto a
        mostrar e não altera a notificação. Não mostra nada no ecrã.
        """
        return self.texto


class NotificacaoBreve(Notificacao):
    """Notificação que apresenta só o texto: faz tudo como a classe base."""


class NotificacaoDetalhada(Notificacao):
    """Notificação que apresenta o texto com um aviso antes."""

    def apresentar(self):
        """Devolve o texto com "Aviso interno: " antes."""
        return "Aviso interno: " + self.texto


class NotificacaoAssinada(Notificacao):
    """Notificação que diz, no fim, quem a enviou."""

    def __init__(self, texto, origem):
        """Guarda o texto, através do construtor da classe base, e a origem."""
        super().__init__(texto)
        self.origem = origem

    def apresentar(self):
        """Devolve o texto seguido da origem, entre parênteses."""
        return self.texto + " (enviada por: " + self.origem + ")"


class NotificacaoUrgente(Notificacao):
    """Notificação que pede atenção imediata: o texto aparece em maiúsculas."""

    def apresentar(self):
        """Devolve "URGENTE: " seguido do texto em maiúsculas, sem alterar o texto guardado."""
        return "URGENTE: " + self.texto.upper()


avisos = [
    NotificacaoBreve("Contagem concluída"),
    NotificacaoDetalhada("Material em falta"),
    NotificacaoAssinada("Encomenda recebida", "Secretaria"),
    NotificacaoUrgente("A02 esgotou"),
]

for aviso in avisos:
    print(aviso.apresentar())

print("Texto guardado na urgente:", avisos[3].texto)
```

As cinco classes vêm por ordem: a base, com o contrato, e as quatro variantes, cada uma só com o que muda. Em baixo, a lista tem uma notificação de cada variante, o ciclo pede a todas que se apresentem, e a última linha confirma o texto guardado na urgente.

Pensa antes de terminares: sem a urgente, a árvore de especialização das notificações, lida de baixo para cima com "é uma", é esta:

```text
Notificacao
├── NotificacaoBreve
├── NotificacaoDetalhada
└── NotificacaoAssinada
```

Como fica com a urgente, e que frase diz o que ela acrescenta ou muda em relação à `Notificacao`? A resposta: a árvore ganha um ramo, por baixo da `Notificacao`, ao lado dos outros três.

```text
Notificacao
├── NotificacaoBreve
├── NotificacaoDetalhada
├── NotificacaoAssinada
└── NotificacaoUrgente
```

A frase: "A `NotificacaoUrgente` é uma `Notificacao`; não guarda dados novos e redefine o `apresentar`, que devolve "URGENTE: " e o texto em maiúsculas."

## Se alguma coisa falhar

1. Guardaste antes de executar? Quando a saída fica igual à de antes da tua alteração, quase sempre o ficheiro não foi guardado.
2. Estás a executar o `notificacoes.py` da pasta `tema-05`, e não um ficheiro de outro tema?
3. Executaste o ficheiro inteiro? Cada execução começa do zero e cria as notificações com os textos escritos no ficheiro.
4. Desfizeste a experiência anterior? Nas fases 2, 3, 5 e 6, cada experiência diz como se desfaz. Se te perderes nas fases 1 ou 2, recomeça pelo passo 1 da fase 1. Mais à frente, copia o ficheiro da última paragem que o mostra inteiro, a 3, a 5 ou a 6, e refaz daí os passos.
5. Apareceu uma mensagem de erro? Os títulos a seguir são as mensagens que este laboratório pode dar: procura o que diz a última linha da tua.

### Aparece `IndentationError`, `TabError` ou `SyntaxError`

Com um erro de escrita, nenhuma linha do programa corre: o Python para logo na leitura do ficheiro. A mensagem não tem `Traceback`: começa pelo ficheiro e pelo número da linha onde a leitura parou. Neste laboratório, as mais prováveis são estas:

- `IndentationError: expected an indented block after class definition on line`, com o número da linha da classe (no Python 3.9, só `expected an indented block`): uma classe ficou sem nada por baixo. Acontece à breve sem a docstring, ou à detalhada, na fase 2, se apagares o `apresentar` e também a docstring da classe.
- `IndentationError: unexpected indent` ("indentação inesperada"): uma linha tem espaços a mais à frente, como uma linha de teste a meio das outras.
- `IndentationError: unindent does not match any outer indentation level`: uma linha ficou numa margem que não é a de nenhuma linha de cima, como um `def` com dois espaços.
- `TabError: inconsistent use of tabs and spaces in indentation`: uma tabulação misturou-se com os espaços da indentação. Apaga-a e escreve os espaços.
- `SyntaxError: expected ':'` (no Python 3.9, só `invalid syntax`): a linha de um `class`, de um `def` ou do `for` acabou sem os dois pontos.

Numa classe, a docstring e cada `def` começam a quatro espaços da margem, e o que está dentro de um método começa a oito. As linhas de teste, a lista e o `for` ficam encostados à margem, e a linha de dentro do `for` leva quatro. Põe a linha que a mensagem aponta, e a de cima, ao lado das do bloco do laboratório, espaço a espaço.

### Aparece `NameError: name 'Notificacao' is not defined`, ou com um nome parecido

`NameError` quer dizer erro de nome. A mensagem aponta a linha de uma classe derivada, como `class NotificacaoBreve(Notificacao):`, e o Python não conhece o nome entre parênteses quando a lê. A base está escrita mais abaixo, ou o nome entre parênteses não é, letra a letra, o da base. Neste caso, as versões recentes sugerem o nome parecido, como `Did you mean: 'Notificacao'?` ("querias dizer `Notificacao`?"). Põe a classe base antes de todas as outras, e compara, letra a letra, o nome entre parênteses com o da linha `class Notificacao:`.

### Aparece `NameError` com o nome da última classe do ficheiro, ou não aparece nada

Há espaços no início das linhas que vêm depois das classes. Com quatro espaços, o Python junta-as à última classe, que ainda está a ler, e a linha `File` de baixo acaba em `in` e no nome dessa classe. A mensagem mostra também a linha `class` dessa classe e, no Python 3.14, uma linha como `...<7 lines>...`, e pode sugerir outro nome, que aqui não ajuda. Com oito espaços, a partir da fase 2, as linhas entram no último método e nunca correm, e não aparece nada. Tira os espaços do início dessas linhas, para ficarem fora das classes.

### Uma linha aparece repetida, a meio das linhas do ciclo

A linha que acrescentaste depois do ciclo tem espaços à frente, e o Python juntou-a ao `for`. O ciclo corre-a em cada volta, mesmo com uma linha em branco pelo meio. Encosta-a à margem, como o `for`.

### Aparece `TypeError: NotificacaoAssinada.__init__() missing 1 required positional argument: 'origem'`

`TypeError` quer dizer erro de tipo. A assinada foi criada só com o texto, e o construtor dela pede dois valores, além do `self`: o texto e a origem, por esta ordem. No Python 3.9, a mensagem começa só por `__init__()`. Escreve os dois, como em `NotificacaoAssinada("Encomenda recebida", "Secretaria")`.

### Aparece `TypeError: Notificacao.__init__() missing 1 required positional argument: 'texto'`

Quem se queixa é o construtor da base, e a linha `File` de baixo mostra o `super().__init__()` do construtor da assinada, com os parênteses vazios. No Python 3.9, a última linha não tem o `Notificacao.` antes do `__init__()`. O construtor da base também precisa do texto, e é a assinada que lho passa: escreve `super().__init__(texto)`.

### Aparece `TypeError: Notificacao.__init__() takes 1 positional argument but 2 were given`

Quer dizer que o construtor da `Notificacao` aceita um valor e recebeu dois. A linha `def __init__` ficou sem o `self`, ou sem o `texto`. Ao criar uma notificação, o Python passa ao construtor dois valores, o próprio objeto e o texto, e o `def` tem de ter um nome para cada um. Escreve `def __init__(self, texto):`. Na assinada, o mesmo engano dá `takes 2 positional arguments but 3 were given`, e num `apresentar` sem o `self` aparece `NotificacaoDetalhada.apresentar() takes 0 positional arguments but 1 was given`. No Python 3.9, a mensagem não tem o nome da classe antes do método.

### Aparece `AttributeError: 'NotificacaoAssinada' object has no attribute 'texto'`

É o erro que provocaste no passo 3 da fase 3: falta a linha `super().__init__(texto)` no construtor da assinada. Põe-na como primeira linha do construtor. Se a linha está lá, ou se a mensagem traz outra classe, como `'NotificacaoBreve'`, o engano está no construtor da `Notificacao`. A linha de dentro dele tem de ser `self.texto = texto`, com o `self.` e o nome `texto`. Nesse caso, as versões recentes sugerem o nome que lá ficou, como `Did you mean: 'text'?`.

### Uma variante apresenta-se como a base, sem nenhum erro

A linha dessa variante mostra só o texto, como a breve. O Python não encontrou um `apresentar` na classe dela e, pela regra de procura, usou o da base. Confirma que o método se chama exatamente `apresentar`, e não `apresenta`, e que o `def` está quatro espaços para dentro, na classe, e não encostado à margem.

### Aparece `None` numa linha do ciclo, com uma linha a mais por cima

O `apresentar` de uma variante mostra o texto com `print`, em vez de o devolver com `return`. A linha de cima vem do `print` do método, e o `None` é o que o ciclo recebeu, porque um método sem `return` não devolve nada. Troca o `print` por `return`: quem pede o texto é que decide se o mostra.

### Aparece `TypeError: can only concatenate str (not "builtin_function_or_method") to str`

Aparece na quarta volta do ciclo, depois das três primeiras linhas, e a linha `File` de baixo mostra o `return` da urgente. Compara essa linha, letra a letra, com a do passo 1 da fase 6.

## Desafios

Os desafios fazem-se numa cópia. Cria no editor um ficheiro `desafios.py`, também na pasta `tema-05`, e cola nele todo o `notificacoes.py` da paragem 6. As respostas vão para um comentário no fim do `desafios.py`, e o `notificacoes.py` não muda.

1. Uma variante tua, sem dados novos. Inventa uma maneira nova de apresentar uma notificação só a partir do texto, diferente das deste laboratório, como pôr o texto entre parênteses retos ou começar por "Lembrete: ". Escreve a classe, com uma docstring na classe e outra no método, e junta um objeto dela à lista `avisos`. Prevê a linha nova antes de executares. Depois do ciclo, mostra também o atributo `texto` da tua notificação, e confirma que não mudou.

   Responde no comentário do fim: esta variante precisa de construtor próprio? Porquê?

   Pista: pensa no que a variante tem de guardar que a base ainda não guarde.

2. Uma variante tua, com um dado novo. Inventa uma variante que guarde mais um dado além do texto, como uma notificação com prazo, que se apresente como "Devolver os marcadores (até sexta-feira)". O dado e o formato escolhes tu, desde que não sejam os da assinada. O construtor recebe o texto e o dado novo. Junta um objeto desta variante à lista, prevê a linha que vai aparecer e executa.

   Pista: lembra-te do que aconteceu na fase 3, quando faltou uma linha no construtor.

3. A árvore e a descrição do teu programa. Desenha no papel a árvore de especialização do teu `desafios.py`, sem copiar a da paragem 6. Põe a `Notificacao` no topo e, por baixo, todas as variantes que o ficheiro tem, também as tuas. Debaixo da árvore, escreve uma frase para cada variante, com "é uma `Notificacao`" e o que ela acrescenta ou redefine.

## Antes de terminares

- [ ] Ao executar o `notificacoes.py`, aparecem as cinco linhas da paragem 6.
- [ ] Desfizeste as experiências e apagaste as duas linhas da notificação geral: o `notificacoes.py` está igual ao da paragem 6.
- [ ] As docstrings da `Notificacao` e do seu `apresentar` têm o contrato da fase 5.
- [ ] Entregaste, como o professor indicar, o `notificacoes.py` e, se fizeste os desafios, o `desafios.py`, com as respostas no fim, e o desenho do desafio 3.
- [ ] Sabes dizer onde o Python encontrou o `apresentar` de cada volta do ciclo.
- [ ] Sabes dizer o que a docstring da classe base diz a quem escreve uma variante nova, e porque é que não obriga ninguém a cumprir o contrato.
- [ ] Consegues explicar o polimorfismo por palavras tuas, com o ciclo deste laboratório.

![Rodapé](../../imagens/rodape.png)

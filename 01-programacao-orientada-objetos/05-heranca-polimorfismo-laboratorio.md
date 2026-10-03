![Cabeçalho](../imagens/cabecalho.png)

# Laboratório: notificações com herança, polimorfismo e uma classe abstrata

*M10 · Caderno 5 · Laboratório*

Este laboratório acompanha o [caderno 5](05-heranca-polimorfismo.md). Diz-te o que fazer, passo a passo, com o editor de Python aberto ao lado. As explicações do porquê estão no caderno: cada parte diz em que secção deves ter o caderno aberto, e quando um passo usa uma ideia, o texto diz em que secção ela está explicada. Conta com cerca de 85 minutos, repartidos pela aula, à medida que o professor for explicando cada secção.

No fim deves ter um ficheiro `notificacoes.py` com uma classe abstrata, várias variantes e um ciclo que as apresenta todas; deves ter provocado de propósito, e lido, três erros típicos da herança; e deves ter escrito duas variantes tuas.

## Antes de começar

Precisas do computador com o editor de Python que usas nas aulas, e de papel e caneta para as previsões e para o diagrama da última parte.

Não precisas de ler o caderno todo antes de começar: o laboratório faz-se ao longo da aula, e cada parte diz que secção deves ter aberta. A parte 7 usa também o exemplo guiado da secção 9. O laboratório não repete as explicações: aplica-as.

A forma de trabalhar é a do laboratório anterior. Antes de executares, escreves no papel o que esperas ver. Depois executas e comparas. Quando o resultado é diferente do que previste, explica a diferença antes de continuares. Executa sempre o ficheiro inteiro.

Nas partes 3, 4 e 6 vais estragar o programa de propósito, para veres um erro acontecer. Faz sempre a alteração pedida, observa, e desfaz a alteração antes de passares à parte seguinte. Se te perderes, o programa completo de cada parte está no caderno, na secção indicada.

## Parte 1: preparar o ficheiro (3 min)

1. Na pasta onde guardas os trabalhos de LP, cria uma pasta nova chamada `caderno-5`.
2. Dentro dela, cria um ficheiro chamado `notificacoes.py`.

## Parte 2: a classe base e a primeira classe derivada (10 min)

Tem aberta ao lado a secção 3 do caderno.

1. Escreve à mão, no ficheiro, a classe `Notificacao` e a classe `NotificacaoBreve`, tal como estão no programa completo da secção 3. Não escrevas ainda a classe `NotificacaoDetalhada`.
2. No fim do ficheiro, encostadas à margem, escreve estas linhas:

```python partial
breve = NotificacaoBreve("Contagem concluída")
print(breve.texto)
print(breve.apresentar())
print(isinstance(breve, NotificacaoBreve))
print(isinstance(breve, Notificacao))
```

3. Antes de executar, responde no papel: a classe `NotificacaoBreve` não escreve construtor. Que construtor vai ser executado na primeira linha, e onde está escrito? E que `apresentar` vai ser executado na terceira?
4. Escreve as quatro linhas que esperas ver. Depois executa e compara.

Deves ver `Contagem concluída` duas vezes, seguido de `True` duas vezes. Volta às tuas respostas do passo 3 e confirma-as com a secção 3 do caderno: a classe `NotificacaoBreve` só tem a docstring, e mesmo assim a notificação breve tem texto e sabe apresentar-se. Se alguma resposta estava errada, corrige-a no papel antes de continuares.

## Parte 3: redefinir um método (10 min)

Tem aberta ao lado a secção 4 do caderno.

1. Entre a classe `NotificacaoBreve` e as linhas do programa principal, escreve a classe `NotificacaoDetalhada`, tal como está na secção 3.
2. Substitui as linhas do programa principal por estas:

```python partial
breve = NotificacaoBreve("Contagem concluída")
detalhada = NotificacaoDetalhada("Material em falta")
print(breve.apresentar())
print(detalhada.apresentar())
```

3. Antes de executar, copia para o papel e preenche esta tabela, com a regra da secção 4:

| Chamada | Classe do objeto | Onde o Python encontra `apresentar` | Resultado |
| --- | --- | --- | --- |
| `breve.apresentar()` | A completar | A completar | A completar |
| `detalhada.apresentar()` | A completar | A completar | A completar |

4. Executa e compara com a tabela.
5. Agora, uma experiência. Apaga, na classe `NotificacaoDetalhada`, o método `apresentar` inteiro, as três linhas, e deixa só a docstring da classe. Antes de executar, escreve o que achas que a segunda linha vai mostrar. Executa.

A segunda linha passa a mostrar `Material em falta`, sem o aviso, e não aparece nenhum erro. Responde no papel: de que classe veio o `apresentar` usado agora, e porquê? Porque é que o Python não se queixou? Guarda esta resposta para a parte 6, onde vais reencontrar a mesma situação.

6. Volta a escrever o método `apresentar` da classe `NotificacaoDetalhada` e executa, para confirmares que o aviso voltou.

## Parte 4: acrescentar dados com `super()` (15 min)

Tem aberta ao lado a secção 5 do caderno.

1. A seguir à classe `NotificacaoDetalhada`, escreve a classe `NotificacaoAssinada`, tal como está na secção 5.
2. Substitui as linhas do programa principal por estas:

```python partial
assinada = NotificacaoAssinada("Encomenda recebida", "Secretaria")
print(assinada.origem)
print(assinada.apresentar())
```

3. Prevê as duas linhas e executa. Deves ver `Secretaria` e `Encomenda recebida (enviada por: Secretaria)`.
4. Agora, a experiência do esquecimento. No construtor de `NotificacaoAssinada`, apaga a linha `super().__init__(texto)`. Antes de executar, responde no papel: em que linha do programa achas que vai aparecer o erro, na que cria a notificação ou na que a apresenta? Executa.

O programa mostra `Secretaria` e depois para, com um traceback cuja última linha é:

```text
AttributeError: 'NotificacaoAssinada' object has no attribute 'texto'
```

5. Lê o traceback de baixo para cima e responde:
   - Em que método estava o Python quando o erro aconteceu? Procura, na entrada de baixo, o nome no fim da linha que começa por `File`.
   - A criação da notificação correu bem, e o erro só apareceu na chamada seguinte. Porquê?
   - O traceback aponta para o método `apresentar`, mas o engano está no construtor. Explica esta distância entre o sítio do erro e o sítio da causa, usando a secção 5.

6. Volta a escrever a linha `super().__init__(texto)` e executa, para confirmares que tudo funciona.

## Parte 5: polimorfismo (5 min)

Tem aberta ao lado a secção 6 do caderno.

1. Substitui todas as linhas do programa principal pela lista `avisos` e pelo ciclo `for` do programa completo da secção 6.
2. Antes de executar, copia a tabela da secção 6 para o papel, tapa a coluna "Resultado" e preenche-a tu.
3. Executa e compara.

Repara que a linha dentro do ciclo é sempre a mesma, e que nenhuma linha do teu programa pergunta de que variante é cada notificação. Quem escolhe o `apresentar` certo é o Python, a partir da classe de cada objeto.

## Parte 6: tornar a classe base abstrata (10 min)

Tem aberta ao lado a secção 8 do caderno.

1. No início do ficheiro, antes da classe `Notificacao`, escreve a linha `from abc import ABC, abstractmethod`, seguida de duas linhas em branco.
2. Muda a primeira linha da classe base para `class Notificacao(ABC):`.
3. Substitui o método `apresentar` da classe `Notificacao` pela versão abstrata da secção 8: o decorador `@abstractmethod`, a linha do `def` e a docstring com o contrato, sem nenhuma instrução.
4. Não mudes mais nada. Antes de executar, pensa na experiência da parte 3: que classe derivada ainda não escreveu o seu próprio `apresentar`? Escreve no papel o que achas que vai acontecer. Depois executa.

O programa para logo na criação da lista, com uma última linha parecida com esta (o texto exato muda de uma versão do Python para outra):

```text
TypeError: Can't instantiate abstract class NotificacaoBreve without an implementation for abstract method 'apresentar'
```

Responde no papel: porque é que a `NotificacaoBreve` deixou de poder ser criada, se não lhe mexeste? Que tem isto a ver com a experiência da parte 3? A secção 8 do caderno ajuda-te a responder.

5. Resolve o problema escrevendo, na classe `NotificacaoBreve`, o seu próprio `apresentar`, como está na secção 8. Corrige também a docstring da classe, que dizia "faz tudo como a classe base" e deixou de ser verdade: usa a da secção 8. Executa e confirma que as três notificações voltam a aparecer.
6. Por fim, acrescenta no fim do ficheiro, fora de qualquer `try`, a linha `geral = Notificacao("Olá")`. Executa, lê a última linha do erro e diz por palavras o que ela quer dizer. Depois apaga essa linha.

## Parte 7: duas variantes tuas, sozinho (20 min)

Nesta parte não há código dado. Cada variante é uma classe derivada de `Notificacao`, escrita por ti, com uma docstring, e tem de cumprir o contrato de `apresentar` da secção 7 do caderno: não recebe nada além do `self`, devolve um texto e não altera a notificação.

### 7.1: uma variante sem dados novos

Inventa uma maneira nova de apresentar uma notificação, só a partir do texto. Por exemplo, pôr o texto entre parênteses retos, ou começar por "Lembrete: ". Escolhe tu, desde que seja diferente das variantes do caderno.

1. Escreve a classe. Antes de escreveres, decide e escreve no papel: esta variante precisa de construtor próprio? Porquê?
2. Acrescenta um objeto da tua variante à lista `avisos`. Acrescenta também uma `NotificacaoUrgente`, escrita como no exemplo guiado da secção 9, se ainda não a tiveres.
3. Antes de executar, acrescenta à tua tabela da parte 5 uma linha por cada notificação nova, com o resultado previsto. Depois executa e compara.
4. Acrescenta uma linha que mostre o atributo `texto` da tua notificação depois do ciclo, e confirma que não mudou.

### 7.2: uma variante com um dado novo

Inventa uma variante que precise de guardar mais um dado além do texto. Por exemplo, uma notificação com prazo, que se apresente como "Devolver os marcadores (até sexta-feira)". Escolhe tu o dado e o formato, desde que sejam diferentes da notificação assinada do caderno.

1. Escreve a classe, com um construtor que receba o texto e o dado novo. Lembra-te do que aprendeste na parte 4 sobre a primeira linha desse construtor.
2. Acrescenta um objeto desta variante à lista, prevê o resultado e executa.

## Parte 8: atualizar o diagrama (10 min)

No papel, desenha o diagrama de classes do teu programa final: a classe abstrata `Notificacao`, com o nome em itálico ou com `{abstract}`, e todas as variantes que o teu ficheiro tem, com as linhas de herança e o triângulo. Em cada caixa derivada escreve só o que ela acrescenta ou redefine. Usa o desenho da secção 8 do caderno como modelo.

## Problemas frequentes neste laboratório

| O que aparece | O que costuma ser | Como resolver |
| --- | --- | --- |
| `NameError: name 'Notificacao' is not defined` | Uma classe derivada foi escrita antes da classe base, ou a base tem outro nome | A classe base tem de estar escrita antes das classes que herdam dela |
| `NameError: name 'ABC' is not defined` | Falta a linha `from abc import ABC, abstractmethod`, ou tem um engano | Confirma a linha no início do ficheiro, com as maiúsculas de `ABC` |
| `TypeError: ... missing 1 required positional argument ...` ao criar uma notificação | Foi criada uma variante com menos valores do que o seu construtor pede | Confirma quantos valores o construtor dessa variante recebe, sem contar o `self` |
| `TypeError: Can't instantiate abstract class ...` | Uma variante não escreveu o método `apresentar`, ou escreveu-o com outro nome | Confirma o nome do método, letra a letra, e a indentação dentro da classe |
| Na parte 6 não aparece nenhum erro, e a notificação breve aparece como `None` no ciclo | Falta `(ABC)` na primeira linha da classe base: sem essa herança, o `@abstractmethod` não tem efeito | Confirma que a linha é `class Notificacao(ABC):`, como na secção 8 |
| Aparece `None` numa das linhas do ciclo | O `apresentar` de uma variante usa `print` em vez de `return` | Troca o `print` por `return`: é quem pede o texto que decide mostrá-lo (secção 7) |

## O que fica guardado

Guarda o ficheiro `notificacoes.py`, com a classe abstrata, as variantes do caderno, as tuas duas variantes e o ciclo, e a folha com as previsões, as tabelas, as respostas das partes 4 e 6 e o diagrama da parte 8. Entrega-os pelo meio indicado pelo professor.

![Rodapé](../imagens/rodape.png)

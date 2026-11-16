![Cabeçalho](../../../imagens/cabecalho.png)

# Programas da aula do encapsulamento

São sete programas curtos, mostrados na aula. Começam num artigo que aceita quantidades impossíveis e acabam na propriedade que as recusa. Os programas 6 e 7 mostram dois enganos frequentes nas propriedades. São mais curtos do que os do guia: o artigo tem só um nome e uma quantidade, e cada programa mostra uma ideia só. São usados no tema [03 Encapsulamento e contratos](../../../01-programacao-orientada-objetos/03-encapsulamento-contratos.md).

Nos sete, a regra que se quer garantir é a mesma: a quantidade de um artigo é um número inteiro, 0 ou mais. Os programas usam o que o guia do tema explica e, no programa 4, um `for` sobre uma lista, do 10.º ano.

## O que está nesta pasta

- [`1-o-problema.py`](1-o-problema.py): sem regras, o artigo aceita -3, 2.5 e "muitos". O erro só aparece no último pedido do programa, longe da linha que o causou. No guia: [Nada impede uma quantidade impossível](../../../01-programacao-orientada-objetos/03-encapsulamento-contratos.md#nada-impede-uma-quantidade-impossível).
- [`2-get-e-set.py`](2-get-e-set.py): um set que recusa com um `print`. Quem o chamou não fica a saber da recusa, e nada obriga a usar o set. No guia: [Um set que verifica, mas não obriga](../../../01-programacao-orientada-objetos/03-encapsulamento-contratos.md#um-set-que-verifica-mas-não-obriga).
- [`3-raise.py`](3-raise.py): o atributo com sublinhado e o `raise`. A recusa faz parar o programa, com uma mensagem. No guia: [O sublinhado: um atributo privado por convenção](../../../01-programacao-orientada-objetos/03-encapsulamento-contratos.md#o-sublinhado-um-atributo-privado-por-convenção) e [Recusar a sério, com `raise`](../../../01-programacao-orientada-objetos/03-encapsulamento-contratos.md#recusar-a-sério-com-raise).
- [`4-try-except.py`](4-try-except.py): o `try` e o `except`. Um `for` percorre uma lista de quatro valores, e o programa apanha cada recusa e continua. No guia: [Tratar a recusa com `try` e `except`](../../../01-programacao-orientada-objetos/03-encapsulamento-contratos.md#tratar-a-recusa-com-try-e-except).
- [`5-propriedade.py`](5-propriedade.py): a propriedade a recusar valores, também quando o artigo é criado. No guia: [A propriedade `quantidade`](../../../01-programacao-orientada-objetos/03-encapsulamento-contratos.md#a-propriedade-quantidade) e [O construtor também passa pelo setter](../../../01-programacao-orientada-objetos/03-encapsulamento-contratos.md#o-construtor-também-passa-pelo-setter).
- [`6-recursion-error.py`](6-recursion-error.py): um engano de propósito. O setter guarda o valor em `self.quantidade`, sem o sublinhado. No guia, nos erros frequentes: [`RecursionError: maximum recursion depth exceeded`](../../../01-programacao-orientada-objetos/03-encapsulamento-contratos.md#recursionerror-maximum-recursion-depth-exceeded).
- [`7-construtor-sem-setter.py`](7-construtor-sem-setter.py): o engano contrário, também de propósito. O construtor guarda em `self._quantidade` e salta a regra. No guia: [O construtor também passa pelo setter](../../../01-programacao-orientada-objetos/03-encapsulamento-contratos.md#o-construtor-também-passa-pelo-setter).

## Como correr

Para correres um programa, abre-o na lista de cima e copia o código para um ficheiro com o mesmo nome, numa pasta tua. Depois executa-o no editor das aulas, como nos guias.

Se preferires o terminal, abre-o nessa pasta e escreve `python3` seguido do nome do ficheiro. Por exemplo, para o primeiro:

```bash
python3 1-o-problema.py
```

No Windows, se `python3` não funcionar, experimenta `python` ou `py` no lugar de `python3`.

Antes de executares cada programa, pensa no que ele vai mostrar. Depois de o executares, compara o ecrã e a tua previsão com o que vem a seguir.

O que deves ver: os programas 2, 4, 5 e 7 acabam normalmente. Os programas 1, 3 e 6 acabam com uma mensagem de erro, de propósito. Numa mensagem de erro, lê primeiro a última linha: diz o tipo de erro e o que aconteceu. As linhas de cima dizem onde aconteceu, e a causa pode estar noutra linha, mais acima.

1. `1-o-problema.py` mostra três linhas e depois uma mensagem de erro:

   ```text
   Depois de retirar 9: -3
   Depois de escrever 2.5: 2.5
   Depois de escrever muitos: muitos
   ```

   A última linha da mensagem é `TypeError: unsupported operand type(s) for -: 'str' and 'int'`.

2. `2-get-e-set.py`:

   ```text
   Valor recusado: -3
   O programa continua como se nada fosse.
   Quantidade: 6
   Quantidade: -3
   ```

3. `3-raise.py` mostra `Quantidade: 4` e depois uma mensagem de erro, que acaba em `ValueError: A quantidade não pode ser negativa.`.

4. `4-try-except.py`:

   ```text
   Aceite: 4
   Recusado: -3 -> A quantidade não pode ser negativa.
   Recusado: 2.5 -> A quantidade tem de ser um número inteiro.
   Aceite: 10
   Quantidade no fim: 10
   ```

5. `5-propriedade.py`:

   ```text
   Quantidade: 4
   Recusado: A quantidade não pode ser negativa.
   Quantidade: 4
   A caneta não chegou a ser criada: A quantidade não pode ser negativa.
   ```

6. `6-recursion-error.py` não mostra nenhuma linha antes da mensagem de erro. Na mensagem, a linha `self.quantidade = valor` aparece várias vezes. Depois vem uma linha que começa por `[Previous line repeated` e diz quantas vezes mais se repetiu. A última linha é `RecursionError: maximum recursion depth exceeded`. No Python 3.9, acaba em `RecursionError: maximum recursion depth exceeded in comparison`.

7. `7-construtor-sem-setter.py` mostra uma linha: `A caneta nasceu com: -5`.

## Versões e compatibilidade

As versões usadas são o Python 3.9.6 e o Python 3.14.8. Os programas não precisam de mais nada instalado. Também não usam nada que dependa da versão: serve o Python das aulas. O que mostram é igual nas duas versões, menos nas mensagens de erro. No Python 3.14, por baixo de algumas linhas de código da mensagem, aparecem os sinais `~` e `^`, a apontar a parte da instrução onde o erro aconteceu. No programa 6, o número de repetições muda de uma versão para a outra.

![Rodapé](../../../imagens/rodape.png)

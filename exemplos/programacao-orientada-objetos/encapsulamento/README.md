![Cabeçalho](../../../imagens/cabecalho.png)

# Programas da aula do encapsulamento

Sete programas curtos, mostrados na aula, que vão do artigo que aceita quantidades impossíveis à propriedade que as recusa, com dois enganos frequentes nas propriedades. São mais curtos do que os do guia: o artigo tem só um nome e uma quantidade, e cada programa mostra uma ideia só. São usados no tema [03 Encapsulamento e contratos](../../../01-programacao-orientada-objetos/03-encapsulamento-contratos.md).

A regra é a mesma nos sete: a quantidade de um artigo é um número inteiro, 0 ou mais. Os programas usam o que o guia do tema explica e, no programa 4, um `for` sobre uma lista, do 10.º ano.

## O que está nesta pasta

- `1-o-problema.py`: sem regras, o artigo aceita -3, 2.5 e "muitos". O erro só aparece na última linha, longe da linha que o causou. No guia, "Nada impede uma quantidade impossível".
- `2-get-e-set.py`: um set que recusa com um `print`. Quem o chamou não fica a saber da recusa, e nada obriga a usar o set. No guia, "Primeiro passo: métodos get e set".
- `3-raise.py`: o atributo com sublinhado e o `raise`. A recusa para o programa, com uma mensagem. No guia, "O sublinhado: um atributo privado por convenção" e "Recusar a sério: `ValueError` e `raise`".
- `4-try-except.py`: o `try` e o `except`. Um `for` percorre uma lista de quatro valores, e o programa apanha cada recusa e continua. No guia, "Tratar a recusa: `try` e `except`".
- `5-propriedade.py`: a propriedade a recusar valores, também quando o artigo é criado. No guia, "Propriedades: `@property`" e "O construtor também passa pelo setter".
- `6-recursion-error.py`: um engano de propósito. O setter guarda o valor em `self.quantidade`, sem o sublinhado. No guia, "Propriedades: `@property`".
- `7-construtor-sem-setter.py`: o engano contrário, também de propósito. O construtor guarda em `self._quantidade` e salta a regra. No guia, "O construtor também passa pelo setter".

## Como correr

Abre o terminal nesta pasta e escreve `python3` seguido do nome do programa. Por exemplo, para o primeiro:

```bash
python3 1-o-problema.py
```

No Windows, se `python3` não funcionar, experimenta `python` ou `py` no lugar de `python3`. Também podes abrir o programa no editor de Python das aulas e executá-lo de lá. Antes de executares, escreve o que achas que vai acontecer, e só depois compara.

O que deves ver: os programas 2, 4, 5 e 7 acabam normalmente. Os programas 1, 3 e 6 acabam com uma mensagem de erro, e é isso que devem fazer. Lê primeiro a última linha da mensagem: diz o tipo de erro e o que aconteceu. As linhas de cima dizem onde aconteceu, e a causa pode estar noutra linha, mais acima. Lê o que vem a seguir só depois de escreveres a tua previsão para cada programa.

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

6. `6-recursion-error.py` não mostra nenhuma linha antes da mensagem de erro, que é muito comprida. A última linha é `RecursionError: maximum recursion depth exceeded`. No Python 3.9, acaba em `RecursionError: maximum recursion depth exceeded in comparison`.

7. `7-construtor-sem-setter.py` mostra uma linha: `A caneta nasceu com: -5`.

## Versões com que foram testados

Python 3.9.6 e Python 3.14.8, a 17 de outubro de 2026, a partir de uma pasta vazia. O que os programas mostram é igual nas duas versões, menos nas mensagens de erro. A partir do Python 3.11, aparecem linhas com os sinais `~` e `^` a apontar a parte da instrução onde o erro aconteceu. No programa 6, a última linha da mensagem tem mais umas palavras no Python 3.9, como "Como correr" mostra.

![Rodapé](../../../imagens/rodape.png)

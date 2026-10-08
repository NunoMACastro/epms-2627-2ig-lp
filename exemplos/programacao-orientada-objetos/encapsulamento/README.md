![Cabeçalho](../../../imagens/cabecalho.png)

# Programas da aula do encapsulamento

Estes são os programas mostrados na aula do [caderno 3](../../../01-programacao-orientada-objetos/03-encapsulamento-contratos.md). São mais curtos do que os do caderno: o artigo tem só um nome e uma quantidade, e cada programa mostra uma ideia só. A regra é sempre a mesma: a quantidade de um artigo é um número inteiro, 0 ou mais.

Para executar um programa, abre o terminal nesta pasta e escreve, por exemplo, `python3 1-o-problema.py`. No Windows, se `python3` não funcionar, experimenta `python` ou `py`. Antes de executares, escreve o que achas que vai acontecer, e só depois compara.

| Programa | O que mostra | No caderno |
| --- | --- | --- |
| `1-o-problema.py` | Sem regras, o artigo aceita -3, 2.5 e "muitos". O erro só aparece na última linha, longe da linha que o causou | Secção 1 |
| `2-get-e-set.py` | Um set que recusa com um `print`: quem o chamou não fica a saber da recusa, e nada obriga a usar o set | Secção 5 |
| `3-raise.py` | O atributo com sublinhado e o `raise`: a recusa para o programa, com uma mensagem | Secções 6 e 7 |
| `4-try-except.py` | O `try` e o `except`: o programa apanha a recusa e continua | Secção 8 |
| `5-propriedade.py` | A propriedade a recusar valores, também quando o artigo é criado | Secções 9 e 10 |
| `6-recursion-error.py` | Um engano de propósito: o setter guarda o valor em `self.quantidade`, sem o sublinhado | Secção 9 |
| `7-construtor-sem-setter.py` | O engano contrário: o construtor guarda em `self._quantidade` e salta a regra | Secção 10 |

Os programas 1, 3 e 6 acabam com uma mensagem de erro, e é isso que devem fazer. Lê a última linha da mensagem primeiro: diz o tipo de erro. As linhas de cima dizem onde aconteceu, e a causa pode estar noutra linha, mais acima.

![Rodapé](../../../imagens/rodape.png)

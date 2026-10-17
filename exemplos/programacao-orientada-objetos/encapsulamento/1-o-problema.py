# 1-o-problema.py: um artigo sem regras aceita quantidades impossíveis.
# Exemplo da aula do tema 03. Acaba com uma mensagem de erro, de propósito.

class Artigo:
    """Artigo do inventário, só com nome e quantidade, ainda sem nenhuma regra."""

    def __init__(self, nome, quantidade):
        """Guarda o nome (texto) e a quantidade inicial (número), sem os verificar."""
        self.nome = nome
        self.quantidade = quantidade

    def retirar(self, unidades):
        """Subtrai as unidades (número) à quantidade, sem verificar o pedido. Não devolve nada."""
        self.quantidade = self.quantidade - unidades


caderno = Artigo("Caderno", 6)

caderno.retirar(9)
print("Depois de retirar 9:", caderno.quantidade)

caderno.quantidade = 2.5
print("Depois de escrever 2.5:", caderno.quantidade)

caderno.quantidade = "muitos"
print("Depois de escrever muitos:", caderno.quantidade)

# O erro só aparece aqui, mas a causa está mais acima, na linha que guardou "muitos".
caderno.retirar(1)

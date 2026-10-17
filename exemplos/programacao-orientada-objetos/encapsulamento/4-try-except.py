# 4-try-except.py: o programa apanha cada recusa com try e except, e continua.
# Exemplo da aula do tema 03.

class Artigo:
    """Artigo do inventário; a quantidade fica num atributo interno, _quantidade."""

    def __init__(self, nome, quantidade):
        """Guarda o nome (texto) e a quantidade inicial (número), sem os verificar."""
        self.nome = nome
        self._quantidade = quantidade

    def get_quantidade(self):
        """Devolve a quantidade atual, sem a alterar."""
        return self._quantidade

    def set_quantidade(self, valor):
        """Guarda o valor como quantidade se for um inteiro não negativo.

        Se não for, lança ValueError, e a quantidade fica como estava.
        """
        if not isinstance(valor, int):
            raise ValueError("A quantidade tem de ser um número inteiro.")
        if valor < 0:
            raise ValueError("A quantidade não pode ser negativa.")
        self._quantidade = valor


caderno = Artigo("Caderno", 6)

for valor in [4, -3, 2.5, 10]:
    try:
        caderno.set_quantidade(valor)
        print("Aceite:", valor)
    except ValueError as erro:
        print("Recusado:", valor, "->", erro)

print("Quantidade no fim:", caderno.get_quantidade())

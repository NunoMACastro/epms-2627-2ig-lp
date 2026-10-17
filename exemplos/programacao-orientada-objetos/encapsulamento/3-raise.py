# 3-raise.py: o atributo com sublinhado e um set que recusa a sério, com raise.
# Exemplo da aula do tema 03. Acaba com uma mensagem de erro, de propósito.

class Artigo:
    """Artigo do inventário; a quantidade fica num atributo interno, _quantidade."""

    def __init__(self, nome, quantidade):
        """Guarda o nome (texto) e a quantidade inicial (número), sem os verificar."""
        self.nome = nome
        # O sublinhado avisa: este atributo é só para uso da classe.
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
        # Só chega aqui se o valor passou nas duas verificações.
        self._quantidade = valor


caderno = Artigo("Caderno", 6)

caderno.set_quantidade(4)
print("Quantidade:", caderno.get_quantidade())

caderno.set_quantidade(-3)
print("Esta linha já não corre.")

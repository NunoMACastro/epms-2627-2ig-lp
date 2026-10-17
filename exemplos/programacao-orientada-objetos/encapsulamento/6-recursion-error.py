# 6-recursion-error.py: um setter com um erro de propósito, que se chama a si próprio.
# Exemplo da aula do tema 03. Acaba com um RecursionError, de propósito.

class Artigo:
    """Artigo do inventário, com uma propriedade quantidade mal escrita, de propósito."""

    def __init__(self, nome, quantidade):
        """Guarda o nome (texto) e a quantidade inicial, que passa pelo setter."""
        self.nome = nome
        self.quantidade = quantidade

    @property
    def quantidade(self):
        """Getter: devolve a quantidade atual, sem a alterar."""
        return self._quantidade

    @quantidade.setter
    def quantidade(self, valor):
        """Setter: devia guardar o valor se não for negativo, mas tem um erro de propósito."""
        if valor < 0:
            raise ValueError("A quantidade não pode ser negativa.")
        # ERRO: sem o sublinhado, esta linha chama outra vez o setter.
        self.quantidade = valor


caderno = Artigo("Caderno", 6)

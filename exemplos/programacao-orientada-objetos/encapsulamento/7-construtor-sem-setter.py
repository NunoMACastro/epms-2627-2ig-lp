# 7-construtor-sem-setter.py: um construtor com um erro de propósito, que salta o setter.
# Exemplo da aula do tema 03.

class Artigo:
    """Artigo do inventário, com um construtor mal escrito, de propósito."""

    def __init__(self, nome, quantidade):
        """Guarda o nome (texto) e a quantidade inicial, mas tem um erro de propósito."""
        self.nome = nome
        # ERRO: com o sublinhado, o construtor salta o setter.
        self._quantidade = quantidade

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


caneta = Artigo("Caneta", -5)
print("A caneta nasceu com:", caneta.quantidade)

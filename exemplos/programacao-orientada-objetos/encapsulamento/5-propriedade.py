# 5-propriedade.py: a propriedade quantidade, que recusa valores, também ao criar o artigo.
# Exemplo da aula do tema 03.

class Artigo:
    """Artigo do inventário; a quantidade é uma propriedade que recusa valores inválidos."""

    def __init__(self, nome, quantidade):
        """Guarda o nome (texto) e a quantidade inicial, que passa pelo setter.

        Se a quantidade for inválida, o setter lança ValueError e a criação é interrompida.
        """
        self.nome = nome
        # Sem sublinhado: o construtor também passa pelo setter.
        self.quantidade = quantidade

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


caderno = Artigo("Caderno", 6)
caderno.quantidade = 4
print("Quantidade:", caderno.quantidade)

try:
    caderno.quantidade = -3
except ValueError as erro:
    print("Recusado:", erro)
print("Quantidade:", caderno.quantidade)

try:
    caneta = Artigo("Caneta", -5)
except ValueError as erro:
    print("A caneta não chegou a ser criada:", erro)

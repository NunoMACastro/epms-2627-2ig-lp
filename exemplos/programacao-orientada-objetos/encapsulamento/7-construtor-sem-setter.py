class Artigo:
    def __init__(self, nome, quantidade):
        self.nome = nome
        # ERRO: com o sublinhado, o construtor salta o setter.
        self._quantidade = quantidade

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, valor):
        if not isinstance(valor, int):
            raise ValueError("A quantidade tem de ser um número inteiro.")
        if valor < 0:
            raise ValueError("A quantidade não pode ser negativa.")
        self._quantidade = valor


caneta = Artigo("Caneta", -5)
print("A caneta nasceu com:", caneta.quantidade)

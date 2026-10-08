class Artigo:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, valor):
        if valor < 0:
            raise ValueError("A quantidade não pode ser negativa.")
        # ERRO: sem o sublinhado, esta linha chama outra vez o setter.
        self.quantidade = valor


caderno = Artigo("Caderno", 6)

class Artigo:
    def __init__(self, nome, quantidade):
        self.nome = nome
        # O sublinhado avisa: este atributo é só para uso da classe.
        self._quantidade = quantidade

    def get_quantidade(self):
        return self._quantidade

    def set_quantidade(self, valor):
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

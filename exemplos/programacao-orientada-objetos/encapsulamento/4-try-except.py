class Artigo:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self._quantidade = quantidade

    def get_quantidade(self):
        return self._quantidade

    def set_quantidade(self, valor):
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

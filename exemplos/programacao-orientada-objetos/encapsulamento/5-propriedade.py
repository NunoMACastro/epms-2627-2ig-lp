class Artigo:
    def __init__(self, nome, quantidade):
        self.nome = nome
        # Sem sublinhado: o construtor também passa pelo setter.
        self.quantidade = quantidade

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

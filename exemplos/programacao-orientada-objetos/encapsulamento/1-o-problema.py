class Artigo:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def retirar(self, unidades):
        self.quantidade = self.quantidade - unidades


caderno = Artigo("Caderno", 6)

caderno.retirar(9)
print("Depois de retirar 9:", caderno.quantidade)

caderno.quantidade = 2.5
print("Depois de escrever 2.5:", caderno.quantidade)

caderno.quantidade = "muitos"
print("Depois de escrever muitos:", caderno.quantidade)

# O erro só aparece aqui, mas a causa está na linha de cima.
caderno.retirar(1)

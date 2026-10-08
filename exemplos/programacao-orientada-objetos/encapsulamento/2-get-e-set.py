class Artigo:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def get_quantidade(self):
        return self.quantidade

    def set_quantidade(self, valor):
        # O set verifica antes de guardar.
        if valor < 0:
            print("Valor recusado:", valor)
        else:
            self.quantidade = valor


caderno = Artigo("Caderno", 6)

# Problema 1: o set recusa, mas quem o chamou não fica a saber.
caderno.set_quantidade(-3)
print("O programa continua como se nada fosse.")
print("Quantidade:", caderno.get_quantidade())

# Problema 2: nada obriga a usar o set.
caderno.quantidade = -3
print("Quantidade:", caderno.get_quantidade())

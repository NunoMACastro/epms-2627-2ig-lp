# 2-get-e-set.py: um set que verifica o valor, mas recusa só com um print.
# Exemplo da aula do tema 03.

class Artigo:
    """Artigo do inventário, com um método get e um método set para a quantidade."""

    def __init__(self, nome, quantidade):
        """Guarda o nome (texto) e a quantidade inicial (número), sem os verificar."""
        self.nome = nome
        self.quantidade = quantidade

    def get_quantidade(self):
        """Devolve a quantidade atual, sem a alterar."""
        return self.quantidade

    def set_quantidade(self, valor):
        """Guarda o valor como quantidade se não for negativo; senão, mostra uma mensagem.

        Não devolve nada, nem quando aceita nem quando recusa.
        """
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

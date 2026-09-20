/**
 * M10: programa inicial do trabalho prático. A retirada está por completar.
 * Guarda uma cópia de trabalho e segue as instruções do enunciado.
 * O método retirar devolve sempre falso até o exercício ser completado.
 * Os dados fornecidos são válidos; não alterar construtor, códigos ou nomes.
 * O bloco exterior permite repetir a execução com o estado inicial.
 */
{
  // Esta classe descreve os dados e as operações comuns aos artigos.
  class Artigo {
    #quantidade;

    /**
     * Guarda dados fictícios previamente verificados pelo autor.
     * @param {string} codigo Código não vazio, distinto do outro artigo fornecido.
     * @param {string} nome Designação não vazia.
     * @param {number} quantidade Inteiro não negativo pequeno.
     * Os dois conjuntos de dados usados no trabalho já estão preparados.
     */
    constructor(codigo, nome, quantidade) {
      this.codigo = codigo;
      this.nome = nome;
      this.#quantidade = quantidade;
    }

    /** @returns {number} Quantidade actual, sem modificar o estado. */
    consultarQuantidade() {
      return this.#quantidade;
    }

    /**
     * Acrescenta unidades quando o pedido respeita o contrato.
     * @param {number} unidades Número inteiro positivo; usar valores pequenos.
     * @returns {boolean} Verdadeiro se alterou o estado; falso se rejeitou.
     */
    adicionar(unidades) {
      if (Number.isInteger(unidades) === false) {
        return false;
      }
      if (unidades <= 0) {
        return false;
      }
      this.#quantidade = this.#quantidade + unidades;
      return true;
    }

    /**
     * Parte a completar: decidir se o pedido pode ser aceite e realizar a retirada.
     * @param {number} unidades Quantidade pedida.
     * @returns {boolean} Deverá indicar aceitação ou rejeição do pedido.
     */
    retirar(unidades) {
      // Esta resposta é provisória. Completa a operação seguindo o enunciado.
      return false;
    }
  }

  // Criamos duas fichas diferentes, cada uma com o seu próprio estado.
  const artigoA = new Artigo("A01", "Caderno", 6);
  const artigoB = new Artigo("A02", "Pasta", 2);
  // O inventário reúne as duas fichas e encaminha pedidos para uma delas.
  const inventario = {
    artigos: [artigoA, artigoB],
    /**
     * Encaminha ao primeiro artigo; não decide a validade do pedido.
     * @param {number} unidades Quantidade pedida ao artigo.
     * @returns {boolean} Resultado recebido do artigo.
     */
    retirarDoPrimeiro(unidades) {
      return this.artigos[0].retirar(unidades);
    },
  };

  // Começa por observar esta sequência. Depois compara com o método completado.
  console.log("Inicial:", artigoA.consultarQuantidade(), artigoB.consultarQuantidade());
  console.log("Pedido 2:", inventario.retirarDoPrimeiro(2));
  console.log("Após pedido 2:", artigoA.consultarQuantidade(), artigoB.consultarQuantidade());
  console.log("Pedido 9:", inventario.retirarDoPrimeiro(9));
  console.log("Após pedido 9:", artigoA.consultarQuantidade(), artigoB.consultarQuantidade());
  // Para os ensaios seguintes, substitui estas chamadas como indica a secção 5 do enunciado.
}

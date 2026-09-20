/**
 * M10-B04: o inventário encaminha, o artigo protege a quantidade.
 * Executar num Snippet do browser, com apoio.
 * As quantidades iniciais 6 e 2 são dados válidos fornecidos pelo autor.
 * O construtor prepara cada artigo com um destes valores iniciais.
 */
{
  class Artigo {
    #quantidade;

    /**
     * Prepara uma instância com uma quantidade inicial previamente verificada.
     * @param {number} quantidade Inteiro não negativo pequeno, fornecido no exemplo.
     */
    constructor(quantidade) {
      this.#quantidade = quantidade;
    }

    /** @returns {number} Quantidade actual, sem modificar o estado. */
    consultarQuantidade() {
      return this.#quantidade;
    }

    /**
     * Protege a quantidade: rejeita antes de efectuar a subtracção.
     * @param {number} unidades Número inteiro positivo, até ao stock disponível.
     * @returns {boolean} Verdadeiro se retirou; falso sem alterar o estado.
     */
    retirar(unidades) {
      // Primeiro verificamos; só depois alteramos a quantidade.
      if (Number.isInteger(unidades) === false) {
        return false;
      }
      if (unidades <= 0) {
        return false;
      }
      if (unidades > this.#quantidade) {
        return false;
      }
      this.#quantidade = this.#quantidade - unidades;
      return true;
    }
  }

  const artigoA = new Artigo(6);
  const artigoB = new Artigo(2);
  const inventario = {
    artigos: [artigoA, artigoB],
    /**
     * Encaminha um pedido ao primeiro dos dois artigos fornecidos.
     * @param {number} unidades Quantidade a entregar ao método do artigo.
     * @returns {boolean} Resultado devolvido pelo artigo, sem repetir a validação.
     */
    retirarDoPrimeiro(unidades) {
      return this.artigos[0].retirar(unidades);
    },
  };

  console.log("Aceite:", inventario.retirarDoPrimeiro(2));
  console.log("A01:", artigoA.consultarQuantidade());
  console.log("A02:", artigoB.consultarQuantidade());
  console.log("Rejeitada:", inventario.retirarDoPrimeiro(9));
  console.log("A01 após rejeição:", artigoA.consultarQuantidade());
}

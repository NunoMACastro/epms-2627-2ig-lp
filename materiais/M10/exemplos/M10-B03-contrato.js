/**
 * M10-B03: demonstração guiada de encapsulamento e contrato.
 * Executar integralmente num Snippet do browser.
 * Lê primeiro o caderno 3: aí explicamos cada verificação e o campo privado.
 * Quantidades pequenas e dados fictícios; não há entradas de formulário.
 */
{
  class Artigo {
    #quantidade = 6;

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

  const artigo = new Artigo();
  console.log("Estado:", artigo.consultarQuantidade());
  console.log("Retirar 2:", artigo.retirar(2), artigo.consultarQuantidade());
  console.log("Retirar 9:", artigo.retirar(9), artigo.consultarQuantidade());
  console.log("Adicionar 3:", artigo.adicionar(3), artigo.consultarQuantidade());
}

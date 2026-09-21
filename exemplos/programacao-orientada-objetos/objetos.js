/**
 * Observar dois objectos com estados independentes.
 * Executar integralmente num Snippet do browser, sem Node.
 * Demonstração limitada a retiradas válidas, com números inteiros pequenos.
 * A protecção contra entradas inválidas só é introduzida em B03.
 * Executa o ficheiro inteiro para começar novamente com as quantidades iniciais.
 */
{
  const artigoA = {
    codigo: "A01",
    nome: "Caderno",
    quantidade: 6,
    /**
     * Retira unidades previamente confirmadas como válidas pelo exercício.
     * @param {number} unidades Inteiro positivo que não excede a quantidade.
     * @returns {number} Quantidade restante; este exemplo ainda não valida.
     */
    retirar(unidades) {
      this.quantidade = this.quantidade - unidades;
      return this.quantidade;
    },
  };

  const artigoB = { codigo: "A02", nome: "Pasta", quantidade: 2 };
  // B não precisa de um método próprio para observarmos que o seu estado não muda.
  console.log("Antes:", artigoA.quantidade, artigoB.quantidade);
  const restante = artigoA.retirar(2);
  console.log("Depois:", artigoA.quantidade, artigoB.quantidade);
  console.log("Devolvido:", restante);
}

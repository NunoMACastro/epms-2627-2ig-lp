// inventario.js: o comportamento da página do inventário.
// Guarda a quantidade do caderno A01 e retira unidades quando se carrega no botão.

/**
 * Devolve a quantidade que fica depois de um pedido de retirada.
 * Se o pedido for possível, devolve a quantidade menos as unidades pedidas.
 * Se não for possível, devolve a quantidade que recebeu, sem mudanças.
 * @param {number} quantidade as unidades que existem
 * @param {number} unidades as unidades que se querem retirar
 * @returns {number} a quantidade que fica depois do pedido
 */
function retirar(quantidade, unidades) {
  if (unidades > 0 && unidades <= quantidade) {
    return quantidade - unidades;
  }
  return quantidade;
}

// A quantidade muda a cada pedido aceite, por isso é let e não const.
let quantidadeCaderno = 6;

const campoUnidades = document.querySelector("#unidades");
const botaoRetirar = document.querySelector("#botao-retirar");
const saida = document.querySelector("#resultado");

/**
 * Mostra na saída da página a quantidade atual do caderno.
 * Não devolve nada: muda o texto do elemento de saída.
 */
function mostrarQuantidade() {
  saida.textContent = "Unidades do caderno A01: " + quantidadeCaderno + ".";
}

/**
 * Trata o clique no botão Retirar: lê o campo, faz o pedido e mostra o resultado.
 * Não devolve nada: muda a quantidade do caderno e o texto da saída.
 */
function aoCarregarEmRetirar() {
  // O campo dá sempre texto, como "2", e a retirar espera um número: o Number converte-o no número 2.
  const unidades = Number(campoUnidades.value);
  quantidadeCaderno = retirar(quantidadeCaderno, unidades);
  mostrarQuantidade();
}

// Sem parênteses: o browser chama a função em cada clique, e não agora.
botaoRetirar.addEventListener("click", aoCarregarEmRetirar);

// A saída começa vazia no HTML; esta chamada mostra a quantidade inicial.
mostrarQuantidade();

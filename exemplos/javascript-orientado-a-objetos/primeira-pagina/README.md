![Cabeçalho](../../../imagens/cabecalho.png)

# A primeira página do inventário

É a página do inventário no fim do [laboratório do tema 01](../../../02-javascript-orientado-a-objetos/laboratorios/01-primeira-pagina-com-javascript-laboratorio.md), com o caderno A01: um campo, o botão "Retirar" e a saída com as unidades que ficam. É o ponto de partida do [laboratório do tema 02, Do objeto literal à classe](../../../02-javascript-orientado-a-objetos/laboratorios/02-do-objeto-literal-a-classe-laboratorio.md), para quem não tem a sua pasta `primeira-pagina`.

## O que está nesta pasta

- [`index.html`](index.html): a estrutura da página, com o rótulo, o campo, o botão e a saída. Carrega a folha de estilos e o script.
- [`estilos.css`](estilos.css): a apresentação da página, com as cores escolhidas pelo contraste e o contorno do foco.
- [`inventario.js`](inventario.js): o comportamento da página, com a função `retirar` e o clique no botão.

## Como correr

Para teres a página no teu computador, cria uma pasta e, dentro dela, os três ficheiros, com os mesmos nomes. Cria-os no VS Code, que mostra o nome completo de cada ficheiro. Depois abre cada ficheiro da lista de cima, aqui no GitHub. Carrega no botão `Copy raw file` (copiar o ficheiro), por cima do código, à direita, e cola o conteúdo no ficheiro com o mesmo nome. Guarda os três.

A página abre-se com duplo clique no `index.html`, na janela de ficheiros do computador, sem servidor nem instalações.

O que deves ver: o título Inventário da sala, o campo com o rótulo "Unidades a retirar", o botão azul-escuro "Retirar" e, por baixo, `Unidades do caderno A01: 6.`. Com `2` no campo, um clique no botão deixa `Unidades do caderno A01: 4.`, e a consola do browser não mostra erros.

## Versões e compatibilidade

Corre num browser atual, como o Chrome, o Edge ou o Firefox, aberto como ficheiro local. O script é um script normal, com `defer`, e não precisa de servidor.

![Rodapé](../../../imagens/rodape.png)

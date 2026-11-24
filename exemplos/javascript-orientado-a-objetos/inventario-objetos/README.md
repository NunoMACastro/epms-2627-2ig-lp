![Cabeçalho](../../../imagens/cabecalho.png)

# O inventário com objetos

É a página do inventário no fim do [laboratório do tema 02](../../../02-javascript-orientado-a-objetos/laboratorios/02-do-objeto-literal-a-classe-laboratorio.md): a classe `Artigo`, o caderno A01 e a pasta A02, e um botão para cada um. É o ponto de partida do [laboratório do tema 03, Interface pública e campos privados](../../../02-javascript-orientado-a-objetos/laboratorios/03-interface-publica-e-campos-privados-laboratorio.md), para quem não tem a sua pasta `inventario-objetos`.

## O que está nesta pasta

- [`index.html`](index.html): a estrutura da página, com o campo, os dois botões e uma saída para cada artigo.
- [`estilos.css`](estilos.css): a apresentação da página, a mesma do tema 01.
- [`inventario.js`](inventario.js): a classe `Artigo`, com o `constructor`, o `retirar` e o `descrever`, os dois artigos e as funções dos cliques.

## Como correr

Para teres a página no teu computador, cria uma pasta e, dentro dela, os três ficheiros, com os mesmos nomes. Cria-os no VS Code, que mostra o nome completo de cada ficheiro. Depois abre cada ficheiro da lista de cima, aqui no GitHub. Carrega no botão `Copy raw file` (copiar o ficheiro), por cima do código, à direita, e cola o conteúdo no ficheiro com o mesmo nome. Guarda os três.

A página abre-se com duplo clique no `index.html`, na janela de ficheiros do computador, sem servidor nem instalações.

O que deves ver: o título Inventário da sala, o campo com o rótulo "Unidades a retirar" e os botões "Retirar do caderno" e "Retirar da pasta". Por baixo, aparecem `A01 Caderno, quantidade: 6` e `A02 Pasta, quantidade: 2`. Com `2` no campo, um clique em "Retirar do caderno" deixa o caderno com 4 e a pasta com 2, e a consola do browser não mostra erros.

## Versões e compatibilidade

Corre num browser atual, como o Chrome, o Edge ou o Firefox, aberto como ficheiro local. O script é um script normal, com `defer`, e não precisa de servidor.

![Rodapé](../../../imagens/rodape.png)

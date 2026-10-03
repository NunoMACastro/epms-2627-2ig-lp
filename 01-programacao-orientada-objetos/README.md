![Cabeçalho](../imagens/cabecalho.png)

# Aprender a pensar com objetos

**M10: Introdução à Programação Orientada por Objetos**

Como pode um programa representar os materiais de uma sala? Que dados precisa de guardar? Como se alteram esses dados sem perder informação ou criar quantidades impossíveis?

Vamos construir as respostas ao longo de seis cadernos. Começamos por situações em papel e só depois observamos como algumas delas se escrevem em Python. Não precisas de dominar Python para começares a estudar os conceitos.

## Os cadernos

Cada tema tem até três documentos: o caderno, para ler e estudar, com as explicações e os exemplos resolvidos; o laboratório, para seguir passo a passo no computador, com o editor de Python aberto ao lado; e a ficha de exercícios, para praticares sozinho depois de estudares o caderno.

1. [Dos materiais da sala aos dados de um programa](01-entidades-estado-acoes.md): escolher o que representar e distinguir informação de operação. [Laboratório](01-entidades-estado-acoes-laboratorio.md) e [ficha de exercícios](01-entidades-estado-acoes-exercicios.md).
2. [Objetos e classes: uma descrição comum, vários artigos](02-objetos-classes-instancias.md): perceber objeto, atributo, método, classe e instância. [Laboratório](02-objetos-classes-instancias-laboratorio.md) e [ficha de exercícios](02-objetos-classes-instancias-exercicios.md).
3. [Proteger a quantidade de um artigo](03-encapsulamento-contratos.md): compreender regras, encapsulamento e contratos. [Laboratório](03-encapsulamento-contratos-laboratorio.md) e [ficha de exercícios](03-encapsulamento-contratos-exercicios.md).
4. [Reunir artigos num inventário](04-composicao-modelacao.md): relações entre objetos, composição e agregação, esquemas de classes em UML leve e a classe do inventário. [Laboratório](04-composicao-modelacao-laboratorio.md) e [ficha de exercícios](04-composicao-modelacao-exercicios.md).
5. [A mesma operação, maneiras diferentes de a realizar](05-heranca-polimorfismo.md): estudar herança, polimorfismo e abstração através de notificações. [Laboratório](05-heranca-polimorfismo-laboratorio.md) e [ficha de exercícios](05-heranca-polimorfismo-exercicios.md).
6. [Juntar as ideias num pequeno inventário](06-sintese.md): compreender e completar um programa com apoio.

Antes dos primeiros conceitos, o professor propõe o [diagnóstico](../avaliacoes/diagnostico-inicial.md) e escolhe contigo as [atividades de apoio](bridge-raciocinio.md) de que precisas. No fim, realizarás o [trabalho de síntese](../avaliacoes/mini-problema.md).

## Como usar um caderno

Lê a situação inicial e acompanha o exemplo resolvido. Quando aparecer uma tabela com valores antes e depois, segue os passos pela ordem apresentada. Só depois tenta o exercício correspondente.

Nos exercícios, escreve a tua previsão antes de executar código. Se a observação for diferente, tenta explicar a diferença em vez de mudar números ao acaso. Podes voltar às explicações e pedir uma pista ao professor.

Os diagramas e o pseudocódigo servem para pensar sobre o programa; não são comandos para executar. Os trechos apresentados como excertos dependem de outras partes do ficheiro. Quando for para executar um exemplo completo, o caderno indica qual é o ficheiro.

## Onde estão os programas?

- Cadernos 1 a 5: os programas estão completos dentro de cada caderno, em Python. Os laboratórios dizem, passo a passo, como os usar no computador.
- O caderno 6 e o trabalho de síntese ainda estão na versão antiga, em JavaScript, e passam a Python antes de lá chegarmos. O [programa inicial do trabalho de síntese](../avaliacoes/inventario-inicial.js) tem uma operação por completar.
- O ficheiro [composicao.js](../exemplos/programacao-orientada-objetos/composicao.js) pertencia à versão antiga do caderno 4, em JavaScript. O caderno 4 já não o usa.

## Executar um programa em Python

Os programas dos cadernos 1 a 5 executam-se no editor de Python que usas nas aulas. Copia o programa completo para um ficheiro novo com a extensão `.py`, guarda-o e executa o ficheiro inteiro. Cada execução começa do zero, com os valores iniciais escritos no programa. Os programas destes cadernos funcionam com Python 3, a partir da versão 3.10.

Se aparecer uma mensagem de erro, lê primeiro a última linha: diz o tipo de erro e a razão. As linhas de cima dizem onde aconteceu. O caderno 3 explica como ler estas mensagens.

## Executar um programa JavaScript (caderno 6 e trabalho de síntese)

Esta secção serve enquanto o caderno 6 e o trabalho de síntese estiverem na versão antiga, em JavaScript. O professor vai acompanhar esta preparação. Usaremos as ferramentas do browser para executar JavaScript e ver as mensagens na **consola**, uma área onde o programa pode apresentar resultados.

1. Abre um separador vazio, escrevendo `about:blank` na barra de endereços.
2. Em Chrome ou Edge, abre o menu “Mais ferramentas” → “Ferramentas de programação”. Em macOS também podes usar Option+Cmd+I; em Windows/Linux, Ctrl+Shift+I.
3. Abre “Sources” (Fontes) e procura “Snippets” (Fragmentos) no painel lateral. Um fragmento é uma área onde podes guardar e executar um pequeno conjunto de instruções. Cria um novo fragmento com o nome do exercício.
4. Coloca nesse fragmento o conteúdo completo do ficheiro indicado no caderno. O professor pode preparar este passo contigo. Se o browser bloquear a colagem, pede ajuda em vez de desativar a proteção.
5. Usa o botão de execução do fragmento e consulta as mensagens na área “Console” (Consola). Compara-as com as previsões que escreveste.
6. Para começar de novo, executa outra vez o ficheiro completo. Isso volta a criar os artigos com os valores iniciais. Para experimentar alterações, usa a tua cópia de trabalho e conserva o exemplo original de estudo.

Os menus podem ter nomes diferentes no computador da escola. Se não conseguires abrir o ambiente, avisa o professor. Podes começar pelo traço em papel enquanto preparas a execução.

Usa apenas os dados fictícios dos exercícios. As respostas e os ficheiros de trabalho são entregues pelo meio indicado pelo professor.

![Rodapé](../imagens/rodape.png)

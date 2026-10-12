![Cabeçalho](../imagens/cabecalho.png)

# O teu projeto

*M10, M11, M12 e M13 · Projeto*

Este ano vais construir uma aplicação tua. Começas a pensá-la no fim do M10, escreves a primeira versão no M11, organizas e completas a aplicação no M12 e, no M13, voltas a fazer a interface com React. A aplicação vai crescendo com a matéria: cada módulo ensina-te uma coisa de que ela precisa, e no fim de cada etapa a aplicação faz mais do que fazia antes.

Esta página explica tudo o que precisas de saber sobre o projeto: os temas por onde podes escolher, o que a aplicação tem de ter, o que fazes em cada etapa, como vais ser avaliado e o que fica de fora. Volta a ela sempre que tiveres uma dúvida sobre o que é pedido.

## Um projeto que atravessa três módulos

Os três primeiros módulos do ano ensinam partes diferentes da mesma maneira de programar. O M10 ensina os conceitos da programação orientada a objetos: classes, objetos, estado, encapsulamento e composição. O M11 leva esses conceitos para o JavaScript e para o browser, com páginas, formulários e eventos. O M12 ensina a organizar um programa em módulos, a tratar erros, a guardar os dados e a testar as regras.

Cada um destes módulos, sozinho, daria um projeto pequeno e pouco interessante: só conceitos no papel, ou só uma página que esquece tudo quando a fechas. Juntos, dão uma aplicação completa, que guarda dados com regras, funciona no browser e se lembra do que lá puseste. Por isso o M10, o M11 e o M12 têm **uma avaliação conjunta**: o teu projeto, avaliado no fim do M12, é a avaliação prática dos três módulos, a de cada módulo com os critérios desse módulo.

Trabalhas no projeto ao longo dos três módulos; a avaliação é que olha para a aplicação já completa, quando já aprendeste tudo aquilo de que ela precisa. Pelo caminho há um momento para mostrares ao professor como vai o trabalho, no fim do M11, que não tem nota e serve para corrigires o rumo a tempo.

O M13 tem a sua própria avaliação: a versão React do mesmo projeto, com a sua defesa.

## O inventário das aulas serve de exemplo

Nas aulas, os cadernos, os laboratórios e as fichas usam sempre o mesmo exemplo: um inventário de materiais, em que cada artigo tem um código que não se repete, um nome e uma quantidade que nunca pode ser negativa. Em cada etapa vais ver, feito com o inventário, aquilo que tens de fazer no teu projeto.

O inventário não é um dos temas do projeto. Serve para veres o caminho feito num caso concreto. Depois, fazes o mesmo caminho na tua aplicação, com o teu tema, e tens de tomar decisões que o exemplo não tomou por ti: que regra tem o teu número, que mensagem aparece quando um valor é recusado, que filtro faz sentido no teu tema.

## Os seis temas

Escolhes o tema do teu projeto de uma lista de seis, preparada pelo professor. Os seis temas parecem muito diferentes, mas por baixo têm todos a mesma estrutura, igual à do inventário: uma lista de registos, em que cada registo tem um **identificador** que não se pode repetir, um **texto obrigatório** e um **número** com uma regra de validade. Como a estrutura é a mesma, a matéria das aulas serve para qualquer tema, e o trabalho pedido é igual para todos.

| Tema | Cada registo é | Identificador, que não se repete | Texto obrigatório | Número e a sua regra |
| --- | --- | --- | --- | --- |
| Coleção de jogos | um jogo | o código do jogo, por exemplo J01 | o título do jogo | horas jogadas: número inteiro, 0 ou mais |
| Cartas colecionáveis | uma carta | o código da carta, por exemplo C001 | o nome da carta | raridade: número inteiro de 1 a 5 |
| Diário de treinos | um treino | o código do treino, por exemplo T01 | a atividade, por exemplo "Corrida" | duração em minutos: número inteiro maior do que 0 |
| Playlist | uma música | o código da música, por exemplo M01 | o título da música | duração em segundos: número inteiro maior do que 0 |
| Campeonato | uma equipa | a sigla da equipa, por exemplo LBO | o nome da equipa | pontos: número inteiro, 0 ou mais |
| Livro de receitas | uma receita | o código da receita, por exemplo R01 | o nome da receita | tempo de preparação em minutos: número inteiro maior do que 0 |

Em todos os temas o número é inteiro. Um valor com casas decimais, como 2,5, é recusado, tal como um campo vazio ou um valor fora da regra. Repara também que as regras não são todas iguais: umas aceitam o 0 e outras não, e uma delas tem um limite máximo. Saber exatamente onde fica o limite da tua regra é uma das coisas que vais ter de mostrar.

Podes acrescentar outros campos de texto, como a plataforma de um jogo, o artista de uma música ou o tipo de treino, desde que os três campos da tabela estejam lá. Um campo a mais não melhora a nota e é mais uma coisa que tens de saber explicar.

### Coleção de jogos

Registas os jogos que tens ou que jogaste e quantas horas jogaste cada um. Um jogo com 0 horas é válido: acabaste de o instalar e ainda não o abriste. Um jogo com -3 horas não é. Alterar um registo é, por exemplo, somar as horas de uma nova sessão de jogo ou corrigir o total, que continua a ter de ser 0 ou mais. Um filtro possível é mostrar só os jogos com mais de 10 horas.

### Cartas colecionáveis

Registas as cartas de uma coleção, cada uma com uma raridade de 1, a mais comum, a 5, a mais rara. Este é o único tema com dois limites: o 1 e o 5 são válidos, o 0 e o 6 não são. Alterar um registo é corrigir a raridade de uma carta, e a raridade nova tem de cumprir a mesma regra. Um filtro possível é mostrar só as cartas de raridade 4 ou mais.

### Diário de treinos

Registas os treinos que fizeste e quanto tempo durou cada um. Aqui o 0 não é válido: um treino de 0 minutos não aconteceu. O valor mais pequeno aceite é 1. Alterar um registo é corrigir a duração de um treino. Um filtro possível é mostrar só os treinos de uma atividade, ou só os que duraram mais de 30 minutos.

### Playlist

Registas as músicas de uma lista e a duração de cada uma, em segundos: uma música de 3 minutos e 20 segundos tem 200 segundos. Guardar a duração em segundos, como número inteiro, evita teres de tratar minutos e segundos em separado. Uma duração de 0 segundos não é válida. Alterar um registo é corrigir a duração de uma música. Um filtro possível é mostrar só as músicas com mais de 4 minutos, ou seja, mais de 240 segundos.

### Campeonato

Registas as equipas de um campeonato inventado por ti e os pontos de cada uma. Uma equipa acabada de inscrever tem 0 pontos, e isso é válido. Alterar um registo é somar os pontos ganhos num jogo ou corrigir o total, que nunca pode ficar negativo. Um filtro possível é mostrar só as equipas com pelo menos um certo número de pontos.

### Livro de receitas

Registas receitas e o tempo de preparação de cada uma, em minutos. Uma receita que se prepara em 0 minutos não existe, por isso o valor mais pequeno aceite é 1. Alterar um registo é corrigir o tempo de uma receita. Um filtro possível é mostrar só as receitas que se fazem em 30 minutos ou menos.

Vários colegas podem escolher o mesmo tema. Cada um faz a sua aplicação, e a avaliação é individual. Podem trocar ideias, como se faz em qualquer trabalho, mas o código que entregas tem de ser teu, porque na avaliação vais ter de o explicar e de o alterar sozinho.

## Propor uma ideia tua

Se tiveres uma ideia para um tema que não está na lista, podes propô-la ao professor. A ideia é aceite se couber na mesma estrutura dos seis temas e se o professor a aprovar. Caber na mesma estrutura quer dizer quatro coisas:

1. A aplicação guarda um só tipo principal de registo, como os jogos, as cartas ou as receitas.
2. Cada registo tem um identificador que não se pode repetir, um texto obrigatório e um número inteiro com uma regra de validade clara.
3. As operações pedidas fazem sentido no teu tema: criar um registo, ver a lista, alterar o número de um registo, filtrar a lista e gravar os dados.
4. A ideia respeita os limites do projeto, explicados no fim desta página: nada de dinheiro, preços, contas de utilizador ou dados pessoais de pessoas reais.

A proposta escreve-se numa página e diz: o nome do tema; o que é cada registo; qual é o identificador, o texto obrigatório e o número, com a regra escrita por palavras; dois registos de exemplo que cumprem a regra e um que não cumpre, com a razão; o que quer dizer alterar um registo no teu tema; e um exemplo de filtro. Entrega-a ao professor até à altura em que se escolhe o tema, no fim do M10.

O professor pode aprovar a ideia, pedir-te que a acertes ou não a aprovar. Se não for aprovada, escolhes um dos seis temas da lista. O inventário não pode ser proposto como ideia tua, porque é o exemplo das aulas.

Alguns exemplos ajudam a perceber o que não cabe. Uma lista de compras com preços não cabe, porque mexe com dinheiro. Uma rede social não cabe, porque precisa de contas de utilizador e de um servidor. Uma lista com os contactos ou as notas dos colegas não cabe, porque guarda dados pessoais de pessoas reais. Já uma coleção de livros lidos, com o número de páginas, ou um registo de plantas, com os dias entre regas, cabem na estrutura e podem ser propostos.

## O que a aplicação tem de ter

Esta secção descreve a aplicação completa. Não tens de fazer tudo de uma vez: a secção seguinte, sobre as etapas, diz o que fazes em cada módulo.

### Os dados

A aplicação funciona no teu computador, para uma só pessoa, sem internet. Guarda registos do tipo que escolheste, e cada registo tem o identificador, o texto obrigatório e o número com a regra do teu tema.

Os dados servem só para experimentar a aplicação. Podes inventá-los ou usar nomes que toda a gente conhece, como o título de um jogo ou de uma música, mas nunca dados pessoais de pessoas reais, como nomes, moradas, contactos ou notas de colegas.

### As operações

A aplicação tem de deixar fazer cinco coisas:

1. **Criar** um registo novo, num formulário.
2. **Listar** os registos que existem. Quando não há nenhum, aparece uma mensagem a dizê-lo, em vez de uma lista vazia sem explicação.
3. **Alterar** o número de um registo que já existe, somando ou substituindo, conforme faça sentido no teu tema. Depois da alteração, a regra continua a valer.
4. **Filtrar** a lista, para ver só os registos que cumprem uma condição. Filtrar muda só o que se vê: não apaga nem altera nenhum registo.
5. **Gravar** os dados, para que, ao fechar e voltar a abrir a aplicação, os registos continuem lá.

Não é pedido apagar registos.

### As recusas

Uma aplicação com regras tem de saber dizer que não. A tua aplicação recusa:

- um identificador que já existe;
- um texto obrigatório vazio;
- um número que não cumpre a regra do teu tema, que tem casas decimais ou que ficou por preencher.

Uma recusa tem duas partes, e as duas contam. A primeira é a mensagem: o utilizador tem de perceber o que está mal, sem ter de adivinhar. A segunda é o estado: quando um pedido é recusado, os dados ficam exatamente como estavam antes. Uma aplicação que mostra a mensagem certa mas já alterou o registo não está a proteger os dados; foi isso que estudaste no caderno 3, com a quantidade de um artigo.

### A organização do código

O código da aplicação usa a matéria dos três módulos. Do M10 vêm as classes, que no projeto vais escrever em JavaScript a partir do M11: uma classe para o registo, que protege a regra do número, e uma classe para a coleção de registos, que reúne os registos e garante que não há identificadores repetidos. É a mesma divisão de trabalho que viste no inventário, entre o artigo e o inventário. Não precisas de herança: só a uses se houver mesmo uma relação "é um" no teu tema, e num tema destes normalmente não há.

Do M11 vem a interface no browser: a página, o formulário, a lista, os eventos que respondem aos cliques e às submissões, e a ligação entre a interface e as classes. Do M12 vem a organização em módulos, com o domínio (as classes e as regras), a interface e a gravação em ficheiros separados, a gravação em formato JSON, a validação dos dados que se leem e os testes das regras.

### Os cenários mínimos

Os cenários são situações concretas que a aplicação tem de tratar bem. Servem para experimentares a tua aplicação antes de a entregares, e são os primeiros que vais mostrar na avaliação. Entre parênteses está o caso do inventário das aulas.

1. Ao arrancar sem dados, a aplicação mostra a lista vazia com uma mensagem.
2. Criar um registo com o número exatamente no limite da regra é aceite (quantidade 0); criar um registo com um identificador repetido ou com o texto obrigatório vazio é recusado.
3. Um número que não cumpre a regra, que tem casas decimais ou que ficou vazio é recusado e não altera nada (quantidade negativa, decimal ou vazia).
4. Alterar um registo atualiza o que se vê no ecrã (ajustar a quantidade); filtrar mostra só parte da lista e não modifica os registos guardados.
5. Gravar, fechar e voltar a abrir recupera os dados; dados estragados no armazenamento não são aceites em silêncio.
6. Sabes explicar o caminho de um dado: da entrada no formulário à regra, da regra ao estado dos objetos, do estado ao ecrã e do ecrã à gravação. E sabes encontrar e corrigir uma falha pequena.

## As etapas

O projeto faz-se por etapas, uma por módulo. Cada etapa usa a matéria desse módulo e aproveita o que ficou feito na anterior, por isso convém não deixar uma etapa por acabar quando começa a seguinte.

### No fim do M10: o tema e o modelo

No fim do M10 escolhes o tema, da lista ou com uma ideia tua aprovada, e fazes o modelo das entidades da tua aplicação. Ainda não programas a aplicação: pensas nela, como os cadernos do M10 te ensinaram a fazer antes de escrever código.

O modelo tem:

- o esquema das classes em UML leve, como os do [caderno 4](../01-programacao-orientada-objetos/04-composicao-modelacao.md): a classe do registo e a classe da coleção, com os atributos e as operações de cada uma, e a ligação entre as duas;
- a regra do número, escrita por palavras, com o limite bem claro;
- dois registos de exemplo que cumprem as regras;
- uma alteração válida e outra inválida, cada uma com o que acontece aos dados: na válida, o valor antes e depois; na inválida, a razão da recusa e a prova de que os dados ficaram iguais.

Entregas o tema e o modelo ao professor pelo meio que ele indicar, para ele ver se as regras estão claras antes de começares a programar no M11.

### No M11: a primeira versão no browser

No M11 aprendes JavaScript, classes em JavaScript e a construir páginas que respondem ao utilizador. À medida que a matéria avança, escreves a primeira versão da tua aplicação no browser:

- as classes do teu modelo em JavaScript, com a regra do número protegida dentro da classe do registo e a recusa de identificadores repetidos na classe da coleção;
- uma página com um formulário para criar registos, a lista dos registos e uma maneira de alterar o número de um registo;
- mensagens claras para cada recusa, com os dados intactos depois dela.

Nesta versão ainda não há gravação: ao recarregar a página, os dados perdem-se, e isso está certo nesta etapa.

No fim do M11 há um **marco de acompanhamento**: mostras ao professor a tua aplicação a funcionar e explicas, em poucos minutos, como um registo novo vai do formulário até à lista. O professor diz-te o que está bem e o que tens de corrigir antes do M12. O marco não tem nota. Serve para o projeto não derrapar, e um problema descoberto aqui resolve-se com muito menos trabalho do que no fim do M12.

### No M12: a versão modular, com gravação e testes

No M12 aprendes a organizar um programa em módulos, a validar dados e a tratar erros, a guardar dados em JSON e a escrever testes. A tua aplicação ganha tudo isso:

- o código dividido em módulos, com o domínio, a interface e a gravação em ficheiros separados, ligados por importações;
- o filtro da lista;
- a gravação dos dados no browser, em formato JSON, e a leitura desses dados quando a aplicação arranca, com validação: se os dados guardados estiverem estragados, a aplicação não os aceita em silêncio e diz o que se passou;
- testes automáticos das regras, que confirmam pelo menos o valor no limite, o identificador repetido, o texto vazio e o número inválido;
- um ficheiro README que explica como pôr a aplicação a funcionar, que cenários testaste e que limites conhecidos a aplicação tem.

No fim do M12 entregas o projeto e defende-lo na avaliação descrita a seguir. O exercício de ficheiros em Node.js, que também se faz no M12, é separado e não faz parte do projeto.

### No M13: a versão React

No M13 aprendes React, uma forma de construir interfaces com componentes. Voltas a fazer a interface da tua aplicação com componentes funcionais, aproveitando as regras e os dados do M12:

- um formulário controlado para criar registos, com as mesmas recusas e mensagens;
- a lista, a alteração e o filtro;
- um botão Guardar, com uma mensagem de sucesso ou de erro, e a leitura validada dos dados quando a aplicação arranca;
- a aplicação preparada para entrega com o comando de build, que vais aprender no M13, e o README atualizado, com uma frase sobre o que faz cada componente.

No fim do M13 apresentas e defendes a versão React.

## Como vais ser avaliado

### A avaliação do fim do M12

A avaliação do projeto faz-se no fim do M12 e é individual. Tem três partes:

1. **Demonstração.** Pões a aplicação a funcionar e mostras os cenários mínimos, a começar pelos casos de recusa.
2. **Explicação.** Explicas o teu código e as tuas decisões. O professor pode perguntar, por exemplo, onde é que a regra do número é verificada, o que acontece aos dados quando um pedido é recusado, porque é que é a coleção, e não a interface, que impede um identificador repetido, ou como um registo novo chega à gravação.
3. **Uma pequena alteração feita na hora.** O professor pede-te uma alteração pequena à tua aplicação, e tu fazes essa alteração sozinho, ali mesmo. A alteração usa só matéria dada nas aulas e é rápida para quem conhece o seu próprio código. O professor pode também pedir-te que encontres e corrijas uma pequena falha. Nenhuma destas tarefas é divulgada antes, porque servem precisamente para mostrar que sabes mexer no código que entregaste.

Esta avaliação dá a parte prática da nota do M10, do M11 e do M12, cada uma com os critérios do seu módulo:

| Módulo | O que se observa |
| --- | --- |
| M10 | Classes, objetos e estado: o que é a classe do registo e o que é cada objeto. Encapsulamento: a regra protegida dentro da classe, com os dados intactos depois de uma recusa. Composição e responsabilidades: a coleção que reúne os registos e decide o que é da coleção, e o registo que decide o que é seu. |
| M11 | A interface no browser e o DOM: a página mostra o estado dos objetos e muda quando ele muda. Os eventos e os formulários: a aplicação responde às ações do utilizador e trata as entradas. A ligação entre o domínio e a interface: a interface usa as classes sem mexer diretamente nos dados delas. |
| M12 | Os módulos: o código dividido com responsabilidades claras. A validação e os erros: entradas e dados lidos verificados, com mensagens úteis. O JSON e a persistência: gravar e voltar a ler sem perder nem aceitar dados estragados. Os testes: as regras confirmadas por testes que correm. |

A explicação e a alteração feita na hora contam para os três módulos. Uma aplicação que funciona, mas que não sabes explicar nem alterar, não mostra que aprendeste o que cada módulo pede. Uma explicação clara de uma parte que ficou incompleta também mostra o que percebeste.

A nota de cada módulo junta quatro critérios: atitudes e valores, 30% (assiduidade e pontualidade, comportamento, respeito, cumprimento das regras, ser bom colega); autonomia, 10%; empenho, 20%; e avaliação prática, 40%, que é este projeto. A autonomia e o empenho observam-se ao longo dos módulos, também no trabalho que fazes no projeto. Também não contam a teu favor, por si sós, coisas que parecem trabalho a mais: muitas classes, uma aparência elaborada, bibliotecas extra ou matéria que ainda não foi dada. Conta o que a aplicação faz bem e o que tu sabes explicar sobre ela.

### A avaliação do M13

A versão React tem a sua própria avaliação, no fim do M13, com a mesma forma: demonstras a aplicação, explicas que componente guarda o estado e que informação passa de um componente para outro, e fazes sozinho uma alteração simples pedida na hora. Esta avaliação é a parte prática da nota do M13.

## Os limites do projeto

O projeto tem limites, qualquer que seja o tema. Não inclui:

- compras, faturação, preços ou qualquer conta com dinheiro;
- contas de utilizador, palavras-passe ou permissões;
- servidores, bases de dados, ligação a serviços na internet ou envio de ficheiros para outro computador;
- sincronização dos dados entre computadores;
- publicação da aplicação online;
- dados pessoais de pessoas reais.

Cada uma destas coisas traz problemas que a matéria deste ano ainda não ensina a resolver, e que ficariam mal resolvidos se entrassem agora. Alguns, como os servidores e as bases de dados, ficam para depois do 11.º ano. Dentro destes limites há muito para fazer bem, e é isso que a avaliação procura.

A aplicação também não pretende resolver um problema real de uma empresa. É uma aplicação pequena, com um tema de que gostes, feita para aprenderes a programar com objetos, no browser, com dados guardados e regras testadas.

![Rodapé](../imagens/rodape.png)

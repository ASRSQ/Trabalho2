<h1>Sistema Cadastros</h1>
<p>Auno: Alex de Sousa Ramos</p>
<p>Disciplina: Técnicas de Programação</p>
<p>Professor: Wendley S. Silva</p>
<p>Matricula: 428359</p>
<p>Universidade Federal do Ceará-UFC</p>
<h2>Primeiro passo</h2>
<p>O projeto foi feito na versão 3.7 do python em um pc com windows</p>
<p>Para que o programa seja executado é necesário que seja feito clone do arquivo no formato .zip e apenas executar o arquivo Aluguel.exe</p>
<p>*Caso não dê certo abra O Idle importe o arquivo tb2.py e execute</p>
<h2>Tela principal</h2>
<p>Quando o programa for executa aprecerá uma tela principal parecida com os segunites itens:</p>
<h3>No cabeçalho</h3>
<p><b>Cadastros:</b>aqui um contador mostra a quantidade de carros Cadastrados.</p>
<p><b>Alugueis:</b>aqui um contador mostra a quantidade de carros Alugados.</p>
<p><b>Atrassos:</b>aqui um contador mostra a quantidade de carros Atrassados.</p>
<h3>No corpo</h3>
<p>1-Consultar veículos </p>
<p>2-Adicionar veículos </p>
<p>3-Alugar/reservar veículos</p>
<p>4-Devolver/liberar veículos </p>
<p>5-Excluir veículos </p>
<p>6-Avançar data atual</p>
<p>7-Sair</p>
<p>Cada item acima tem uma funcionalidade que será explicada a seguir.</p>
<h3>No rodapé</h3>
<p>Aqui são mostrados data e hora.</p>
<p>Por  fim tem a seguinte ordem: "Digite um número de 1-7 para escolher uma das opções:"</p>
<p>*Caso seja digitado um caractere que não está listado será apresentado um erro.</p>
<h2>1-Consultar veículos</h2>
<p>Aqui aparece a lista de todos os veículos cadastrados(Até os excluidos).</p>
<p>Caso queira ver mais detalhes sobre o veículo digite seu código que é o primeiro item que aparece nas listas como: "001".</p>
<p>*Caso seja digitado um número não cadastrado será apresentado um erro.</p>
<h2>2-Adicionar veículos</h2>
<p>Aqui será cadastrado um novo veículo.</p>
<p>Serão pedidos a marca, o modelo, o ano e o valor da diária do veículo.</p>
<p>Depois de adicionado o novo veículo aparecerá na lista, podera ser alugado ou reservado e o contador "Cadastros" será adicionado em um.
<h2>3-Alugar/reservar veículos</h2> 
<p>Há duas opções 1 alugar e 2 resevar.</p>
<h3>Alugar</h3>
<p>Caso escolha alugar será pedido o código do veículo, o nome do locatário e a quantidade de dias que ele passará a partir do dia atual.</p>
<p>*Essa quantidade de dias conta o dia atual também ou seja se forem 3 dias serão dois dias a mais além do atual.</p>
<h3>Reservar</h3>
<p>Caso escolha alugar será pedido o código do veículo, o nome do locatário, a data da reserva e a quantidade de dias que ele passará a partir do dia da reserva.<b> ATENÇÃO: </b> a data da reserva deve ser do formato "DDAAAAMM" ou seja se deseja reservar para dia primeiro de dezembro de 2018 deve ser digitado: 01201812, caso seja digitado em um formato diferente o programa não funcionará direito.</p>
<p>*Assim como no aluguel essa quantidade de dias conta o dia da reserva também ou seja se forem 3 dias serão dois dias a mais além do dia da reserva.</p>
<h2>4-Devolver/liberar veículos</h2>
<p>Aqui os veículos serão devolvidos mostrando o valor a ser pago.</p>
<p>São mostrados os veículos alugados ou reservados, seus modelos e os respectivos Locatários.</p>
<p>Há duas opções 1 devolver e 2 liberar.</p>
<h3>Devolver</h3>
<p>Caso escolha devolver será pedido o código ou número do veículo que deseja ser devolvido.</p>
<p>Aparecerá a divida que foi acumulada e uma mensagem dizendo que o veículo foi liberado e ele já estará dispinível para aluguel ou reserva.</p>
<h3>Liberar</h3>
<p>Caso escolha liberar será pedido o código ou número do veículo que deseja ser liberado.</p>
<p>*A diferença desse para Devolver é que não gera dívida.</p>
<h2>5-Excluir veículos </h2>
<p>Aqui poderão ser excluidos os veículos que estão dispiníveis.</p>
<p>*O veículo ainda será contabilizado como registrado mas terá o status de excluido e não poderá ser alugado nem reservado.</p>
<h2>6-Avançar data atual</h2>
<p>Avance um dia.Os meses são considerados com 30 dias.</p>
<h2>7-Sair</h2>
<p>Sai do programa.</p>








  







/**
 * Envia requisicao ajax
 */
$(document).ready(function () {

	/* Pega evento de button click e chama metodo*/
	$("#buttonSend").click(function() {

		var computers = getValueComputer();
		var commands = getValueCommand();

		$.ajax({
			url: '/home/',
			type: 'POST',
			data: { 
				'computers[]' : computers,
				'commands[]': commands,
				'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
			},

		});

	}); 
	
});

/**
 * Verifica maquina e comandos para confirmacao do usuario.
 */
$("#buttonBeforeSend").click(function(){

	// Recebe checkeds
	var computers = getValueComputer();
	var commands = getValueCommand();

	// Verifica se foram seleciona computadores e comandos
	if(computers.length > 0 && commands.length > 0){

		$('#validacao').modal('show');

	}else{

		// Erro em ambos os campos
		if(computers.length == 0 && commands.length == 0 ){

			$('#erro').modal('show');
			$('#msgErro').text("Selecione o(s) computadores e o(s) comandos!");


		// Erro em computadores
		}else if(computers.length == 0) {

			$('#erro').modal('show');
			$('#msgErro').text("Selecione o(s) computadores!");

		// Erro em comandos
		}else{

			$('#erro').modal('show');
			$('#msgErro').text("Selecione o(s) comandos!");

		}

	}

});


/* Pega valores de computeadores */
function getValueComputer(){

	var computers = [];
	
	/* Pega pelo id da tabela os checks */
	$("#tableComputer input:checked").each(function() {
		computers.push($(this).val());
	});

	return computers;
	
};

/* Pega valores de commando */
function getValueCommand(){

	var commands = [];
	
    /* Pega pelo id da tabela os checks */
	$("#tableCommand input:checked").each(function() {
		commands.push($(this).val());
	});

	return commands;
	
};

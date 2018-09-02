
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

function getValueComputer(){

	var computers = [];
	
	/* Pega pelo id da tabela os checks */
	$("#tableComputer input:checked").each(function() {
		computers.push($(this).val());
	});

	return computers;
	
};


function getValueCommand(){

	var commands = [];
	
    /* Pega pelo id da tabela os checks */
	$("#tableCommand input:checked").each(function() {
		commands.push($(this).val());
	});

	return commands;
	
};

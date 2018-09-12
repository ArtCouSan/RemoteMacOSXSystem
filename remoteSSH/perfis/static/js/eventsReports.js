/**
 * Envia requisicao ajax
 */
$(document).ready(function () {

	/* Pega evento de button click e chama metodo*/
	$("#buttonSend").click(function() {

		var computers = getValueComputer();
		var reports = getValueReport();

		$.ajax({
			url: '/report/',
			type: 'POST',
			data: { 
				'computers[]' : computers,
				'reports[]': reports,
				'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
			},

		});

	}); 
	
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

/* Pega valores de reports */
function getValueReport(){

	var reports = [];
	
    /* Pega pelo id da tabela os checks */
	$("#tableReport input:checked").each(function() {
		reports.push($(this).val());
	});

	return reports;
	
};

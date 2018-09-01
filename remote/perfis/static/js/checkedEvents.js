$(document).ready(function () {

	/* Pega evento de button click e chama metodo*/
	$("#buttonSend").click(function() {
        getValueComputer();
        getValueCommand();
    });
    
});

function getValueComputer(){
	var chkArray = [];
	
	/* Pega pelo id da tabela os checks */
	$("#tableComputer input:checked").each(function() {
		chkArray.push($(this).val());
	});
	
	/* Declara em variavel o array */
	var selected;
	selected = chkArray.join(',') ;
	
	/* check if there is selected checkboxes, by default the length is 1 as it contains one single comma */
	if(selected.length > 0){
		alert("You have selected " + selected);	
	}else{
		alert("Please at least check one of the checkbox");	
	}
}


function getValueCommand(){
	var chkArray = [];
	
    /* Pega pelo id da tabela os checks */
	$("#tableCommand input:checked").each(function() {
		chkArray.push($(this).val());
	});
	
	/* Declara em variavel o array */
	var selected;
	selected = chkArray.join(',') ;
	

}
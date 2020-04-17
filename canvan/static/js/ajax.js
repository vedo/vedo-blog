$(document).ready(function() {
	var csrftoken = $("[name=csrfmiddlewaretoken]").val();
	$.ajax({
		method: 'POST',
		url: '/canvan/funcion-pruebas/',
		headers: {"X-CSRFToken": csrftoken},
		data: {'Valor': 5},
		success: function(response){
			console.log("exito")
		}
	});
});

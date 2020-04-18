const tarjetas = document.querySelectorAll('.tarjeta');
const columnas = document.querySelectorAll('.columna')

let draggedItem = null;

for ( let i = 0; i < tarjetas.length; i++){
    const tarjeta = tarjetas[i];

    tarjeta.addEventListener('click', function(){
        tarjeta.style.backgroundColor = "rgba(57, 135, 167, 0.3)";
    });

    tarjeta.addEventListener('mouseover', function(){
        tarjeta.style.backgroundColor = "rgba(57, 135, 167, 0.3)";
    });

    tarjeta.addEventListener('mouseleave', function(){
        tarjeta.style.backgroundColor = "white";
    });

    tarjeta.addEventListener('dragstart', function(){
		draggedItem = this;
		setTimeout(function(){
			tarjeta.style.display = 'none';
		}, 0);
	});

	tarjeta.addEventListener('dragend', function(){
		setTimeout(function(){
			draggedItem.style.display = 'block';
			draggedItem = null;
		}, 0);
	});
}

for ( let i = 0; i < columnas.length; i++ ){
    const columna = columnas[i];

    columna.addEventListener('dragover', function(e){
		e.preventDefault();
	});

	columna.addEventListener('dragenter', function(e){
		e.preventDefault();
	});

	columna.addEventListener('drop', function(){
		this.append(draggedItem);
		var csrftoken = $("[name=csrfmiddlewaretoken]").val();
		$.ajax({
			method: 'POST',
			url: '/canvan/actualizarColumna/',
			headers: {"X-CSRFToken": csrftoken},
			data: {
				'id_tarjeta': draggedItem.id,
				'id_columna': columna.id,
			},
			success: function(response){
				console.log(response.respuesta);
			}
		});
	});
}



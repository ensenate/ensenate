var elementos = document.getElementsByClassName('form-control');
var datos = obtener_datos();
var imagen = form_imagen();
var cambio = false;

function form_imagen(){
	try {
  		var image = document.getElementById('id_image');
  		this.datos.push(image.name);
  		this.datos.push(image.value);
	}
	catch (error) {
  	}

  	return image;
}

function obtener_datos(){
	var datos = [];
	for (var i = 0; i < elementos.length; i++) {
		datos.push(elementos[i].name);
		datos.push(elementos[i].value);
	}
	return datos;
}

function replazarElemento (ruta, tagname) {
	var rango = document.createRange();
	var elemento = document.createElement(tagname);

	if(tagname == "span"){
		elemento.className = "boton-enviar inactivo";
		this.cambio = false;
	}
	else{ 
		elemento.value = 'Guardar Cambios';
		elemento.type = 'submit';
		this.cambio = true;
		elemento.className = "boton-enviar activo";

	}

	rango.selectNodeContents(ruta);
	elemento.appendChild(rango.extractContents());	
	ruta.parentNode.replaceChild(elemento, ruta);
}


function validar(valor_elemento, nombre_elemento){
	for (var i = 0; i < datos.length; i++) {
		if(datos[i] == nombre_elemento){
			if(datos[i + 1] != valor_elemento){
				if(!this.cambio){
  					replazarElemento(document.querySelector('.boton-enviar'), 'input');
  				}
  			}
			else{
				if(this.cambio && validar_todos()){
  					replazarElemento(document.querySelector('.boton-enviar'), 'span');
  				}
  			}
		}
	}
}

function validar_todos(){
	var dato = document.getElementsByClassName('form-control');
	var contador = 0;
	var x = []; 

	for (var i = 1; i < this.datos.length; i++) {
		x.push(this.datos[i]);
		i++;
	}

	for (var i = 0; i < dato.length; i++) {
		if(x[i] == dato[i].value){
			contador++;
		}
	}

	if(contador == elementos.length){
		return true;
	}
	else{
		return false;
	}
}




for (var i = 0; i < elementos.length; i++) {

	elementos[i].addEventListener("input",function () {
		validar(this.value, this.name);
	});

}

function validar_imagen(elemento){

	replazarElemento(document.querySelector('.boton-enviar'), 'input');
}

imagen.addEventListener("change",function(){
	validar_imagen(this);
});

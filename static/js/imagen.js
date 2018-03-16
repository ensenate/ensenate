var boton_pause = document.getElementsByClassName("pause");
var boton_play = document.getElementsByClassName("play");

function funcion(boton, tipo){
	var img = boton.parentElement; 
	img = img.parentElement;
	img = img.children[1];
	
	if(tipo == 1){
		img.src = img.src.replace(".png", ".gif");	
	}
	if(tipo == 2){
		img.src = img.src.replace(".gif", ".png");
	}
}

for(var i=0; i < boton_pause.length; i++){
	boton_pause[i].addEventListener("click", function(){
		funcion(this, 2);
	});
	boton_play[i].addEventListener("click", function(){
		funcion(this, 1);
	});
}
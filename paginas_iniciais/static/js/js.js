var menu = document.querySelectorAll('li')[0];
var toggle = [];
var ativo = true;

var ligaDesliga = document.querySelectorAll('.navbar li');

if (document.title == "Aluno - FaTecCi"){
	console.log("Funciona!");
}

menu.addEventListener('click', function(){
	console.log('Teste');
	if(ativo == true){
		for(var i = 0; i < ligaDesliga.length; i++){
			ligaDesliga[i].style.display = 'block';
			ativo = false;
		}
	}else{
		for(var i = 0; i < ligaDesliga.length; i++){
			ligaDesliga[i].style.display = 'none';
		}
		ligaDesliga[0].style.display = 'block';
		ativo = true;
	}
});
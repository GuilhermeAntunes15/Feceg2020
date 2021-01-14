const numbers = ['zero','one','two','three','four','five','six','seven','eight','nine'];
var randomNumber;


function generateNumber(){
    var sorteio = document.getElementById('sorteio');
    randomNumber = Math.floor(Math.random() * (9.9 - 0) + 0);
    sorteio.innerHTML = numbers[randomNumber];
}

function checkAnswer(){
    var decisao = document.getElementById('decisao');
    var answer = document.getElementById('output').textContent;
    if(answer == randomNumber){
        decisao.innerHTML = 'Correto';
    }
    else {
        decisao.innerHTML = 'Errado';
    }
}
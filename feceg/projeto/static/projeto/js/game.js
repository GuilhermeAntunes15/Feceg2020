window.addEventListener('load',(function(){
    /// Definindo Variáveis
    let [submit, reset, span] = [this.document.querySelector('#check'), this.document.querySelector('#reset'), 
        document.querySelector('#result')];
    const colors = ['red', 'blue', 'black','green','orange','pink','yellow','brown'];
 
    /// Definindo Eventos
    submit.addEventListener('click', validateAnswers);
    reset.addEventListener('click', resetGame);


    /// Funções
    function validateAnswers(){
        let right = 0,
            answer = document.querySelectorAll('.form-control');
        
        for(let c = 0; c < 8; c++){
            answer[c].disabled = true;

            let user = (answer[c].value).toLowerCase();
            
            if(user.trim() === colors[c]){
                right += 1;
                answer[c].style.borderColor = "blue";
            } else { 
                answer[c].style.borderColor = "red";
            }
        }
         function showResult(right){
            let robotImage = "";
            if(right > 5){
                robotImage = "robot_acerto"
                span.style.color = 'green';
            } else {
                robotImage = "robot_erro"
                span.style.color = 'red';
            }
            span.innerHTML = `Você acertou ${right}/8! <img src="/static/projeto/img/mascote/${robotImage}.png" style="width: 125px"/>`
         }
        anotherTry();
        showResult(right);
        
    }

    function resetGame(){
        answer = document.querySelectorAll('.form-control');
        for(let c = 0; c < 8; c++){          
            answer[c].disabled = false;
            answer[c].value = '';
            answer[c].style.borderColor = "";
        }
        anotherTry();
    }

    function anotherTry(){
        span.innerHTML = '';
        if(submit.style.display === 'none'){ 
            submit.style.display = 'block' 
        }
        else { 
            submit.style.display = 'none' 
        }
        if( reset.style.display === 'none'){ 
            reset.style.display = 'block' 
        }
        else{ 
            reset.style.display = 'none' 
        }
    }
})
)
window.addEventListener('beforeunload', () => {
    window.scrollTo(0, 0);
})


function MudaBola(src, alt) {
    var aalt = alt;
    var src = src;
    if(alt == aalt){
        img_destaque.src = src;
        img_destaque.alt = alt;
        img_destaque.title = alt;
        texto_destaque.innerHTML = aalt;
        texto_destaque.style.color= aalt;
        audio.src = "/static/projeto/mp3s/colors/" +alt+ ".mp3";
        audio.play()
    }
}

function MudaAnimal(src, alt) {
console.log(src, alt);
    var aalt = alt;
    var src = src;
    if(alt == aalt){
        img_destaque.src = src;
        img_destaque.alt = alt;
        img_destaque.title = alt;
        texto_destaque.innerHTML = aalt;
        texto_destaque.style.color= aalt;
        audio.src = "/static/projeto/mp3s/animals/" +alt+ ".mp3";
        audio.play()
    }
}

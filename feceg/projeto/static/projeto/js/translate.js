google.load("language", "l");

 var text = document.getElementById("englishText").innerHTML ;
function translate() {
    window.doneCallback = function(response) {
        document.getElementById("arabicText").innerHTML +=response; }
    var s = document.createElement("script");
    s.src = "http://api.microsofttranslator.com/V2/Ajax.svc/Translate?oncomplete=doneCallback&appId=MyAppID&
    from=en&to=ar" + "&text=" + text;
    document.getElementsByTagName("head")[0].appendChild(s);
}

function Clicar(event){
    console.log(event)
    msg = event.path[1].children[1].textContent;
    translate(msg);
}
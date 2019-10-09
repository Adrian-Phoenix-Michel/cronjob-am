function myFunction() {
  var checkBox = document.getElementById("myCheck");
  var text = document.getElementById("text");
  var benutzerName = document.getElementById("Benutzername");
  var passWort = document.getElementById("Passwort");


  if (checkBox.checked === true){
      benutzerName.value="";
      passWort.value="";
      text.style.display = "block";
  }
  else {
      benutzerName.value=" ";
      passWort.value=" ";
      text.style.display = "none";
  }
}

function nightMode() {
    var night = document.getElementById("Night");
    var body = document.getElementById("Body");
    var submit = document.getElementById("Submit");
    var input = document.getElementById( "Input");

    var image = document.getElementById('Sun');

    if (night.checked === true){
        body.style.backgroundColor = "grey";
        image.src="https://img.icons8.com/cotton/2x/moon-satellite.png";
    }
    else {
        body.style.backgroundColor = "white";
        image.src="https://img.icons8.com/cotton/2x/sun--v2.png";
    }


}
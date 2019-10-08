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
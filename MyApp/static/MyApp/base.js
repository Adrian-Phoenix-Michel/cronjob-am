
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

function myReset() {
    var reset = document.getElementById("Reset");

    var title = document.getElementById("Title");
    var address = document.getElementById("Address");

    var checkBox = document.getElementById("myCheck");
    var text = document.getElementById("text");
    var benutzerName = document.getElementById("Benutzername");
    var passWort = document.getElementById("Passwort");

    var input1 = document.getElementById("Input1");
    var input2 = document.getElementById("Input2");
    var input3 = document.getElementById("Input3");
    var custom = document.getElementById("InputCustom");
    var textarea = document.getElementById("myTextArea");

    var inputbf = document.getElementById("InputBF");
    var inputbe = document.getElementById("InputBE");
    var inputbd = document.getElementById("InputBD");

    var inputas = document.getElementById("InputAS");


    benutzerName.value="";
    passWort.value="";
    title.value="";
    address.value="https://";
    checkBox.checked = false;
    text.style.display = "none";
    textarea.style.display = "none";
    textarea.value="Your text here";
    input1.checked = false;
    input2.checked = false;
    input3.checked = false;
    custom.checked = false;
    inputbf.checked = false;
    inputbe.checked = false;
    inputbd.checked = false;
    inputas.checked = false;


}

function myCustom() {
    var custom = document.getElementById("InputCustom");
    var textarea = document.getElementById("myTextArea");
    var minuteselect = document.getElementById("minutenSelect");
    var timeselect = document.getElementById("timeSelect");
    var dayselect = document.getElementById("daySelect");
    var time2select = document.getElementById("time2Select");
    var input1 = document.getElementById("Input1");
    var input2 = document.getElementById("Input2");
    var input3 = document.getElementById("Input3");

    if (custom.checked === true){
      textarea.style.display = "block";
    }
    else {
      textarea.style.display = "none";
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
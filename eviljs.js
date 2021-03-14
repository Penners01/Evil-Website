var d = new Date();
document.getElementById("evilDate").innerHTML = d;

function evilItems(word) {
    var word = document.getElementById("submitField").value;
    document.getElementById("evilItems").innerHTML = word + " is undeniably evil!";
};
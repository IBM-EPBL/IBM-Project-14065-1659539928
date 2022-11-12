
 function hide_password() {
    document.getElementsByClassName("fa-eye")[0].classList.toggle("fa-eye-slash");
    var x = document.getElementById("password");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}

function hide_con_password() {
    document.getElementsByClassName("fa-eye")[1].classList.toggle("fa-eye-slash");
    var x = document.getElementById("con_password");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}


function check_password(){
    let y =  document.getElementById("password");
    let y1 = document.getElementById("con_password");
    if(y.value!=y1.value){
        alert("Passwords mismatched");
        return false
    }
    else{
        return true
    }
}

function validate_password(password){
     if(password < 6){
      return false;
     }
     else{
        return true;
     }
}

function hide_password() {
    document.getElementsByClassName("fa-eye")[0].classList.toggle("fa-eye-slash");
    var x = document.getElementById("password");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}
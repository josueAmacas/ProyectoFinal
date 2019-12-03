function calcularEdad(fecha) {
    var hoy = new Date();
    var cumpleanos = new Date(fecha);
    var edad = hoy.getFullYear() - cumpleanos.getFullYear();
    var m = hoy.getMonth() - cumpleanos.getMonth();
    if (m < 0 || (m === 0 && hoy.getDate() < cumpleanos.getDate()))
    {
        edad--;
    }
    if (edad < 0) {
        edad = 0;
    }
    return edad;
}

function validarCedula(cedula) {
    var cad = cedula.trim();
    var total = 0;
    var longitud = cad.length;
    var longcheck = longitud - 1;
    if (cad !== "" && longitud === 10)
    {
        for (i = 0; i < longcheck; i++)
        {
            if (i % 2 === 0)
            {
                var aux = cad.charAt(i) * 2;
                if (aux > 9)
                    aux -= 9;
                total += aux;
            } else
            {
                total += parseInt(cad.charAt(i)); // parseInt o concatenará en lugar de sumar
            }
        }
        total = total % 10 ? 10 - total % 10 : 0;

        if (cad.charAt(longitud - 1) == total) {
            return true;
        } else {
            return false;
        }
    }
}
function manejoErrores(xml) {
    var xmlData = $.parseXML(xml);
    var error = $(xml).find("faultstring").text();
    //console.log(error);
    var mensaje = '<div class="alert alert-danger">';
    mensaje += error;
    mensaje += '</div>';
    $("#error").html(mensaje);
}
function verificarInicioSesion() {
    if (localStorage["token"] != null)
    {
        location.href = "inicio.html";
    }
}
function verificarNoInicioSesion() {
    if (localStorage["token"] == null)
    {
        location.href = "login.html";
    }
}
function cerrar_sesion() {
    localStorage.removeItem("token");
    localStorage.removeItem("user");
    localStorage.removeItem("external");
    location.href = "login.html";
}


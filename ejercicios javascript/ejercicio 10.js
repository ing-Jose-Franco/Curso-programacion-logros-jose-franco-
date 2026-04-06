let edad = 18;
let tieneEntrada = true;

if (edad >= 18 && tieneEntrada) {
    console.log("Acceso concedido");
} else {
    console.log("Acceso denegado");
}

edad = 19;
tieneEntrada = false;

if (edad >= 18 && tieneEntrada) {
    console.log("Acceso concedido");
} else {
    console.log("Acceso denegado");
}
const producto= "Tablet 10 pulgadas";
let precio= 450.99;
let stock= 25
let cantidad= 2
const envioGratis= true;

let subtotal= precio * cantidad;
subtotal= parsefloat(subtotal.toFixed(2))
let total = precio * 1.07;
total = parsefloat(total.toFixed(2));

console.log(`El precio inicial era "${subtotal}" y con IVA es "${total}"`)

<?php
$tabla = 8;

echo "TABLA DE MULTIPLICAR DEL $tabla"

for ($i = 1; $i <= 10; $i++) {
    $resultado = $tabla * $i;
    // Usamos el formato "8 x i = resultado"
    echo "$tabla x $i = $resultado\n";
}
?>
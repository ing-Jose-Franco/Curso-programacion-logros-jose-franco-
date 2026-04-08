<?php
$tabla = 8;

echo "TABLA DE MULTIPLICAR DEL $tabla\n";

for ($i = 1; $i <= 10; $i++) { 
    $resultado = $tabla * $i;
    echo "$tabla x $i = $resultado\n";
}
?>
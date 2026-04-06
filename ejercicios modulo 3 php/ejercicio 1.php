<?php
$pares = 0;
$impares = 0;


echo "Analizando números del $inicio al 50...\n\n";

for ($i = 1; $i <= 50; $i++) {
    if ($i % 2 == 0) {
        $pares++;
    } else {
        $impares++;
    }
}

echo "Resultados\n";
echo "Cantidad de números pares: $pares\n";
echo "Cantidad de números impares: $impares\n";
?>
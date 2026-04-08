<?php
$numero_secreto = 7;
$intento = 0;
$contador = 0;

echo "Adivina el número secreto (entre 1 y 10): \n";

while ($intento != $numero_secreto) {
    $intento++; 
    $contador++;
    echo "Intento $contador: ¿Es el $intento? \n";
}

echo "¡Adivinado! El número era $numero_secreto. Total intentos: $contador";
?>
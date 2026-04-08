<?php
$temperatura = 18;

if ($temperatura < 10) {
    echo "Fría";
} elseif ($temperatura >= 10 && $temperatura <= 25) {
    echo "Templada";
} else {
    echo "Calurosa";
}
?>
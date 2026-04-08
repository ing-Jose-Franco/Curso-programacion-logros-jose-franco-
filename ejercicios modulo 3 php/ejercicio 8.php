<?php
for ($n = 1; $n <= 30; $n++) {
    if ($n % 3 == 0 && $n % 5 == 0) {
        echo "MarTierra \n";
    } elseif ($n % 3 == 0) {
        echo "Mar \n";
    } elseif ($n % 5 == 0) {
        echo "Tierra \n";
    } else {
        echo "$n \n";
    }
}
?>
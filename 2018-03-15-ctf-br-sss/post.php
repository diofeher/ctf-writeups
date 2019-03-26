<?php
    $fp = fopen("log.txt", "a");
    $escreve = fwrite($fp, $_POST['x']);
    fclose($fp);
?>

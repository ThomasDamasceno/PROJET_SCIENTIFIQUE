<?php

$content = file_get_contents('php://input');
$file = fopen('test.txt', "w+");
fwrite($file, $content);
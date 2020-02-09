<?php

# JUST DO THIS IN NOTEPAD++

$orig = "\\v 9 اِس حصے کا کِیا کِیا ہم سبق ہے؟";
$repl = "\v 9 اِس حصے کا کِیا کِیا اہم سبق ہے؟";

if (!isset($argv[1])) {
 echo "Syntax: replace.php <filename>\n";
 exit;
} else {
 $filename = $argv[1];
 file_put_contents($filename,preg_replace("/$orig/",$repl,file_get_contents($filename)));
}
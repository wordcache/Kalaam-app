<?php
$orig = "पीछले बार";
$repl = "पिछली बार";

if (!isset($argv[1])) {
 echo "Syntax: replace.php <filename> <source-text> <replacement-text>\n";
 exit;
} else {
 $filename = argv[1];
 file_put_contents($argv[1],preg_replace("/{$orig/",$repl,file_get_contents($argv[1])));
}
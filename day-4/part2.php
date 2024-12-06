<?php
$file = fopen("day-4/input.txt", "r") or die("Unable to open file!");
$txt = fread($file,filesize("day-4/input.txt"));
$txt = preg_split('/\s+/', $txt);
$s = array();

foreach ($txt as $row) {
	$row = str_split($row);
	array_push($s, $row);
}

$amount = 0;

$xlength = count($s[0]);
$ylength = count($s);
// check for X - MAS
for ($y = 1; $y < $ylength - 1; $y+=1) {
	for ($x = 1; $x < $xlength - 1; $x+=1) {
        if ($s[$y][$x] == 'A') { // look for center 'A'
            if ($s[$y-1][$x-1] == 'M' && $s[$y-1][$y+1] == 'M') { // look for the m on top 
                if ($s[$y+1][$x-1] == 'S' && $s[$y+1][$x+1] == 'S') { // look for the s on bottom 
                    $amount += 1;
                }
            } else if ($s[$y-1][$x-1] == 'S' && $s[$y-1][$y+1] == 'S') { // look for the m on top 
                if ($s[$y+1][$x-1] == 'M' && $s[$y+1][$x+1] == 'M') { // look for the s on bottom 
                    $amount += 1;
                }
            }
        }
    }
}
?>
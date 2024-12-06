<?php
$file = fopen("day-4/input.txt", "r") or die("Unable to open file!");
//$file = fopen("day-4/testcase.txt", "r") or die("Unable to open file!");
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
            $tl = $s[$y-1][$x-1]; // top left
            $tr = $s[$y-1][$x+1]; // top right
            $bl = $s[$y+1][$x-1]; // bottom left
            $br = $s[$y+1][$x+1]; // bottom right
            if ($tl == 'M' && $tr == 'M') { 
                if ($bl == 'S' && $br == 'S') {
                    $amount += 1;
                }
            } else if ($tl == 'S' && $tr == 'S') {  
                if ($bl == 'M' && $br == 'M') { 
                    $amount += 1;
                }
            } else if ($tl == 'M' && $tr == 'S') {  
                if ($bl == 'M' && $br == 'S') {  
                    $amount += 1;
                }
            } else if ($tl == 'S' && $tr == 'M') {  
                if ($bl == 'S' && $br == 'M') { 
                    $amount += 1;
                }
            }
        }
    }
}
echo $amount;
?>
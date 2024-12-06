<?php
$file = fopen("day-4/input.txt", "r") or die("Unable to open file!");
$txt = fread($file,filesize("day-4/input.txt"));
$txt = preg_split('/\s+/', $txt);
$s = array();

foreach ($txt as $row) {
	$row = str_split($row);
	array_push($s, $row);
}

//print_r($s);
$amount = 0;
// count how many occurences of XMAS
$xlength = count($s[0]);
$ylength = count($s);
for ($y = 0; $y < $ylength; $y+=1) {
	for ($x = 0; $x < $xlength; $x+=1) {
		if ($s[$y][$x] == 'X') { // look for primary 'x'
			if ($y >= 3) {// we can look up
				if ($s[$y-1][$x] == 'M' && $s[$y-2][$x] == 'A' && $s[$y-3][$x] == 'S') {
					$amount += 1;
				}
			} 
			if ($y <= $ylength-3) { // we can look down
				if ($s[$y+1][$x] == 'M' && $s[$y+2][$x] == 'A' && $s[$y+3][$x] == 'S') {
					$amount += 1;
				}
			} 
			if ($x >= 3) { // we can look left
				if ($s[$y][$x-1] == 'M' && $s[$y][$x-2] == 'A' && $s[$y][$x-3] == 'S') {
					$amount += 1;
				}
			} 
			if ($x <= $xlength-3) { // we can look right
				if ($s[$y][$x+1] == 'M' && $s[$y][$x+2] == 'A' && $s[$y][$x+3] == 'S') {
					$amount += 1;
				}
			}
			// look for diagonals
			if ($y >= 3 && $x >= 3) { // we can look up-left
				if ($s[$y-1][$x-1] == 'M' && $s[$y-2][$x-2] == 'A' && $s[$y-3][$x-3] == 'S') {
					$amount += 1;
				}
			}
			if ($y >= 3 && $x <= $xlength-3) { // we can look up-right
				if ($s[$y-1][$x+1] == 'M' && $s[$y-2][$x+2] == 'A' && $s[$y-3][$x+3] == 'S') {
					$amount += 1;
				}
			}
			if ($y <= $ylength-3 && $x >= 3) { // we can look down-left
				if ($s[$y+1][$x-1] == 'M' && $s[$y+2][$x-2] == 'A' && $s[$y+3][$x-3] == 'S') {
					$amount += 1;
				}
			}
			if ($y <= $ylength-3 && $x <= $xlength-3) { // we can look down-right
				if ($s[$y+1][$x+1] == 'M' && $s[$y+2][$x+2] == 'A' && $s[$y+3][$x+3] == 'S') {
					$amount += 1;
				}
			}
		}
	}
}
echo $amount;
?>
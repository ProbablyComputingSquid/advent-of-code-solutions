/*
tasks: 
- sort two lists
- compare distance between items of both lists
- add up total distances
*/

import { readFileSync } from 'fs';

var file = readFileSync('aoc-1-2/input.txt').toString("utf-8");

var lines = file.split("\n")
var list1: String[] = [];
var list2: String[] = [];

for (let i = 0; i < lines.length; i++) {
    let split = lines[i].split("   ");
    list1.push(split[0]);
    list2.push(split[1]);
}

list1.sort();
list2.sort();

var total = 0;
for (let i = 0; i < list1.length; i++) {
    total += Math.abs(Number(list1[i]) - Number(list2[i]));
}
console.log(total);


//document.getElementById("result").innerHTML = String(total);
import { readFileSync } from 'fs';

var file = readFileSync('aoc-1-2/input.txt').toString("utf-8");

var lines = file.split("\n")

var list2Times: Record<number, number> = {};

for (let i = 0; i < lines.length; i++) {
    let split = lines[i].split("   ");  
    let num2 = split[1];
    if (list2Times[num2] == undefined) {
        list2Times[num2] = 0;
    }
    list2Times[num2] += 1;
}
//console.log(list2Times);
let total = 0;

for (let i = 0; i < lines.length; i++) {
    let split = lines[i].split("   ");
    //console.log(split[0]);
    let num1 = Number(split[0]);
   // console.log(num1);
    if (list2Times[num1] != undefined) {
        total += num1 * list2Times[num1];
    }
}
console.log(total);

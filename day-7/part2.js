const fs = require('node:fs');

//var file_data = fs.readFileSync('day-7/input.txt', 'utf8').split('\n');
var file_data = fs.readFileSync('day-7/test.txt', 'utf8').split('\n');
//console.log(file_data);
var info = [];
function allAdds(result, input) {
    let total = 0;
    input.forEach(element => {
        total += Number(element);
    })
    return total == result;
}
function allMultiply(result, input) {
    let total = 1;
    input.forEach(element => {
        total *= Number(element);
    })
    return total == result;
}
function mixed(result, input) {
    let total = input[0];
    let operands = Array(input.length).fill(0, 0, input.length);
    for (let j = 0; j < 3 ** operands.length; j++) { // go through the operands
        for (let i = 0; i < input.length; i++) { // evaluate if the operand sequence is correct
            if (operands[i] == 0) {
                total += input[i];
            } else if (operands[i] == 1) {
                total *= input[i];
            } else if (operands[i] == 2) {
                let temp = String(total);
                let temp2 = String(input[i]);
                temp = temp + temp2;
                total = Number(temp);
                //console.log(total);
            }
        } 
        if (total == result) { // if found a match return true
            return true;
        } else { // else change the operands
            //console.log(operands)
            for (let k = 0; k < operands.length; k++) {
                if (operands[k] == 0) {
                    operands[k] = 1;
                    break;
                } else if (operands[k] == 1) {
                    operands[k] = 2;
                    break;
                }  else {
                    operands[k] = 0;
                }
            }
            total = 0;
        }    
    }
    return false;
}
/*
var operands = [0,0,0,0]
for (let i = 0; i < 3 ** operands.length - 1; i++) {
    for (let k = 0; k < operands.length; k++) {
        if (operands[k] == 0) {
            operands[k] = 1;
            break;
        } else if (operands[k] == 1) {
            operands[k] = 2;
            break;
        }  else {
            operands[k] = 0;
        }
        
    }console.log(operands);
}*/

//console.log(mixed(156, [15,6]));
var log = [];
for (let i = 0; i < file_data.length; i++) {
    let result = file_data[i].split(':')[0]
    let inp = file_data[i].split(':')[1].trim().split(' ')
    let input = [];
    inp.forEach(e => input.push(Number(e)));
    if (allAdds(result,input) || allMultiply(result, input) || mixed(result, input)) {
        info.push(result);
        log.push(input);
    }
}

var sum = 0;
info.forEach(num => {
    sum += Number(num);
})

console.log(sum);
const fs = require('node:fs');

var file_data = fs.readFileSync('day-7/input.txt', 'utf8').split('\n');

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
    for (let j = 0; j < 2 ** operands.length; j++) { // go through the operands
        for (let i = 0; i < input.length; i++) { // evaluate if the operand sequence is correct
            if (operands[i] == 0) {
                total += input[i];
            } else if (operands[i] == 1) {
                total *= input[i];
            }
        } 
        if (total == result) {
            return true;
        } else {
            //console.log(operands)
            for (let k = operands.length - 1; k >= 0; k--) {
                if (operands[k] == 0) {
                    operands[k] = 1;
                    break;
                } else {
                    operands[k] = 0;
                }
            }
            total = 0;
        }    
    }
    return false;
}

//console.log(mixed(3267, [81, 40,27]));
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

#!/usr/bin/node

function add(a, b) {
    let result = a + b;
    return result;
}
console.log(add(process.argv[2], process.argv[3]));
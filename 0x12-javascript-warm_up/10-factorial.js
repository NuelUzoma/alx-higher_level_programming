#!/usr/bin/node

function factorial (x) {
  if (x === 0) {
    return 1;
  }
  if (isNaN(x)) {
    return 1;
  }
  return (x * factorial(x - 1));
}
console.log(Number(factorial(process.argv[2])));

#!/usr/bin/node

const argCount = process.argv.length - 2;

switch (argCount) {
  case 0:
    console.log('Not a number');
    break;
  case 1:
    if (`${process.argv[2]}`) {
      console.log('Not a number');
    }
    console.log(`My number: ${process.argv[2]}`);
    break;
}

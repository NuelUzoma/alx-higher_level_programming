#!/usr/bin/node

const argsCount = process.argv.length - 2;

switch (argsCount) {
  case 0:
    console.log('undefined is undefined');
    break;
  case 1:
    console.log(`${process.argv[2]} is undefined`);
    break;
  case 2:
    console.log(`${process.argv[2]} is ${process.argv[3]}`);
    break;
}

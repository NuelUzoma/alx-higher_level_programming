#!/usr/bin/node

const argCounts = process.argv.length - 2;

switch (argCounts) {
  case 0:
    console.log('No argument');
    break;
  case 1:
    console.log(`${process.argv[2]}`);
    break;
}

#!/usr/bin/node

const argCountss = process.argv.length - 2;
const myWord = "C is fun";

switch (argCountss)
{
    case 0:
        console.log("Missing number of occurences");
        break;
    case 1:
        console.log(myWord[process.argv[2]]);
        break;
}

#!/usr/bin/node

const argCount = process.argv.length - 2;

switch(argCount)
{
    case 0:
        console.log("No argument");
        break;
    case 1:
        console.log("Argument found");
        break;
    default:
        console.log("Arguments found");
        break;
}
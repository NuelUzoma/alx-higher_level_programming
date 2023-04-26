#!/usr/bin/node

const fs = require('fs');

const filename = process.argv[2];
fs.readFile(filename, 'utf8', function (err, data) {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});

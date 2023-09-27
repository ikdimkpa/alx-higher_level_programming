#!/usr/bin/node

const fs = require('fs');

const pathToFile = process.argv[2];

fs.readFile(pathToFile, { encoding: 'utf-8' }, (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});

#!/usr/bin/node

const fs = require('fs');

const pathToFile = process.argv[2];
const data = process.argv[3];

fs.writeFile(pathToFile, data, (err) => {
  if (err) {
    console.log(err);
  }
});

#!/usr/bin/node
const num = parseInt(process.argv[2]);
let index = 0;

if (!num) {
  console.log('Missing number of occurrences');
} else {
  while (index < process.argv[2]) {
    console.log('C is fun');
    index++;
  }
}

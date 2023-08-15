#!/usr/bin/node
const arg = parseInt(process.argv[2]);

if (!arg) {
  console.log('Not a number');
} else {
  console.log('My number:' + ' ' + parseInt(process.argv[2]));
}

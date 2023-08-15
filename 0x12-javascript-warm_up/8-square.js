#!/usr/bin/node
const size = Number(process.argv[2]);
let index = 0;

if (!size) {
  console.log('Missing size');
} else {
  while (index < size) {
	  length = '';
    for (let index = 0; index < size; index++) {
	    length += 'x';
    }
	  console.log(length);
    index++;
  }
}

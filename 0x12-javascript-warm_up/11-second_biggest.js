#!/usr/bin/node
const arg = process.argv.slice(2);

if (arg.length <= 1) {
  console.log(0);
} else {
  const numbers = arg.map(x => parseInt(x));
  const max = Math.max(...numbers);
  const secondMax = Math.max(...numbers.filter(x => x < max));
  console.log(secondMax);
}

#!/usr/bin/node
const argv = process.argv;
const i = parseInt(process.argv[2]);
let j = 0;
if (i) {
  while (j < i) {
  console.log('C is fun');
  j++;
  }
} else {
  console.log('Missing number of occurrences');
}

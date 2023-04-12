#!/usr/bin/node
const argv = process.argv;
const i = parseInt(process.argv[2]);
let j = 0
let size = '';
if (i) {
for (let k = 0; k < i; k++) {
  size += 'X';
}
  while (j < i) {
  console.log(size);
  j++;
  }
} else {
  console.log('Missing size')
}

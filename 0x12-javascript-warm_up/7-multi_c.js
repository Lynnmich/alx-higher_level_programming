#!/usr/bin/node
const argv = process.argv;
const i = parseInt(argv[2]);
if (isNaN(i)) {
console.log('Missing number of occurrrences');
} else {
  for (let j = 0; j < i; j++) {
    console.log('C is fun');
}
}

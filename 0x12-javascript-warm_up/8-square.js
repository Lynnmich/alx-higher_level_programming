#!/usr/bin/node
const argv = process.argv;
const i = parseInt(argv[2]);
const size = 'X';
if (i) {
for (let j = 0; j < i; j++) {
  console.log();
} else if (isNaN(i)) {
    console.log('Missing size')
}
}


#!/usr/bin/node
const argv = process.argv;
const i = parseInt(process.argv[2]);
function factor (num) {
  if (num > 1) {
  return num * factor(num - 1);
  } else {
  return 1;
  }
}
console.log(factor(i));

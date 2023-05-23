#!/usr/bin/node
// A script that writes a string to a file

const fs = require('fs');

const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, { encoding: 'utf-8' }, (error) => {
  if (error) {
    console.log(error);
  }
});

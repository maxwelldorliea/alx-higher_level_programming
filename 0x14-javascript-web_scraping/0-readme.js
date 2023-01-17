#!/usr/bin/node

const fs = require('fs');
const argv = require('process').argv;

fs.readFile(argv[2], 'utf8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});

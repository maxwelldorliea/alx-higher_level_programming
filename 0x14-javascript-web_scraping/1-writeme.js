#!/usr/bin/node

const fs = require('fs');
const argv = require('process').argv;

fs.writeFile(argv[2], argv[3], 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});

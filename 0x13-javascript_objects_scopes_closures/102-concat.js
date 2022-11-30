#!/usr/bin/node

const fs = require('fs');
const argv = process.argv;

const data1 = fs.readFileSync(argv[2]);
const data2 = fs.readFileSync(argv[3]);
const data = data1.toString() + data2.toString();

fs.writeFile(argv[4], data, (err) => {
  if (err) {
    throw err;
  }
});

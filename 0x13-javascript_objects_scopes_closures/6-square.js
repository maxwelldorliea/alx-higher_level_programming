#!/usr/bin/node

const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c) {
    let i = 0;
    if (c === undefined) {
      c = 'X';
    }
    while (i < this.height) {
      let j = 0;
      while (j < this.width) {
        process.stdout.write(c);
        j++;
      }
      console.log();
      i++;
    }
  }
}

module.exports = Square;

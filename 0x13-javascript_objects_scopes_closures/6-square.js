#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let i = 0;
    if (c === undefined) {
      c = 'X';
    }
    while (i < this.width) {
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

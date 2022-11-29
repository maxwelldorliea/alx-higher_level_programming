#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w === undefined || w < 1 || h === undefined || h < 1) {
      const Rect = class Rectangle {};
      return new Rect();
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let i = 0;
    while (i < this.height) {
      let j = 0;
      while (j < this.width) {
        process.stdout.write('X');
        j++;
      }
      console.log();
      i++;
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
}

module.exports = Rectangle;

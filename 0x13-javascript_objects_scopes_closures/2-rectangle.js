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
}

module.exports = Rectangle;

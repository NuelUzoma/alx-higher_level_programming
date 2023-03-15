#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || !Number.isInteger(w) || h <= 0 || !Number.isInteger(h)) {
      return {};
    } else {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;

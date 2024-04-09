#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (!w || !h || (w <= 0 || h <= 0)) { return; }
    this.width = w;
    this.height = h;
  }

  print () {
    let printX = '';
    for (let index2 = 0; index2 < this.width; index2++) {
      printX += 'X';
    }
    for (let index = 0; index < this.height; index++) {
      console.log(printX);
    }
  }
}
module.exports = Rectangle;

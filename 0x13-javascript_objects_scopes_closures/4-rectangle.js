#!/usr/bin/node
class Rectangle {
  constructor(w, h) {
    if (!w || !h || (w <= 0 || h <= 0)) { return; }
    this.width = w;
    this.height = h;
  }

  print() {
    let printX = '';
    for (let index2 = 0; index2 < this.width; index2++) {
      printX += 'X';
    }
    for (let index = 0; index < this.height; index++) {
      console.log(printX);
    }
  }

  double() {
    this.width *= 2
    this.height *= 2
  }

  rotate() {
    let hold = this.width;
    this.width = this.height;
    this.height = hold;

  }
}
module.exports = Rectangle;

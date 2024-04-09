#!/usr/bin/node

const Rectangle = require('./5-square');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (!c) { super.print(); } else {
      let printX = '';
      for (let index2 = 0; index2 < this.width; index2++) {
        printX += c;
      }
      for (let index = 0; index < this.height; index++) {
        console.log(printX);
      }
    }
  }
}
module.exports = Square;

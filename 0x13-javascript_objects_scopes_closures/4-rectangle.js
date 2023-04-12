#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w >= 1 && h >= 1){
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const charactr = 'X';
    for (let i = 0; i < this.height; i++) {
    console.log(charactr.repeat(this.width));
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;

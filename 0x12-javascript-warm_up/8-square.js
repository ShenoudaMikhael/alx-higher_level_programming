#!/usr/bin/node
let printX = '';
for (let index2 = 0; index2 < parseInt(process.argv[2]); index2++) {
  printX += 'X';
}
for (let index = 0; index < parseInt(process.argv[2]); index++) {
  console.log(printX);
}

#!/usr/bin/node
function factorial (num) {
  if (num > 1) { return factorial(num - 1) * num; }
  return num;
}

if (!parseInt(process.argv[2])) {
  console.log(1);
} else {
  console.log(factorial(parseInt(process.argv[2])));
}

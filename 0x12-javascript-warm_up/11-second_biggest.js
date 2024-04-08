#!/usr/bin/node
if (!process.argv[2]) { console.log(0); } else if (process.argv[2] && !process.argv[3]) { console.log(0); } else {
  const args = process.argv.slice(2);
  let largest = -Infinity;
  let secondLargest = -Infinity;

  args.forEach(arg => {
    const current = parseInt(arg);
    if (current > largest) {
      secondLargest = largest;
      largest = current;
    } else if (current > secondLargest && current !== largest) {
      secondLargest = current;
    }
  });

  console.log(secondLargest);
}

#!/usr/bin/node
// print file data
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});

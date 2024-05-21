#!/usr/bin/node
const request = require('request');
const fs = require('fs');
request(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  fs.writeFile(process.argv[3], body, err => {
    if (err) {
      console.error(err);
    }
  });
});

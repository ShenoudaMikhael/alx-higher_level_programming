#!/usr/bin/node
const request = require('request');
request(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log('code:', response && response.statusCode);
});

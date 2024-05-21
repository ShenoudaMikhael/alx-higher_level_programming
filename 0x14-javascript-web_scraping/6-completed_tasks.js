#!/usr/bin/node
const request = require('request');
request(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  let q = {}
  let k = JSON.parse(body);
  for (let index = 0; index < k.length; index++) {
    const element = k[index];
    console.log(element)
    if (element.completed === true) {
      if (q.hasOwnProperty(element.userId)) {
        q[element.userId] = q[element.userId] + 1

      } else {
        q[element.userId] = 1

      }
    }
  }
  console.log(q);
});

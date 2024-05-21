#!/usr/bin/node
const request = require('request');
request(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  let count = 0;
  const b = JSON.parse(body);
  const cid = 18;
  b.results.forEach(element => {
    const movie = element;
    movie.characters.forEach(character => {
      const aa = character.split('/');
      if (aa[aa.length - 2] === cid) {
        count++;
      }
    });
  });
  console.log(count);
});

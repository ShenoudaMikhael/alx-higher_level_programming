#!/usr/bin/node
const request = require('request');
request(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  let count = 0;
  const b = JSON.parse(body);
  b.results.forEach(element => {
    const movie = element;
    movie.characters.forEach(character => {
      if (character.endsWith('/18/')) {
        count++;
      }
    });
  });
  console.log(count);
});

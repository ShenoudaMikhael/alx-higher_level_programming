#!/usr/bin/node
const request = require('request');
request('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const d = JSON.parse(body);
  d.characters.forEach(element => {
    request(element, (err, response, body) => {
      if (err) {
        console.log(err);
        return;
      }
      console.log(JSON.parse(body).name);
    });
  });
});

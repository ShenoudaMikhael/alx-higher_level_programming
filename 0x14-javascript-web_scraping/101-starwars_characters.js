#!/usr/bin/node
const request = require('request');

const makeRequest = (element) => {
  return new Promise((resolve, reject) => {
    request(element, (err, response, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
};

const processElements = async (kk) => {
  const qq = {};
  for (const element of kk) {
    qq[element.split('/')[element.split('/').length - 2]] = 0;
    try {
      const name = await makeRequest(element);
      qq[element.split('/')[element.split('/').length - 2]] = name;
      console.log(name);
    } catch (err) {
      console.error(err);
    }
  }
  return qq;
};

request('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const d = JSON.parse(body);
  const kk = d.characters;

  processElements(kk);
});

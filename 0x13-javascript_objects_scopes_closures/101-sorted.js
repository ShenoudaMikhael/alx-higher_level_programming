#!/usr/bin/node

const { dict } = require('./101-data');
const q = {};
for (const key in dict) {
  if (Object.hasOwnProperty.call(dict, key)) {
    const element = dict[key];
    if (!q[element]) { q[element] = []; }
    q[element].push(key);
  }
}
console.log(q);

#!/usr/bin/node

const { list } = require('./100-data');

const q = list.map((v, i) => { return v * i; });
console.log(list);
console.log(q);

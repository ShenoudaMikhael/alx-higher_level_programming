#!/usr/bin/node
const fs = require('fs');
const a = fs.readFileSync(process.argv[2], 'utf-8');
const b = fs.readFileSync(process.argv[3], 'utf-8');
const c = a + b;
fs.writeFileSync(process.argv[4], c);

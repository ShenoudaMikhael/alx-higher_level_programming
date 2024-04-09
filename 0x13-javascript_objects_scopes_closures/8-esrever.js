#!/usr/bin/node
exports.esrever = function (list) {
  const q = [];
  for (let i = list.length - 1; i >= 0; i--) {
    const element = list[i];
    q.push(element);
  }
  return q;
};

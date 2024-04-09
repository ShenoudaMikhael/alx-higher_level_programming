#!/usr/bin/node
exports.converter = function (base) {
  return q => q.toString(base);
};

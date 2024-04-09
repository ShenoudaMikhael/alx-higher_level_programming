#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const q =
        list.filter(v => {
          if (v === searchElement) { return true; }
          return false;
        });
  return q.length;
};

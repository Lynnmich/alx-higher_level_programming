#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const counts = list.reduce((i, value) => i + (value === searchElement), 0);
  return counts;
};

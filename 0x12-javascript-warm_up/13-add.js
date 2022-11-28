#!/usr/bin/node

exports.add = function (a, b) {
  a = parseInt(a);
  b = parseInt(b);
  if (isNaN(a) && isNaN(b)) {
    console.log(NaN);
    return 0;
  }
  return a + b;
};

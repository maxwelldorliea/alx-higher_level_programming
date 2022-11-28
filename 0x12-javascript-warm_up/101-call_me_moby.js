#!/usr/bin/node

exports.callMeMoby = function (x, printXTime) {
  let i = 0;

  while (i < x) {
    printXTime();
    i++;
  }
};

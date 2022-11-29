#!/usr/bin/node

let cnt = 0;

exports.logMe = function (item) {
  console.log(`${cnt}: ${item}`);
  cnt++;
};

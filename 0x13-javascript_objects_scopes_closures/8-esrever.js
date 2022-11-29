#!/usr/bin/node

exports.esrever = function (list) {
  const arr = [];

  const reverseArr = () => {
    let len = list.length - 1;

    while (len >= 0) {
      arr.push(list[len]);
      len--;
    }
  };

  reverseArr();

  return arr;
};

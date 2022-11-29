#!/usr/bin/node

exports.converter = function (base) {
  return (num) => {
    if (base !== 16) {
      return parseInt(num, base);
    }
    return num.toString(base);
  };
};

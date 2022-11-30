#!/usr/bin/node

const dict = require('./101-data').dict;
const newDict = (dict) => {
  const newDict = {};
  for (const k in dict) {
    if (newDict[dict[k]] === undefined) {
      newDict[dict[k]] = [];
    }
    newDict[dict[k]].push(k);
  }

  return newDict;
};

console.log(newDict(dict));

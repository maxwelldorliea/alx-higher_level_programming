#!/usr/bin/node

const dict = require('./101-data').dict;
const newDict = (dict) => {
  const newDict = {};
  for (const k in dict) {
    if (!Object.hasOwn(newDict, dict[k])) {
      newDict[dict[k]] = [];
    }
      const list = newDict[dict[k]];
      list.push(k);
  }

  return newDict;
};

console.log(newDict(dict));

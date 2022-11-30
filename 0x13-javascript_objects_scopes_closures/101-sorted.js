#!/usr/bin/node

const dict = require('./101-data').dict;
const out = dict.map((k, val) => {
  const newDict = {};
  for (const k in dict) {
    if (!Object.hasOwn(newDict, val)) {
      newDict[val] = [k];
    } else {
      const list = newDict[val];
      list.push(k);
    }
  }

  return newDict;
}
);

console.log(newDict);

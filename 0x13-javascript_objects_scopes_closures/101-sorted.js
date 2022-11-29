#!/usr/bin/node

const dict = require('./101-data').dict;
const newDict = {};

for (const k in dict) {
  if (!Object.hasOwn(newDict, dict[k])) {
    newDict[dict[k]] = [k];
  } else {
    const list = newDict[dict[k]];
    list.push(k);
  }
}

console.log(newDict);

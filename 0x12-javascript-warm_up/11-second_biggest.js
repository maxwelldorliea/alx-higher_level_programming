#!/usr/bin/node

function secondMax (arr) {
  let maxVal = -Infinity;
  let idx;
  let secMax = -Infinity;

  if (arr.length < 2) {
    return 0;
  }

  arr = arr.map((it) => parseInt(it));

  for (const i in arr) {
    if (arr[i] > maxVal) {
      maxVal = arr[i];
      idx = i;
    }
  }

  for (const j in arr) {
    if (j !== idx && arr[j] > secMax) {
      secMax = arr[j];
    }
  }

  return secMax;
}

let _, _1, arr;
[_, _1, ...arr] = process.argv;
_1 = _;
_ = _1;

console.log(secondMax(arr));

#!/usr/bin/node

function add (a, b) {
  a = parseInt(a);
  b = parseInt(b);
  if (isNaN(a) && isNaN(b)) {
    console.log(NaN);
    return;
  }
  console.log(a + b);
}

add(process.argv[2], process.argv[3]);

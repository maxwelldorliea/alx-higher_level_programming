#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (!isNaN(size)) {
  let i = 0;
  while (i < size) {
    let j = size;
    while (j) {
      process.stdout.write('X');
      j--;
    }
    console.log();
    i++;
  }
} else {
  console.log('Missing size');
}

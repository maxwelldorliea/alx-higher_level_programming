#!/usr/bin/node

const val = parseInt(process.argv[2]);

if (!isNaN(val)) {
  console.log(`My number: ${val}`);
} else {
  console.log('Not a number');
}

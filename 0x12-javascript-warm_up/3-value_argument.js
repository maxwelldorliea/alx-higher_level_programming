#!/usr/bin/node

const len = process.argv.length;

if (len > 2) {
  console.log(process.argv[2]);
} else {
  console.log('No aegument');
}

#!/usr/bin/node

const arg = process.argv;

if (arg[2]) {
  console.log(arg[2]);
} else {
  console.log('No argument');
}

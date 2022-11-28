#!/usr/bin/node

let argv = process.argv[2];

if (argv) {
  let i = 0;
  argv = parseInt(argv);
  while (i < argv) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}

#!/usr/bin/node

const request = require('request');
const argv = require('process').argv;

request(argv[2], (err, res, body) => {
  if (err) {
    throw err;
  }
  const data = JSON.parse(body).results;
  let count = 0;
  // data = data.filter(({ characters }) => characters.includes('https://swapi-api.alx-tools.com/api/people/18/'));
  for (const obj of data) {
    if (obj.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      count++;
    }
  }
  console.log(count);
});

#!/usr/bin/node

const request = require('request');
const argv = require('process').argv;

request(argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body).results;
  let count = 0;
  // data = data.filter(({ characters }) => characters.includes('https://swapi-api.alx-tools.com/api/people/18/'));
  for (let i = 0; data[i] !== undefined; i++) {
    if (data[i].characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      count++;
    }
  }
  console.log(count);
});

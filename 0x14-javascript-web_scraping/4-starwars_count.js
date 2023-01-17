#!/usr/bin/node

const request = require('request');
const argv = require('process').argv;

request(argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  }
  let data = JSON.parse(body).results;
  data = data.filter(({ characters }) => characters.includes('https://swapi-api.alx-tools.com/api/people/18/'));
  console.log(data.length);
});

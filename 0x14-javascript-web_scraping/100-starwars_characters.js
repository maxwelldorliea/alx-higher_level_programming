#!/usr/bin/node

const request = require('request');
const argv = require('process').argv;
const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}/`;

request(url, (err, res, body) => {
  if (err) {
    throw err;
  }
  const data = JSON.parse(body).characters;
  for (const userUrl of data) {
    request(userUrl, (error, response, value) => {
      if (error) {
        throw err;
      }
      console.log(JSON.parse(value).name);
    });
  }
});

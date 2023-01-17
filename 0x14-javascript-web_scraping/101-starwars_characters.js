#!/usr/bin/node

const request = require('request');
const argv = require('process').argv;
const baseUrl = `https://swapi-api.alx-tools.com/api/films/${argv[2]}/`;

const promiseRquest = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (err, res, body) => {
      if (res) {
        return resolve(res);
      }
      if (err) {
        return reject(err);
      }
    });
  });
};

const printAuthor = async () => {
  const charRes = await promiseRquest(baseUrl);
  const data = JSON.parse(charRes.body).characters;
  for (const userUrl of data) {
    try {
      const res = await promiseRquest(userUrl);
      console.log(JSON.parse(res.body).name);
    } catch (err) {
      console.log(err);
    }
  }
};
printAuthor();

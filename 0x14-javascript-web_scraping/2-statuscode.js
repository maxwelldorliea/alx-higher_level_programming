#!/usr/bin/node

const request = require('request');
const argv = require('process').argv;

request.get(argv[2]).on('response', (response) => {
  console.log('code:', response.statusCode);
});

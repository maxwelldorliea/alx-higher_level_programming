#!/usr/bin/node

const request = require('request');
const argv = require('process').argv;

request(argv[2], (err, res, body) => {
  if (err) {
    throw err;
  }
  let data = JSON.parse(body);
  const obj = {};
  let n = 1;
  data = data.filter(({ completed }) => completed === true);
  while (n <= 10) {
    const userTodos = data.filter(({ userId }) => userId === n);
    obj[n] = userTodos.length;
    n++;
  }
  console.log(obj);
});

#!/usr/bin/node

const request = require('request');
const argv = require('process').argv;

request(argv[2], (err, res, body) => {
  if (err) {
    throw err;
  }
  let data = JSON.parse(body);
  const objs = {};
  data = data.filter(({ completed }) => completed === true);
  for (const UserObj of data) {
    const userId = UserObj.userId;
    if (objs[userId]) {
      objs[userId] += 1;
    } else {
      objs[userId] = 1;
    }
  }
  console.log(objs);
});

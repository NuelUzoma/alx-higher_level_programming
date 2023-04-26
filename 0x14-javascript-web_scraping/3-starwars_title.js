#!/usr/bin/node

const request = require('request');

const id = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${id}`, function (err, response, body) {
  if (!err && response.statusCode === 200) {
    const film = JSON.parse(body);
    console.log(film.title);
  } else {
    console.log(err);
  }
});

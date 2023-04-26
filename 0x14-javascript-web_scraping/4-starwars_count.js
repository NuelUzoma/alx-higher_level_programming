#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];
const filmId = '18';

request(URL, function (error, body) {
  if (!error && request.statusCode === 200) {
    const filmsData = JSON.parse(body).results;
    const movies = filmsData.filter(film => {
      return film.characters.indexOf(`https://swapi-api.alx-tools.com/api/people/${filmId}/`) !== -1;
    });
    console.log(movies.length);
  } else {
    console.log(error);
  }
});

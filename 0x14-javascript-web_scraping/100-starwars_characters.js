#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

request(`https://swapi.dev/api/films/${movieId}/`, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const movie = JSON.parse(body);

  movie.characters.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error(`Error: ${error}`);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});

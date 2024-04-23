#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18; // Wedge Antilles character ID

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const films = JSON.parse(body).results;
  let count = 0;
  films.forEach(film => {
    if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
      count++;
    }
  });
  console.log(count);
});

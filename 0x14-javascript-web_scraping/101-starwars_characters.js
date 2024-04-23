#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const filmData = JSON.parse(body);
  const charactersUrls = filmData.characters;
  const charactersPromises = charactersUrls.map(characterUrl => new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  }));

  Promise.all(charactersPromises)
    .then(characters => {
      characters.forEach(character => console.log(character));
    })
    .catch(error => console.error(error));
});

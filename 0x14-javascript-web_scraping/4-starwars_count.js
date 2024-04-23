#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const characterId = '18';

let count = 0;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const data = JSON.parse(body);
  count = data.results.reduce((total, film) => {
    const hasCharacter = film.characters.some(character => character.includes(characterId));
    return total + (hasCharacter ? 1 : 0);
  }, 0);

  console.log(count);
});

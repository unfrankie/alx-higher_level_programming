#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const characterId = '18';

let count = 0;

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  try {
    const data = JSON.parse(body);
    count = data.results.reduce((total, film) => {
      const characterFound = film.characters.some(character => character.includes(characterId));
      return total + (characterFound ? 1 : 0);
    }, 0);
    console.log('Number of movies:', count);
  } catch (parseError) {
    console.error('Parsing error:', parseError);
  }
});

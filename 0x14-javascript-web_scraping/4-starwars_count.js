#!/usr/bin/node

const axios = require('axios');

const apiUrl = process.argv[2];
const characterId = 18;

axios.get(apiUrl)
  .then(response => {
    const films = response.data.results;
    const count = films.filter(film => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)).length;
    console.log(count);
  })
  .catch(error => {
    console.error(error);
  });

#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const actor = 'https://swapi-api.alx-tools.com/api/people/18';

request(url, (err, res, data) => {
  if (err) {
    console.log(err);
  } else {
    try {
      const jsonData = JSON.parse(data);
      if (jsonData && jsonData.results) {
        const films = jsonData.results;
        const match = films.filter((film) => film.characters.includes(actor));
        console.log(match.length);
      } else {
        console.log('Unexpected JSON structure: missing results property');
      }
    } catch (error) {
      console.log('Error parsing JSON:', error.message);
    }
  }
});

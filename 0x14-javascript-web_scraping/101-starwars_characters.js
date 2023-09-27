#!/usr/bin/node

// Prints all characters of a Star Wars movie synchronously
// and et movie ID from command line argument
const request = require('request');
const movieId = process.argv[2];

// Construct URL to fetch movie data and make a request to fetch movie data
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request(url, (err, res, body) => {
  // Error handling
  if (err) {
    console.log('Error: ', err);
    return;
  }
  // Movie data parsing
  const film = JSON.parse(body);
  // URLs of characters in the movie
  const charactersUrls = film.characters;

  // Array of promises to fetch the data of each character
  const charactersPromises = charactersUrls.map(characterUrl => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (err, response, body) => {
        if (err) {
          reject(err);
          return;
        }
        // Character data parsing
        const character = JSON.parse(body);
        // Resolve the promise with the name of the character
        resolve(character.name);
      });
    });
  });

  // Wait for all promises to resolve and then print the names of the characters
  Promise.all(charactersPromises)
    .then((characters) => {
      console.log(characters.join('\n'));
    })
    .catch((err) => {
      console.error('Error:', err);
    });
});

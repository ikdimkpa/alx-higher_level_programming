#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

request(url, (err, res, data) => {
  if (err) {
    console.log(err);
  } else {
    const actorsList = JSON.parse(data).characters;
    actorsList.forEach((actor) => {
      request(actor, (err, res, body) => {
        if (err) {
          console.log(err);
          return;
        }
        try {
          console.log(JSON.parse(body).name);
        } catch (error) {
          console.log('Error parsing JSON:', error.message);
        }
      });
    });
  }
});

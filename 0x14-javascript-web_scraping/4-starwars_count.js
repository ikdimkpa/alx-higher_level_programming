#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const actor = 'https://swapi-api.alx-tools.com/api/people/18';

request(url, (err, res, data) => {
  if (err) {
    console.log(err);
  } else {
    const films = jsonDdata.result;
	const match = films.filter((films) => film.character.includes.actor(actor));
	console.log(match.length);
  }
});

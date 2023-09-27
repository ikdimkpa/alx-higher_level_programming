#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2]
const pathToFile = process.argv[3];

request({url: url, encoding: 'utf-8'}, (err, res, data) => {
	if (err) {
		console.log(err);
		return;
	}
fs.writeFile(pathToFile, data, (err) => {
  if (err) {
    console.log(err);
  }
})});

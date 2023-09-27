#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const tasksCompleted = {};

request(url, (err, res, data) => {
  if (err) {
    console.log(err);
  } else {
    try {
      const todos = JSON.parse(data);

      todos.forEach((todo) => {
        if (todo.completed) {
          if (tasksCompleted[todo.userId]) {
            tasksCompleted[todo.userId]++;
          } else {
            tasksCompleted[todo.userId] = 1;
          }
        }
      });

      console.log(tasksCompleted);
    } catch (error) {
      console.log('Error parsing JSON:', error.message);
    }
  }
});

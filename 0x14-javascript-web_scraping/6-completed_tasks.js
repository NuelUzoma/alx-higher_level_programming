#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const todos = JSON.parse(body);
    const tasks = {};
    todos.forEach(todo => {
      if (todo.completed) {
        if (tasks[todo.userId]) {
          tasks[todo.userId]++;
        } else {
          tasks[todo.userId] = 1;
        }
      }
    });
    Object.entries(tasks).forEach(([userId, numTasks]) => {
      console.log(`'${userId}': ${numTasks}`);
    });
  } else {
    console.error(error);
  }
});

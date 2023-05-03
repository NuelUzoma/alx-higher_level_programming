#!/usr/bin/node

const header = $('UL#list_movies');

$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    type: 'GET',
    dataType: 'json',
    success: function (data) {
      header.text(data.title);
    }
  });
});

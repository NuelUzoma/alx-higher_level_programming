#!/usr/bin/node

const header = $('DIVcharacter');

$(document).ready(function () {
  $.ajax({
    type: 'GET',
    dataType: 'json',
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    success: function (data) {
      header.text(data.name);
    }
  });
});

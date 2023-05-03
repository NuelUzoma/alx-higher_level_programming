#!/usr/bin/node

const header = $('DIV#hello');

$(document).ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    header.text(data.hello);
  });
});

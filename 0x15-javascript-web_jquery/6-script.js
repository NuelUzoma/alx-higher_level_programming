#!/usr/bin/node

const header = $('DIV#update_header');

$(document).ready(function () {
  header.click(function () {
    header.text('New Header!!!');
  });
});

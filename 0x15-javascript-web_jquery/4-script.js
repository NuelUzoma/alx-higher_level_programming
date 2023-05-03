#!/usr/bin/node

const header = $('DIV#red_header');

$(document).ready(function () {
  header.click(function () {
    header.toggleClass('red green');
  });
});

#!/usr/bin/node

const header = $('DIV#add_item');

$(document).ready(function () {
  header.click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
});

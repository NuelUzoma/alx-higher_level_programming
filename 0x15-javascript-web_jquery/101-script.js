#!/usr/bin/node

$(document).ready(function () {
  const header = $('DIV#add_item');
  header.click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });

  const headerr = $('DIV#remove_item');
  headerr.click(function () {
    $('UL.my_list li:last-child').remove();
  });

  const headerrr = $('DIV#clear_list');
  headerrr.click(function () {
    $('UL.my_list').empty();
  });
});

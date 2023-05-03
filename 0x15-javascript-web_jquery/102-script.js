#!/usr/bin/node

$(document).ready(function () {
  const header = $('INPUT#btn_translate');
  header.click(function () {
    const lang = $('INPUT#language_code').val();
    const url = 'https://fourtonfish.com/hellosalut/?lang=' + lang;

    $.getJSON(url, function (data) {
      const headerr = $('DIV#hello');
      headerr.text(data.hello);
    });
  });
});

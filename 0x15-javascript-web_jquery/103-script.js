#!/usr/bin/node

$(document).ready(function () {
  function translate () {
    const lang = $('INPUT#language_code').val();
    const url = 'https://fourtonfish.com/hellosalut/?lang=' + lang;

    $.getJSON(url, function (data) {
      const headerr = $('DIV#hello');
      headerr.text(data.hello);
    });
  }

  const header = $('INPUT#btn_translate');
  header.click(function () {
    translate();
  });

  const headerrr = $('INPUT#language_code');
  headerrr.keypress(function (e) {
    if (e.which === 13) {
      translate();
    }
  });
});

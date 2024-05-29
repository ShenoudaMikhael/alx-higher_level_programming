$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    $.ajax({
      url: 'https://hellosalut.stefanbohacek.dev/?lang=' + $('INPUT#language_code').val(),
      context: document.body
    }).done(function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});

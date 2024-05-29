$(document).ready(function () {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    context: document.body
  }).done(function (data) {
    $('DIV#hello').text(data.hello);
  });
});

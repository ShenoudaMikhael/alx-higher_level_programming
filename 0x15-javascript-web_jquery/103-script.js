$(document).ready(function () {
  function tr () {
    $.ajax({
      url: 'https://hellosalut.stefanbohacek.dev/?lang=' + $('INPUT#language_code').val(),
      context: document.body
    }).done(function (data) {
      $('DIV#hello').text(data.hello);
    });
  }
  $('INPUT#btn_translate').click(function () {
    tr();
  });
  $('INPUT#language_code').focus(function () {
    $(this).keydown(function (e) {
      if (e.keyCode === 13) {
        tr();
      }
    });
  });
});

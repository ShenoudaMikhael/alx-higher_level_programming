$(document).ready(function () {
  $('DIV#add_item').click(function (e) {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('DIV#remove_item').click(function (e) {
    $('UL LI:last').remove();
  });
  $('DIV#clear_list').click(function (e) {
    $('UL LI').remove();
  });
});

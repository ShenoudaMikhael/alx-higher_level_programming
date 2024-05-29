$(document).ready(function () {
  $('DIV#add_item').click(function (e) {
    $('UL.my_list').append('<li>Item</li>');
  });
});

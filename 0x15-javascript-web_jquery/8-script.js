$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    context: document.body
  }).done(function (data) {
    data.results.forEach(element => {
      $('UL#list_movies').append('<LI>' + element.title + '</LI>');
    });
  });
});

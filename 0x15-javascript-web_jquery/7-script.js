$('document').ready(() => {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json'),
    (data) => {
      $('DIV#character').text(data.name);
    });
});

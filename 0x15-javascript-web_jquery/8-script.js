$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, statusCode) {
  if (statusCode === 'success') {
    $.each(data.results, function (i, obj) {
      $('#list_movies').append('<li>' + obj.title + '</li>');
    });
  }
});

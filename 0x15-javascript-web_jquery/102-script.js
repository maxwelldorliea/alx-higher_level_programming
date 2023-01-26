$(function () {
  const URL = 'https://www.fourtonfish.com/hellosalut/hello/?lang=';
  $('#btn_translate').click(function () {
    const CODE = $('#language_code').val(); 
    $.get(URL + CODE, function (data, stateCode) {
      $('#hello').text(data.hello);
    });
  });
});

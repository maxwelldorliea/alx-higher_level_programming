$(function () {
  const URL = 'https://www.fourtonfish.com/hellosalut/hello/?lang=';
  $('#btn_translate').click(function () {
    const CODE = $('#language_code').val();
    $.get(URL + CODE, function (data, stateCode) {
      $('#hello').text(data.hello);
    });
  });
  $('#language_code').keyup(function (e) {
    if (e.keyCode === 13) {
      const CODE = $('#language_code').val();
      $.get(URL + CODE, function (data, stateCode) {
        $('#hello').text(data.hello);
      });
    }
  });
});

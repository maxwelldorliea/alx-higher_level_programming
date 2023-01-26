const $ = window.$;
$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data, statusCode) {
  if (statusCode === 'success') {
    $('#hello').text(data.hello);
  }
});

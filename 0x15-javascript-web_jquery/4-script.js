/** $('#toggle_header').click(function () {
  $(this).toggleClass('red');
});**/

/** $('#toggle_header').toggle(function () {
  $(this).removeClass('green').addClass('red');
}, function () {
  $(this).removeClass('red').addClass('green');
})**/

$('#toggle_header').click(function () {
  $(this).toggleClass(function () {
    if ($(this).hasClass('red')) {
      return 'green';
    }
    return 'red';
  });
});

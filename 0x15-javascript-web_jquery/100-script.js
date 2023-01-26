function changeHeaderColor () {
  document.querySelector('header').style.color = '#FF0000';
}

if (document.readyState === 'complete') {
  changeHeaderColor();
} else {
  if (window.addEventListener) {
    window.addEventListener('load', changeHeaderColor, false);
  } else {
    window.attachEvent('onload', changeHeaderColor);
  }
}

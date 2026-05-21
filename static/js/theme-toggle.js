(function () {
  'use strict';
  var btn = document.querySelector('[data-theme-toggle]');
  if (!btn) { return; }
  btn.addEventListener('click', function () {
    var html = document.documentElement;
    var current = html.getAttribute('data-theme') || 'light';
    var next = current === 'dark' ? 'light' : 'dark';
    html.setAttribute('data-theme', next);
  });
}());

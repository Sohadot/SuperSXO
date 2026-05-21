(function () {
  'use strict';

  var STORAGE_KEY = 'sxo-theme';
  var html = document.documentElement;

  var stored = null;
  try { stored = localStorage.getItem(STORAGE_KEY); } catch (e) {}

  if (stored === 'dark' || stored === 'light') {
    html.setAttribute('data-theme', stored);
  }

  var btn = document.querySelector('[data-theme-toggle]');
  if (!btn) { return; }

  btn.addEventListener('click', function () {
    var current = html.getAttribute('data-theme') || 'light';
    var next = current === 'dark' ? 'light' : 'dark';
    html.setAttribute('data-theme', next);
    try { localStorage.setItem(STORAGE_KEY, next); } catch (e) {}
  });
}());

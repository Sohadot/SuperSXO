/*
  tribunal-viewport.js
  SuperSXO — Tribunal Viewport Interaction Prototype
  Non-public. Not deployed. Not part of build output.

  Handles: touch/click activation, keyboard (Enter/Space/Escape),
  aria-expanded state. Hover is driven by CSS; this JS layer
  handles touch devices and explicit keyboard activation.

  No analytics. No tracking. No localStorage. No cookies.
  No network calls.
*/

(function () {
  'use strict';

  function init() {
    var articles = document.querySelectorAll('.article-inner[role="button"]');
    if (!articles.length) return;

    articles.forEach(function (inner) {
      var sheet = inner.closest('.article-sheet');
      if (!sheet) return;

      inner.addEventListener('click', function (e) {
        e.stopPropagation();
        toggleArticle(sheet, inner, articles);
      });

      inner.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          toggleArticle(sheet, inner, articles);
        }
        if (e.key === 'Escape') {
          deactivateAll(articles);
          inner.blur();
        }
      });
    });

    document.addEventListener('click', function (e) {
      if (!e.target.closest('.article-sheet')) {
        deactivateAll(articles);
      }
    });
  }

  function toggleArticle(sheet, inner, allInners) {
    var wasActive = sheet.classList.contains('is-active');
    deactivateAll(allInners);
    if (!wasActive) {
      sheet.classList.add('is-active');
      inner.setAttribute('aria-expanded', 'true');
    }
  }

  function deactivateAll(inners) {
    inners.forEach(function (i) {
      var s = i.closest('.article-sheet');
      if (s) s.classList.remove('is-active');
      i.setAttribute('aria-expanded', 'false');
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

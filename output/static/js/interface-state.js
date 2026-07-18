(function () {
  'use strict';

  if (!('IntersectionObserver' in window)) { return; }

  var panels = document.querySelectorAll('.station-panel[data-station-index]');
  var railItems = document.querySelectorAll('.station-item[data-station-index]');

  if (!panels.length || !railItems.length) { return; }

  var railMap = Object.create(null);
  var i;
  for (i = 0; i < railItems.length; i++) {
    var idx = railItems[i].dataset.stationIndex;
    if (idx) { railMap[idx] = railItems[i]; }
  }

  function onIntersect(entries) {
    var j, entry, stationIdx, railItem;
    for (j = 0; j < entries.length; j++) {
      entry = entries[j];
      stationIdx = entry.target.dataset.stationIndex;
      railItem = railMap[stationIdx];
      if (!railItem) { continue; }
      if (entry.isIntersecting) {
        railItem.classList.add('is-active');
        entry.target.classList.add('is-active');
      } else {
        railItem.classList.remove('is-active');
        entry.target.classList.remove('is-active');
      }
    }
  }

  var observer = new IntersectionObserver(onIntersect, {
    rootMargin: '-10% 0px -60% 0px',
    threshold: 0
  });

  var k;
  for (k = 0; k < panels.length; k++) {
    observer.observe(panels[k]);
  }
}());

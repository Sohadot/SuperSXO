/*
 * SuperSXO Score — governed self-assessment instrument.
 *
 * Governance (data/approved-scripts.json):
 *   - Runs only where #sxo-score-form exists; no-op everywhere else.
 *   - All answers stay in memory. No network calls, no storage, no
 *     cookies. Results are discarded on page unload.
 *   - Result markup is built with createElement/textContent only.
 *   - The reading is a self-reported diagnostic signal, never a
 *     performance prediction. Wording below is claim-governed.
 */
(function () {
  "use strict";

  var TOTAL_STATEMENTS = 14;
  var POINTS_PER_STATEMENT = 2;

  function bandFor(ratio) {
    if (ratio >= 1) { return "Governed"; }
    if (ratio >= 0.5) { return "Partially governed"; }
    return "Ungoverned";
  }

  function el(tag, className, text) {
    var node = document.createElement(tag);
    if (className) { node.className = className; }
    if (text) { node.textContent = text; }
    return node;
  }

  function readLayers(form) {
    var layers = [];
    var fieldsets = form.querySelectorAll("fieldset.score-layer");
    var unanswered = 0;

    fieldsets.forEach(function (fs) {
      var legend = fs.querySelector("legend");
      var name = legend ? legend.textContent.replace(/^[0-9]+\s*·\s*/, "") : "Layer";
      var groups = {};
      fs.querySelectorAll("input[type=radio]").forEach(function (input) {
        groups[input.name] = true;
      });
      var points = 0;
      var answered = 0;
      Object.keys(groups).forEach(function (groupName) {
        var checked = fs.querySelector("input[name=" + groupName + "]:checked");
        if (checked) {
          answered += 1;
          points += parseInt(checked.value, 10) || 0;
        }
      });
      var statementCount = Object.keys(groups).length;
      unanswered += statementCount - answered;
      layers.push({
        name: name,
        points: points,
        max: statementCount * POINTS_PER_STATEMENT
      });
    });

    return { layers: layers, unanswered: unanswered };
  }

  function renderIncomplete(result, unanswered) {
    result.replaceChildren();
    result.appendChild(el(
      "p",
      "score-incomplete",
      unanswered + " of " + TOTAL_STATEMENTS +
      " statements are still unanswered. Answer every statement to compute the reading."
    ));
  }

  function renderReading(result, layers) {
    result.replaceChildren();

    var totalPoints = 0;
    var totalMax = 0;
    layers.forEach(function (layer) {
      totalPoints += layer.points;
      totalMax += layer.max;
    });
    var percent = Math.round((totalPoints / totalMax) * 100);

    result.appendChild(el("h3", "score-reading-heading", "Assessment Reading"));
    result.appendChild(el(
      "p",
      "score-reading-total",
      "Journey governance signal: " + totalPoints + " of " + totalMax +
      " condition points (" + percent + "%)."
    ));

    var list = el("ul", "score-reading-layers");
    var weakest = [];
    var weakestRatio = 2;
    layers.forEach(function (layer) {
      var ratio = layer.max > 0 ? layer.points / layer.max : 0;
      var band = bandFor(ratio);
      list.appendChild(el(
        "li",
        "score-reading-layer",
        layer.name + ": " + band + " (" + layer.points + " of " + layer.max + ")"
      ));
      if (ratio < weakestRatio) {
        weakestRatio = ratio;
        weakest = [layer.name];
      } else if (ratio === weakestRatio) {
        weakest.push(layer.name);
      }
    });
    result.appendChild(list);

    if (weakestRatio < 1) {
      result.appendChild(el(
        "p",
        "score-reading-weakest",
        "Lowest-signal layer" + (weakest.length > 1 ? "s" : "") + ": " +
        weakest.join(", ") + ". This is where the search-to-action journey is most likely breaking down."
      ));
    }

    result.appendChild(el(
      "p",
      "score-reading-disclaimer",
      "This reading is a self-reported diagnostic signal. It is not a performance prediction, " +
      "and it does not guarantee any change in rankings, traffic, or conversions."
    ));

    var next = el("p", "score-reading-next",
      "For findings you can act on with confidence, the professional pathway is the ");
    var link = el("a", "score-reading-audit-link", "SXO Audit");
    link.setAttribute("href", "/sxo-audit/");
    next.appendChild(link);
    next.appendChild(document.createTextNode("."));
    result.appendChild(next);
  }

  function init() {
    var form = document.querySelector("#sxo-score-form");
    var button = document.querySelector("#score-compute");
    var result = document.querySelector("#score-result");
    if (!form || !button || !result) { return; }

    button.removeAttribute("disabled");
    button.addEventListener("click", function () {
      var reading = readLayers(form);
      if (reading.unanswered > 0) {
        renderIncomplete(result, reading.unanswered);
        return;
      }
      renderReading(result, reading.layers);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();

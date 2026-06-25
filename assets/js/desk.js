/* D-LOGIC Desk — render paneli z window.DESK oraz zywe sesje i zegar. Komentarze PL. */
(function () {
  var D = window.DESK || {};
  function $(id) { return document.getElementById(id); }
  function set(id, html) { var e = $(id); if (e) e.innerHTML = html; }
  // znak +/- z wlasciwym minusem
  function sgn(v, dec) {
    dec = (dec == null) ? 2 : dec;
    var a = Math.abs(v).toFixed(dec);
    return (v < 0 ? "−" : (v > 0 ? "+" : "")) + a;
  }

  // ---------- REZIM ----------
  function regime() {
    if (!D.regime) return;
    var r = D.regime, c = D.conditions || {};
    set("dk-regime",
      '<div class="dk-phase">' + r.phase_pl + '</div>' +
      '<div class="dk-chips"><span class="dk-chip acc">USD: ' + r.usd_bias + '</span>' +
      '<span class="dk-chip neg">EUR/USD: ' + r.eurusd_bias + '</span></div>' +
      '<div class="dk-cond">' +
      '<div><span class="dk-ok">✓</span> Realne stopy <b>' + c.real_10y + '</b></div>' +
      '<div><span class="dk-ok">✓</span> Krzywa 2s10s <b>' + c.curve + '</b></div>' +
      '<div><span class="dk-ok">✓</span> Carry Fed−EBC <b>' + c.carry + '</b></div>' +
      '</div>' +
      '<div class="dk-score">' + c.score + ' warunków → reżim potwierdzony</div>');
  }

  // ---------- SILA WALUT ----------
  function strength() {
    if (!D.strength) return;
    var a = D.strength, pxz = 108, cx = 300, top = 14, rh = 25, h = top + a.length * rh + 4;
    var s = '<svg viewBox="0 0 600 ' + h + '" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,Segoe UI,Roboto,sans-serif">';
    s += '<line class="dk-axis" x1="300" y1="8" x2="300" y2="' + (h - 6) + '"/>';
    for (var i = 0; i < a.length; i++) {
      var d = a[i], y = top + i * rh, w = Math.abs(d.z) * pxz, x = d.z >= 0 ? cx : cx - w;
      var cls = d.z >= 0 ? "dk-pos" : "dk-neg";
      var vx = d.z >= 0 ? (cx + w + 6) : (cx - w - 6), anc = d.z >= 0 ? "start" : "end";
      s += '<rect class="' + cls + '" x="' + x.toFixed(1) + '" y="' + y + '" width="' + w.toFixed(1) + '" height="14" rx="3"/>';
      s += '<text class="dk-t" x="6" y="' + (y + 11) + '" font-size="12">' + d.ccy + '</text>';
      s += '<text class="dk-tm" x="' + vx.toFixed(1) + '" y="' + (y + 11) + '" font-size="11" text-anchor="' + anc + '" font-family="ui-monospace,monospace">' + sgn(d.z, 2) + '</text>';
      s += '<text class="dk-tm" x="594" y="' + (y + 11) + '" font-size="10" text-anchor="end" font-family="ui-monospace,monospace">5D ' + sgn(d.bps5d, 0) + '</text>';
    }
    s += '</svg>';
    set("dk-strength", s);
  }

  // ---------- ZMIENNOSC ----------
  function vol() {
    if (!D.vol) return;
    var v = D.vol, fx = v.atr_pctile * 3.2, mx = 20 + fx;
    set("dk-vol",
      '<svg viewBox="0 0 360 76" xmlns="http://www.w3.org/2000/svg" font-family="ui-monospace,Consolas,monospace">' +
      '<text class="dk-tm" x="20" y="15" font-size="10">ATR(14) ' + v.atr_pips + ' pip</text>' +
      '<text class="dk-tm" x="340" y="15" font-size="10" text-anchor="end">' + v.regime + '</text>' +
      '<rect class="dk-track" x="20" y="26" width="320" height="12" rx="6"/>' +
      '<rect class="dk-fill" x="20" y="26" width="' + fx.toFixed(1) + '" height="12" rx="6"/>' +
      '<line class="dk-mark" x1="' + mx.toFixed(1) + '" y1="20" x2="' + mx.toFixed(1) + '" y2="44"/>' +
      '<text class="dk-t" x="' + mx.toFixed(1) + '" y="60" font-size="11" text-anchor="middle">' + v.atr_pctile + ' percentyl</text>' +
      '</svg>' +
      '<div class="dk-meta">koperta dnia <b>' + v.range_low + ' – ' + v.range_high + '</b> · RV/ATR ' + v.rv_atr + ' · variance-ratio ' + v.variance_ratio + '</div>');
  }

  // ---------- POZIOMY ----------
  function levels() {
    if (!D.levels) return;
    var html = '<div class="dk-levels">';
    for (var i = 0; i < D.levels.length; i++) {
      var l = D.levels[i];
      html += '<div class="dk-lv' + (l.spot ? ' spot' : '') + '"><span class="dk-lv-l">' + l.label +
        '</span><span class="dk-lv-p">' + l.price + '</span><span class="dk-lv-n">' + l.note + '</span></div>';
    }
    html += '</div>';
    set("dk-levels", html);
  }

  // ---------- KORELACJA ----------
  function ccol(v) {
    if (v >= 0.999) return "rgba(26,158,106,.30)";
    var a = (Math.min(Math.abs(v), 1) * 0.34 + 0.05).toFixed(2);
    return (v >= 0 ? "rgba(26,158,106," : "rgba(229,72,77,") + a + ")";
  }
  function correlation() {
    if (!D.correlation) return;
    var c = D.correlation, S = c.symbols, M = c.matrix;
    var html = '<div class="dk-corr" style="grid-template-columns:62px repeat(' + S.length + ',1fr)">';
    html += '<div class="dk-cc dk-ch"></div>';
    for (var k = 0; k < S.length; k++) html += '<div class="dk-cc dk-ch">' + S[k] + '</div>';
    for (var i = 0; i < M.length; i++) {
      html += '<div class="dk-cc dk-rh">' + S[i] + '</div>';
      for (var j = 0; j < M[i].length; j++) {
        var v = M[i][j], t = (v > 0 ? "+" : (v < 0 ? "−" : "")) + Math.abs(v).toFixed(2);
        html += '<div class="dk-cc' + (i === j ? " dk-diag" : "") + '" style="background:' + ccol(v) + '">' + t + '</div>';
      }
    }
    html += '</div>';
    var meta = '<div class="dk-meta">korelacja zwrotów dziennych · ' + c.lookback + ' sesji · dane do ' + c.asof + '</div>';
    set("dk-corr", html + meta);
  }

  // ---------- SESJE (live) ----------
  var SES = [{ i: 0, o: 21, c: 6 }, { i: 1, o: 23, c: 8 }, { i: 2, o: 7, c: 16 }, { i: 3, o: 12, c: 21 }];
  function isOpen(s, h) { return s.o < s.c ? (h >= s.o && h < s.c) : (h >= s.o || h < s.c); }
  function pad(n) { return (n < 10 ? "0" : "") + n; }
  function tick() {
    var d = new Date();
    var hf = (d.getUTCHours() * 3600 + d.getUTCMinutes() * 60 + d.getUTCSeconds()) / 3600;
    var clk = $("dk-clock");
    if (clk) clk.textContent = pad(d.getUTCHours()) + ":" + pad(d.getUTCMinutes()) + ":" + pad(d.getUTCSeconds()) + " UTC";
    var x = 84 + hf / 24 * 864;
    var nl = $("dk-now-line"); if (nl) { nl.setAttribute("x1", x); nl.setAttribute("x2", x); }
    var nd = $("dk-now-dot"); if (nd) nd.setAttribute("cx", x);
    var cnt = 0;
    for (var k = 0; k < SES.length; k++) {
      var s = SES[k], op = isOpen(s, hf); if (op) cnt++;
      var tgt = op ? s.c : s.o, diff = ((tgt - hf) % 24 + 24) % 24; if (diff < 0.0001) diff = 24;
      var hh = Math.floor(diff), mm = Math.floor((diff - hh) * 60);
      var ch = $("dk-ses" + s.i);
      if (ch) {
        var dot = ch.querySelector(".dot"); if (dot) dot.style.background = op ? "#1a9e6a" : "#cdd3da";
        var st = ch.querySelector(".st");
        if (st) {
          st.textContent = (op ? "otwarte · zamyka za " : "zamknięte · otwiera za ") + hh + "h " + mm + "m";
          st.style.color = op ? "#1a9e6a" : "";
        }
      }
    }
    var liq = $("dk-liq");
    if (liq) liq.textContent = cnt >= 2 ? ("wysoka płynność · " + cnt + " sesje") : (cnt === 1 ? "niższa płynność · 1 sesja" : "pauza · brak sesji");
  }

  regime(); strength(); vol(); levels(); correlation();
  tick(); setInterval(tick, 1000);
})();

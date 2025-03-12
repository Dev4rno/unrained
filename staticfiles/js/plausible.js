!(function () {
    var a,
        o = window.location,
        r = window.document,
        t = r.currentScript,
        l = t.getAttribute("data-api") || new URL(t.src).origin + "/api/event",
        s = t.getAttribute("data-domain");
    function c(t, e, n) {
        e && console.warn("Ignoring Event: " + e), n && n.callback && n.callback(), "pageview" === t && (a = !0);
    }
    var u = o.href,
        d = {},
        w = -1,
        p = !1,
        e = !1,
        v = null,
        f = 0;
    function n() {
        var t = r.body || {},
            e = r.documentElement || {};
        return Math.max(
            t.scrollHeight || 0,
            t.offsetHeight || 0,
            t.clientHeight || 0,
            e.scrollHeight || 0,
            e.offsetHeight || 0,
            e.clientHeight || 0
        );
    }
    function i() {
        var t = r.body || {},
            e = r.documentElement || {},
            n = window.innerHeight || e.clientHeight || 0,
            e = window.scrollY || e.scrollTop || t.scrollTop || 0;
        return g <= n ? g : e + n;
    }
    function h() {
        return v ? f + (Date.now() - v) : f;
    }
    var g = n(),
        b = i();
    function m() {
        var t = h();
        e ||
            a ||
            !(w < b || 3e3 <= t) ||
            ((w = b),
            setTimeout(function () {
                e = !1;
            }, 300),
            (t = { n: "engagement", sd: Math.round((b / g) * 100), d: s, u: u, p: d, e: t }),
            (v = null),
            (f = 0),
            S(l, t));
    }
    function y(t, e) {
        var n = "pageview" === t;
        if (/^localhost$|^127(\.[0-9]+){0,2}\.[0-9]+$|^\[::1?\]$/.test(o.hostname) || "file:" === o.protocol)
            return c(t, "localhost", e);
        if (
            (window._phantom || window.__nightmare || window.navigator.webdriver || window.Cypress) &&
            !window.__plausible
        )
            return c(t, null, e);
        try {
            if ("true" === window.localStorage.plausible_ignore) return c(t, "localStorage flag", e);
        } catch (t) {}
        var i = {};
        (i.n = t),
            (i.u = o.href),
            (i.d = s),
            (i.r = r.referrer || null),
            e && e.meta && (i.m = JSON.stringify(e.meta)),
            e && e.props && (i.p = e.props),
            n &&
                ((a = !1),
                (u = i.u),
                (d = i.p),
                (w = -1),
                (f = 0),
                (v = Date.now()),
                p ||
                    (r.addEventListener("visibilitychange", function () {
                        "hidden" === r.visibilityState
                            ? ((f = h()), (v = null), m())
                            : "visible" === r.visibilityState && null === v && (v = Date.now());
                    }),
                    (p = !0))),
            S(l, i, e);
    }
    function S(t, e, n) {
        window.fetch &&
            fetch(t, {
                method: "POST",
                headers: { "Content-Type": "text/plain" },
                keepalive: !0,
                body: JSON.stringify(e),
            }).then(function (t) {
                n && n.callback && n.callback({ status: t.status });
            });
    }
    window.addEventListener("load", function () {
        g = n();
        var t = 0,
            e = setInterval(function () {
                (g = n()), 15 == ++t && clearInterval(e);
            }, 200);
    }),
        r.addEventListener("scroll", function () {
            g = n();
            var t = i();
            b < t && (b = t);
        });
    var E = (window.plausible && window.plausible.q) || [];
    window.plausible = y;
    for (var H, L = 0; L < E.length; L++) y.apply(this, E[L]);
    function _(t) {
        (t && H === o.pathname) || (t && p && (m(), (g = n()), (b = i())), (H = o.pathname), y("pageview"));
    }
    function k() {
        _(!0);
    }
    var T,
        t = window.history;
    t.pushState &&
        ((T = t.pushState),
        (t.pushState = function () {
            T.apply(this, arguments), k();
        }),
        window.addEventListener("popstate", k)),
        "prerender" === r.visibilityState
            ? r.addEventListener("visibilitychange", function () {
                  H || "visible" !== r.visibilityState || _();
              })
            : _(),
        window.addEventListener("pageshow", function (t) {
            t.persisted && _();
        });
})();

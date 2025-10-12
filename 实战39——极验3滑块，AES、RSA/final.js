function get_user_response(t,e) {
    for (var n = e["slice"](-2), r = [], i = 0; i < n["length"]; i++) {
        var o = n["charCodeAt"](i);
        r[i] = 57 < o ? o - 87 : o - 48;
    }
    n = 36 * r[0] + r[1];
    var s, a = Math["round"](t) + n, _ = [[], [], [], [], []], c = {}, u = 0;
    i = 0;
    for (var l = (e = e["slice"](0, -2))["length"]; i < l; i++)
        c[s = e["charAt"](i)] || (c[s] = 1,
        _[u]["push"](s),
        u = 5 == ++u ? 0 : u);
    var h, f = a, d = 4, p = "", g = [1, 2, 5, 10, 50];
    while (0 < f)
        0 <= f - g[d] ? (h = parseInt(Math["random"]() * _[d]["length"], 10),
        p += _[d][h],
        f -= g[d]) : (_["splice"](d, 1),
        g["splice"](d, 1),
        d -= 1);
    return p;
}
// console.log(get_user_response(83,"33add2516b56b3adc058778ae9c00f6cjb"));

function n(t) {
    var e = "()*,-./0123456789:?@ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqr"
      , n = e["length"]
      , r = ""
      , i = Math["abs"](t)
      , o = parseInt(i / n);
    n <= o && (o = n - 1),
    o && (r = e["charAt"](o));
    var s = "";
    return t < 0 && (s += "!"),
    r && (s += "$"),
    s + r + e["charAt"](i %= n);
}
function generate_list(t) {
    for (var e, n, r, i = [], o = 0, s = 0, a = t["length"] - 1; s < a; s++)
        e = Math["round"](t[s + 1][0] - t[s][0]),
        n = Math["round"](t[s + 1][1] - t[s][1]),
        r = Math["round"](t[s + 1][2] - t[s][2]),
        0 == e && 0 == n && 0 == r || (0 == e && 0 == n ? o += r : (i["push"]([e, n, r + o]),
        o = 0));
    return 0 !== o && i["push"]([e, n, o]),
    i;
}
$_BBEl = function(t, e, n) {
    if (!e || !n)
        return t;
    var r, i = 0, o = t, s = e[0], a = e[2], _ = e[4];
    while (r = n["substr"](i, 2)) {
        i += 2;
        var c = parseInt(r, 16)
          , u = String["fromCharCode"](c)
          , l = (s * c * c + a * c + _) % t["length"];
        o = o["substr"](0, l) + u + o["substr"](l);
    }
    return o;
}
function get_aa(track_list,c,s) {
    new_list = generate_list(track_list);
    var r = []
    , i = []
    , o = [];
    new_list.map(function(t) {
    var e = function(t) {
        for (var e = [[1, 0], [2, 0], [1, -1], [1, 1], [0, 1], [0, -1], [3, 0], [2, -1], [2, 1]], n = 0, r = e['length']; n < r; n++)
            if (t[0] == e[n][0] && t[1] == e[n][1])
                return "stuvwxyz~"[n];
        return 0;
    }(t);
    e ? i['push'](e) : (r['push'](n(t[0])),
    i['push'](n(t[1]))),
    o['push'](n(t[2]));
})
    result = (r["join"](""))+ "!!" + (i["join"]("")) + "!!" + (o["join"](""));
    return $_BBEl(result, c, s)
}

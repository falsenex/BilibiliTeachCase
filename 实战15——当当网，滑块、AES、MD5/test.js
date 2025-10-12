const CryptoJS = require('crypto-js')
J = function(t) {
    return CryptoJS.MD5(t).toString()
}
function G() {
    var t = "DDClick521"
      , e = new Date
      , n = e.getFullYear() + ""
      , a = e.getMonth() + 1;
    a < 10 && (a = "0" + a);
    var r = e.getDate();
    r < 10 && (r = "0" + r);
    var s = e.getHours();
    s < 10 && (s = "0" + s);
    var i = e.getMinutes();
    i < 10 && (i = "0" + i);
    var o = e.getSeconds();
    o < 10 && (o = "0" + o);
    var c = "00" + e.getMilliseconds();
    c = c.substr(c.length - 3, 3);
    var l = Math.floor(1e5 + 9e5 * Math.random())
      , u = Math.floor(1e5 + 9e5 * Math.random())
      , d = n + a + r + s + i + o + c + l + u + t
      , p = J(d)
      , h = function(t) {
        var e = function(t, e) {
            return new Array(e + 1).join(t)
        }
          , n = parseInt(t.substr(0, 8), 16)
          , a = String(n).substr(0, 6)
          , r = a.length;
        return r < 6 && (a += e("0", Math.abs(6 - r))),
        a
    };
    return p = h(p),
    n + a + r + s + i + o + c + p + l + u
}
console.log(G())
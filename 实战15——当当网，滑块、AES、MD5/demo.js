const CryptoJS = require("crypto-js");
J = function(t) {
    return CryptoJS.MD5(t).toString()
}
function get_permanent_id() {
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

console.log(get_permanent_id())

Y = function(t, e) {
    U = CryptoJS.enc.Utf8.parse("0102030405060708")
    e = CryptoJS.enc.Utf8.parse(e);
    var n = CryptoJS.enc.Utf8.parse(t);
    return CryptoJS.AES.encrypt(n, e, {
        iv: U
    }).toString()
}
function get_sign(r,rankey) {
    r = decodeURIComponent(r)
    r = J(r)
    return Y(r, rankey)
}
// n = {
//     ct: "pc",
//     t: 1747036051173,
//     permanent_id: get_permanent_id(),
//     requestId: "2505121523025440SncQd9_9fd0",
//     situation: "login",
//
// }
// var a = {};
// Object.keys(n).sort().map(
//     (function(t) {
//         ("sign" != t && n[t] || 0 === n[t]) && (a[t] = n[t])
//     })
// );
// console.log(a)
rankey = "DCTfm6V1lJGsRoNU"
str = "ct=pc&permanent_id=20250512210452215207919356244452060&requestId=2505122142584820IhotJ2_8f57&situation=login&t=1747057814564"
console.log(get_sign(str, rankey))
console.log("xH+TCtqfTVBbsA5drhSynVEU1PEkpWQ8qZe3Xq5eEY7KnMlhOF8eBnjiSnoL6JoT" === get_sign(str, rankey))
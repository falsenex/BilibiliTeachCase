const CryptoJS = require('crypto-js')
function neo(a, e) {
    return Math.round(Math.random() * (e - a) + a)
}
function j3o(a) {
    a = a || 32;
    const e = "ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz"
      , n = e.length;
    let t = "";
    for (let r = 0; r < a; r++)
        t += e.charAt(Math.floor(Math.random() * n));
    return t
}
function ceo() {
    // let a = uo.get("browserId") || "";
    return j3o(24) + neo(1e7, 99999999)
}
function e4o(a) {
    const e = {};
    return Object.keys(a).sort().forEach(n => {
        e[n] = a[n]
    }
    ),
    e
}
function JC(a) {
    const e = [];
    return Object.keys(a).forEach(function(n) {
        e.push(n + "=" + a[n])
    }),
    e.join("&")
}
function ZVo(a) {
    const e = "1emiEKvaFBggjMPxPB8gEL7CM*#ViuStM54dafsX24l4h9#j6L4CWjusaiJHHtJj"
      , n = a;
    n.private_key = e;
    const t = e4o(n)
      , r = JC(t)
      , s = CryptoJS.MD5(r).toString();
    return delete n.private_key,
    n.sign = s,
    JC(n)
}
px = () => {
    const e = ceo()
      , n = -1
      , t = 1;
    return ZVo({
        browserId: e,
        isForeign: n,
        language: t
    })
}
function get_web_x7sy_dev(){
    return px()
}
// Web_X7sy_Dev = px()
// console.log(Web_X7sy_Dev)




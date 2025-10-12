const CryptoJS = require("crypto-js");
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
e = ceo()
, n = -1
, t = 1;
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
result =  ZVo({
    browserId: e,
    isForeign: n,
    language: t
})
console.log(result)

function p() {
    return "8f4d3cb0b7317bbfaa7a721bc210d7e4"
}
// r1 = CryptoJS.enc.Hex.parse(p())
// console.log(r1)
i= function(u, _, x) {
    // const d = a;
    u = "object" == typeof u ? JSON["stringify"](u) : u;

    // const T = ["C", "B", "C"]["join"]("")
    //   , f = n(["iv", "mode", "padding"], [_, Ja.mode[T], HVo]);
    // return au.encrypt(u, x, f)["ciphertext"]
    const encrypted = CryptoJS.AES.encrypt(u, x, {
            iv: _,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7 // CBC模式通常使用Pkcs7填充
        });
    return encrypted["ciphertext"]
}

o = function (u) {
    return u.replace(/\+/g, "-")['replace'](/\//g, "_")['replace'](/=/g, "")
}
function feo(g,v) {
    f = {
    "words": [
        875704368,
        1681141817,
        862139705,
        1684235317,
        875640884,
        1684092261,
        878786103,
        1697919845
    ],
    "sigBytes": 32
}
    const C = i(g, CryptoJS.enc.Hex.parse(p()), f)
      , S = CryptoJS.enc.Hex.parse(p())["concat"](C)["toString"](CryptoJS.enc.Base64)
      , w = o(S);
    // console.log(w)
    return "/" + "ga.do" + "/" + (v ||"") + w
}
part_url = feo("/login/loginByPwd", "api/")
console.log(part_url)
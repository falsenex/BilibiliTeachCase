// const CryptoJS = require('crypto-js')
// str = "bf505251bce250a560c556cf341c74d9"
// result = CryptoJS.enc.Hex.parse(str)
// console.log(result)
const CryptoJS = require("crypto-js");
fun_e = function (n, t) {
    const s = new Array(n["length"]);
        for (let i = -1 * 9245 + 7155 + -190 * -11; i < t["length"]; i++)
            s[t[i]] = n[i];
        return String["fromCharCo" + "de"](...s)
}
// console.log(CryptoJS.enc.Hex.parse("68fbff05bb6af1d8bf0b9a04413c6041"))
d = function(){
    r = fun_e([4364 + -9624 + 5359, -41 * 223 + -3801 + 7 * 1856, -1141 + -23 * 237 + 949 * 7, 5622 + 6332 + -11904, -8397 + -4204 + 12653, 3088 + 2469 + -1 * 5504, 6485 + -1815 * 5 + 1321 * 2, 2694 + 9201 * 1 + -11795, 31 * -135 + 31 * 10 + -3924 * -1, 271 * -35 + 4348 + 5237, 1432 + -4 * 1919 + 6292, 73 + -3 * 61 + 209, -3587 + 6322 + -2683 * 1, -708 + 776 * -1 + 1532, 7290 + 2 * 4652 + -16493, -893 * -7 + -4563 + -43 * 37, -3 * -715 + -7170 + 5077, 3224 + -3 + -3166 * 1, -895 * -10 + -4556 + -4341, 3299 + -7 * 1042 + 4052, -9107 + 1 * -8469 + 17627, -3 * 168 + 5789 * -1 + 6393, 7 * -331 + 3782 + 1 * -1412, -86 * 101 + 4795 * 2 + 212 * -4, 113 * -7 + -145 + -61 * -17, 180 + 20 * 87 + -1868, 6374 * -1 + 5924 + 550, -9609 * 1 + -797 + 10460, 9256 * -1 + -9886 + 19194, -106 * 17 + 1 * 8753 + -6850, 729 + -8024 + -7352 * -1, -2 * -331 + -9129 + -1 * -8564], [-7761 * 1 + -1400 + 10 * 917, -7064 + 7033 + 37 * 1, -1 * 1663 + 676 + -9 * -113, -4066 * 2 + 9558 + 3 * -475, -54 * 26 + -5461 + 6894, -79 * -1 + -1 * 7703 + 7639, -4917 * -1 + 1258 + -1 * 6159, -332 * 20 + -64 * -156 + -3324, -6733 + 911 + 5839, 1010 + -60 * 113 + 5774, -14 * 439 + 66 * 134 + 1348 * -2, -593 * -5 + 3026 * 1 + 122 * -49, -2348 + 8544 * -1 + 2729 * 4, -3579 + 4988 + 1 * -1406, -69 * -93 + -9103 * 1 + 2709, -23 * 179 + 3320 + -2 * -411, 1 * 8269 + 44 * 149 + -14820, 6391 + -9305 + -2941 * -1, -1284 + 607 * 13 + 6585 * -1, -4721 + 978 * 1 + 1 * 3754, 13 * 19 + 9997 + 4 * -2559, -2720 + 4141 + -1407, -1690 * 5 + -2359 * -2 + 2 * 1871, 8742 + 2 * 4163 + 2 * -8525, -503 * 11 + 3367 * -1 + 8931, -5299 + -14 * -526 + 1 * -2046, 1 * -6473 + -874 + 33 * 223, 1 * -8663 + -4174 + 12863, -2961 + 2 * -1962 + 6885, -3796 + 1652 + 2172, 701 * -5 + -8782 + 1 * 12294, 1 * 9685 + -459 * -19 + 1 * -18385]);
    return r
}
// console.log(d());
f = CryptoJS.enc.Latin1.parse(unescape(encodeURIComponent(d())))
i = function(u, _, x) {
    // const d = a;
    u = "object" == typeof u ? JSON["stringify"](u) : u;
    // const T = ["C", "B", "C"]["join"]("")
    //     , f = n(["iv", "mode", "padding"], [_, Ja.mode[T], HVo]);
    // return au.encrypt(u, x, f)["ciphertext"]
    // 将WordArray对象转换为CryptoJS可识别的格式
    const key = CryptoJS.lib.WordArray.create(x.words, x.sigBytes);
    const iv = CryptoJS.lib.WordArray.create(_.words, _.sigBytes);
    const encrypted = CryptoJS.AES.encrypt(u, key, {
            iv: iv,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        });

    // 返回Base64格式的加密结果
    return encrypted.ciphertext;
}
c = function(u) {
    // const _ = a;
    if (false) {
        const x = e[_(232)]
            , d = e[_(290)]
            , T = _0x1a6b58[x][d]
            , f = new _0x4fd60c(e[_(250)](T, 669 + 6457 + -548 * 13));
        let p = -4342 + -7796 * 1 + 3 * 4046, g, v;
        for (v = -8803 + -2475 + -5639 * -2; v < T; v++)
            g = _0x59b057[x][v],
            f[p++] = g >> -7124 + -15 * 569 + 15683,
            f[p++] = e.FsUpr(g, -7412 + 7056 + 372) & 2570 + 4961 + -7276,
            f[p++] = e[_(266)](e.MgZIK(g, 1408 * -1 + 1569 * 2 + -1722), -4656 + 1482 + -127 * -27),
            f[p++] = e.knKVo(-164 * -4 + -9371 + -13 * -690, g);
        return f
    } else
        return u.replace(/\+/g, "-")["replace"](/\//g, "_")["replace"](/=/g, "")
}
function feo(g, v){
    const C = i(g, CryptoJS.enc.Hex.parse("68fbff05bb6af1d8bf0b9a04413c6041"), f)
      , S = CryptoJS.enc.Hex.parse("68fbff05bb6af1d8bf0b9a04413c6041")["concat"](C)["toString"](CryptoJS.enc.Base64)
      , w = c(S);
    return ("/" + "ga.do" + "/" + (v || "") + w)
}
console.log(feo("/login/loginByPwd","api/"))
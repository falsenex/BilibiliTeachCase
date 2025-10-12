const CryptoJS = require('crypto-js')
// let e = {
//     "ts": 1746627891651,
//     "pageNo": 4,
//     "pageSize": 20,
//     "total": 2856,
//     "KIND": "GCJS",
//     "GGTYPE": "1",
//     "timeType": "6",
//     "BeginTime": "2024-11-07 00:00:00",
//     "EndTime": "2025-05-07 23:59:59"
// }
function s(e) {
    return CryptoJS.MD5(e).toString()
}
function l(t, e) {
    return t.toString().toUpperCase() > e.toString().toUpperCase() ? 1 : t.toString().toUpperCase() == e.toString().toUpperCase() ? 0 : -1
}
function u(t) {
    for (var e = Object.keys(t).sort(l), n = "", a = 0; a < e.length; a++)
        if (void 0 !== t[e[a]])
            if (t[e[a]] && t[e[a]]instanceof Object || t[e[a]]instanceof Array) {
                var i = JSON.stringify(t[e[a]]);
                n += e[a] + i
            } else
                n += e[a] + t[e[a]];
    return n
}
function d(t) {
    for (var e in t)
        "" !== t[e] && void 0 !== t[e] || delete t[e];
    var n = "B3978D054A72A7002063637CCDF6B2E5" + u(t);
    return s(n).toLocaleLowerCase()
}
function get_sign(e) {
    return d(e)
}
// console.log(get_sign(e))
// function decrypt(t) {
//     var e = h.a.enc.Utf8.parse(r["e"])
//       , n = h.a.enc.Utf8.parse(r["i"])
//       , a = h.a.AES.decrypt(t, e, {
//         iv: n,
//         mode: h.a.mode.CBC,
//         padding: h.a.pad.Pkcs7
//     });
//     return a.toString(h.a.enc.Utf8)
// }
function decrypt_data(t) {
	var e = CryptoJS.enc.Utf8.parse("EB444973714E4A40876CE66BE45D5930")
	  , n = CryptoJS.enc.Utf8.parse("B5A8904209931867")
	  , a = CryptoJS.AES.decrypt(t, e, {
		iv: n,
		mode: CryptoJS.mode.CBC,
		padding: CryptoJS.pad.Pkcs7
	});
	return a.toString(CryptoJS.enc.Utf8)
}
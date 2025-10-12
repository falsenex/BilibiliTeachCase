const CryptoJS = require('crypto-js')
var Yt = function(e) {
    // var t = Ut,
      n = CryptoJS['enc']['Utf8']["parse"]("lOrd6SqeZpDdGBoY")
      , r = CryptoJS['enc']['Utf8']["parse"]("RxE86Of9vRkNvfZL")
      , o = "";
    if ("string" == typeof e) {
        var c = Rt.a.parse(e);
        o = zt.a[t(276)](c, n, {
            iv: r,
            mode: Nt.a,
            padding: Ht.a
        })
    } else if (typeof(e) === "object") {
        var l = CryptoJS['enc']['Utf8']["parse"](JSON["stringify"](e));
        o = CryptoJS.AES.encrypt(l, n, {
            iv: r,
            mode: CryptoJS.mode.CTR,
            padding: CryptoJS.pad.Pkcs7
        })
    }
    // console.log(o)
    return o["ciphertext"]["toString"]()
}

function get_data(data_obj) {
    return Yt(data_obj)
}
// data_obj = {
//     "name": "productivity-workflow",
//     "size": 48
// }
// console.log(get_data(data_obj))
// result = Yt(data_obj)
// console.log(result)
// 08aaae3e96636dfa1396c4e07f9e2d5d42cc90770f4fff0116d19987bdee7a8943414be0fd46f2dc4271bf95006788a0
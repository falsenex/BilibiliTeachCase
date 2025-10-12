window = global;
const CryptoJS = require("crypto-js");
const JSEncrypt  = require('jsencrypt');
function yt(t) {
    t = t || {};
    var e = function(t) {
        for (var e = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*", i = "", r = 0; r < t; r++) {
            var n = Math.floor(Math.random() * e.length);
            i += e.substring(n, n + 1)
        }
        return i
    }(16)
      // , i = new gt({});
        ,i = new JSEncrypt();
    i.setPublicKey("MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCYEVrK/4Mahiv0pUJgTybx4J9P5dUT/Y0PuwMbk+gMU+jrZnBiXGv6/hCH1avIhoBcE535F8nJQQN3UavZdFkYidsoXuEnat3+eVTp3FslyhRwIBDF09v4vDhRtxFOT+R7uH7h/mzmyA2/+lfIMWGIrffXprYizbV76+YQKhoqFQIDAQAB");
    var r = i.encrypt(window.btoa(e)),
      s = CryptoJS.enc.Utf8.parse("0102030405060708")//{"words": [808529970,808661044,808792118,808923192],"sigBytes": 16}
      , h = CryptoJS.enc.Utf8.parse(e)
      //   , h = CryptoJS.enc.Utf8.parse("TR^IGRE*%EpMT8x6")
      , u = window.btoa(Object.keys(t).join(","))
      , c = {};
    return Object.keys(t).forEach((function(e) {
        var i = t[e]
          , r = CryptoJS.AES.encrypt(i, h, {
            iv: s,
            padding: CryptoJS.pad.Pkcs7
        });
        r = r.toString(),
        c[e] = r
    }
    )),
    {
        EUI: "".concat(r, ".").concat(u),
        encryptedParams: c
    }
}

function get_paras(user_json){
    return yt(user_json)
}
// console.log(get_paras({"user": "12140545349"}))

function get_passwd(mima_mingwen){
    return CryptoJS.MD5(mima_mingwen).toString().toUpperCase()
}

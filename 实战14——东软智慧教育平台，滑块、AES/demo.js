const CryptoJS = require('crypto-js');
function get_pointJson(a,d) {
    const l = CryptoJS.enc.Utf8.parse(d)
      , o = CryptoJS.enc.Utf8.parse(a);
    return CryptoJS.AES.encrypt(o, l, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    }).toString()
}

// console.log(get_pointJson('{"x":161.975,"y":5}', 'j3RmPj3rOIE2jrnA'))
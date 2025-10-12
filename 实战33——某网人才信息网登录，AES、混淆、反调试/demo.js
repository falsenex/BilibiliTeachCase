const CryptoJS = require('crypto-js')
arg1 = "type=0&username=12140545349&passwordeasy=W5E9j8YqIr13EqSuSyJfHA%3D%3D&osTenantId=2ad7bce569694baabe8ee27797ee23ee"
// _0x360806['b']["encrypt"](arg1, "/sysViewLoginApi/viewUserNameLoginaes")

//md5('123456')    16分割一下，分别作为key iv
//md5('console.log')  16分割一下，分别作为key iv

function get_passwd(mingwen) {
    _0x564fe5 = CryptoJS["enc"]["Utf8"]['parse'](mingwen)
    key_iv_str = CryptoJS.MD5('123456').toString()
    key = CryptoJS["enc"]["Utf8"]['parse'](key_iv_str.slice(0,16))
    iv = CryptoJS["enc"]["Utf8"]['parse'](key_iv_str.slice(16,32))
    _0x10a61f = CryptoJS['AES']["encrypt"](_0x564fe5, key, {
        iv:iv,
        mode:CryptoJS.mode.CBC,
        padding:CryptoJS.pad.Pkcs7
    });
    result = _0x10a61f["toString"]();
    console.log(result)
}
get_passwd('123456')
// '8pZHzCFnBZYuG2XX1TQWug=='
// 8pZHzCFnBZYuG2XX1TQWug==
function get_a(mingwen) {
    _0x564fe5 = CryptoJS["enc"]["Utf8"]['parse'](mingwen)
    key_iv_str = CryptoJS.MD5('console.log').toString()
    console.log(key_iv_str)
    key = CryptoJS["enc"]["Utf8"]['parse'](key_iv_str.slice(0,16))
    iv = CryptoJS["enc"]["Utf8"]['parse'](key_iv_str.slice(16,32))
    _0x10a61f = CryptoJS['AES']["encrypt"](_0x564fe5, key, {
        iv:iv,
        mode:CryptoJS.mode.CBC,
        padding:CryptoJS.pad.Pkcs7
    });
    result = _0x10a61f["toString"]();
    console.log(result)
}
get_a("type=0&username=12140545049&passwordeasy=8pZHzCFnBZYuG2XX1TQWug%3D%3D&osTenantId=2ad7bce569694baabe8ee27797ee23ee")


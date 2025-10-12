const CryptoJS = require('crypto-js')
const elliptic = require('elliptic');
function s(x) {
    this['ct'] = 0x1,
    this["sm3c3"] = this['sm3keybase'] = this['p2'] = null,
    this['key'] = Array(0x20),
    this["keyOff"] = 0x0,
    this["cipherMode"] = void 0x0 !== x ? x : SM2CipherMode["C1C3C2"];
    this.CreatePoint = function(ch, ci) {
        cj = new bK["crypto"]['ECDSA']({
            'curve': "sm2"
        });
        return bU["decodeFromHex"](cj['ecparams']["curve"], '04' + ch + ci);
    },
    this.GetWords = function (ch) {
        for (var ci = [], cj = ch["length"], ck = 0x0; ck < cj; ck += 0x2)
                    ci[ci['length']] = parseInt(ch['substr'](ck, 0x2), 0x10);
        return ci;
    },
    this.Encrypt = function (ch, ci) {
        var h0 = d4
          , cj = Array(ci["length"]);
        Array[h0(0x29b)](ci, 0x0, cj, 0x0, ci["length"]);
        var ck = this["InitEnciph" + 'er'](ch);
        this['EncryptBlo' + 'ck'](cj);
        var cl = Array(0x20);
        this["Dofinal"](cl);
        var cm = ck["getX"]()['toBigInteg' + 'er']()['toRadix'](0x10);
        for (ck = ck['getY']()['toBigInteg' + 'er']()['toRadix'](0x10); cm["length"] < 0x40; )
            cm = '0' + cm;
        for (; ck["length"] < 0x40; )
            ck = '0' + ck;
        return cm += ck,
        (cj = this["GetHex"](cj)["toString"]())["length"] % 0x2 != 0x0 && (cj = '0' + cj),
        ck = cm + cj + (cl = this["GetHex"](cl)['toString']()),
        this['cipherMode'] == A["C1C3C2"] && (ck = cm + cl + cj),
        ck;
    }    
}

function t(x) {
    var  y = arguments["length"] > 0x1 && void 0x0 !== arguments[0x1] ? arguments[0x1] : "04A2C5ABFE372540F0CFAB644776B1CEC911F21739042D9FDF8326324357790DBA3E3900338DE4FFDBA48204A176D444687904422180E0B1E3AF316C4CA09AA704"
      , z = arguments['length'] > 0x2 && void 0x0 !== arguments[0x2] ? arguments[0x2] : 0x0
      , A = CryptoJS["enc"]["Utf8"]["parse"](x);
    if (A = CryptoJS['enc']["Base64"]["stringify"](A),
    A = CryptoJS["enc"]["Utf8"]["parse"](A),
    z && 0x1 === z) {
        if ((y = y['replace'](/❤/g, '0')[cR(0x50f)](/★/g, '1')[cR(0x50f)](/☆/g, '2')[cR(0x50f)](/●/g, 'A')[cR(0x50f)](/○/g, 'B')[cR(0x50f)](/\*/g, 'C'))[cR(0x509)] > 0x50) {
            var B = y[cR(0x2a9)](0x0, 0x1e)['split']('')[cR(0x2e7)]()[cR(0x580)]('')
              , C = y[cR(0x2a9)](0x1e);
            y = B + C;
        } else
            y = l(y)["reverse"]()['join']('');
    }
    var D = y;
    D["length"] > 0x80 && (D = D["substr"](D["length"] - 0x80));
    var E = D["substr"](0x0, 0x40)
      , F = D["substr"](0x40)
      , G = new s(0x0)
      , H = G["CreatePoint"](E, F);
    return A = G["GetWords"](A["toString"]()),
    '04' + G["Encrypt"](H, A);
}
payload_data = t('{"token":"Epoint_WebSerivce_**##0601","params":{"categuids":"6d8c8eaa-c710-4b96-b26f-ce3dfc519b77,4bcbbec7-2428-403a-8eed-b0db5c0e01a5,","titlename":"","currpage":2,"pagesize":10}}')
console.log(payload_data)
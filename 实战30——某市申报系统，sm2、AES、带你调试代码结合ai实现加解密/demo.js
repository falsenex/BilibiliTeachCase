const { sm2 } = require('sm-crypto');
const CryptoJS = require('crypto-js');
function l(str) {
    return str.split('');
}

class SM2Encryptor {
    constructor(x) {
        this.ct = 1;
        this.sm3c3 = this.sm3keybase = this.p2 = null;
        this.key = Array(32);
        this.keyOff = 0;
        this.cipherMode = void 0x0 !== x ? x : SM2CipherMode[cQ(0x234)];
    }

    CreatePoint(x, y) {
        return { x, y };
    }

    GetWords(str) {
        return Buffer.from(str, 'utf8');
    }

    Encrypt(point, data) {
        try {
            // 组合公钥
            const publicKey = '04' + point.x + point.y;
            // 使用 sm-crypto 进行加密
            const encrypted = sm2.doEncrypt(data.toString(), publicKey, 0);
            return encrypted;
        } catch (error) {
            console.error('加密过程中出错:', error);
            throw error;
        }
    }
}

function encrypt(x) {
    const y = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] :
        "04A2C5ABFE" + "372540F0CF" + "AB644776B1" + "CEC911F217" +
        '39042D9FDF' + '8326324357' +
        "790DBA3E3900338DE4FFDBA48204A176D4446879" +
        '04422180E0' + "B1E3AF316C4CA09AA704";

    const z = arguments.length > 2 && arguments[2] !== undefined ? arguments[2] : 0x0;
    let A = Buffer.from(x, 'utf8');

    // 模拟 CryptoJS 的 Base64 编码
    A = Buffer.from(A.toString('base64'), 'utf8');

    let D = y;

    if (z && 0x1 === z) {
        if ((D = D.replace(/❤/g, '0').replace(/★/g, '1').replace(/☆/g, '2')
                .replace(/●/g, 'A').replace(/○/g, 'B').replace(/\*/g, 'C')).length > 0x50) {
            const B = D.substr(0x0, 0x1e).split('').reverse().join('');
            const C = D.substr(0x1e);
            D = B + C;
        } else {
            D = l(D).reverse().join('');
        }
    }

    if (D.length > 0x80) {
        D = D.substr(D.length - 0x80);
    }

    const E = D.substr(0x0, 0x40);
    const F = D.substr(0x40);
    const G = new SM2Encryptor(0x0);
    const H = G.CreatePoint(E, F);
    A = G.GetWords(A.toString());
    return '04' + G.Encrypt(H, A);
}

// console.log(encrypt('{"token":"Epoint_WebSerivce_**##0601","params":{"categuids":"6d8c8eaa-c710-4b96-b26f-ce3dfc519b77,4bcbbec7-2428-403a-8eed-b0db5c0e01a5,","titlename":"","currpage":2,"pagesize":10}}'));
// console.log(encrypt('{"token":"Epoint_WebSerivce_**##0601","params":{"categuids":"6d8c8eaa-c710-4b96-b26f-ce3dfc519b77,4bcbbec7-2428-403a-8eed-b0db5c0e01a5,","titlename":"","currpage":2,"pagesize":10}}').length);
function aesDecrypt(x) {
    var y = CryptoJS["enc"]["Utf8"]["parse"]("qnbpwgttcfv96fgw")
      , z = CryptoJS["enc"]["Utf8"]["parse"]("5141928399038306");
    return CryptoJS["AES"]["decrypt"](decodeURIComponent(x), y, {
        'iv': z,
        'mode': CryptoJS["mode"]["CBC"],
        'padding': CryptoJS['pad']["Pkcs7"]
    })["toString"](CryptoJS["enc"]['Utf8']);
}

// console.log(aesDecrypt("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"))




const CryptoJS = require("crypto-js");
function sig(Jd) {
    let JB = encodeURIComponent(Jd);
    for (var JP = 0, Jb = 0; Jb < JB.length; Jb++)
        JP = ((((JP << 7) - JP) +  398) + JB["charCodeAt"](Jb)),
        JP |= 0;
    return JP;
}
function f1(Jd, JP) {
    var PH = {
        J: 0x1e9,
        f: 0x296
    }
    JB = ["4","1","3","2","0"]
    Jb = 0;
    while (!![]) {
        switch (JB[Jb++]) {
        case '0':
            switch (Ju.length % 4) {
            default:
            case -0x4ff + -0x732 + 0xc31:
                return Ju;
            case 0x2277 + 0x1 * -0x1566 + -0xd10:
                return (Ju +  '===');
            case -0x902 + -0x1b86 + 0x1245 * 0x2:
                return (Ju + '==');
            case -0x1 * -0x2475 + -0x1c9e + -0x3ea * 0x2:
                return (Ju + '=');
            }
            continue;
        case '1':
            continue;
        case '2':
            if (JP)
                return Ju;
            continue;
        case '3':
            var Ju = f2(Jd, 6, function(Jp) {
                return JL["HdXfE"]["charAt"](Jp);
            });
            continue;
        case '4':
            var JE = {};
            JE["HdXfE"] = "DGi0YA7BemWnQjCl4+bR3f8SKIF9tUz/xhr2oEOgPpac=61ZqwTudLkM5vHyNXsVJ";
            var JL = JE;
            continue;
        }
        break;
    }
}
function f2(Jd, JP, JB) {
    for (var Jb, Ju, JE, JL, Jp = {}, Jv = {}, Jc = '', JD = 2, JG = 3, JN = 2, JO = [], Jw = 0, Ja = 0, Jg = 0; Jg < Jd['length']; Jg += 1)
        if (JE = Jd["charAt"](Jg), Object["prototype"]["hasOwnProperty"]["call"](Jp, JE) || (Jp[JE] = JG++, Jv[JE] = true), JL = Jc + JE, Object["prototype"]["hasOwnProperty"]["call"](Jp, JL))
            Jc = JL;
        else {
            if (Object["prototype"]["hasOwnProperty"]["call"](Jv, Jc)) {
                if (Jc["charCodeAt"](0) < 256) {
                    for (Jb = 0; Jb < JN; Jb++)
                        Jw <<= 1,
                        (Ja === (JP - 1)) ? (Ja = 0, JO["push"](JB(Jw)), Jw = 0) : Ja++;
                    for (Ju = Jc["charCodeAt"](0),Jb = 0; Jb < 8; Jb++)
                        Jw = (Jw << 1) | (1 & Ju),
                        (Ja === (JP - 1)) ? (Ja = 0, JO["push"]((JB(Jw))), Jw = 0) : Ja++,
                        Ju >>= 1;
                }
                else {
                    for (Ju = 1, Jb = 0; Jb < JN; Jb++)
                        Jw = (Jw << 1) | Ju,
                        (Ja === (JP - 1)) ? (Ja = 0, JO["push"](JB(Jw)), Jw = 0) : Ja++,
                        Ju = 0;
                    for (Ju = Jc["charCodeAt"](0), Jb = 0; Jb < 16; Jb++)
                        Jw = (Jw << 1) | (1 & Ju),
                        (Ja === (JP - 1)) ? (Ja = 0, JO["push"](JB(Jw)), Jw = 0) : Ja++,
                        Ju >>= 1;
                }
                (0 === (--JD)) && (JD = Math["pow"](2, JN),JN++),
                delete Jv[Jc];
            } else {
                for (Ju = Jp[Jc],Jb = 0; Jb < JN; Jb++)
                    Jw = (Jw << 1) | (1 & Ju),
                    (Ja === (JP - 1)) ? (Ja = 0, JO["push"](JB(Jw)), Jw = 0) : Ja++,
                    Ju >>= 1;
            }
            (0 === (--JD)) && (JD = Math["pow"](2, JN), JN++),
            Jp[JL] = JG++,
            Jc = String(JE);
        }
    if ('' !== Jc) {
        if (Object["prototype"]["hasOwnProperty"]["call"](Jv, Jc)) {
            if (Jc["charCodeAt"](0) < 256) {
                for (Jb = 0; Jb < JN; Jb++)
                    Jw <<= 1,
                    (Ja === (JP - 1)) ? (Ja = 0, JO["push"](JB(Jw)), Jw = 0) : Ja++;
                for (Ju = Jc["charCodeAt"](0),Jb = 0; Jb < 8; Jb++)
                    Jw = (Jw << 1) | (1 & Ju),
                    (Ja & (JP - 1)) ? (Ja = 0, JO["push"](JB(Jw)), Jw = 0) : Ja++,
                    Ju >>= 1;
            }
            else {
                for (Ju = 1, Jb = 0; Jb < JN; Jb++)
                    Jw = (Jw << 1) | Ju,
                    (Ja === (JP - 1)) ? (Ja = 0,JO["push"](JB(Jw)), Jw = 0) : Ja++,
                    Ju = 0;
                for (Ju = Jc["charCodeAt"](0), Jb = 0; Jb < 16; Jb++)
                    Jw = (Jw << 1) | (1 & Ju),
                    (Ja === (JP - 1)) ? (Ja = 0, JO["push"](JB(Jw)), Jw = 0) : Ja++,
                    Ju >>= 1;
            }
            (0  === (--JD)) && (JD = Math["pow"](2, JN), JN++),
            delete Jv[Jc];
        } else {
            for (Ju = Jp[Jc], Jb = 0; Jb < JN; Jb++)
                Jw = (Jw << 1) | (1 & Ju),
                (Ja === (JP - 1)) ? (Ja = 0, JO["push"](JB(Jw)), Jw = 0) : Ja++,
                Ju >>= 1;
        }
        (0 === (--JD) && (JD = Math["pow"](2, JN)), JN++);
    }
    for (Ju = 2,Jb = 0; (Jb < JN); Jb++)
        Jw = (Jw << 1) | (1 & Ju),
        (Ja === (JP - 1)) ? (Ja = 0,JO["push"](JB(Jw)), Jw = 0) : Ja++,
        Ju >>= 1;
    for (; ; ) {
        if (Jw <<= 1,(Ja === (JP - 1))) {
            JO["push"](JB(Jw));
            break;
        }
        Ja++;
    }
    return JO["join"]('');
}
function decryptByDES(ciphertext) {
    var keyHex = CryptoJS.enc.Utf8.parse("1qaz@wsx3e");
    //  ctpstp@custominfo!@#qweASD
    // direct decrypt ciphertext
    var decrypted = CryptoJS.DES.decrypt({
            ciphertext: CryptoJS.enc.Base64.parse(ciphertext),
        },
        keyHex, {
            mode: CryptoJS.mode.ECB,
            padding: CryptoJS.pad.Pkcs7,
        }
    );
    return decrypted.toString(CryptoJS.enc.Utf8);
}
function decrypt_data(data) {
    return JSON.parse(decryptByDES(data))
}

function get_para(params) {
    JP = sig(params) +  '|' + 0 +  '|' + new Date()["getTime"]() + '|1'
    Ju = f1(JP, true)
    return Ju
}

// console.log(get_para(obj['D']))





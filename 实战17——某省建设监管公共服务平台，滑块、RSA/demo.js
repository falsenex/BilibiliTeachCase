window = global;
const JSEncrypt = require('jsencrypt');
const to = 16
  , Vi = Uint8Array.from([214, 144, 233, 254, 204, 225, 61, 183, 22, 182, 20, 194, 40, 251, 44, 5, 43, 103, 154, 118, 42, 190, 4, 195, 170, 68, 19, 38, 73, 134, 6, 153, 156, 66, 80, 244, 145, 239, 152, 122, 51, 84, 11, 67, 237, 207, 172, 98, 228, 179, 28, 169, 201, 8, 232, 149, 128, 223, 148, 250, 117, 143, 63, 166, 71, 7, 167, 252, 243, 115, 23, 186, 131, 89, 60, 25, 230, 133, 79, 168, 104, 107, 129, 178, 113, 100, 218, 139, 248, 235, 15, 75, 112, 86, 157, 53, 30, 36, 14, 94, 99, 88, 209, 162, 37, 34, 124, 59, 1, 33, 120, 135, 212, 0, 70, 87, 159, 211, 39, 82, 76, 54, 2, 231, 160, 196, 200, 158, 234, 191, 138, 210, 64, 199, 56, 181, 163, 247, 242, 206, 249, 97, 21, 161, 224, 174, 93, 164, 155, 52, 26, 85, 173, 147, 50, 48, 245, 140, 177, 227, 29, 246, 226, 46, 130, 102, 202, 96, 192, 41, 35, 171, 13, 83, 78, 111, 213, 219, 55, 69, 222, 253, 142, 47, 3, 255, 106, 114, 109, 108, 91, 81, 141, 27, 175, 146, 187, 221, 188, 127, 17, 217, 92, 65, 31, 16, 90, 216, 10, 193, 49, 136, 165, 205, 123, 189, 45, 116, 208, 18, 184, 229, 180, 176, 137, 105, 151, 74, 12, 150, 119, 126, 101, 185, 241, 9, 197, 110, 198, 132, 24, 240, 125, 236, 58, 220, 77, 32, 121, 238, 95, 62, 215, 203, 57, 72])
  , Qwe = Uint32Array.from([462357, 472066609, 943670861, 1415275113, 1886879365, 2358483617, 2830087869, 3301692121, 3773296373, 4228057617, 404694573, 876298825, 1347903077, 1819507329, 2291111581, 2762715833, 3234320085, 3705924337, 4177462797, 337322537, 808926789, 1280531041, 1752135293, 2223739545, 2695343797, 3166948049, 3638552301, 4110090761, 269950501, 741554753, 1213159005, 1684763257])
  , Hi = Uint32Array.from([2746333894, 1453994832, 1736282519, 2993693404])
  , Fo = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "+",
    "/"
];
function stringToArrayBufferInUtf8(t) {
    return new TextEncoder().encode(t)
}
function padding(t) {
    if (t === null)
        return null;
    let n = to - t.length % to
      , o = new Uint8Array(t.length + n);
    return o.set(t, 0),
    o.fill(n, t.length),
    o
}

function uint8ToUint32Block(t, n=0) {
    let o = new Uint32Array(4);
    return o[0] = t[n] << 24 | t[n + 1] << 16 | t[n + 2] << 8 | t[n + 3],
    o[1] = t[n + 4] << 24 | t[n + 5] << 16 | t[n + 6] << 8 | t[n + 7],
    o[2] = t[n + 8] << 24 | t[n + 9] << 16 | t[n + 10] << 8 | t[n + 11],
    o[3] = t[n + 12] << 24 | t[n + 13] << 16 | t[n + 14] << 8 | t[n + 15],
    o
}
function doBlockCrypt(t, n) {
    let o = new Uint32Array(36);
    o.set(t, 0);
    for (let s = 0; s < 32; s++)
        o[s + 4] = o[s] ^ tTransform1(o[s + 1] ^ o[s + 2] ^ o[s + 3] ^ n[s]);
    let r = new Uint32Array(4);
    return r[0] = o[35],
    r[1] = o[34],
    r[2] = o[33],
    r[3] = o[32],
    r
}
const encryptRoundKeys = new Uint32Array([
  2615698777, 2788935463, 3497622499, 1788654098,
  4183254308, 1820784068, 2094938868, 3301063251,
  3107256341, 1594224700, 142606450, 516629961,
  788593773, 2078732848, 2980268046, 2798705885,
  1855651285, 2542085819, 1862059521, 1266859094,
  293981496, 3232145720, 1800457868, 393421813,
  3608591203, 497208042, 2254379384, 1196878423,
  598037690, 1685626069, 3662564248, 2648349557
]);
function tauTransform(t) {
    return Vi[t >>> 24 & 255] << 24 | Vi[t >>> 16 & 255] << 16 | Vi[t >>> 8 & 255] << 8 | Vi[t & 255]
}
function rotateLeft(t, n) {
    return t << n | t >>> 32 - n
}
function linearTransform1(t) {
    return t ^ rotateLeft(t, 2) ^ rotateLeft(t, 10) ^ rotateLeft(t, 18) ^ rotateLeft(t, 24)
}
function tTransform1(t) {
    let n = tauTransform(t);
    return linearTransform1(n)
}
function Sxe(e) {
    return Fo[e >> 18 & 63] + Fo[e >> 12 & 63] + Fo[e >> 6 & 63] + Fo[e & 63]
}
function Exe(e, t, n) {
    for (var o, r = [], s = t; s < n; s += 3)
        o = (e[s] << 16 & 16711680) + (e[s + 1] << 8 & 65280) + (e[s + 2] & 255),
        r.push(Sxe(o));
    return r.join("")
}
function fromByteArray(e) {
    for (var t, n = e.length, o = n % 3, r = [], s = 16383, a = 0, l = n - o; a < l; a += s)
        r.push(Exe(e, a, a + s > l ? l : a + s));
    return o === 1 ? (t = e[n - 1],
    r.push(Fo[t >> 2] + Fo[t << 4 & 63] + "==")) : o === 2 && (t = (e[n - 2] << 8) + e[n - 1],
    r.push(Fo[t >> 10] + Fo[t >> 4 & 63] + Fo[t << 2 & 63] + "=")),
    r.join("")
}
function arrayBufferToBase64(t) {
    return fromByteArray(t)
}
function utf8ArrayBufferToString(t) {
    // const n = typeof window == "undefined" ? Cd.TextDecoder : window.TextDecoder;
    return new TextDecoder("utf-8").decode(t)
}
function encrypt(t) {
    let n = stringToArrayBufferInUtf8(t)
      , o = padding(n)
      , r = o.length / to
      , s = new Uint8Array(o.length);
    if (this.mode === "cbc") {
        if (this.iv === null || this.iv.length !== 16)
            throw new Error("iv error");
        let a = this.uint8ToUint32Block(this.iv);
        for (let l = 0; l < r; l++) {
            let i = l * to
              , u = this.uint8ToUint32Block(o, i);
            a[0] = a[0] ^ u[0],
            a[1] = a[1] ^ u[1],
            a[2] = a[2] ^ u[2],
            a[3] = a[3] ^ u[3];
            let c = this.doBlockCrypt(a, this.encryptRoundKeys);
            a = c;
            for (let f = 0; f < to; f++)
                s[i + f] = c[parseInt(f / 4)] >> (3 - f) % 4 * 8 & 255
        }
    } else
        for (let a = 0; a < r; a++) {
            let l = a * to
              , i = uint8ToUint32Block(o, l)
              , u = doBlockCrypt(i, encryptRoundKeys);
            for (let c = 0; c < to; c++)
                s[l + c] = u[parseInt(c / 4)] >> (3 - c) % 4 * 8 & 255
        }
    return true ? arrayBufferToBase64(s) : utf8ArrayBufferToString(s)
}
function Jo(e, t) {
    const n = ec();
    return Oo = function(o, r) {
        o = o - 268;
        let s = n[o];
        if (Oo.QmZRnV === void 0) {
            var a = function(c) {
                const f = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/=";
                let d = ""
                  , p = "";
                for (let h = 0, x, v, b = 0; v = c.charAt(b++); ~v && (x = h % 4 ? x * 64 + v : v,
                h++ % 4) ? d += String.fromCharCode(255 & x >> (-2 * h & 6)) : 0)
                    v = f.indexOf(v);
                for (let h = 0, x = d.length; h < x; h++)
                    p += "%" + ("00" + d.charCodeAt(h).toString(16)).slice(-2);
                return decodeURIComponent(p)
            };
            Oo.lgkIGe = a,
            e = arguments,
            Oo.QmZRnV = !![]
        }
        const l = n[0]
          , i = o + l
          , u = e[i];
        return u ? s = u : (s = Oo.lgkIGe(s),
        e[i] = s),
        s
    }
    ,
    Oo(e, t)
}
function u$e(e) {
    const t = Jo
      , n = new JSEncrypt();
    n['setPublicKey']("MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC29miF1Wp9XlhCECo+FYpCHad1ipEMgXf4IdgYjMIQwczzo9GXdcZ4eeV+9lkh6+aTqzzU843rdkMt0vrSnujU+GOuDPLfa5LZ6SfanAoysi6xxTX02Xizb3k+Z1USIzm9QAwE+SR1AQ78rGTRFHWFu7OGPkVNeF+vrX3inQTiawIDAQAB");
    const o = 117
      , r = Math["ceil"](e["length"] / o);
    let s = [];
    for (let a = 0; a < r; a++) {
        const l = e["slice"](a * o, (a + 1) * o)
          , i = n["encrypt"](l);
        s["push"](i)
    }
    return s.join(",")
}
function getParams(obj) {
    obj_str = JSON.stringify(obj);
    return u$e(encrypt(obj_str))
}
// '{"pageNum":1,"pageSize":10,"certificateType":"","name":"","slideId":"1374351097312837632","key":"query","width":210}'
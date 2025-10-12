const crypto = require('crypto');
r = '-----BEGIN PRIVATE KEY-----\r\nMIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQg97vQNbtBDpUhbtSn\r\nPmy5X9/7jbcNsQbJDqc3Ek2Oa4ihRANCAASDBOF6O6tir3srNCUQHZuFErsLw5L8\r\nGiArLGiKb4ZNsHrIT5O8hCQbhtYUnikahnMbg+A/7ZFUIKEBMx7bzo3d\r\n-----END PRIVATE KEY-----\r\n'
t = '-----BEGIN CERTIFICATE-----\nMIIEfTCCBCKgAwIBAgIUXWdS2tzmSoewCWfKFyiWMrJqs/0wCgYIKoZIzj0EAwIw\nMTELMAkGA1UEBhMCQ04xIjAgBgNVBAMMGXRpY2tldF9ndWFyZF9jYV9lY2RzYV8y\nNTYwIBcNMjIxMTE4MDUyMDA2WhgPMjA2OTEyMzExNjAwMDBaMCQxCzAJBgNVBAYT\nAkNOMRUwEwYDVQQDEwxlY2llcy1zZXJ2ZXIwWTATBgcqhkjOPQIBBggqhkjOPQMB\nBwNCAASE2llDPlfc8Rq+5J5HXhg4edFjPnCF3Ua7JBoiE/foP9m7L5ELIcvxCgEx\naRCHbQ8kCCK/ArZ4FX/qCobZAkToo4IDITCCAx0wDgYDVR0PAQH/BAQDAgWgMDEG\nA1UdJQQqMCgGCCsGAQUFBwMBBggrBgEFBQcDAgYIKwYBBQUHAwMGCCsGAQUFBwME\nMCkGA1UdDgQiBCABydxqGrVEHhtkCWTb/vicGpDZPFPDxv82wiuywUlkBDArBgNV\nHSMEJDAigCAypWfqjmRIEo3MTk1Ae3MUm0dtU3qk0YDXeZSXeyJHgzCCAZQGCCsG\nAQUFBwEBBIIBhjCCAYIwRgYIKwYBBQUHMAGGOmh0dHA6Ly9uZXh1cy1wcm9kdWN0\naW9uLmJ5dGVkYW5jZS5jb20vYXBpL2NlcnRpZmljYXRlL29jc3AwRgYIKwYBBQUH\nMAGGOmh0dHA6Ly9uZXh1cy1wcm9kdWN0aW9uLmJ5dGVkYW5jZS5uZXQvYXBpL2Nl\ncnRpZmljYXRlL29jc3AwdwYIKwYBBQUHMAKGa2h0dHA6Ly9uZXh1cy1wcm9kdWN0\naW9uLmJ5dGVkYW5jZS5jb20vYXBpL2NlcnRpZmljYXRlL2Rvd25sb2FkLzQ4RjlD\nMEU3QjBDNUE3MDVCOTgyQkU1NTE3MDVGNjQ1QzhDODc4QTguY3J0MHcGCCsGAQUF\nBzAChmtodHRwOi8vbmV4dXMtcHJvZHVjdGlvbi5ieXRlZGFuY2UubmV0L2FwaS9j\nZXJ0aWZpY2F0ZS9kb3dubG9hZC80OEY5QzBFN0IwQzVBNzA1Qjk4MkJFNTUxNzA1\nRjY0NUM4Qzg3OEE4LmNydDCB5wYDVR0fBIHfMIHcMGygaqBohmZodHRwOi8vbmV4\ndXMtcHJvZHVjdGlvbi5ieXRlZGFuY2UuY29tL2FwaS9jZXJ0aWZpY2F0ZS9jcmwv\nNDhGOUMwRTdCMEM1QTcwNUI5ODJCRTU1MTcwNUY2NDVDOEM4NzhBOC5jcmwwbKBq\noGiGZmh0dHA6Ly9uZXh1cy1wcm9kdWN0aW9uLmJ5dGVkYW5jZS5uZXQvYXBpL2Nl\ncnRpZmljYXRlL2NybC80OEY5QzBFN0IwQzVBNzA1Qjk4MkJFNTUxNzA1RjY0NUM4\nQzg3OEE4LmNybDAKBggqhkjOPQQDAgNJADBGAiEAqMjT5ADMdGMeaImoJK4J9jzE\nLqZ573rNjsT3k14pK50CIQCLpWHVKWi71qqqrMjiSDvUhpyO1DpTPRHlavPRuaNm\nww==\n-----END CERTIFICATE-----'
A = function(t) {
    var e = new window.ZTJssign.X509;
    e.readCertPEM(t);
    var r = e.getPublicKey().getPublicKeyXYHex();
    return "02".concat(r.x)
}

o = function(t, e, r) {
    if (r || 2 == arguments.length)
        for (var n, i = 0, o = e.length; i < o; i++)
            (n || !(i in e)) && (!n && (n = Array.prototype.slice.call(e, 0, i)),
            n[i] = e[i]);
    return t.concat(n || Array.prototype.slice.call(e))
}
i = function(t, e) {
            var r = "function" == typeof Symbol && t[Symbol.iterator];
            if (!r)
                return t;
            var n, i, o = r.call(t), s = [];
            try {
                for (; (void 0 === e || e-- > 0) && !(n = o.next()).done; )
                    s.push(n.value)
            } catch (t) {
                i = {
                    error: t
                }
            } finally {
                try {
                    n && !n.done && (r = o.return) && r.call(o)
                } finally {
                    if (i)
                        throw i.error
                }
            }
            return s
        }
a = function(t) {
    return Uint8Array.from((t.match(/.{1,2}/g) || []).map(function(t) {
        return parseInt(t, 16)
    }))
};
I = function(t, e) {
    var r, n, u, c, h, f = A(e),
        d = null === (h = window.ZTJssign.KEYUTIL.getKey(t)) || void 0 === h ? void 0 : h.prvKeyHex,

        l = new window.ZTEC.ec("p256"),
        p = new Uint8Array(l.keyFromPrivate(d, "hex").derive(l.keyFromPublic(f, "hex").getPublic()).toArray("be", 32));
    return r = new Uint8Array,
    n = p,
    u = new Uint8Array,
    c = 32,
    function(t, e, r) {
        void 0 === r && (r = 32);
        for (var n = new Uint8Array, u = "", c = 0; n.length < r; ) {
            c++;
            var h, f = Uint8Array.from(o(o(o([], i(Array.from(Uint8Array.from(a(u)))), !1), i(Array.from(e)), !1), [c], !1));
            h = a(t),
            u = s(h, f),
            n = Uint8Array.from(o(o([], i(Array.from(n)), !1), i(Array.from(Uint8Array.from(a(u)))), !1))
        }
        return Uint8Array.from(n.slice(0, r))
    }(function(t, e) {
        return (!t || 0 === t.length) && (t = new Uint8Array(32)),
        s(t, e)
    }(r, n), u, c)
}

x = I(r,t)
st1 = 'ticket=hash.Ik73GjKDIrgBITwPYkPEkxXhqybbbKWR+UvDCZAI2bA=&path=/aweme/v1/web/comment/list/&timestamp=1742567038'
x ={
    "0": 187,
    "1": 254,
    "2": 5,
    "3": 136,
    "4": 136,
    "5": 194,
    "6": 199,
    "7": 113,
    "8": 86,
    "9": 48,
    "10": 126,
    "11": 233,
    "12": 35,
    "13": 188,
    "14": 243,
    "15": 236,
    "16": 163,
    "17": 4,
    "18": 127,
    "19": 183,
    "20": 172,
    "21": 51,
    "22": 232,
    "23": 210,
    "24": 0,
    "25": 228,
    "26": 134,
    "27": 217,
    "28": 149,
    "29": 95,
    "30": 19,
    "31": 95
} //？？？怎么生成
const keyBuffer = Buffer.from(Object.values(x));
s = hmacSha256Sign = function(key, data) {
    // 创建 HMAC 对象，指定使用 SHA256 算法和传入的密钥
    const hmac = crypto.createHmac('sha256', keyBuffer);
    // 更新 HMAC 对象的数据
    hmac.update(data);
    // 计算签名并以十六进制字符串形式返回
    return hmac.digest('hex');
}
//ticket  在localStorage
// fun2   === hmacSha256Sign
// hmacSha256Sign生成结果fun2(arg1,arg2)
hex_str = hmacSha256Sign(arg1,arg2)
var y = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
fun3 = function x(t) {
    var e, r, i = "";
    for (e = 0; e + 3 <= t.length; e += 3)
        r = parseInt(t.substring(e, e + 3), 16),
        i += y.charAt(r >> 6) + y.charAt(63 & r);
    e + 1 == t.length ? (r = parseInt(t.substring(e, e + 1), 16),
    i += y.charAt(r << 2)) : e + 2 == t.length && (r = parseInt(t.substring(e, e + 2), 16),
    i += y.charAt(r >> 2) + y.charAt((3 & r) << 4));
    for (; (3 & i.length) > 0; )
        i += "=";
    return i
}
req_sign = fun3(hex_str)
// req_sign =？？
A = {
    // localStorage
    "ts_sign": "ts.2.c193d93b0b2a9ca29de9c5f6aeed9e6be0c95ee4fddcda901e771faf99aafeafc4fbe87d2319cf05318624ceda14911ca406dedbebeddb2e30fce8d4fa02575d",
    "req_content": "ticket,path,timestamp", //固定的
    "req_sign": "sGkurk/rTbKaPGMl6mRbdzjtC5FB/alosgebAgU70Qk=", //？？
    "timestamp": 1742566423 //时间戳
}

fun1 = window.ZTJssign.utf8tob64(t)//标准的bs64
bd = fun1(JSON.stringify(A))
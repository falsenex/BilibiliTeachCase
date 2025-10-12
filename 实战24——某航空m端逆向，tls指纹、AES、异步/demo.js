function get_transactionId() {
    return "05" + String((new Date).toISOString().replace(/[T\-\:]/g, "").replace(/\.[\d]{3}Z/, "")) + String(Math.ceil(1e4 * Math.random()));
}

//////////////////////////////////////////////////////////////////////////////////////////////////////
function get_refer__1036(ZM) {
    aF = 931
    Zx = {
        "protocol": "https:",
        "host": "m.ceair.com",
        "hostname": "m.ceair.com",
        "port": "",
        "pathname": "/m-base/sale/shoppingv2",
        "search": "",
        "hash": "",
        "P": "https://m.ceair.com/m-base/sale/shoppingv2"
    }
    ZV = {
        "z":function(Zx) {
            // var vF = pa,
                ZM, ZJ = -0x36 + -0x1 * 0x1e2d + 0x1e63;
            for (ZM = 0x159a + 0x4 * 0x78d + -0x19e7 * 0x2; (ZM < Zx["length"]); ZM++)
                ZJ = ((ZJ << 7) - ZJ) + 398 + Zx["charCodeAt"](ZM),
                ZJ |= 0x138 + -0x1045 + 0xf0d;
            return ZJ;
        }
    }
    var Zg = "https://m.ceair.com/m-base/sale/shoppingv2";
    ZM = JSON.stringify(ZM)
    Zg = encodeURIComponent(Zg + ZM);
    ZG = ZV['z'](Zg);
    ZG = ZG + '|' + 0 + '|' + new Date()["getTime"]() + '|1'
    console.log(ZG)
    // ZG = "103580191|0|1750756486180|1"
    ZM = {
        'v': function(ZJ, ZK, ZY) {
            // var Pk = Pc;
            // if (Ab[Pk(cz.A4)](null, ZJ))
            //     return '';
            var ZG, Zg, ZU, ZS = {}, ZW = {}, Zw = '', Zn = '', p0 = '', p1 = -0x25f6 + 0x2 * 0x6d + 0x1 * 0x217b + aF, p2 = -0x920 + 0x8e1 * 0x2 + -0x89f * 0x1, p3 = 0x5 * 0x40d + -0x1a5 * -0x14 + 0x3523 * -0x1, p4 = [], p5 = 0x34 * 0x11 + -0x1699 + 0x179 * 0xd, p6 = 0x9 * -0x29e + -0x35 * -0x5 + 0x12e2 + aF;
            for (ZU = -0x3d * -0x1d + -0x1 * -0x10e5 + -0x1b71 + aF; (ZU < ZJ["length"]); ZU += -0x151a + 0x17ad + -0x635 + aF)
                if (Zw = ZJ["charAt"](ZU),
                Object["prototype"]["hasOwnProperty"]["call"](ZS, Zw) || (ZS[Zw] = p2++,
                ZW[Zw] = !(0x16df + 0x13c1 + -0x2aa0)),
                Zn = (p0 + Zw),
                Object["prototype"]["hasOwnProperty"]["call"](ZS, Zn))
                    p0 = Zn;
                else {
                    if (Object["prototype"]["hasOwnProperty"]["call"](ZW, p0)) {
                        if ((p0["charCodeAt"](-0xba * 0x1d + 0x19a1 + 0x2 * -0x419 + aF) < 256)) {
                            for (ZG = -0x258a + 0x2ba * 0x6 + 0x118b + aF; (ZG < p3); ZG++)
                                p5 <<= 0x816 + -0xa78 + -0x40 * 0x5 + aF,
                                (p6 === (ZK - (-0x66a + 0xe0b + -0xb43 + aF))) ? (p6 = -0x7 * 0x515 + -0x1 * 0x1ef4 + 0x162d * 0x3,
                                p4["push"](ZY(p5)),
                                p5 = 0xb * -0x136 + -0x1bfd + -0x19 * -0x1a7) : p6++;
                            for (Zg = p0["charCodeAt"](-0x1581 + 0x2076 + -0xe98 + aF),
                            ZG = 0x1ae3 * -0x1 + -0xc65 * 0x1 + 0xc * 0x346; (ZG < 8); ZG++)
                                p5 = ((p5 <<  1) | (1 & Zg)),
                                (p6 === (ZK  - 1)) ? (p6 = -0xfd * 0x17 + 0x106 + 0x101 * 0x12 + aF,
                                p4["push"](ZY(p5)),
                                p5 = -0x1114 + -0x10a7 + 0x1e18 + aF) : p6++,
                                Zg >>= -0x595 + 0x1025 * -0x1 + 0x1218 + aF;
                        } else {
                            for (Zg = 0xddf * 0x1 + 0x1 * -0x24b0 + 0xb69 * 0x2,
                            ZG = -0x2523 + 0x66b * 0x1 + 0x1eb8; Ab[Pk(cz.Ai)](ZG, p3); ZG++)
                                p5 = Ab[Pk(cz.Aa)](Ab[Pk(cz.Ac)](p5, 0xe8d + 0x68e * -0x1 + -0xba1 + aF), Zg),
                                Ab[Pk(cz.Az)](p6, Ab[Pk(cz.AC)](ZK, 0x8 * 0x15a + -0x7f4 * 0x2 + 0x3 * 0x1b3)) ? (p6 = -0x1089 + -0x202c + 0xf06 * 0x3 + aF,
                                p4[Pk(cz.AB)](Ab[Pk(cz.Aq)](ZY, p5)),
                                p5 = 0xafd + -0x1e9e + 0xffe + aF) : p6++,
                                Zg = -0x7f9 * -0x2 + 0x919 * 0x1 + 0x859 * -0x3;
                            for (Zg = p0[Pk(cz.Ae)](0x1e1 * 0xb + -0x721 + -0x112d + aF),
                            ZG = -0x147a + 0x18c5 + -0x7ee + aF; Ab[Pk(cz.AO)](ZG, -0x491 + 0x1 * 0x24dc + -0x203b * 0x1); ZG++)
                                p5 = Ab[Pk(cz.Aa)](Ab[Pk(cz.AX)](p5, 0x1 * -0x14f6 + 0x107 + -0x104d * -0x1 + aF), Ab[Pk(cz.AQ)](0x3 * 0x199 + -0xea1 + 0x9d7, Zg)),
                                Ab[Pk(cz.AE)](p6, Ab[Pk(cz.AV)](ZK, -0x1573 + -0x1 * -0x1231 + 0x4 * -0x18 + aF)) ? (p6 = -0x14be + 0x1 * -0x1514 + 0x262f + aF,
                                p4[Pk(cz.AB)](Ab[Pk(cz.AI)](ZY, p5)),
                                p5 = -0x1abb * 0x1 + 0x1 * -0xf21 + 0x1 * 0x29dc) : p6++,
                                Zg >>= 0x1545 + -0x12 * -0x19c + 0x35df * -0x1 + aF;
                        }
                        ((0x1 * -0x12df + -0x1a88 + 0x29c4 + aF) === --p1) && (p1 = Math["pow"](-0x265 * -0x9 + 0x2 * 0x943 + 0x315 * -0xd, p3),
                        p3++),
                        delete ZW[p0];
                    } else {
                        for (Zg = ZS[p0],
                        ZG = -0x13 * 0x1fa + -0x1a5 * 0x4 + 0x287f + aF; (ZG < p3); ZG++)
                            p5 = ((p5  << (0x14e2 + -0x3 * -0x70d + -0x2dab + aF)) | ((0x1446 + -0x2 * -0x7b0 + -0x16d * 0x19) & Zg)),
                            (p6 === (ZK - (0x7db * 0x1 + 0x3 * -0x5f + -0xa60 + aF))) ? (p6 = 0x1 * 0x26bf + -0x55 * 0x5 + 0x65 * -0x5e,
                            p4["push"](ZY(p5)),
                            p5 = -0xa44 + 0xa9 * 0x21 + -0xb85) : p6++,
                            Zg >>= 0x1a46 + 0xec8 + -0x290d;
                    }
                    ((0x1d0a + -0x389 + -0x5 * 0x5d4 + aF) ===  --p1) && (p1 = Math["pow"](-0x1 * 0x1945 + -0x2275 + -0x1 * -0x3819 + aF, p3),
                    p3++),
                    ZS[Zn] = p2++,
                    p0 = String(Zw);
                }
            if ('' !== p0) {
                if (Object["prototype"]["hasOwnProperty"]["call"](ZW, p0)) {
                    if (Ab[Pk(cz.Ag)](p0[Pk(cz.AU)](0xc31 * 0x1 + -0x142c + 0x7fb), -0x1 * 0x1bff + 0x1 * -0x13d + 0x24 * 0xd7)) {
                        for (ZG = -0x1178 + 0x2116 + 0x1f * -0x9f + aF; Ab[Pk(cz.AS)](ZG, p3); ZG++)
                            p5 <<= -0x1 * -0x254d + -0xd * -0xef + -0x316f,
                            Ab[Pk(cz.AW)](p6, Ab[Pk(cz.Aw)](ZK, -0x4cb * -0x5 + -0x1687 * -0x1 + -0x2e7d)) ? (p6 = -0x1 * 0x17d5 + 0x1 * 0x87c + 0x1 * 0xf59,
                            p4[Pk(cz.An)](Ab[Pk(cz.Ax)](ZY, p5)),
                            p5 = 0x1 * -0x247b + 0x7cc * -0x2 + 0x3413) : p6++;
                        for (Zg = p0[Pk(cz.b0)](-0x1d7e + -0x10e3 + 0x2abe * 0x1 + aF),
                        ZG = 0x1ded + -0x1 * 0x1a29 + -0x3c4; Ab[Pk(cz.Ag)](ZG, 0x1 * -0x1c9d + -0x164 * 0x1 + -0x21 * -0xe9); ZG++)
                            p5 = Ab[Pk(cz.AR)](Ab[Pk(cz.b1)](p5, 0x241f + 0xde9 + -0x3207), Ab[Pk(cz.b2)](0x1059 + 0xb32 + -0x1b8a, Zg)),
                            Ab[Pk(cz.b3)](p6, Ab[Pk(cz.b4)](ZK, -0x148b + 0x5d * -0x26 + 0x1eb7 + aF)) ? (p6 = -0x2055 + 0x1c63 + -0xca * -0x5,
                            p4[Pk(cz.AB)](Ab[Pk(cz.b5)](ZY, p5)),
                            p5 = 0x1d * -0x8 + -0x8e1 + 0x9c9) : p6++,
                            Zg >>= -0x10d9 + 0x6f5 + 0x642 + aF;
                    } else {
                        for (Zg = 0x15bf * 0x1 + 0x1 * -0x1c5e + 0x2fd + aF,
                        ZG = 0x1 * 0xa33 + -0x1d13 * 0x1 + 0x1 * 0x12e0; Ab[Pk(cz.b6)](ZG, p3); ZG++)
                            p5 = Ab[Pk(cz.b7)](Ab[Pk(cz.b8)](p5, 0x4 * -0x100 + 0x313 * -0xb + 0x222f + aF), Zg),
                            Ab[Pk(cz.AD)](p6, Ab[Pk(cz.b9)](ZK, 0xd * -0xd6 + -0x1012 + 0x8fb * 0x3)) ? (p6 = 0x1ae * 0x1 + 0x1 * 0x1309 + -0x1 * 0x14b7,
                            p4[Pk(cz.AB)](Ab[Pk(cz.bA)](ZY, p5)),
                            p5 = 0x1 * 0xd3f + -0x2685 + -0xa * -0x287) : p6++,
                            Zg = -0xd61 + -0x10e + 0x566 * 0x2 + aF;
                        for (Zg = p0[Pk(cz.AU)](0xb54 + 0xc5 * -0x9 + 0xa1 * -0x7),
                        ZG = -0x2 * -0x89b + 0x3 * 0xac1 + -0x11 * 0x2e9; Ab[Pk(cz.bb)](ZG, 0x322 * 0x7 + 0x52b + -0x1eac + aF); ZG++)
                            p5 = Ab[Pk(cz.bZ)](Ab[Pk(cz.bp)](p5, 0x11 * -0x19 + -0x1 * -0xad3 + -0xccc + aF), Ab[Pk(cz.bP)](-0x21c7 * -0x1 + -0x10b1 * -0x2 + 0x266 * -0x1c, Zg)),
                            Ab[Pk(cz.by)](p6, Ab[Pk(cz.bv)](ZK, -0xd6 * -0x1 + -0x1ef5 + -0x1 * -0x1a7d + aF)) ? (p6 = -0x22a3 * -0x1 + -0x1ab * 0xd + 0x2 * -0x67a,
                            p4[Pk(cz.AB)](Ab[Pk(cz.br)](ZY, p5)),
                            p5 = -0x123f + -0x61 * -0x3e + 0x17b * -0x6 + aF) : p6++,
                            Zg >>= 0x1 * -0xe40 + 0x8a5 + 0x1f9 + aF;
                    }
                    Ab[Pk(cz.bm)](-0x7 * 0x7f + -0x95 * 0x1c + 0x1022 + aF, --p1) && (p1 = Math[Pk(cz.As)](-0x2d5 + -0x349 * 0x7 + -0x1 * -0x1633 + aF, p3),
                    p3++),
                    delete ZW[p0];
                } else {
                    for (Zg = ZS[p0],
                    ZG = 0x3 * -0x189 + 0xe9 * -0x23 + -0x123b * -0x2; (ZG < p3); ZG++)
                        p5 = ((p5 << (-0x1b45 + -0x4 * 0x33e + 0x66 * 0x65)) | ((-0x8b * -0x1f + -0x10c + -0x3 * 0x679 + aF) & Zg)),
                        (p6 === (ZK - (-0x1 * 0x31a + -0x2 * -0xfb3 + -0x1fee + aF))) ? (p6 = -0x1 * -0x23ff + 0x16 * 0x168 + 0x1 * -0x42ef,
                        p4["push"](ZY(p5)),
                        p5 = -0xd3 * -0x8 + -0x20a + -0x48e) : p6++,
                        Zg >>= 0x1 * -0x3c0 + -0xc2c + 0xfed;
                }
                ((-0x1035 + 0x1 * 0xd58 + -0xc6 + aF) === --p1) && (p1 = Math["pow"](-0x87c + 0x1d90 + -0x18b5 + aF, p3),
                p3++);
            }
            for (Zg = -0x13b9 + -0x8 * -0x477 + -0x4 * 0x4e8 + aF,
            ZG = -0xf7f + 0x277 + 0xd * 0xb9 + aF; (ZG < p3); ZG++)
                p5 = ((p5 << (-0x11f2 + -0x1 * -0xb76 + 0x67d)) | ((-0xadd * 0x1 + 0x1 * 0x26e7 + -0x1 * 0x1c09) & Zg)),
                (p6 === (ZK - (0x18d5 + 0x586 * 0x3 + -0x2966))) ? (p6 = -0x1 * 0x2063 + 0x1 * -0x1fb5 + 0x4018,
                p4["push"](ZY(p5)),
                p5 = 0x153 * -0x2 + 0x531 * -0x5 + -0x3 * -0x989) : p6++,
                Zg >>= 0x1633 + 0x5dc + -0x1c0e;
            for (; ; ) {
                if (p5 <<= 0x1 * 0x158e + 0x250c + 0x85f * -0x7,
                (p6 ===  (ZK - (0x41 + -0x269e + 0x11 * 0x20b + aF)))) {
                    p4["push"](ZY(p5));
                    break;
                }
                p6++;
            }
            return p4["join"]('');
        }
    }
    AG = {
        'y': function(ZJ, ZK) {
                var ci = {
                    A4: 0x745,
                    A5: 0x30d
                }
                var ZY = ZM['v'](ZJ, -0x8f2 + -0x1 * 0x1d0 + -0x1f * -0x3b + aF, function(ZG) {
                    // var Pt = Pd;
                    return "DGi0YA7BemWnQjCl4+bR3f8SKIF9tUz/xhr2oEOgPpac=61ZqwTudLkM5vHyNXsVJ"["charAt"](ZG);
                });
                return ZY;
            }
    }
    ZW = AG['y'](ZG, !(-0x1c25 + 0xe3a + -0x178 * -0x7 + aF))
    refer__1036 = ZW
    return refer__1036
}
// //////////////////////////////////////////////////////////////////////////////////////////////////
function bl() {
    return "SLo-Zt9rm8k" ? "c=B|" + "SLo-Zt9rm8k" : ""
}
function Df() {
    try {
        var t = ba();
        if (!t)
            return;
        if (!kf || !Cf)
            return "base64#".concat(Sf(t));
        var e = Cf
          , n = e.sm2Enc
          , r = (0,
        e.sm4Enc)(t, kf)
          , i = n(kf, li.encPubKey);
        if (r && i)
            return "gmjs#".concat(i, "#").concat(r)
    } catch (a) {}
}
Y = function() {
    function t(t) {
        return t < 0 ? NaN : t <= 30 ? 0 | Math.random() * (1 << t) : t <= 53 ? (0 | Math.random() * (1 << 30)) + (0 | Math.random() * (1 << t - 30)) * (1 << 30) : NaN
    }
    function e(t, e) {
        for (var n = t.toString(16), r = e - n.length, i = "0"; r > 0; r >>>= 1,
        i += i)
            1 & r && (n = i + n);
        return n
    }
    return function(n) {
        var r = "-";
        return n && (r = ""),
        e(t(32), 8) + r + e(t(16), 4) + r + e(16384 | t(12), 4) + r + e(32768 | t(14), 4) + r + e(t(48), 12)
    }
}()
function get_X_Tingyun() {
    var a = function() {
        try {
            return Y(!0).substring(0, 16)
        } catch (dv) {}
    }()
      , o = bl();
    a && (o += ";x=" + a);
    var c = Df();
    c && (o += ";u=" + c)
    return o;
}

// console.log(get_X_Tingyun())





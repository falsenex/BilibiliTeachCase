const CryptoJS = require('crypto-js');
func_chufa = function (a,b) {
    return a / b;
}
func_yushu = function (a,b) {
    return a % b;
}
func_jiafa = function (a,b) {
    return a + b;
}
func_chengfa = function (a,b) {
    return a * b;
}
function set_random(Xi) {
    var XM = {};
    XM["qTmGq"] = "function random() { [native code] }";
    var Xg = XM;
    F = -0x139d5b97 + -0xed0f55d + 0x5fd2a01a;
    // Error检测
    var XR = 1436544;
    var Xy = -0x17603115 + -0xf38cfa0f + -0x6e99ab * -0x412 + 997
        , XA = function () {
            return func_chufa(F = func_yushu(func_jiafa(func_chengfa(XR, F), Xi), Xy), Xy);
        };
    return XA['toString'] = function () {
        return Xg["qTmGq"];
    }, XA;
}
get_arg1_arr = function (arg1) {
    var XR = CryptoJS.MD5(arg1).toString();
    for (var XM = [], Xg = 10; Xg < 26; ++Xg)
        XM['push'](XR[Xg % XR['length']]);
    return XM;
}
function arr_paix(Xi) {
    for (var Xs = Xi["slice"](), Xj = Xs['length'] - 1; Xj >= 0; Xj--) {
        var XR = Math['floor']((Math.random() * (Xj + 1)))
          , XM = Xs[XR];
        Xs[XR] = Xs[Xj],
        Xs[Xj] = XM;
    }
    return Xs['length'],
    Xs;
}
function get_zfc() {
    var a = [1591183137, 3735516421, 91694891, 105016660, 3024613259, 3094858481, 678784961, 1670000817];
    var Xi = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
    return Xi['length'],
    Xi['push'](Math.random_() > 0.5 ? 1 : 0),
    Xi['push'](1),
    Xi['push'](Math['floor']((new Date().getTime() / 1000) % 2)),
    Xi['push'](Math.random_() > 0.5 ? 1 : 0),
    Xi['length'],
    Xi = arr_paix(Xi['concat']((function() {
            for (var Xs = [91694891,1375423787,678770358,1711727025,3095512628,1269158918,1591259993,678741349,1591185675,1589657591,1591391801,1591431809,1070775239,1481726678,1854307266,678765557,2051079477,678784961,406277495,1591756844,3451852696,678768153,1292981058,1536799862], Xj = [], XR = 0; XR < 8; ++XR)
                Xj['push'](Xs['indexOf'](a[XR]) > -(0x2 * -0xc5 + 0x5 * -0x55d + 0x1877 + 997) ? 1 : 0);
            return Xj;
    }()))),
        function (Xs) {
            Math.random = Math.random_;
            for (var Xj = 0, XR = 0; XR < Xs['length']; ++XR)
                Xj |= ((Xs[XR] ? 1 : 0) << XR);
            return Xj;
        }(Xi);
}
var encrypt = function (XM) {
        var Xg = 6;
        var x = ['T', 'J', 'P', 'g', 'l', 'M', '7', 'H', 'i', '8', 'k', '1', '0', 'h', 'O', 't', '3', 'Z', 'X', '2', '4', 'n', 'B', 'b', 'S', 'j', 'q', 'w', 'r', 'm', 'C', 'N', '6', 'p', 'I', 'E', 'e', 'u', 'x', 'Q', 'y', 'f', '/', '5', '_', '=', 'K', 'o', 'U', 'd', 'Y', 's', 'v', 'D', 'z', 'a', 'c', 'W', 'G', 'R', 'V', 'L', '9', 'A', 'F'];
        var Xy = function (XM) {
            return x[XM];
        };
        var XA, Xh, Xm, XV = {}, Xb = {}, XQ = '', Xw = '', XI = '', Xz = 2, Xf = 3, Xx = 2, XH = [], Xv = 0, XF = 0;
        for (Xm = 0; Xm < XM['length']; Xm += 1)
            if (XQ = XM["charAt"](Xm),
            Object['prototype']['hasOwnProperty']['call'](XV, XQ) || (XV[XQ] = Xf,
            Xf += 1,
            Xb[XQ] = !(0)),
            Xw = XI + XQ,
            Object['prototype']['hasOwnProperty']['call'](XV, Xw))
                XI = Xw;
            else {
                if (Object['prototype']['hasOwnProperty']['call'](Xb, XI)) {
                    if (XI['charCodeAt'](0) < 256) {
                        for (XA = 0; XA < Xx; XA++)
                            Xv <<= 1,
                            (XF == (Xg - 1)) ? (XF = 0,
                            XH['push'](Xy(Xv)),
                            Xv = 0) : XF++;
                        for (Xh = XI['charCodeAt'](0),
                        XA = 0; XA < 8; XA++)
                            Xv = ((Xv << 1) | (1 & Xh)),
                            (XF == (Xg - 1)) ? (XF = 0,
                            XH['push'](Xy(Xv)),
                            Xv = 0) : XF++,
                            Xh >>= 1;
                    } else {
                        for (Xh = 1,
                        XA = 0; XA < Xx; XA++)
                            Xv = ((Xv << 1) | Xh),
                            (XF == (Xg - 1)) ? (XF = 0,
                            XH['push'](Xy(Xv)),
                            Xv = 0) : XF++,
                            Xh = 0;
                        for (Xh = XI['charCodeAt'](0),
                        XA = 0; XA < 16; XA++)
                            Xv = ((Xv << 1) | (1 & Xh)),
                            (XF == (Xg - 1)) ? (XF = 0,
                            XH['push'](Xy(Xv)),
                            Xv = 0) : XF++,
                            Xh >>= 1;
                    }
                    (0 == --Xz) && (Xz = Math['pow'](2, Xx),
                    Xx++),
                    delete Xb[XI];
                } else {
                    for (Xh = XV[XI],
                    XA = 0; XA < Xx; XA++)
                        Xv = ((Xv << 1) | (1 & Xh)),
                        (XF == (Xg - 1)) ? (XF = 0,
                        XH['push'](Xy(Xv)),
                        Xv = 0) : XF++,
                        Xh >>= 1;
                }
                (0 == --Xz) && (Xz = Math['pow'](2, Xx),
                Xx++),
                XV[Xw] = Xf,
                Xf += -0x17bb + -0xc7 * -0x1c + 0x1f8,
                XI = String(XQ);
            }
        if ('' !== XI) {
            if (Object['prototype']['hasOwnProperty']['call'](Xb, XI)) {
                if (XI['charCodeAt'](0) < 256) {
                    for (XA = 0; XA < Xx; XA++)
                        Xv <<= -0xc3 * -0x15 + 0x4a * 0x52 + -0x27b2 * 0x1,
                        (XF == (Xg - 1)) ? (XF = -0xa67 + 0x11fc * 0x1 + -0x1 * 0x795,
                        XH['push'](Xy(Xv)),
                        Xv = 0x1 * -0xb60 + -0x1f4f + 0x2aaf) : XF++;
                    for (Xh = XI['charCodeAt'](0),
                    XA = 0; XA < 8; XA++)
                        Xv = ((Xv << 1) | (1 & Xh)),
                        (XF == (Xg - 1)) ? (XF = 0,
                        XH['push'](Xy(Xv)),
                        Xv = 0) : XF++,
                        Xh >>= 1;
                } else {
                    for (Xh = -0x8ec + -0x13a1 + 0x1c8e,
                    XA = 0; XA < Xx; XA++)
                        Xv = ((Xv << 1) | Xh),
                        (XF == (Xg - 1)) ? (XF = 0,
                        XH['push'](Xy(Xv)),
                        Xv = -0x7 * -0xd9 + -0x232 * 0x5 + 0x1 * 0x50b) : XF++,
                        Xh = -0xe95 + 0x3ed + -0x2aa * -0x4;
                    for (Xh = XI['charCodeAt'](0),
                    XA = 0; XA < 16; XA++)
                        Xv = ((Xv << 1) | (1 & Xh)),
                        (XF == (Xg - 1)) ? (XF = 0x48a + -0x1738 + 0x12ae,
                        XH['push'](Xy(Xv)),
                        Xv = 0) : XF++,
                        Xh >>= 0x1e29 + 0x225e + 0xac1 * -0x6;
                }
                (0 == --Xz) && (Xz = Math['pow'](0x973 + 0xa * -0x368 + 0x1 * 0x189f, Xx),
                Xx++),
                delete Xb[XI];
            } else {
                for (Xh = XV[XI],
                XA = -0x18a4 * -0x1 + 0xb55 + -0x23f9; XA < Xx; XA++)
                    Xv = ((Xv << 1) | (1 & Xh)),
                    (XF == (Xg - 1)) ? (XF = -0x1d03 + -0xcfd + 0x2a0 * 0x10,
                    XH['push'](Xy(Xv)),
                    Xv = -0x98f + 0x1 * -0x106b + 0x19fa) : XF++,
                    Xh >>= 0x151 * 0x1d + 0x120e + -0x1c1d * 0x2;
            }
            (0 == --Xz) && (Xz = Math['pow'](0x1a4f + 0x29 * -0x40 + -0x100d, Xx),
            Xx++);
        }
        for (Xh = 0xb40 + -0x2252 + 0x1714,
        XA = -0x1bd * 0xd + -0x209a + 0x3733; XA < Xx; XA++)
            Xv = ((Xv << 1) | (1 & Xh)),
            (XF == (Xg - 1)) ? (XF = 0x1687 + -0x33 * -0x32 + -0x207d,
            XH['push'](Xy(Xv)),
            Xv = 0) : XF++,
            Xh >>= 1;
        for (; ; ) {
            if (Xv <<= 1,XF == (Xg - 1)) {
                XH['push'](Xy(Xv));
                break;
            }
            XF++;
        }
        return XH['join']('');
}
function get_header(o) {
    I = Date.now();
    for (a = I,
        "",
        s = "",
        f = new Array(1,2,3,4,5,6,7,8,9),
        l = 0; l < 6; l++)
            d = Math.floor(9 * Math.random()),
            s += f[d];
    if (c = Number(s), p = [], 'post')
        p.push("PZTimestamp=" + a + "&Random=" + c + "&2147483647=" + encodeURIComponent(JSON.stringify(o)))
    E = p.join("&") + "&accessKey=3qXyB7uf",O = void 0,O = E.replace(/[(]/g, "%28"),
    E = O = (O = (O = (O = (O = O.replace(/[)]/g, "%29")).replace(/[']/g, "%27")).replace(/[*]/g, "%2A")).replace(/[~]/g, "%7E")).replace(/[!！]/g, "%21"),
    b = CryptoJS.MD5(E).toString();
    return {
        Timestamp: a+'',
        strMd5: b,
        Random: c+''
    }
}
function get_decode__1174(_waf_bd8ce2ce37,_waf_a86dfdc5f2,data) {
    // _waf_bd8ce2ce37 = 'bgLo7lj/x3EfCe5ZjupzyVB8JCsuQwGdwLw2tY0GG2o=';
    // _waf_a86dfdc5f2 = 1756103964432;
    method = 'POST'
    key_yan = '28178cb220'
    api = 'api.pzds.com/api/web-client/v2/public/goodsPublic/page'
    data = JSON.parse(data)
    // data = {"order":"ASC","sort":null,"page":3,"pageSize":21,"action":{"gameId":"8","goodsCatalogueId":6,"merchantMark":null,"keywords":[],"searchWords":[],"searchPropertyIds":[],"unionGameIds":[],"goodsSearchActions":[]}}
    datastr = JSON.stringify(data)
    header = get_header(data);
    arg1 = encodeURIComponent(_waf_bd8ce2ce37 + method.toLocaleLowerCase() + key_yan + api) + encodeURIComponent(datastr)
    arg2 = encodeURIComponent(_waf_bd8ce2ce37 + method.toLocaleLowerCase() + key_yan + api)
    arg1_arr = get_arg1_arr(arg1)
    arg1_arr_copy = arg1_arr
    if (arg1 != arg2) {
        arg1_arr = get_arg1_arr(arg2)
    }
    // 固定0.6398672226746067
    Math.random_ = Math.random;
    Math.random = set_random(1693719615);
    n1 = arr_paix(arg1_arr_copy)["join"]('')["toLowerCase"]();
    n2 = arr_paix(arg1_arr)["join"]('')["toLowerCase"]();
    arr = ([n1,n2,get_zfc(),new Date().getTime()+'',_waf_bd8ce2ce37,_waf_a86dfdc5f2,'2105840676a198dee460b7']).join('|')
    decode__1174 = key_yan + "-" + encrypt(arr)
    return {
        'headers': header,
        'decode__1174':decode__1174
    }
}
// console.log(get_decode__1174('1JpIQLs8k07eMEqiONB94LWgeBietyVeVU88qmnUlqY=',1756106309136))


GD = function(k3) {
    // k1 = "DGi0YA7BemWnQjCl4+bR3f8SKIF9tUz/xhr2oEOgPpac=61ZqwTudLkM5vHyNXsVJ"
    k1 = "DGi0YA7BemWnQjCl4_bR3f8SKIF9tUz/xhr2oEOgPpac=61ZqwTudLkM5vHyNXsVJ"
    return k1["charAt"](k3);
}
W = function(GI, Gr, GD) {
    // var yk = k;
    // if (Gq[yk(uE.d6)](null, GI)) return "";
    var k0, k1, k2, k3 = {},
    k4 = {},
    k5 = "",
    k6 = "",
    k7 = "",
    k8 = -8247 + -8078 + 16327,
    k9 = -8813 * 1 + 1140 + 2 * 3763 + 150,
    d = 1 * -5540 + -1887 * -2 + 4 * 442,
    kd = [],
    kx = -6898 + -2956 + 4927 * 2,
    kG = 19 * 226 + -1 * 7583 + 3289;
    for (k2 = -480 * -2 + -259 * 15 + 2925; k2 < GI['length']; k2 += -7282 + -1085 + 8218 * 1 + 150) if (k5 = GI['charAt'](k2), Object['prototype']['hasOwnProp' + 'erty']['call'](k3, k5) || (k3[k5] = k9++, k4[k5] = !(9164 + -2 * -297 + -9908 + 150)), k6 = k7 + k5, Object['prototype']['hasOwnProp' + 'erty']['call'](k3, k6)) k7 = k6;
    else {
        if (Object['prototype']['hasOwnProp' + 'erty']['call'](k4, k7)) {
            if (k7['charCodeAt']( - 71 * 57 + -4064 + 8111) < 6020 + -5826 + 62) {
                for (k0 = 4153 + 4909 * 1 + -9062; k0 < d; k0++) kx <<= -5208 + -4443 + 9652,
                (kG === (Gr - (3531 + -7 * -368 + 6256 * -1 + 150))) ? (kG = -8803 * -1 + 7710 + -16513, kd['push'](GD(kx)), kx = -5949 + 6910 + -961) : kG++;
                for (k1 = k7['charCodeAt']( - 2079 + 1 * 790 + 1139 + 150), k0 = 6416 * 1 + -983 * -3 + -9515 + 150; (k0 < (45 * 123 + -2 * -4471 + 21 * -689)); k0++) kx = ((kx << -3539 + 5433 + -2043 + 150) | (-9750 + 1 * -6695 + -1 * -16446 & k1)),
                (kG === (Gr - ( - 4437 + 9965 + -5677 * 1 + 150))) ? (kG = 11 * 311 + -1578 + -1843, kd['push'](GD(kx)), kx = -1669 + -6042 + 1 * 7711) : kG++,
                k1 >>= 400 * 8 + 2044 + -5393 * 1 + 150
            } else {
                for (k1 = 1 * 5033 + 1 * 9697 + -14729, k0 = 5422 + 7712 + 33 * -398; k0 < d; k0++) kx = (kx << (8228 + 7417 * 1 + -7822 * 2)) | k1,
                (kG === ((Gr - (17 * -198 + -7 * 461 + 1 * 6594)))) ? (kG = -1292 * 4 + 4227 + 1 * 941, kd['push'](GD(kx)), kx = -47 * 143 + -2096 + 8667 + 150) : kG++,
                k1 = 1709 + 10 * 17 + -1879;
                for (k1 = k7['charCodeAt'](49 * 83 + 55 * -157 + 571 * 8), k0 = 7603 + -6389 * -1 + -14142 + 150; (k0 < (1 * 1416 + -2095 + 545 + 150)); k0++) kx = (kx << (958 + 57 * 39 + 1 * -3330 + 150)) | -6735 + -422 + 2336 * 3 + 150 & k1,
                kG == Gr - ( - 4048 + -8937 + 12986) ? (kG = 15 * 427 + 3272 + -9677, kd['push'](GD(kx)), kx = 580 * -11 + -4428 + 1 * 10658 + 150) : kG++,
                k1 >>= 8323 + -43 * 94 + 1 * -4280
            }
            (( - 991 * 3 + 894 + -1 * -1929 + 150) ===  (--k8)) && (k8 = Math['pow']( - 8500 + -4009 + -1 * -12361 + 150, d), d++),
            delete k4[k7]
        } else {
            for (k1 = k3[k7], k0 = 5663 + 97 * 17 + 574 * -13 + 150; k0 < d; k0++) kx = (kx << (2874 + 1596 + 4619 * -1 + 150)) | ((8335 + 4547 * -1 + -3787 * 1) & k1),
            (kG === ((Gr - (-8468 + 5042 * 1 + 113 * 29 + 150)))) ? (kG = 2 * -4751 + -3257 * -3 + -269 * 1, kd['push'](GD(kx)), kx = 7458 + 3 * 1707 + -12729 + 150) : kG++,
            k1 >>= 17 * -585 + 6173 + -3623 * -1 + 150
        }
        ((1 * 6427 + 1 * -3409 + -6 * 503) ===  (--k8)) && (k8 = Math['pow'](43 * 122 + -2547 + -2847 + 150, d), d++),
        k3[k6] = k9++,
        k7 = String(k5)
    }
    if ("" !== k7) {
        if (Object['prototype']['hasOwnProp' + 'erty']['call'](k4, k7)) {
            if (k7['charCodeAt'](4019 * 2 + 7 * 851 + 933 * -15) < -4 * 1705 + -3871 * 1 + 10797 + 150) {
                for (k0 = -4236 * -2 + 7877 + -16349; (k0 < d); k0++) kx <<= 23 * 320 + -7003 + -506 + 150,
                (kG === ((Gr - (-7241 + -2 * 1987 + 22 * 503 + 150)))) ? (kG = -6520 + 1231 * 3 + 2827, kd['push'](GD(kx)), kx = 11 * 461 + 29 * -48 + -3679) : kG++;
                for (k1 = k7['charCodeAt'](83 * 51 + 2810 * -1 + -1573 + 150), k0 = -8967 + 1 * -1859 + 10676 + 150; k0 < 4 * 432 + -4529 + -2659 * -1 + 150; k0++) kx = kx << -1745 + -163 * -41 + 5087 * -1 + 150 | 7005 + -2 * 1693 + -27 * 134 & k1,
                (kG === (Gr - (7 * -73 + 4969 + -4457 * 1))) ? (kG = -4398 + -7074 * -1 + 9 * -314 + 150, kd['push'](GD(kx)), kx = -4780 + 6191 * -1 + 3607 * 3 + 150) : kG++,
                k1 >>= -2 * 686 + 4772 * -2 + 9 * 1213
            } else {//不走这个分支
                for (k1 = 2 * -1042 + -1 * 3209 + 1 * 5294, k0 = -3233 + -5075 + -268 * -31; (k0 < d); k0++) kx = ((kx <<  (-9600 + 3 * -62 + 9637 + 150)) | k1),
                kG == (Gr - (4336 + -1 * -4097 + -8432)) ? (kG = 4 * 1784 + -7474 + 47 * 4 + 150, kd['push'](GD(kx)), kx = -6193 + -8627 + 14820) : kG++,
                k1 = -221 + 3719 + -12 * 304 + 150;
                for (k1 = k7['charCodeAt']( - 9743 * -1 + 4350 + -829 * 17), k0 = 3178 + 3566 * -1 + -194 * -2; k0 < 796 * -7 + -5098 + -3 * -3512 + 150; k0++) kx = kx << 53 * 43 + 3148 + -5576 + 150 | Gq[yk(uE.dM)](12 * 55 + 4348 + -5007, k1),
                kG == Gr - (4651 + 1 * -9257 + 4457 + 150) ? (kG = -1661 + 7632 + 6121 * -1 + 150, kd['push'](GD(kx)), kx = -9935 + 1414 + 8371 + 150) : kG++,
                k1 >>= -4633 + 9361 + -4877 + 150
            }
            739 * 1 + 6184 + -6923 == --k8 && (k8 = Math['pow']( - 2435 + -5228 + 7515 + 150, d), d++),
            delete k4[k7]
        } else {
            for (k1 = k3[k7], k0 = -2235 * 2 + 221 * -10 + 6530 + 150; k0 < d; k0++) kx = (kx << (-4136 + -881 * -2 + 19 * 125)) | -751 * 3 + 109 * -79 + 1 * 10865 & k1,
            kG == Gr - (17 * -497 + -546 + -8996 * -1) ? (kG = -4872 + 31 * 233 + -1 * 2351, kd['push'](GD(kx)), kx = -6472 + 5024 + 1298 + 150) : kG++,
            k1 >>= -60 * -39 + -3 * -3322 + -12455 + 150
        }
        ((4636 + -1 * -5329 + -10115 + 150) === (--k8)) && (k8 = Math['pow']( - 818 * 3 + 331 * 14 + -2178, d), d++)
    }
    for (k1 = -2 * -929 + 1 * -5589 + 1 * 3733, k0 = -5147 * 1 + -379 * -9 + -1 * -1736; k0 < d; k0++) kx = ((kx << 1 * 2489 + 2 * 2323 + -7284 + 150) | ((143 * 29 + -8008 + 3862) & k1)),
    (kG === Gr - (1 * 2999 + 9796 + 1618 * -8 + 150)) ? (kG = 6215 + -13 * -244 + -867 * 11 + 150, kd['push'](GD(kx)), kx = -9843 + -4889 + -14582 * -1 + 150) : kG++,
    k1 >>= 1 * 3282 + 7389 + -10670;
    for (;;) {
        if (kx <<= 1687 + 4107 + 1931 * -3, kG == (Gr -  (-9074 + 3353 + 5572 + 150))) {
            kd['push'](GD(kx));
            break
        }
        kG++
    }
    return kd['join']("")
}
function get_cookies() {
    str1 = "2039988618a199c979ffa6^websdk-2.3.13d^1760190627542^15^1|15^zh-CN^-480^16705151|12791^1536|864|1536|150|0|0|1538|865|1536|816|0|0^2^Win32^8^ANGLE (Intel, Intel(R) UHD Graphics 630 (0x00003E9B) Direct3D11 vs_5_0 ps_5_0, D3D11)|Google Inc. (Intel)^24|24^0^28^5|1318940364^3313701045^2981263722^1^0^1^0^P^0^0^0^416^Google Inc.^8^88|59|23|15|0^3726056879^3^1760190667342^599647252^0^29"
    // str1 = `2039988618a199c979ffa6^websdk-2.3.13d^${new Date().getTime()}42^1|15^zh-CN^-480^16705151|12791^1536|864|1536|150|0|0|1538|865|1536|816|0|0^2^Win32^8^ANGLE (Intel, Intel(R) UHD Graphics 630 (0x00003E9B) Direct3D11 vs_5_0 ps_5_0, D3D11)|Google Inc. (Intel)^24|24^0^28^5|1318940364^3313701045^2981263722^1^0^1^0^P^2^0^0^416^Google Inc.^8^88|59|23|15|0^3726056879^34^${new Date().getTime()}^599647252^0^29`
    str2 = `2039988618a199c979ffa6^websdk-2.3.13d^${new Date().getTime()}39^P^2228874^830+149+2228874|126+0+789280^0^^^0^0^0^31^${new Date().getTime()}^0^0^0^0^0`
    // str1 = `2039988618a199c979ffa6^websdk-2.3.13d^1760097332003^42^1|15^zh-CN^-480^16705151|12791^1536|864|1536|150|0|0|1538|865|1536|816|0|0^2^Win32^8^ANGLE (Intel, Intel(R) UHD Graphics 630 (0x00003E9B) Direct3D11 vs_5_0 ps_5_0, D3D11)|Google Inc. (Intel)^24|24^0^28^5|1318940364^3313701045^2981263722^1^0^1^0^P^2^0^0^416^Google Inc.^8^88|59|23|15|0^3726056879^34^${new Date().getTime()}^599647252^0^29`
    // str2 = `2039988618a199c979ffa6^websdk-2.3.13d^1760097332003^39^P^2228874^830+149+2228874|126+0+789280^0^^^0^0^0^31^${new Date().getTime()}^0^0^0^0^0`
    return {
        'ssxmod_itna': "1-" + W(str1,6,GD),
        'ssxmod_itna2':"1-" + W(str2,6,GD)
    }
}


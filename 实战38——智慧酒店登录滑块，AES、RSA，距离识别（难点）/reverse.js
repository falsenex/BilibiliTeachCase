window = global
window.self = window.window = window
const CryptoJS = require('crypto-js')
const JSEncrypt = require('jsencrypt')
_0x51bcee = (function (_0x4e832e) {
  _0x4e832e.version = "1.2.2";
  function _0x14a07b() {
    var _0x3c9016 = 0;
    var _0x2a5804 = new Array(256);
    for (var _0x450011 = 0; _0x450011 != 256; ++_0x450011) {
      _0x3c9016 = _0x450011;
      _0x3c9016 = _0x3c9016 & 1 ? _0x3c9016 >>> 1 ^ -306674912 : _0x3c9016 >>> 1;
      _0x3c9016 = _0x3c9016 & 1 ? _0x3c9016 >>> 1 ^ -306674912 : _0x3c9016 >>> 1;
      _0x3c9016 = _0x3c9016 & 1 ? _0x3c9016 >>> 1 ^ -306674912 : _0x3c9016 >>> 1;
      _0x3c9016 = _0x3c9016 & 1 ? _0x3c9016 >>> 1 ^ -306674912 : _0x3c9016 >>> 1;
      _0x3c9016 = _0x3c9016 & 1 ? _0x3c9016 >>> 1 ^ -306674912 : _0x3c9016 >>> 1;
      _0x3c9016 = _0x3c9016 & 1 ? _0x3c9016 >>> 1 ^ -306674912 : _0x3c9016 >>> 1;
      _0x3c9016 = _0x3c9016 & 1 ? _0x3c9016 >>> 1 ^ -306674912 : _0x3c9016 >>> 1;
      _0x3c9016 = _0x3c9016 & 1 ? _0x3c9016 >>> 1 ^ -306674912 : _0x3c9016 >>> 1;
      _0x2a5804[_0x450011] = _0x3c9016;
    }
    if (typeof Int32Array !== "undefined") {
      return new Int32Array(_0x2a5804);
    } else {
      return _0x2a5804;
    }
  }
  var _0xe75851 = _0x14a07b();
  function _0x4b66a9(_0x13a442) {
    var _0x515054 = 0;
    var _0x2b97cf = 0;
    var _0x296fc4 = 0;
    var _0x5cd945 = typeof Int32Array !== "undefined" ? new Int32Array(4096) : new Array(4096);
    for (_0x296fc4 = 0; _0x296fc4 != 256; ++_0x296fc4) {
      _0x5cd945[_0x296fc4] = _0x13a442[_0x296fc4];
    }
    for (_0x296fc4 = 0; _0x296fc4 != 256; ++_0x296fc4) {
      _0x2b97cf = _0x13a442[_0x296fc4];
      for (_0x515054 = 256 + _0x296fc4; _0x515054 < 4096; _0x515054 += 256) {
        _0x2b97cf = _0x5cd945[_0x515054] = _0x2b97cf >>> 8 ^ _0x13a442[_0x2b97cf & 255];
      }
    }
    var _0x1cffe4 = [];
    for (_0x296fc4 = 1; _0x296fc4 != 16; ++_0x296fc4) {
      _0x1cffe4[_0x296fc4 - 1] = typeof Int32Array !== "undefined" ? _0x5cd945.subarray(_0x296fc4 * 256, _0x296fc4 * 256 + 256) : _0x5cd945.slice(_0x296fc4 * 256, _0x296fc4 * 256 + 256);
    }
    return _0x1cffe4;
  }
  var _0x1cbf85 = _0x4b66a9(_0xe75851);
  var _0x3693dc = _0x1cbf85[0];
  var _0x292923 = _0x1cbf85[1];
  var _0x2c1838 = _0x1cbf85[2];
  var _0x1b4858 = _0x1cbf85[3];
  var _0x1edca3 = _0x1cbf85[4];
  var _0x424543 = _0x1cbf85[5];
  var _0x4e5712 = _0x1cbf85[6];
  var _0x3627a0 = _0x1cbf85[7];
  var _0x5ba75f = _0x1cbf85[8];
  var _0x26464c = _0x1cbf85[9];
  var _0x27278e = _0x1cbf85[10];
  var _0xa82290 = _0x1cbf85[11];
  var _0x4cea26 = _0x1cbf85[12];
  var _0x2e7abc = _0x1cbf85[13];
  var _0x15f8d5 = _0x1cbf85[14];
  function _0x1fa378(_0x4af079, _0x57f720) {
    var _0x56a288 = _0x57f720 ^ -1;
    for (var _0x761c6b = 0, _0x3cf2de = _0x4af079.length; _0x761c6b < _0x3cf2de;) {
      _0x56a288 = _0x56a288 >>> 8 ^ _0xe75851[(_0x56a288 ^ _0x4af079.charCodeAt(_0x761c6b++)) & 255];
    }
    return ~_0x56a288;
  }
  function _0xc51586(_0x4f72ff, _0xb4c0ca) {
    var _0x5cdda6 = _0xb4c0ca ^ -1;
    var _0x554469 = _0x4f72ff.length - 15;
    var _0x46e5da = 0;
    while (_0x46e5da < _0x554469) {
      _0x5cdda6 = _0x15f8d5[_0x4f72ff[_0x46e5da++] ^ _0x5cdda6 & 255] ^ _0x2e7abc[_0x4f72ff[_0x46e5da++] ^ _0x5cdda6 >> 8 & 255] ^ _0x4cea26[_0x4f72ff[_0x46e5da++] ^ _0x5cdda6 >> 16 & 255] ^ _0xa82290[_0x4f72ff[_0x46e5da++] ^ _0x5cdda6 >>> 24] ^ _0x27278e[_0x4f72ff[_0x46e5da++]] ^ _0x26464c[_0x4f72ff[_0x46e5da++]] ^ _0x5ba75f[_0x4f72ff[_0x46e5da++]] ^ _0x3627a0[_0x4f72ff[_0x46e5da++]] ^ _0x4e5712[_0x4f72ff[_0x46e5da++]] ^ _0x424543[_0x4f72ff[_0x46e5da++]] ^ _0x1edca3[_0x4f72ff[_0x46e5da++]] ^ _0x1b4858[_0x4f72ff[_0x46e5da++]] ^ _0x2c1838[_0x4f72ff[_0x46e5da++]] ^ _0x292923[_0x4f72ff[_0x46e5da++]] ^ _0x3693dc[_0x4f72ff[_0x46e5da++]] ^ _0xe75851[_0x4f72ff[_0x46e5da++]];
    }
    _0x554469 += 15;
    while (_0x46e5da < _0x554469) {
      _0x5cdda6 = _0x5cdda6 >>> 8 ^ _0xe75851[(_0x5cdda6 ^ _0x4f72ff[_0x46e5da++]) & 255];
    }
    return ~_0x5cdda6;
  }
  function _0x106884(_0x419116, _0x3a4ecb) {
    var _0x9f5d7f = _0x3a4ecb ^ -1;
    for (var _0x3cf6af = 0, _0x44f2f1 = _0x419116.length, _0x3fef0f = 0, _0x36013e = 0; _0x3cf6af < _0x44f2f1;) {
      _0x3fef0f = _0x419116.charCodeAt(_0x3cf6af++);
      if (_0x3fef0f < 128) {
        _0x9f5d7f = _0x9f5d7f >>> 8 ^ _0xe75851[(_0x9f5d7f ^ _0x3fef0f) & 255];
      } else if (_0x3fef0f < 2048) {
        _0x9f5d7f = _0x9f5d7f >>> 8 ^ _0xe75851[(_0x9f5d7f ^ (_0x3fef0f >> 6 & 31 | 192)) & 255];
        _0x9f5d7f = _0x9f5d7f >>> 8 ^ _0xe75851[(_0x9f5d7f ^ (_0x3fef0f & 63 | 128)) & 255];
      } else if (_0x3fef0f >= 55296 && _0x3fef0f < 57344) {
        _0x3fef0f = (_0x3fef0f & 1023) + 64;
        _0x36013e = _0x419116.charCodeAt(_0x3cf6af++) & 1023;
        _0x9f5d7f = _0x9f5d7f >>> 8 ^ _0xe75851[(_0x9f5d7f ^ (_0x3fef0f >> 8 & 7 | 240)) & 255];
        _0x9f5d7f = _0x9f5d7f >>> 8 ^ _0xe75851[(_0x9f5d7f ^ (_0x3fef0f >> 2 & 63 | 128)) & 255];
        _0x9f5d7f = _0x9f5d7f >>> 8 ^ _0xe75851[(_0x9f5d7f ^ (_0x36013e >> 6 & 15 | 128 | (_0x3fef0f & 3) << 4)) & 255];
        _0x9f5d7f = _0x9f5d7f >>> 8 ^ _0xe75851[(_0x9f5d7f ^ (_0x36013e & 63 | 128)) & 255];
      } else {
        _0x9f5d7f = _0x9f5d7f >>> 8 ^ _0xe75851[(_0x9f5d7f ^ (_0x3fef0f >> 12 & 15 | 224)) & 255];
        _0x9f5d7f = _0x9f5d7f >>> 8 ^ _0xe75851[(_0x9f5d7f ^ (_0x3fef0f >> 6 & 63 | 128)) & 255];
        _0x9f5d7f = _0x9f5d7f >>> 8 ^ _0xe75851[(_0x9f5d7f ^ (_0x3fef0f & 63 | 128)) & 255];
      }
    }
    return ~_0x9f5d7f;
  }
  _0x4e832e.table = _0xe75851;
  _0x4e832e.bstr = _0x1fa378;
  _0x4e832e.buf = _0xc51586;
  _0x4e832e.str = _0x106884;
  return _0x4e832e
})({})
var _0x280ffe = function (_0x520a6a, _0x13f91f, _0xb59e9f) {
  if (_0xb59e9f || arguments.length === 2) {
    for (var _0xfae3bc = 0, _0x4020d5 = _0x13f91f.length, _0xec9a9; _0xfae3bc < _0x4020d5; _0xfae3bc++) {
      if (_0xec9a9 || !(_0xfae3bc in _0x13f91f)) {
        if (!_0xec9a9) {
          _0xec9a9 = Array.prototype.slice.call(_0x13f91f, 0, _0xfae3bc);
        }
        _0xec9a9[_0xfae3bc] = _0x13f91f[_0xfae3bc];
      }
    }
  }
  return _0x520a6a.concat(_0xec9a9 || Array.prototype.slice.call(_0x13f91f));
};
function _0x8531f7(_0x3aecb1, _0x5ca615 = 8) {
  _0x3aecb1 = Math.abs(_0x3aecb1);
  if (Math.abs(_0x3aecb1) > Math.pow(2, _0x5ca615) - 1) {
    return _0x80c353(_0x5ca615).map(function (_0x57b09c) {
      return 0;
    });
  }
  var _0x2e4d11 = _0x3aecb1 < 0 ? _0x2a12cc(new Number(_0x3aecb1).toString(2)) : new Number(_0x3aecb1).toString(2);
  var _0x201fae = _0x2e4d11.split("");
  var _0x424fff = [];
  for (var _0x1b16db = 0; _0x1b16db < _0x201fae.length; _0x1b16db++) {
    _0x424fff.push(Number(_0x201fae[_0x1b16db]));
  }
  if (_0x424fff.length < _0x5ca615) {
    _0x80c353(_0x5ca615 - _0x424fff.length).map(function (_0x426429) {
      return _0x424fff.unshift(0);
    });
  }
  return _0x424fff.slice(0, _0x5ca615 + 1);
}
function _0x80c353(_0x31bf0b) {
  var _0x101aeb = [];
  for (var _0x309773 = 0; _0x309773 < _0x31bf0b; _0x309773++) {
    _0x101aeb.push(0);
  }
  return _0x101aeb;
}
function _0x2a12cc(_0x5156ac) {
  var _0x447e37 = _0x5156ac.split("");
  var _0x42d27b = [];
  if (_0x447e37[0] === "-") {
    _0x42d27b.push(0);
  }
  _0x447e37.slice(1, _0x447e37.length).map(function (_0x331f4b) {
    _0x42d27b.push(_0x331f4b === "0" ? 0 : 1);
  });
  return _0x42d27b.join("");
}
function intToByteList(_0x3aecb1, _0x5ca615 = 8) {
  _0x3aecb1 = Math.abs(_0x3aecb1);
  if (Math.abs(_0x3aecb1) > Math.pow(2, _0x5ca615) - 1) {
    return _0x80c353(_0x5ca615).map(function (_0x57b09c) {
      return 0;
    });
  }
  var _0x2e4d11 = _0x3aecb1 < 0 ? _0x2a12cc(new Number(_0x3aecb1).toString(2)) : new Number(_0x3aecb1).toString(2);
  var _0x201fae = _0x2e4d11.split("");
  var _0x424fff = [];
  for (var _0x1b16db = 0; _0x1b16db < _0x201fae.length; _0x1b16db++) {
    _0x424fff.push(Number(_0x201fae[_0x1b16db]));
  }
  if (_0x424fff.length < _0x5ca615) {
    _0x80c353(_0x5ca615 - _0x424fff.length).map(function (_0x426429) {
      return _0x424fff.unshift(0);
    });
  }
  return _0x424fff.slice(0, _0x5ca615 + 1);
}
function stringToBytes(_0x61caa3, _0x4cb3fc = 2040) {
  var _0x2d3e70 = new Array();
  for (var _0x2569e1 = 0; _0x2569e1 < _0x61caa3.length; _0x2569e1++) {
    var _0x512462 = _0x61caa3.charCodeAt(_0x2569e1);
    var _0x3a1e99 = parseInt("" + _0x512462).toString(2);
    if (_0x512462 >= parseInt("000080", 16) && _0x512462 <= parseInt("0007FF", 16)) {
      var _0x35c6b5 = "";
      for (var _0x37cd88 = 0; _0x37cd88 < 11 - _0x3a1e99.length; _0x37cd88++) {
        _0x35c6b5 += "0";
      }
      _0x35c6b5 += _0x3a1e99;
      var _0x1b0bfb = parseInt("110" + _0x35c6b5.substring(0, 5), 2);
      var _0x33d1fd = parseInt("110" + _0x35c6b5.substring(5), 2);
      if (_0x1b0bfb > 127) {
        _0x1b0bfb -= 256;
      }
      if (_0x33d1fd > 127) {
        _0x33d1fd -= 256;
      }
      _0x2d3e70.push(_0x1b0bfb);
      _0x2d3e70.push(_0x33d1fd);
    } else if (_0x512462 >= parseInt("000800", 16) && _0x512462 <= parseInt("00FFFF", 16)) {
      var _0x35c6b5 = "";
      for (var _0x37cd88 = 0; _0x37cd88 < 16 - _0x3a1e99.length; _0x37cd88++) {
        _0x35c6b5 += "0";
      }
      _0x35c6b5 += _0x3a1e99;
      var _0x1b0bfb = parseInt("1110" + _0x35c6b5.substring(0, 4), 2);
      var _0x33d1fd = parseInt("10" + _0x35c6b5.substring(4, 10), 2);
      var _0x837142 = parseInt("10" + _0x35c6b5.substring(10), 2);
      if (_0x1b0bfb > 127) {
        _0x1b0bfb -= 256;
      }
      if (_0x33d1fd > 127) {
        _0x33d1fd -= 256;
      }
      if (_0x837142 > 127) {
        _0x837142 -= 256;
      }
      _0x2d3e70.push(_0x1b0bfb);
      _0x2d3e70.push(_0x33d1fd);
      _0x2d3e70.push(_0x837142);
    } else if (_0x512462 >= parseInt("010000", 16) && _0x512462 <= parseInt("10FFFF", 16)) {
      var _0x35c6b5 = "";
      for (var _0x37cd88 = 0; _0x37cd88 < 21 - _0x3a1e99.length; _0x37cd88++) {
        _0x35c6b5 += "0";
      }
      _0x35c6b5 += _0x3a1e99;
      var _0x1b0bfb = parseInt("11110" + _0x35c6b5.substring(0, 3), 2);
      var _0x33d1fd = parseInt("10" + _0x35c6b5.substring(3, 9), 2);
      var _0x837142 = parseInt("10" + _0x35c6b5.substring(9, 15), 2);
      var _0x38c329 = parseInt("10" + _0x35c6b5.substring(15), 2);
      if (_0x1b0bfb > 127) {
        _0x1b0bfb -= 256;
      }
      if (_0x33d1fd > 127) {
        _0x33d1fd -= 256;
      }
      if (_0x837142 > 127) {
        _0x837142 -= 256;
      }
      if (_0x38c329 > 127) {
        _0x38c329 -= 256;
      }
      _0x2d3e70.push(_0x1b0bfb);
      _0x2d3e70.push(_0x33d1fd);
      _0x2d3e70.push(_0x837142);
      _0x2d3e70.push(_0x38c329);
    } else {
      _0x2d3e70.push(_0x512462 & 255);
    }
  }
  var _0xa48d1a = [];
  _0x2d3e70.map(function (_0x352777) {
    _0xa48d1a = _0xa48d1a.concat(_0x8531f7(_0x352777));
  });
  return _0xa48d1a.slice(0, _0x4cb3fc);
}
function listComposite(_0xa5ee9e, _0x4d07b4 = 2, _0x498cbd) {
  var _0x36a3c1 = _0xa5ee9e;
  if (_0x498cbd) {
    var _0x6fe0fe = _0x8531f7(1);
    var _0x3e1675 = _0x8531f7(_0x4d07b4 === 1 ? 11 : Math.min(_0x498cbd.split("").length, 2040) + 3);
    var _0x826690 = _0x8531f7(_0x4d07b4);
    var _0x51f1f9 = _0x4d07b4 === 1 ? _0x8531f7(_0x498cbd) : _0x4e354a(_0x498cbd);
    _0x36a3c1 = _0x36a3c1.concat(_0x5d9ec6(_0x5d9ec6(_0x5d9ec6(_0x5d9ec6([], _0x6fe0fe, true), _0x3e1675, true), _0x826690, true), _0x51f1f9, true));
  } else {
    var _0x6fe0fe = _0x8531f7(0);
    var _0x3e1675 = _0x8531f7(4);
    var _0x826690 = _0x8531f7(1);
    var _0x51f1f9 = _0x8531f7(0);
    _0x36a3c1 = _0x36a3c1.concat(_0x5d9ec6(_0x5d9ec6(_0x5d9ec6(_0x5d9ec6([], _0x6fe0fe, true), _0x3e1675, true), _0x826690, true), _0x51f1f9, true));
  }
  return _0x36a3c1;
}
function byteList2Uint8Array(_0x3fc715) {
  var _0x2495ef = [];
  var _0x42e9c4 = _0x3fc715.length / 8;
  for (var _0x17fb7a = 0; _0x17fb7a < _0x42e9c4; _0x17fb7a++) {
    var _0xa5cee3 = 0;
    for (var _0x1a5fe8 = 0; _0x1a5fe8 < 8; _0x1a5fe8++) {
      _0xa5cee3 += _0x3fc715[_0x17fb7a * 8 + _0x1a5fe8] == 1 ? Math.pow(2, 7 - _0x1a5fe8) : 0;
    }
    _0x2495ef.push(_0xa5cee3);
  }
  return new Uint8Array(_0x2495ef);
}
function bytesToBase64(_0x5b438c) {
  var _0x9b1a0c = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
  var _0x2c89da = [];
  for (var _0x523d08 = 0; _0x523d08 < _0x5b438c.length; _0x523d08 += 3) {
    var _0x3aadcf = _0x5b438c[_0x523d08] << 16 | _0x5b438c[_0x523d08 + 1] << 8 | _0x5b438c[_0x523d08 + 2];
    for (var _0x13a98e = 0; _0x13a98e < 4; _0x13a98e++) {
      if (_0x523d08 * 8 + _0x13a98e * 6 <= _0x5b438c.length * 8) {
        _0x2c89da.push(_0x9b1a0c.charAt(_0x3aadcf >>> (3 - _0x13a98e) * 6 & 63));
      } else {
        _0x2c89da.push("=");
      }
    }
  }
  return _0x2c89da.join("");
}
_0x137d59 = { intToByteList, stringToBytes, listComposite, byteList2Uint8Array, bytesToBase64 };
_0x520183 = function () {
  function _0x3d13af(_0x318307) {
    this.maxlen = 251;
    this.trackMaxLen = 252;
    this.counts = 0;
    this.window = _0x318307;
  }
  _0x3d13af.prototype.make = function (_0x4079ed) {
    var _0x55f1d5 = [];
    if (_0x4079ed?.length) {
      var _0x3e301c = [];
      var _0x3dd3d2 = this.trackMaxLen * 8;
      for (var _0xf7c7bd = 0; _0xf7c7bd < _0x4079ed.length; _0xf7c7bd++) {
        var _0xa36b75 = _0x4079ed[_0xf7c7bd];
        if (_0xa36b75) {
          var _0x5a472f = _0xa36b75.split("");
          var _0xc5eece = _0x5a472f.length * 8;
          if (_0xc5eece > this.trackMaxLen) {
            continue;
          }
          if (_0xc5eece > _0x3dd3d2 - 8) {
            _0x3e301c = (0, _0x137d59.intToByteList)(2).concat(_0x3e301c);
            _0x3e301c = (0, _0x137d59.intToByteList)(2 + _0x3e301c.length / 8).concat(_0x3e301c);
            _0x3e301c = (0, _0x137d59.intToByteList)(1).concat(_0x3e301c);
            _0x55f1d5 = _0x55f1d5.concat(_0x3e301c);
            this.counts = this.counts + 1;
            _0x3e301c = [];
            _0x3dd3d2 = this.trackMaxLen * 8;
            _0x3e301c = _0x3e301c.concat((0, _0x137d59.stringToBytes)(_0xa36b75));
            _0x3dd3d2 = _0x3dd3d2 - _0xc5eece;
          } else {
            if (_0x3e301c.length) {
              _0x3e301c = _0x3e301c.concat((0, _0x137d59.stringToBytes)("|"));
              _0x3dd3d2 = _0x3dd3d2 - 8;
            }
            _0x3e301c = _0x3e301c.concat((0, _0x137d59.stringToBytes)(_0xa36b75));
            _0x3dd3d2 = _0x3dd3d2 - _0xc5eece;
            if (_0xf7c7bd === _0x4079ed.length - 1) {
              _0x3e301c = (0, _0x137d59.intToByteList)(2).concat(_0x3e301c);
              _0x3e301c = (0, _0x137d59.intToByteList)(2 + _0x3e301c.length / 8).concat(_0x3e301c);
              _0x3e301c = (0, _0x137d59.intToByteList)(1).concat(_0x3e301c);
              _0x55f1d5 = _0x55f1d5.concat(_0x3e301c);
              this.counts = this.counts + 1;
            }
          }
        }
      }
    }
    return _0x55f1d5;
  };
  _0x3d13af.prototype.listComposite = function (_0x32abb7, _0xb17fae = 2, _0x18fc6b) {
    var _0x567937 = _0x32abb7;
    if (_0x18fc6b) {
      var _0x1219c9 = Math.min(_0x18fc6b.split("").length, this.maxlen);
      var _0x24d279 = (0, _0x137d59.intToByteList)(1);
      var _0x5ab793 = (0, _0x137d59.intToByteList)(_0xb17fae === 1 ? 11 : _0x1219c9 + 3);
      var _0x1feae4 = (0, _0x137d59.intToByteList)(_0xb17fae);
      var _0x4e28f7 = _0xb17fae === 1 ? (0, _0x137d59.intToByteList)(_0x18fc6b) : (0, _0x137d59.stringToBytes)(_0x18fc6b.substring(0, _0x1219c9));
      _0x567937 = _0x567937.concat(_0x280ffe(_0x280ffe(_0x280ffe(_0x280ffe([], _0x24d279, true), _0x5ab793, true), _0x1feae4, true), _0x4e28f7, true));
    } else {
      var _0x24d279 = (0, _0x137d59.intToByteList)(0);
      var _0x5ab793 = (0, _0x137d59.intToByteList)(4);
      var _0x1feae4 = (0, _0x137d59.intToByteList)(1);
      var _0x4e28f7 = (0, _0x137d59.intToByteList)(0);
      _0x567937 = _0x567937.concat(_0x280ffe(_0x280ffe(_0x280ffe(_0x280ffe([], _0x24d279, true), _0x5ab793, true), _0x1feae4, true), _0x4e28f7, true));
    }
    return _0x567937;
  };
  _0x3d13af.prototype.makeUserBrowerInfo = function (_0x5b1e3c) {
    var _0x14c818 = [];
    var _0x3876a5 = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0';
    _0x14c818 = this.listComposite(_0x14c818, 2, _0x3876a5);
    var _0x197689 = '1482,330';
    _0x14c818 = this.listComposite(_0x14c818, 2, _0x197689);
    var _0x5d19e4 = 'https://hotel.ocyuan.com/login';
    _0x14c818 = this.listComposite(_0x14c818, 2, _0x5d19e4);
    var _0x528bde = '0';
    _0x14c818 = this.listComposite(_0x14c818, 2, _0x528bde);
    var _0x78cf86 = '0';
    _0x14c818 = this.listComposite(_0x14c818, 2, _0x78cf86);
    var _0x26fd0f = Date.now().toString();
    _0x14c818 = this.listComposite(_0x14c818, 2, _0x26fd0f);
    this.counts = this.counts + 6;
    return _0x14c818
  };
  _0x3d13af.prototype.bufferBuilder = function (_0x343746, _0x496ffc) {
    var _0x19d55d = [];
    _0x19d55d = _0x19d55d.concat((0, _0x137d59.intToByteList)(1));
    var _0x5c0cee = [];
    _0x5c0cee = _0x5c0cee.concat(this.makeUserBrowerInfo(_0x343746));
    _0x5c0cee = _0x5c0cee.concat(this.make(_0x496ffc));
    _0x19d55d = _0x19d55d.concat((0, _0x137d59.intToByteList)(Math.min(this.counts, this.maxlen)));
    var _0x106a70 = (0, _0x51bcee.buf)((0, _0x137d59.byteList2Uint8Array)(_0x5c0cee));
    _0x19d55d = _0x19d55d.concat((0, _0x137d59.intToByteList)(_0x106a70, 32));
    _0x19d55d = _0x19d55d.concat(_0x5c0cee);
    var _0x32ed1e = (0, _0x137d59.bytesToBase64)((0, _0x137d59.byteList2Uint8Array)(_0x19d55d));
    return _0x32ed1e;
  };
  return _0x3d13af;
}()
var _0xf3a3a7 = {
  getKey: function (_0x4a3e32) {
    var _0x544c9f = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];
    var _0x33f64e = "";
    for (var _0x17dc91 = 0; _0x17dc91 < _0x4a3e32; _0x17dc91++) {
      var _0x1eb9d4 = Math.ceil(Math.random() * 35);
      _0x33f64e += _0x544c9f[_0x1eb9d4];
    }
    return _0x33f64e;
  },
  encode: function (_0x3865e0, _0x5753eb) {
    var _0x470bc1 = CryptoJS.enc.Utf8.parse(_0x5753eb);
    var _0x2ea94c = this.getKey(16);
    var _0x110f3e = CryptoJS.enc.Utf8.parse(_0x2ea94c);
    var _0x246aad = {
      mode: CryptoJS.mode.CTR,
      padding: CryptoJS.pad.NoPadding,
      iv: _0x110f3e
    };
    var _0x1211ee = CryptoJS.AES.encrypt(_0x3865e0, _0x470bc1, _0x246aad).toString();
    return CryptoJS.enc.Base64.stringify(_0x110f3e.concat(CryptoJS.enc.Base64.parse(_0x1211ee)));
  }
};
var _0x313169 = {
  publicKeyEncrypt: function (_0x1b9ff2, _0x347537) {
    var _0xb15ad3 = "-----BEGIN PUBLIC KEY-----PUBLIC_KEY-----END PUBLIC KEY-----";
    var _0x2fc45d = new JSEncrypt();
    var _0xf5d796 = _0xb15ad3.replace("PUBLIC_KEY", _0x347537);
    _0x2fc45d.setPublicKey(_0xf5d796);
    return _0x2fc45d.encrypt(_0x1b9ff2);
  }
};
function getEncryptParams(_0x3c0113, _0x2a4c49) {
  // _0x2a4c49:RSA公钥
  // _0x3c0113:加密后的轨迹数据
  var _0xf87a91 = _0xf3a3a7.getKey(16);
  var _0x439b22 = _0xf3a3a7.encode(_0x3c0113, _0xf87a91);
  var _0x4e92fb = _0x313169.publicKeyEncrypt(_0xf87a91, _0x2a4c49);
  var _0x5b3f6a = "verify_" + new Date().getTime();
  var _0x1aeac9 = {
    collectData: _0x439b22,
    key: _0x4e92fb,
    callback: _0x5b3f6a
  };
  return _0x1aeac9;
}
function handleTrack(trackList) {
  trackBulider = new _0x520183()
  trackStr = trackBulider.bufferBuilder(window, trackList.map(function (_0x24e1fa) {
    var _0x50da05 = _0x24e1fa[0].toFixed(2);
    var _0x32fd74 = _0x24e1fa[1].toFixed(2);
    return `${_0x50da05},${_0x32fd74},${_0x24e1fa[2]}`;
  }))
  return trackStr;
}


function E(e, t, n) {
    var r = CryptoJS.enc.Utf8.parse(t)
      , o = CryptoJS.enc.Utf8.parse(n)
      , a = CryptoJS.AES.encrypt(e, r, {
        iv: o,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    })
      , i = a.toString();
    return i
}
function get_user_passwd(user,passwd,p,i){
  username = E(user, p, i)
  password = E(CryptoJS.MD5(passwd).toString(),p,i)
  return {
      'username':username,
      'password':password
  }
}


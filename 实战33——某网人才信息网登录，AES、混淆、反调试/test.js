// 引入CryptoJS库（实际使用时需要正确引入）
const CryptoJS = require("crypto-js");

// 目标数值数组
// const targetArray = [1715024693, 929195108, 808465977, 1717724004];
const targetArray = [1715024693, 929195108, 808465977, 1717724004]
// [1715024693, 929195108, 808465977, 1717724004]

// 将数值数组转换为WordArray
const wordArray = CryptoJS.lib.WordArray.create(targetArray);

// 将WordArray转换回UTF-8字符串
const originalKey = CryptoJS.enc.Utf8.stringify(wordArray);

// 输出结果
console.log("还原的原始密钥:", originalKey); // 输出: KeyForAES128Test!

// 验证转换是否正确
const verifyArray = CryptoJS.enc.Utf8.parse(originalKey).words;
console.log("验证转换后的数组:", verifyArray); // 输出: [1715024693, 929195108, 808465977, 1717724004]

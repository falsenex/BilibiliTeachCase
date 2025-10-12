// 同步版（Node.js）：等价于你那段 WebCrypto 代码，输出相同 Base64
const crypto = require('crypto');
function randomIv12() {
  const iv = new Uint8Array(12);
  crypto.getRandomValues(iv);
  return iv;
}
function encryptSyncToBase64(plaintext) {
    keyBytes = [189, 48, 95, 16, 208, 255, 116, 182, 239, 84, 218, 184, 53, 181, 225, 207]
    ivBytes = randomIv12()
    const key = Buffer.from(keyBytes);            // 16/24/32 bytes → AES-128/192/256
    const iv  = Buffer.from(ivBytes);             // 12 bytes IV
    const algo = `aes-${key.length * 8}-gcm`;

    const cipher = crypto.createCipheriv(algo, key, iv);
    const ct = Buffer.concat([cipher.update(Buffer.from(plaintext, 'utf8')), cipher.final()]);
    const tag = cipher.getAuthTag();              // 16 bytes
    return Buffer.concat([iv, ct, tag]).toString('base64'); // IV || CT || TAG
}


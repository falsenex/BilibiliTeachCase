const crypto = require('crypto');
const CryptoJS = require('crypto-js');
 
window = globalThis;
require('./__NUXT__.js');
state = __NUXT__.state;
 
kaArr = new Uint8Array(Buffer.from(state.ka,  "base64"));
privateKey = Buffer.from(state.privc, "base64").toString("utf8");
publicKey = Buffer.from(state.pubs,  "base64").toString("utf8");
 
function parsePrivateKey(pemKey) {
    // This is a simplified version - in a real app you'd want to properly parse the PEM
    // and extract all RSA parameters (n, e, d, p, q, dp, dq, qi)
    const key = crypto.createPrivateKey({ 
        key: pemKey,
        format: 'pem'
    });
    
    return {
        key: key,
        modulus: key.export({  type: 'pkcs1', format: 'der' }) // Simplified - actual modulus would need extraction 
    };
}
 
function decryptWithRSA(privateKey, cipherText, isPublic) {
        // Parse the private key
        const keyDetails = parsePrivateKey(privateKey);
        
        // Convert cipherText to Buffer if it's a Uint8Array 
        const cipherBuffer = Buffer.from(cipherText); 
        
        // Decrypt using the private key 
        const decrypted = crypto.privateDecrypt( 
            {
                key: keyDetails.key, 
                padding: crypto.constants.RSA_PKCS1_OAEP_PADDING, 
                oaepHash: 'sha1'
            },
            cipherBuffer
        );
        
        return decrypted;
}
function encryptWithRSA(publicKeyPem, plaintext) {
        // 确保 plaintext 是 Buffer 
        const plaintextBuffer = Buffer.from(JSON.stringify(plaintext),  'utf8');
 
        // 使用 RSA-OAEP 加密 
        const encrypted = crypto.publicEncrypt( 
            {
                key: publicKeyPem,
                padding: crypto.constants.RSA_PKCS1_OAEP_PADDING, 
                oaepHash: 'sha1' // 使用 SHA-1（与你的私钥解密一致）
            },
            plaintextBuffer 
        );
 
        // 返回 base64 编码的加密数据 
        return encrypted.toString('base64'); 
}

function get_data(data) {
    const decrypted = decryptWithRSA(privateKey, kaArr, false).toString('utf8');
    var decrypted_split = decrypted.split("##spa##");

    var key = decrypted_split[0].slice(0, 32);
    var iv = decrypted_split[1].slice(0, 16);
    var data_str = JSON.stringify(data);
    var datac = {
        data: CryptoJS.AES.encrypt(data_str, CryptoJS.enc.Utf8.parse(key), { iv: CryptoJS.enc.Utf8.parse(iv) }).toString(),
        t: encryptWithRSA(publicKey,Math.floor(Math.random() * 100 + 100).toString() + "##spa##" + new Date().getTime()),
        k: encryptWithRSA(publicKey, `${key}##spa##${iv}`)
    }
    return datac;
}

function decrypt_data(data) {
    const decrypted = decryptWithRSA(privateKey, kaArr, false).toString('utf8');
    var decrypted_split = decrypted.split("##spa##");

    var key = decrypted_split[0].slice(0, 32);
    var iv = decrypted_split[1].slice(0, 16);
    var datac = CryptoJS.AES.decrypt(data, CryptoJS.enc.Utf8.parse(key), { iv: CryptoJS.enc.Utf8.parse(iv) }).toString(CryptoJS.enc.Utf8)
    return datac;
}
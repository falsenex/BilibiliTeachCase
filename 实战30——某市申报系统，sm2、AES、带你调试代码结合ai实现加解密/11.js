const { sm2 } = require('sm-crypto');

// SM2 加密模式常量
const SM2CipherMode = {
  C1C3C2: 0,
  C1C2C3: 1
};

// SM2 加密类
class SM2Encryptor {
  constructor(mode) {
    this.cipherMode = (mode !== undefined) ? mode : SM2CipherMode.C1C3C2;
    // 是否使用 C1C3C2 模式
    this.encryptMode = (this.cipherMode === SM2CipherMode.C1C3C2);
  }

  // 加密函数
  encrypt(publicKeyHex, plaintext) {
    // 移除公钥前缀（如果有）
    const cleanPublicKey = publicKeyHex.startsWith('04')
      ? publicKeyHex.slice(2)
      : publicKeyHex;

    // 使用 sm-crypto 进行加密
    return sm2.doEncrypt(plaintext, cleanPublicKey, this.encryptMode ? 1 : 0);
  }
}

// 使用示例
function testSM2Encryption() {
  try {
    // 示例公钥 (需要使用有效的 SM2 公钥)
    const publicKey = 'B9C9A6E04E9C91F7BA880429273747D7EF5DDEB0BB2FF6317EB00BEF331A83081A6994B8993F3F5D6EADDDB81872266C87C018FB4162F5AF347B483E24620207';

    // 创建加密器实例 (默认为 C1C3C2 模式)
    const encryptor = new SM2Encryptor(SM2CipherMode.C1C3C2);

    // 待加密的明文
    const plaintext = 'Hello, SM2 Encryption!';

    // 执行加密
    const encrypted = encryptor.encrypt(publicKey, plaintext);

    console.log('加密结果:', encrypted);
    console.log('加密模式:', encryptor.cipherMode === SM2CipherMode.C1C3C2 ? 'C1C3C2' : 'C1C2C3');
  } catch (error) {
    console.error('加密过程出错:', error);
  }
}

// 执行测试
testSM2Encryption();
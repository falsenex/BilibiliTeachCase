const smCrypto = require('sm-crypto')
const sm2 = smCrypto.sm2

// 公钥，对应Java代码中的 "04064c2a3bcafba2c1ca4f5fb8ecd876b23d70fc4479b78f3c8066c02a8c17749458bca86361bc563d2501b61e2ac93a676a1305893aafcc6be2ea48ecb048672e"
const publicKey = "04064c2a3bcafba2c1ca4f5fb8ecd876b23d70fc4479b78f3c8066c02a8c17749458bca86361bc563d2501b61e2ac93a676a1305893aafcc6be2ea48ecb048672e"

// para_str = {
//     "Trip": [
//         {
//             "Date": "2025-06-05",
//             "Dep": "SZX",
//             "Arrival": "HGH"
//         }
//     ],
//     "Passenger": {
//         "adult": 1,
//         "child": 0,
//         "baby": 0
//     },
//     "notchType": null,
//     "aimPrice": null,
//     "RequestParameterSecurityIdentificationBit": true
// }


// 加密选项，对应Java代码中的 a.yV（假设为 true 表示返回 C1C3C2 顺序的密文）
const options = {
  pointPool: [sm2.getPoint()], // 可选，指定点池
  cipherMode: 1 // 1 表示 C1C3C2 顺序，0 表示 C1C2C3 顺序
}
function get_params(para_json) {
    // 待加密的数据，对应Java代码中的 t
    const dataToEncrypt = encodeURIComponent(JSON.stringify(para_json))
    // 执行加密
    const encryptedData = sm2.doEncrypt(dataToEncrypt, publicKey, options.cipherMode)
    return encryptedData
}


// console.log("加密结果:", get_params(para_str))
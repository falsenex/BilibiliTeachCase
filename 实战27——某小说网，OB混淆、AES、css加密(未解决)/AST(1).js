const parser=require("@babel/parser");
const generate=require("@babel/generator").default
const traverse=require("@babel/traverse").default
const types = require("@babel/types");
const fs = require('fs')

// // 寻找解密函数名 并且运行代码存入解密函数
// const decryFunction = fs.readFileSync('./decryFunction.js', 'utf8');
// let ast=parser.parse(decryFunction);
// let visitor={
//   VariableDeclarator(path){
//     const node = path.node
//     if (!types.isIdentifier(node.id)) return;
//     if (!types.isFunctionExpression(node.init)) return;
//     obDecryptoName = node.id.name
//   }
// }
// traverse(ast,visitor)
// eval(decryFunction)

// 同名函数进行解密
const originalCode = fs.readFileSync('./original_code.js', 'utf8');
ast=parser.parse(originalCode);
visitor={
  CallExpression(path){
    let node = path.node
    if (!types.isIdentifier(node.callee)) return;
    if (obDecryptoName !== node.callee.name) return;
    let result = eval(path+'')
    path.replaceWith(types.stringLiteral(result))
  }
}

traverse(ast,visitor)
result=generate(ast)
handleCode = result.code
filePath = 'handle.js'
// 同步写入（推荐小文件、脚本）
fs.writeFileSync(filePath, handleCode, 'utf8');

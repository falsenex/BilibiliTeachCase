// 定义对象d，包含一个数组n，其中第三个元素是add函数
n = [5, 4, function add(a, b) { return a + b },1, 2]

let g = 0;
n[++g] = n[++g].call(this, n[++g], n[++g]);
console.log('当前g值：'+ g)
console.log('结果：',n[g-3],'函数：',n[g-2],'参数1：',n[g-1],'参数2：',n[g])
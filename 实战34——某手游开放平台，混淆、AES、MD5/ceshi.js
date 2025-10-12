function i(u, _) {
    const d = [];
    let T = (-573 * -1 + 7 * 466 + -82 * 46) & u;
    T = T < -23 * -331 + -1746 * -1 + -9357 ? 2777 * -1 + -7349 + 10128 : (T > _["length"]) ? _.length : T;
    const f = Math["floor"]((_["length"] / T));
    for (let p = -2387 + 1 * 8741 + -3 * 2118; p < T; p++)
        p < (T - (-8056 + -2531 + -4 * -2647)) ? d.push(_.slice((p * f), ((p + (9872 + 7 * -249 + -8128)) * f))) : d["push"](_.slice((p * f)));
    return d
}

const CryptoJS = require("crypto-js");
function s(u, _, x, d) {
    const f = i(x, (u + _ + x)).reverse()["join"]("");
    // return GVo(f + d).toString()
    return CryptoJS.MD5(f + d).toString()
}

w ="0A6tJJr6wTTNBnIjn8mvmBS1dCDIj5Z2XmcJ_Enrwi86tZenY0JsK3Ax6Dc51rL88Gq_YKRDz6mDGA3U1GtZhf-4OAfaQnnyO8LjSCFb9HY"
C ="SYYf269607"
S =1754236557156
    // _() =
_ ="prod#request#MDQzYzUxZDk1MDRjZjJlZDgyMmEwNjIzMDg2ZGJlMTliZjc3YThkMDRhOTU2YzVhNzBlNDcxZWNkYzI5OTE1MA@3"
console.log(s(w, C, S,_))
// t(["c", "r", "t", "s"], [w, C, S, s(w, C, S,_)])
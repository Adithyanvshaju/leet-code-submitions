/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
   let x = s.split(" ")
   let y = x.map(z=> z.split("").reverse().join(""))
   return y.join(" ")

};
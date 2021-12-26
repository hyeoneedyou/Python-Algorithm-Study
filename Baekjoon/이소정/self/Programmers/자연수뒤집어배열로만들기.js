function solution(n) {
  var answer = [];
  answer = Array.from(String(n), Number);
  answer.reverse();
  return answer;
}

console.log(solution(12345));

// 다른사람 풀이
// function solution(n) {
//   return (n + '').split('').reverse().map(n => parseInt(n));
// }

// Number to String
// n + ''
// n.toString()
// String(n)

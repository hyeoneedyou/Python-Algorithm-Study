function solution(n) {
  var answer = 0;
  let arr = Array.from(String(n), Number);
  let nString = arr.sort().reverse().join(""); // string
  answer = Number(nString);
  return answer;
}

console.log(solution(118372));

// Array를 쉼표(,)로 구분하여 String으로 리턴
// arr.toString()

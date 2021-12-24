function solution(num) {
  var answer = "";
  if (Number.IisInteger(num / 2)) {
    answer = "Even";
    return answer;
  }
  answer = "Odd";
  return answer;
}

// 다른사람 풀이
// function solution(num) {
//   return num % 2 ? "Odd" : "Even";
// }

// 0은 false이다.

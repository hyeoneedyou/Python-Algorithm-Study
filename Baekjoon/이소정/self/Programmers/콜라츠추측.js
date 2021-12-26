// 입력된 수가 짝수 -> 2로 나누기
// 입력된 수가 홀수 -> 3 곱하고 1 더하기
// 반복

function solution(num) {
  var answer = 0;
  while (num != 1) {
    num = num % 2 == 0 ? num / 2 : num * 3 + 1;
    answer += 1;
    // 이중으로 웬만하면 쓰지 말자...
    if (answer == 500) {
      return -1;
    }
  }
  return answer;
}

console.log(solution(626331));

// 다른사람 풀이
// function solution(num) {
//   var answer = 0;
//   while (num != 1 && answer != 500) {
//     num % 2 == 0 ? (num = num / 2) : (num = num * 3 + 1);
//     answer++;
//   }
//   return num == 1 ? answer : -1;
// }

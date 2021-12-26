function solution(n) {
  var answer = 0;
  if (Number.isInteger(Math.sqrt(n))) {
    answer = (Math.sqrt(n) + 1) ** 2;
    return answer;
  }
  return -1;
}

console.log(solution(121));

// 정수 판별
// k % 1 == 0

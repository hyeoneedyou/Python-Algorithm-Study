function solution(n) {
  var answer = 0;
  const arr = Array.from(String(n), Number);
  answer = arr.reduce((prev, curr) => {
    return prev + curr;
  });

  return answer;
}

console.log(solution(123));

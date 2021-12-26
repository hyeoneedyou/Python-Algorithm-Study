function solution(arr) {
  var answer = 0;
  let sum = arr.reduce((prev, curr) => {
    return prev + curr;
  });
  answer = sum / arr.length;
  return answer;
}

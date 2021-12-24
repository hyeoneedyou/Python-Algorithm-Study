function solution(arr) {
  var answer = [];
  let small = Math.min(...arr); // 전개 연산자
  answer = arr.filter((ele) => ele != small);
  if (answer.length == 0) {
    answer.push(-1);
  }
  return answer;
}

console.log(solution([4, 3, 2, 1]));
// console.log(solution([10]));

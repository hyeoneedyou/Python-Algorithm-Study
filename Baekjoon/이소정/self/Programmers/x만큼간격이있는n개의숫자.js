function solution(x, n) {
  var answer = [];
  let tmp = 0;
  while (answer.length != n) {
    tmp = tmp + x;
    answer.push(tmp);
  }
  return answer;
}

console.log(solution(-4, 2));

// 다른사람 코드
// function solution(x, n) {
//   return Array(n).fill(x).map((v, i) => (i + 1) * v)
// }

// Array(data.length).fill(null);
// -> n개의 length를 가진 배열을 모두 null로 채우기

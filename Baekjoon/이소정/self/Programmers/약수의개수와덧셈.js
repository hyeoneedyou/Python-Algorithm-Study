function solution(left, right) {
  var answer = 0;
  for (let i = left; i <= right; i++) {
    let count = 0;
    for (let j = 1; j <= i; j++) {
      if (i % j === 0) {
        // console.log(`${j}`);
        count += 1;
      }
    }
    console.log(`${i} : ${count}`);
    if (count % 2 === 0) {
      answer += i;
    } else {
      answer -= i;
    }
  }
  return answer;
}

// 다른 사람 풀이

// function solution(left, right) {
//   var answer = 0;
//   for (let i = left; i <= right; i++) {
//       if (Number.isInteger(Math.sqrt(i))) {
//           answer -= i;
//       } else {
//           answer += i;
//       }
//   }
//   return answer;
// }

// 제곱근이 정수면 약수의 개수가 홀수다.

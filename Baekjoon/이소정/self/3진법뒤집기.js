function solution(n) {
  var answer = 0;
  let quo = n;
  let remainder = [];
  while (quo !== 0) {
    remainder.push(quo % 3);
    quo = Math.floor(quo / 3);
  }
  remainder.reverse();
  remainder.forEach((ele, index) => (answer += ele * Math.pow(3, index)));
  return answer;
}

// forEach문 자유롭게 쓰기

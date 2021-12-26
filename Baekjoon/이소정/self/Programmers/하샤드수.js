// 하샤드 수 : x % (x자릿수 합) == 0
// true or false

function solution(x) {
  let arr = Array.from(String(x), Number);
  let sum = arr.reduce((prev, curr) => {
    return prev + curr;
  });
  let answer = x % sum == 0 ? true : false;
  return answer;
}

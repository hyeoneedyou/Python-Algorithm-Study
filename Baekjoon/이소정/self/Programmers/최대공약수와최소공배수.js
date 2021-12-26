function solution(n, m) {
  var answer = [];
  const gcd = (a, b) => {
    if (b == 0) return a;
    return gcd(b, a % b);
  };

  const lcm = (a, b) => {
    return (a * b) / gcd(a, b);
  };

  answer = [gcd(n, m), lcm(n, m)];
  return answer;
}

console.log(solution(3, 12));

// 1 2 4 8
// 1 2 3 4 6 12

// 유클리드 호제법
// 12 % 4 == 0 -> 최대공약수 4
// 12 % 8 = 4 -> 8 % 4 == 0 -> 최대공약수 4

// 최소공배수
// (a*b) / gcd(a, b)

// 다른사람 풀이
// const solutuon = (n, m) => {
//   const gcd = (a, b) => {
//     if (b === 0) return a; // 나누어지면 a 리턴
//     return gcd(b, a % b); // 나누어지지 않는다면 b와 a%b를 다시 나눈다
//   };
//   const lcm = (a, b) => (a * b) / gcd(a, b); // 두 수의 곱을 최대공약수로 나눈다.
//   return console.log(
//     `최대 공약수는? ${gcd(n, m)}, 최대 공배수는? ${lcm(n, m)}`
//   );
// };

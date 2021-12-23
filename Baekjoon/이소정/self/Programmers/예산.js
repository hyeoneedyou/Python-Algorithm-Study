function solution(d, budget) {
  var answer = 0;
  d.sort((a, b) => {
    return a - b;
  });
  let result = d.reduce((prev, curr) => {
    if (prev <= budget) {
      answer += 1;
    }
    return prev + curr;
  });
  if (result <= budget) {
    answer += 1;
  }
  return answer;
}

console.log(solution([1, 3, 2, 10, 11, 12], 17));
// console.log(solution([2, 2, 3, 3], 10));
// console.log(solution([100], 101));

// 다른 풀이
// function solution(d, budget) {
//     let answer = 0;
//     let money = 0;
//     d.sort((a,b) => a-b).forEach(function(val){
//         money += val;
//         if(money <= budget){
//             answer++;
//         }

//     })
//     return answer;
// }

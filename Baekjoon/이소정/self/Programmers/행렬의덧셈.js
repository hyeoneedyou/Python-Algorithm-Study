function solution(arr1, arr2) {
  var answer = [[]];
  answer = arr1.map((arr, i) => {
    return arr.map((ele, j) => arr1[i][j] + arr2[i][j]);
  });
  return answer;
}

console.log(
  solution(
    [
      [1, 2],
      [2, 3],
    ],
    [
      [3, 4],
      [5, 6],
    ]
  )
);

// 다른 사람 풀이
// function solution(arr1, arr2) {
//   return arr1.map((a,i) => a.map((b, j) => b + arr2[i][j]));
// }

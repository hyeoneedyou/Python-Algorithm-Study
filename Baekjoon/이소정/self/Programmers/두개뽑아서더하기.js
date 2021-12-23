function solution(numbers) {
  var answer = [];
  numbers.forEach((num1, index) => {
    numbers.slice(index + 1).forEach((num2) => {
      answer.push(num1 + num2);
    });
  });
  answer = Array.from(new Set(answer));
  answer.sort((a, b) => {
    return a - b;
  });
  return answer;
}

console.log(solution([5, 0, 2, 7]));

// answer.sort() 하면 아스키코드 순서대로 정렬된다.

// 아래 두 개는 같은 코드
// answer = Array.from(new Set(answer));
// answer = [...new Set(answer)]; -> spread operation으로 풀 수도 있다.

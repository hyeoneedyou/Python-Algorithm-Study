// 각 단어의
// 짝수 -> 대문자
// 홀수 -> 소문자

function solution(s) {
  var answer = "";
  let words = s.split(" ");
  let newWords = words.map((word) => {
    let result = "";
    for (let i = 0; i < word.length; i++) {
      result += i % 2 == 0 ? word[i].toUpperCase() : word[i].toLowerCase();
      // if (i % 2 == 0) {
      //   result += word[i].toUpperCase();
      // } else {
      //   result += word[i].toLowerCase();
      // }
    }
    return result;
  });
  answer = newWords.join(" ");
  return answer;
}

console.log(solution("try hello world"));

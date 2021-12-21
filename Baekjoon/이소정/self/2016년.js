function solution(a, b) {
  var answer = "";
  const dayList = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"];
  const monthList = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  let monthStart = 5;
  // for (let i = 0; i < a - 1; i++) {
  //   if (monthList[i] == 31) {
  //     monthStart += 3;
  //   } else if (monthList[i] == 29) {
  //     monthStart += 1;
  //   } else {
  //     monthStart += 2;
  //   }
  // }
  //let monthA = monthStart % 7;

  // 새로운 코드
  let aMonthFirst = 0;
  if (a >= 2) {
    aMonthFirst = monthList.slice(0, a - 1).reduce((acc, cur) => acc + cur);
  }
  let monthA = (monthStart + aMonthFirst) % 7;
  //
  let dayB = (monthA + ((b - 1) % 7)) % 7;
  answer = dayList[dayB];
  return answer;
}

console.log(solution(1, 1));

// 다른 사람 풀이
// function getDayName(a,b){
//   var dayList = ['FRI','SAT','SUN','MON','TUE','WED','THU'];
// var monthArr = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
// var daySum;
// if(a < 2) {
//   daySum = b - 1;
// } else {
//   daySum = monthArr.slice(0, a - 1).reduce((a, b) => a + b) + b - 1;
// }
//   return dayList[daySum % 7];
// }

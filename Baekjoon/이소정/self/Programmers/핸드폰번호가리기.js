function solution(phone_number) {
  let phone_hide = "*".repeat(phone_number.length - 4) + phone_number.slice(-4);
  return phone_hide;
}

// substring vs substr vs slice

// 정규식으로 풀기
// function hide_numbers(s) {
//   return s.replace(/\d(?=\d{4})/g, "*");
// }

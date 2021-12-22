// 1 내꺼 (여벌 존재)
// 2 없음
// 3 내꺼
// 4 없음
// 5 내꺼 (여벌 존재)

function solution(n, lost, reserve) {
  lost.sort();
  reserve.sort();
  let nothing = lost.filter((ele) => !reserve.includes(ele)); // 없음
  let haveReserve = reserve.filter((ele) => !lost.includes(ele)); //여분있음
  nothing.forEach((ele) => {
    if (haveReserve.includes(ele - 1)) {
      haveReserve = haveReserve.filter((item) => item != ele - 1);
    } else if (haveReserve.includes(ele + 1)) {
      haveReserve = haveReserve.filter((item) => item != ele + 1);
    } else {
      n -= 1;
    }
  });
  return n;
}

console.log(solution(5, [3, 5], [2, 4]));

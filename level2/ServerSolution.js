//서버증설횟수
function solution(players, m, k) {
  let total = 0;
  let running = 0;
  let endTime = Array(24).fill(0); // 0~24까지

  for (let hour = 0; hour < 24; hour++) {
    // 1. 만료 서버 제거
    running -= endTime[hour];

    // 2. 필요한 서버 수 계산
    let required = Math.floor(players[hour] / m);

    // 3. 서버 추가 필요
    if (required > running) {
      let need = required - running;
      running += need;
      total += need;

      // 4. 종료 시간
      let end = hour + k;

      // 오늘 안에 종료되면 endTime에 기록
      if (end <= 23) {
        endTime[end] += need;
      }
      // 24 이상이면 무시 (하루 지나서 종료됨)
    }
  }

  return total;
}

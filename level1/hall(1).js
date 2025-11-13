// https://school.programmers.co.kr/learn/courses/30/lessons/138477?language=javascript
// 명예의 전당(1)
function solution(k, score) {
  const hall = []; // 명예의 전당 저장
  const result = [];

  for (let s of score) {
    hall.push(s);
    hall.sort((a, b) => b - a); // 내림차순 정렬

    if (hall.length > k) hall.pop(); // k명 초과 → 최하위 제거

    result.push(hall[hall.length - 1]); // 명예의 전당 최하위 점수
  }

  return result;
}

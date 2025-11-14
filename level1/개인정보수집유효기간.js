//https://school.programmers.co.kr/learn/courses/30/lessons/150370
//2023 KAKAO BLIND RECRUITMENT

function solution(today, terms, privacies) {
  let termMap = new Map();
  for (let i = 0; i < terms.length; i++) {
    let term = terms[i].split(" ");
    termMap[term[0]] = term[1];
  }
  var answer = [];

  for (let i = 0; i < privacies.length; i++) {
    const privacie = privacies[i].split(" ");
    const date = privacie[0];
    const term = Number(termMap[privacie[1]]);
    if (evaluate(today, date, term)) answer.push(i + 1);
  }

  return answer;
}

//date->개인정보 수집날짜, term->유효기간(단위: 달)
function evaluate(today, date, term) {
  const todayInfo = today.split(".");
  const dateInfo = date.split(".");

  const todayDates =
    Number(todayInfo[0]) * 28 * 12 +
    Number(todayInfo[1]) * 28 +
    Number(todayInfo[2]);
  let year = Number(dateInfo[0]);
  let month = Number(dateInfo[1]);
  let day = Number(dateInfo[2]);
  const privacieDates = year * 28 * 12 + (month + term) * 28 + day;
  console.log(todayDates, privacieDates);
  if (privacieDates > todayDates) return false;
  else return true;
}

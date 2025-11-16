const parseSets = (s) => {
  return s
    .slice(2, -2)
    .split("},{")
    .map((group) => group.split(",").map(Number));
};

const diff = (a, b) => a.filter((x) => !b.includes(x));

function solution(s) {
  let sList = parseSets(s);
  let answer = [];

  sList.sort((a, b) => a.length - b.length);
  answer.push(sList[0][0]);
  console.log(answer);
  console.log(sList);
  console.log(diff(sList, answer));
  for (let i = 1; i < sList.length; i++) {
    answer.push(diff(sList[i], answer)[0]);
  }

  return answer;
}

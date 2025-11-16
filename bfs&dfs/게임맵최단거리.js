function solution(maps) {
  const n = maps.length;
  const m = maps[0].length;
  const visited = Array.from({ length: n }, () => Array(m).fill(0));

  const dx = [-1, 1, 0, 0];
  const dy = [0, 0, -1, 1];

  const queue = [[0, 0]];
  visited[0][0] = 1;

  while (queue.length) {
    const [x, y] = queue.shift();

    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i];
      const ny = y + dy[i];

      if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue; // 범위 체크
      if (maps[nx][ny] === 0) continue; // 벽
      if (visited[nx][ny] !== 0) continue; // 이미 방문

      visited[nx][ny] = visited[x][y] + 1;
      queue.push([nx, ny]);
    }
  }

  const result = visited[n - 1][m - 1];
  return result === 0 ? -1 : result;
}

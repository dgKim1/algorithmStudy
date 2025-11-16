function solution(n, computers) {
  let visited = Array(n).fill(false);
  let count = 0;

  function dfs(node) {
    visited[node] = true;

    for (let next = 0; next < n; next++) {
      if (computers[node][next] === 1 && !visited[next]) {
        dfs(next);
      }
    }
  }

  for (let i = 0; i < n; i++) {
    if (!visited[i]) {
      dfs(i);
      count++;
    }
  }

  return count;
}

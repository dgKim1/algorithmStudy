import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i,k):
    q = deque()
    q.append((i,k))
    dist = [[-1] * m for _ in range(n)]
    dist[i][k] = 0
    maxD = 0
    while q:
        x,y = q.popleft()
        
        


        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx<n and 0<= ny <m:
                #탐색하는 곳이 육지 & 방문한적 없던 곳이라면 dist갱신
                if board[nx][ny] == "L" and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    maxD = max(maxD, dist[nx][ny])
                    q.append((nx,ny))

    return maxD








n, m = map(int, input().split())

board = []
answer=0
for _ in range(n):
    board.append(list(input().rstrip()))
for i in range(n):
    for k in range(m):
        if board[i][k] == "L":
            answer = max(answer,bfs(i,k))
print(answer)

import sys
from collections import deque


input = sys.stdin.readline

m,n,k = map(int,input().rstrip().split())

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def dfs(x,y):
    stack = deque()
    stack.append((x,y))
    ans = 1
    board[x][y] = 1
    while stack:
        x,y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0<=nx<m and 0<=ny<n) and board[nx][ny] == 0:
                board[nx][ny] = 1
                stack.append((nx,ny))
                ans+=1
    
    return ans

board = [[0]*n for _ in range(m)]
#모두 0으로 초기화
places =[]
for i in range(k):
    places.append(map(int,input().split()))

for x1,y1,x2,y2 in places:
    for i in range(y1,y2):
        for k in range(x1,x2):
            board[i][k] = -1
answer = []

for i in range(m):
    for k in range(n):
        if board[i][k] == 0:
            answer.append(dfs(i,k))



print(len(answer))
print(*answer)


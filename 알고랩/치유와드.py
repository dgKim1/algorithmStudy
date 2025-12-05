import sys

input = sys.stdin.readline

t = int(input().rstrip())


def cherishev(x1,y1,x2,y2):
    return max(abs(x1-x2),abs(y1-y2))


def manhattan(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)


for _ in range(t):
    n, m = map(int, input().rstrip().split())# n-> 맵 크기
    a, b = map(int, input().rstrip().split())
    #a 시체 
    #b 와드수
    zombie =[]
    ward = []
    board = [[0] * n for _ in range(n)]
    for _ in range(a):
        r,c = map(int, input().rstrip().split())
        zombie.append((r,c))
    for _ in range(b):
        r,c = map(int, input().rstrip().split())
        ward.append((r,c))
    for (r,c) in zombie:
        for x in range(n):
            for y in range(n):
                d = cherishev(x,y,r,c)
                if d <= m:
                    val = (d-m)-1
                    if d == 0:
                        val+=1
                    board[x][y] += val
    for (r,c) in ward:
        for x in range(n):
            for y in range(n):
                d = manhattan(x,y,r,c)
                if d <= m:
                    val = (m-d)+1
                    if d == 0:
                        val -=1
                    board[x][y] += val

    for r in board:
        print(*r)


    


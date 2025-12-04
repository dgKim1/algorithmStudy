import sys
input = sys.stdin.readline


# 거리 함수
def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def chebyshev(x1, y1, x2, y2):
    return max(abs(x1 - x2), abs(y1 - y2))

# 메인
for _ in range(int(input())):
    n, m = map(int, input().split())
    a, b = map(int, input().split())

    poison = [tuple(map(int, input().split())) for _ in range(a)]
    heal   = [tuple(map(int, input().split())) for _ in range(b)]

    board = [[0] * n for _ in range(n)]

    # 독-Chebyshev
    for r, c in poison:

        # 독이 맵 끝까지 퍼지는 데 필요한 최대 시간 T 
        T = max(r, c, n-1-r, n-1-c)
        d = min(m, T)

        # 탐색 범위 제한
        for i in range(max(0, r - d), min(n, r + d + 1)):
            for j in range(max(0, c - d), min(n, c + d + 1)):

                dist = chebyshev(i, j, r, c)

                if dist <= m:
                    days = m - dist + 1
                    if dist == 0:
                        days -= 1
                    board[i][j] -= days



    # 치유 - Manhattan 
    for r, c in heal:

        # 치유 영향 반경 최적화용 최대 맨해튼 거리 T
        T = max(
            r + c,
            (n-1-r) + c,
            r + (n-1-c),
            (n-1-r) + (n-1-c)
        )
        d = min(m, T)

        for i in range(max(0, r - d), min(n, r + d + 1)):
            dx = abs(i - r)
            for j in range(max(0, c - d), min(n, c + d + 1)):

                dist = manhattan(i, j, r, c)

                if dist <= m:
                    days = m - dist + 1
                    if dist == 0:
                        days -= 1
                    board[i][j] += days

    # 출력
    for row in board:
        print(*row)

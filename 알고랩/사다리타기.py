import sys

### 백트래킹 문제 ###
def trace_ladder(n, m, d, ladder):
    # d에 해당하는 column 위치
    col = (d - 1) * 2

    # 아래 → 위 순서로 탐색
    for row in reversed(range(m)):
        # 왼쪽 이동 가능
        if col > 0 and ladder[row][col - 1] == '+':
            col -= 2
        # 오른쪽 이동 가능
        elif col < 2 * n - 2 and ladder[row][col + 1] == '+':
            col += 2

    return (col // 2) + 1  


t = int(input().strip())
answers = []


input = sys.stdin.readline

for i in range(t):
    n, m, d = map(int, input().split())
    ladder = [input().rstrip('\n') for _ in range(m)]
    answers.append(trace_ladder(n, m, d, ladder))

for ans in answers:
    print(ans)

import sys
input = sys.stdin.readline

t = int(input())
# 차례대로 아래, 오른, 왼, 위
move = {
    ("FF","RL","LR","BB"):(1,0),
    ("FR","RF","LB","BL"):(0,1),
    ("FL","RB","LF","BR"):(0,-1),
    ("FB","RR","LL","BF"):(-1,0)
}
orderDic = {(1,0):"F",(0,1):"R",(0,-1):"L",(-1,0):"B"}

def changeOrder(r,c):
    return orderDic.get((r,c))

def checkValue(order):
    for tup in move:
        if order in tup:
            return move[tup]

for _ in range(t):
    n = int(input())
    board = [input().split() for _ in range(n)]

    check = [[set() for _ in range(n)] for _ in range(n)]

    r, c = 0, 0
    last = "B"  # 처음 들어온 방향은 B로 가정

    temp, stride = list(board[r][c])
    order = last + temp
    dr, dc = checkValue(order)
    direct = changeOrder(dr, dc)
    moveR, moveC = dr * int(stride), dc * int(stride)

    check[r][c].add(last)

    while True:
        # 이동
        r += moveR
        c += moveC

        # 이번 칸으로 들어온 방향은 last = direct
        last = direct

        # 두 번째 방문 판정
        if last in check[r][c]:
            print(r, c)
            break

        # 방문 기록
        check[r][c].add(last)

        # 다음 방향 계산
        temp, stride = list(board[r][c])
        order = last + temp
        dr, dc = checkValue(order)
        direct = changeOrder(dr, dc)
        moveR, moveC = dr * int(stride), dc * int(stride)

import sys

input = sys.stdin.readline

t = int(input().rstrip())
for i in range(t):
    n = int(input().rstrip())
    game = list(map(int,input().rstrip().split()))

    vMap = []


    for k in range(n):
        start = k
        left = start # 왼쪽으로만 이동하는 말 인덱스
        right = start # 오른쪽으로만 이동하는 말 인덱스
        while ((right+1)<n and game[right] <= game[right+1]):
            right += 1

        while ((left-1)>=0 and game[left] <= game[left-1]):
            left -= 1
        vMap.append(right-left+1)
    print(max(vMap))
        

    


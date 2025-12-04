import sys
input = sys.stdin.readline



def solve(n,p):
    pos=0
    step = 0

    while (pos<n):
        #다음 계단이 망가진 계단인 경우 - 2칸이동
        if(pos+1==p):
            pos+=2
        #두칸이동이 가능할 경우
        elif(pos+2<=n and pos+2 != p):
            pos+=2
        #나머지 케이스는 모두 1칸 이동
        else:
            pos+=1
        step+=1
    return step

t = int(input())
for i in range(t):
    n, p = map(int,input().split())
    print(solve(n,p))
import sys

input = sys.stdin.readline

def generate(t,A,B,C):
    return (pow(t,2)*A + B*t + C) % 999983



T = int(input().rstrip())


for i in range(T):
    n = int(input().rstrip()) #고객수
    oOtp = [tuple(map(int,input().rstrip().split())) for _ in range(n)]
    m = int(input().rstrip()) # otp갯수
    for _ in range(m):
        u, t, x = map(int, input().split())
        a,b,c = oOtp[u-1]
        check = False

        for k in range(t-3,t+4,1):
            temp = generate(k,a,b,c)

            if temp == x:
                print("YES")
                check = True
                break
        if check:
            continue
        print("NO")
import sys


input = sys.stdin.readline

t = int(input())



def formatStr(list,n):
    newStr = ""
    for i in range(n,len(list)):
        if i == n:
            newStr += list[i] + "0"*n
        else:
            newStr += list[i]



    return newStr




for i in range(t):
    numbersStr = input().rstrip() #각 자리 수를 배열로
    numberList = list(numbersStr)
    numberList.sort()
    zeroNum = numbersStr.count("0")
    answer = formatStr(numberList,zeroNum)
    print(answer)

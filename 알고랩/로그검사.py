import sys
import re

input = sys.stdin.readline


# ^ / $ : 문자열 전체가 이 패턴과 완전히 일치해야 함 (앞뒤에 다른 거 있으면 비정상)

# line_name : 등은 그냥 고정 문자열

# [A-Za-z]+ : 1글자 이상 영문자만

# 정상 로그 패턴
pattern = re.compile(
    r'^line_name : [A-Za-z]+ product_name : [A-Za-z]+ error_level : [A-Za-z]+ message : [A-Za-z]+$'
)

T = int(input().rstrip())

for _ in range(T):
    n = int(input().rstrip())
    invalid = 0

    for _ in range(n):
        log = input().rstrip('\n')  # 뒤에 개행만 제거


        if len(log) > 100:
            invalid += 1
            continue
        # 패턴과 완전히 일치하지 않으면 비정상 로그
        if pattern.fullmatch(log) is None:
            invalid += 1

    print(invalid)

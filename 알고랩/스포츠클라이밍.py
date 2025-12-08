import sys
from collections import deque

input = sys.stdin.readline


def bfs(board):
    q = deque()
    x,y = n-1,0
    dists = [[]*n for _ in range(n)]
    while q:






for _ in range(int(input())):
    n = int(input().rstrip())
    board = []
    for _ in range(n):
        board.append(list(input().rtrip()))
    dists = bfs(board)
import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
cards = set(cards)
M = int(input())
find_numlist = list(map(int, input().split()))

for num in find_numlist:
    if num in cards:
        print(1, end = ' ')
    else:
        print(0, end = ' ')
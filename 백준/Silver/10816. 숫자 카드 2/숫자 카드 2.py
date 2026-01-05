# 10816
# 숫자 카드 2
import sys

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
cards_dict = {}

for card in cards:
    if card in cards_dict:
        cards_dict[card] += 1
    else:
        cards_dict[card] = 1

M = int(sys.stdin.readline())
find_cards = list(map(int, sys.stdin.readline().split()))

for card in find_cards:
    if card in cards_dict:
        print(cards_dict[card], end = ' ')
    else:
        print(0, end=' ')
import sys
input = sys.stdin.readline

N = int(input())
words = []

for _ in range(N):
    words.append(input().rstrip())

words = sorted(set(words))
sorted_words = sorted(words, key=lambda x: len(x))

for word in sorted_words:
    print(word)
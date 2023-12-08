word = input()
alphabets = 'abcdefghijklmnopqrstuvwxyz'
result = []

for alphabet in alphabets:
    if alphabet in word:
        result.append(str(word.index(alphabet)))
    else:
        result.append('-1')

print(' '.join(result))

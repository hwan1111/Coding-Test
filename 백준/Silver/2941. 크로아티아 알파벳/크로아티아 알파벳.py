word = input()
Croatia = ['c=', 'c-', 'dz=', 'd-', 'lj','nj', 's=', 'z=']

for i in Croatia :
    word = word.replace(i, 'a')
print(len(word))
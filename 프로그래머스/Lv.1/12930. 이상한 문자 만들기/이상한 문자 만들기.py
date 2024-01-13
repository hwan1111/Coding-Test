def solution(string):
    answer = []
    string = string.split(' ')
    
    for word in string:
        modified_word = ''
        for i in range(len(word)):
            if i % 2 == 0:
                modified_word += word[i].upper()
            else:
                modified_word += word[i].lower()
        answer.append(modified_word)
    
    return ' '.join(answer)
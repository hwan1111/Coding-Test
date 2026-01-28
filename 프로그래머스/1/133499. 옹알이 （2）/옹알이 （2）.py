def solution(babbling):
    answer = 0
    can_speak = ["aya", "ye", "woo", "ma"]
    
    for bab in babbling:
        skip = False
        for sound in can_speak:
            if sound * 2 in bab:
                skip = True
                break
        
        if skip:
            continue
        
        for sound in can_speak:
            bab = bab.replace(sound, ' ')
        
        if bab.strip() == '':
            answer += 1
    
    return answer
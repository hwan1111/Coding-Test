def solution(hp):
    general = hp//5
    hp = hp - 5 * general
    
    soldier = hp//3
    hp = hp - 3 * soldier

    worker = hp

    return general + soldier + worker
def solution(sizes):
    max_width = max(max(card) for card in sizes)
    max_height = max(min(card) for card in sizes)
    
    wallet_size = max_width * max_height
    
    return wallet_size

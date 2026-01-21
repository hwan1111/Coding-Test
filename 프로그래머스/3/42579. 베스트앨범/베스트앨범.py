def solution(genres, plays):
    genre_total = {}
    songs = {}
    
    # 1. 장르별 총합 + 곡 목록 만들기
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        if genre in genre_total:
            genre_total[genre] += play
            songs[genre].append((play, idx))
        else:
            genre_total[genre] = play
            songs[genre] = [(play, idx)]
    
    # 2. 장르를 총 재생 수 기준으로 정렬
    sorted_genres = sorted(genre_total, key=lambda g: genre_total[g], reverse=True)
    
    answer = []
    
    # 3. 각 장르에서 노래 정렬 후 상위 2개 선택
    for genre in sorted_genres:
        songs[genre].sort(key=lambda x: (-x[0], x[1]))
        
        for play, idx in songs[genre][:2]:
            answer.append(idx)
    
    return answer
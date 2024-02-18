def solution(name, yearning, photo):
    answer = []
    grade = {name[i]: yearning[i] for i in range(len(name))}
    for query in photo:
        missing = 0
        for i in range(len(query)):
            if query[i] in grade:
                missing += grade[query[i]]
        answer.append(missing)

    return answer
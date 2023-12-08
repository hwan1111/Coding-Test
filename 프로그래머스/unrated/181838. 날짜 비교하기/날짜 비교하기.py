def solution(date1, date2):
    year1, month1, day1 = date1
    year2, month2, day2 = date2
    if year1 < year2:
        return 1
    elif year1 == year2:
        if month1 < month2:
            return 1
        elif month1 == month2:
            if day1 < day2:
                return 1
            else:
                return 0
        else:
            return 0
    else:
        return 0
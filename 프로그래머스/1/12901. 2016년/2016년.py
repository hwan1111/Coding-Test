def solution(a, b):
    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_of_week = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    total_days = sum(days_in_month[:a-1]) + b
    return days_of_week[total_days % 7]
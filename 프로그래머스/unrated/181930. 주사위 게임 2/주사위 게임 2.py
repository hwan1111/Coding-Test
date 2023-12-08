def solution(a, b, c):
    if a == b and b == c and c == a:
        return (a + b + c)*(a**2 + b**2 + c**2)*(a**3 + b**3 + c**3)
    elif (a == b and a != c) or (b == c and b != a) or (c == a and c != b):
        return (a + b + c)*(a**2 + b**2 + c**2)
    elif a != b and b != c and c != a:
        return a + b +c
# 두 원의 방정식을 비교하여 교점의 개수 판단
def find_intersection_points(x1, y1, r1, x2, y2, r2):

    # 두 원의 중심 사이의 거리 계산
    distance_between_centers = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    
    # 두 원의 반지름 합과 중심 사이의 거리를 비교하여 교점의 개수 판단
    if distance_between_centers > r1 + r2:
        return 0
    elif distance_between_centers < abs(r1 - r2):
        return 0
    elif distance_between_centers == 0 and r1 == r2:
        return -1
    elif distance_between_centers == r1 + r2 or distance_between_centers == abs(r1 - r2):
        return 1
    else:
        return 2

T = int(input())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    print(find_intersection_points(x1, y1, r1, x2, y2, r2))

tri = []
for _ in range(3):
    angle = int(input())
    tri.append(angle)

if sum(tri) == 180:
    if tri[0] == tri[1] == tri[2]:
        print("Equilateral")
    elif (tri[0] == tri[1]) or (tri[1] == tri[2]) or (tri[2] == tri[0]):
        print("Isosceles")
    elif tri[0] != tri[1] != tri[2]:
        print("Scalene")
else:
    print("Error")
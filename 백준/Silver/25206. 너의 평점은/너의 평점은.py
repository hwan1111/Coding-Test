Grade = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+':2.5, 'C0': 2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
s = 0
total_credits = 0
for _ in range(20):
    subject, credit, grade = map(str, input().split())
    credits = float(credit)

    if grade != 'P':
        grades = Grade[grade]
        s += grades * credits
        total_credits += credits
    
print(s/total_credits)
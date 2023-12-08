def solution(binomial):
    op = binomial.split()[1]
    if op == '+':
            return int(binomial.split()[0])+int(binomial.split()[2])
    if op == '-':
            return int(binomial.split()[0])-int(binomial.split()[2])
    if op == '*':
            return int(binomial.split()[0])*int(binomial.split()[2])

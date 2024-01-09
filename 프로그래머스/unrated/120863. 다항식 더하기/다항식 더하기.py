def solution(polynomial):
    list0 = sorted(polynomial.split(' + '))
    rank_x = 0
    C = 0

    for poly in list0:
        if 'x' in poly:
            if poly == 'x':
                rank_x += 1
            elif poly == '-x':
                rank_x -= 1
            else:
                rank_x += int(poly.replace('x', ''))
        else:
            C += int(poly)

    if rank_x == 0 and C == 0:
        return '0'
    elif rank_x == 0 and C != 0:
        return f'{C}'
    elif rank_x != 0 and C == 0:
        if rank_x == 1:
            return 'x'
        else:
            return f'{rank_x}x'
    elif rank_x != 0 and C != 0:
        if rank_x == 1:
            if C > 0:
                return f'x + {C}'
            else:
                return f'x - {-C}'
        else:
            if C > 0:
                return f'{rank_x}x + {C}'
            else:
                return f'{rank_x}x - {-C}'
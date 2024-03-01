def solution(elements):
    element_sum = []

    element_sum.extend(elements)

    for i in range(2, len(elements) + 1):
        
        for j in range(len(elements)):
            sum = (i + j - 1) % len(elements)
            element_sum.append(element_sum[(i-2)*len(elements)+j] + element_sum[sum])
    
    return len(set(element_sum))
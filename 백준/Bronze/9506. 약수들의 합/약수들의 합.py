while True:
    mod = []
    n = int(input())
    if 2 < n < 100000:
        for i in range(1, n):
            if n%i == 0:
                mod.append(i)
        
        if sum(mod) == n:
            print(f"{n} = ", end = "")
            for j in range(len(mod)-1):
                print(f"{mod[j]}", end = " + ")
            print(f"{mod[-1]}")
        else:
            print(f"{n} is NOT perfect.")
    elif n == -1:
        break
    else:
        break
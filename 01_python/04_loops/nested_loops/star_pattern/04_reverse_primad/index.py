n = 5
i = 1
while i <= n:
    k = 1
    while k <= i:
        print(" ", end="")
        k +=1
    j = 1
    while j <= (n - i) * 2 - 1:
        print("*", end="")
        j += 1
    print('')
    i += 1
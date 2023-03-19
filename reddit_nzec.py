import math
    
t = int(input())
n_list = []
k_list = []
    
for i in range(t):
    x = int(input())
    k = 1
    while 5**k <= x:
        k += 1
        if x < 5**(k+1):
            break
    n_list.append(x)
    k_list.append(k)

for j in range(t):
    trailingZeros = 0
    
    if n_list[j] < 5:
        print(trailingZeros)
    else:
        for x in range(1, k_list[j]+1):
            trailingZeros += (math.floor((n_list[j]/(5**x))))
        print(trailingZeros)
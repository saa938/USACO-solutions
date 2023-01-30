def solve(n,l):
    num = 0
    while True:
        for i in l:
            if i < 0:
                return -1
        if len(set(l)) == 1: 
            return num

        smallest = min(l)
        
        for i in range(n-1):
            if l[i] > smallest:
                diff = l[i] - smallest
                l[i] -= diff
                l[i+1] -= diff
                num += 2*diff
        
        if l[-1] > l[-2]:
            return -1

t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    print(solve(n,l))

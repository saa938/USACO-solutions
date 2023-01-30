import sys
sys.setrecursionlimit(1000000)

sys.stdin = open("herding.in","r")
sys.stdout = open("herding.out","w")

a,b,c = list(map(int, input().split()))
ans = 0
if c-a == 2:
    ans = 0
    print(ans)
    print(ans)
elif b-a == 2 or c-b == 2:
    ans = 1
    print(ans) 
    print(max(b-a-1,c-b-1))
else:
    ans = 2
    print(ans)
    print(max(b-a-1,c-b-1))



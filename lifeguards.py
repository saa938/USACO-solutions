import sys
sys.setrecursionlimit(1000000)

sys.stdin = open("lifeguards.in","r")
sys.stdout = open("lifeguards.out","w")

l = [0]*1000
n = int(input())
c = []
ans = 0
for i in range(n):
    c.append(list(map(int, input().split())))

def check(c,l):
    for i,j in c:
        for k in range(i-1,j-1):
            l[k] = 1
    # print(l)
    return l.count(1)

for i in range(n):
    l = [0]*1000
    nc = c[:i] + c[i+1:]
    # print(nc)
    ans = max(ans, check(nc,l))

print(ans)

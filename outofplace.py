import sys
sys.setrecursionlimit(1000000)

sys.stdin = open("outofplace.in","r")
sys.stdout = open("outofplace.out","w")

n = int(input())
l = []
for i in range(n):
    l.append(int(input()))

c = sorted(l)

swaps = 0
for i,j in zip(l,c):
    if i != j:
        swaps += 1
print(swaps - 1)

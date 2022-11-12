import sys
sys.setrecursionlimit(1000000)

sys.stdin = open("div7.in","r")
sys.stdout = open("div7.out","w")

n = int(input())
psum = [0]
for i in range(n):
    j = int(input())
    psum.append((j+psum[-1])%7)
# print(psum[1:])


s = 0
found = {}
for i,j in enumerate(psum[1:]):
    if j in found:
        s = max(s, i - found[j])
    else:
        found[j] = i
print(s)

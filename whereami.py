import re
import sys
sys.setrecursionlimit(1000000)

sys.stdin = open("whereami.in","r")
sys.stdout = open("whereami.out","w")

n = int(input())
s = input().strip()
ans = n

for i in range(1, n+1):
    sub = set()
    for j in range(n-i+1):
        sub.add(s[j: i+j])
    if len(sub) == n-i+1:
        ans = i
        break
print(ans)
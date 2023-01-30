import sys
sys.setrecursionlimit(1000000)

sys.stdin = open("cowtip.in","r")
sys.stdout = open("cowtip.out","w")

n = int(input())
l = []

def flip(l, row, col):
    for i in range(row+1):
        for j in range(col+1):
            if l[i][j] == '1':
                l[i][j]='0'
            else:
                l[i][j]='1'
    # print(nl)
    return l

for i in range(n):
    l.append([i for i in input().strip()])
# print(l)
# print(flip(l,2,2))
ans = 0
for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):
        if l[i][j] == '1':
            l = flip(l,i,j)
            ans += 1
            # print(l)
print(ans)
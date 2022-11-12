import sys
sys.stdin = open("bcount.in","r")
sys.stdout = open("bcount.out","w")

n,q = map(int, input().split())
s=[[0,0,0]]

for i in range(n):
    x = int(input())
    if x == 1:
        s.append([s[-1][0]+1,s[-1][1],s[-1][2]])
    elif x == 2:
        s.append([s[-1][0],s[-1][1]+1,s[-1][2]])
    else:
        s.append([s[-1][0],s[-1][1],s[-1][2]+1])

for i in range(q):
    start,end = map(int, input().split())
    h,g,j=0,0,0
    h = s[end][0]-s[start-1][0]
    g=s[end][1]-s[start-1][1]
    j=s[end][2]-s[start-1][2]
    print(h,g,j)

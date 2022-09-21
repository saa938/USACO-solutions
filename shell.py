import sys
sys.setrecursionlimit(1000000)

sys.stdin = open("shell.in","r")
sys.stdout = open("shell.out","w")

N = int(input())
l = []
for i in range(N):
	l.append(list(map(int, input().split())))
ans = 0
for i in range(1,4):
	dsa=0
	x=[1,2,3] 
	for j in range(N):
		a,b,g=l[j][0],l[j][1],l[j][2]
		x[a-1],x[b-1]=x[b-1],x[a-1]
		if x[g-1] == i:
			dsa += 1
	ans = max(ans, dsa)

print(ans)
					 
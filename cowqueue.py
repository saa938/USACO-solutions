import sys
sys.setrecursionlimit(1000000)

sys.stdin = open("cowqueue.in","r")
sys.stdout = open("cowqueue.out","w")

n = int(input())
l = []
for _ in range(n):
	l.append(list(map(int, input().split())))
l.sort()
time = 0
for i,j in l:
	print(i,j,time)
	if time > i:
		time += j
	else:
		time = i+j	

print(time)
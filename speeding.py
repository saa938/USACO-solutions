import sys
sys.setrecursionlimit(1000000)

sys.stdin = open("speeding.in","r")
sys.stdout = open("speeding.out","w")
n, m = list(map(int, input().split()))

speedlimits = []
for i in range(n):
	length, limit = list(map(int,input().split()))
	for j in range(length):
		speedlimits.append(limit)

speed = []
for i in range(m):
	length, limit = list(map(int,input().split()))
	for j in range(length):
		speed.append(limit)

over = 0
for i in range(100):
	over = max(over, speed[i]-speedlimits[i])

print(over)
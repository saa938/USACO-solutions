import sys
sys.setrecursionlimit(1000000)

sys.stdin = open("balancing.in","r")
sys.stdout = open("balancing.out","w")

n, b = list(map(int, input().split()))

x_vals=[]
y_vals=[]
for i in range(n):
	a,b = list(map(int, input().split()))
	x_vals.append(a)
	y_vals.append(b)

ans = n
for x in range(n):
	for y in range(n):
		xDivider = x_vals[x] + 1
		yDivider = y_vals[y] + 1
		upperLeft, upperRight, lowerLeft, lowerRight = 0,0,0,0
		for i in range(n):
			if x_vals[i] < xDivider and y_vals[i] < yDivider:
				lowerLeft += 1
			if x_vals[i] < xDivider and y_vals[i] > yDivider:
				upperLeft += 1
			if x_vals[i] > xDivider and y_vals[i] < yDivider:
				lowerRight += 1
			if x_vals[i] > xDivider and y_vals[i] > yDivider:
				upperRight += 1
		ans = min(max(upperLeft, lowerLeft, lowerRight, upperRight), ans)

print(ans)
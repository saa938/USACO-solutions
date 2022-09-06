import sys
sys.setrecursionlimit(1000000)

sys.stdin = open("cownomics.in","r")
sys.stdout = open("cownomics.out","w")

n, b = list(map(int, input().split()))

spotty_cows = []
plain_cows = []
for i in range(n):
	spotty_cows.append(input().strip())
for i in range(n):
	plain_cows.append(input().strip())

ans = 0
for i in range(b):
	a = False
	for j in range(n):
		for k in range(n):
			if spotty_cows[j][i] == plain_cows[k][i]:
				a = True
				break
	if a == False:
		ans += 1
print(ans)
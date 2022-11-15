# import sys
# sys.setrecursionlimit(1000000)

# sys.stdin = open("1.in","r")
# sys.stdout = open("1.out","w")

alphabet = input().strip()
hummed = input().strip()
N = len(hummed)
found = ''
n = 0
ans = 0
while found != hummed:
	for i in alphabet:
		if n < N:
			if i == hummed[n]:
				found += i
				n += 1
	ans += 1
print(ans)
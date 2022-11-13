import sys
sys.setrecursionlimit(1000000)

sys.stdin = open("circlecross.in","r")
sys.stdout = open("circlecross.out","w")

crossings = input().strip()
ans = 0
cows = {}
for index, element in enumerate(crossings):
	if element in cows:
		cows[element].append(index)
	else:
		cows[element] = [index]
# print(cows)
a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for i in range(26):
	for j in range(i+1, 26):
		w,x = cows[a[i]]
		y,z = cows[a[j]]
		# print(cow1, cow2)
		if w in range(y,z):
			if x not in range(y,z):
				ans += 1
		elif x in range(y,z):
			if w not in range(y,z):
				ans += 1
print(ans)
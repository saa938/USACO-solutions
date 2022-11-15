n = int(input())
cow_heights = list(map(int, input().split()))
barn_heights = list(map(int, input().split()))
cow_heights.sort(reverse=True)
ans = 1
for i in range(n):
	fit = 0
	for j in range(n):
		if cow_heights[i] <= barn_heights[j]:
			fit += 1
	fit -= i
	ans *= fit
print(ans)
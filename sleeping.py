T = int(input())
for i in range(T):
	length = int(input())
	log = list(map(int, input().split()))
	if len(set(log)) == 1:
		print(0)
	else:
		modMin = 10**6
		s = sum(log)
		for r in range(s+1, 0, -1):
			if s % r == 0:
				target = s // r
				# print("r", r, "target", target)
				current = 0
				works = True
				for j in range(length):
					current += log[j]
					# print("current", current)
					if current > target:
						works = False
						break
					if current == target:
						current = 0
				if works == True:
					modMin = min(modMin, length-r)
		print(modMin)
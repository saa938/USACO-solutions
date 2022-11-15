n = int(input())
ids = list(map(int, input().split()))
odds, evens = 0,0 
for i in ids:
	if i % 2 == 0:
		evens += 1
	else:
		odds += 1
while odds > evens:
	odds -= 2
	evens += 1
if evens > odds + 1:
	evens = odds + 1
print(odds + evens)


import sys
sys.setrecursionlimit(1000000)

sys.stdin = open("tttt.in","r")
sys.stdout = open("tttt.out","w")

ttt=[]
for i in range(3):
	a = input()
	ttt.append(a.strip())

cows = set()
for i in range(3):
	cows.add(''.join(set(ttt[i])))
	cows.add(''.join({ttt[0][i], ttt[1][i], ttt[2][i]}))
cows.add(''.join({ttt[0][0], ttt[1][1], ttt[2][2]}))
cows.add(''.join({ttt[0][2], ttt[1][1], ttt[2][0]}))



different_cows = []
for i in cows:
	different_cows.append(len(i))

print(different_cows.count(1))
print(different_cows.count(2))
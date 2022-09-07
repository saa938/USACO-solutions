import sys
sys.setrecursionlimit(1000000)

sys.stdin = open("paint.in","r")
sys.stdout = open("paint.out","w")

a,b = list(map(int, input().split()))
c,d = list(map(int, input().split()))
# print(a,b,c,d)
if d in range(a,b+1) or c in range(a,b+1) or a in range(c,d+1) or b in range(c,d+1):
	print(max(b,d)-min(a,c))
else:
	print((b-a) + (d-c))
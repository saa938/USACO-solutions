import sys
sys.setrecursionlimit(1000000)

sys.stdin = open("reduce.in","r")
sys.stdout = open("reduce.out","w")

N = int(input())
smallx1, smallx2, smally1, smally2 = 10**8,10**8,10**8,10**8
largex1, largex2, largey1, largey2 = 0,0,0,0
x = []
y = []
for i in range(N):
	a,b = list(map(int, input().split()))
	x.append(a)
	y.append(b)
	if a < smallx1:
			smallx2 = smallx1
			smallx1 = a
	else: smallx2 = min(a, smallx2)
		
	if a > largex1:
		largex2 = largex1
		largex1 = a
	else: largex2 = max(largex2, a)
		
	
	if b < smally1:
		smally2 = smally1
		smally1 = b
	else: smally2 = min(b, smally2)
	
	if b > largey1:
		largey2 = largey1
		largey1 = b
	else: largey2 = max(largey2, b)
		

fence = (largex1 - smallx1) * (largey1 - smally1)
for i in range(N):
	smallx=smallx1
	if x[i] == smallx:
		smallx = smallx2
		
	largex = largex1
	if x[i] == largex:
		largex = largex2

	smally = smally1
	if y[i] == smally:
		smally = smally2

	largey = largey1
	if y[i] == largey:
		largey = largey2

	fence = min(fence, (largex - smallx) * (largey - smally))

print(fence)
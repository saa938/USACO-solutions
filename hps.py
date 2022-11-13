import sys
sys.setrecursionlimit(1000000)

sys.stdin = open("hps.in","r")
sys.stdout = open("hps.out","w")

n = int(input())
#          H,P,S
prefix = [[0,0,0]]
for i in range(n):
    move = input().strip()
    if move == 'H':
        prefix.append([prefix[-1][0]+1,prefix[-1][1],prefix[-1][2]])
    elif move == 'P':
        prefix.append([prefix[-1][0],prefix[-1][1]+1,prefix[-1][2]])
    else:
        prefix.append([prefix[-1][0],prefix[-1][1],prefix[-1][2]+1])
# print(prefix[-1])
ans = 0
for i in range(n):
    maxr, maxl = 0,0
    for j in range(3):
        maxr = max(maxr, prefix[i][j])
        maxl = max(maxl, prefix[-1][j] - prefix[i][j])
    ans = max(ans, maxr+maxl)
print(ans)
import sys
sys.setrecursionlimit(1000000)

sys.stdin = open("teleport.in","r")
sys.stdout = open("teleport.out","w")

start,end,teleport1,teleport2=list(map(int,input().split()))
ans = min(abs(end-start), abs(start-teleport1)+abs(teleport2-end),abs(start-teleport2)+abs(teleport1-end))
print(ans)	
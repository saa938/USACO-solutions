import sys
sys.setrecursionlimit(1000000)

sys.stdin = open("breedflip.in","r")
sys.stdout = open("breedflip.out","w")

n = int(input())
want = input().strip()
get = input().strip()

ans, cons = 0, 0
for i in range(n):
    wbreed, gbreed = want[i], get[i]
    if wbreed == gbreed and cons > 0:
        ans += 1
        cons = 0
    elif wbreed != gbreed:
        cons += 1

print(ans)
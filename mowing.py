import sys
sys.setrecursionlimit(1000000)

sys.stdin = open("mowing.in","r")
sys.stdout = open("mowing.out","w")

n = int(input())
l = []
x,y=0,0
ans = 10000

def check(ans):
    if [x,y] in l:
        ans = min(ans, len(l)-l.index([x,y]))
        # print([x,y], len(l)-l.index([x,y]))
        return ans
    return 10000

for i in range(n):
    direction, steps = input().split()
    steps = int(steps)
    if direction == 'N':
        for i in range(steps):
            y += 1
            b = check(ans)
            ans = min(ans, b)
            l.append([x,y])
    elif direction == 'S':
        for i in range(steps):
            y -= 1
            b = check(ans)
            ans = min(ans, b)
            l.append([x,y])
    elif direction == 'W':
        for i in range(steps):
            x -= 1
            b = check(ans)
            ans = min(ans, b)
            l.append([x,y])
    elif direction == 'E':
        for i in range(steps):
            x += 1
            b = check(ans)
            ans = min(ans, b)
            l.append([x,y])
# print(l)
print(ans)

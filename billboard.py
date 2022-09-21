import sys
sys.setrecursionlimit(1000000)

sys.stdin = open("billboard.in","r")
sys.stdout = open("billboard.out","w")

ax1,ay1,ax2,ay2=list(map(int,input().split()))
bx1,by1,bx2,by2=list(map(int,input().split()))
tx1,ty1,tx2,ty2=list(map(int,input().split()))

area_a=(ay2-ay1)*(ax2-ax1)
area_b=(by2-by1)*(bx2-bx1)
# area_t=(ty2-ty1)*(tx2-tx1)

overlap_x = max(0, min(ax2, tx2) - max(ax1, tx1))

overlap_y = max(0, min(ay2, ty2) - max(ay1, ty1))

ans1= overlap_x*overlap_y

overlap_x = max(0, min(bx2, tx2) - max(bx1, tx1))
overlap_y = max(0, min(by2, ty2) - max(by1, ty1))

ans2= overlap_x*overlap_y

print(area_a+area_b-ans1-ans2)
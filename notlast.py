import sys
sys.setrecursionlimit(1000000)

sys.stdin = open("notlast.in","r")
sys.stdout = open("notlast.out","w")

n = int(input())
d = {
    'Bessie':0, 
    'Elsie':0, 
    'Daisy':0, 
    'Gertie':0, 
    'Annabelle':0, 
    'Maggie':0, 
    'Henrietta':0
}
for i in range(n):
    cow, num = input().split()
    d[cow] += int(num)
# print(d)
x= sorted(list(set(d.values())))
if len(x) == 1:
    smallest_value = x[0]
else:
    smallest_value = x[1]
# print(smallest_value)
rd = {}
nums = 0
for i,j in d.items():
    rd[j] = i
    if j == smallest_value:
        nums += 1
if nums > 1:
    print('Tie')
else:
    print(rd[smallest_value])
    
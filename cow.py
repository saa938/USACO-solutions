import sys
sys.setrecursionlimit(1000000)

sys.stdin = open("cow.in","r")
sys.stdout = open("cow.out","w")

N = int(input())
string = input().strip()
c_counter, o_counter, w_counter = 0,0,0
for i in string:
	if i == 'C':
		c_counter += 1
	elif i == "O":
		o_counter += c_counter
	elif i == "W":
		w_counter += o_counter
print(w_counter)
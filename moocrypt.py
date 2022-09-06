import sys
sys.setrecursionlimit(1000000)

sys.stdin = open("moocrypt.in","r")
sys.stdout = open("moocrypt.out","w")

N,M = list(map(int, input().split()))
l = []
for i in range(N):
	l.append(input().strip())
#  1 2 3
#	 4 5 6
#  7 8 9
delta_y = [0, 1, 1, 1, 0, -1, -1, -1]
delta_x = [-1, -1, 0, 1, 1, 1, 0, -1]
delta_y_2 = [0, 2, 2, 2, 0, -2, -2, -2]
delta_x_2 = [-2, -2, 0, 2, 2, 2, 0, -2]
total = 0
alphabet1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V','W', 'X', 'Y', 'Z']
alphabet2 =  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V','W', 'X', 'Y', 'Z']
for char1 in alphabet1:
	for char2 in alphabet2:
		if char1 != char2:
			s = 0
			for row in range(N):
				for col in range(M):
					if l[row][col] == char1:
						# print("Neighbors of", l[row][col] + ":")
						for i in range(8):
							x = row+delta_x[i]
							y = col+delta_y[i]
							x2, y2 = row+delta_x_2[i], col+delta_y_2[i]
							if x2 >= 0 and x2 < N and y2 >= 0 and y2<M:
								if (l[x][y], l[x2][y2]) ==  (char2, char2):
									s += 1
			total = max(total, s)
									
print(total)
				
#!/usr/bin/python
import sys
chessboard = []
fp = open('output.txt', 'w')
moves = ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, -1), (-2, 1))
def check_move_legality(x_incr, y_incr, size ):
	if (((x_incr >= 0) and (y_incr >= 0)) and ((x_incr < size) and (y_incr < size)) and (chessboard[x_incr][y_incr] == 0)):
		return 1
	else:
		#print "Illegal move"
		return 0

def find_no_neighbours(i, size):
	count = 0
	for j in moves:
		if check_move_legality(i[0] + j[0], i[1] + j[1], size):
			count = count + 1
	return count

def main():
	sys.setrecursionlimit(200000)
	size  = input("Enter size of square matrix")

	for i in range(0, size):
		temp = []	
		for j in range(0,size):
			temp.append(0)
		chessboard.append(temp)
	start(0, 0, 1, size)

def start(x, y, count, size):
	assert chessboard[x][y] == 0
	chessboard[x][y] = count
	#print count
	if count == size * size:
		for i in chessboard:
			fp.write(str(i))
			fp.write("\n")	
			fp.write("-" *  size)
			fp.write("\n")
		sys.exit(1)
	neighbour = []
	"""Find the current list of neighbours for an input x, y"""
	for move in moves:
		if check_move_legality(x + move[0], y + move[1], size):
			neighbour.append((x + move[0], y + move[1]))

	"""for each of the found neighbours, find # of neighbours for each one and sort"""
	neighbour_finder = []
	for co_ords in neighbour:
		neighbour_finder.append((co_ords, find_no_neighbours(co_ords, size)))
	neighbour_finder = sorted(neighbour_finder, key = lambda x: x[1] )

	for term in neighbour_finder:
		start(term[0][0], term[0][1], count + 1, size)
	chessboard[x][y] = 0
		
if __name__ == "__main__":
	main()

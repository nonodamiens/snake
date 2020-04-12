import random
import os
# os.system("mode con: cols=25 lines=25")

clear = lambda: os.system('cls') #on Windows System
clear()

head = "☺"
corps = "■"
pastille = "●"

area = {"0" : "         ",\
		"1" : "         ",\
		"2" : "         ",\
		"3" : "         ",\
		"4" : "         ",\
		"5" : "         ",\
		"6" : "         ",\
		"7" : "         ",\
		"8" : "         ",\
		}

j_coord = (4, 4)
p_coord = (random.randint(0, 9), random.randint(0, 9))
while p_coord == j_coord:
	p_coord = (random.randint(0, 9), random.randint(0, 9))

print("pastille coord: ", p_coord)
area[str(p_coord[0])] = " " * (p_coord[1] - 1) + pastille + " " * (9 - p_coord[1])
area[str(j_coord[0])] = area[str(j_coord[0])][:j_coord[1]] + head + area[str(j_coord[0])][j_coord[1] + 1:]

print("┌─────────┐\n│{}│\n│{}│\n│{}│\n│{}│\n│{}│\n│{}│\n│{}│\n│{}│\n│{}│\n└─────────┘"\
	.format(area["0"], area["1"], area["2"], area["3"], area["4"], area["5"], area["6"], area["7"], area["8"]))
print("coord joueur:", j_coord)

go = True
while go:
	clear()
	print("pastille coord: ", p_coord)
	area[str(p_coord[0])] = " " * (p_coord[1] - 1) + pastille + " " * (9 - p_coord[1])
	area[str(j_coord[0])] = area[str(j_coord[0])][:j_coord[1]] + head + area[str(j_coord[0])][j_coord[1] + 1:]

	print("┌─────────┐\n│{}│\n│{}│\n│{}│\n│{}│\n│{}│\n│{}│\n│{}│\n│{}│\n│{}│\n└─────────┘"\
		.format(area["0"], area["1"], area["2"], area["3"], area["4"], area["5"], area["6"], area["7"], area["8"]))
	print("coord joueur:", j_coord)
	
	x = raw_input()
	if x == "e":
		go = False
	elif x == "q":
		area[str(j_coord[0])] = "         "
		j_coord = (j_coord[0], j_coord[1] - 1)
		area[str(j_coord[0])] = area[str(j_coord[0])][:j_coord[1]] + head + area[str(j_coord[0])][j_coord[1] + 1:]
	elif x == "s":
		go = False
	elif x == "z":
		go = False
	elif x == "w":
		go = False



# print(area)
# clear()
# print(area)

# area[5][5] = corps
# coord = (5, 5)

# direction = "b"
# x = 0
# while x < 10:
#   if direction == "b":
#     area[coord[0]][coord[1]] = " "
#     coord = (coord[0] + 1, coord[1])
#     area[coord[0]][coord[1]] = corps
#     print(area)
#   x += 1
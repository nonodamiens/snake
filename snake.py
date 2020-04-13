import random
import os
import time
from msvcrt import getch, kbhit
# os.system("mode con: cols=25 lines=25")

clear = lambda: os.system('cls') #on Windows System
clear()

head = "☺"
tail = "■"
pastille = "●"

j_coord = (4, 4)
t_coord =[(3, 4)]
p_coord = (random.randint(0, 8), random.randint(0, 8))
while p_coord == j_coord:
	p_coord = (random.randint(0, 8), random.randint(0, 8))
go = True
d = 'down'
x = ""
points = 0
die = False

while go:	
	clear()

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

	print("pastille coord: ", p_coord)
	area[str(p_coord[0])] = area[str(p_coord[0])][:p_coord[1]] + pastille + area[str(p_coord[0])][p_coord[1] + 1:]
	area[str(j_coord[0])] = area[str(j_coord[0])][:j_coord[1]] + head + area[str(j_coord[0])][j_coord[1] + 1:]
	for c in t_coord:
		area[str(c[0])] = area[str(c[0])][:c[1]] + tail + area[str(c[0])][c[1] + 1:]
	print("┌─────────┐\n│{}│\n│{}│\n│{}│\n│{}│\n│{}│\n│{}│\n│{}│\n│{}│\n│{}│\n└─────────┘"\
		.format(area["0"], area["1"], area["2"], area["3"], area["4"], area["5"], area["6"], area["7"], area["8"]))
	print("coord joueur:", j_coord)
	print("score:", points)

	time.sleep(0.5)
	if kbhit():
		x = getch()
	if x == b'\x00':
		d = {b"H": "up", b"P": "down", b"M": "right", b"K": "left"}[getch()]
	elif x == b"q":
		go = False
	if d == "up" and (j_coord[0] - 1, j_coord[1]) not in t_coord:
		t_coord = [j_coord] + t_coord[:-1]
		j_coord = (j_coord[0] - 1, j_coord[1])
	elif d == "down" and (j_coord[0] + 1, j_coord[1]) not in t_coord:
		t_coord = [j_coord] + t_coord[:-1]
		j_coord = (j_coord[0] + 1, j_coord[1])
	elif d == "right" and (j_coord[0], j_coord[1] + 1) not in t_coord:
		t_coord = [j_coord] + t_coord[:-1]
		j_coord = (j_coord[0], j_coord[1] + 1)
	elif d == "left" and (j_coord[0], j_coord[1] - 1) not in t_coord:y
		t_coord = [j_coord] + t_coord[:-1]
		j_coord = (j_coord[0], j_coord[1] - 1)
	else:
		die = True
	if -1 in j_coord or 9 in j_coord or die == True:
		print('\033[93myou died\033[0m')
		print("restart ? (y)")
		r = input()
		if r == "y":
			j_coord = (4,4)
			t_coord = [(3, 4)]
			d = 'down'
			x = ''
			points = 0
			die = False
		else :
			go = False
	elif j_coord == p_coord:
		points += 100
		t_coord = [j_coord] + t_coord
		p_coord = (random.randint(0, 8), random.randint(0, 8))
	x = ''


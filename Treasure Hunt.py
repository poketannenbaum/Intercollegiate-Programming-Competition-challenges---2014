treasurearr = [[0,0,0,0,0,0],[0,35,11,11,11,11],[0,11,11,11,11,11],[0,11,11,11,11,42],[0,11,42,11,11,11],[0,11,11,11,11,11]]
pointer = [1,1]
prevpoint = []
print("Started at 1 1")
while(True):
	prevpoint = pointer.copy()
	pointer = list(map(int, list(str(treasurearr[pointer[0]][pointer[1]]))))
	if prevpoint == pointer:
		print(f"Treasure is at: {pointer}")
		break
	print(f"Visited {pointer}")
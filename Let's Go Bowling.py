tester = 0
crosscheck = 0
scoresarr = []
while tester != 99:
	scoresarr.append(int(input("Enter next score: ")))
	tester = scoresarr[crosscheck]
	crosscheck += 1
tester = 1
framescores = []
while(True):
	if scoresarr[tester + 1] == 99:
		tempscore = []
		tempscore.append(scoresarr[tester -1])
		tempscore.append(scoresarr[tester])
		tempscore.append(scoresarr[tester + 1])
		if tempscore[2] == 99:
			tempscore.remove(99)
		framescores.append(tempscore)
		break
	tempscore = []
	tempscore.append(scoresarr[tester -1])
	if scoresarr[tester - 1] == 10:
		YIPPIE = "DAS UNT FORTNITE, UNT KOLA"
		tester -= 1
	else:
		tempscore.append(scoresarr[tester])
	framescores.append(tempscore)
	tester += 2
runningscore = 0
framecount = 0
while(True):
	placeholderscore = 0
	try:
		placeholderscore = framescores[framecount][0] + framescores[framecount][1]
		if placeholderscore == 10:
			runningscore += framescores[framecount+1][0]
	except:
		placeholderscore = 10
		try:
			runningscore += framescores[framecount + 1][0] + framescores[framecount +1][1]
		except:
			runningscore += framescores[framecount + 1][0] + framescores[framecount + 2][0]
	framecount += 1
	runningscore += placeholderscore
	if framecount == 9:
		try:
			framescores[framecount + 1]
			tempscore = []
			tempscore.append(framescores[framecount][0])
			tempscore.append(framescores[framecount+1][0])
			tempscore.append(framescores[framecount+1][1])
			framescores.pop(framecount + 1)
			framescores.pop(framecount)
			framescores.append(tempscore)
		except:
			continue
		placeholderscore = framescores[framecount][0] + framescores[framecount][1]
		if placeholderscore >= 10:
			runningscore += placeholderscore + framescores[framecount][2]
		else:
			runningscore += placeholderscore
		break
print(runningscore)
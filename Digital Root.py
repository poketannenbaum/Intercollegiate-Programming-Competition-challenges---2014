number = input("Number: ")
ognum = number
while(1 == 1):
	number = list(number)
	number = list(map(int, number))
	try:
		number[1]
	except:
		break
	placeholder = 0
	for num in number:
		placeholder += num
	number = str(placeholder)
print(f"The digital root of {ognum} is {placeholder}")
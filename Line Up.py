import re
numboys = input("Enter the number of boys: ")
boysheights = input("Enter the height of the boys: ")
numgirls = input("Enter the number of girls: ")
girlsheights = input("Enter the height of the girls: ")
boysheights = re.split (" ", boysheights)
girlsheights = re.split (" ", girlsheights)
allnums = []
for boy in boysheights:
	allnums.append(boy)
for boy in girlsheights:
	allnums.append(boy)
allnums.sort()
print(f"Line up: {allnums}")
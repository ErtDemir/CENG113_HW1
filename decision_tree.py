n = int(input("enter n : "))
uString = str(input("enter string : "))
mult = (n/(len(uString)))
if(type(mult) == float):
	mult += 1
uString = uString*int(mult)
sayac = 0
for i in range(n):
	if(uString[i] == "a"):
		sayac += 1

print(sayac)
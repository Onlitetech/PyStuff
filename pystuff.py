from string import *
def rot13(str):
	intab = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	outtab = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
	trantab = maketrans(intab, outtab)
	transs=str.translate(trantab);
	return transs
def fs(s):
	f=open(s,'r')
	words=0
	lines=0
	chars=0
	vowels=0
	cons=0
	vowels = ["a","A","e","E","i","I","o","O","u","U"]
	a = 0 #Current letter
	vow = 0
	cons = 0
	str = f.read()
	for x in str:
		if str[a] == x in vowels:
			vow +=1
		else:
			cons +=1
		a +=1

	if vow == 0:
		if "y" or "Y" in str[a]:
			vow +=1
			cons -=1 #remove 1 from cons, because the y has already been counted as a consonant.
	
	for line in f:
		words +=len(split(line))
		for x in split(line):
			chars +=len(x)
		lines +=1
	return "words: " + str(words) + " Lines: " + str(lines) + " Characters: " + str(chars) + "Vowels: " + str(vows) + "Consanants: " + str(cons)
def palin(str):
	a = len(str) # length of string
	b = a / 2 # half of string length
	c = 0 #Current letter in str
	prestring = [] #first half of string
	endstring = [] #last half of string
	while b > len(prestring):
		prestring.append(str[c])
		c += 1
		c += 1

	while b > len(endstring):
		endstring.append(str[c])
		c += 1
	
	endstring = endstring[::-1]
	if prestring == endstring:
		return "Palindrome"
	else:
		return "Not a palindrome"
def ode(n):
	int(n)
	if n % 2 != 0:
		print "Odd"
	else:
		print "Even"
def divis(num, divby):
	int(num)
	int(divby)
	if num % divby == 0:
		return num + " Is divisible by " + divby
	elif num % divby != 0:
		return num + " Is not divisible by " + divby
def fact(max, divby)
	int(max)
	int(divby)
	nums = range(max)
	nums +=1
	factors=[]
	for x in nums:
		if x % divby == 0:
			factors.append(x)
	return factors
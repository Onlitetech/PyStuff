from string import maketrans
def rot13(str):
	intab = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	outtab = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
	trantab = maketrans(intab, outtab)
	transs=str.translate(trantab);
	return transs
def lsf(s):
	f=open(s,'r')
	words=0
	lines=0
	chars=0
	for line in f:
		words +=len(split(line))
		for x in split(line):
			chars +=len(x)
		lines +=1
	return "words: " + str(words) + " Lines: " + str(lines) + " Characters: " + str(chars)
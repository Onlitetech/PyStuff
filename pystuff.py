from string import maketrans
def rot13(str):
	intab = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	outtab = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
	trantab = maketrans(intab, outtab)
	transs=str.translate(trantab);
	return transs

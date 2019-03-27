def replaceSpace(s,l):
	for i in range(l):
		if s[i] == ' ':
			s=s[:i]+'%20'+s[i+1:]
	return s	

def main():
	s = 'Mr John Smith	'
	l = 13
	r=replaceSpace(s,l)
	print(r)

main()

def stringUnique(s):
	if len(s) == len(set(s)):
	
		return True
	else:

		return False


def main():
	s='abca'
	print(stringUnique(s))

main()

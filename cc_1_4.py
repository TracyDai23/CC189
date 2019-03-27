#corner case: input is an empty string will return as True.

#logic: lower case input; check at most one character has single number of occurance; 

def palindromePermutate (s):
	s=s.lower()
	htable ={}
	for i in range(len(s)):
		if s[i] != ' ':
			try:
				htable.pop(s[i])
			except: 
				htable[s[i]]=1
	if len(htable)<=1:
		return True
	return False

def main():
	s = 'Tact Coa'
	r = palindromePermutate(s)
	print(r)

main()

#Hint asked to find algorithm with Time Complexity as nlog(n). Current solution only have O(n2)

#Dongdong's solution to work only on input string, no additional data structure:
def isUnique(strs):
	n=1
	for item in strs:
		if item not in strs[:n-1]:
			n=n+1
		else: return False
	return True
				 

#My list data structure only solution:
def stringUnique(s):
	d = []
	for i in range(len(s)):
		if s[i] in d: return False
		else: d.append(s[i])
	return True

# My 1st solution:
def stringUnique(s):
	if len(s) == len(set(s)):	
		return True
	else:
		return False


def main():
	s='abca'
	print(stringUnique(s))

main()

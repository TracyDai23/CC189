import time
import collections
def checkPermutation(s1,s2):
	a =collections.Counter(s1)
	b = collections.Counter(s2)
	if a==b: return True
	else: return False

def main():
	s1 = 'abca'
	s2 = 'cbaa'
	time1 = time.time()
	a=checkPermutation(s1,s2)
	time2 = time.time()
	print('run time: ',time2-time1)
	print(a)

main()

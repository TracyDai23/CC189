import unittest
def oneAway (s1, s2):
	if len(s1)< len(s2):
		s1,s2=s2,s1
	
	n=0
	while n <len(s2):	
		if s1[n] == s2[n]:
			s1 = s1[n+1:]
			s2 = s2[n+1:]
			n=n+1
			continue
		if len(s1) == len(s2):
			s1 = s1[n+1:]
			s2 = s2[n+1:]
		else: 
			s1 = s1[n+1:]
		if s1 != s2:
			return False


	return True
	
			

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'pkle', True)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = oneAway(test_s1, test_s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
	unittest.main()

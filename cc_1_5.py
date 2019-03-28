import unittest
def oneAway (s1, s2):
	print('s1, s2:',s1, s2)
	#corner case added after test
	if abs(len(s1) - len(s2))>1:
		return False
	
	if len(s1)< len(s2):
		s1,s2=s2,s1
	
	n=0
	while n <len(s2):	
		if s1[n] == s2[n]:
			s1 = s1[1:]
			s2 = s2[1:]
			n=n+1
			continue
		if len(s1) == len(s2):
			s1 = s1[1:]
			s2 = s2[1:]
		else: 
			s1 = s1[1:]
		if s1 != s2:
			return False


	return True
	
			

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'pkle', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
	('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = oneAway(test_s1, test_s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
	unittest.main()

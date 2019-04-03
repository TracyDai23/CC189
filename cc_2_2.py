from LinkedList import LinkedList
def kthtoLast (k, ll):
	if ll.size() = 0:
		return None
	s=ll.size()-k
	c = ll.head
	while s:
		c = c.getNext()
		s-=1
	else:
		return c.getData()
	
def main():
	k=3
	ll = LinkedList()
	ll.add('3')
	ll.add('4')
	ll.add('5')
	ll.add('6')
	print(kthtoLast(k,ll))

main()
	


from LinkedList import LinkedList
def removeDup(ll):
	a = []
	#check l.val,if not in a then add value into a, else remove node from l. 
	c = ll.head
	while c:
		if c.getData() not in a:
			a.append(c.getData())
			c=c.getNext()
		else:
			ll.remove(c.getData())
			c=c.getNext()

	return ll

ll = LinkedList()
ll.add(1)
ll.add(3)
ll.add(5)
ll.add(3)

r=removeDup(ll)
n=r.head
while n:
	print(n.getData())
	n=n.getNext()

		

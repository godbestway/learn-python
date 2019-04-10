#before: head 1>2>3>4>5>6>7
#after:  head 7>6>5>4>3>2>1
#explain List: the type of LNode.data is int
#	       the type of LNode.next is instance




class LNode:
	def _new_(self,x):
		self.data=x
		self.next=None

def reverse(head):
	if head == None or head.next == None:
		return
	next = None
	cur = head	
	pre = None
	
	while cur != None:
		next = cur.next
		cur.next = pre
		pre = cur
		cur = next
		
	return pre



		
#prove the algorithm
if __name__=="__main__":
	five = LNode()
	five.data = 5
	five.next = None
 
	four = LNode()
	four.data = 4
	four.next = five

	three = LNode()
	three.data = 3
	three.next = four
	
	two = LNode()
	two.data = 2
	two.next = three
	

	one = LNode()
	one.data = 1
	one.next = two

	head = LNode()
	head.data = None
	head.next = one
 	
	print"before reverse"
	old_head = head
	while old_head != None:
		if old_head.data != None:
			print old_head.data
		old_head = old_head.next
	
	
	print"after reverse"
	new_head = reverse(head)
	
	while new_head != None:
		if new_head.data != None:
			print new_head.data
		new_head = new_head.next





	












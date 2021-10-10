class deque:
    	def __init__(self):
		self.items = []
		
	def __init__(self, s):
		self.items = []
		
	def append(self, c):
		self.items.append(c)
	
	def appendleft(self, c):
		self.items.appendleft(c)
	
	def pop(self):
		self.items.pop()
	
	def popleft(self):
		self.items.popleft()
		
	def __len__(self):
		return len(self.items)
	
	def right(self):
		return self.items[0]
	
	def left(self):
		return self.items[-1]
		


from collections import deque

def check_palindrome(s):
	dq = deque(s)
	palindrome = True
	
	while len(dq) > 1:
		if dq.popleft() != dq.pop():
			palindrome = False
			
	return palindrome

n = input()
print(check_palindrome(n))
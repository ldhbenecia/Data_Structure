# stack_queue.py 에 저장
class Queue:
	def __init__(self):
		self.items = []	# 데이터 저장을 위한 리스트 준비
	def enqueue(self, val):
		self.items.append(val)
	def dequeue(self):
		try:	# pop할 아이템이 없으면
			return self.items._____________ # 어떤 함수를 호출해야 할까?
		except IndexError:	# indexError 발생
			print("Queue is empty")
	def front(self):
		try:
			return self.items[______]  # 어떤 값이 와야할까?
		except IndexError:
			print("Queue is empty")
	def __len__(self):	# len()로 호출하면 stack의 item 수 반환
 		return len(self.items)
	def isEmpty(self):
		return len(self)
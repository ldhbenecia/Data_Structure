class Queue:
    def __init__(self):
        self.item = []
        self.front_index = 0
        
    def enqueue(self, val):
        self.item.append(val)
        
    def dequeue(self):
        if (self.front_index == len(self.item)): # 큐가 비어있음
            print("Queue is empty!")
            return None
        else:
            x = self.item[self.front_index]
            self.front_index += 1
            return x
    
    def isEmpty(self):
        if (self.front_index == len(self.item)):
            print("Queue is empty!")
        else:
            return len(self.item) - self.front_index
        
    def front(self): # 가장 왼쪽에 저장된 값을 삭제하지 않고 리턴
        return self.item[self.front_index]
    
    def len(self):
        return len(self.item) - self.front_index


class Node:
    def __init__(self,element):
        self.data = element
        self.link = None

'''
head = Node(10)        #head--> 10 ---> 20 ---> 30
head.link = Node(20)
head.link.link = Node(30)
#print(head.data, head.link.data, head.link.link.data)
#head--> 10 ---> 20 ---> 30

node = Node(50)  # node -> 50 None
node.link = head
head = node   #head -> 50 -> 10 -> 20  -> 30
#print(head.data, head.link.data, head.link.link.data, head.link.link.link.data)
    
#head -> 50 -> 10 -> 20  -> 30
#       node
#head -> 50 -> 10 -> 20  -> 30
#             node
    
node = head
print(node.data) # 50
node = node.link
print(node.data) # 10
node = node.link
print(node.data) # 20
node = node.link
print(node.data) # 30
node = node.link
print(node) # None
    
node = head
while node != None:
    print(node.data, end = ' ') # 50 10 20 30
    node = node.link
print()
'''

# 연결리스트를 만드는 방법 1: insertFront를 이용
def insertFront(head, e):   #
    node = Node(e)
    node.link = head
    return node


head = None
head = insertFront(head, 30)
# head -> 30
head = insertFront(head, 20)
# head -> 20 -> 30
head = insertFront(head, 10)
# head -> 10 -> 20 -> 30
head = insertFront(head, 50)
# head -> 50 -> 10 -> 20 -> 30

node = head
while node != None:
    print(node.data, end = ' ') # 50 10 20 30
    node = node.link

print()
     
def printList(head):
    node = head
    while node != None:
        print(node.data, end = ' ')
        node = node.link
    print()
    

# 클래스를 이용한 연결리스트     
class LinkedList:
    def __init__(self):
        self.head = None
  
    def insertFront(self, e):
        node = Node(e)
        node.link = self.head
        self.head =  node

#    def insert(self,pos,e):      
#    def delete(self,pos):

    def printList(self):
        node = self.head
        while node != None:
            print(node.data, end = ' ')
            node = node.link
        print()
            
def linkedListPractice():
    L = LinkedList()
    L.insertFront(20)
    L.insertFront(40)
    L.insertFront(30)
    L.printList() # 30 40 20
    L.insertFront(25) # 25 30 40 20
    L.printList()
    

linkedListPractice()

    

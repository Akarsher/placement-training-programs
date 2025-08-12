# Singly Linkedlist implementation
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 

class Singly_Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def Print_list(self):
        if self.head == None:
            print("Empty list")
        else:
            currnode = self.head
            while currnode:
                print(f' {currnode.data} ->',end="")
                currnode = currnode.next
            print('None')
    
    def Insert_end(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode

list1 = Singly_Linkedlist()
while True:
    print('0 - Exit')
    print('1 - Print list')
    print('2 - Insert end')
    print('3 - Insert begin')
    print('4 - Delete end')
    print('5 - Delete begin')
    n = int(input())
    if n==0:
        break
    elif n==1:
        list1.Print_list()
    elif n==2:
        data = int(input())
        list1.Insert_end(data)
    
        

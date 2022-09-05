class node:
    def __init__(s,x):
        s.data = x
        s.prev = None
        s.next = None
        
class DLL:
    def __init__(s):
        s.head = None
        
    def insertFront(s,x):
            new_node = node(x)
            if s.head != None:
                new_node.next = s.head
                s.head.prev = new_node
            s.head = new_node
    def display(s):
        if s.head == None:
            print("Empty list")
            return
        t = s.head
        while t != None:
            print(t.data,end="-->")
            t = t.next
        print("None")
    def delete(s,x):
        t = s.head
        while t != None and t.data != x:
            t = t.next
        if t == None:
            print("Value not found")
            return
        if s.head.data == x:
            s.head = s.head.next 
            s.head.prev = None
        return
        t.prev.next = t.next
        t.next.prev = t.prev
            
list1 = DLL()

list1.insertFront(50)
list1.insertFront(40)
list1.insertFront(30)
list1.insertFront(20)
list1.display()
list1.delete(100)
list1.display()

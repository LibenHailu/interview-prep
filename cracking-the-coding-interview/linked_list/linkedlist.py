
class LinkedListNode:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    def addToTail(self,val):
        node = LinkedListNode(val)
        n = self.head
        while n:
            n = n.next
            print("here")
        n = node
        print(node.val,n.val,self.head)
    
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __str__(self) -> str:
        values = [str(x) for x in self]
        print(values,self.head)
        return " -> ".join(values)

ll = LinkedList()
ll.addToTail(5)
print(ll.__str__())

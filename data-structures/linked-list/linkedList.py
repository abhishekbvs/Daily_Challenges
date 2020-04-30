class Node:

    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None

    def printList(self):
        
        temp = self.head
        while(temp):
            print(temp.data, end=" => ")
            temp = temp.next
        print('#')
    
    def insertFirst(self, data):
        
        if self.head is not None:

            temp = self.head
            self.head = Node(data)
            self.head.next = temp

        else:

            self.head = Node(data)
    
    def insertLast(self, data):
        
        if self.head is not None:
            
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = Node(data)
        
        else:

            self.head = Node(data)

    def insertAfter(self,prev_node,data):

        
        if prev_node is None:
            print("prev_node should be in linked list")
            return

        temp = prev_node.next
        prev_node.next = Node(data)
        prev_node.next.next = temp

    def deleteAt(self, data):

        if self.head.data == data:
            self.head = self.head.next
        else:
            temp = self.head
            while(temp.next):
                if temp.next.data == data:
                    temp.next = temp.next.next
                    break
                temp = temp.next

    def deleteAtPos(self,pos):

        if pos == 0:
            self.head = self.head.next
        else:
            c = 1
            prev = self.head
            temp = self.head.next
            while temp:
                if c == pos:
                    prev.next = temp.next
                    break
                prev = temp
                temp = temp.next
                c+=1
    
    def length(self):
        l = 0
        temp = self.head
        while(temp):
            l+=1
            temp = temp.next
        return l

    def lengthrec(self, node):
        if not node:
            return 0
        else:
            return 1+self.lengthrec(node.next)

    def swap(self,key1,key2):
        temp1=self.head
        x1 = 1
        temp2=self.head
        x2 = 1

        while x1 or x2:
            if x1 and temp1.data==key1:
                x1=0
            elif x1!=0:
                temp1=temp1.next
            if x2 and temp2.data==key2:
                x2=0
            else:
                temp2=temp2.next

if __name__ == '__main__':

    llist = LinkedList()
    llist.insertLast(2)
    llist.insertLast(3)
    llist.insertFirst(4)
    llist.insertAfter(llist.head,1)
    llist.printList()
    # llist.deleteAt(3)
    # llist.printList()
    # llist.deleteAtPos(2)
    # llist.printList()
    print(llist.length())
    print(llist.lengthrec(llist.head))
    # llist.swap(2,1)


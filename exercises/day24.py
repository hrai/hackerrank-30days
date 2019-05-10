class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next


    def removeDuplicates(self,head):
        #Write your code here
        if not head:
            return head 

        current=head
        while current and current.next:
            if current.data == current.next.data:
                current.next=current.next.next
                continue

            current = current.next

        return head

mylist= Solution()
# T=int(input())
numList=[ 3, 9, 9, 11, 11, 11, 11, 89, 89, 100, 100, 101, 102, 103, 108, 200, 250, 250, 250, 250]

head=None
for i in numList:
    data=i
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 

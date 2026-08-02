#206. Reverse Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from pyparsing import Optional
from ast import ListNode




class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        curr=head
        while curr:
            t=curr.next
            curr.next=prev
            prev=curr
            curr=t
        return prev

#21. Merge Two Sorted Lists

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        curr=dummy
        while list1 and list2:
            if list1.val < list2.val:
                curr.next=list1
                curr=list1
                list1=list1.next
            else:
                curr.next=list2
                curr=list2
                list2=list2.next
        curr.next=list1 if list1 else list2
        return dummy.next
#876. Middle of Linked List
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next #fast is the twice of slow
            fast=fast.next.next
        return slow



#141. Linked List Cycle
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                return True
        return False

#203. Remove Linked List Elements
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy =ListNode(next=head)
        prev,curr=dummy,head
        while curr:

            next=curr.next
            if curr.val==val:
                prev.next=next
            else:
                prev=curr
            curr=next
        
        return dummy.next

#707. Design Linked List
class ListNode:
    def __init__(self,val):
        self.val=val
        self.prev=None
        self.next=None

class MyLinkedList:

    def __init__(self):
        self.left=ListNode(0)
        self.right=ListNode(0)
        self.left.next=self.right
        self.right.prev=self.left

    def get(self, index: int) -> int:
        cur=self.left.next
        while cur and index>0:
            cur=cur.next
            index -= 1
        if cur and cur!= self.right and index==0:
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        node,next,prev=ListNode(val), self.left.next , self.left
        prev.next=node
        next.prev=node
        node.next=next
        node.prev=prev
    def addAtTail(self, val: int) -> None:
        node,next,prev=ListNode(val), self.right , self.right.prev
        prev.next=node
        next.prev=node
        node.next=next
        node.prev=prev

    def addAtIndex(self, index: int, val: int) -> None:
        cur=self.left.next
        while cur and index > 0:
            cur=cur.next
            index -= 1 
        if cur and index==0:
            node,next,prev=ListNode(val), cur , cur.prev
            prev.next=node
            next.prev=node
            node.next=next
            node.prev=prev


    def deleteAtIndex(self, index: int) -> None:
        cur=self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and cur!= self.right and index==0:
            next,prev = cur.next, cur.prev
            next.prev=prev
            prev.next=next

#19. Remove Nth Node From End
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy  = ListNode(0,head)
        left=dummy
        right=head
        while n > 0 and right:
            right = right.next
            n -= 1
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next

#92. Reverse Linked List II
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        leftPrev,cur=dummy,head
        for i in range(left - 1):
            leftPrev,cur=cur,cur.next
        prev=None
        for i in range(right - left + 1):
            tmpNext= cur.next
            cur.next=prev
            prev,cur=cur,tmpNext
        leftPrev.next.next=cur
        leftPrev.next=prev
        return dummy.next

#143. Reorder List
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #find middle
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            #reverse second half
        second=slow.next
        prev=slow.next=None
        while second:
            tmp=second.next
            second.next=prev
            prev=second
            second=tmp
            #merge two halfs
        first,second=head,prev
        while second:
            tmp1,tmp2=first.next,second.next
            first.next=second
            second.next=tmp1
            first,second=tmp1,tmp2

#25. Reverse Nodes in K-Group
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        groupPrev=dummy
        while True:
            kth=self.getKth(groupPrev,k)
            if  not kth:
                break
            groupNext=kth.next
            prev,cur=kth.next,groupPrev.next
            while cur != groupNext:
                tmp=cur.next
                cur.next=prev
                prev=cur
                cur=tmp
            tmp=groupPrev.next
            groupPrev.next=kth
            groupPrev=tmp
        return dummy.next
    def getKth(self,cur,k):
        while cur and k > 0:
            cur=cur.next
            k -=1
        return cur
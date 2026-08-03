#707 – Design Linked List

from pyparsing import Optional
#listNode does not exists in python ast module """dont use from ast import ListNode"""
class Node:                    
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

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



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)



#1472 – Design Browser History
class BrowserHistory:

    def __init__(self, homepage: str):
        self.i=0
        self.len=1
        self.history=[homepage]


    def visit(self, url: str) -> None:
        if len(self.history) < self.i + 2:
            self.history.append(url)
        else:
            self.history[self.i + 1]=url
        self.i += 1
        self.len = self.i + 1

    def back(self, steps: int) -> str:
        self.i=max(self.i - steps ,0)
        return self.history[self.i]

    def forward(self, steps: int) -> str:
        self.i=min(self.i + steps , self.len - 1)
        return self.history[self.i]



#430 – Flatten a Multilevel Doubly Linked List

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """def dfs(node):
            curr = node
            last = None

            while curr:
                nxt = curr.next

                if curr.child:
                    child_tail = dfs(curr.child)

                    curr.next = curr.child
                    curr.child.prev = curr

                    if nxt:
                        child_tail.next = nxt
                        nxt.prev = child_tail

                    curr.child = None
                    last = child_tail
                else:
                    last = curr

                curr = nxt

            return last

        dfs(head)
        return head"""

#using stack
        stack=[]
        start =head
        while head:
            if head.child:
                if head.next:
                    stack.append(head.next)
                head.next=head.child
                head.next.prev=head
                head.child=None

            if head.next==None and len(stack) != 0:
                head.next=stack.pop()
                head.next.prev=head
            head=head.next
        return start



#146 – LRU Cache 
class Node:
    def __init__(self,key,val):
        self.key, self.val=key,val
        self.prev=self.next=None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache={}
        self.left,self.right=Node(0,0), Node(0,0)
        self.left.next,self.right.prev=self.right,self.left
    def remove(self,node):
        prev,nxt=node.prev,node.next
        prev.next,nxt.prev=nxt,prev
    def insert(self,node):
        prev,nxt=self.right.prev,self.right
        prev.next=nxt.prev=node
        node.next,node.prev=nxt,prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


#432 – All O(1) Data Structure
class Bucket:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:

    def __init__(self):
        self.head = Bucket(0)
        self.tail = Bucket(0)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.keyBucket = {}

    def insertAfter(self, node, newNode):
        newNode.next = node.next
        newNode.prev = node

        node.next.prev = newNode
        node.next = newNode

    def removeBucket(self, bucket):
        bucket.prev.next = bucket.next
        bucket.next.prev = bucket.prev

    def inc(self, key: str) -> None:
        if key not in self.keyBucket:

            if self.head.next == self.tail or self.head.next.count != 1:

                newBucket = Bucket(1)

                self.insertAfter(self.head, newBucket)

            self.head.next.keys.add(key)

            self.keyBucket[key] = self.head.next

        else:

            bucket = self.keyBucket[key]

            nxt = bucket.next

            if nxt == self.tail or nxt.count != bucket.count + 1:

                newBucket = Bucket(bucket.count + 1)

                self.insertAfter(bucket, newBucket)

                nxt = newBucket

            nxt.keys.add(key)

            self.keyBucket[key] = nxt

            bucket.keys.remove(key)

            if len(bucket.keys) == 0:
                self.removeBucket(bucket)

    def dec(self, key: str) -> None:
        if key not in self.keyBucket:
            return

        bucket = self.keyBucket[key]

        if bucket.count == 1:

            del self.keyBucket[key]

        else:

            prev = bucket.prev

            if prev == self.head or prev.count != bucket.count - 1:

                newBucket = Bucket(bucket.count - 1)

                self.insertAfter(prev, newBucket)

                prev = newBucket

            prev.keys.add(key)

            self.keyBucket[key] = prev

        bucket.keys.remove(key)

        if len(bucket.keys) == 0:
            self.removeBucket(bucket)
        

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""

        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
         if self.head.next == self.tail:
            return ""
    

         return next(iter(self.head.next.keys))
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
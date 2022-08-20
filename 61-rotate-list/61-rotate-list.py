# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def node_length(self, head: Optional[ListNode]):
        tail = head
        n = 1
        while tail.next:
            n += 1
            tail = tail.next
        return n
    
    def move(self, head: Optional[ListNode], k: int):
        tail = head
        for _ in range(k):
            tail = tail.next
        return tail
        
    def append(self, node: Optional[ListNode], head: Optional[ListNode]):
        cur = node
        while node.next:
            node = node.next
        node.next = head
        return cur
        
    #k 이후 전부 삭제
    def remove(self, node: Optional[ListNode], k:int):
        cur = node
        node = self.move(node,k-1)
        node.next = None
        return cur
        
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        n = self.node_length(head)
        
        if n < k:
            k = k % n
        if k == 0 or n-k == 0:
            return head
        
        tail = self.move(head, n-k)
            
        node = ListNode(tail.val, tail.next)
        head = self.remove(head, n-k)
        node = self.append(node, head)
        
        return node
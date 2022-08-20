# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        tail = head
        n = 1
        while tail.next:
            n += 1
            tail = tail.next
        if n < k:
            k = k % n
            
        if k == 0:
            return head
        
        tail = head
        for _ in range(n-k):
            tail = tail.next
            
        node = ListNode()
        node.val = tail.val
        node.next = tail.next
        
        cur = node
        
        while node.next:
            node = node.next
            
        node.next = head
        
        for _ in range(n-k):
            node = node.next
            
        node.next = None
        
        return cur
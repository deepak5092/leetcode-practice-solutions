# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # implement gcd
        def divi(a, b):
            pass
        
        curr = head
        while curr and curr.next:
            new_val = gcd(curr.val, curr.next.val)

            new_node = ListNode(new_val, curr.next)
            curr.next = new_node
            curr = new_node.next
        
        return head
            
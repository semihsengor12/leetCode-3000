# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return

        dummyNode = ListNode(0)
        dummyNode.next = head
        
        curr = head
        while curr.next:
            temp = curr.next 
            curr.next = curr.next.next

            temp.next = dummyNode.next
            dummyNode.next = temp
        
        return dummyNode.next
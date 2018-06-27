# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        pro = None
        
        while (curr):
            pro = curr.next
            curr.next = prev
            prev = curr
            curr = pro
    
        self.head = prev
        return self.head


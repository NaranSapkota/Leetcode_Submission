# Last updated: 12/5/2025, 12:43:00 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        fast=head
        slow=head
        
        # finding the middle and slow 
        while  fast  and fast.next:
            fast=fast.next.next
            slow=slow.next
        
        # reverse second half
        prev=None
        while slow:
            tmp=slow.next
            slow.next=prev
            prev=slow
            slow=tmp
            
        #check palindrome
        l,r =head,prev
        
        while r:
            if l.val  != r.val:
                return False
            l=l.next
            r=r.next
        return True
            
            
        
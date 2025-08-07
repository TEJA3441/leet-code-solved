# Definition for singly-linked list.
import math
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        cnt=0
        dummy=ListNode(0)
        if temp.next is None:
            return temp

        while temp:
            temp=temp.next
            cnt+=1
        res=(cnt//2)
        temp=head
        while res>1:
            temp=temp.next
            res-=1
        dummy.next=temp.next
        return dummy.next
        

        


        
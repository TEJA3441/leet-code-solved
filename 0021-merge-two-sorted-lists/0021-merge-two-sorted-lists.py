# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        dummy=ListNode(0)
        temp=dummy
        l1=list1
        l2=list2
        while l1 and l2:
            if l1.val >= l2.val:
                temp.next=l2
                l2=l2.next
                temp=temp.next
            else:
                temp.next=l1
                l1=l1.next
                temp=temp.next

        if l1:
            temp.next=l1
        else:
            temp.next=l2
        return dummy.next
        
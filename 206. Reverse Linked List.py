#206. Reverse Linked List
#https://leetcode.com/problems/reverse-linked-list/submissions/
#my ans
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dummy_head=sublist_head=ListNode(0, head)
        length, data=0, []
        while sublist_head.next:
            data.append(sublist_head.next.val)
            sublist_head=sublist_head.next
            length+=1
        for i in range(length):
            head.val=data[~i]
            head=head.next
        return dummy_head.next


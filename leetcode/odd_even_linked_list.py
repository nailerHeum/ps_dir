# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        return_head = head
        even_head = None
        cur_even = None
        cur_head = head
        while cur_head and cur_head.next:
            if cur_even:
                cur_even.next = cur_head.next
                cur_even = cur_even.next
            else:
                even_head = cur_head.next
                cur_even = even_head
            cur_head.next = cur_head.next.next
            if not cur_head.next:
                break
            cur_head = cur_head.next
        if cur_even:
            cur_even.next = None
        if cur_head:
            cur_head.next = even_head
        return return_head
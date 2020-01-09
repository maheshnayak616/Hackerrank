# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        length = self.lengthOfLinkedList(head)
        ans = 0
        while head:
            ans += head.val * math.pow(2, length)
            length -= 1
            head = head.next
        return int(ans)

    def lengthOfLinkedList(self, head):
        length = 0
        curr = head
        if curr:
            while curr.next:
                length += 1
                curr = curr.next
        return length
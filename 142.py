class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            # if there is a cycle
            if slow is fast:
                # the head and slow nodes move step by step
                while head:
                    if head == slow:
                        return head
                    head = head.next
                    slow = slow.next
        return None

a = Solution()
b = ListNode(1)
c = ListNode(2)
b.next = c
c.next = b
print a.detectCycle(b).val




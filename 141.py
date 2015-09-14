class Solution(object):
    def hasCycle(self, head):
        fast = slow = head
        if fast and fast.next and fast.next.next:
            fast = fast.next.next
        else:
            return False
        while True:
            if not fast or not fast.next:
                return False
            elif fast == slow or fast.next == slow:
                return True
            else:
                fast = fast.next.next
                slow = slow.next

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        if k == 0 or head is None:
            return head
        temp = head
        l = 1
        while temp.next != None:
            temp = temp.next
            l += 1
        temp.next = head
        if k >= l:
            k = k%l
        k = l-k-1
        while k > 0:
            k -= 1
            head = head.next
        result = head.next
        head.next = None
        return result 

a = Solution()
x = ListNode(1)
##y = x
##for i in xrange(2,3):
##    y.next = ListNode(i)
##    y = y.next
print a.rotateRight(x,1)

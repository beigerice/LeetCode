from random import randint
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head. Note that the head is guanranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        temp = self.head
        res = temp.val
        l = 0
        while temp.next:
            temp = temp.next
            l += 1
            if randint(0,l) == 0:
                res = temp.val
        return res
            


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

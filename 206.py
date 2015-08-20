class Solution:
    def reverseList(self, head):
        if head:
            temp = None
            while head.next != None:
                the = head.next
                head.next = temp
                temp = head
                head = the
            head.next = temp
            return head

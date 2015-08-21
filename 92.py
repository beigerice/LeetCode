class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        n -= m
        if n == 0:
            return head
        if head:
            if m == 1:
                x = head
                previous = head
                head = head.next
                if n == 1:
                    x.next,head.next = head.next,x
                    return head
                else:
                    while n > 1:
                        hou = head.next
                        head.next = previous
                        previous = head
                        head = hou
                        n -= 1
                    x.next,head.next = head.next,previous
                    return head
            else:
                toreturn = head
                while m > 2:
                    head = head.next
                    m -= 1        
                x = head
                head = head.next
                y = head
                temp = y
                head = head.next
                if n == 1:
                    x.next = head
                    y.next,head.next = head.next,y
                    return toreturn
                else:
                    while n > 1:
                        the = head.next
                        head.next = temp
                        temp = head
                        head = the
                        n -= 1
                    x.next = head
                    y.next,head.next = head.next,temp
                    return toreturn
        

a = Solution()
alpha = ListNode(1)
beta = ListNode(2)
gamma = ListNode(3)
lala = ListNode(4)
alpha.next = beta
beta.next = gamma
gamma.next = lala
print a.reverseBetween(alpha,2,4).next.val


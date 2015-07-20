class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def addTwoNumbers(self, l1, l2):
        temp1 = 0
        d = 0
        while l1.next != None:
            temp1 += l1.val*10**d
            l1 = l1.next
            d += 1
        temp1 += l1.val*10**d
        temp2 = 0
        d = 0
        while l2.next != None:
            temp2 += l2.val*10**d
            l2 = l2.next
            d += 1
        temp2+= l2.val*10**d
        temp = temp1+temp2
        result = []           
        for i in xrange(len(str(temp))):
            result.append(ListNode(int(str(temp)[i])))
        for i in xrange(len(result)-1,0,-1):
            result[i].next = result[i-1]
        return result[-1]

a = Solution()
a1 = ListNode(1)
x1 = ListNode(8)
a1.next = x1

a2 = ListNode(0)

print a.addTwoNumbers(a1,a2).next.val
                

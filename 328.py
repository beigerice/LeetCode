class Solution(object):
    def oddEvenList(self, head):
        odd_pre = head
        if not head or not head.next or not head.next.next:
            return head
        even_pre = head.next
        odd_head = head
        even_head = head.next
        while odd_pre.next and even_pre.next:
            odd = even_pre.next
            even = odd.next
            odd_pre.next = odd
            even_pre.next = even        
            odd_pre = odd
            even_pre = even
        odd.next = even_head
        return odd_head

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        hresult = ListNode(0)
        result = l1
        l1.val += l2.val
        while l1.next and l2.next:
            if l1.val > 9:
                l1.val %= 10
                l1.next.val += 1
            l1.next.val += l2.next.val
            l1 = l1.next
            l2 = l2.next

        if l2.next != None:
            l1.next = l2.next

        while l1.val > 9:
            l1.val %= 10
            if l1.next:
                l1.next.val += 1
                l1 = l1.next
            else:
                l1.next = ListNode(1)
        
        return result
                

                

                

                

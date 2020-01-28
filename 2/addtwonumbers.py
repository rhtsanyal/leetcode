from Common import ListNode,stringToListNode
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        l3 = ListNode(-1)
        head = l3
        while l1 or l2:
            val1,val2 = 0,0
            if l1:
                val1 = l1.val
            if l2:
                val2 = l2.val
            sum = val1 + val2 + carry
            if sum > 9:
                sum = sum % 10
                carry = 1
            else:
                carry = 0
            l3.next = ListNode(sum)
            l3 = l3.next
            if l2:
                l2 = l2.next
            if l1:
                l1= l1.next
        if carry == 1:
            l3.next = ListNode(carry)
        return head.next












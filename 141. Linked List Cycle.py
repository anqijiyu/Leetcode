# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#方法：设置两个指针，第一个指针从头开始每次走两步，第二个指针每次走一步，如果第一个指针追上了第二个指针，就是循环链表
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast=slow=head
        if fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                return True
        return False

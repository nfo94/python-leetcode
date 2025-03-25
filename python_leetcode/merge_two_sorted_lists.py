from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy_node = ListNode()
        tail = dummy_node

        while list1.next and list2.next:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # If list1 still has items and list2 doesn't
        if list1:
            tail.next = list1
        # If list2 still has items and list1 doesn't
        elif list2:
            tail.next = list2

        return dummy_node.next


test = Solution()
test.mergeTwoLists([1, 2, 4], [1, 3, 5])

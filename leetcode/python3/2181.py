from typing import Optional, List
# https://leetcode.com/problems/merge-nodes-in-between-zeros/description/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def arr_to_linked_list(arr: List):
    result_node = []
    arr.reverse()
    for i, e in enumerate(arr):
        if i > 0:
            node = ListNode(e, result_node[i-1])
        else:
            node = ListNode(e, None)

        result_node.append(node)
    head = node
    return head

def print_linked_list(head: ListNode):
    cur = head
    str_print = ""
    while cur is not None:
        str_print += str(cur.val)
        if cur.next is not None:
            str_print += " -> "
        cur = cur.next
    return str_print

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def merge(this_node: ListNode, next_node: ListNode):
            this_node.val = this_node.val + next_node.val
            this_node.next = next_node.next
            return this_node

        def delete_zeros(head: ListNode):
            cur = head
            while cur is not None:
                if cur.next is None:
                    cur = None
                    break
                if cur.next.val == 0:
                    next_node = cur.next
                    if next_node.next is not None:
                        cur.next = next_node.next
                    else:
                        cur.next = None
                    del next_node
                cur = cur.next

            if head.val == 0:
                head = head.next
            return head



        # iterating node
        cur = head
        while cur is not None:
            # check if cur is 0
            if cur.val == 0:
                cur = cur.next
                continue

            # cur is not None
            # check if cur.next is None:
            if cur.next is None:
                cur = cur.next
                # we stop next iter
                continue

            # next value is 0, move on
            if cur.next.val == 0:
                cur = cur.next
                continue
            # next value is not 0, we merge until it is 0
            while cur.next is not None and cur.next.val != 0:
                cur = merge(cur, cur.next)

            cur = cur.next

        head = delete_zeros(head)
        return head
"""
You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.

For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.

Return the head of the modified linked list.
"""
if __name__ == "__main__":
    head_arr = [0,3,1,0,4,5,2,0]
    head = arr_to_linked_list(head_arr)
    print(print_linked_list(head))
    sol = Solution()
    head2 = sol.mergeNodes(head)
    print(print_linked_list(head2))

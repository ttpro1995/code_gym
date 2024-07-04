from typing import Optional, List

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
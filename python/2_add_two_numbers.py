from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'ListNode({self.val})'


def initialize_numbers(l):
    return ListNode(l[0], ListNode(l[1], ListNode(l[2])))


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    carry = 0
    result_node_head = ListNode()
    current_node = result_node_head
    while True:

        if l1 is None:
            l1 = ListNode()
        if l2 is None:
            l2 = ListNode()

        current_sum = l1.val + l2.val + carry
        carry = current_sum // 10
        current_sum -= carry * 10

        current_node.val = current_sum

        l1 = l1.next
        l2 = l2.next

        if l1 is None and l2 is None and carry == 0:
            break

        current_node.next = ListNode()
        current_node = current_node.next

    return result_node_head


if __name__ == '__main__':
    list_1 = initialize_numbers([2, 4, 3])
    list_2 = initialize_numbers([5, 6, 4])

    output = add_two_numbers(list_1, list_2)
    while output is not None:
        print(output.val, end='')
        output = output.next

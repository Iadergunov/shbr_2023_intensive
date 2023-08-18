"""
Разворот односвязного списка
"""


class Node:
    def __init__(self, value, next_el):
        self.value = value
        self.next_el = next_el


def reverse_list(head: Node):
    def reverse_node(node: Node, parent: Node):
        next_el = node.next_el
        node.next_el = parent
        if next_el:
            return reverse_node(next_el, node)
        else:
            return node

    next_node = head.next_el
    head.next_el = None
    return reverse_node(next_node, head)


def print_list(head: Node):
    ans = [head.value]
    next_node = head.next_el
    while next_node:
        ans.append(next_node.value)
        next_node = next_node.next_el

    print(*ans)


node_5 = Node(5, None)
node_4 = Node(4, node_5)
node_3 = Node(3, node_4)
node_2 = Node(2, node_3)
test_head = Node(1, node_2)

print_list(test_head)
new_head = reverse_list(test_head)
print_list(new_head)

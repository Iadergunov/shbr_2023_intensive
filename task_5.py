"""
Обход дерева в ширину
"""
from collections import deque


def tree_bfs(tree, start) -> str:
    answer = []

    candidates = deque()
    candidates.append(start)
    while candidates:
        next_node = candidates.popleft()
        answer.append(next_node)
        for child in tree.get(next_node, []):
            candidates.append(child)

    return "".join(answer)


test_tree = {
    "b": ["h", "i"],
    "h": ["a", "j"],
    "j": ["d"],
    "i": ["k", "l"],
    "k": ["e", "f", "g"]
}

assert tree_bfs(test_tree, start="b") == "bhiajkldefg"

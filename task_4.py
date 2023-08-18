"""
Обход дерева в глубину
"""


def dfs_tree(tree: dict[str, list], start: str):
    def dfs(node, path):
        path.append(node)
        for child in tree[node]:
            if child is not None:
                dfs(child, path)

    answer = []
    dfs(start, answer)
    return "".join(answer)


test_tree = {
    "F": ["B", "G"],
    "B": ["A", "D"],
    "A": [None, None],
    "D": ["C", "E"],
    "C": [None, None],
    "E": [None, None],
    "G": [None, "I"],
    "I": ["H", None],
    "H": [None, None]
}
assert dfs_tree(test_tree, start="F") == "FBADCEGIH"

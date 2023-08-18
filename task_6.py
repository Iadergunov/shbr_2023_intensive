"""
Правильная скобочная последовательность
"""


def check_brackets(line: str) -> bool:
    started = 0
    for ch in line:
        if ch == "(":
            started += 1
        elif ch == ")":
            if started == 0:
                return False
            else:
                started -= 1

    return started == 0


assert check_brackets("()((()))()") is True
assert check_brackets("()(((()))()") is False
assert check_brackets("()(") is False

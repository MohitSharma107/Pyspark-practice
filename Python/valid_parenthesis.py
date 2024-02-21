"""
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

def isValid(s):
    mapping = {"(":")","{":"}","[":"]"}
    stack = []
    for char in s:
        if char in ["(","{","["]:
            stack.append(mapping[char])
        elif len(stack) == 0 or stack.pop() != char:
            return False
    return not len(stack) != 0



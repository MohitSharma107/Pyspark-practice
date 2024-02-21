"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
"""

def evalRPN(tokens):
    #If the ele is number then. Stack -> push
    #If the ele is operator. Pop two elements of stack and perfrom operation
    # After performing operation store the values back in stack.
    stack = []
    for token in tokens:
        if token in ["+","-","*","/"]:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a+b)
            elif token == "-":
                stack.append(a-b)
            elif token == "*":
                stack.append(a*b)
            else:
                stack.append(int(a/b))
        else:
            stack.append(int(token))
    return stack.pop()
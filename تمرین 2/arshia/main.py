def precedence(op):
    if op == '+' or op == '-':
        retdef precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0

def to_postfix(expression):
    stack = []
    result = []
    for char in expression:
        if char.isalnum(): 
            result.append(char)
        else:
            while (stack and precedence(stack[-1]) >= precedence(char)):
                result.append(stack.pop())
            stack.append(char)

    while stack:
        result.append(stack.pop())
    
    return ''.join(result)

def to_prefix(expression):
    expression = expression[::-1]
    stack = []
    result = []

    for char in expression:
        if char.isalnum():
            result.append(char)
        else:
            while (stack and precedence(stack[-1]) > precedence(char)):
                result.append(stack.pop())
            stack.append(char)

    while stack:
        result.append(stack.pop())
    
    return ''.join(result[::-1])

infix_expr = "A+B*C"
prefix_expr = to_prefix(infix_expr)
postfix_expr = to_postfix(infix_expr)
print("Postfix: ", postfix_expr)
print("Prefix: ", prefix_expr)

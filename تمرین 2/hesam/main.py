def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    output = []
    
    for char in expression:
        if char.isalnum(): 
            output.append(char)
        elif char == '(':  
            stack.append(char)
        elif char == ')':  
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  
        else:  
            while stack and stack[-1] != '(' and precedence.get(char, 0) <= precedence.get(stack[-1], 0):
                output.append(stack.pop())
            stack.append(char)
    
    while stack:
        output.append(stack.pop())
    
    return ''.join(output)

def infix_to_prefix(expression):
    expression = expression[::-1]
    expression = expression.replace('(', 'temp').replace(')', '(').replace('temp', ')')

    postfix = infix_to_postfix(expression)
    return postfix[::-1]

expr = "(A-B/C)*(A/K-L)"
print("Postfix:", infix_to_postfix(expr))
print("Prefix:", infix_to_prefix(expr))

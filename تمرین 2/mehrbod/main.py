class Stack:
    def __init__(self) -> None:
        self._array = []

    def is_empty(self) -> bool:
        return self.size() == 0

    def size(self) -> int:
        return len(self._array)

    def top(self):
        return self._array[-1]

    def push(self, item) -> None:
        self._array.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self._array.pop()

def op_weight(op:str) -> int:
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^':
        return 3
    return 0

def add_parentheses(exp:str) ->str:
    output = []
    stack = Stack()
    for char in exp:
        if char.isdigit() or char.isalpha():
            output.append(char)
        else:
            while stack.size() and op_weight(stack.top()) >= op_weight(char):
                operator = stack.pop()
                right = output.pop()
                left = output.pop()
                output.append(f'({left}{operator}{right})')
            stack.push(char)

    while stack.size():
        operator = stack.pop()
        right = output.pop()
        left = output.pop()
        output.append(f'({left}{operator}{right})')

    return output[0]

def toPrefix(exp:str) -> str:
    exp = add_parentheses(exp)
    stack = Stack()
    array = []
    i = len(exp) - 1
    while i >= 0:
        char = exp[i]
        if char in ")+-*/":
            stack.push(char)
        elif char != '(':
            array.append(char)
        elif char == '(':
            array.append(stack.pop())
            stack.pop()
            if stack.is_empty():
                array.reverse()
        i -= 1
    return "".join(array)

def toPostfix(exp:str) -> str:
    exp = add_parentheses(exp)
    stack = Stack()
    array = []
    for char in exp:
        if char in "(+-*/":
            stack.push(char)
        elif char != ')':
            array.append(char)
        elif char == ')':
            array.append(stack.pop())
            stack.pop()
    return "".join(array)
def parentheses_balanced(expression):
    stack = []
    matching_parentheses = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in matching_parentheses.values():
            stack.append(char)
        elif char in matching_parentheses.keys():
            if not stack or matching_parentheses[char] != stack.pop():
                return False
    return not stack  # More Pythonic way to check if the stack is empty

# Get user input
while True:
    expression = input("Enter an expression (or type 'exit' to quit): ")
    if expression.lower() == 'exit':
        print("Exiting the program.")
        break
    if parentheses_balanced(expression):
        print("The parentheses are balanced.")
    else:
        print("The parentheses are not balanced.")

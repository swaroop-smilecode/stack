def paired_parentheses(string):
    stack = []
    for char in string:
        # To handle edge case 
        if not stack and char == ')':
            return False
        # Main logic
        if char == '(':
            stack.append(char)
        elif char == ')':
            stack.pop()
    # This is important in parenthesis questions. You should return not stack.
    return not stack

print(paired_parentheses("(david)((abby))"))
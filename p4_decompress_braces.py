def decompress_braces(string):
    numbers = "123456789"
    stack = []

    for char in string:
        # What to be done if we see 'number'
        if char in numbers:
            stack.append(int(char))
        # What to be done if we see '{'
        elif char == "{":
            continue
        # What to be done if we see 'alphabyte'
        elif 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            stack.append(char)
        # What to be done if we see '}'

        # Here you can use 'else', but for better understanding(to know when 
        # this code block will execute, i am keeping 'elif' here).        
        elif char == "}":
            segment = ""
            while isinstance(stack[-1], str):
                popped_char = stack.pop()
                segment = popped_char + segment
            num = stack.pop()
            stack.append(segment * num)
    return "".join(stack)

print(decompress_braces("2{q}3{tu}v")) # -> qqtututuv
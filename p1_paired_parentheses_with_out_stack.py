def paired_parentheses(string):
  count = 0
  for char in string:
    # To handle edge case 
    if count == 0 and char == ")":
      return False
    # Main logic
    if char == "(":
      count += 1
    elif char == ")":
      count -= 1
  # This is important in parenthesis questions. You should return not stack.
  return count == 0

print(paired_parentheses("(david)((abby))"))
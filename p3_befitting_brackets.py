# Before solving this problem, you should know math behind it.
# You can't have something like this ([6*6)+6]
# The valid one is ([]{}). Why it is valid? Whenever a bracket opens,
# the next bracket has to be the corresponding closing bracket.

# When you know above logic, obvisouly stack comes to your mind to solve this 
# problem.

# Assumption: string contains only the brackets, not alphabytes.
def befitting_brackets(string):
  stack = []
  
  brackets = {
    '(': ')',
    '[': ']',
    '{': '}',
  }
  
  for char in string:
    # To handle edge case 
    if not stack and char in [")", "}", "]"]:
        return False
        
    if char in brackets:
      # Observe here. If i encounter an opening symbol, i am appending corresponding closing 
      # symbol on top of the stack. So, that when i encounter closing symbol, i can directly check
      # whether that closing symbol is at top of my stack/not.
      stack.append(brackets[char])
    else:
        if stack and stack[-1] == char:
                stack.pop()
      
  return len(stack) == 0

print(befitting_brackets('(){}[](())'))
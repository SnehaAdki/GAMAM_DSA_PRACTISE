# 20. Valid Parentheses
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([])"
# Output: true

# Example 5:
# Input: s = "([)]"
# Output: false

def valid_parentheses(string):
    stack = []
    hash_map = {')':'(','}':'{',']':'['}
    for i in string:
        if i in hash_map.values():
            stack.append(i)
        else:
            if len(stack)!= 0 and hash_map[i]  == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
    return True if len(stack) == 0 else False



s = ")"
print(valid_parentheses(s))

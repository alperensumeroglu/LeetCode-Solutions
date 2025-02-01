class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Stack to keep track of indices of unmatched parentheses
        stack = [-1]  # Initialize with -1 to handle edge cases like "()"
        max_length = 0  # Variable to store the maximum length of valid parentheses

        # Iterate through the string
        for i in range(len(s)):
            if s[i] == '(':
                # Push the index of '(' onto the stack
                stack.append(i)
            else:
                # Pop the last unmatched '(' or starting index
                stack.pop()
                if not stack:
                    # If the stack is empty, push the current index as a new base
                    stack.append(i)
                else:
                    # Calculate the length of the current valid substring
                    max_length = max(max_length, i - stack[-1])

        return max_length

'''

# Intuition
The problem is about finding the longest valid parentheses substring. A stack is used to track unmatched parentheses' indices.
We use this to efficiently calculate the length of valid substrings.

# Approach
- Use a stack to store indices of unmatched parentheses or serve as markers for valid substrings.
- Traverse the string:
  - For '(', push its index onto the stack.
  - For ')', pop the stack. If the stack becomes empty, push the current index as a new base. Otherwise, calculate the valid substring length.
- The `max_length` variable keeps track of the maximum valid substring length.

# Complexity
- Time complexity: O(n)
  - We traverse the string once, making this solution linear.
- Space complexity: O(n)
  - The stack size is proportional to the input string's length in the worst case.
'''

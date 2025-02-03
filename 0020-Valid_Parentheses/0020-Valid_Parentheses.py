class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize a stack to keep track of open brackets
        stack = []

        # Dictionary to map each open bracket to its corresponding close bracket
        bracket_pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        # Iterate through each character in the string
        for char in s:
            # If the character is an open bracket, push it onto the stack
            if char in bracket_pairs:
                stack.append(char)
            # If the character is a close bracket
            else:
                # Check if the stack is empty or the top of the stack does not match the close bracket
                if not stack or bracket_pairs[stack.pop()] != char:
                    return False

        # If the stack is empty at the end, the string is valid
        return not stack
'''

Intuition
To determine if a string containing brackets is valid, we need a mechanism to ensure every opening bracket has a corresponding closing bracket in the correct order. A stack is an ideal data structure for this as it allows us to process brackets in a last-in, first-out manner.

Approach
1. Use a stack to keep track of open brackets encountered while traversing the string.
2. Maintain a dictionary to map each type of open bracket to its corresponding close bracket.
3. Iterate through the string:
   - If an open bracket is encountered, push it onto the stack.
   - If a close bracket is encountered, check:
     a) If the stack is empty (invalid string).
     b) If the top of the stack does not match the closing bracket (invalid string).
4. At the end of the traversal, check if the stack is empty. If it is, the string is valid.

Complexity
- Time complexity: O(n), where n is the length of the input string. Each character is pushed or popped from the stack at most once.
- Space complexity: O(n), due to the space required by the stack in the worst case when all characters are open brackets.

'''
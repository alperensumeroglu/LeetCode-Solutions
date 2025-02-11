class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []  # Using a stack to build the final string
        part_length = len(part)  # Length of the substring to remove

        for char in s:
            stack.append(char)  # Add character to stack

            # Check if the last part_length characters match the target substring
            if len(stack) >= part_length:
                if "".join(stack[-part_length:]) == part:
                    # Remove the last part_length characters
                    for _ in range(part_length):
                        stack.pop()

        return "".join(stack)  # Return the final string after all removals

'''
# Intuition
The problem requires us to remove all occurrences of a given substring `part` from string `s`. The removal should be done iteratively until there are no more occurrences left. This suggests a stack-based approach where we dynamically build the result while continuously checking for `part`.

# Approach
We use a **stack** to simulate the gradual construction of the final string while removing `part` whenever it appears at the end of our current stack.

1. Iterate through each character in `s`, appending it to the `stack`.
2. After adding a character, check if the last `len(part)` characters of `stack` form `part`.
3. If they do, remove these characters from `stack`.
4. Finally, return the stack as a string.

This approach ensures that we remove occurrences of `part` as soon as they appear, making the solution efficient.

# Complexity
- Time complexity: **O(n)**  
  Each character is processed once, and in the worst case, each character might be pushed and popped from the stack a few times.
  
- Space complexity: **O(n)**  
  The stack stores the modified version of `s`, which in the worst case can be the same length as `s`.
'''


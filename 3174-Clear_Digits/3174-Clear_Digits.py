
class Solution:
    def clearDigits(self, input_string: str) -> str:
        # Initialize a stack to keep track of non-digit characters
        character_stack = []

        # Iterate through each character in the input string
        for character in input_string:
            # If the character is a digit, remove the closest non-digit character from the stack
            if character.isdigit():
                if character_stack:  # Ensure the stack is not empty before popping
                    character_stack.pop()
            else:
                # If the character is not a digit, add it to the stack
                character_stack.append(character)
        
        # Join and return the remaining characters in the stack as the final result
        return "".join(character_stack)
        
'''
# Intuition
The task involves removing digits and the closest non-digit character to their left repeatedly until no digits remain.
A stack is the most suitable data structure for this, as it allows efficient addition and removal of elements.

# Approach
1. Use a stack to keep track of non-digit characters in the string.
2. For each character in the string:
   - If it's a digit, remove the top non-digit character from the stack (if the stack is not empty).
   - Otherwise, push the character onto the stack.
3. After processing the entire string, the stack will contain the remaining characters.
4. Join and return the characters in the stack.

# Complexity
- Time complexity: O(n), where n is the length of the input string. Each character is processed once.
- Space complexity: O(n), in the worst case, the stack may store all non-digit characters from the input string.
'''

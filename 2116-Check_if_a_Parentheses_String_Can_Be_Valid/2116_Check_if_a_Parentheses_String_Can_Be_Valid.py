class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # If the length of the string is odd, it's impossible to have balanced parentheses
        if len(s) % 2 != 0:
            return False
        
        # Forward pass: check if we can balance open parentheses
        open_count = 0
        flexible_slots = 0
        
        for i in range(len(s)):
            if s[i] == '(' or locked[i] == '0':
                open_count += 1
            else:
                open_count -= 1
            
            # If open_count becomes negative, it's invalid at this point
            if open_count < 0:
                return False
        
        # Backward pass: check if we can balance close parentheses
        close_count = 0
        flexible_slots = 0
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ')' or locked[i] == '0':
                close_count += 1
            else:
                close_count -= 1
            
            # If close_count becomes negative, it's invalid at this point
            if close_count < 0:
                return False
        
        # If both passes succeed, the string can be valid
        return True

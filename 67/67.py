class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Reverse the strings for easier processing from least significant bit to most
        a_reversed, b_reversed = a[::-1], b[::-1]
        result = []
        carry = 0
        
        # Loop through each digit, using the length of the longer string
        max_length = max(len(a), len(b))
        for i in range(max_length):
            # Get the current digit or 0 if index is out of range
            digit_a = int(a_reversed[i]) if i < len(a) else 0
            digit_b = int(b_reversed[i]) if i < len(b) else 0
            
            # Calculate the sum and the next carry
            total = digit_a + digit_b + carry
            result.append(str(total % 2))
            carry = total // 2
        
        # If there's a remaining carry, add it to the result
        if carry:
            result.append("1")
        
        # Reverse the result list to get the correct binary representation and join into a string
        return ''.join(result[::-1])

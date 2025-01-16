class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # Count the number of set bits in num2
        num2_set_bits = 0
        while num2 > 0:
            num2_set_bits += num2 & 1
            num2 >>= 1

        # Result variable
        result = 0

        # Set bits in result where num1 has set bits, starting from the highest bit
        for i in range(31, -1, -1):
            if (num1 & (1 << i)) > 0 and num2_set_bits > 0:
                result |= (1 << i)
                num2_set_bits -= 1

        # Set remaining bits in result starting from the lowest bit
        for i in range(32):
            if num2_set_bits > 0 and (result & (1 << i)) == 0:
                result |= (1 << i)
                num2_set_bits -= 1

        return result

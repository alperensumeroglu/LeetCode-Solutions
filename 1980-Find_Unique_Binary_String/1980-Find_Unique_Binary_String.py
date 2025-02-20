# 1980-Find_Unique_Binary_String.py

class Solution:
    def findDifferentBinaryString(self, binary_strings):
        n = len(binary_strings)  # Get the length of the list (which is also the length of each binary string)
        return self._generate_unique_binary("", binary_strings, n)
    
    def _generate_unique_binary(self, current, binary_strings, n):
        # Base case: If the current binary string reaches the required length
        if len(current) == n:
            # Check if it is unique and not in the given list
            if current not in binary_strings:
                return current
            return None  # Otherwise, return None to continue searching

        # Try appending '0' and '1' recursively to generate a unique binary string
        for bit in ['0', '1']:
            unique_string = self._generate_unique_binary(current + bit, binary_strings, n)
            if unique_string:
                return unique_string  # Return the first unique string found

''' 
# Intuition
The problem requires us to find a binary string of length `n` that is not present in the given list.
Since the input list contains unique binary strings of length `n`, the maximum number of binary strings in the list is `2^n`.
If `n` unique binary strings are given, there will always be at least one missing binary string.

# Approach
1. Use recursion to generate all possible binary strings of length `n`.
2. If a generated string is not in the given list, return it as the result.
3. We start with an empty string and recursively append '0' and '1' to build valid binary strings.
4. As soon as we find a valid missing binary string, we return it to avoid unnecessary computations.

# Complexity
- Time complexity: O(2^n) in the worst case, as we generate all possible binary strings of length `n`.
- Space complexity: O(n) due to the recursion depth.
''' 

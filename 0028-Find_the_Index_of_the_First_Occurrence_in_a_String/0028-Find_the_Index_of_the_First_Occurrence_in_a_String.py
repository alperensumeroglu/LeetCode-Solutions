class Solution:
    def findFirstOccurrence(self, text: str, pattern: str) -> int:
        # If the pattern is an empty string, return 0 as per the problem statement
        if pattern == "":
            return 0

        # Iterate through the text, ensuring there is enough room for pattern to fit
        for index in range(len(text) - len(pattern) + 1):
            # Check if the substring of text matches the pattern
            if text[index: index + len(pattern)] == pattern:
                return index

        # If no match is found, return -1
        return -1


"""
# Intuition
The problem requires us to find the first occurrence of a substring (needle) in a given string (haystack). 
If the substring does not exist, return -1. A straightforward way to solve this is by checking all possible starting positions in `haystack` where `needle` can fit and comparing the substrings.

# Approach
We iterate through `haystack`, checking substrings of length `needle`. If we find a match, we return the index. 
If we complete the loop without finding a match, we return -1. 

# Complexity
- Time complexity: O(n * m) where `n` is the length of `haystack` and `m` is the length of `needle`. 
  In the worst case, we check `needle` against all possible substrings of `haystack`.
- Space complexity: O(1) since we only use a few extra variables regardless of input size.
"""
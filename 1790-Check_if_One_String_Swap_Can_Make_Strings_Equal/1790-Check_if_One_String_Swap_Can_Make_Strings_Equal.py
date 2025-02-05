class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # Count the number of mismatched characters between s1 and s2
        mismatch_count = 0
        mismatched_indices = set()
        
        # Iterate through the characters of both strings
        for i, (char1, char2) in enumerate(zip(s1, s2)):
            if char1 != char2:
                mismatch_count += 1
                mismatched_indices.add(i)
                
                # If more than two mismatches, return False early
                if mismatch_count > 2:
                    return False
        
        # Check if mismatched characters can be swapped
        if mismatch_count == 0:
            return True  # Strings are already equal
        if mismatch_count == 2:
            i, j = list(mismatched_indices)
            # Ensure swapping resolves the mismatch
            return s1[i] == s2[j] and s1[j] == s2[i]
        
        return False  # Cannot resolve with one swap

'''
Intuition
The problem requires determining whether two strings can become equal by swapping at most one pair of characters. 
We track mismatched positions and verify if they can be fixed with a single swap.

Approach
1. Count mismatched characters between s1 and s2.
2. If mismatches exceed two, return False since one swap won't suffice.
3. If mismatches are two, check if swapping the mismatched characters results in equality.
4. If no mismatches exist, the strings are already equal.

Complexity
- Time complexity: O(n), where n is the length of the strings. We iterate through the strings once.
- Space complexity: O(1), as we only store indices and counts.
'''


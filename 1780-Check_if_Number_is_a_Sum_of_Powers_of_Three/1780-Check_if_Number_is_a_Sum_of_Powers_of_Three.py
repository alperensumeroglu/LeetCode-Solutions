class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        """
        Determines if a given integer can be represented as a sum of distinct powers of three.
        
        :param n: The integer to be checked.
        :return: True if n can be expressed as a sum of distinct powers of three, False otherwise.
        """
        while n:
            # If any digit in base 3 representation is 2, return False
            if n % 3 == 2:
                return False
            # Reduce n by dividing by 3
            n //= 3
        return True

'''
🔼 Please Upvote
🔼 Please Upvote
🔼 Please Upvote
🔼 Please Upvote

💡If this helped, don’t forget to upvote! 🚀🔥

# Intuition
To determine if a number can be expressed as a sum of distinct powers of three, 
we can leverage its base-3 representation.

# Approach
- The problem can be reduced to checking the base-3 representation of `n`.
- If any digit in this representation is `2`, then `n` cannot be expressed 
  as a sum of distinct powers of three (since we can only use `0` or `1` for each power).
- We iterate by dividing `n` by `3` and checking the remainder.
- If we find `2` at any step, return `False`, otherwise return `True`.

# Complexity
• Time complexity: **O(log₃ n)** since we are dividing `n` by 3 in each iteration.
• Space complexity: **O(1)** since we are using only a few variables.
'''

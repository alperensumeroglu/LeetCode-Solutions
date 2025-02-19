class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        """
        Find the k-th lexicographical happy string of length n.
        A happy string consists of characters 'a', 'b', 'c' where no two adjacent characters are the same.
        """

        # Compute the number of happy strings of length `n-1`
        partition_size = 2 ** (n - 1)

        # If k is greater than the total possible happy strings, return an empty string
        if k > 3 * partition_size:
            return ""

        # Determine the first character of the happy string
        index = (k - 1) // partition_size
        result = ['a', 'b', 'c'][index]

        # Construct the rest of the happy string
        while partition_size > 1:
            k = (k - 1) % partition_size + 1  # Update k within the new partition
            partition_size //= 2  # Reduce partition size

            # Choose the next character that is different from the last character
            if result[-1] == 'a':
                next_char = ['b', 'c'][(k - 1) // partition_size]
            elif result[-1] == 'b':
                next_char = ['a', 'c'][(k - 1) // partition_size]
            else:
                next_char = ['a', 'b'][(k - 1) // partition_size]

            result += next_char  # Append chosen character to result

        return result

'''
# Intuition
The problem requires generating a lexicographically sorted list of "happy" strings of length `n` and returning the `k`-th one.
A happy string is a string where no two adjacent characters are the same and only consists of 'a', 'b', and 'c'.
Instead of generating all possible strings, we use a structured approach to find the k-th string efficiently.

# Approach
1. Each position in the happy string can be determined by dividing the possibilities into partitions.
2. We first compute the number of happy strings of length `n-1` to determine partition sizes.
3. The first character is chosen by dividing `k` by the number of partitions per character.
4. Using a loop, we progressively determine each character by selecting a different one than the last chosen.
5. We update `k` accordingly and continue until the full string is constructed.

# Complexity
- Time complexity: **O(n)**  
  Since we construct the happy string character by character in `O(n)`, our approach is efficient compared to generating all possible strings.

- Space complexity: **O(1)**  
  We only store a few variables and the output string, so our space usage is constant.
'''

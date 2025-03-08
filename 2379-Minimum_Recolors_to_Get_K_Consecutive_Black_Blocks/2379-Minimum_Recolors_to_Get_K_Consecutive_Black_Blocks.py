class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # Get the length of the blocks string
        n = len(blocks)

        # Initialize the minimum recolors needed with the worst case (k)
        min_recolors = k

        # Count the number of white blocks in the first window of size k
        current_white_count = sum(1 for i in range(k) if blocks[i] == 'W')

        # Set the minimum recolors needed as the initial white count
        min_recolors = current_white_count

        # Use a sliding window technique to find the minimum recoloring needed
        for i in range(k, n):
            # Remove the leftmost element of the previous window
            if blocks[i - k] == 'W':
                current_white_count -= 1

            # Add the rightmost element of the current window
            if blocks[i] == 'W':
                current_white_count += 1

            # Update the minimum recolors required
            min_recolors = min(min_recolors, current_white_count)

        return min_recolors



'''
🔼 Please Upvote
🔼 Please Upvote
🔼 Please Upvote
🔼 Please Upvote

💡If this helped, don’t forget to upvote! 🚀🔥

# Intuition
The problem requires us to find the minimum number of recoloring operations needed to achieve at least one occurrence of `k` consecutive black blocks. 
Since we can only change white blocks (`'W'` to `'B'`), our goal is to find the window of size `k` with the fewest white blocks, as those are the ones we need to recolor.

# Approach
We use the **Sliding Window** technique:
1. **Initialize a window of size `k`** and count the number of `'W'` blocks.
2. **Use a sliding window** to traverse through the string and dynamically update the count of white blocks by removing the leftmost character and adding the new rightmost character.
3. **Keep track of the minimum number of white blocks** found in any window, as this is the minimum number of recolors required.

# Complexity
• Time complexity: **O(n)**, since we iterate through the string only once using the sliding window technique.

• Space complexity: **O(1)**, as we only use a few integer variables for tracking counts and do not use any extra space dependent on the input size.


'''
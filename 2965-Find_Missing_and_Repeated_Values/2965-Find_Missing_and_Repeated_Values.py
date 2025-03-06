class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # Set to track visited numbers
        seen_numbers = set()
        total_sum = 0
        n = len(grid)
        result = []

        # Traverse the grid to find the repeated number and calculate sum of unique numbers
        for row in grid:
            for num in row:
                if num not in seen_numbers:
                    seen_numbers.add(num)
                    total_sum += num
                else:
                    result.append(num)  # The repeated number

        # Calculate the missing number using sum formula
        total = n ** 2
        result.append(total * (total + 1) // 2 - total_sum)

        return result

'''

🔼 Please Upvote
🔼 Please Upvote
🔼 Please Upvote
🔼 Please Upvote

💡If this helped, don’t forget to upvote! 🚀🔥

# Intuition
Given an n x n grid where numbers from 1 to n^2 appear exactly once except for one repeated number and one missing number, 
we need to determine these two values efficiently.

# Approach
We use a set to track numbers already seen and a variable to accumulate the sum of unique numbers. As we iterate over the grid,
we check if a number has been seen before; if so, it's the repeated number. 
Then, we use the sum formula for the first n^2 natural numbers to compute the missing number.

# Complexity
• Time complexity: O(n^2), as we iterate through all elements in the grid.
• Space complexity: O(n^2), due to the set storing up to n^2 numbers.

'''

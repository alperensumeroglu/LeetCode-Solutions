class Solution:
    def punishmentNumber(self, n: int) -> int:
        # Helper function to check if a number's square can be partitioned into substrings summing to itself
        def is_valid_partition(remaining_str, current_sum):
            # If the string is empty and the sum matches the number, it's a valid partition
            if not remaining_str and current_sum == target:
                self.is_valid = True
                return
            # If the current sum exceeds the number, stop checking
            if current_sum > target:
                return
            # Try all possible partitions
            for split_index in range(1, len(remaining_str) + 1):
                is_valid_partition(remaining_str[split_index:], current_sum + int(remaining_str[:split_index]))

        total_sum = 0  # Store the final punishment number sum

        for i in range(1, n + 1):
            self.is_valid = False  # Reset validation flag
            target = i  # The current number
            square_str = str(i * i)  # Compute the square and convert to string
            is_valid_partition(square_str, 0)  # Check if it can be partitioned
            if self.is_valid:
                total_sum += i * i  # Add to result if valid

        return total_sum


'''# Intuition
This problem requires us to check if the square of a number can be split into contiguous substrings summing to the number itself. 
Thus, we must validate this condition for all numbers from 1 to n and sum their squares if they satisfy the given condition.

# Approach
1. Iterate through numbers from 1 to n.
2. Compute the square of each number.
3. Use a recursive backtracking approach to check if the square can be partitioned such that the sum of the partitions equals the original number.
4. If a valid partition is found, add the square to the punishment number.
5. Return the total punishment number at the end.

# Complexity
- Time complexity: $$O(n * m)$$ where n is the input range and m is the length of the squared number. Backtracking can make it expensive.
- Space complexity: $$O(n)$$ due to recursive calls and storing results.
'''
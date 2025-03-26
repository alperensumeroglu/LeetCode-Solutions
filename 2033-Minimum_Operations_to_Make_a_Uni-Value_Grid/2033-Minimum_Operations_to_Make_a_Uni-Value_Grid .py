class Solution:
    def minOperations(self, grid, x):
        nums = []
        for row in grid:
            nums.extend(row)  # Add all elements of each row to the nums list
        
        min_value = min(nums)  # Find the minimum value in the grid
        
        # Check if all elements can be transformed to the same value. For this, the difference between each element and the minimum value must be divisible by x.
        # If any element fails this condition, it's impossible to make all elements equal, so we return -1.
        for num in nums:
            if (num - min_value) % x != 0:
                return -1  # If the difference is not divisible by x, return -1 because it's not possible to make all elements the same.
        
        nums.sort()  # Sort the numbers to find the median element
        
        median = nums[len(nums) // 2]  # The median minimizes the total number of operations required to make all elements equal.
        
        operations = 0
        for num in nums:
            operations += abs(num - median) // x  # Each operation changes the value by x, so we divide the absolute difference by x.
        
        return operations  # Return the total number of operations

        '''
        Intuition: The problem asks to make all elements in a 2D grid equal with the fewest operations, 
        where each operation allows us to add or subtract a given integer x. To solve this problem, we 
        first check if it's possible to make all elements equal by verifying that the difference between 
        each element and the minimum value is divisible by x. Then, we use the median of the grid elements 
        as the optimal target, because it minimizes the total number of operations required.

        Approach: 
        1. Flatten the 2D grid into a 1D list of numbers.
        2. Check if the difference between each element and the minimum value is divisible by x. If not, return -1.
        3. Sort the list to find the median element.
        4. Calculate the number of operations (add/subtract x) required to make all elements equal to the median.

        Complexity:
        - Time Complexity: O(m * n * log(m * n)), where m * n is the total number of elements in the grid. The time complexity is dominated by the sorting step.
        - Space Complexity: O(m * n), as we are storing the flattened grid in a 1D list.

        🚀🔥 Keep coding and stay awesome!
        '''

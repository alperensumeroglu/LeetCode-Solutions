class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)  # Length of the input list
        results, current_permutation = [], []

        def backtrack():
            # If the current permutation is complete, add it to the results
            if len(current_permutation) == n:
                results.append(current_permutation[:])  # Make a deep copy
                return
            
            # Iterate over each number in nums
            for number in nums:
                if number not in current_permutation:  # Check if the number is already used
                    current_permutation.append(number)  # Add the number to the current permutation
                    backtrack()  # Continue building the permutation
                    current_permutation.pop()  # Backtrack by removing the last number

        backtrack()  # Start the backtracking process
        return results

'''
# Intuition
The problem requires generating all possible permutations of a given list of distinct integers. The first thought was to use a backtracking approach, which is well-suited for generating combinations or permutations.

# Approach
The solution uses a backtracking technique:
1. Use a helper function `backtrack` to generate permutations recursively.
2. Maintain a `current_permutation` list to build permutations step-by-step.
3. At each step, check if a number is already used; if not, add it to the current permutation.
4. If a complete permutation is formed (its length equals the input list), add it to the results.
5. Use backtracking to remove the last added number and try other possibilities.

# Complexity
- Time complexity: O(n * n!) 
  Generating all permutations of n distinct numbers takes O(n!) and constructing each permutation requires O(n) time.
- Space complexity: O(n)
  The space is used for the recursion stack and the current permutation being built.
'''  
class Solution:
    def minOperations(self, nums, k):
        """
        Function to calculate the minimum number of operations needed to achieve the given value k by applying 
        a specific operation on the list of numbers.

        Parameters:
        nums (List[int]): A list of integers.
        k (int): The target value to be achieved through operations.

        Returns:
        int: The minimum number of operations needed or -1 if it's not possible.
        """

        # Intuition:
        # 1. First, we check if the target value 'k' can be achieved. If 'k' is greater than the minimum 
        #    value in the list 'nums', then it's impossible to achieve 'k' since no operation can increase
        #    values beyond the smallest element. Hence, we return -1.
        # 2. We need to know how many unique elements are in the list, since every unique element gives us 
        #    a potential transformation operation. We will count unique elements using a set.
        # 3. If 'k' is already in the list, we subtract 1 from the number of unique elements because no 
        #    transformation is needed to achieve 'k'.
        # 4. If 'k' is not in the list, we simply return the count of unique elements in the list.
        
        # Approach:
        # Step 1: If 'k' is greater than the smallest number in 'nums', return -1 because it's impossible.
        # We return -1 early, to avoid unnecessary computations when it's clear that the problem cannot be solved.
        if k > min(nums):
            return -1

        # Step 2: Count the number of unique elements in the list by converting it to a set.
        # Converting the list to a set removes duplicates, leaving us with only unique elements.
        unique_elements = set(nums)
        unique_count = len(unique_elements)

        # Step 3: If 'k' is already in the list, return the number of unique elements minus 1.
        # No operation is needed to reach 'k', so we subtract 1 from the unique count.
        if k in unique_elements:
            return unique_count - 1
        else:
            # Step 4: If 'k' is not in the list, return the number of unique elements.
            # In this case, we must perform at least one operation for each unique element in the list.
            return unique_count

        # Complexity:
        # Time complexity:
        # The time complexity is O(n), where n is the length of the list 'nums'. Converting the list to a 
        # set and checking whether 'k' is in the set are both O(n) operations.
        #
        # Space complexity:
        # The space complexity is O(n) because we use a set to store the unique elements in the list, which
        # requires linear space.

        # Conclusion:
        # This approach efficiently solves the problem by using a set to count unique elements and performs 
        # simple checks to determine if 'k' is already in the list or not. It guarantees a minimal time and
        # space complexity.
        
        # 🚀🔥 Keep coding and stay awesome!

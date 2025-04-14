class Solution:
    def countGoodTriplets(self, arr, a, b, c):
        """
        Count the number of valid triplets (i, j, k) such that:
        - i < j < k
        - |arr[i] - arr[j]| <= a
        - |arr[j] - arr[k]| <= b
        - |arr[i] - arr[k]| <= c
        
        :param arr: List of integers representing the array.
        :param a: The maximum allowed difference between arr[i] and arr[j].
        :param b: The maximum allowed difference between arr[j] and arr[k].
        :param c: The maximum allowed difference between arr[i] and arr[k].
        :return: The count of good triplets satisfying the above conditions.
        """

        res = 0  # Variable to store the count of good triplets
        interval = [0] * 1001  # Prefix count array, tracks the frequency of values seen so far
        
        # Intuition:
        # We need to find triplets (i, j, k) such that i < j < k and the differences 
        # between the values at these indices satisfy the given conditions.
        # To solve this efficiently, we use a prefix count array to avoid redundant calculations.
        
        # Approach:
        # 1. We iterate over all possible pairs of j and k, where k > j.
        # 2. For each pair (j, k), check if the condition |arr[j] - arr[k]| <= b holds.
        # 3. For each valid pair (j, k), calculate the range of valid values for i, where:
        #    - |arr[i] - arr[j]| <= a
        #    - |arr[i] - arr[k]| <= c
        # 4. The interval array keeps track of how many values of arr[i] (where i < j) 
        #    satisfy the conditions for each possible i in a given range.
        # 5. Finally, we update the interval array for the next iteration of j and k.

        for j in range(len(arr)):
            # Iterate over all k's where k > j
            for k in range(j + 1, len(arr)):
                # Check if the difference between arr[j] and arr[k] satisfies the condition
                if abs(arr[j] - arr[k]) <= b:
                    # Calculate the valid range for arr[i] based on conditions involving a and c
                    left = max(0, max(arr[j] - a, arr[k] - c))
                    right = min(1000, min(arr[j] + a, arr[k] + c))
                    
                    # If there is a valid range for i, add the count of valid i's from the interval array
                    if left <= right:
                        if left == 0:
                            res += interval[right]
                        else:
                            res += interval[right] - interval[left - 1]
            
            # Update the interval array for arr[j] after processing this element
            # Increment all indices from arr[j] to 1000 in the interval array
            for ind in range(arr[j], 1001):
                interval[ind] += 1

        return res

# Example Usage:
sol = Solution()
arr = [3, 0, 1, 1, 9, 7]
a, b, c = 7, 2, 3
result = sol.countGoodTriplets(arr, a, b, c)
print(result)  # Expected output based on the example data


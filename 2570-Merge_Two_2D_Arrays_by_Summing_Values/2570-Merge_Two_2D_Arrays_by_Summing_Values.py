 
class Solution:
    def mergeArrays(self, nums1, nums2):
        # Dictionary to store summed values for each unique ID
        id_value_map = {}

        # Iterate through nums1 and update dictionary
        for identifier, value in nums1:
            if identifier in id_value_map:
                id_value_map[identifier] += value
            else:
                id_value_map[identifier] = value

        # Iterate through nums2 and update dictionary
        for identifier, value in nums2:
            if identifier in id_value_map:
                id_value_map[identifier] += value
            else:
                id_value_map[identifier] = value

        # Convert the dictionary into a sorted list of lists
        merged_result = [[identifier, id_value_map[identifier]] for identifier in sorted(id_value_map.keys())]

        return merged_result

'''
🔼 Please Upvote
🔼 Please Upvote
🔼 Please Upvote
🔼 Please Upvote

💡If this helped, don’t forget to upvote! 🚀🔥

# Intuition
We need to merge two sorted 2D arrays while ensuring unique IDs appear only once and their values are summed correctly.

# Approach
1. Use a dictionary to store the sum of values for each unique `id`.
2. Iterate over `nums1` and `nums2` to update the dictionary manually without using external libraries.
3. Extract and sort the dictionary keys and return the result as a list of lists.

# Complexity
• Time Complexity: $$O(n + m + k \log k)$$  
  - $$O(n + m)$$ for iterating through `nums1` and `nums2`.  
  - $$O(k \log k)$$ for sorting unique keys (where $$k$$ is the number of unique IDs).  

• Space Complexity: $$O(k)$$  
  - We use extra space for the dictionary storing unique IDs and their summed values.

'''
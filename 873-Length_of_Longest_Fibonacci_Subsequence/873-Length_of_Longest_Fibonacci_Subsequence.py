class Solution:
    def lenLongestFibSubseq(self, arr):
        """
        Optimized approach to find the longest Fibonacci-like subsequence in a given strictly increasing array.
        """
        num_set = set(arr)  # Store array elements in a set for quick lookup
        max_length = 0  # Variable to track the longest sequence found

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                x, y = arr[i], arr[j]  # Start with two initial elements
                length = 2  # Minimum length starts at 2

                while x + y in num_set:  # Check if the next Fibonacci-like number exists
                    x, y = y, x + y  # Move to the next numbers in sequence
                    length += 1  # Increase sequence length

                if length > 2:  # Update max_length only if we found a valid sequence
                    max_length = max(max_length, length)

        return max_length if max_length > 2 else 0  # Return the maximum length found, or 0 if no valid sequence

'''
🔼 Please Upvote
🔼 Please Upvote
🔼 Please Upvote
🔼 Please Upvote

💡If this helped, don’t forget to upvote! 🚀🔥

# Intuition
This problem requires finding the longest subsequence in a strictly increasing array that follows Fibonacci-like properties.
A Fibonacci-like sequence must have at least three elements, where each number is the sum of the previous two.

# Approach
1. Convert the array into a set for quick lookup.
2. Iterate over every pair of numbers in the array and try to form a Fibonacci-like sequence.
3. Use a while loop to extend the sequence as long as the next number exists in the set.
4. Track the maximum length found.
5. If no sequence of length 3 or more is found, return 0.

# Complexity
• Time complexity: O(n^2 log n) – We iterate through all pairs (O(n^2)), and each sequence lookup is O(log n).
• Space complexity: O(n) – We store the elements in a set for quick lookup.
'''
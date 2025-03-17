class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        """
        Determines whether the given array can be divided into equal pairs.
        
        :param nums: list[int] - The input array consisting of 2 * n integers.
        :return: bool - True if the array can be divided into equal pairs, otherwise False.
        """

        # Step 1: Create a dictionary to count occurrences of each element
        frequency_count = {}

        # Step 2: Populate the dictionary with frequencies
        for num in nums:
            if num in frequency_count:
                frequency_count[num] += 1
            else:
                frequency_count[num] = 1

        # Step 3: Check if every element appears an even number of times
        for count in frequency_count.values():
            if count % 2 != 0:
                return False  # If any element has an odd count, return False

        return True  # If all elements appear an even number of times, return True


"""
🔍 Intuition:
- The problem requires us to check if we can divide the given list into pairs where both elements in each pair are equal.
- This means that every unique number must appear an even number of times.

🛠️ Approach:
1. Use a dictionary to count occurrences of each number in `nums`.
2. Iterate over the dictionary and check if all numbers have even counts.
3. If all counts are even, return `True`, otherwise return `False`.

⏱ Complexity:
- Time Complexity: **O(n)** (Iterating through the list once to count elements and once to check counts)
- Space Complexity: **O(n)** (Using a dictionary to store counts)

🚀🔥 Keep coding and stay awesome!
"""

class Solution(object):
    def countLargestGroup(self, n):
        """
        Intuition:
        ------------
        The goal is to group numbers from 1 to n based on the sum of their digits,
        and then count how many groups have the largest size.
        
        Approach:
        ------------
        1. Create a dictionary to map digit sums to their frequency.
        2. Iterate through all numbers from 1 to n.
        3. For each number, calculate the digit sum using a helper function.
        4. Update the count of that digit sum in the dictionary.
        5. Track the size of the largest group while building the dictionary.
        6. Finally, count how many groups have the size equal to the maximum group size.

        Complexity:
        ------------
        Time Complexity: O(n * d), where d is the number of digits in n.
                         Each digit sum calculation takes O(log₁₀(n)) time.
        Space Complexity: O(n) in the worst case, storing frequency of each digit sum.
        """

        # Dictionary to store frequency of each digit sum
        digit_sum_freq = {}

        # Variables to track the maximum group size and how many such groups exist
        max_group_size = 0
        group_count = 0

        # Loop through all numbers from 1 to n
        for number in range(1, n + 1):
            # Calculate digit sum of the current number
            digit_sum = self.digsum(number)

            # Increment the frequency count of this digit sum
            digit_sum_freq[digit_sum] = digit_sum_freq.get(digit_sum, 0) + 1

            # Update the maximum group size if needed
            max_group_size = max(max_group_size, digit_sum_freq[digit_sum])

        # Count how many groups have the maximum group size
        for freq in digit_sum_freq.values():
            if freq == max_group_size:
                group_count += 1

        return group_count

    def digsum(self, n):
        """
        Helper function to calculate the sum of digits of a number.
        """
        digit_sum = 0
        while n > 0:
            digit_sum += n % 10  # Add the last digit
            n //= 10             # Remove the last digit
        return digit_sum

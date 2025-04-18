class Solution:
    def countAndSay(self, n: int) -> str:
        """
        Generate the nth term of the "Count and Say" sequence.

        Intuition:
        The "Count and Say" sequence is a sequence of numbers where each term is derived from 
        the previous one by describing the frequency of consecutive digits. For example:
        1 -> "1" (One 1)
        2 -> "11" (Two 1's)
        3 -> "21" (One 2, one 1)
        4 -> "1211" (One 1, one 2, two 1's)
        This pattern continues.

        Approach:
        1. Start with the base string "1".
        2. For each subsequent term, iterate over the previous term and count the consecutive digits.
        3. For each block of consecutive digits, append the count and the digit to the new term.
        4. Repeat this process until the nth term is generated.

        Complexity:
        - Time Complexity: O(n * m), where n is the number of terms and m is the length of the sequence in each term.
        - Space Complexity: O(m), where m is the space used for each term in the sequence.

        Args:
        n (int): The term of the sequence to be generated.

        Returns:
        str: The nth term in the "Count and Say" sequence.
        """
        # Initialize the first term in the sequence
        result = "1"

        # Iterate through the sequence to generate terms until the nth one
        for _ in range(1, n):
            next_result = ""
            count = 1  # Variable to count the number of consecutive digits

            # Iterate through the characters of the current result
            for i in range(1, len(result)):
                # If the current character is the same as the previous one, increase the count
                if result[i] == result[i - 1]:
                    count += 1
                else:
                    # Otherwise, append the count and the digit to the next result
                    next_result += str(count) + result[i - 1]
                    count = 1  # Reset the count for the next new digit

            # Add the last group of digits to the result
            next_result += str(count) + result[-1]
            
            # Update the result for the next iteration
            result = next_result

        # Return the nth term of the sequence
        return result

# 🚀🔥 Keep coding and stay awesome!

class Solution:
    def maxScore(self, binary_string: str) -> int:
        # Counter for zeros in the left substring
        left_zeros = 0  
        # Total number of ones in the input string (to handle the right substring)
        total_ones = binary_string.count("1")  
        # Variable to store the maximum score
        max_score = 0  

        # Iterate through the string, stopping before the last character
        for i in range(len(binary_string) - 1):
            if binary_string[i] == "0":
                # If the current character is '0', increment the left_zeros counter
                left_zeros += 1  
            else:
                # If the current character is '1', decrement the total_ones counter
                total_ones -= 1  

            # Calculate the score as the sum of zeros in the left substring
            # and ones in the right substring
            current_score = left_zeros + total_ones  
            # Update max_score if the current_score is higher
            max_score = max(max_score, current_score)  

        return max_score

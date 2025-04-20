class Solution(object):
    def numRabbits(self, answers):
        """
        Intuition:
        Each rabbit saying "x" implies a group of (x + 1) rabbits of the same color exists.
        If multiple rabbits report the same "x", we need to group them properly to avoid overcounting.

        Approach:
        1. Count occurrences of each answer manually using a dictionary.
        2. For each unique answer x:
           - group_size = x + 1
           - total groups needed = ceil(count / group_size)
           - total rabbits = number of groups * group_size
        3. Sum these values for the final answer.

        Complexity:
        - Time Complexity: O(n), where n = len(answers)
        - Space Complexity: O(n), for the dictionary
        """

        # Manual implementation of Counter
        answer_frequency = {}
        for answer in answers:
            if answer in answer_frequency:
                answer_frequency[answer] += 1
            else:
                answer_frequency[answer] = 1

        total_rabbits = 0

        for reported_same_color in answer_frequency:
            count = answer_frequency[reported_same_color]
            group_size = reported_same_color + 1

            # Manually implementing ceil division: ceil(a / b) = (a + b - 1) // b
            number_of_groups = (count + group_size - 1) // group_size

            # Total rabbits that must exist for this answer
            rabbits_for_this_answer = number_of_groups * group_size
            total_rabbits += rabbits_for_this_answer

        return total_rabbits

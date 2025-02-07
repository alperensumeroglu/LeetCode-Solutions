# Solution for LeetCode Problem: 3160-Find_Number_of_Distinct_Colors

class Solution:
    def queryResults(self, limit: int, queries: list[list[int]]) -> list[int]:
        # Dictionary to track the count of each color
        color_frequency = {}
        # Dictionary to map each ball to its current color
        ball_to_color = {}
        
        # List to store results
        result = []

        for ball, color in queries:
            # If the ball is already colored, decrease the frequency of its current color
            if ball in ball_to_color:
                color_frequency[ball_to_color[ball]] -= 1
                # If the color frequency becomes zero, remove it from the dictionary
                if color_frequency[ball_to_color[ball]] == 0:
                    del color_frequency[ball_to_color[ball]]

            # Assign the new color to the ball and update the frequency of the new color
            ball_to_color[ball] = color
            if color in color_frequency:
                color_frequency[color] += 1
            else:
                color_frequency[color] = 1

            # Append the current number of distinct colors to the result
            result.append(len(color_frequency))

        return result


"""
Intuition
To solve the problem, we need to keep track of the color assignments for each ball and maintain the count of distinct colors dynamically. By updating these counts after each query, we can efficiently answer the number of distinct colors.

Approach
1. Use a dictionary to map balls to their current colors (ball_to_color).
2. Use another dictionary to maintain the frequency of each color (color_frequency).
3. For each query, update the color of the ball and adjust the frequency dictionary accordingly.
4. Append the count of distinct colors after each query to the result list.

Complexity
- Time complexity: O(n), where n is the number of queries. Each query involves constant-time operations on dictionaries.
- Space complexity: O(limit), where limit is the number of balls. We store mappings for up to `limit` balls.
"""
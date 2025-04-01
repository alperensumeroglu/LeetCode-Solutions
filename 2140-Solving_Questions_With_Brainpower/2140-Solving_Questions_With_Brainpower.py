class Solution:
    def mostPoints(self, questions):
        """
        Calculates the maximum points obtainable from exam questions with brainpower constraints.
        
        The function processes questions in reverse order, using dynamic programming to determine
        whether solving or skipping each question yields more points, considering the required
        skip period after solving any question.

        Args:
            questions: List of question pairs where each contains [points, brainpower]
                      points: Earned points for solving the question
                      brainpower: Number of subsequent questions to skip if solved

        Returns:
            Maximum achievable points from all questions
        """
        n = len(questions)
        # dp array where dp[i] stores maximum points obtainable from question i to end
        dp = [0] * n
        
        # Base case: Last question can only be solved (no questions after to skip)
        dp[-1] = questions[-1][0]
        
        # Process questions in reverse order (from second last to first)
        for i in range(n - 2, -1, -1):
            current_points, skip_count = questions[i]
            
            # Calculate points if we solve current question
            solve_points = current_points
            next_available = i + skip_count + 1  # Next solvable question index
            
            if next_available < n:  # Add points from next solvable question
                solve_points += dp[next_available]
            
            # Points if we skip current question
            skip_points = dp[i + 1]
            
            # Store maximum of solving or skipping
            dp[i] = max(solve_points, skip_points)
        
        return dp[0]  # Maximum points from first question to end
'''
## Intuition:
The problem resembles a weighted interval scheduling challenge where each "job" (question)
has a value (points) and excludes certain subsequent jobs (brainpower skip). We must
select the optimal combination of questions to maximize total points while respecting
the exclusion constraints.

## Approach:
1. **Dynamic Programming Table**: We use a dp array where each entry dp[i] represents
   the maximum points obtainable from question i to the end of the list.

2. **Reverse Processing**: We start from the last question and move backward. This allows
   us to build solutions based on already computed future states.

3. **Decision Making**: For each question, we calculate:
   - Solving: Current points + maximum points after skip period
   - Skipping: Maximum points from the next question
   Then store the better option in dp[i]

4. **Result Extraction**: After processing all questions, dp[0] contains the maximum
   points obtainable from the entire exam.

## Complexity Analysis:
- Time Complexity: O(n) - We process each question exactly once in reverse order
- Space Complexity: O(n) - We maintain a dp array of size n to store intermediate results

## Edge Cases Handled:
- Single question exams (returns that question's points)
- Questions requiring skips beyond exam length
- Zero-point questions
- Large skip counts that might cause index overflow

🚀 Excellent work! You've mastered dynamic programming optimization! Keep solving and leveling up! 💻🔥
'''

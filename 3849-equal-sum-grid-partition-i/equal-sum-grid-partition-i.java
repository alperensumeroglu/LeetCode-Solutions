/*
Clarifying Questions:
1) What are the grid constraints? (→ m * n ≤ 1e5)
2) Can values be negative? (→ No, all are positive)
3) Are we allowed only one cut? (→ Yes, exactly one cut)
4) Can resulting parts be empty? (→ No)
5) Should we check both horizontal and vertical cuts? (→ Yes, either one is enough)

--------------------------------------------------

Example (Manual Walkthrough):
Input: grid = [[1,4],[2,3]]

Step 0 (start):
• total = 1+4+2+3 = 10 → target = 5

Step 1:
• Rule/choice: try horizontal cut
• After operation:
  top = 1+4 = 5
  bottom = 2+3 = 5

Stop condition met because: both parts have equal sum

Answer for example: true

--------------------------------------------------

Edge Cases:
• Already in target state: irrelevant (must make at least one cut)
• Small n cases (n=1, n=2): only horizontal or vertical may be possible
• Negatives / duplicates: no negatives, duplicates don’t matter
• Tie-break scenario: not needed (return on first match)
• Overflow risk (int vs long): sum can be large → use long if needed
• Any tricky case: if total is odd → directly false

--------------------------------------------------

Solution (Approach):

Idea (1-3 sentences):
• Compute total sum
• Set target = total / 2
• Check if any prefix (row-wise or column-wise) equals target

--------------------------------------------------

Data Structure Choice:
• Using: int[] rowSum, int[] colSum
• Because: enables fast prefix sum checks
  (no insert/delete needed, just access)

--------------------------------------------------

Algorithm Steps:
1) Compute total sum
2) If total % 2 != 0 → return false
3) Build rowSum and colSum arrays
4) Check prefix sum over rows
5) Check prefix sum over columns

--------------------------------------------------

Correctness (Why it works):
• Each cut splits the grid into two parts
• If prefix sum equals target, the remaining part is also target
• All possible cuts (horizontal + vertical) are checked

--------------------------------------------------

Complexity:
Time: O(m * n)
Space: O(m + n)

--------------------------------------------------

Implementation Notes:
• Helper methods: not needed
• Tie-break handling: return immediately when found
• Index update pitfalls: don’t cut at last row/column (must be non-empty)
• Other notes: consider using long to avoid overflow
*/
class Solution {
    public boolean canPartitionGrid(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        long total = 0;

        // total sum
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                total += grid[i][j];
            }
        }

        if (total % 2 != 0) return false;

        long target = total / 2;

        long current = 0;
        for (int i = 0; i < m - 1; i++) {
            long rowSum = 0;
            for (int j = 0; j < n; j++) {
                rowSum += grid[i][j];
            }

            current += rowSum;
            if (current == target) return true;
        }

        
        current = 0;
        for (int j = 0; j < n - 1; j++) {
            long colSum = 0;
            for (int i = 0; i < m; i++) {
                colSum += grid[i][j];
            }

            current += colSum;
            if (current == target) return true;
        }

        return false;
    }
}
/*
Clarifying Questions:
1) Can the matrix be empty?
2) Are matrix values guaranteed to be only 0 or 1?
3) Should we return the count of special positions or their coordinates?
4) What are the constraints on m and n?
5) Is a position special only if both the row and column contain exactly one '1'?

Example (Manual Walkthrough):
Input: mat = [[1,0,0],[0,0,1],[1,0,0]]

Step 0 (start):
• Matrix has 3 rows and 3 columns.

Step 1:
• Rule/choice: Count number of 1s in each row and column.
• After operation:
  rowCount = [1,1,1]
  colCount = [2,0,1]

Step 2:
• Rule/choice: Traverse matrix again and check cells with value 1.
• After operation:
  (0,0) -> rowCount=1 but colCount=2 → not special
  (1,2) -> rowCount=1 and colCount=1 → special
  (2,0) -> rowCount=1 but colCount=2 → not special

Stop condition met because: All matrix cells have been checked.

Answer for example: 1

Edge Cases:
• Already in target state: Matrix already has rows and columns with single 1s
• Small n cases (n=1, n=2): Single column matrix where only one row contains 1
• Negatives / duplicates: Not applicable (values only 0 or 1)
• Tie-break scenario: Not applicable
• Overflow risk (int vs long): No overflow risk since matrix size ≤ 100
• Any tricky case: Rows with multiple 1s or columns with multiple 1s invalidate special positions

Solution (Approach):
Idea (1-3 sentences):
• First count how many 1s appear in each row.
• Then count how many 1s appear in each column.
• A position (i,j) is special if mat[i][j] == 1 and both rowCount[i] and colCount[j] equal 1.

Data Structure Choice:
• Using: Two arrays (rowCount and colCount)
• Because: They allow O(1) lookup to check how many 1s exist in a row or column.

Algorithm Steps:
1) Get matrix dimensions m and n.
2) Initialize rowCount[m] and colCount[n].
3) Traverse matrix and count 1s in each row and column.
4) Traverse matrix again and check if mat[i][j] == 1 and rowCount[i] == 1 and colCount[j] == 1.
5) Increment result counter and return it.

Correctness (Why it works):
• A special position requires the only 1 in both its row and column.
• Precomputing row and column counts guarantees constant-time verification.

Complexity:
Time: O(m * n)
Space: O(m + n)

Implementation Notes:
• Helper methods: Not necessary for this problem.
• Tie-break handling: Not applicable.
• Index update pitfalls: Ensure correct indexing when accessing rowCount[i] and colCount[j].
• Other notes: Using two passes over the matrix keeps the logic simple and efficient.
*/

class Solution {
    public int numSpecial(int[][] mat) {
        int m = mat.length;
        int n = mat[0].length;

        int[] rowCount = new int[m];
        int[] colCount = new int[n];

        // First pass: count 1s in rows and columns
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 1) {
                    rowCount[i]++;
                    colCount[j]++;
                }
            }
        }

        int result = 0;

        // Second pass: check special positions
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 1 && rowCount[i] == 1 && colCount[j] == 1) {
                    result++;
                }
            }
        }

        return result;
    }
}
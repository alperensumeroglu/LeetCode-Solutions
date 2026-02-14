class Solution {
    public double champagneTower(int poured, int query_row, int query_glass) {
        double[][] dp = new double[101][101];
        dp[0][0] = poured;

        for(int r = 0; r < 100; r++) {
            for(int c = 0; c <= r; c ++) {
                double overflow = Math.max(0.0, dp[r][c] - 1.0);
                if(overflow > 0) {
                    dp[r+1][c] += overflow / 2.0;
                    dp[r+1][c+1] += overflow / 2.0;
                }
            }
        }
        return Math.min(1.0, dp[query_row][query_glass]);
    }
}
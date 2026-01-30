/*
Clarifying Questions:
1) Can a character be converted using multiple intermediate characters?
   → Yes, unlimited intermediate conversions are allowed.
2) Can the same conversion (original -> changed) appear multiple times with different costs?
   → Yes, we must take the minimum cost.
3) Are characters independent across positions in the string?
   → Yes, each index can be converted independently.
4) What if source[i] == target[i]?
   → No cost is needed for that position.
5) What should be returned if any conversion is impossible?
   → Return -1.

Example (Manual Walkthrough):
Input:
source = "abcd"
target = "acbe"
original = [a,b,c,c,e,d]
changed  = [b,c,b,e,b,e]
cost     = [2,5,5,1,2,20]

Step 0 (start):
•⁠  ⁠We model each character ('a' to 'z') as a node in a graph.
•⁠  ⁠Each given conversion is a directed edge with a cost.

Step 1:
•⁠  ⁠Rule/choice: Build direct conversion costs from input.
•⁠  ⁠After operation: dist[a][b]=2, dist[c][e]=1, dist[e][b]=2, etc.

Step 2:
•⁠  ⁠Rule/choice: Use Floyd–Warshall to find cheaper paths via intermediate characters.
•⁠  ⁠After operation: dist[c][b] becomes 3 via c -> e -> b (1 + 2).

Stop condition met because:
•⁠  ⁠All character-to-character minimum costs are computed.

Answer for example:
•⁠  ⁠Total cost = 0 (a->a) + 5 (b->c) + 3 (c->b) + 20 (d->e) = 28

Edge Cases:
•⁠  ⁠Already in target state: cost is 0 for that index.
•⁠  ⁠Small n cases (n=1, n=2): handled normally, still per-character.
•⁠  ⁠Negatives / duplicates: duplicates allowed; we take minimum cost.
•⁠  ⁠Tie-break scenario: irrelevant since we minimize cost only.
•⁠  ⁠Overflow risk (int vs long): costs can accumulate, so long is required.
•⁠  ⁠Any tricky case: conversion chain exists but direct conversion does not.

Solution (Approach):
Idea (1-3 sentences):
•⁠  ⁠Treat characters as nodes in a directed weighted graph.
•⁠  ⁠Compute all-pairs shortest paths between characters.
•⁠  ⁠Sum the minimum conversion cost for each character position.

Data Structure Choice:
•⁠  ⁠Using: 2D array dist[26][26]
•⁠  ⁠Because: constant alphabet size allows fast access and updates.

Algorithm Steps:
1) Initialize dist matrix with MAX_VALUE, dist[i][i] = 0.
2) Fill direct conversions from original -> changed with minimum cost.
3) Run Floyd–Warshall on 26 characters.
4) For each index i, add dist[source[i]][target[i]] to answer.
5) If any required conversion is impossible, return -1.

Correctness (Why it works):
•⁠  ⁠Floyd–Warshall guarantees the minimum cost between any two characters.
•⁠  ⁠Since positions are independent, summing per-character minimum costs is optimal.

Complexity:
Time: O(26^3 + n) ≈ O(n)
Space: O(26^2)

Implementation Notes:
•⁠  ⁠Helper methods: none needed.
•⁠  ⁠Tie-break handling: not applicable.
•⁠  ⁠Index update pitfalls: careful char-to-index conversion using (c - 'a').
•⁠  ⁠Other notes: use Long.MAX_VALUE to represent unreachable states safely.
*/
import java.util.*;

class Solution {
    public long minimumCost(String source, String target,
                            char[] original, char[] changed, int[] cost) {

        int n = source.length();

        // dist[x][y] = x harfinden y harfine en ucuz dönüşüm maliyeti
        long[][] dist = new long[26][26];

        // 1) Başlangıç: her şey imkânsız (Long.MAX_VALUE), aynı harf -> 0
        for (int i = 0; i < 26; i++) {
            Arrays.fill(dist[i], Long.MAX_VALUE);
            dist[i][i] = 0;
        }

        // 2) Direkt dönüşümleri ekle (aynı dönüşüm birden fazla olabilir -> min al)
        for (int i = 0; i < cost.length; i++) {
            int from = original[i] - 'a';
            int to   = changed[i] - 'a';
            dist[from][to] = Math.min(dist[from][to], (long) cost[i]);
        }

        // 3) Floyd–Warshall: tüm harf çiftleri için en ucuz maliyet
        for (int mid = 0; mid < 26; mid++) {
            for (int i = 0; i < 26; i++) {
                if (dist[i][mid] == Long.MAX_VALUE) continue;
                for (int j = 0; j < 26; j++) {
                    if (dist[mid][j] == Long.MAX_VALUE) continue;

                    long newCost = dist[i][mid] + dist[mid][j];
                    if (newCost < dist[i][j]) dist[i][j] = newCost;
                }
            }
        }

        // 4) Source -> Target maliyetini pozisyon pozisyon topla
        long ans = 0;
        for (int i = 0; i < n; i++) {
            char s = source.charAt(i);
            char t = target.charAt(i);

            if (s == t) continue;

            long d = dist[s - 'a'][t - 'a'];
            if (d == Long.MAX_VALUE) return -1;

            ans += d;
        }

        return ans;
    }
}

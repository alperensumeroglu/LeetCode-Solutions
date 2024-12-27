class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_value = -1
        i_value = values[0]
        
        for j in range(1, len(values)):
            j_value = values[j] - j
            max_value = max(max_value, j_value + i_value)
            i_value = max(i_value, values[j] + j)
        
        return max_value

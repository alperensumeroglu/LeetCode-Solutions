class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_expected = n * (n + 1) // 2  
        sum_actual = sum(nums)        
        return sum_expected - sum_actual  

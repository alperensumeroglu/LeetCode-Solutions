class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        prefix = [0] * len(nums)
        for i in range(1, len(nums)):
            same = nums[i-1] % 2 == nums[i] % 2
            prefix[i] = prefix[i-1]
            if same: prefix[i] += 1

        res = []
        for x, y in queries:
            res.append(prefix[x] == prefix[y])
        return res
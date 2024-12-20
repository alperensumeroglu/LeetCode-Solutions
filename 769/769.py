class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        N = len(arr)
        prefix = [0] * N
        
        for index, x in enumerate(arr):
            if x != index:
                prefix[min(x, index)] += 1
                prefix[max(x, index)] -= 1
        
        chunks = 0
        current = 0
        
        for x in prefix:
            current += x
            if current == 0:
                chunks += 1
        
        return chunks
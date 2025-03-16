class Solution:
    def repairCars(self, ranks, cars):
        """
        Finds the minimum time required to repair all cars given the mechanics' ranks.
        """
        
        # Helper function to check if a given time limit is sufficient to repair all cars
        def can_repaired(time):
            total_cars_repaired = 0
            for rank in ranks:
                total_cars_repaired += int((time / rank) ** 0.5)  # Each mechanic repairs sqrt(time / rank) cars
            return total_cars_repaired >= cars
        
        # Binary search boundaries
        left, right = 1, min(ranks) * cars * cars  # Upper bound is worst-case scenario
        
        # Perform binary search on time
        while left <= right:
            mid = (left + right) // 2  # Middle point as a potential minimum time
            if can_repaired(mid):
                right = mid - 1  # Try to find a smaller valid time
            else:
                left = mid + 1  # Increase time as current is insufficient
        
        return left  # The smallest valid time found

    """
    Intuition:
    - Each mechanic repairs cars at a speed determined by their rank.
    - A mechanic with rank `r` needs `r * n^2` minutes to repair `n` cars.
    - The goal is to find the minimum time required for all mechanics, working in parallel, to repair `cars` cars.
    
    Approach:
    - Use binary search on the possible time range (1 to `min(ranks) * cars^2`).
    - For each midpoint, check if all cars can be repaired using a helper function.
    - The helper function iterates through mechanics and calculates the maximum number of cars each can repair in the given time.
    - If the total is enough, decrease the search space; otherwise, increase it.
    
    Complexity:
    - Let `N` be the number of mechanics and `M` be `min(ranks) * cars^2` (upper bound on time).
    - Binary search operates in O(log M) time.
    - Each iteration of binary search calls `can_repaired`, which runs in O(N).
    - Thus, the overall time complexity is O(N log M).
    - Space complexity: O(1) since only a few extra variables are used.
    """

# 🚀🔥 Keep coding and stay awesome!
class Solution:
    def mincostTickets(self, travel_days: List[int], ticket_costs: List[int]) -> int:
        # Dynamic programming array to store minimum costs
        min_cost = [0] * (travel_days[-1] + 1)
        travel_set = set(travel_days)

        for day in range(1, travel_days[-1] + 1):
            # If it's not a travel day, cost is the same as the previous day
            if day not in travel_set:
                min_cost[day] = min_cost[day - 1]
            else:
                # Calculate minimum cost for 1-day, 7-day, and 30-day passes
                min_cost[day] = min(
                    min_cost[day - 1] + ticket_costs[0],  # 1-day pass
                    min_cost[max(day - 7, 0)] + ticket_costs[1],  # 7-day pass
                    min_cost[max(day - 30, 0)] + ticket_costs[2]  # 30-day pass
                )

        return min_cost[-1]

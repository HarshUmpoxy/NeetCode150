# We are allowed at most k stops, which means at most k + 1 flights (edges).
# Bellman–Ford is perfect here because it relaxes edges level by level, where each iteration allows one more edge in the path.

# Key idea:
# After i iterations, we know the cheapest cost to reach every city using at most i flights.
# By running the relaxation k + 1 times, we ensure we only consider paths that respect the stop limit.
# We use a temporary array each iteration so that paths from the same iteration don't chain together and accidentally exceed the allowed number of flights.


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Bellman Ford Algorithm
        prices = [float("inf")]*n
        prices[src] = 0

        for i in range(k+1): # iterating k times for k stops exactly till destination
            tmpPrices = prices.copy()

            for s, d, p in flights:
                if prices[s]==float("inf"):
                    continue
                if prices[s]+p<tmpPrices[d]:
                    tmpPrices[d]=p+prices[s]
            prices = tmpPrices
        
        return -1 if prices[dst] == float("inf") else prices[dst]
# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

# Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.

# Solution:
# If the total gas is sufficient, then there must be exactly one valid starting station.

# The greedy idea is to scan the stations from left to right while keeping track of the current tank balance.

# If at some index the tank becomes negative, it means we cannot start from any station between the previous start and this index, because they would all run out of gas at the same point.
# So we reset the tank and try the next station as a new starting point.


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n, total, curr, ans = len(gas), 0, 0, 0

        for i in range(n):
            total = total + (gas[i]-cost[i])
            curr = curr + gas[i]-cost[i]
            if curr < 0:
                curr = 0
                ans = i+1
        if total >= 0:
            return ans
        return -1
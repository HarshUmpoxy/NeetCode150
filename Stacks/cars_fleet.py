# Solution:
# No need to simulate as it will be complex, just think greedy
# Sort the array based on (position, speed)
# Store the time traversing from the back of array
# If the time is greater than the current max, increment the ans and update the current max

# Bonus: Ask LLM model for hints and problem intuition building

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        n = len(position)
        for i in range(n):
            arr.append((position[i], speed[i]))
        
        arr.sort()

        def time(pos, speed, target):
            return (target-pos)/speed
        
        ans = 0
        curr_max = float("-inf")
        for i in range(n-1, -1, -1):
            curr_time = time(arr[i][0], arr[i][1], target)
            if curr_time > curr_max:
                ans +=1
                curr_max = curr_time
        
        return ans
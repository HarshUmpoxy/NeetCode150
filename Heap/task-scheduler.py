# Revise Must:
# Solution - 1:
# Use max heap to always process the most frequent task first
# Use queue to store the most frequent task and its remaining count (this enforces the cooldown)
# Use time to store the current time
# If the current time is greater than the time stored in q, pop the most frequent task from q and push it back into the max heap
# Return the time

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-i for i in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque() # element number, time
        while q or maxHeap:
            time +=1
            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time

# Solution - 2
# Maths and Greedy
# The task with the highest frequency determines the minimum needed structure of the schedule.
# If a task appears maxf times, these copies must be at least n units apart.
# This creates (maxf - 1) "gaps", and each gap must have a length of (n + 1) slots (the task itself + n cooldowns).
# If multiple tasks share this maximum frequency (maxCount tasks), they all occupy the final row of the structure.
# So the minimal time required to schedule all tasks without violating cooldown rules is: time = (maxf - 1) * (n + 1) + maxCount
# However, if the number of tasks is larger than this calculated time, then simply performing all tasks takes longer.
# Thus, the actual answer must be: max(len(tasks), time)

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1

        maxf = max(count)
        maxCount = 0
        for i in count:
            maxCount += 1 if i == maxf else 0

        time = (maxf - 1) * (n + 1) + maxCount
        return max(len(tasks), time)
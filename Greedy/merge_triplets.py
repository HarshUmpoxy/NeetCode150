# Observation is that any triplet with a value greater than the target cannot be a part of the answer
# Also, we can take max of the remaining triplets to form the answer

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        n = len(triplets)
        ans = [0, 0, 0]
        for i, (x,y,z) in enumerate(triplets):
            if x>target[0] or y>target[1] or z>target[2]:
                continue
            ans = [max(x, ans[0]), max(y, ans[1]), max(z, ans[2])]
        if ans == target:
            return True
        
        return False

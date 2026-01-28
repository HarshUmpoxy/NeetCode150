class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        arr = []
        for i in range(n-2): # Memory Leak check
            if i > 0 and nums[i] == nums[i - 1]: # i duplicate check
                continue
            l = i+1; r = n-1
            while l<r:
                sum = nums[i]+nums[l]+nums[r]
                if sum == 0:
                    arr.append([nums[i], nums[l], nums[r]])
                    l+=1; r-=1 # Imp Now, avoid duplicates and move
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif sum>0:
                    r-=1
                else:
                    l+=1
        return arr
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashMap = {}
        for i, x in enumerate(nums):
            if target - x in hashMap:
                return [hashMap[target-x], i]
            hashMap[x] = i
        

S = Solution()
print(S.twoSum([2,7,11,15], 9))
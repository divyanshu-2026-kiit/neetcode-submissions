class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = dict()
        for i in range(len(nums)):
            r = target - nums[i]
            if r in result:
                return [result[r],i]
            result[nums[i]] = i

                
        
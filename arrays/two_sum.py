class Solution(object):
    def twoSum(self, nums, target):
        hashMap = {}

        for idx, num in enumerate(nums):
            complement = target - num

            if complement in hashMap:
                return [hashMap[complement], idx]
            hashMap[num] = idx


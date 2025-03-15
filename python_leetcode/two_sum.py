from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for index in range(len(nums)):
            complement = target - nums[index]
            if complement in num_dict:
                return [num_dict[complement], index]
            num_dict[nums[index]] = index

        return None

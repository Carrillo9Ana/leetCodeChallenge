''' 
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]. 

'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # set an array where to store the expected value
        ls = []
        # loop thru the given nums 
        for i in range(0, len(nums)):
            # subtract the number that is at the index from the target 
            item = target - nums[i]
            nums[i] = "done"
            # if the item is in the list of nums, append the index to the new list
            if item in nums:
                ls.append(i)
                # index() method that looks for the least number and returns its index
                ls.append(nums.index(item))
                return ls
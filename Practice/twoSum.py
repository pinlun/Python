#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tmpnums = nums.copy()
        tmp = [(x-target)*-1 for x in nums]
        for i in range(len(tmp)):
            nums = tmpnums.copy()
            nums[i]= target
            if tmp[i] in nums:
                tmp_index = [i, nums.index(tmp[i])]
        tmp_index.sort()
        return tmp_index

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        newi = 0
        i = 0
        while i < len(nums):
            if nums[i]:
                nums[newi], nums[i] = nums[i], nums[newi]
                newi = newi + 1
            i = i + 1
        

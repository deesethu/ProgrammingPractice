class Solution:
    def twoSum(self, nums, k):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mydict = {}
        
        for i in range(len(nums)):
            t = k - nums[i]  
            if t in mydict and i != mydict[t]:
                if i > mydict[t]:
                    return [mydict[t], i]
                else:
                    return [i, mydict[t]]
            else:
                mydict[nums[i]] = i
        
        return []

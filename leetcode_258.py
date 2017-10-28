class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        k = num % 9
        if k == 0:
            return 9
        return k
        

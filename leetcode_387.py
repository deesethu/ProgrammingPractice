class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        mydict = {}
        for t in s:
            if t in mydict:
                mydict[t] = mydict[t] + 1
            else:
                mydict[t] = 1
        
        print mydict
        for m in range(len(s)):
            if mydict[s[m]] == 1:
                return m
                
        
        return -1
        

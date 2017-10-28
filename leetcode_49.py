class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        myd = {}
        for st in strs:
            ke = ''.join(sorted(st))
            if myd.has_key(ke): 
                myd[ke].append(st)
            else:
                myd[ke] = [st]
        
            
        return list(myd.values())

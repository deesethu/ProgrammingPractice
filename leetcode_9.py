class Solution(object):
    
    """def isPalindrome3(self, x):
        if str(x) == str(x)[::-1]:
            return True
        return False
    
    def isPalindrome2(self, x):
        rev, y = 0, x
        if x < 0:
            return False
        while x:
            rev = (rev * 10) + (x % 10)
            x = x/10
        if rev == y:
            return True
        return False
       """
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x == 0: 
            return True
        t = int(math.log10(x))
    
        while (t > 0):
            
            r = int(x /(10 ** t)) % 10
            s = x % 10 
            if r != s:
                return False
            x = x - (r * (10 ** (t)))
            x = x / 10
            t = t - 2


        if not x/10:
            return True
        else:
            return False
